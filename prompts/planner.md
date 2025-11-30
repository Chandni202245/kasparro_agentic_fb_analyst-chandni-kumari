Planner Agent Prompt Template (structured)
- Input: user_query (string), high-level instructions
- Task: Decompose into ordered subtasks with short explanation and output as JSON list
- Output format (JSON):
{
  "tasks": [
    {"id": "load_data", "desc":"Load dataset summary", "params":{}},
    {"id": "trend_analysis", "desc":"Compute CTR/ROAS trends by date/campaign", "params":{}},
    {"id": "generate_hypotheses", "desc":"Produce candidate hypotheses", "params":{}},
    {"id": "validate", "desc":"Run quantitative validation checks", "params":{}},
    {"id": "creative_generation", "desc":"Produce creatives for low-CTR campaigns", "params":{}}
  ]
}
Use Think → Analyze → Conclude sections when reasoning.
