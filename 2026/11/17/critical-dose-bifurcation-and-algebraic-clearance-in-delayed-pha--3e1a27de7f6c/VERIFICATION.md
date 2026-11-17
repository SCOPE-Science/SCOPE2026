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

The included `verify.py` ran with SymPy and returned `VERIFY_OK linear_infected=1 linear_phages=3 scalar_opposite_signs=2`. It checks center eigenvector identities for three arbitrary phages symbolically and two physically admissible scalar examples giving opposite signs of the nonlinear coefficient. The proof of local infinite-dimensional dynamics is mathematical and invokes standard smooth retarded center-manifold/stable-foliation theory; these finite checks do not establish independent certification. No global or zero-coefficient assertions are verified.
