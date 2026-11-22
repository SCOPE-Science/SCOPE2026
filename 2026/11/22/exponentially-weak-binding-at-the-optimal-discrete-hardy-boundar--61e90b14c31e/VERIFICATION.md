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

The proof's exact dependencies are the ground-state identity, the massive-capacity upper and lower estimates, the finite-support Rayleigh limit, and the codimension-one min–max bound. All are stated and proved in `RESULT.md`.

`CHECKER.py` independently evaluates finite versions of the ground-state identity and finite Jacobi spectral comparisons, and prints diagnostic weak-coupling trends. These checks do not establish the infinite limit. The analytical proof is the evidence for the claimed asymptotic and uniqueness. The results have not undergone independent mathematical validation.
