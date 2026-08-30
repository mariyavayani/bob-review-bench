# Video Demo Script (target: 3–4 minutes)

## 0:00–0:30 — The problem, fast
"On most teams, a PR sits for hours before anyone looks at it, and
whoever finally does is usually strong in one area — style, or security,
or architecture — but rarely all four. We built Bob Review Bench to fix
the *speed and coverage* of that first pass, not to replace the human
reviewer's judgment."

Show on screen: a normal-looking PR (`feature/task-priority-patch`) with
its description (`PR_DESCRIPTION.md`) — looks reasonable, "tested
locally."

## 0:30–1:00 — The seeded issues (so the audience knows what to watch for)
Quickly show the diff (`bob/sample-pr.diff`) and call out, in plain
language, that this PR has five real problems planted in it: a hardcoded
key, a database call that bypasses the team's architecture pattern, no
tests for the new endpoints, a naming/style violation, and (if included)
a performance issue. "A single reviewer skimming this might catch one or
two. Let's see what Bob catches."

## 1:00–1:30 — Document understanding
Show `docs/standards.md`, `docs/security-policy.md`, and
`docs/adr/001-repository-pattern.md` briefly. "These are the team's own
rules — Bob reads these, not generic best practices, to build the actual
review checklist."

## 1:30–2:30 — Agent mode + parallel subagents (the core demo)
Screen-record the live Bob session:
1. Paste `bob/orchestrator-prompt.md` into Bob's Orchestrator mode.
2. Show Bob reading the three governance docs.
3. Show the four subagents dispatching **in parallel** — this is the
   moment to pause and narrate: "these four are running at the same
   time, not one after another — that's what keeps this to minutes
   instead of a sequential checklist."
4. Show each subagent's raw findings briefly.

## 2:30–3:15 — The aggregated result
Show the final review comment Bob produced (the real one, replacing
`bob/sample-review-output.md`). Walk through 2–3 findings out loud,
emphasizing that each one *cites the specific document line* it's based
on — "this isn't a generic lint warning, it's grounded in a document this
team wrote."

## 3:15–3:45 — Impact
Cut to a simple before/after slide or on-screen text:
- Manual first review: hours, one perspective
- Bob Review Bench: [fill in real timing from your session] minutes,
  four perspectives, sourced to the team's own docs
"The human reviewer now reads a short, prioritized, sourced summary
instead of the raw diff — and decides, rather than hunts."

## 3:45–4:00 — Close
"Bob Review Bench: not a faster autocomplete, a faster and more complete
first pass on the slowest step in the SDLC."

---
### Recording checklist
- [ ] Record the actual Bob session live (not narrated over a mockup) —
      this is what makes deliverable #1 and #4 consistent with each other
- [ ] Capture the parallel-subagent moment clearly on screen
- [ ] Show real numbers for the "impact" section, not the placeholder
