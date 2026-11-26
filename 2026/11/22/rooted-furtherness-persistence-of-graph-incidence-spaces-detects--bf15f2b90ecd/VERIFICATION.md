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

A graph vertex has a singleton lower set and a graph edge has a three-point lower set. For a vertex root, all other vertices enter at 1 and its incident edges enter at 2, joining exactly d_v isolated vertices to the root component without a cycle. For an edge root the two endpoints with the subdividing point already form a connected path at 0; the other vertices enter at 1. The level-2 double star joins k_e distinct outside vertices, and after taking its root edge and one edge per outside vertex as a tree, the remaining edges are precisely one per common neighbor. This proves the c_e cycle births at 2. All remaining edges enter at 3; graph inclusions inject cycle spaces and introduce nothing in higher dimension, and the full subdivision is connected with cycle rank m-n+1. This gives the claimed ordinary barcodes, also for a single edge, with triangle recovery by summing c_e and dividing by three. Petersen and the pentagonal prism have the same substituted profiles. They differ by existence of a four-cycle; both incidence posets have no beat points and are their own Stong cores. The finite-space nonhomotopy is not a claim of distinct order-complex weak types. Fresh replay on 771 connected labelled graphs (8100 roots) through five vertices and the named pair corroborates these deductions.

## originality

PASS

The distinct contribution is the full degree/common-neighbor barcode formula for arbitrary connected simple graphs and the explicit barcode collision across distinct finite-space cores. The underlying filtration, general H0 principle, complete-graph subcase, Steiner-design collision precedent, and graph-core method are already covered and are not credited as new.

## value

PASS

For a basic family of finite spaces this gives an exact interpretation of what the established filtration sees: all rooted intervals have a simple combinatorial origin, and a degree-one edge-root birth counts local triangles. The named pair shows the complete root-tagged invariant cannot determine the ordinary finite-space core, despite detecting these graph features. That joint classification and limitation is useful beyond a small computation or the known complete-graph substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
