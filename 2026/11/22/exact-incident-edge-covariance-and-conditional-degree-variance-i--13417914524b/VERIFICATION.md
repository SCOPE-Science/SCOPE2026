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

# Reproduction and proof boundaries

The `checker.py` program (Python standard library only) is standalone. Execute from a directory containing it with `python checker.py`.

The test performs exact `fractions.Fraction` calculations of the displayed joint probability against complete permutations of relevant independent ranks for all admissible abstract pairs of blocker sets on three through seven labels. It additionally evaluates exact-rank probabilities for 16 seeded randomly sampled generic Voronoi site configurations at each size four through eight, and the full degree-variance formula versus exhaustive ranks on 12 configurations for each size three through seven. Seeded floating-point geometry is used only in these supplemental checks.

Most importantly, the two signed-covariance witnesses use **exact rational Voronoi segment-cell intersections**, exact general-position determinant checks, and exact rational probability arithmetic. These tests were run on the provided `checker.py`, with the final output reporting all checks passed.

The proof for all finite site sets does not depend on these finite enumerations; it depends on the uniform-rank reduction, a three-variable integral, a complete partition of its integration domain, and a two-variable nested integral for endpoint obstruction. It does not establish unconditioned randomness over sample locations, infinite-volume scaling, or correlated-height results. Independent audit has not been performed.
