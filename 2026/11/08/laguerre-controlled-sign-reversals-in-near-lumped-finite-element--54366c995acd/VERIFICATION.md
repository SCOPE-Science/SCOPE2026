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

# Verification scope

Run `python verify.py` with Python, NumPy, SciPy, SymPy and mpmath installed. The checked script has been executed from the extracted embedded package and passed 431 finite assertions. Checks include symbolic Laguerre identities, positive polynomial zeros, exact matrix-normalization properties, high-precision endpoint sign comparisons, and a three-node eigenvalue identity. The uniform-on-compact asymptotic and the all-dimension exact positive zero count require the written analytic proof; finite sampling alone cannot verify them. Numerical rounding may obscure tiny far-end entries, which is why the sign comparisons use high-precision arithmetic. No independent audit has been performed.
