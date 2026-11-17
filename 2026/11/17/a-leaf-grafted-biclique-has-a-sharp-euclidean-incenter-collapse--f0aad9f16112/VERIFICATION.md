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
Run `python3 verify.py` from this package; it uses only the Python 3 standard library and fails by assertion if a check fails. The exact run recorded:

```
INDEPENDENT_TIGHT_EDGE_INTEGER_VERTEX_ENUMERATION_PASS cases=6 vertices=184
EXACT_MAXIMUM_CONTACTS_AND_CENTER_RANK_PASS profiles=28 vertices=66224 contact_normals=17116
EXACT_PARITY_THRESHOLD_ARITHMETIC_PASS profiles=9044
PENDANT_BICLIQUE_INBALL_ALL_CHECKS_PASS
```

The first routine independently enumerates bounded integer potentials and tests tight-edge spanning connectedness; the second enumerates the classified vertices and computes exact centered squared norms and rational ranks of tangent normals, and the third checks the parity threshold arithmetic in a larger finite window. These are **finite consistency checks**, not a proof of all integer parameters; the arbitrary-parameter argument is in `RESULT.md`. No independent external verification has been performed.
