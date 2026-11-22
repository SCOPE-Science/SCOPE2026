---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

All claims here concern the explicit 21-vertex point-line incidence graph of the affine plane of order three. Execute the two included programs as shown in RESULT.md.

- `verify_geometry.py` constructs the 36 unordered omitted-point pairs, independently finds their two residual matchings, checks domination and uniqueness, computes all 2556 optimum-pair intersections, and traverses the 72-state four-exchange graph from every source vertex.
- `verify_all_edge_sets.cpp` starts from a separate explicit coordinate list of the 36 flags, evaluates **every** subset with size from one to seven, and confirms zero feasible sets for sizes one to six and exactly 72 at size seven. It independently checks the four-exchange degree, connectivity and diameter.
- Both programs were executed from the exact embedded sources. Their substantive outputs agree: 72 optimum sets, maximum shared-edge count three between distinct optima, 288 four-exchange edges, degree eight, diameter four. The geometry verifier additionally gives the complete common distance profile \((1,8,32,28,3)\).

The geometric lower bound and two-perfect-matching classification are supplied as a human-readable proof. The distance profile is a bounded exhaustive computation, not an infinite inference. Independent external validation has not been performed.
