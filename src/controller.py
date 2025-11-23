# src/controller.py - orchestrator: runs all agents and aggregates outputs

from parser import parse_text_file
from ambiguity_agent import detect_ambiguities
from contradiction_agent import detect_contradictions
from completeness_agent import detect_completeness_issues
from fix_agent import compose_fixes
from task_tool import create_task
from memory import store_snapshot


def run_pipeline(doc_path: str):
    """
    Main orchestrator:
    1. Parse document
    2. Run agents (ambiguity, contradiction, completeness)
    3. Aggregate issues
    4. Compose fixes
    5. Create tasks
    6. Store memory snapshot
    7. Return result
    """

    # 1) Parse doc
    parsed = parse_text_file(doc_path)

    # 2) Run agents
    ambiguities = detect_ambiguities(parsed)
    contradictions = detect_contradictions(parsed)
    completeness = detect_completeness_issues(parsed)

    # 3) Combine issues
    issues = ambiguities + contradictions + completeness

    # 4) Fix suggestions
    fixes = compose_fixes(issues)

    # 5) Task creation (simple stub converting each issue into a task)
    tasks = []
    for it in issues:
        title = (it.get("text") or it.get("description") or "Document issue")[:150]
        meta = {
            "type": it.get("type"),
            "severity": it.get("severity", 0.5),
        }
        t = create_task(title=title, assignee="unknown", due_date=None, meta=meta)
        tasks.append(t)

    # 6) Store memory snapshot
    doc_id = doc_path.split("/")[-1]
    store_snapshot(doc_id, parsed, issues, fixes)

    # 7) Return everything
    return {
        "doc_id": doc_id,
        "issues": issues,
        "fixes": fixes,
        "tasks": tasks,
    }
