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

# Finite verification

The `verify_geometry.py` standalone standard-library program generates twelve vertices and thirty edges from two five-cycles, two apex vertices and their cross edges. It checks that all degrees are five, all graph distances and unique antipodal mates are well-defined, and no semitotal dominating set has fewer than three vertices. It evaluates all 220 three-vertex subsets against closed-neighborhood domination and the distance-two witness predicate, finding 60 antipodal triples and 20 all-distance-two triples. It enumerates all legal jump and edge-slide transitions among those 80 states, checks undirected reciprocity and computes shortest paths by breadth-first search from every configuration. It independently tests the exact characterization of all 30 maximum-detour pairs over all 3160 unordered pairs.

The `check_networkx.py` independent implementation uses `networkx.icosahedral_graph()`, NetworkX ego-neighborhoods, shortest-path routines, an independently reconstructed configuration graph, and all automorphisms. It agrees on the 80 feasible states, the 20 and 60 orbit sizes, all edge and degree counts, the all-pairs distance distributions, and the two-slide extremal characterization.

The finite proof is exhaustive for this 12-vertex graph; it makes no claim about larger graphs. The two implementations share the mathematical definitions and expected invariants but use different graph construction and shortest-path code. Both scripts were executed successfully from extracted delivered bytes. External independent audit is not performed.
