# Orchestrator prompt (paste into Bob — Orchestrator mode)

You are the review orchestrator for the `bob-review-bench` repo. A pull
request has been opened from `feature/task-priority-patch` into `main`.

## Step 1 — Load context (Document Understanding)
Read and summarize the review rubric implied by these three documents:
- `docs/standards.md`
- `docs/security-policy.md`
- `docs/adr/001-repository-pattern.md`

Produce a short internal checklist from each document before continuing —
this checklist is what each subagent below will be graded against, not
generic best practices.

## Step 2 — Dispatch subagents in parallel
Run the following four subagents concurrently against the diff between
`main` and `feature/task-priority-patch` (see `bob/sample-pr.diff` and/or
`PR_DESCRIPTION.md` for the PR's stated intent). Give each subagent only
its relevant document(s) plus the diff — do not let them see each other's
findings yet.

1. `bob/subagents/style-agent-prompt.md`
2. `bob/subagents/security-agent-prompt.md`
3. `bob/subagents/test-coverage-agent-prompt.md`
4. `bob/subagents/architecture-agent-prompt.md`

## Step 3 — Aggregate
Collect all four subagents' findings and produce a single PR review
comment that:
- Groups findings by severity: **Blocking**, **Should fix**, **Nit**.
- For every finding, cites the specific document and rule it's checked
  against (e.g. "docs/security-policy.md § Secrets management") — no
  finding should be asserted without a source.
- De-duplicates anything two subagents both flagged (e.g. the direct
  `sqlite3` call is both an architecture violation and a security
  concern — say that once, note both angles, don't list it twice).
- Ends with a one-line overall recommendation: approve, approve with
  required changes, or request changes.

## Step 4 — Log
Confirm the full action trail (which documents were read, which
subagents ran, what each returned) is captured in Bob's session log —
this is the artifact to export as the required "IBM Bob report" for the
hackathon submission.
