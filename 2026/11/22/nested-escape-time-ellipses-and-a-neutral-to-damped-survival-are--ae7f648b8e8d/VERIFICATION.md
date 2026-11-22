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

# Verification and reproducibility

The main proof is the exact reciprocal-square polar reduction and the positive Gram-matrix argument in RESULT.md. For each fixed positive horizon, direct integration of \(D\), \(C\) and \(H\) yields the exact determinant; no floating-point integration is used to prove the formula. Strict positive definiteness follows because the nonzero trigonometric function \(x_0\sin s+y_0\cos s\) has positive squared integral on every nonempty interval. The finite-time blow-up conclusion uses the polynomial ODE continuation theorem and the explicit reciprocal-square singularity, rather than a numerical escape cutoff.

Run `python3 check_lifetime.py` using Python 3 and its standard library. The script compares explicit Gram entries with independent Simpson integration for five parameter-time pairs, checks determinant identities and positivity, tests the short-time area expansion, verifies normalized damped tails for two parameter values, and checks convergence at six neutral crossover points. It prints `VERIFY_OK: Gram entries, area, small-time, damped tail, crossover` on success.

Finite diagnostics do not certify an all-time theorem. The \(\kappa=0\) case uses its own exact integral rather than a floating-point limiting substitution. Very large horizons require the algebraically stable survival expression in the checker because subtracting two nearly equal ellipse areas loses numerical precision. Independent external review has not occurred.
