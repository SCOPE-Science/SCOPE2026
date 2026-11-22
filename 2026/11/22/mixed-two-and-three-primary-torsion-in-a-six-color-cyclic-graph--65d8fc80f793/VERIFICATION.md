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

Run `python3 verify.py` with Python 3 and no third-party packages. It enumerates the six-color Hom cell poset and all barycentric flag orbits, constructs exact signed boundary matrices, verifies both differential compositions, and performs integer unimodular unit elimination. The terminal marker `HOM_K3_K6_C6_INTEGRAL_HOMOLOGY_OK` was observed on the locally packaged code.

The calculation gives orbit chain-group ranks 351, 3060, 5940, 3240; differential Smith nonzero lists 350 ones, then 2709 ones and one three, then 3229 ones and one two. These determine the claimed integral homology without a floating-point rank approximation. The fundamental-group argument uses the established sphere-wedge connectivity of the original Hom complex and the explicitly enumerated half-turn fixed locus; no computation alone is substituted for that argument.

No independent external mathematical audit has been performed. The computation proves only the specified finite case, and the literature comparison does not establish exhaustive publication priority.
