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

Execute `python verify.py` with Python 3, NumPy and SciPy. The standalone program checks Gaussian maximum density normalization, the exact two-sample maximum moments and associated Poisson correlation, the finite-population correlation formula, the strict clock envelope and its optimal/diffuse examples, Gaussian extreme asymptotics, the Gumbel-to-logistic reduction, and exact positive-scale cancellation. Its recorded outcome is **PASS: 83 deterministic assertions**. Replaying the embedded file is required to verify the checks at the receiving environment.

The analytic proof in `RESULT.md` supplies the infinite-population statements. Finite quadrature and fixed-seed sampling do not prove convergence, originality or independent validation. Numerical Gaussian asymptotics converge slowly; the checker tests a sequence at progressively larger population sizes rather than treating a single finite value as the limit.
