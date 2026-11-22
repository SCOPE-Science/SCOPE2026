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

# Reproducibility and verification

Run `python verify.py` with Python 3.9+ and `mpmath>=1.3`. The included `verification_output.txt` records the local successful run on the included source file.

The script separately evaluates exact rational integrals of Brownian-bridge covariance for 17 polynomial orders and 16 rational times, and exact integrated variances for 50 orders. At high numerical precision it locates the unique positive interior polynomial root, compares its information score to a dense time grid over 8 orders and 6 noise levels, and checks convergence of the noiseless, vanishing-noise, and fixed-positive-noise limiting formulas. The exact algebraic checks reproduce 322 identities; the supplementary finite comparisons cover over 48,000 design points.

The script **does not establish** root uniqueness for all orders, global optimality beyond its finite tests, or any asymptotic expansion by itself. Their proofs are analytic in RESULT.md. Rounding and finite meshes are not relied upon for certification. No independent review was performed.
