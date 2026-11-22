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

## Reproduction

Run `python3 verify_q3.py` in the directory containing this file. It requires Python 3.9 or later and no third-party libraries. The script generated `verification_output.json` successfully. It constructs all 12 edges of the labelled Boolean three-cube from the Hamming-one rule, enumerates all 8! placements in two ways, and checks every state distance obtained by each independently implemented breadth-first search.

## Exact checks performed

The verifier asserts 40,320 distinct states and full reachability; the complete layer census `(1,12,90,476,1903,5472,10388,11756,7347,2408,430,36,1)`; a unique identity-centered diameter-twelve placement `(7,6,5,4,3,2,1,0)`; total 20,160 unordered antipodal pairs by vertex transitivity; and exactly `(19064,18088,3144,24)` placements with deficits zero through three beyond the half-total-distance bound. It checks all 40,320 Cantor ranking/unranking roundtrips and all 40,320 matched BFS distances.

## Boundary and limitations

This is exhaustive enumeration of a precisely specified **finite** configuration graph, not an inference from a partial sample. The generic mathematical justification for BFS shortest paths and vertex-transitive relabeling is given in `RESULT.md`. The two traversals share the same mathematical move definition and are not an independent scholarly audit. No statement is asserted for higher-dimensional cubes, other token-swapping rules, or arbitrary target networks. Historical originality remains subject to independent literature review.
