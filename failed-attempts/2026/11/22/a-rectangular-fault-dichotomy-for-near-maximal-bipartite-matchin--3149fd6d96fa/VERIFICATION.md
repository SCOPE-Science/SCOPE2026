---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

In the surviving bipartite graph the only vertices that can exceed selected degree n-1 are intact vertices, and then only by their full n-edge stars. A surviving edge in the bounding fault rectangle is in no such star, so it is a cone point. If the rectangle is full and proper, the intact stars cover the ground set E of surviving edges, and selecting one edge from each intact star into a faulted vertex of the other class gives distinct private representatives. Put Q equal to E minus those chosen representatives. For each q in Q at any stage, a forbidden set containing q loses its constraint on deletion, and its private representative is a cone point there. Link formation replaces every forbidden set by that set minus q, leaving its private representative in place and still covering the remaining Q. Both star and deletion are contractible, so the gluing gives a suspension; at the last vertex the link consists only of the empty face and there are two contractible components. Here |Q|>=1 since there is an intact star of size n>=2 and exactly one chosen representative belongs to it. This yields S^(|E|-t-1), t=2n-|R|-|C|, and both displayed dimension forms follow. RESULT.md, VERIFICATION.md and verify_rectangular.py were inspected without execution. The finite mod-two checks were not used to infer integral homotopy.

## originality

FAIL

The exact indexed graph formulation appeared only as the frozen record itself, and the closest graph-specific results are different. But the operative spherical-case lemma is a direct corollary of the prior hypergraph star-cluster theorem (Jinha Kim, arXiv:2408.14321v2, Theorem 1.2). Specialization at a private vertex gives the full suspension count, not merely a one-step existence statement. The remaining reduction to that lemma and to the isolated-vertex cone criterion is the immediate intact-star description. This is mathematical coverage by a stronger result, not a rejection based on scope similarity, access failure or catalogue nonreturn.

## value

PASS

As a mathematical classification, the partition into cones and homotopy spheres for all nonempty proper deletions is useful: equal-size faults can have opposite outcomes, and the dimension depends explicitly on two geometric fault extents. This gives a natural diagnostic for instability of the intact topology. That utility does not make the covered specialization an original finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
