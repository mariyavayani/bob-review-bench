# ADR-001: All database access goes through the repository layer

**Status:** Accepted

## Context
Early prototypes of TaskFlow had `sqlite3` calls scattered across route
handlers. This made it hard to reason about input validation, hard to
swap the storage engine later, and made two different endpoints handle
the same query slightly differently (one had a SQL injection bug because
a filter was built with an f-string instead of a parameterized query).

## Decision
All persistence logic lives in `app/repository.py`, inside `TaskRepository`.
Route handlers in `app/app.py` (and any future modules) call methods on
`TaskRepository` — they never open a `sqlite3.connect()` themselves and
never write raw SQL inline.

## Consequences
- New endpoints must add a method to `TaskRepository` rather than querying
  inline, even for "just one quick query."
- Code review should treat any `import sqlite3` outside of
  `app/repository.py` as an architecture violation, not a style nitpick —
  it also re-opens the injection-risk class of bug this ADR exists to
  prevent.
