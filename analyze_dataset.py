import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "adverse_drug_reactions_sample.csv"

def main():
    df = pd.read_csv(DATA)
    print("SAFETY SIGNAL REVIEW — DATA SUMMARY")
    print(f"Total reports: {len(df)}")
    print("\nSeverity counts:")
    print(df["Severity"].value_counts(dropna=False).to_string())
    print("\nOutcome counts:")
    print(df["Outcome"].value_counts(dropna=False).to_string())
    print("\nReporter type counts:")
    print(df["ReporterType"].value_counts(dropna=False).to_string())
    print("\nCase listing:")
    cols = ["ReportID", "SuspectedDrug", "AdverseReaction", "ReactionOnsetDays", "Severity", "Outcome"]
    print(df[cols].to_string(index=False))
    print("\nCaution: descriptive counts only; not incidence or proof of causality.")

if __name__ == "__main__":
    main()
