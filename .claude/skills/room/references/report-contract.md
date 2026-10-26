# Report contract

Every ROOM report is a JSON source rendered to one self-contained HTML file
by `scripts/render_report.py` (Python standard library only). No external
fonts, scripts, or CDNs. Light and dark themes are built in.

```bash
python3 .claude/skills/room/scripts/render_report.py notebook/briefings/2026-10-30.json notebook/briefings/2026-10-30.html
```

The renderer refuses to overwrite an existing file; use a new dated path
(`-2`) for a second version. Run from the repository root.

## JSON

Required: `title`, `date`, `summary`, `sections`. Prose is plain text (not
HTML or Markdown); don't pre-escape it. Literal `[S1]`, `[R1]`, `[N1]`
markers become links to the matching source; unknown markers fail.

```json
{
  "eyebrow": "WELCOME TO THE ROOM · Weekly briefing",
  "title": "Weekly briefing — 30 Oct 2026",
  "date": "As of 2026-10-30 08:00 America/New_York · window 2026-10-23 to 2026-10-30",
  "summary": "Executive verdict in 3–5 sentences [S1].",
  "notice": "P# attributes a persona's view, not evidence. Synthetic items are labeled.",
  "sections": [
    {
      "title": "Evidence radar",
      "paragraphs": ["..."],
      "bullets": ["..."],
      "table": {"headers": ["Item", "Status"], "rows": [["Title [S1]", "Preprint"]], "searchable": true},
      "code": "optional preformatted text, e.g. a code exercise",
      "checklist": ["optional tickable items"],
      "collapsible": false,
      "summary_label": "Show details",
      "solution": false
    }
  ],
  "sources": [
    {"id": "S1", "title": "Paper title", "url": "https://arxiv.org/abs/...", "date": "posted 2026-10-28", "note": "abstract read"},
    {"id": "R1", "title": "Rahul's report.html", "path": "uploaded file, section 3"},
    {"id": "N1", "title": "Last week's briefing", "path": "notebook/briefings/2026-10-23.json"}
  ],
  "skill_drafts": [
    {"name": "lowercase-hyphen-name", "value": "Why it's useful.", "attribution": "Original draft derived from this room exercise.", "markdown": "---\nname: ...\n---\n..."}
  ]
}
```

Field notes:

- `S#` sources need a verified public http(s) `url`. `R#` and `N#` may give a
  `path` instead.
- `collapsible: true` wraps the section in a closed `<details>`; add
  `"solution": true` for answer sections (hidden in print until opened).
- `searchable: true` adds a row filter that works with JavaScript and
  degrades to a plain table without it (use for evidence matrices).
- `checklist` renders native checkboxes; they don't persist between visits.
- Table rows must match the header length. Draft names are unique
  lowercase-hyphen, at most 64 characters, and download offline as `.md`.

## Before delivering

Check the render succeeded, every nav link and citation resolves, solutions
start closed, no promised file is missing, and dates are absolute. Open or
screenshot the HTML when a browser is available; otherwise say only the
structure was checked. Then save, publish (if the Artifact tool exists), and
commit per `notebook.md`.
