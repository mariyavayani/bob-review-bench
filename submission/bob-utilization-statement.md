# How IBM Bob Was Utilized

> **Note on this document:** the sections below describe how each Bob
> capability is designed to be used in this solution, with the prompts
> that were actually fed to Bob (`bob/orchestrator-prompt.md` and
> `bob/subagents/*.md`). The bracketed `[ ]` items are placeholders for
> details that only exist once you've run this repo through an actual
> Bob session — session IDs, timings, screenshots — since those can't be
> fabricated. Fill them in from your real run before submitting.

## Agent Mode
Bob's Orchestrator mode drives the end-to-end workflow: it's given the PR
diff and told to (1) read the team's governance documents, (2) derive a
review checklist from them, (3) dispatch specialist subagents, and (4)
aggregate their output into a single artifact. This is not a single
prompt-response — it's Bob managing a multi-step process across several
files and several agents, which is the "beyond code generation" use case
the contest is looking for.

- Orchestrator prompt used: `bob/orchestrator-prompt.md`
- Bob session/task ID(s): `[fill in from your Bob session]`
- Wall-clock time from PR open to final aggregated comment:
  `[fill in — this is the headline metric for the demo]`

## Subagents / Parallel Tasks
Four subagents run concurrently against the same diff, each scoped to a
single governance document so their findings stay grounded and
non-overlapping in responsibility (even though their outputs can overlap
on the same line of code, as with the direct-`sqlite3` call being both a
security and an architecture finding):

| Subagent | Prompt file | Document it's grounded in |
|---|---|---|
| Style | `bob/subagents/style-agent-prompt.md` | `docs/standards.md` |
| Security | `bob/subagents/security-agent-prompt.md` | `docs/security-policy.md` |
| Test Coverage | `bob/subagents/test-coverage-agent-prompt.md` | `tests/test_app.py` |
| Architecture Fit | `bob/subagents/architecture-agent-prompt.md` | `docs/adr/001-repository-pattern.md` |

- Confirmation these ran as genuinely parallel tasks (not sequential) in
  the Bob session: `[fill in / screenshot from session]`
- Any differences between the four subagents' real output and the
  illustrative mockup in `bob/sample-review-output.md`: `[fill in]`

## Document Understanding
Bob ingests three unstructured team documents — `docs/standards.md`,
`docs/security-policy.md`, and `docs/adr/001-repository-pattern.md` — and
uses their actual content (not generic knowledge of "good practice") as
the checklist each subagent is graded against. This is the piece that
makes the review specific to *this* team's stated rules: e.g. the
security subagent flags the hardcoded key by citing the exact clause in
`security-policy.md`, not a generic "don't hardcode secrets" rule.

- Confirm which document formats were tested (this repo ships them as
  Markdown; if you also tested a PDF version of the security policy for
  the document-understanding requirement, note that here):
  `[fill in]`

## Governance / Auditability
Every action Bob took — which documents it read, which subagents it ran,
what each one returned — is captured in Bob's session log. That log is
the exported evidence required for deliverable #4 (see
`submission/EXPORTED_BOB_REPORT.md` for the export and instructions).
