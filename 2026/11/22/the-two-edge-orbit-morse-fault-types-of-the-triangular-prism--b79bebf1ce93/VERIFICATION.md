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

For an unfilled graph, Morse faces are exactly edge forests with a selected root per component and arrows toward that root: outdegree at most one and no repeated edge force any selected undirected cycle to be a directed cycle; conversely a rooted forest meets the incidence and acyclicity rules. I independently generated faces by selecting undirected forests and rooting them, then checked the actual directed Hasse graph of the coordinate matching. For deletion 25 the face vector is (16,98,284,381,180), 959 nonempty faces are visited with 463 pairs and critical counts (1,16,16) in dimensions (0,3,4). For deletion 01 the values are (16,98,286,397,210), 1007, 491 and (1,4,20). Instead of reusing the submitted Morse differential, I computed integral unit pivots on the original simplicial boundary d4: ranks 171 and 194 with no nonunit residual, giving free H4 of ranks 9 and 16. The images of the simplicial d4 are primitive, so H3, a subgroup of C3/im(d4), has no torsion. The matched CW models therefore have d4 of unit ranks 7 and 4 and no other nonzero invariant factors. Their three-skeleta are wedges of S³; Hurewicz determines each four-cell attaching map by its integer degree vector. Unimodular basis changes are wedge homotopy equivalences, so the mapping cones of the unit summands cancel and the zero summands leave exactly the stated wedges. Simultaneous permutation of the three columns and interchange of the two triangles give transitivity within each edge type; edges in a graph triangle cannot be mixed with rungs.

## originality

PASS

The supported distinct claim is the integral two-orbit table for one graph-edge deletion from the triangular prism. The known intact computations, a same-day integral fault table for K_(3,3), the general connectivity bound, and results for strong Morse or ordinary tree families do not cover the two exact types. The possible directed-forest literature overlap is stated with its access and scope limits.

## value

PASS

The six-vertex prism is a natural highly symmetric cubic graph and its two edge orbits give an exhaustive minimal perturbation question. Deletion produces two genuinely different integral homotopy types, with third homology only on the rung fault. This is useful exact fault data beyond intact computations and common connectivity bounds, established by finite certificates plus an integral homotopy argument rather than just mod-two ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
