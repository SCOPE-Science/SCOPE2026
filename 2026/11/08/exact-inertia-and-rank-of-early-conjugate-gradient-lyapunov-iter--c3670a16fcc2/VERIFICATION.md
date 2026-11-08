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

The package includes `verify_inertia.py`, executable with Python 3 and SymPy. It performs rational-arithmetic (not floating-point) CG iterations on finite diagonal positive-definite matrices with nonzero rational factors, checks the exact positive/negative/zero eigenvalue counts via characteristic-polynomial root isolation and checks independent symbolic determinant and sum-kernel identities. It passed 68 assertion groups on the included instances when extracted from the packaged ledger.

The analytic proof in `RESULT.md` is the basis for the all-matrix, all-dimension assertion. Finite samples do not establish an infinite theorem; they test the recurrence, normalization, inertia computation and factorization. Proof coverage assumes exact arithmetic, SPD coefficients, a rank-one positive right-hand side and zero initialization. The comparison with older articles is limited by full-text accessibility for a potentially related 1995 paper; independent mathematical assessment has not been performed.
