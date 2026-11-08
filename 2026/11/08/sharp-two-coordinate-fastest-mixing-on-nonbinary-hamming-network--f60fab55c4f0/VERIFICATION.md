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

# Reproducibility

Run the standalone `verify.py` with Python 3, requiring no nonstandard packages. The run in this package passed 2,832 exact-rational spectral instances, 306 complete transition-matrix rows and both exceptional signed spectral dual identities.

The checker implements the explicit Krawtchouk formulas and independently forms full finite transition matrices for \((d,q)=(2,3),(3,3),(3,4),(4,3),(3,5)\). It checks stochasticity, distance-two support when claimed and exact coordinate marginals.

Finite checks do not prove the all-integer claim. The infinite-parameter proof uses convexity of the quadratic distance-two eigenvalue, the endpoint inequality \(d(q-2)\ge2(q-1)\), positivity of \(F(d,q)\) in both stated parameter regions, and spectral trace saturation. These steps are given in `RESULT.md` and have been reconstructed separately.

No independent external mathematical validation has been performed.
