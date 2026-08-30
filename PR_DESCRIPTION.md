# Add task priority patching + bulk priority update

## What
Adds two endpoints so the mobile team can update task priority without a
full PUT:
- `PATCH /tasks/<id>/priority` — update a single task's priority, gated by
  an API key for the bulk-import client.
- `PATCH /tasks/bulk-priority` — update priority for a list of task ids at
  once.

## Why
Mobile team needs a lighter-weight call than the full `PUT /tasks/<id>`
for this one field, and wants a bulk path for their "reprioritize sprint"
feature.

## Testing
Manually tested both endpoints locally against a few task ids. Looks good.

---
*(This PR is a seeded demo artifact for the Bob Review Bench hackathon
submission — it intentionally reproduces the kind of PR that ships under
deadline pressure: works locally, reviewed by eye, and carries a few
issues that don't show up until someone checks it against the team's
actual written standards.)*
