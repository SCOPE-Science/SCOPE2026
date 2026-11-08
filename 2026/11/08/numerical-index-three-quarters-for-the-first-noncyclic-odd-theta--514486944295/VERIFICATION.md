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

Run `python verify_theta.py theta_certificate.json` using Python 3 standard library only. The checker explicitly enumerates all 54 extreme rooted Lipschitz potentials, 78 nontrivial edge/vertex convex decompositions with 334 exact rational coefficients, verifies all 7 face sizes and the sharp rank-one witness. The successful output begins `THETA_INDEX_EXACT_OK` and ends `norm 4 radius 3 index 3/4`.

All calculations use integer and rational arithmetic. The proof that these exact finite checks exhaust all real operators is the polytope and support-function reduction provided in RESULT.md. The certificate does not establish originality or independence and has not undergone independent audit.
