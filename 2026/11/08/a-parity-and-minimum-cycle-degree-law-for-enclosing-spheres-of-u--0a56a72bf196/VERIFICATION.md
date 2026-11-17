---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The reduction to endpoints is valid by strict convexity and full-dimensional coordinate boxes (t>0); for a chosen signed edge orientation, maximizing independent box signs yields sum_v(|outdeg-indeg|+t)^2. On a bipartite unicyclic graph exactly two all-pure source/sink orientations saturate every coordinate. On an odd cycle at least one cycle vertex is mixed; the single-vertex square loss is >=4(deg(v)+t-1), and a one-defect alternating cycle orientation with attached tree edges consistently oriented realizes equality at any minimum-degree cycle vertex. Equality forces exactly one such defect, giving four distinct contacts per defect, also when defect degree two because the zero-imbalance box sign doubles the two cycle choices. Center 0 follows from antipodal radius equality; diameter endpoints are antipodal contacts. Independently constructed signed-endpoint searches checked C3,C4,C5 and a branched triangle at positive integer t, matching radius and contact counts. The finite search does not prove all unicyclic graphs or real t.

## originality

PASS

The graph-orientation objective is the sum of squared imbalances with separate coordinate boxes; it differs from geometric inradius problems, ordinary graphical-zonotope cones in one extra coordinate, and most-imbalanced orientation min-objective. Primary Glew manuscript introduces the in-in Minkowski realization without this exact enclosing radius/equality-contact classification. No stronger Resultary theorem found covering unicyclic degree-loss formula in this metric. Best-of-knowledge, not certified priority.

## value

PASS

A sharp metric extremal formula for a naturally defined zonotope, with a discrete parity defect and explicit equality geometry, yields exact farthest-vertex and diameter classifications beyond routine scalar radius estimation. The odd cycle minimum-degree statistic connects graph topology with a Euclidean objective; a researcher studying in-in zonotope geometry could use the exact contact set.

The dated certificate retains the supplied scientific assessment, sources and limitations.
