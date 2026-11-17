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

# Finite-size critical-layer verification

The independent Python-standard-library program `verify.py` reproduces the defining gamma-function ratio, locates the reference root numerically, computes the log-ratio derivative using a recurrence and Stirling-series digamma approximation, and verifies the excess-kurtosis and sharp-displacement constants. It additionally evaluates the Fourier inversion integral for the *actual finite-dimensional diagonal section density* using two nested composite Simpson rules (positive generalized-Gaussian half-line and nonnegative Fourier variable) with fixed integration cutoffs. It tests dimensions \(n=150,600,1200\) at exponents \(p=p_0-0.2,p_0,p_0+0.02\), checks the \(O(n^{-2})\) residual magnitude, and verifies a sign reversal in the finite-dimensional comparison at \(n=1200\).

Executed command: `python3 verify.py`. Outcome: `ALL NUMERICAL CONSISTENCY CHECKS PASSED`. The observed finite-dimensional approximation remainders times \(n^2\) were about \(-0.0166\) to \(-0.0168\) in the tested cases. The calculation tests arithmetic, normalization and sensitivity, not the universal Fourier asymptotic theorem. Mathematical proof of that asymptotic, including parameter differentiation, is in `RESULT.md`. The numeric root and coefficients are decimal approximations to the exact gamma/digamma expressions; no interval-arithmetic certification or independent expert audit is claimed.
