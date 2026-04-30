"""Dataset collection and normalization utilities.

This script prepares a combined dataset for the ENG 685 hybrid scam detection
project using SMS spam, SMS phishing/smishing, and email phishing datasets.

Expected final format
---------------------
text,label,source

Labels are normalized to:
- scam
- legitimate
"""

from __future__ import annotations

import argparse
import io
import zipfile
from pathlib import Path

import pandas as pd
import requests


UCI_SMS_SPAM_URL = (
    "https://archive.ics.uci.edu/static/public/228/"
    "sms+spam+collection.zip"
)


def ensure_directory(path: Path) -> None:
    """Create a directory if it does not already exist.

    Parameters
    ----------
    path : Path
        Directory path to create.
    """
    path.mkdir(parents=True, exist_ok=True)


def download_uci_sms_spam(output_path: Path) -> pd.DataFrame:
    """Download and normalize the UCI SMS Spam Collection dataset.

    Parameters
    ----------
    output_path : Path
        Destination CSV file path.

    Returns
    -------
    pandas.DataFrame
        Normalized dataset with text, label, and source columns.
    """
    response = requests.get(UCI_SMS_SPAM_URL, timeout=30)
    response.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(response.content)) as archive:
        with archive.open("SMSSpamCollection") as file:
            df = pd.read_csv(
                file,
                sep="\t",
                header=None,
                names=["original_label", "text"],
                encoding="utf-8",
            )

    df["label"] = df["original_label"].map(
        {
            "spam": "scam",
            "ham": "legitimate",
        }
    )
    df["source"] = "uci_sms_spam"

    normalized = df[["text", "label", "source"]]
    normalized = normalized.dropna().drop_duplicates()

    ensure_directory(output_path.parent)
    normalized.to_csv(output_path, index=False)

    return normalized


def normalize_kaggle_email_dataset(
    input_path: Path,
    output_path: Path,
) -> pd.DataFrame:
    """Normalize Kaggle phishing/legitimate email dataset.

    This function is designed for the local Kaggle file:
    ``phishing_legit_dataset_KD_10000.csv``.

    Expected columns include:
    - text
    - label
    - phishing
    - severity
    - confidence

    Parameters
    ----------
    input_path : Path
        Raw Kaggle CSV path.
    output_path : Path
        Destination CSV path.

    Returns
    -------
    pandas.DataFrame
        Normalized dataset with text, label, and source columns.
    """
    if not input_path.exists():
        raise FileNotFoundError(
            f"Kaggle email dataset not found: {input_path}\n"
            "Place phishing_legit_dataset_KD_10000.csv in data/raw/."
        )

    df = pd.read_csv(input_path)

    if "text" not in df.columns or "label" not in df.columns:
        raise ValueError(
            "Expected Kaggle dataset to contain 'text' and 'label' columns. "
            f"Found columns: {df.columns.tolist()}"
        )

    normalized = df[["text", "label"]].copy()

    normalized["label"] = normalized["label"].map(
        {
            1: "scam",
            0: "legitimate",
            "1": "scam",
            "0": "legitimate",
            "phishing": "scam",
            "spam": "scam",
            "scam": "scam",
            "legitimate": "legitimate",
            "ham": "legitimate",
        }
    )

    normalized["source"] = "kaggle_email_phishing"
    normalized = normalized[["text", "label", "source"]]
    normalized = normalized.dropna().drop_duplicates()

    ensure_directory(output_path.parent)
    normalized.to_csv(output_path, index=False)

    return normalized


def normalize_mendeley_smishing_dataset(
    input_path: Path,
    output_path: Path,
) -> pd.DataFrame:
    """Normalize the Mendeley SMS phishing/smishing dataset.

    The Mendeley dataset description lists key attributes such as LABEL and TEXT.
    Labels include ham, spam, and smishing. This project maps both spam and
    smishing to ``scam`` and ham to ``legitimate``.

    Parameters
    ----------
    input_path : Path
        Raw Mendeley CSV path.
    output_path : Path
        Destination CSV path.

    Returns
    -------
    pandas.DataFrame
        Normalized dataset with text, label, and source columns.
    """
    if not input_path.exists():
        raise FileNotFoundError(
            f"Mendeley smishing dataset not found: {input_path}\n"
            "Download the dataset from Mendeley and place it in data/raw/."
        )

    df = pd.read_csv(input_path)

    # Normalize column names because public datasets love making us suffer.
    df.columns = [str(col).strip().lower() for col in df.columns]

    possible_text_cols = ["text", "message", "sms", "content", "body"]
    possible_label_cols = ["label", "class", "category", "type"]

    text_col = next((col for col in possible_text_cols if col in df.columns), None)
    label_col = next((col for col in possible_label_cols if col in df.columns), None)

    if text_col is None or label_col is None:
        raise ValueError(
            "Could not detect text/label columns in Mendeley dataset. "
            f"Found columns: {df.columns.tolist()}"
        )

    normalized = df[[text_col, label_col]].copy()
    normalized.columns = ["text", "original_label"]

    label_clean = normalized["original_label"].astype(str).str.lower().str.strip()

    normalized["label"] = label_clean.map(
        {
            "ham": "legitimate",
            "legitimate": "legitimate",
            "0": "legitimate",
            "spam": "scam",
            "smishing": "scam",
            "phishing": "scam",
            "scam": "scam",
            "1": "scam",
        }
    )

    normalized["source"] = "mendeley_sms_phishing"
    normalized = normalized[["text", "label", "source"]]
    normalized = normalized.dropna().drop_duplicates()

    ensure_directory(output_path.parent)
    normalized.to_csv(output_path, index=False)

    return normalized


