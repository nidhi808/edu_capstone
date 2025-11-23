# src/main.py - CLI runner for the EIRS pipeline

import sys
import json
from controller import run_pipeline


def pretty_print(output):
    """
    Nicely prints issues, fixes, and tasks.
    """
    print("\n===== ISSUES FOUND =====")
    for idx, issue in enumerate(output["issues"], start=1):
        print(f"{idx}. [{issue.get('type')}] {issue.get('description') or issue.get('text')}")
        if issue.get("section"):
            print(f"   Section: {issue.get('section')}")
        if issue.get("context"):
            print(f"   Context: {issue.get('context')}")
        print("   Severity:", issue.get("severity"))

    print("\n===== SUGGESTED FIXES =====")
    for fix in output["fixes"]:
        print(f"- Action: {fix.get('action')}")
        print(f"  Suggestion: {fix.get('suggestion')}\n")

    print("\n===== TASKS CREATED =====")
    print(json.dumps(output["tasks"], indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/main.py sample_docs/doc1.txt")
        sys.exit(1)

    doc_path = sys.argv[1]
    result = run_pipeline(doc_path)
    pretty_print(result)
