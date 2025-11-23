# src/fix_agent.py
"""
Compose suggested fixes from detected issues.
This simple agent turns issues into human-readable fix suggestions.
"""

def compose_fixes(issues):
    fixes = []
    for it in issues:
        t = it.get("type", "")
        if t == "ambiguity":
            fixes.append({
                "action": "rewrite",
                "section": it.get("section"),
                "original": it.get("text"),
                "suggestion": it.get("suggested_fix")
            })
        elif t == "contradiction":
            fixes.append({
                "action": "clarify_scope",
                "original": it.get("description"),
                "suggestion": it.get("suggested_fix")
            })
        elif t.startswith("missing"):
            fixes.append({
                "action": "add_acceptance",
                "original": it.get("description"),
                "suggestion": it.get("suggested_fix")
            })
        else:
            fixes.append({
                "action": "investigate",
                "original": it.get("description") or it.get("text"),
                "suggestion": "Please review this item and provide guidance."
            })
    return fixes
