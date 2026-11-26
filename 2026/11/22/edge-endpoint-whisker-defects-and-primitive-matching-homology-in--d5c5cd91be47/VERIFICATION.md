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

An augmented face is a base matching and a subset of the available leaves. On the fiber where no edge other than e covers u or v, toggling e is always legal; otherwise e is absent and the least uncovered leaf-bearing vertex, if any, gives a legal leaf toggle. Both toggles are involutions. A directed Hasse cycle would have constant endpoint-incidence fiber since removing edges cannot increase the indicator. In the first fiber an upward e-toggle cannot be reversed by a downward unmatched e-step. In the second fiber a cycle would have constant base matching (no upward base additions), hence a fixed leaf pivot that likewise cannot be removed. The unpaired faces cover all leaf-bearing vertices and at least one endpoint by an edge different from e. Parity gives exactly all perfect base matchings avoiding e at even order, or the two disjoint one-endpoint-omitting matching sets at odd order. Omitting the empty face restores the extra critical vertex e; the remaining critical faces all have dimension m-1, yielding the asserted wedge also for m=1 or zero additional cells. For the integral map, each perfect matching not using e has a leaf-bearing endpoint on every edge. Joining the corresponding differences of zero-chains gives a reduced cycle with coefficient +1 on its oriented perfect base simplex and 0 on every other perfect base simplex. These simplices are maximal, so their coefficients give cocycles and thus an integral left inverse to the cycles. The ranks from the wedge type make them a basis, with no finite index ambiguity. For full whiskering the least uncovered original vertex can be toggled in each base-matching fiber, giving a point or one sphere per perfect matching; the identical coefficient-pairing argument gives the full integral basis. Hence the inclusion is the coordinate embedding for matchings avoiding e, with the unused coordinates naturally counted by p(H-{u,v}). For cycles these counts are one in even order and two in odd order, from the resulting paths. The argument uses neither connectedness nor bounds on degrees of H.

## originality

PASS

Credit the fully whiskered classification and integral ambient basis to the direct antecedent. Credit the simplicial-vertex machinery for the defect wedge calculation: applying the standard recursion at a leaf edge and iterating already offers a route to the same counts, so the wedge phenomenon and method are not the independent originality basis. The supported distinct result is the exact natural integral coordinate inclusion for this universal two-leaf defect, with its full parity counts specifying the domain. Neither the known ambient basis nor a recursive abstract wedge equivalence gives that inclusion.

## value

PASS

The defect is geometrically canonical: remove the two pendant edges selected by one original edge. For every base graph the absolute topology detects avoiding or near-perfect matchings, and the even-order inclusion measures exactly which classes are missing because the distinguished edge is used. Primitivity supplies integral information not determined by Betti numbers. The cycle examples show an actual parity change rather than only a numerical rank refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
