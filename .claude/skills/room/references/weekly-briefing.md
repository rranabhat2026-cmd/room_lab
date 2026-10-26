# Weekly briefing

One briefing a week. It merges the old Friday calibration and Sunday
frontier scan, and feeds the training pack (`training.md`). In weekly mode,
produce the briefing first, then the training pack from it. They are two
reports, rendered separately.

Read `evidence-rules.md` (freshness) and `transportation-lens.md` first, and
the notebook files listed in `notebook.md`.

## 1. Scan

Search the 7-day window (72 hours first) across:

- **AI/ML frontier:** arXiv (cs.LG, cs.AI, cs.CL, cs.CV, cs.RO, cs.MA,
  stat.ML, physics.comp-ph, math.NA), OpenReview and official proceedings
  (NeurIPS, ICML, ICLR, AAAI, KDD, CVPR/ICCV/ECCV, ACL/EMNLP, CoRL, RSS,
  AISTATS, UAI), major and independent lab blogs, official repositories and
  benchmarks.
- **Transportation-specific:** arXiv eess.SY and physics.soc-ph, TRB
  (annual meeting, TRR), journals such as Transportation Research Parts
  A–F, IEEE T-ITS, Transportation Science, Computer-Aided Civil and
  Infrastructure Engineering; USDOT, FHWA, NHTSA, FTA, state DOT and
  research center releases; open-data and tooling releases (SUMO, MATSim,
  OSMnx, GTFS, open traffic datasets).
- **Broader technology** only when it plausibly matters to transportation
  (sensing, connectivity, energy, geospatial, policy).

Select **5–10 genuinely material items**; fewer in a slow week. Coverage is
relevance-selected, never a representative survey; say so.

## 2. Report structure

1. **Header:** as-of date and timezone, exact window, evidence status (live
   / partial / provisional), and a 3–5 sentence **Executive verdict**: what
   strengthened or weakened ROOM's projects this week and why.
2. **Evidence radar** (table): title (linked), org when useful, date and
   which date it is, status (preprint / workshop / main track / journal /
   agency report / release), the key reported finding, the main limitation,
   and the ROOM project affected.
3. **Transportation integration** (the heart of the briefing): for each
   item that earns it, apply the template in `transportation-lens.md`. Pick
   the strongest 2–3 and develop them fully; give the rest one line.
4. **Accepted-paper notes** (only when a top venue published decisions or
   proceedings in the window): venue and track, paper type, strongest
   contribution, experimental and mathematical depth, reproducibility,
   acceptance evidence (`Documented` or `ROOM inference`), and
   **Mathematics essential?** `Yes` / `Helpful but not essential` / `No`
   with one sentence. Add a short "what actually gets accepted" note,
   flagged as a biased, relevance-selected sample.
5. **Mentor calibration.** For each of P1–P4 (and any active persona the
   roster marks `weekly: true`):
   - worldview update from this week's evidence (cite S#);
   - 5–8 terms, methods, tools, papers, or labs worth recognizing;
   - one belief revised (only against a prior position in the notebook;
     otherwise "first calibration, no prior to compare");
   - one approach to deprioritize;
   - one hard question for Rahul;
   - one warning about hype, weak evidence, or unsafe assumptions.
   Then a **synthesis**: agreements, real disagreements and what they would
   change, open scientific questions.
6. **Opportunities:** top 3 research opportunities and top 3 practical or
   startup opportunities, each tied to transportation. For each: the gap,
   closest verified prior art, the cheapest experiment that would tell you
   something, success and failure metrics, and the main risk. Business
   framing: customer (agency, operator, consultant, fleet, city) →
   expensive workflow → current workaround → failure cost → measurable
   outcome → first interview or prototype. Gains are hypotheses until
   measured.
7. **Project status** (table from `notebook/projects.md`): each project
   marked `Strengthened` / `Threatened` / `Refine` / `Watch` / `Pause`, with
   what already exists and what still needs testing. Novelty is a
   hypothesis until prior art is checked.
8. **Training handoff:** the 3–5 skills next week's training pack should
   build, and why each matters now.
9. **Sources.**

Keep the main body technically dense but readable in about 15 minutes; put
long detail in collapsible sections. Do not repeat the same summary across
sections.

## 3. Publication discipline (for any proposed paper)

One-sentence falsifiable hypothesis; closest verified prior art and the
remaining limitation; controlled baselines including a cheap classical or
numerical one; data or environment, held-out regimes (future periods,
unseen corridors or cities), repeated seeds, uncertainty, hardware and
time budget; how a null result would be read; paper type (method,
benchmark, theory, systems, application, diagnostic); best-fit venues. Keep
what a paper proves mathematically separate from what experiments show.

## 4. Finish

Render, save, update `projects.md`, commit (see `notebook.md`), then build
the training pack if this is a weekly run.
