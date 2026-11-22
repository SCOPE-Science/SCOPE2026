---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For an n-by-n signless incidence matrix of n pair-sum vertices, the affine coordinate-normal Euclidean scaling is Vol = sqrt(n)|det B|/[2(n-1)!]. De Loera–Sturmfels–Thomas Lemma 2.4 gives |det B|=2^c exactly when each graph component is odd-unicyclic; therefore c<=floor(n/3), maximum 2^floor(n/3). Absolute determinant convex multilinearity extends upper bound to arbitrary points of Δ(2,n). When n=3k, all maximizing graphs are disjoint triangles, and distinct maximum graphs cannot share n-1 columns; equality in signed convex averaging precludes a nonvertex simplex apex. When n=3k+1, a remaining labeled leaf d has arbitrary apex in triangle conv(e_d+e_a,e_d+e_b,e_d+e_c) with constant signed determinant; when n=3k+2, independent free leaves d,f give a four-dimensional product of these triangles. The component graph types and labeled counts follow from 12 four-node triangle-with-leaf structures, 162 five-node structures, and exponential-component multinomial factors; checks include n=3,4,5 boundary cases. Independent exhaustive integer determinants for n=3..6 returned maximum absolute determinant/count (2,1),(2,12),(2,162),(4,10), not a proof for all n.

## originality

PASS

The 1995 De Loera–Sturmfels–Thomas signless-incidence determinant theorem completely covers the nonzero vertex-supported criterion, determinant value and (with immediate multilinearity) numerical maximum volume; those are credited rather than called novel. It does not classify unrestricted equality positions, rigidity iff 3|n, or continuous 2D/4D maximizer families in the material read. Those require new signed determinant equality and one-column exchange arguments. Existing hypersimplex tiling and hyperplane-section work does not imply this optimization equality-locus theorem. Census is a useful derived exact classification rather than separate determinant novelty.

## value

PASS

The exact mod-three phase transition between rigid vertex-supported unrestricted optima and positive-dimensional continuous optimizer families is a natural geometric equality-case question, not just recomputation of a known maximum. It fully classifies vertex-supported optimizer types/counts and gives explicit nonvertex families even though it does not classify every nonvertex maximizer. The structural rigidity proof and moving apex construction are independently useful in polytope extremal geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
