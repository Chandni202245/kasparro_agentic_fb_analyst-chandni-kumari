
import os, json, argparse
from src.agents import planner_agent, data_agent, insight_agent, evaluator_agent, creative_agent
from src.utils import logger

def main(user_query, config):
    # 1. Plan
    plan = planner_agent.plan(user_query)
    # 2. Load data
    data = data_agent.load_and_summarize(config['data_path'])
    # Prepare simple recent pct estimators
    daily = data['daily']
    if 'ctr' not in daily.columns:
        daily['ctr'] = daily['clicks'] / daily['impressions']
    if 'roas' not in daily.columns:
        daily['roas'] = daily['revenue'] / daily['spend']
    recent_pct = {'ctr': (daily.tail(7)['ctr'].mean() - daily.tail(14).head(7)['ctr'].mean())/ (daily.tail(14).head(7)['ctr'].mean()+1e-9) if len(daily)>=14 else 0,
                  'spend_growth': (daily.tail(7)['spend'].sum() / (daily.tail(14).head(7)['spend'].sum()+1e-9) - 1) if len(daily)>=14 else 0,
                  'roas': (daily.tail(7)['roas'].mean() - daily.tail(14).head(7)['roas'].mean())/(daily.tail(14).head(7)['roas'].mean()+1e-9) if len(daily)>=14 else 0}
    # 3. Hypotheses
    campaign_df = data['campaign']
    hypos = insight_agent.generate_hypotheses(data['summary'], campaign_df, recent_pct)
    # 4. Validate
    val = evaluator_agent.validate_hypotheses(hypos, data['daily'], campaign_df)
    # 5. Creative generation for low CTR campaigns
    ctr_median = campaign_df['ctr'].median()
    low_ctr = campaign_df[campaign_df['ctr'] < 0.8 * ctr_median]['campaign_name'].tolist()
    creatives = {}
    common_words = []
    # collect common words rudimentarily
    for c in low_ctr:
        sample_msgs = [] # placeholder - real impl should read sample messages
        creatives[c] = creative_agent.generate_for_campaign(c, sample_msgs, common_words)
    out = {'plan':plan,'summary':data['summary'],'hypos':hypos,'validation':val,'creatives':creatives}
    # write outputs
    os.makedirs(config['output_path'], exist_ok=True)
    with open(os.path.join(config['output_path'],'insights.json'),'w') as f:
        json.dump(hypos,f,indent=2)
    with open(os.path.join(config['output_path'],'creatives.json'),'w') as f:
        json.dump(creatives,f,indent=2)
    logger.write_log(os.path.join('logs','run_log.json'), out)
    print('Run complete. Outputs written to', config['output_path'])

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('query', nargs='?', default='Analyze ROAS drop')
    parser.add_argument('--config', default='config/config.yaml')
    args = parser.parse_args()
    import yaml
    with open(args.config) as f:
        cfg = yaml.safe_load(f)
    main(args.query, cfg)