def create_seed_examples(output_path: Path) -> pd.DataFrame:
    """Create a small set of manually curated scam and legitimate examples.

    These examples keep the project linguistically grounded by including clear
    scam indicators such as urgency, impersonation, account verification, and
    credential requests.

    Parameters
    ----------
    output_path : Path
        Destination CSV path.

    Returns
    -------
    pandas.DataFrame
        Seed examples with text, label, and source columns.
    """
    examples = [
        ("Official support here. Verify your account now to avoid suspension.", "scam"),
        ("Your account has been compromised. Reset your password immediately.", "scam"),
        ("Limited time offer. Confirm your identity to claim your reward.", "scam"),
        ("Urgent: your payment failed. Update your billing information now.", "scam"),
        ("Congratulations, you have won a prize. Click the link to claim today.", "scam"),
        ("Your monthly statement is now available in your account portal.", "legitimate"),
        ("Your appointment confirmation has been updated.", "legitimate"),
        ("Your package delivery status changed this morning.", "legitimate"),
        ("Your password was changed successfully.", "legitimate"),
        ("Thank you for contacting customer support. We received your request.", "legitimate"),
    ]

    df = pd.DataFrame(examples, columns=["text", "label"])
    df["source"] = "manual_seed_examples"

    ensure_directory(output_path.parent)
    df.to_csv(output_path, index=False)

    return df


def combine_datasets(input_paths: list[Path], output_path: Path) -> pd.DataFrame:
    """Combine normalized datasets into one project dataset.

    Parameters
    ----------
    input_paths : list[Path]
        CSV files with text, label, and source columns.
    output_path : Path
        Destination CSV path.

    Returns
    -------
    pandas.DataFrame
        Combined and deduplicated dataset.
    """
    frames = []

    for path in input_paths:
        if not path.exists():
            print(f"Skipped missing file: {path}")
            continue

        frame = pd.read_csv(path)

        missing_cols = {"text", "label", "source"} - set(frame.columns)
        if missing_cols:
            raise ValueError(f"{path} missing columns: {missing_cols}")

        frames.append(frame[["text", "label", "source"]])

    if not frames:
        raise FileNotFoundError("No normalized datasets were found to combine.")

    combined = pd.concat(frames, ignore_index=True)
    combined = combined.dropna(subset=["text", "label"])
    combined = combined[combined["label"].isin(["scam", "legitimate"])]
    combined = combined.drop_duplicates(subset=["text"])

    ensure_directory(output_path.parent)
    combined.to_csv(output_path, index=False)

    return combined


def print_dataset_summary(df: pd.DataFrame, name: str) -> None:
    """Print a compact dataset summary.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset to summarize.
    name : str
        Dataset name.
    """
    print(f"\n{name}")
    print("-" * len(name))
    print(f"Shape: {df.shape}")
    print(df["label"].value_counts(dropna=False))
    print(df["source"].value_counts(dropna=False))


def main() -> None:
    """Collect, normalize, and combine project datasets."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path("."),
        help="Project root directory.",
    )
    args = parser.parse_args()

    project_root = args.project_root.resolve()

    raw_dir = project_root / "data" / "raw"
    processed_dir = project_root / "data" / "processed"

    uci_path = raw_dir / "uci_sms_spam.csv"
    kaggle_raw_path = raw_dir / "phishing_legit_dataset_KD_10000.csv"
    kaggle_normalized_path = raw_dir / "kaggle_email_phishing_normalized.csv"
    mendeley_raw_path = raw_dir / "mendeley_sms_phishing.csv"
    mendeley_normalized_path = raw_dir / "mendeley_sms_phishing_normalized.csv"
    seed_path = raw_dir / "manual_seed_examples.csv"
    combined_path = processed_dir / "combined_scam_dataset.csv"

    uci_df = download_uci_sms_spam(uci_path)
    print_dataset_summary(uci_df, "UCI SMS Spam Dataset")

    kaggle_df = normalize_kaggle_email_dataset(
        kaggle_raw_path,
        kaggle_normalized_path,
    )
    print_dataset_summary(kaggle_df, "Kaggle Email Phishing Dataset")

    try:
        mendeley_df = normalize_mendeley_smishing_dataset(
            mendeley_raw_path,
            mendeley_normalized_path,
        )
        print_dataset_summary(mendeley_df, "Mendeley SMS Phishing Dataset")
        normalized_paths = [uci_path, kaggle_normalized_path, mendeley_normalized_path]
    except FileNotFoundError as error:
        print(f"\nMendeley dataset skipped: {error}")
        normalized_paths = [uci_path, kaggle_normalized_path]

    seed_df = create_seed_examples(seed_path)
    print_dataset_summary(seed_df, "Manual Seed Examples")
    normalized_paths.append(seed_path)

    combined_df = combine_datasets(
        normalized_paths,
        combined_path,
    )
    print_dataset_summary(combined_df, "Combined Scam Dataset")

    print(f"\nSaved combined dataset to: {combined_path}")


if __name__ == "__main__":
    main()