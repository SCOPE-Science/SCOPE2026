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

# Reproduction and verification limits

Run `python3 verify_exterior_product.py` in a standard Python 3 environment. The script independently builds the original matrix multiplication tables and checks square-zero and anti-commutation equations, computes image and kernel ranks using finite-field elimination, and tests the theorem's exact count formula. Recorded exact output appears in `verification_output.txt`. No third-party packages or precomputed tables are needed.

Test cases include a complete original-equation census of all compatible ordered pairs in dimensions three over \(\mathbb F_3\) and four over \(\mathbb F_2\); fixed-first-matrix tests in dimensions four and five; and small annihilating residual modules. The checks were executed successfully. Tests do not certify the arbitrary-dimensional statement or historical originality. Independent audit remains unperformed.
