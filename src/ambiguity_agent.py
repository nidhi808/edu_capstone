# src/ambiguity_agent.py - heuristic ambiguous phrase detector
import re

VAGUE_PATTERNS = [
    r"\bsoon\b",
    r"\bas needed\b",
    r"\breasonable time\b",
    r"\bTBD\b",
    r"\boptional\b",
    r"\b(?:asap|ASAP)\b"
]

def detect_ambiguities(parsed_doc: dict):
    """
    Return a list of ambiguity issue dicts found in parsed_doc.
    Each issue contains: type, section, text, context, severity, suggested_fix.
    """
    issues = []
    for sec in parsed_doc.get("sections", []):
        text = sec.get("text", "")
        for patt in VAGUE_PATTERNS:
            for m in re.finditer(patt, text, flags=re.I):
                span = text[m.start():m.end()]
                context = text[max(0, m.start()-40):m.end()+40].strip()
                issues.append({
                    "type": "ambiguity",
                    "section": sec.get("heading"),
                    "text": span,
                    "context": context,
                    "severity": 0.7,
                    "suggested_fix": f"Replace '{span}' with a concrete specification (e.g., a date, SLA, or exact behavior)."
                })
    return issues
