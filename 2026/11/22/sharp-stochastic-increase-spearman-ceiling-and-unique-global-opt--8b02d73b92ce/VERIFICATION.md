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

Run `python check.py` alongside `RESULT.md` with Python, mpmath, SymPy and SciPy installed. The checker symbolically differentiates the exact uniqueness equation and positive envelope, numerically reproduces the two sharp Spearman values at high precision, cross-checks the envelope at representative admissible shapes, checks conditional-CDF derivative signs, and independently evaluates the one-dimensional maximum by quadrature and constrained optimization. Execution of the embedded checker reported `ALL CHECKS PASSED`.

The infinite-parameter conclusions are proved by the exact signs of the conditional derivative and of \(Q'(s)=s^2(2s^2-1)e^{-s^2}\). Finite numerical diagnostics are independent reproducibility checks, not a proof of continuous global uniqueness. The manuscript identifies every necessary boundary and explains the degenerate independence case at shape zero.

No independent external mathematical audit has been performed. Priority comparisons are based on identified primary material, and unknown or unexamined literature remains a scientific limitation.
