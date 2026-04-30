"""Text preprocessing utilities for the hybrid crypto scam detection project."""

import re


def basic_clean_text(text: str) -> str:
    """Clean text while preserving scam-relevant language patterns.

    Parameters
    ----------
    text : str
        Raw input text.

    Returns
    -------
    str
        Cleaned lowercase text with normalized URLs and spacing.
    """
    if not isinstance(text, str):
        return ""

    cleaned = text.lower()
    cleaned = re.sub(r"https?://\S+|www\.\S+", " URL ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    return cleaned