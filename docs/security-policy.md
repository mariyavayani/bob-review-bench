# TaskFlow Security Policy (v1)

## Secrets management
- No credentials, API keys, tokens, or connection strings may be hardcoded
  in source files, ever — including "temporary" or "just for testing" code.
- All secrets are loaded from environment variables via `os.environ`, never
  committed to the repo.

## Input validation
- Every value taken from `request.json`, `request.args`, or `request.form`
  must be validated (type, presence, and reasonable bounds) before use.
- Never interpolate request data directly into a SQL string. Always use
  parameterized queries (`?` placeholders via sqlite3, not f-strings).

## Database access
- All database access must go through `app/repository.py` (see
  `docs/adr/001-repository-pattern.md`). Files outside `repository.py`
  must not import `sqlite3` directly — this is both an architecture rule
  and a security control, since it's the one place input validation and
  parameterization are enforced consistently.

## Error responses
- Error responses must not leak internal details: no stack traces, no
  SQL fragments, no file paths in any response body returned to a client.
