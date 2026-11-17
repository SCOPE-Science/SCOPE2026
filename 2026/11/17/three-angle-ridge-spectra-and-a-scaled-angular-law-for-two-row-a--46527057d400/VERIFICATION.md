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

Use Python 3 and run `python checks/verify_angles.py`. The script has no external packages. Its exact integer/rational computations enumerate all \(n(n-1)\) vertices and all \(\binom{3n}{2}\) distinct pairs of the three facet families, and independently find the affine dimension of the exposed intersection through rational row reduction. For every genuine ridge it verifies the cosine sign and square from the intrinsic projected normals. The checks cover every integer \(n\) between three and eight, inclusive, and terminate with the line `TWO_ROW_FIXED_RANK_RIDGE_EXACT_PASS`.

The universal results rely on explicit strict facet-intersection witnesses and all-pair exclusions, followed by exact normal products and elementary trigonometric/asymptotic identities, as written in `RESULT.md`. The finite verifier is not an exhaustive check of the infinite family. All numerical experiments and other independence or external validation claims are intentionally absent.
