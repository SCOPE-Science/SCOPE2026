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

# Verification of the finite metric-basis classification

Run `python3 verify_ordered_pairs.py` and `python3 verify_lcf.py` using any ordinary Python 3 interpreter. No nonstandard packages are required. Each run recomputes all claims and terminates only if its integral assertions pass. The two recorded JSON outputs are `check_ordered_pairs.json` and `check_lcf.json`.

The first checker builds the truncated tetrahedral graph from directed edge-corners of a tetrahedron, computes all graph distances with breadth-first searches, and exhausts all ordered pairs, triples, symmetry orbits and bases. It builds the legal jump and slide graphs and performs all-source breadth-first searches on their 156 states. The second constructs the same graph from LCF \([2,6,-2]^4\), provides and verifies a vertex isomorphism with the ordered-edge model, uses integer bitmasks, and computes both ordinary and configuration distances with Floyd–Warshall. These are independent implementations of the enumerative steps, not separate analytic infinite proofs.

Specific checks: 220 triples in 13 symmetry orbits, 156 minimum bases in nine orbits, 1,446 jump edges and 450 slide edges, jump distances equal Johnson lower bounds for all 12,090 unordered distinct pairs, and the complete slide distance/penalty distributions. The latter include 36 pairs at diameter seven and 204 at maximum extra cost four. Failed matroid basis exchange is witnessed by two listed bases and their two unsuccessful replacements.

The finite search proves exact shortest distances because every legal configuration and every legal single-step transition is enumerated and the shortest-path algorithms exhaust the resulting finite graphs. An exhaustive finite calculation does not imply a theorem for larger graphs, and the matching computation outputs do not independently verify historical originality.
