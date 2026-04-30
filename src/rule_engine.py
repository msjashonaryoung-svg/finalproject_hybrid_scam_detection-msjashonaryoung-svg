"""Rule-based linguistic scam detector."""

from preprocessing import basic_clean_text


SCAM_RULES = {
    "urgency": [
        "act now",
        "limited time",
        "last chance",
        "immediately",
        "before midnight",
        "now",
    ],
    "guaranteed_profit": [
        "guaranteed returns",
        "risk free",
        "double your money",
        "100x",
        "profit guaranteed",
        "receive double",
    ],
    "wallet_request": [
        "connect wallet",
        "connect your wallet",
        "verify wallet",
        "seed phrase",
        "recovery phrase",
        "import wallet",
    ],
    "impersonation": [
        "official support",
        "admin here",
        "support agent",
        "compliance team",
        "account recovery",
    ],
    "fear_loss": [
        "account suspended",
        "funds at risk",
        "wallet compromised",
        "compromised",
        "avoid losing",
        "restricted account",
    ],
}


def score_with_rules(text: str, rules: dict[str, list[str]] = SCAM_RULES) -> dict:
    """Score a message using explicit scam-related linguistic rules.

    Parameters
    ----------
    text : str
        Input message to evaluate.
    rules : dict[str, list[str]], default=SCAM_RULES
        Dictionary mapping scam categories to phrase lists.

    Returns
    -------
    dict
        Dictionary containing rule score, triggered categories, and matched phrases.
    """
    cleaned = basic_clean_text(text)
    triggered = {}
    total_matches = 0

    for category, phrases in rules.items():
        matches = [phrase for phrase in phrases if phrase in cleaned]

        if matches:
            triggered[category] = matches
            total_matches += len(matches)

    max_possible = sum(len(phrases) for phrases in rules.values())
    rule_score = total_matches / max_possible if max_possible else 0

    return {
        "rule_score": rule_score,
        "triggered_categories": list(triggered.keys()),
        "matched_phrases": triggered,
    }


def rule_predict(rule_score: float, threshold: float = 0.06) -> str:
    """Predict a label from a rule-based scam score.

    Parameters
    ----------
    rule_score : float
        Rule-based scam score.
    threshold : float, default=0.06
        Minimum score required to classify text as scam.

    Returns
    -------
    str
        Predicted label, either ``scam`` or ``legitimate``.
    """
    return "scam" if rule_score >= threshold else "legitimate"