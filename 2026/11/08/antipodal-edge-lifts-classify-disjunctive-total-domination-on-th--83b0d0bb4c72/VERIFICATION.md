---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

D=GP(10,2), 20 cubic vertices with exactly 6 distance-two vertices per root. A 3-set covers at most 9 vertices by adjacency, leaving at least 11 needing >=22 distance-two incidences, but only <=18 available. Four-sets q^{-1}(ab) for each of 15 Petersen quotient edges are valid by two-lift path arguments and meet the minimum. Independently enumerated all 4845 4-sets via exact distance-2 DTD predicate: precisely 15 and equal to antipodal edge lifts. Distinct lifts have 0 or 2 vertices in common; 1-exchange graph is edgeless and 2-exchange graph is Petersen line graph, 30 edges and all-vertex eccentricity three. Finite state exhaustion is a full fixed-graph proof.

## originality

PASS

Henning–Naicker complete original paper establishes general DTD definitions and bounds; it neither asserts nor implies the dodecahedral min-set multiplicity nor 2-token line-graph reconfiguration. Prior dodecahedral ordinary total-domination results use adjacency to a selected vertex, not DTD alternative of two distinct distance-two selected vertices. Yi 2015 discusses edge deletion sensitivity, not selection exchanges. A precise same-object Resultary search did not show equivalent lift census.

## value

PASS

The dodecahedral graph is an intrinsic antipodal double cover of Petersen, and the entire minimum DTD configuration space has a geometric 15-edge lift interpretation. The sharp one-versus-two relocation mobility threshold has a natural robustness meaning and identifies the connected line-graph geometry, an exact motivated finite classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
