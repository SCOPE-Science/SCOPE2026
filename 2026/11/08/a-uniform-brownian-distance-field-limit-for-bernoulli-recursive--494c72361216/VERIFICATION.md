---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The finite checker `check.py` was executed as `python3 check.py`. It passed 708,747 assertions, comprising 708,743 deterministic exhaustive/exact arithmetic checks and four seeded Monte Carlo tolerance checks. The enumerated graph configurations use all independent parent-choice patterns for through vertex index 13 (12 added vertices after the initial edge); these tests do not prove any asymptotic limit.

The critical infinite statements are supported instead by the full proof in `RESULT.md`: exact bounded-martingale decomposition, predictable quadratic-variation limit and functional martingale CLT; universal last-success ancestry bound; logarithmic maximum-failure-run estimate by union bound and Borel--Cantelli; uniform transfer to all tree distances; and a Brownian stochastic-integral calculation for the pairwise-mean variance.

The primary 2026 motivating paper was read in full as text, including statements, trunk/branch structure, longest-run discussion, and references. Related primary theorem statements and model definitions were compared. Historical-priority uncertainty and the absence of an independent external audit remain.
