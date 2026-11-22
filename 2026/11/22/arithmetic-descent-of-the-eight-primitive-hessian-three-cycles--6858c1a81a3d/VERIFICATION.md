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

# Reproducible verification

Execute `python verify.py` with `sympy>=1.12` installed. The standalone exact-arithmetic test verifies the degree-27 numerator factorization of the third iterate minus the identity; checks polynomial coprimality, irreducibility modulo five via Rabin's criterion, all three cycle-sum identities, both quadratic discriminants, and the quartic discriminant, resolvent and modulo-seven transposition type.

Successful execution prints `HESSIAN_PERIOD3_EIGHT_CYCLE_DESCENT_VERIFIED`. These exact finite computations support the rigorous characteristic-zero proof in RESULT.md. The proof relies additionally on the standard modular irreducibility criterion, the finite Galois permutation argument, and the mathematical interpretation of cycle-sum invariants. No independent external mathematical validation has been performed, and possible previously published equivalent arithmetic calculations remain a priority limitation.
