#!/usr/bin/env python3
"""Render a self-contained ROOM report from plain-text JSON (standard library)."""
import argparse
import base64
import html
import json
from pathlib import Path
import re
from urllib.parse import urlsplit


CSS = """
:root{color-scheme:light;--bg:#f4f7f8;--card:#fff;--ink:#172a32;--muted:#53646c;--line:#d9e3e7;--accent:#086c65;--soft:#edf7f4;--th:#edf3f5;--pre:#f4f7f8}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;--bg:#0f1719;--card:#162124;--ink:#e3ecee;--muted:#9fb1b7;--line:#2a3a3f;--accent:#5cc8bd;--soft:#16302d;--th:#1d2b2f;--pre:#111b1e}}
:root[data-theme="dark"]{color-scheme:dark;--bg:#0f1719;--card:#162124;--ink:#e3ecee;--muted:#9fb1b7;--line:#2a3a3f;--accent:#5cc8bd;--soft:#16302d;--th:#1d2b2f;--pre:#111b1e}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 system-ui,sans-serif}
main{max-width:1040px;margin:36px auto;padding:40px;background:var(--card);border:1px solid var(--line);border-radius:12px}
.eyebrow{font-size:.78rem;text-transform:uppercase;letter-spacing:.12em;color:var(--accent);font-weight:700}
h1{font-size:2.25rem;line-height:1.2;margin:12px 0}h2{font-size:1.35rem;line-height:1.35;margin:0 0 14px}
p{margin:10px 0 16px}.meta{color:var(--muted);font-size:.88rem}.summary{font-size:1.12rem;font-weight:550}
.notice{background:var(--soft);border-left:4px solid var(--accent);padding:12px 16px}
nav{display:flex;gap:8px 16px;flex-wrap:wrap;padding:20px 0;border-bottom:1px solid var(--line)}
nav a{font-size:.88rem}a{color:var(--accent);text-underline-offset:3px;overflow-wrap:anywhere}
section{padding:28px 0 6px;border-bottom:1px solid var(--line)}section:last-child{border:0}
.table-wrap{overflow-x:auto}table{width:100%;border-collapse:collapse;font-size:.93rem;margin:14px 0}
th,td{padding:11px 12px;text-align:left;border:1px solid var(--line);vertical-align:top}th{background:var(--th)}
.filter{display:none;width:100%;max-width:360px;padding:7px 10px;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--ink);font:inherit}
.js .filter{display:block}
li{margin:7px 0}ul.checklist{list-style:none;padding-left:0}ul.checklist label{display:flex;gap:10px;align-items:flex-start}
details{margin:14px 0;border:1px solid var(--line);border-radius:8px;padding:14px 18px}
summary{cursor:pointer;font-weight:650}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:.84rem/1.55 ui-monospace,monospace;background:var(--pre);padding:16px;border-radius:6px}
.download{display:inline-block;padding:7px 12px;border:1px solid var(--accent);border-radius:6px;margin:6px 0}
@media(max-width:650px){main{margin:0;padding:22px 16px;border:0;border-radius:0}h1{font-size:1.8rem}th,td{padding:8px}}
@media print{body{background:white;color:black}main{margin:0;border:0;padding:0;max-width:none}nav,.download,.filter{display:none!important}section{break-inside:auto}h2{break-after:avoid}details.solution:not([open]){display:none}}
"""

# Table filter: progressive enhancement only; tables stay fully readable without JavaScript.
JS = """document.documentElement.classList.add('js');
document.querySelectorAll('input.filter').forEach(function(box){
  var rows=document.getElementById(box.dataset.table).tBodies[0].rows;
  box.addEventListener('input',function(){var q=box.value.toLowerCase();
    for(var i=0;i<rows.length;i++){rows[i].style.display=rows[i].textContent.toLowerCase().indexOf(q)<0?'none':'';}});
});"""

REF = r"\[([SRN][1-9][0-9]*)\]"


