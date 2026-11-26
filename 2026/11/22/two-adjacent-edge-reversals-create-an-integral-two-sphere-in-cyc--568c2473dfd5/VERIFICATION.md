---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The original transitive faces are exactly the subsets of cyclic blocks of length m+1, by the source-vertex test. Endpoints of a reversed short arc are consecutive in the order of any original face containing them; disjoint adjacent swaps preserve that order's transitivity. A changed triple contains at most one reversed edge. For i→i+1 there is exactly one original cycle containing it, with third vertex i+m+1. A new face must therefore contain one of these two triangles. For τ_0, any fourth vertex v in 2,…,m creates the old directed cycle on {0,v,m+1}, and any in m+2,…,2m creates the old directed cycle on {1,v,m+1}. Neither can be removed by the second disjoint reversal unless that edge is {v,m+1}; only d=m and v=m allow it. Reflection v↦d+1−v reverses all arrows and swaps the roles of the reversed edges, proving the symmetric test. For d=m, the order 1,m+1,0,m verifies the sole new tetrahedron, and no larger face is possible. For the integral attachment argument, the explicit K_s collapses are valid: each length-s endpoint edge has a unique supporting block and the proposed pairs, processed in decreasing size, remove its whole star. In K_m each edge of ∂τ_i is homotopic relative endpoints to its forward segment of lengths 1,m,m in the cyclic polygon, within the corresponding block simplex. The concatenation winds once in K_1. Thus each attaching boundary is a homotopy equivalence to the base circle, the first disk contracts it, and the second disk adds S². In the extremal case the free τ_0–tetrahedron collapse instead leaves a single disk attached to the circle by that equivalence. This also covers m=2 and requires no extrapolation from finite instances.

## originality

PASS

The inspected one-arc results cover a genuine ingredient. Neither they nor the two-reversal classifications starting from a transitive tournament imply the interaction and extremal exception in the cyclic-tournament family.

## value

PASS

This is a natural next interaction question after the single-flip contraction. It gives an exact all-orders threshold: two disk attachments normally create a sphere, but at extremal separation a new common coface cancels it. This distinguishes genuine integral homotopy behavior, not just Euler characteristic or small-instance counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
