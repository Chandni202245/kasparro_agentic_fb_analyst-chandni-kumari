Evaluator Agent Prompt Template
- Input: hypothesis + data summaries
- Run quantitative checks (e.g., percent changes, t-tests, cohort comparisons)
- Output: validation results: {hypothesis_id, validated: true/false, p_score:0-1, evidence_details}
Include retry logic: if evidence weak, request additional segmentation.
