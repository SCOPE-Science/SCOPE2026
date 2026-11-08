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

# Computational consistency checks

Execute `python3 verify.py`. The check uses exact integer and rational arithmetic and reports `VERIFY_OK`. In each integer size from three to eight it tests all toric homogeneous coordinates in every distinguished affine chart: each normalized monomial equals a product of the proposed independent smooth coordinates and one rank-one matrix coordinate, all minors vanish at the exponent-lattice level, and the local lattice rank equals the proved chart dimension. It separately checks the Segre degree identity.

These tests are finite and do not prove the claim for arbitrary numbers of players. The infinite mathematical argument is the explicit general chart isomorphism, the known prime determinantal presentation, and the canonical divisor computation on a Segre cone. There are no unperformed external proofs or computational dependencies in the package. Independent audit has not been performed.
