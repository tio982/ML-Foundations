# Credit Risk Scoring (Fintech)

## Business Goal
Predict the probability of default so a lender can reduce expected loss while
maintaining a healthy approval rate.

## Success Metrics (Business + ML)
- **Expected loss** reduction at a fixed approval rate.
- **Precision/Recall** at an operating threshold that reflects business cost.
- **ROC‑AUC / PR‑AUC** for overall model discrimination.
- **Calibration error** to ensure probabilities are decision‑ready.

## Dataset (Lending Club, open source)
We will use the open Lending Club sample from OpenIntro:
- Source: https://www.openintro.org/data/index.php?data=loans_full_schema
- Download: `data/raw/loans_full_schema.csv`
- Notes: Open dataset suitable for public GitHub portfolios.

## Planned Deliverables
- Reproducible training pipeline
- Model card with fairness and calibration checks
- Threshold analysis with cost‑based decisioning
- Batch scoring or API inference stub

## Project Structure (to be created)
- `src/` – data prep, features, training, inference
- `notebooks/` – exploration and prototyping
- `data/` – raw/interim/processed
- `models/` – trained artifacts
- `reports/` – charts, metrics, and write‑ups
- `tests/` – unit tests and data checks
- `configs/` – config files for reproducible runs
