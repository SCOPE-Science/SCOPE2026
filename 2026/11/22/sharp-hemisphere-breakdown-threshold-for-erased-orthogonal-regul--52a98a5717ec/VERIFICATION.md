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

# Reproducible verification and bounds of the checks

The proof is in `RESULT.md` and does not depend on finite enumeration. To rerun using the standard library, execute `python3 verify.py`. This exhausts all nonempty remaining subsets of regular polygons of sizes 3 through 10, verifies the signed gap minima and the sharp deletion-count thresholds, and exhausts every erasure pattern of sizes 0 through 4 for the nine-site square–pentagon join. It also constructs a deepest-point candidate in four-dimensional Euclidean coordinates and directly evaluates its objective to check equality with the claimed formula for each nondegenerate two-part pattern. All packaged standard-library checks pass.

An optional independent computational route uses NumPy and SciPy (`python3 verify_hulls.py`); it compares the formula with either the closest four-dimensional convex-hull facet or an independently solved constrained minimum Euclidean distance to the surviving hull. This route passed 1,213 full-dimensional cases across \((p,q)=(4,5),(3,5),(5,6),(6,7)\). The exact count table is \((1,0,0),(5,4,0),(5,31,0),(0,84,0),(0,106,20)\), denoting positive, zero, and negative covering cosine, for zero through four erasures respectively. The negative cosine is \(-0.2831584861794965\) and its covering angle is \(106.44880384125517^\circ\).

The optional hull program requires `numpy` and `scipy` installed separately; they are not required for the proof or for the standard-library verifier. The hull computation skips cases in which the surviving convex hull has lower affine dimension; these are settled by the analytic signed-join lemma and included in `verify.py`. Finite experiments cannot prove the universal integer quantifiers, certify originality, or replace an independent mathematical audit. Independent audit status: not performed.
