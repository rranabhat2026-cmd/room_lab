# room-lab — WELCOME TO THE ROOM

Rahul Ranabhat's research and mastery lab as one Claude skill, plus its memory.

- `.claude/skills/room/` — the skill. Claude Code loads it automatically in any session on this repo.
  Invoke with `/room …` (weekly, briefing, train, grade, roster, lesson, proposal, brainstorm, or a task for a room).
- `notebook/` — ROOM's memory: roster, learner profile, projects, progress, and every dated report.
  Sessions read it at the start and commit changes at the end.

Examples:

```
/room weekly
/room roster add a TRB reviewer who has seen 200 traffic-forecasting papers
/room have P1, P3 and P5 critique my LWR-PINN study design
/room teach me now
/room grade   (then paste code / a derivation / a draft link)
/room proposal   (attach a paper and describe the idea)
```

To use in claude.ai chat instead, zip `.claude/skills/room` and upload it under Settings → Capabilities → Skills.
Chat has no notebook, so ROOM will end each output with a state block to paste back next time.
