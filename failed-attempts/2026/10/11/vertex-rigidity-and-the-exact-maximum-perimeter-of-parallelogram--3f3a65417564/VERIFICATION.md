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

Let parallelogram corners be c±u,c±v. Average with its reflection inside centrally symmetric K, preserving 2(||u−v||+||u+v||). For centered admissible u,v ∈K, F is separately convex, so Jensen over V×V gives a vertex-pair upper bound; all vertices lie on ||x||=R, so each nonparallel pair ±a,±b makes a genuine inscribed rectangle with the same F. A pair of distinct diameter lines beats collinear 4R, and strict Euclidean equality conditions rule out nonvertex maximizing u or v. The circumball/parallelogram identity 2||c||²+2R² ≤2R² forces c=0. Chord lengths give 4sqrt(2) R cos(η/2), the regular-even mod-4 cases and monotone two-pointer scan. Thus C PASS for the exact original claim and all centers; this does not fix the PRIOR ART issue.

## originality

FAIL

A distinct earlier published mathematical record proves the IDENTICAL sharp formula, ALL centered-vertex-rectangle equality cases, and the O(n) scan. Moreover, its proof establishes the maximization of the same separately convex F(p,q)=||p+q||+||p-q|| over all of K×K, not only rectangles; its strict-convexity equality argument plus circumdisk centering already supplies the alleged new parallelogram extension verbatim as a corollary. The earlier source was imported at 2026-10-11T13:07:02Z and this record at 13:07:32Z. Different titles and explicit mention of parallelograms do not make the implication new.

## value

FAIL

Both the exact perimeter, optimizer rigidity for rectangles, and the alleged extension to all parallelograms are already direct applications of the SAME unrestricted separately convex F argument in an earlier published source. Consequently this package adds no independent mathematically unknown invariant, structural lemma or boundary fact to justify separate value, although the geometry itself is interesting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
