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
# Reproducibility and limits

The accompanying `CHECK.py` uses only the Python standard library and exact `fractions.Fraction` arithmetic. Run from the extracted file directory with `python3 CHECK.py`. It reconstructs the exact one-dimensional mass and stiffness blocks, forms tensor products, checks all Walsh eigenvector identities, computes the closed-form maximal frequencies for dimensions one through four, tests anisotropic meshes and exact crossing values, and verifies the 3D cube thresholds. The actual extracted run returned `VERIFY_OK 8751`.

The infinite-dimensional-in-parameter and all-integer-dimension statements are established analytically in `RESULT.md`. A finite set of regression assertions cannot establish universal validity or historical originality. Independent external examination has not taken place.
