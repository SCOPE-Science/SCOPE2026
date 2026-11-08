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

# Reproducible checks

Run `python3 checker.py` from the package directory. Python 3.9+ standard library is sufficient. The checker calculates exact rational one-coordinate mandatory-edge volumes using all coordinate orders, independently performs signed non-edge inclusion–exclusion for all six connected four-point types, and verifies the stated dimension-one and dimension-two tables. It enumerates every possible labelled four-vertex graph to confirm the complete six-class connected classification. It also validates strict two-dimensional witnesses for the claw and four-cycle, and tests exact positivity for finite dimensions two through nineteen.

Expected output: `FOUR_COMPONENT_ALL_CHECKS_OK: exact inclusion-exclusion, D=1,2, six graph types, strict witnesses`.

The unbounded-dimension identities follow analytically from the inclusion–exclusion formulas; a finite collection of tests alone would not prove them. The joint Poisson convergence follows from the explicitly cited published theorem, not from the checker. Historical originality and all source materials remain subject to independent evaluation.
