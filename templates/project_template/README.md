# Project Template

This template is the standard structure for every ML project in this repo.
It keeps data, code, experiments, and reports organized and easy to explain.

## Folder Guide
- `src/` – production‑style code (data prep, features, training, inference)
- `notebooks/` – exploration and prototyping
- `data/`
  - `raw/` – untouched source data
  - `interim/` – cleaned but not feature‑ready
  - `processed/` – feature‑ready datasets
- `models/` – saved model artifacts
- `reports/` – figures, charts, and written summaries
- `tests/` – unit tests and quality checks
- `configs/` – config files for reproducible runs

## How to Start a New Project
1. Copy this folder into `projects/<project_name>/`.
2. Rename the project README with the business problem and success metrics.
3. Build in small, documented steps so decisions are easy to follow.
