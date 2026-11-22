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

# Verification

The standalone program `verify_octagon_quotient.py` uses integer bitmasks and exact arithmetic without external packages. It reconstructs the 130 nonempty admissible faces, forms all orbit chains under the 16 rotations/reflections, checks the quotient boundary-square identity in every degree and applies 257 unimodular chain cancellations. The final chain dimensions are `(1,0,0,1,0)` and all differentials vanish. This checks **integral homology**, not simple connectivity or a direct homeomorphism. Simple connectivity instead follows from the fixed-reflection argument and Armstrong's theorem; the homotopy type follows by Hurewicz and Whitehead. The actual checker output ends `OCTAGON_DIHEDRAL_QUOTIENT_INTEGRAL_HOMOLOGY_OK`.

The full literature-priority comparison has not been independently certified. Inaccessible and unindexed publications remain a possible limitation.
