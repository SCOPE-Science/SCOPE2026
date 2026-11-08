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

# Verification details

Run `python3 verifier.py` with SymPy installed. The recorded run in `verifier_output.txt` checked the expanded Hessian polynomial identity, the cubic discriminant, the quadratic-in-parameter discriminant, the two special factorization identities, projective signed-permutation count, and derivatives ensuring a simple vanishing root at the Fermat parameter. Its last line was `ALL_CHECKS_PASSED`.

The program checks exact algebraic identities but cannot certify on its own that the resulting Galois extension is normal, that the two Kummer classes are independent, or that the local inertia belongs to the stated conjugacy classes. Those steps are proved separately in RESULT.md with irreducibility, valuation and analytic continuation arguments. No independent audit was performed.
