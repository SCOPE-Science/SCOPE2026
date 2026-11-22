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
The scientific proof is analytic: use facet area-normals, Cauchy's formula, a finite maximum of 18 explicit linear forms, three algebraic squared-norm comparisons, then a certified disjoint-union of spherical caps near the largest brightness. The proof quantifies over every \(a,b,h>0\) and all real thresholds in the reported exact interval.

The packaged `verify.py` uses only standard Python. It constructs all five vertices of the right rectangular pyramid, projects them to a basis of each sampled plane, computes the planar convex hull and its area independently, and compares against the face-normal formula. It reports 14,400 exact-structure comparisons (numeric arithmetic) across twelve representative families, including all boundary multiplicities. It tests that the area maximum agrees with maximizing support-vector norms, that the listed winner sets attain the maximum, and that the spherical cap threshold is strictly submaximal and enforces separation. It is not a formal proof of the continuum claim, which is established in `RESULT.md`, and not an independent external mathematical audit.

The first public date and prior literature comparisons derive from the public arXiv listing and inspected accessible publications. No completeness of historical literature coverage, formal certification, or external independent review is asserted.
