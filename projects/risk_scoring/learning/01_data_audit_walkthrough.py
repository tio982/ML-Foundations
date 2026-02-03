"""
Step 1: Data audit (walkthrough script)

This script is intentionally verbose and commented for learning.
Run it with:
    python learning/01_data_audit_walkthrough.py
"""

from pathlib import Path

import pandas as pd


# ---------- Step 0: Define paths (single source of truth) ----------
# Why: using Path avoids OS-specific issues and keeps paths readable.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "loans_full_schema.csv"


def main() -> None:
    # ---------- Step 1: Load data ----------
    # We read the CSV directly into a pandas DataFrame.
    # pandas is efficient for tabular data and gives us quick profiling tools.
    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(
            f"Missing dataset at {RAW_DATA_PATH}. "
            "Download it from https://www.openintro.org/data/csv/loans_full_schema.csv"
        )

    # low_memory=False keeps pandas from guessing mixed dtypes in chunks.
    # This makes type inference more reliable for audit work.
    df = pd.read_csv(RAW_DATA_PATH, low_memory=False)

    # ---------- Step 2: Basic shape + sample ----------
    # This tells us how many rows/columns we have, and a quick look at values.
    print("\n=== BASIC SHAPE ===")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Cols: {df.shape[1]:,}")

    print("\n=== SAMPLE (first 5 rows) ===")
    print(df.head())

    # ---------- Step 3: Column types ----------
    # Knowing types helps us decide preprocessing steps (numeric vs categorical).
    print("\n=== COLUMN TYPES ===")
    print(df.dtypes.sort_values())

    # ---------- Step 4: Missing values ----------
    # Missingness impacts model choice and imputation strategy.
    missing_pct = (df.isna().mean() * 100).sort_values(ascending=False)
    print("\n=== MISSING VALUE % (top 15) ===")
    print(missing_pct.head(15))

    # ---------- Step 5: Target exploration ----------
    # For credit risk, a typical target is loan_status.
    # We inspect distribution before defining a label.
    if "loan_status" in df.columns:
        print("\n=== LOAN STATUS DISTRIBUTION ===")
        print(df["loan_status"].value_counts(dropna=False))
    else:
        print("\n[WARN] 'loan_status' column not found. We will choose another target.")

    # ---------- Step 6: Potential leakage flags ----------
    # These columns often contain information *after* the loan decision
    # (payments, balances), which would leak future outcomes into training.
    leakage_candidates = [
        "paid_total",
        "paid_principal",
        "paid_interest",
        "paid_late_fees",
        "balance",
    ]

    present_leakage = [col for col in leakage_candidates if col in df.columns]
    print("\n=== LEAKAGE CANDIDATES PRESENT ===")
    print(present_leakage if present_leakage else "None found")

    # ---------- Step 7: Save a simple audit report ----------
    # We keep a small CSV summary so later steps can reference it.
    report_path = PROJECT_ROOT / "reports" / "data_audit_summary.csv"
    audit_df = pd.DataFrame(
        {
            "column": df.columns,
            "dtype": df.dtypes.astype(str),
            "missing_pct": (df.isna().mean() * 100).round(2).values,
        }
    ).sort_values("missing_pct", ascending=False)
    audit_df.to_csv(report_path, index=False)
    print(f"\nSaved audit summary to: {report_path}")


if __name__ == "__main__":
    main()
