---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The canonical vertices span the affine sum-one hyperplane: a functional constant on all three vertices of each edge must have equal coefficients at its two endpoints, and comparison with the third vertex forces the edge and vertex coefficients equal as well. The connected-subgraph facet theorem exhausts the constraints, including the n spanning paths whose omitted edge contributes coefficient 2. Projecting each normal off the all-ones vector gives the intrinsic Euclidean denominators. Cyclic averaging preserves admissible radius. At (a,...,a,b,...,b), a+b=1/n, the singleton and scattering constraints cross at the claimed R0, and the constant two-vertex constraint gives R2=1/sqrt(n(n−2)). Comparison reduces to n−4 ≤ sqrt(6n−9), with n=3 automatic; the strict integer split is 11/12. For a0 at the crossing or a1=R2(c4−c3), the line of proper-path slacks dominates the secant of c_t through t=3,4, extended to t≥4, and hence lies strictly above R c_t at all later integer t. In the second regime L1(a0)>R2=L1(a1) forces a1>a0, so the scattering constraint is strict. At both centers b≥a>0, and the spanning-path/slack comparison gives M>S, since d_n/sqrt(n/2)<1+2/n. This proves the radius and exact contacts at the specified centers, not at every optimal center. The finite LP script was inspected, not executed or used as proof.

## originality

PASS

The general facet theorem is an essential input, but none of the inspected same-object or general results evaluates the intrinsic Chebyshev radius of a cycle or its strict contact transition. The lower bound requires controlling all the proper and spanning paths beyond the two upper-bound competitors.

## value

PASS

The canonical radius is a natural metric invariant of a standard infinite family. Its exact evaluation shows where the global scattering obstruction gives way to local two-vertex facets, and establishes nρ_n→1. The transition is not a routine tabulation of the known faces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