def render(data):
    def string(value):
        if not isinstance(value, str):
            raise ValueError("Text fields must be strings")
        return value

    def esc(value):
        return html.escape(string(value), quote=True)

    for key in ("title", "date", "summary"):
        string(data[key])
    if not isinstance(data["sections"], list) or not data["sections"]:
        raise ValueError("sections must be a nonempty list")
    sources = data.get("sources", [])
    source_ids = set()
    for source in sources:
        sid = string(source["id"])
        if not re.fullmatch(r"[SRN][1-9][0-9]*", sid) or sid in source_ids:
            raise ValueError("Source IDs must be unique S, R, or N plus positive digits")
        source_ids.add(sid)
        string(source["title"])
        if sid.startswith("S") or source.get("url"):
            url = string(source["url"])
            parsed = urlsplit(url)
            if parsed.scheme not in ("http", "https") or not parsed.hostname or parsed.username or parsed.password or any(ord(c) < 32 for c in url):
                raise ValueError("Source URL must be a public http/https URL without credentials")

    def linked(value):
        value = string(value)
        refs = re.findall(r"\[([SRN][0-9]+)\]", value)
        if any(ref not in source_ids for ref in refs):
            raise ValueError("Unknown source reference in: " + value[:100])
        return re.sub(REF, lambda m: '<a href="#' + m[1] + '">[' + m[1] + ']</a>', esc(value))

    eyebrow = data.get("eyebrow", "WELCOME TO THE ROOM")
    parts = ['<!doctype html><html lang="en"><head><meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width, initial-scale=1">',
             '<title>' + esc(data["title"]) + '</title><style>' + CSS + '</style></head><body><main>',
             '<header><div class="eyebrow">' + esc(eyebrow) + '</div><h1>' + esc(data["title"]) + '</h1>',
             '<p class="meta">' + esc(data["date"]) + '</p><p class="summary">' + linked(data["summary"]) + '</p>']
    if data.get("notice"):
        parts.append('<p class="notice">' + linked(data["notice"]) + '</p>')
    parts.append('</header><nav aria-label="Report sections">')
    for i, sec in enumerate(data["sections"], 1):
        parts.append(f'<a href="#section-{i}">' + esc(sec["title"]) + '</a>')
    if data.get("skill_drafts"):
        parts.append('<a href="#skills">Reusable skill drafts</a>')
    if sources:
        parts.append('<a href="#sources">Sources</a>')
    parts.append('</nav>')
    uses_filter = False
    for i, sec in enumerate(data["sections"], 1):
        parts.append(f'<section id="section-{i}"><h2>' + esc(sec["title"]) + '</h2>')
        if sec.get("collapsible"):
            css = ' class="solution"' if sec.get("solution") else ''
            parts.append('<details' + css + '><summary>' + esc(sec.get("summary_label", "Show details")) + '</summary>')
        for paragraph in sec.get("paragraphs", []):
            parts.append('<p>' + linked(paragraph) + '</p>')
        if sec.get("bullets"):
            parts.append('<ul>' + ''.join('<li>' + linked(x) + '</li>' for x in sec["bullets"]) + '</ul>')
        if sec.get("checklist"):
            parts.append('<ul class="checklist">' + ''.join('<li><label><input type="checkbox"> <span>' + linked(x) + '</span></label></li>' for x in sec["checklist"]) + '</ul>')
        if sec.get("table"):
            table = sec["table"]
            headers = table["headers"]
            if not isinstance(headers, list) or not headers:
                raise ValueError("Table headers must be a nonempty list")
            if table.get("searchable"):
                uses_filter = True
                parts.append(f'<input class="filter" type="search" placeholder="Filter rows" aria-label="Filter table rows" data-table="table-{i}">')
            parts.append(f'<div class="table-wrap"><table id="table-{i}"><thead><tr>' + ''.join('<th scope="col">' + esc(x) + '</th>' for x in headers) + '</tr></thead><tbody>')
            for row in table["rows"]:
                if not isinstance(row, list) or len(row) != len(headers):
                    raise ValueError("Table row length must match headers")
                parts.append('<tr>' + ''.join('<td>' + linked(x) + '</td>' for x in row) + '</tr>')
            parts.append('</tbody></table></div>')
        if sec.get("code"):
            parts.append('<pre><code>' + esc(sec["code"]) + '</code></pre>')
        if sec.get("collapsible"):
            parts.append('</details>')
        parts.append('</section>')
    drafts = data.get("skill_drafts", [])
    names = set()
    if drafts:
        parts.append('<section id="skills"><h2>Reusable skill drafts</h2><p class="meta">Original drafts from this exercise; not installed skills or recovered private workflows.</p>')
        for draft in drafts:
            name = string(draft["name"])
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64 or name in names:
                raise ValueError("Draft names must be unique lowercase-hyphen names, at most 64 characters")
            names.add(name)
            markdown = string(draft["markdown"])
            linked(markdown)  # Validate references without modifying downloadable bytes.
            encoded = base64.b64encode(markdown.encode("utf-8")).decode("ascii")
            parts.append('<details><summary>' + esc(name) + '</summary><p>' + linked(draft["value"]) + '</p>')
            parts.append('<p class="meta">' + linked(draft["attribution"]) + '</p>')
            parts.append('<a class="download" download="' + name + '.md" href="data:text/markdown;charset=utf-8;base64,' + encoded + '">Download ' + name + '.md</a>')
            parts.append('<pre><code>' + esc(markdown) + '</code></pre></details>')
        parts.append('</section>')
    if sources:
        parts.append('<section id="sources"><h2>Sources</h2><ul>')
        for source in sources:
            label = esc(source["title"])
            if source.get("url"):
                label = '<a href="' + esc(source["url"]) + '">' + label + '</a>'
            parts.append('<li id="' + esc(source["id"]) + '"><strong>[' + esc(source["id"]) + ']</strong> ' + label)
            for key in ("path", "date", "note"):
                if source.get(key):
                    parts.append(' · ' + esc(source[key]))
            parts.append('</li>')
        parts.append('</ul></section>')
    parts.append('</main>')
    if uses_filter:
        parts.append('<script>' + JS + '</script>')
    parts.append('</body></html>')
    return '\n'.join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        document = render(json.loads(args.input.read_text(encoding="utf-8")))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as handle:
            handle.write(document)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(1, f"Cannot render report: {exc}\n")
    print(args.output.resolve())


if __name__ == "__main__":
    main()
