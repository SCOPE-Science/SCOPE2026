---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a nonempty set of at most three landmarks, two sign-matrix columns coincide up to negation; the empty set also cannot resolve. In a normalized four-set a distance-four pair forces zero on the remaining coordinate and zero sum on the first four. Repeated binary signatures on those coordinates give a difference witness; if all signatures are distinct, assign +1 to 00 and 11, and −1 to 01 and 10 (the checkerboard). The remaining distance-two case reduces to a triangle, which has a ternary witness on unused coordinates, or a star, for which the remaining coordinate must be twice the center, forcing a zero ternary kernel. The star determines its pentad already from three members. For the jump metric, each common class with a sign mismatch must have its target sign inserted, as must a class in the target support absent initially when omissions differ; a move inserts only one sign. Flips followed by at most one exchange attain that bound. The resulting distance histogram and the legal Hamming replacement lengths 2, 3 and 5 give the claimed radius, diameter and edgeless slide graph.

## originality

FAIL

The strongest distinct indexed result gives the complete Clebsch basis classification and both exchange graphs, not merely the value of metric dimension. The purported additional cube classification is equivalent by a direct parity argument: quotient distance is min(d,5−d); for the even representatives, d is even, so this minimum recovers d uniquely (0→0, 1→4, 2→2). Thus a nonresolving projected set supplies an unresolved pair of even representatives in the cube; using arbitrary antipodal landmark signs does not change equality. If the projected set resolves, unequal classes are distinguished upstairs, and two vertices in one class have distances summing to five, hence unequal, to every landmark. Therefore the complete projected census gives exactly all lifts. A slide projects to a Clebsch slide because adjacent cube vertices are in different classes, so Clebsch slide isolation implies cube slide isolation. Jumps lift by retaining all signs on shared landmarks and assigning either sign to the incoming one, or flipping one sign within a support. The exact signed distances and enumerations are direct calculations in this forced lift of 16K5. This is demonstrable equivalent coverage and routine consequences, not an assertion of ordering between the two same-day results.

## value

FAIL

The cube optimum-mobility question is natural, but this exact finite case reduces by parity to the already classified folded case. Slide isolation is inherited and not a separate boundary theorem. The signed census, jump graph and distance profile are mechanically forced by the lifted four-of-five support moves; no independent nonmechanical remainder is established by the frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
