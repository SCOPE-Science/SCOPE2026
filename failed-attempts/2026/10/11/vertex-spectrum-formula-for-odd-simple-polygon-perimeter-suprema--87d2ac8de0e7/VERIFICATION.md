---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The primary Lángi theorem bounds perim(P) for every simple odd m-gon in convex C by (m−2) longest triangle side plus other two. Define G_m=p+(m−3)d. Pairwise Euclidean distances and their maximum are convex on C³, so max_C³G_m=max_V³G_m. The longest-side back-and-forth construction can be embedded with strictly rising narrow horizontal zigzag strips inside any nondegenerate triangle and converges to G_m, establishing a supremum (not attainment for m>3). Diameter endpoints with an off-line vertex strictly beat any repeated-vertex triple. Finite-affine envelope yields the precise eventual diameter phase; pentagon chord multisets {1,1,φ} and {1,φ,φ} give target 1+(m−1)φ. Independent symbolic φ check and full original source verify normalization. C PASS; implication-level originality is separately rejected.

## originality

FAIL

Lángi’s pre-existing general-convex-body theorem proves the sharp triangle-controlled supremum for every odd side count, with multiple-longest-edge approximants. For polygonal C the claimed finite vertex optimization follows immediately by joint convexity of G_m on C³ and the textbook fact that a convex function on a product polytope achieves a maximum at a vertex. Its finite affine upper envelope, eventual largest-slope diameter phase, and pentagon distance calculation are elementary consequences. This is legitimate and useful specialization but directly implied by stronger prior work plus routine polytope convexity; nonidentical wording is not a new result.

## value

PASS

For a natural convex polygonal container, the complete odd-m perimeter supremum is an exact finite vertex-triple optimization with an eventual diameter-controlled phase; such a formula would be useful for computation and qualitative polygon spectra. The value of the object/invariant is genuine despite the fact that the entire result is a routine corollary of Lángi’s stronger theorem, which separately defeats originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
