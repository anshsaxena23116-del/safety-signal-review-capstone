# Safety Signal Review Capstone

**Project type:** Pharmacovigilance / Drug Safety  
**Milestone:** 5 of 5 — Aggregate Safety Review  
**Status:** Training/sample analysis

## Objective
Review a small aggregate adverse-reaction dataset, summarize report counts and outcomes, prioritize a potential safety concern for follow-up, consider alternative explanations, and recommend further evidence collection.

## Repository contents
- `data/adverse_drug_reactions_sample.csv` — supplied sample dataset.
- `reports/Safety_Signal_Review_Capstone.pdf` — completed briefing report.
- `src/analyze_dataset.py` — reproducible summary script.
- `requirements.txt` — Python dependency.

## Key findings from this sample
- 8 reports in total.
- 3 reports have the outcome recorded as `Hospitalized`.
- 1 report is marked `Life-Threatening`.
- The highest-priority individual case for follow-up is the warfarin / uncontrolled hemorrhage report (ADR-9007), based on the recorded severity and outcome.
- The dataset has one report per distinct drug–reaction combination, and lacks report dates and exposure denominators. Therefore, it cannot establish a recurring aggregate signal, incidence, or causality.

## How to reproduce the summary
Install Python 3 and run:

```bash
pip install -r requirements.txt
python src/analyze_dataset.py
```

The script prints summary counts from the CSV. It does not diagnose patients or determine causality.

## Limitations
This is a small training dataset. Spontaneous/sample report counts are not incidence rates and cannot by themselves establish that a drug caused an event. Clinical narratives, relevant history, concomitant medicines, verified outcomes, report dates, duplicate checks, product reference safety information, and exposure denominators may be needed for a fuller assessment.

**Training use only — not for clinical decision-making or as a real-patient safety assessment or regulatory submission.**
