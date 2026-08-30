# Exported IBM Bob Report — ACTION NEEDED

The contest requires "evidence of technology proof-of-concept solution,
including exported IBM Bob report of all relevant tasks/sessions used for
the contest." That export has to come from an actual Bob session, since
it's a record of real tool calls and reasoning — it can't be pre-written.

## How to produce it

1. Open this repo in Bob (IDE integration or Bob CLI/BobShell).
2. Run `bob/orchestrator-prompt.md` in **Orchestrator mode**, pointing it
   at the `feature/task-priority-patch` branch.
3. Let it dispatch the four subagents from `bob/subagents/` as parallel
   tasks and produce the aggregated review comment.
4. Export the session/task history. Depending on your Bob version this is
   typically available as:
   - A session export from the IDE panel, or
   - A BobShell log (`bob/reports/session-<date>.json` or similar —
     BobShell is described as producing self-documenting records of every
     agentic action).
5. Save the export into this folder, e.g.:
   - `submission/bob-session-export.json` (or whatever format Bob gives
     you — PDF, JSON, or Markdown transcript are all fine)
6. Replace `bob/sample-review-output.md` with the *real* aggregated
   review comment Bob produced, and update
   `submission/bob-utilization-statement.md`'s bracketed placeholders
   with real session IDs and timings from this run.

## Checklist before submitting
- [ ] Session export file added to `submission/`
- [ ] `bob/sample-review-output.md` replaced with real output (or kept
      alongside it, clearly labeled which is which)
- [ ] Bracketed placeholders in `bob-utilization-statement.md` filled in
- [ ] Video demo (see `demo/video-script.md`) recorded showing this
      session live, not just the final output
