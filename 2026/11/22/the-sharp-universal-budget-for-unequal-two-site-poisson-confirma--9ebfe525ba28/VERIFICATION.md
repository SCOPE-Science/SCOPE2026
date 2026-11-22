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

# Reproduction and limits

Run the embedded standalone `proof_checks.py` using Python 3 standard libraries only. The checker executes exact rational interval enclosures for the two critical-root signs and the three worked-example objective comparisons, followed by reproducible pseudorandom finite parameter tests of the factorization, derivative and subcritical endpoint-or-balance inequality.

Observed result: `all checks passed: 7205`. The exact-series bounds use the positive exponential Taylor series through term 96 and upper bound its remaining tail by a geometric ratio, using exact `fractions.Fraction` arithmetic. The certified bracket is \(420103/100000<y_*<420104/100000\). At \(p=999/1000\), \(B=41/4\), split \((3,29/4)\) has joint failure strictly below both the concentrated and balanced options by certified rational enclosures.

Finite randomized tests do **not** prove the all-budget theorem. The proof of global optimization, existence of the unique critical root, and the asymptotic balanced regime is analytic in `RESULT.md`. No external or independent validation was performed.
