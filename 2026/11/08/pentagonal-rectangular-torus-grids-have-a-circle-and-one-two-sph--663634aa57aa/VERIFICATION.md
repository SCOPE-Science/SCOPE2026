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

The proof gives a uniform symbolic classification of faces and links for \(n\ge7\). The finite independent checker `verify_rectangular.py` uses the Python standard library only, constructs graph distances by breadth-first search, enumerates all Rips simplices, verifies every prescribed free-face removal, compares the entire residual face set with the two-column slab union, and checks a standalone 48-pair collapse certificate `local_sphere_collapse.json` against the directly constructed ten-vertex slab. The residual surface has face vector \((6,12,8)\) and four-cycle vertex links. The checker prints per-size PASS statements and a terminal success marker.

The checked second-factor sizes are \(n=7,8,9,10,11,12\). These finite checks support but do not replace the all-parameter proof. The proof does not assert a statement for \(n\le6\), a complete persistence barcode, or an independent external validation.
