# kasparro-agentic-fb-analyst-yourname

This repository is a seeded implementation for the Kasparro Applied AI Engineer assignment (Agentic Facebook Performance Analyst).
The original task PDF and assignment instructions were provided by the user. See `data/sample_fb_dataset.csv` for the sample dataset.

## Quick start
1. Create virtualenv and install deps:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run the orchestrator (sample run):
   ```bash
   make run
   ```
   or directly:
   ```bash
   python src/orchestrator/run.py "Analyze ROAS drop" --config config/config.yaml
   ```

## Files & Structure
- `src/agents/` - Planner, Data, Insight, Evaluator, Creative agents (light implementations)
- `src/orchestrator/run.py` - Orchestration entrypoint
- `prompts/` - Prompt templates for each agent (planner, data, insight, evaluator, creative)
- `config/config.yaml` - thresholds and paths
- `data/sample_fb_dataset.csv` - provided sample dataset
- `reports/` - outputs: insights.json, creatives.json, report.md
- `logs/` - execution logs
- `tests/` - unit tests

## Reproducing outputs & git hygiene (for submission)
1. Initialize git repo, commit changes, create v1.0 tag:
   ```bash
   git init
   git add .
   git commit -m "feat: initial agentic fb-analyst scaffold"
   git commit -m "chore: add sample data and run outputs" || true
   git tag v1.0
   ```
2. Create a self-review PR title and description (example):
   - Title: `self-review`
   - Description: explain architecture choices: Planner→Data→Insight→Evaluator→Creative; discuss validations performed; note limits (synthetic sample, rule-based checks), and how to extend with LLM prompts and Langfuse traces.

3. Provide final submission link and evidence in the PR description:
   - Commit hash: `$(git rev-parse HEAD)`
   - Release tag: `v1.0`
   - Command used: `make run`

## Notes & next steps
- This scaffold focuses on reasoning, prompt templates, and reproducibility. Replace the simple rule-based parts with LLM-backed prompts in `prompts/` when ready.
- Seed randomness and pin versions in `requirements.txt` for reproducibility.

---
Generated on 2025-11-28 06:12:12Z
