# Evidence rules (all modes)

## Labels

| Label | Means | Is it evidence? |
|---|---|---|
| **S#** | Verified external source: title, working primary URL, date (and page/section when specific) | Yes |
| **R#** | A report or file Rahul supplied, with filename and section | Yes, for what it asserts; not independent verification |
| **N#** | A notebook record (past briefing, submission, score) with its path | Yes, for what happened in ROOM |
| **P#** | A persona's proposal or judgment | No. Attribution only |
| **A#** | Assumption or synthetic scenario | No |

Write **Synthetic scenario; assumptions are for this exercise.** once at the
top of a synthetic section, then work naturally. Mark claims at the point
they appear: *Evidence*, *Interpretation*, *Hypothesis*, *Simulation*.

One persona or one source repeated across rooms is not independent
corroboration. Equal speaking time is not equal evidential weight.

## Freshness for current-frontier work

1. Get today's date and Rahul's timezone (America/New_York unless the
   notebook says otherwise). If only the environment's timezone is known,
   say so.
2. Use a rolling 7-day window ending now, prioritizing the last 72 hours.
   State the exact window.
3. Distinguish **posted**, **updated**, **decision**, and **proceedings**
   dates. A new preprint is not a new acceptance. Workshop ≠ main track;
   Findings and journal track ≠ main track; an author's claim of acceptance
   is not official confirmation. A repository update is not a publication.
4. Verify against primary sources: the paper, official proceedings or
   OpenReview, lab publications, official repositories and documentation,
   agency reports (USDOT, FHWA, NHTSA, state DOTs, TRB). Search indexes
   (Google Scholar, arXiv listings, Scopus, Web of Science) are for
   discovery only.
5. Older work is allowed, labeled **background**. In a slow week say so;
   never pad with stale "new" work.
6. Never explain why a paper was accepted unless an official review or
   decision documents it. Otherwise label it `ROOM inference`.
7. Read skeptically: baseline fairness, task selection, ablations, compute
   budget, variance, out-of-distribution tests, leakage, code availability.
8. If live search is unavailable or blocked, say plainly this is a
   **non-current, provisional synthesis**.
9. Distinguish abstract-level reading from full-text reading.

## Numbers

Prefer qualitative likelihood. Date and justify any numerical estimate.
Label illustrative weights as illustrative. Use tools for nontrivial
arithmetic; never present unexecuted code output as a result.

## Synthetic learner priors

A clearly labeled *hypothetical* prior about how ambitious students
commonly get stuck (passive paper collecting, premature implementation,
no customer discovery) may shape diagnostics. It is not data, telemetry, or
retrieved conversations, and it is confirmed or refuted only by Rahul's
submitted work.
