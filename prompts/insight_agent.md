Insight Agent Prompt Template
- Input: data summaries from Data Agent
- Process: Generate 3-6 hypotheses explaining ROAS/CTR changes. For each hypothesis include:
  - hypothesis (string)
  - supporting_evidence (list)
  - expected_data_checks (list of checks to run)
- Output: JSON array of hypotheses with initial confidence (0-1)
Include reflection: if low confidence, propose extra analysis steps.
