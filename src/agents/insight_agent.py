
def generate_hypotheses(data_summary, campaign_stats, recent_pct):
    hypos = []
    # Simple rule: large CTR drop
    if recent_pct.get('ctr',0) < -0.1:
        hypos.append({'id':'h1','hypothesis':'Creative underperformance causing CTR drop','confidence':0.6,'evidence':['recent_ctr_drop']})
    # spend vs roas mismatch
    if recent_pct.get('spend_growth',0) > 0.05 and recent_pct.get('roas',0) < -0.1:
        hypos.append({'id':'h2','hypothesis':'Increased spend but falling ROAS — audience mismatch or creative fatigue','confidence':0.65,'evidence':['spend_up_roas_down']})
    # platform drift placeholder
    hypos.append({'id':'h3','hypothesis':'No strong signal — recommend segmentation and A/B tests','confidence':0.4,'evidence':['fallback']})
    return hypos
