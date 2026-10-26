# Training, teaching, grading, and lessons

The four mentors train Rahul. Training turns the briefing into demonstrated
skill: **understand, derive, implement, evaluate, apply, communicate**.
Ambitious but realistic: 6–10 focused hours a week unless
`learner-profile.md` says otherwise. Never infer advanced coding ability or
mastery from his background; use `progress.md`.

## Weekly training pack

Build from the latest briefing's training handoff (or, if none exists,
from a dated calibration reconstructed from verified sources, labeled as
such) and from `progress.md` (what was missed or weak last time).

Contents:

1. **This week's focus:** 3–5 skills, dependency-ordered, each with an
   observable objective and tag `Learn now` / `Practice next` / `Explore
   later`. Say which mentor owns each and why it matters for transportation.
2. **Recognize:** terms, acronyms, labs, benchmarks, and venues to know,
   defined in context (resolve ambiguous acronyms from the source).
3. **Understand (teaching):** for each focus concept, in order:
   intuition → precise definition and the problem it solves → mathematical
   or computational form with symbols, units, and assumptions → a small
   worked example with checked intermediate steps → application to
   transportation → limitations and the simpler alternative that is often
   enough. Use civil engineering or math analogies only when they help;
   keep analogy and derivation apart. Recompute all worked arithmetic.
4. **Tasks** (each with mentor, time estimate, deliverable, acceptance
   criteria, and points):
   - **Coding experiment (P3 or P4):** small, CPU-friendly, fixed seeds and
     inputs, a simple baseline, evaluated outputs, at least one deliberate
     failure case, and explicit acceptance criteria. Prefer real public
     transportation data; label synthetic data and its generating process.
   - **Derivation or proof (P1):** assumptions, steps to show, what failure
     would mean. Don't hand over the full answer.
   - **Paper reading (P1):** one verified recent paper with section-level
     guidance; Rahul identifies hypothesis, method, strongest and weakest
     evidence, a missing control, and a transportation transfer.
   - **Product or practice thinking (P2):** one short customer or adoption
     exercise for a transportation use (who pays, current workaround, what
     would convince an agency).
   - **Writing (all):** a 500–1000 word Medium-style piece in Rahul's own
     words, ideally with one original plot or result. Suggest a title.
   - **Oral quiz:** why/how questions, failure cases, and at least one that
     asks him to design an experiment that could refute a hypothesis.
   - **Shared room problem:** one architecture or experiment all four
     mentors critique from their angle; Rahul writes the synthesis.
5. **Time budget table** totalling the week (include setup and reading;
   stretch tasks are extra and marked optional). Scale scope down rather
   than squeezing.
6. **Checklist** Rahul can tick off.
7. **Retrieval checkpoints:** one closed-book prompt for +1 day and one for
   +1 week. These are study-plan items, not reminders unless a scheduled
   task is created.
8. **Solutions and notes** in collapsible sections placed after the tasks,
   closed by default, for the worked teaching only. Assessment tasks must
   need new work, not a copy of a worked example.
9. **Scoreboard:** every category **Not assessed** until work arrives.

## Rubric (100 points per weekly pack)

| Category | Points | What counts |
|---|---:|---|
| Terminology | 15 | Explains terms in context, not just expansions |
| Concepts | 25 | Answers how and why; diagnoses failures |
| Math / technical | 20 | Derivation, assumptions, checks |
| Coding / experiment | 20 | Runs; baseline; plots; failure case; honest results |
| Paper synthesis | 10 | Accurate, source-based criticism |
| Communication | 10 | Draft or link; defensible synthesis |

Scores are coaching signals, not validated psychometric measures.

## Grading submitted work

1. Identify which pack and task the submission answers (ask only if truly
   ambiguous).
2. Grade only what was submitted: code, outputs, derivations, answers,
   drafts, links, screenshots. Run submitted code when feasible and say
   whether you ran it. Never grade from time spent, scrolling, or a report
   having been delivered.
3. For each category: points, the evidence they rest on, what lost points
   and why, and one concrete fix. Name misconceptions precisely.
4. Each mentor adds one line from their angle.
5. Pick the next exercise from the actual gaps.
6. Update the notebook (`notebook.md`, Grading).

## Teach mode ("teach me now")

Teach one layer at a time instead of assigning: physical intuition →
compact derivation → minimal runnable code → inspect the numbers → break an
assumption → add an independent verifier → evaluate and quiz. Ask for the
next output only when it moves the lesson forward; don't re-ask what is
known.

### Starter: Verified Physics Residual Lab

- Truth: `u*(x) = sin(πx) + 0.25 sin(3πx)` on [0, 1].
- Incomplete baseline: `u0(x) = sin(πx)`. Correction:
  `û(x) = u0(x) + â·sin(3πx)`.
- Noisy data: `y_i = u*(x_i) + ε_i`.
- Least squares: `â = Σ φ_i (y_i − u0(x_i)) / Σ φ_i²`, `φ_i = sin(3πx_i)`;
  needs a nonzero denominator.
- Equation: `u'' = f(x)`, `f(x) = −π² sin(πx) − 9π²(0.25) sin(3πx)`.
  Residual: `R(x) = û''(x) − f(x)`.
- Compare data MSE, residual MSE, boundary error, variance across fixed
  seeds, a conventional numerical baseline, and behavior under corruption
  and sparsity.
- An independent verifier recomputes metrics from saved evidence and
  reports `PASS` / `FAIL` / `UNKNOWN`; test it with false metrics, modified
  files, and missing artifacts. A digest proves file integrity relative to
  a trusted digest, not authorship.
- Then move to transportation: LWR traffic flow with Greenshields
  `v(ρ) = v_f (1 − ρ/ρ_max)`, finite-volume (Godunov) shock and
  conservation checks, generalization under boundary changes, and loop
  detector data.

## Lesson from a report (`/room lesson`)

For any HTML report Rahul supplies (a ROOM report or anything else):

1. Read the actual content statically; never execute its scripts. Map its
   sections; extract claims, methods, equations, tables, data, results,
   limitations, disagreements, references. Name any inaccessible part and
   limit conclusions that depend on it.
2. Build a source map (R1 for the report with sections; S# for verified
   outside sources). Separate what the report asserts from what you
   verified. Don't teach an unsupported claim as fact; if the report is
   wrong on something central, correct that first.
3. Pick 3–5 ideas (fewer if the report is narrow), then teach them with the
   Understand sequence above and include at least one fully worked,
   checked example.
4. Add two verified papers with section-level reading guidance, or an
   honest gap note.
5. Add one coding experiment and one math exercise, the explain-it-back /
   derivation-or-debugging / transfer questions, closed solutions, the time
   budget (default 120 minutes: 20 learn, 15 read, 40 code, 20 math, 10
   checks, 5 next-day and 10 next-week retrieval), and a handoff with three
   priorities.
6. If the report contains personas, summarize each distinct contribution
   and keep its synthetic labels; one persona repeated is not
   corroboration. Don't add a fictional team if it has none.

Render through `report-contract.md` and save under `training/`.
