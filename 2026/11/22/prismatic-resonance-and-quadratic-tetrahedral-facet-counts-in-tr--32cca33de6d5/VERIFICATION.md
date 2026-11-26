---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python3 verify_facets.py` with Python 3's standard library. It counts two-edge contacts over the original regular-polygon support inequalities for each integer \(3\le n\le80\). Separately, using the actual cap triangles, it reconstructs the side faces from the horizontal edge normals and tests their vertex counts and degrees. Expected initial lines: `3 two-edge tetrahedra 0 prism 6`, `4 two-edge tetrahedra 12 octahedron 4`; expected final line: `PASS 3 <= n <= 80`. The all-parameter proof is in `RESULT.md`; numerical checks have finite scope and use a tolerance.
