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

The mathematical claim, all exact variance values, and the exhaustive finite boundary are reproducible with `python3 verify.py` (standard library only). The program generates every nondecreasing positive partition of total size 2 through 13, evaluates an exact covariance identity with rational arithmetic, and detects a decline followed by a later rise. It tests 259 profiles through 12 species, and 100 profiles at 13 species; only the profile `(1,6,6)` at size 13 is non-unimodal. An independent direct count of survivor subsets verifies the witness at all 14 sample budgets and another 438 small profile-budget combinations.

For the infinite family the checker makes 95 exact sample checks over indices 6 through 100, while the all-index conclusion rests on the explicit analytic positive-polynomial and binomial-growth proof in RESULT.md. The finite experiment is not treated as proof for unbounded family sizes.

The embedded formula counts only idealized functional-group occupancy under uniform sampling without replacement. The first literature source has an accessible abstract but not the full primary text; historical-priority assessment therefore retains this risk. External independent audit has not been performed.
