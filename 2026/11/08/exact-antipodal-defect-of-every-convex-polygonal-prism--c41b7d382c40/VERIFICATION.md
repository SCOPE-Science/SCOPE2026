---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS — For P=Q×[-1,1], antipodality of two distinct points is equivalent to their difference lying on ∂((Q−Q)×[-2,2]). Thus every different-layer vertex pair qualifies (n²), and same-layer pairs reduce to n+p(Q) planar antipodal pairs per layer. Rotating support normals count the latter with two additional cross-endpoint pairs for each opposite-parallel edge pair. Edge midpoints split disjointly into horizontal/horizontal opposite layers n², horizontal/horizontal same layer 2p, vertical/vertical n+p, horizontal/vertical 2n+4p; hence B=n²+3n+7p, A=n²+2n+2p, δ=3n−1+5p. Affine invertibility preserves support and midpoint structure. Direct independent integer difference-body hull tests for triangle, generic quadrilateral, trapezoid, rectangle and centrally symmetric hexagon reproduced (n,p,A,B,δ)=(3,0,15,18,8),(4,0,24,28,11),(4,1,26,35,16),(4,2,28,42,21),(6,3,54,75,32). No finite examples replace the rotating-support argument.

## originality

PASS

PASS — The final claim is the separate exact A and B counts and n,p defect formula for all three-dimensional affine polygonal prisms, especially every parallel-edge degeneracy. Phat (June 2026) gives a general defect/homology theorem, exact local facet-opposite formula and cube value 21; its prism proposition 11.16 explicitly assumes d≥4 and concerns the top normal-fan shadow. Its complete primary text does not state the three-dimensional formulas for A,B across all n,p. Standard rotating-calipers count n+p is acknowledged prior. Derived homology rank is not independently novel.

## value

PASS

PASS — A complete geometrically natural polytope family yields both vertex- and edge-midpoint-antipodality incidence spectra, sharp +5 defect per opposite parallel edge pair and integral homology rank from an existing theorem. Nontrivial degeneracy bookkeeping makes it more than a cube-table recomputation; the contribution is family-specific, not a new general homology theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
