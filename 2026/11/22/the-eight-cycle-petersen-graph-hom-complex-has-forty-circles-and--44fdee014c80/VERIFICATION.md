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

# Verification of the hexagon components

Run `python3 verify_hexagon_triangles.py` (standard library only) and compare with `expected.txt`. It enumerates the Kneser graph's rooted hexagons and constructs the triangles and their incidences by the insertion formula. It checks the intersection paths close to 24-cycles, that every recoloring from the constructed maps stays within the corresponding component, and that multiple mutable sites are always adjacent. The proof in `RESULT.md` uses square-freeness to exclude cells varying at multiple adjacent sites. The verification concerns ordinary graph-Hom cells for the specified graphs, not an all-length homotopy classification.
