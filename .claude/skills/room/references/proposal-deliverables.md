# Evidence and deliverable specifications

## Search log

Record one entry per actual search: date/time, database or endpoint, exact query, filters, accessible coverage, screening decision, and relevant results. Mark searches completed, blocked, partial, or planned. Record counts only if actually observed.

Construct queries from problem synonyms, theory, method families, application, and competing approaches. Adapt syntax to each database rather than pasting one expression everywhere. When accessible, verify current syntax in official help. Supply native queries for inaccessible databases as unexecuted suggestions. Record targeted web search separately from native Scopus, Web of Science, or Google Scholar searches.

Trace references and citing papers for the seed paper and closest competitors. Deduplicate preprints and final publications by DOI/title/authors and preserve version information when differences matter. Record important exclusions and contradictory findings; describe the search as focused unless a systematic-review protocol was actually followed.

## Evidence matrix

Use one row per study and stable study IDs. Include:

| Group | Required fields |
| --- | --- |
| Identity | Verified title, authors, year, venue, publication status, DOI/direct primary link |
| Inspection | Full text, partial text, abstract only, or metadata only; version and inspection date |
| Scientific basis | Question, theory, key assumptions, method |
| Experiment | Data, study units, baselines, split/design, metrics, uncertainty |
| Findings | Supported claims, numerical results only when verified, section/page/table locator |
| Limitations | Author-stated limitations separately from analyst concerns |
| Proposal relevance | Competing solution, supporting mechanism, unresolved limitation, or feasibility evidence |

Use “not reported” or “not inspected” instead of filling gaps with guesses. Do not infer full-text details from an abstract. Distinguish author-reported performance from independent replication and your own executed results. Make score comparability conditional on matching data, splits, tasks, and metrics.

## Claims and references

Place citations close to supported claims. Use primary evidence and clickable source URLs/DOIs; include page/section locators for PDF-specific statements. Separate quotations from paraphrases, observe applicable source limits, and avoid unsupported precision. Do not reproduce tables or long passages when an attributed summary suffices.

Maintain claim-to-source mappings for consequential novelty, theory, calibration, performance, and journal-ranking statements. Label analyst inferences explicitly. Keep references consistent across the report, matrix, parameter registry, and checkpoint.

## Journal shortlist

For each of 3–5 candidates provide official scope/source, fit to the contribution, likely reviewer expectations, and known constraints. Record quartile, ranking system (JCR or SJR), ranking year, subject category, verification URL, and access date, or explicitly mark unverified. Do not mix categories or years, promise acceptance, or imply a paper inherits its venue's methodological quality.

## HTML report outline

Create one readable, downloadable HTML report by default. Use inline CSS and necessary JavaScript, searchable evidence rows, compact navigation, accessible contrast, responsive tables, and print-friendly styling. Embed required figures so the file is self-contained; outbound source links may require internet. A self-contained report does not require website publication.

Include these sections, adjusted only for an explicit narrower request:

1. Executive summary, selected direction, readiness assessment, and study status.
2. Starting-paper analysis and relation to the idea.
3. Search date, scope, access limitations, and reproducible search log.
4. Searchable literature evidence matrix (approximately 15–25 relevant studies).
5. Comparison of three directions and justified selection.
6. Complete proposal: title, abstract, problem, gap, questions/hypotheses, theory/equations, method, data, design, baselines, metrics, ablations, uncertainty, contributions, limitations, and validity threats.
7. Synthetic-study design, assumptions, parameter provenance, execution status, results actually obtained, negative findings, and empirical-validation needs.
8. Minimum viable study, first experiment, resources/compute, milestones, essential/optional work, failure criteria, and fallback.
9. Journal shortlist, skeptical review, and incorporated revisions.
10. Glossary for unfamiliar terms, references, unresolved questions, and next three actions.

Deliver simulation code, data sample, data dictionary, parameters/configuration, dependency information, run manifest, and relevant figures. Keep a machine-readable evidence matrix/search log when useful. Use actual file links only after successful creation and saving. If the requested format differs, preserve the evidence and reproducibility requirements in that format.

## Final quality gates

- Check the closest competing work is discussed and novelty is bounded by the actual search.
- Confirm consequential factual claims, parameter sources, and rankings have support or an uncertainty label.
- Confirm hypotheses and expected outcomes are not presented as completed findings.
- Confirm the synthetic study is present for a full run, or the exact execution limitation and runnable code are supplied.
- Confirm simulation claims match saved outputs and the actual implemented methods, with fair baseline and misspecification checks.
- Confirm leakage prevention, fair comparisons, uncertainty, and negative outcomes are addressed.
- Verify local report assets and evidence search behavior where rendering/execution tools are available; check citation anchors and link targets for consistency without claiming every external link was opened.
- Confirm all promised files exist and were saved through the available artifact workflow.
- State material incomplete stages and actual execution/scheduling status.

## Continuation checkpoint

Save a Markdown checkpoint when interruption is likely or a completed step is costly to reproduce. Include:

- Objective, current question, selected direction, and user constraints.
- Supplied inputs, accessible resources, and provisional assumptions.
- Completed steps, verified findings, references, and claim/source locators.
- Searches performed versus pending/blocked and source inspection levels.
- Artifact locations and stable identifiers if available.
- Simulation code/configuration, parameter provenance, seeds, scenarios, replications, dependency versions, execution status, outputs, and failures.
- Unresolved questions, decisions needed, and exact next actions in dependency order.
- Delivery target/timezone and any confirmed task identifier, scheduled timestamp, actual task type, and access dependencies.

Do not put credentials or unnecessary personal data in checkpoints. Ensure a configured future run can read its inputs. Resume from verified artifacts rather than assuming the previous context, computation, or background execution persisted.
