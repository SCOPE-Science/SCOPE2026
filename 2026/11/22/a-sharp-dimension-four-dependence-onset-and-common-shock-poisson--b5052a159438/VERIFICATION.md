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

The finite checks are reproducible with `python3 checker.py` using the standard Python library. Full orientation enumeration is exhaustive only for dimensions 2 and 3; higher-dimensional exact constraints are checked symbolically using fractions up to dimension 8. The proof for all dimensions and the Poisson limit require the edge-set argument and the Arratia–Goldstein–Gordon process bound in RESULT.md, not finite data. No independently performed validation is claimed.
