
import numpy as np

def validate_hypotheses(hypotheses, daily_df, campaign_df):
    results = []
    for h in hypotheses:
        if h['id']=='h1':
            recent = daily_df.tail(7)['ctr'].mean() if len(daily_df)>=7 else daily_df['ctr'].iloc[-1]
            prev = daily_df.tail(14).head(7)['ctr'].mean() if len(daily_df)>=14 else daily_df['ctr'].iloc[0]
            validated = (recent < prev*0.9)
            score = float(min(1.0, max(0.0, (prev-recent)/(prev+1e-9))))
            results.append({'id':h['id'],'validated':bool(validated),'score':score,'details':{'recent_ctr':float(recent),'previous_ctr':float(prev)}})
        elif h['id']=='h2':
            # quick spend vs roas check
            spend_growth = daily_df.tail(7)['spend'].sum() / (daily_df.tail(14).head(7)['spend'].sum()+1e-9) - 1 if len(daily_df)>=14 else 0
            roas_recent = daily_df.tail(7)['roas'].mean() if 'roas' in daily_df.columns else None
            validated = (spend_growth>0.05 and roas_recent and roas_recent < 1.0)
            score = float(min(1.0, abs(spend_growth)))
            results.append({'id':h['id'],'validated':bool(validated),'score':score,'details':{'spend_growth':float(spend_growth),'roas_recent':float(roas_recent) if roas_recent is not None else None}})
        else:
            results.append({'id':h['id'],'validated':False,'score':0.2,'details':{}})
    return results
