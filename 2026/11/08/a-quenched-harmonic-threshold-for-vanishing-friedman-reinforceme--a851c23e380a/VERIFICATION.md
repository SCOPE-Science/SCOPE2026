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

Run `python3 check.py` (Python 3 standard library only). Expected output: `PASS: 1950 exact finite-horizon assertions; maximum 6 updates; rational masses and moments.`

The checker independently enumerates all colour-draw histories for five parameter choices and 127 rule strings, checks exact total probability, the first and second moments, then sums over random-rule histories for 15 inhomogeneous schedules. Its rational arithmetic avoids rounding error. It does not numerically establish the infinite-horizon almost-sure claims. The proof's infinite-horizon ingredients are square-summable martingale differences, summation by parts, total variance, and the convergence of independent centered harmonic series.

Limits: no external independent assessment of mathematical correctness or novelty; nondegenerate does not imply a density; no adaptive or unbalanced rules covered.
