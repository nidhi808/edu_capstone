# src/parser.py - simple parser stub that returns sections
def parse_text_file(path: str) -> dict:
    """
    Read a plain text file and return a dict:
    {"title": <filename>, "sections": [{"heading":..., "text":...}, ...], "raw": <full_text>}
    """
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    sections = []
    cur = {"heading": "Intro", "text": ""}
    for line in raw.splitlines():
        if line.strip().startswith("##"):
            # start new section
            if cur["text"].strip():
                sections.append(cur)
            cur = {"heading": line.strip().lstrip("# ").strip(), "text": ""}
        else:
            cur["text"] += line + "\n"
    if cur["text"].strip():
        sections.append(cur)
    return {"title": path, "sections": sections, "raw": raw}
