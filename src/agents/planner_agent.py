
def plan(user_query):
    tasks = [
        {'id':'load_data','desc':'Load dataset and produce summary'},
        {'id':'trend_analysis','desc':'Compute CTR/ROAS trends'},
        {'id':'generate_hypotheses','desc':'Create hypotheses for ROAS/CTR changes'},
        {'id':'validate','desc':'Run evaluator checks'},
        {'id':'creative_generation','desc':'Produce creatives for low-CTR campaigns'}
    ]
    return {'tasks': tasks, 'query': user_query}
