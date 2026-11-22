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

Execute `python verify.py` with SymPy. Exact symbolic checks include the sixth-degree dynatomic discriminant, both cubic factors and root permutations, the scalar multiplier products, the three-dimensional Floquet characteristic polynomial, the unit-circle factorization, and the asymptotic prefactors. Eighteen numerical checks additionally compare the Schur criterion to direct spectral roots for three coupling constants. The global root count, hyperbolic-sink equivalence, and asymptotics follow from the written proof, not from finite numerical checks.

The result is for the exact real map with \(0<b<1\), period three, and local linear attraction. Only self-review has been completed; there is no independent validation or certification.
