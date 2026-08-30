# Illustrative expected output

> **This file is a mockup**, written by hand to show the *shape* of what
> the orchestrator should produce, so the team knows what "done" looks
> like before running it through Bob. **Replace this file with the real,
> Bob-generated aggregated comment** once you've run
> `bob/orchestrator-prompt.md` in an actual Bob session, and keep this
> version only as a "before" reference in the video/demo if useful.

---

## Bob Review Bench — automated first-pass review
**PR:** `feature/task-priority-patch` → `main`
**Subagents run in parallel:** Style, Security, Test Coverage, Architecture
**Recommendation: Request changes**

### 🔴 Blocking
1. **Hardcoded secret** — `app/app.py`, `BULK_IMPORT_API_KEY`.
   *docs/security-policy.md § Secrets management*: credentials must never
   be hardcoded, even with a "move to env before shipping" TODO. Move to
   `os.environ["BULK_IMPORT_API_KEY"]` before merge.
2. **Database access bypasses the repository layer** —
   `doStuff()` in `app/app.py` opens its own `sqlite3.connect()` and
   builds SQL via string concatenation.
   *docs/adr/001-repository-pattern.md*: all persistence must go through
   `TaskRepository`. This is also a
   *docs/security-policy.md § Input validation* violation — the
   `newPriority` value is concatenated directly into the UPDATE
   statement, which is a SQL injection vector. Add a
   `update_priority(task_id, priority)` method to `TaskRepository` using
   parameterized queries, and call that instead.

### 🟡 Should fix
3. **No test coverage for either new endpoint** —
   `tests/test_app.py` has no cases for `PATCH /tasks/<id>/priority` or
   `PATCH /tasks/bulk-priority`. Needs: valid update, missing/incorrect
   API key (401), unknown task id (404), empty `ids` list. Draft test
   attached separately by the Test Coverage subagent.
4. **Naming and documentation** — `doStuff`, `taskId`, `newPriority` in
   `app/app.py` don't follow *docs/standards.md § Naming*
   (`snake_case`, descriptive verbs). Rename to `update_task_priority`,
   `task_id`, `new_priority`, and add the required one-line docstrings
   to both new routes.

### 🟢 Nit
5. **Response shape inconsistency** — `patch_priority` manually rebuilds
   the task dict field-by-field instead of reusing the shape
   `TaskRepository.get_task()` already returns, per
   *docs/standards.md § Response shape*.

---
*Every finding above cites the specific document and section it's
grounded in — nothing here is a generic lint suggestion. Full subagent
transcripts and the orchestrator's session log are the exported evidence
for this contest submission.*
