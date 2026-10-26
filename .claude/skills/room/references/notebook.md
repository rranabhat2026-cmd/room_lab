# Notebook: ROOM's memory

ROOM remembers only what is written in `notebook/` at the root of the
room-lab repository and committed. A new session (including a scheduled
one) starts with nothing else.

## Layout

```
notebook/
  learner-profile.md     who Rahul is, time budget, demonstrated skills
  roster.yaml            personas and rooms (P1–P4 permanent)
  projects.md            portfolio with status and last change
  progress.md            score history and open assignments
  briefings/YYYY-MM-DD.json + .html     weekly briefings (JSON is the source)
  training/YYYY-MM-DD.json + .html      training packs
  submissions/YYYY-MM-DD-<task>/        what Rahul submitted, as given
  rooms/YYYY-MM-DD-<slug>.json + .html  ad hoc room reports
  proposals/<slug>/                     proposal reports, checkpoints, simulation code
```

## Read at the start

| Mode | Read |
|---|---|
| Weekly / briefing | latest `briefings/*.json`, `projects.md`, `roster.yaml`, `learner-profile.md` |
| Training / teach | latest briefing, latest `training/*.json`, `progress.md`, `learner-profile.md` |
| Grade | the training pack the work answers, `progress.md`, the new submission |
| Room | `roster.yaml`, plus anything the task names |
| Proposal | `proposals/<slug>/checkpoint.md` if resuming, `projects.md` |

If a file is missing or empty, say so once and continue; never invent its
contents. If the notebook isn't present at all (for example in claude.ai
chat without the repo), work without memory, say so, and end the output with
a short **State to carry forward** block Rahul can paste next time.

## Write at the end

- Save the report's JSON and rendered HTML under the dated path; never
  overwrite an earlier dated file (add `-2` for a second run that day).
- Briefing: update `projects.md` statuses with a one-line reason and the
  briefing date.
- Training: add the new assignments to `progress.md` under **Open**, with
  due date and points.
- Grading: copy the submission into `submissions/`, record scores and the
  evidence they rest on in `progress.md`, move the assignment to **Graded**,
  and update **Demonstrated skills** in `learner-profile.md` only from
  graded evidence.
- Roster change: edit `roster.yaml` and note the change in its `changelog`.
- Then commit with a short message (`room: weekly 2026-11-01`) and push the
  working branch. If committing or pushing fails, tell Rahul exactly which
  files are unsaved.

Keep credentials and unnecessary personal data out of the notebook.
