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

# Reproducibility and limitations

Run `python3 artifacts/verify.py` with Python 3 and the standard library. The program was executed from the actual package path and reported:

`UNICYCLIC_THIRD_INTRINSIC_CHECKS_PASSED exhaustive_graphs=72192 random_graphs=1300`

The exhaustive finite census covers all labeled connected simple unicyclic graphs of sizes 4, 5, 6, 7; the domain of the theorem begins at size 5. The same script checks expected labeled isomorphism multiplicities of both extremizers, edge-triple identities and Gram determinant types, plus 1,300 seeded larger examples. Finite checks do not establish the theorem for arbitrarily large size: the symbolic graph identities, star bound and exact inequality comparison in RESULT.md do. No separate independent examination has been performed.
