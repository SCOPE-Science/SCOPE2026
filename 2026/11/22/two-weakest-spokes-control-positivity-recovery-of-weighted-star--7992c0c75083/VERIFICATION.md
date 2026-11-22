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

The derivation is algebraic: Schur-complement inversion of a finite complex matrix, positivity of its Schur angle, ordering of the leaf angles, and strict monotonicity of the scalar root equation. No finite testing is used to infer an all-weight theorem.

Run `python3 verify.py` with Python 3 and the standard library. In the reviewed candidate the checker printed: `PASS: 70 exact-rational resolvent checks, 300 threshold-bound checks, 17 limiting/equal-weight cases`. Checks cover rational conductances and finite samples, not an exhaustive continuum.

The upper threshold bound is strict for every finite positive weighting with at least three leaves and becomes sharp only in a high-conductance limit. An entrywise-positive matrix is not asserted at \(h=0\); the matrix there is the identity, which is only entrywise nonnegative. Independent mathematical audit has not been performed.
