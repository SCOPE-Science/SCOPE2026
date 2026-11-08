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

# Reproducibility and limits

Run `python3 verification/verify.py` with Python 3.10 or later. The program requires only the standard library and was executed after extraction into the package workspace. Its observed output was:

```
PASS: 271 exact algebraic, Fourier-generator and transient-ODE checks
```

The exact-rational portion reconstructs the two extremal angular laws at eight first-harmonic values, checks cancellation formulas and endpoint inequalities, verifies the critical three-angle law, and checks a family of rational convex mixtures. A separate characteristic-polynomial calculation verifies that the sixth-order eigenvalue Taylor coefficients solve the finite-mode determinant. Direct positive-eigenvalue root calculations compare to that expansion. An independent time-domain moment hierarchy, integrated with fourth-order Runge–Kutta, checks the opposite sixth-cumulant growth signs and the near-zero critical coefficient.

These are consistency checks; neither finite enumeration nor numerical integrations prove the universal parameter and long-time assertions. The proof of those assertions is contained in `RESULT.md`, including its exact finite-moment closure, the nonnegative-polynomial third-moment bounds, explicit realizing laws and threshold factorization. The program does not claim independent validation or any claim beyond sixth-order projected-displacement cumulants.
