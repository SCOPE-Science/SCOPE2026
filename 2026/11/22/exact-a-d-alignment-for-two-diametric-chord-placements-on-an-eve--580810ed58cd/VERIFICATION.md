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

Exact-rational verification: run `python3 check.py` using the standard Python library. The program recomputes Kirchhoff indices from grounded Laplacian inverses and spanning-tree counts from grounded Laplacian determinants, without using the Woodbury formulas in those computations. It checks every distinct relative diameter separation for cycle half-sizes 2 through 9, and checks the two optimizer sets. The universal formulas are proved in RESULT.md; a bounded computation cannot establish an all-size claim. Neither independent review nor priority certification has been performed.
