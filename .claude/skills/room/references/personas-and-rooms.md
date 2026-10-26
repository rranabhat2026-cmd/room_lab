# Personas and rooms

Rahul can create any persona he wants and have personas work together in
rooms for any purpose: critique a paper, design a study, plan a startup,
review a proposal, prepare for a defense, model how a request might land.

## Roster (`notebook/roster.yaml`)

Operations: **add**, **edit**, **pause / resume**, **remove**, **regroup**
(change room membership), **list**. P1–P4 are permanent: pause them, never
delete them. IDs are stable (`P5`, `P6`, …, never reused); removing someone
from one room doesn't remove them elsewhere unless Rahul says so.

Each persona records: `id`, `name` (display role), `expertise`,
`responsibilities`, `goals`, `incentives`, `constraints`, `working_style`,
`typical_objections`, `uncertainty`, `weekly` (true if it joins the weekly
briefing), `status` (active / paused). Ground traits in the role and task,
not stereotypes from a title. When Rahul describes a persona loosely, fill
the fields with sensible defaults, show the entry, and save it; he can
edit.

Personas built on real institutions or job titles are fictional composite
perspectives: no claimed affiliation, private access, or real person's
voice. Never build a persona that impersonates a specific real individual.

Each room records: `id`, `question`, `members`, `assignments`,
`deliverable`, `synthesis_owner`. Model personas as nodes, collaborations
as edges, and rooms as overlapping subgraphs; show a membership table when
clearer than a diagram. Don't create rooms a small task doesn't need.

Record every change in the roster's `changelog` with date and reason.

## Running a room (`/room <task>`)

1. **Define the task:** objective, audience, constraints, deliverable,
   success criteria. Infer routine defaults; state consequential
   assumptions; ask only when an answer changes the result.
2. **Independent first pass:** each member gets a distinct question and a
   bounded contribution (about 100–150 words, adjusted for roster size).
   Collect all first positions before anyone sees others' conclusions.
   Where a subagent tool exists and the parts are separable, delegate for
   real, passing the objective, evidence, assignment, date, timezone, and
   constraints, and batch large rosters without dropping anyone. Say which
   contributions were delegated and which were simulated in labeled passes;
   never claim independent models otherwise.
3. **AI-use cases** (when useful): for a persona, a realistic task they'd
   use AI for; inputs and tools (synthetic stand-ins for anything
   confidential); an example prompt, expected output, how to verify it, and
   an acceptance criterion; benefits, failure modes, an alternative
   workflow.
4. **Cooperation modeling** (only for persuasion or psychology tasks):
   draft a truthful request stating purpose, relevance, effort, and benefit;
   simulate acceptance, conditional acceptance, and refusal with stated
   assumptions; revise wording to address concerns while keeping the
   freedom to decline. For coursework separate manipulated factors,
   outcomes, and confounds, and suggest a measurable comparison. Simulated
   responses are never findings.
5. **Challenge round:** one focused round of cross-critique, then
   synthesis. Add a round only for an unresolved issue that changes the
   decision. Stop when assignments have usable answers and uncertainty is
   recorded.
6. **Participation pause** (Rahul's "solitary confinement" rule): a persona
   that takes another turn before others have had theirs, or repeatedly
   overruns its budget after a reminder, is paused. Its new comments queue;
   its existing evidence and urgent factual corrections stay on the record.
   Others finish one bounded round. On release it gets a short recap and
   one concise reply limited to new evidence or changed conclusions. Apply
   globally by ID across rooms. Record pause and release in one line, and
   describe it as simulated turn-taking unless real isolation was used.
7. **Synthesize:** merge, de-duplicate, resolve conflicts against the
   success criteria, and trace repeated claims to their origin. Keep strong
   minority objections. Explain the evidence behind the recommendation.
8. **Reusable workflow drafts:** when a workflow from the room is worth
   repeating, write 1–3 complete Markdown skill drafts (frontmatter `name`
   and `description`, then Inputs, Procedure, Verification and limitations,
   Output), labeled **original draft derived from this room exercise**,
   never a recovered private workflow. Explain why none is warranted when
   none is. Drafts are not installed unless Rahul asks.

## Room report

Objective and conclusion; date and timezone; execution mode (delegated or
simulated); roster and room map; distinct contributions (P#); AI-use cases
and cooperation exercise when relevant; moderation and disagreements;
recommendation; workflow drafts; sources and assumptions; open questions;
next actions. Usually 800–1,500 words for four personas, with full drafts
and detail in collapsible sections. Render via `report-contract.md` and
save under `rooms/`. When it would help, end with a lesson handoff (key
concepts, prerequisites, verified papers or tools, open questions, one
exercise, three priorities) that `/room lesson` can pick up.
