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

An independent exhaustive GP(10,2) recomputation checked all 190 endpoint pairs against all 30 edges, agreeing between shortest-path enumeration/intersection and deletion distances. There are 0 monitoring seven-sets among 77,520 (monotonicity excludes all smaller sets) and 25 monitoring eight-sets among 125,970, with exact equality to optima.json. The induced classes are 5 edgeless and 20 consisting of three disjoint edges plus two isolates. The 300 unordered intersections, indexed 0 through 8, are (30,0,80,60,90,40,0,0,0); the 40 pairs meeting in five are precisely the r=3 exchanges. Each matching-type optimum has two edgeless neighbors and every unordered pair of the five edgeless optima has exactly two such neighbors in common. This proves the doubled-K5 subdivision, not just its degree sequence. Its five degree-eight vertices have eccentricity 3 and the remaining twenty eccentricity 4. The exact private replay is branches/fa87f157-9ce2-425b-a88b-0bd3521d93fb/recompute_dodecahedron.py with --certificate pointing to the assigned optima.json; same-stem .out records the run. Uploaded scripts inspected, not executed. This proves only the specified finite graph and does not extend to movement constrained to original graph edges.

## originality

PASS

Qualified PASS on the simultaneous-exchange geometry, not on the bare minimum or the already overlapping census. The known related threshold with one-at-a-time moves and spare sensors is a different reconfiguration problem.

## value

PASS

A concrete, naturally posed fixed-budget reconfiguration question on a canonical graph has a sharp answer: an isolated optimum landscape for one or two replacements becomes one connected and fully identifiable incidence graph at three. That geometry is not encoded by the census and is a useful exact comparison case for other monitoring reconfiguration models. The count and computations alone would not support generality or establish a practical network migration protocol.

The dated certificate retains the supplied scientific assessment, sources and limitations.
