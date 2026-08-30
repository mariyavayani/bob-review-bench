# TaskFlow Coding Standards

## Naming
- Functions and variables use `snake_case`. No `camelCase` in Python code.
- Function names must be descriptive verbs (`create_task`, not `doStuff` or `handle`).
- No single-letter variable names outside of short loop counters (`i`, `j`).

## Documentation
- Every route handler must have a one-line docstring describing what it does.
- Non-obvious logic gets an inline comment explaining *why*, not *what*.

## Constants
- No magic numbers or magic strings inline. Define them as named constants
  at the top of the module (e.g. `MAX_TITLE_LENGTH = 200`, not a bare `200`
  buried in a conditional).

## Error handling
- Every route must return a JSON error body with an `error` key on failure,
  matching the pattern already used in `app/app.py`.
- Never let an unhandled exception return a raw 500 with a stack trace to
  the client.

## Response shape
- List endpoints return a JSON array.
- Single-resource endpoints return a JSON object.
- Mutations that don't return a body use `204 No Content`, not `200` with
  an empty body.
