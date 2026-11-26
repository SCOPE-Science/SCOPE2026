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

For at most seven selected vertices, one or two points meet at most four or seven lines, forcing at least nine or six selected lines, and zero points forces all lines. Duality then leaves only (3,3), (3,4), (4,3). Three noncollinear points force four external lines; three collinear points force their common line and three external lines, all through the unselected fourth point, which violates the upper bound. For a triangle the external line forms (1,±1,±1) have no triple concurrence, cover exactly ten points, and meet outside points at most twice. Duality yields exactly the oval configurations, with external lines forced. The four extensions of the coordinate triangle to an oval and the four triangles per oval give 234 of each. For equal-type jumps, the external lines determine the point set as the complement of their union, and the point set in turn determines the lines; no same-side replacement is possible. A cross-type jump must be triangle inclusion, and its line exchange is with the unique oval tangent at the removed point. An independently written exact checker constructs Singer translates in PG(2,3), exhausts both classes of selected vertices through total size seven using mandatory line choices, compares literal one-token adjacency with inclusion, and computes every BFS profile. It finds precisely the two asserted families, 936 edges and the common profile (1,4,12,30,60,96,114,96,47,8); thus connectivity, radius and diameter all follow.

## originality

PASS

The credited oval enumeration and oval-only metric are covered. The distinct claim is the [1,2] minimum-set classification and identification of its two-type reconfiguration graph, with evaluated mixed distances. The old oval graph is a halved graph, not itself the optimizer problem, and its scalar distance profile should not be counted again as new.

## value

PASS

The exact optimizer geometry explains how an outside-only lower and upper neighbor count constrains seven-set exchanges in a natural symmetric incidence graph. The dual geometric classes and their single incidence move are not obtained just by recomputing the old oval metric. The mixed paths and exact diametral layer give useful reconfiguration data; the main value is the connection to the domination optimizers, not a bare table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
