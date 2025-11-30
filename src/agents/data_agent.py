
import pandas as pd
from collections import defaultdict

def load_and_summarize(path, sample_n=3):
    df = pd.read_csv(path, parse_dates=['date'])
    df = df.sort_values('date')
    sample = df.head(sample_n).to_dict(orient='records')
    summary = {
        'rows': int(len(df)),
        'date_range': [str(df['date'].min().date()), str(df['date'].max().date())],
        'unique_campaigns': int(df['campaign_name'].nunique()),
    }
    # daily aggregates
    daily = df.groupby('date').agg({'spend':'sum','impressions':'sum','clicks':'sum','revenue':'sum'}).reset_index()
    daily['ctr'] = daily['clicks'] / daily['impressions']
    daily['roas'] = daily['revenue'] / daily['spend']
    campaign = df.groupby('campaign_name').agg({'spend':'sum','impressions':'sum','clicks':'sum','revenue':'sum'}).reset_index()
    campaign['ctr'] = campaign['clicks'] / campaign['impressions']
    campaign['roas'] = campaign['revenue'] / campaign['spend']
    return {'sample': sample, 'summary': summary, 'daily': daily, 'campaign': campaign}
