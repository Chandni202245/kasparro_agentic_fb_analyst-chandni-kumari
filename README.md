# Kasparro Agentic FB Analyst – Chandni Kumari

This repository contains my complete submission for the **Kasparro Applied AI Engineer Assignment (Agentic Facebook Performance Analyst)**.
The project implements a modular, agentic workflow that analyzes Meta Ads performance data and generates insights, recommendations, and ad creatives.

---


### 1. Create virtual environment and install dependencies

```
python -m venv .venv
.\.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 2. Run the agentic orchestrator

```
python -m src.orchestrator.run "Analyze ROAS drop" --config config/config.yaml
```

This generates:

* `reports/insights.json`
* `reports/creatives.json`
* `reports/report.md`
* `logs/run_log.json`

---

## 📁 Project Structure

```
src/
  ├─ agents/            # Planner, Data, Insight, Evaluator, Creative agents  
  ├─ orchestrator/      # Main agent pipeline  
  ├─ utils/             # Helper functions  
config/config.yaml       # Persona, thresholds, paths  
data/synthetic_fb_ads_undergarments.csv   # Provided dataset  
prompts/                # Prompt templates for each agent  
reports/                # Generated insights + creatives + final report  
logs/                   # Execution logs  
tests/                  # Unit tests  
```

---

##  Agent Workflow Overview

### 1. **Planner Agent**

Breaks down the user query into structured analytical steps.

### 2. **Data Agent**

Loads and analyzes Facebook (Meta) Ads dataset:

* spend, impressions, clicks, CTR
* purchases, revenue, ROAS
* audience, creative_type, creative_message

### 3. **Insight Agent**

Generates data-driven insights such as:

* ROAS drop causes
* CPC/CPM/CTR patterns
* creative fatigue signals
* audience performance shifts

### 4. **Evaluator Agent**

Validates insights and removes weak or unsupported conclusions.

### 5. **Creative Agent**

Produces:

* hooks
* headlines
* primary text
* descriptions
* creative variations

---

##  Reproducibility

To reproduce the final outputs:

```
python -m src.orchestrator.run "Analyze ROAS drop" --config config/config.yaml
```

---

##  Release & Pull Request (submitted to Kasparro)

* Release Tag: **v1.0**
* Pull Request: **self-review**

---

##  Notes

* Dataset is synthetic and meant for evaluation only.
* Agents are modular and can be extended with LLM reasoning or Langfuse instrumentation.
* Outputs are fully reproducible using the command above.

---

##  Submission Completed

This repository represents my final submission for the Kasparro Agentic FB Analyst assignment.
