# Bob Review Bench

An automated, multi-agent first-pass code review system built on IBM Bob
2.0. Submission for the IBM Dev Day: Bob in Action + Hackathon.

**Workflow targeted:** Code Review

## What's in this repo

```
app/            # TaskFlow — a small Flask REST API (the sample project)
tests/          # existing test suite (baseline coverage)
docs/           # the team's governance docs the subagents check against:
                #   standards.md, security-policy.md, adr/001-*.md
bob/            # prompts to run in IBM Bob (orchestrator + 4 subagents),
                # the seeded PR diff, and an illustrative expected output
demo/           # video demo script
submission/     # the four required written/exported deliverables
PR_DESCRIPTION.md
```

## The two branches
- `main` — clean baseline: working API, repository-pattern data access,
  passing tests, and the governance docs.
- `feature/task-priority-patch` — a PR seeded with five real, planted
  issues (hardcoded secret, architecture violation, missing tests, style
  violations, and an optional performance issue) so a live Bob session
  has something concrete to catch. See `PR_DESCRIPTION.md` and
  `bob/sample-pr.diff`.

## How to run the baseline app
```bash
pip install -r requirements.txt
python -m pytest tests/    # 5 passing tests
python -m app.app          # runs the API on localhost:5000
```

## How to run the actual Bob review
1. Open the repo in IBM Bob (IDE or Bob CLI).
2. Paste `bob/orchestrator-prompt.md` into Orchestrator mode, pointed at
   `feature/task-priority-patch`.
3. Bob reads the three governance docs, dispatches the four subagents in
   `bob/subagents/` in parallel, and produces an aggregated review
   comment — see `bob/sample-review-output.md` for the illustrative shape
   of that output (replace it with the real one once you've run this).
4. Export the session log — see `submission/EXPORTED_BOB_REPORT.md` for
   exactly what's needed and where it goes.

## The four contest deliverables, and where they live here
| # | Deliverable | Where |
|---|---|---|
| 1 | Video demonstration | `demo/video-script.md` (script — record per this, save the final video alongside it) |
| 2 | Problem and solution statement | `submission/problem-and-solution-statement.md` |
| 3 | How Bob was utilized | `submission/bob-utilization-statement.md` |
| 4 | Working code + exported Bob report | This repo + `submission/EXPORTED_BOB_REPORT.md` (instructions + placeholder for the real export) |

## What's real vs. what needs your Bob session
Everything in `app/`, `tests/`, `docs/`, and the seeded PR is real,
working code — you can run the tests yourself right now. What still needs
doing before submission: actually running `bob/orchestrator-prompt.md`
through IBM Bob, exporting that session, and recording the video against
that real run. `submission/EXPORTED_BOB_REPORT.md` has the exact
checklist.
