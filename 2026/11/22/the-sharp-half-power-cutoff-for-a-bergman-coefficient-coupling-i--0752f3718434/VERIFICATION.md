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

# Verification

The Jacobi reduction uses the exact Bergman moments and is reproduced step by step in `RESULT.md`. The decisive analytic checks are the first correction to the Jacobi tail, the strict AM-GM coefficient comparison for \(s\ge1/2\), the compact-perturbation essential spectrum, and the many-block min-max construction for \(s<1/2\). Every inequality is quantified over all polynomial degrees and every positive exponent.

Run `python check.py` with Python 3, NumPy and SciPy. It tests the exact weight normalization at finitely many indices and provides finite-matrix examples for both spectral regimes. Numerical tests neither establish the asymptotic coefficients uniformly in the index nor certify infinitely many outliers. The proof, not the checker, establishes those claims.

Historical priority is only checked against the listed accessible primary sources; it has not undergone independent audit. No claim is made about all possible other weighted Bergman measures or about explicit subcritical eigenvalue counts.
