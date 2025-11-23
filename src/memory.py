# src/memory.py - simple long-term memory store (json)
import json
import os
import datetime

# memory.json stays in repo root
MEM_FILE = os.path.join(os.path.dirname(__file__), "..", "memory.json")

def store_snapshot(doc_id: str, parsed_doc: dict, issues: list, fixes: list):
    """
    Save a versioned record of the analysis.
    Each run overwrites the entry for this document ID.
    """
    try:
        with open(MEM_FILE, "r", encoding="utf-8") as f:
            memory = json.load(f)
    except Exception:
        memory = {}

    memory[doc_id] = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "parsed": parsed_doc,
        "issues": issues,
        "fixes": fixes
    }

    with open(MEM_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)

    return True
