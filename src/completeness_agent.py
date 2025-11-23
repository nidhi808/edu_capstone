# src/completeness_agent.py
"""
Detects missing acceptance criteria and missing owners in a parsed document.
This is a simple heuristic-based detector for the demo.
"""

import re

def detect_completeness_issues(parsed_doc: dict):
    issues = []
    raw = parsed_doc.get("raw", "") or ""
    text_lower = raw.lower()

    # 1) Missing acceptance criteria
    if "acceptance" not in text_lower and "given" not in text_lower:
        issues.append({
            "type": "missing_acceptance",
            "description": "No explicit acceptance criteria found in the document.",
            "severity": 0.95,
            "suggested_fix": "Add measurable acceptance criteria (e.g., Given-When-Then or precise success metrics)."
        })

    # 2) Missing or unclear owners
    # Heuristic: look for common owner patterns ("Owner:", "Owners:", "Alice", "Bob")
    owner_patterns = ["owner:", "owners:", "assigned to", "responsible:", "alice", "bob", "carla"]
    found_owner = any(p in text_lower for p in owner_patterns)
    if not found_owner:
        issues.append({
            "type": "missing_owner",
            "description": "No clear owner/assignee found for features or tasks.",
            "severity": 0.6,
            "suggested_fix": "Assign clear owners for each feature (e.g., 'Alice: Integration, Bob: QA')."
        })

    # 3) Missing deadlines or TBDs flagged
    if re.search(r"\bTBD\b", parsed_doc.get("raw", ""), flags=re.I) or "deadline is tbd" in text_lower:
        issues.append({
            "type": "missing_deadline",
            "description": "One or more deadlines are marked as TBD or not specified.",
            "severity": 0.8,
            "suggested_fix": "Specify concrete deadlines or a decision owner and timeframe."
        })

    return issues
