# src/contradiction_agent.py - simple contradiction checker

def detect_contradictions(parsed_doc: dict):
    """
    Simple check:
    If document contains both 'optional' and 'required' in different places,
    we flag a contradiction.
    This is a minimal heuristic for demo.
    """
    text = parsed_doc.get("raw", "").lower()
    issues = []

    if "optional" in text and "required" in text:
        issues.append({
            "type": "contradiction",
            "description": "Conflict detected: The document uses both 'optional' and 'required'. Clarify the true requirement.",
            "severity": 0.9,
            "suggested_fix": "Decide if the feature is optional OR required and update all sections consistently."
        })

    return issues
