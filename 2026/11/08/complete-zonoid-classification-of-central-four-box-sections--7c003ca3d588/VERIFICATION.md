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

# Verification of the four-box classification

The proof is contained in `RESULT.md`, including the key planar cube-section lemma and the borderline cases. The exact rational support check is reproducible with `python3 verify.py`, using the Python standard library only. It checks every nonzero four-entry normal with coordinates from 0 through 5, computes exact rational section vertices, detects genuine two-dimensional facets, and tests whether each facet is centrally symmetric by reflecting its vertex set through its arithmetic mean. Expected classification uses zero coefficients or a maximal coefficient at least the sum of the others.

The executed program reported 1295 coefficient quadruples, of which 730 satisfy the criterion and 565 do not, ending with `FOUR_CUBE_ZONOID_CLASSIFICATION_RATIONAL_CHECKS_PASSED`. These tests are finite sanity checks. The universal proof for all positive real coefficients, and all equality/zero cases, is algebraic and geometric rather than computational.

The exact criterion is invariant under positive coordinate rescalings, so tests on the unit cube also check the formula's correct scaling for rectangular boxes. No independent audit has been conducted.
