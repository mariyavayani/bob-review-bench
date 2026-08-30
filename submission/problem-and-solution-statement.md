# Problem and Solution Statement

## The Problem

Code review is the highest-latency, most inconsistent step in most teams'
day-to-day development workflow.

- **First-review latency:** PRs commonly wait 4–24 hours before a human
  reviewer even opens them, because review competes with the reviewer's
  own primary work.
- **No single reviewer has every relevant expertise.** One PR can touch
  style conventions, security, test adequacy, and architecture fit all at
  once — but reviewers are typically strong in one or two of these, not
  all four. Whatever the reviewer happens to be weakest in is where
  issues slip through.
- **Review fatigue leads to skimming, not reading**, especially for large
  or late-in-sprint PRs — so the *deepest* review often happens on the
  PRs that most need one.
- **Late-caught issues are expensive.** A security or architecture issue
  caught in a second review round, or after merge, costs far more to fix
  than the same issue caught before the first review even starts.

The workflow cost isn't the review itself — it's the queueing, the
inconsistency of what gets checked, and the round-trips created when
issues are found late.

## The Solution

**Bob Review Bench** is an automated first-pass review system built on
IBM Bob 2.0 that runs the moment a PR opens, before a human reviewer
looks at it.

An orchestrator agent reads the PR diff alongside the team's own
governance documents — a style guide, a security policy, and an
architecture decision record — and uses those documents to build the
actual review rubric, rather than relying on generic best practices. It
then dispatches four specialist subagents **in parallel** — Style,
Security, Test Coverage, and Architecture Fit — each checking the diff
against only its relevant document. Their findings are aggregated into a
single, severity-ranked review comment where every flag cites the
specific document and rule behind it.

The human reviewer's job changes from "read the whole diff and hope to
catch everything in my area of strength" to "read a short, sourced
summary and make the judgment call." Blocking issues (hardcoded secrets,
architecture violations, missing input validation) are surfaced before
the human ever opens the PR; style nits and test gaps come pre-drafted
where possible.

## Why this matters

This isn't a linter with better copy. It's a demonstration of an AI
system managing a *multi-step workflow* — reading unstructured team
documents, running genuinely parallel specialist analysis, reconciling
overlapping findings, and producing a single trustworthy artifact — which
is the difference between "helps me write code faster" and "changes how
long code review actually takes."
