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

# Reproducibility

Run `python verify.py` with Python 3 and the `sympy` and `mpmath` packages installed. The checker should print `VERIFY_OK determinant_identity=1 cubic_contact=1 three_physical_preimages=1` and the three preimages, their common image, and the exact fold threshold in a representative physical parameter regime.

The symbolic checks reconstruct the factored Jacobian determinant and verify the coefficient of the cubic contact at the critical learning rate. The 75-digit numerical check confirms one triple-preimage witness at parameters disclosed in the result. Neither a finite test nor this program alone proves the theorem for all real parameters. The proof is given in `RESULT.md`; uniqueness of the positive root in the triple-preimage construction and the monotonicity arguments are analytical.

Independent scientific audit has not been performed. No external certificate is claimed.
