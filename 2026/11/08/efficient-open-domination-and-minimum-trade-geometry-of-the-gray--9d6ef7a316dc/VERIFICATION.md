---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The 54-vertex Gray incidence model has 27 points and 27 three-point axis lines; EOD splits independently into an exact point-on-each-line transversal (12 ternary affine Latin graphs of size nine) and nine-line grid tiling (21 choices). Distinct Latin slopes intersect in three points, giving minimum six-point replacements, so point trade graph is K_{3,3,3,3}. The 21 axis tilings consist of three 8-vertex cubes sharing their respective pure tilings; nearest line replacements are three. Their 36-edge glue graph T has eccentricity four and the full code-trade graph is Cartesian product with 252 vertices, 1566 edges, diameter/eccentricity six, and exact distance histogram (1566,4896,8460,9180,6444,1080). Symmetry group S3 wreath S3 of size 1296 splits line pure vs mixed configurations into orbits 36 and 216. No claim about arbitrary trades. The independent checker constructs all 12 codes and all 21 exact line tilings from scratch and recomputes distances.

## originality

PASS

The classical 12 Latin squares and 21 three-dimensional rod tilings are acknowledged known components; the accepted result is the full constrained minimum-trade graph and its global distances/orbit structure, which is not a bare product-count calculation. Earlier Gray graph work supplies automorphism group, and graph-product EOD literature does not classify EOD of this incidence graph.

## value

PASS

Minimum reconfiguration moves, connectivity, diameter and orbit decomposition of all efficient codes are natural discrete optimization and reconfiguration invariants; the exact 252-state structure is a complete and reusable benchmark on a distinguished semisymmetric cubic graph. Its nontrivial trade graph is not a cheap small-instance count because of complete factor characterization and metric.

The dated certificate retains the supplied scientific assessment, sources and limitations.
