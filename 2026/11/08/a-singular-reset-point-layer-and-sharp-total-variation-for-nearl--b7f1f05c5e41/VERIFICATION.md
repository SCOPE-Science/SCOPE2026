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

Execute `python3 verify.py` from this extracted directory. The checker requires only the Python standard library. It tests the finite-Laplace convolution's partial fraction coefficients, normalisation, characteristic function, origin-layer profile, strict finite-scale probability metrics, monotone density ratios and numerically bracketed unique crossing for several values of the contraction factor.

The proof in `RESULT.md` establishes the infinite-product stationary representation, all four singular asymptotic conclusions, and the sharp total-variation coefficient. Finite numerical agreement is a check on formulas, not a proof of uniform convergence or the exact coefficient. Earlier papers establish the fixed-parameter stationary formula, and the present result does not claim independent validation or external certification.
