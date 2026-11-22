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

# Verification record

The independent audit has not been performed. The accompanying `verify.py` uses only standard-library Python. It checks 205 fixed positive weight triples, 200 from a reproducible fixed random seed, the closed-form scale against three spherical contact angles, the first derivative of every pair clearance at the extremal scale, and the exact distance between the nonparallel skew witness axes. Successful execution prints `PASS 205 unequal/equal weight triples`.

Analytical proof, not the finite program, establishes the all-weights theorem and the square-root stability bounds. The proof's nonstandard points are the spherical-perimeter equality geometry, stable two-vector Gram inversion, and the skew-line cross-product formula. The constants depend on the weights. Historical priority and correctness have not been independently certified.
