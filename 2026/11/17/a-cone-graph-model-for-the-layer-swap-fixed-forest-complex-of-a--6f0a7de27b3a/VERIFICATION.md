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

# Finite verification and mathematical proof boundaries

Run `python3 verify_cone_cover.py` using Python 3 standard library. The program enumerates all labeled simple graphs with one through four vertices and seven additional five-vertex examples, enumerates every union of edge orbits of the layer swap, and compares acyclicity in the double-cover graph with acyclicity in the graph cone. It checks compatibility with every graph automorphism of each tested graph and verifies complete-graph forest face counts.

Recorded output in `verification_cone_output.txt` reports `graphs_checked=82` and `invariant_edge_subsets_checked=49302` and ends with `K_3,K_4,K_5,K_6_cone_f_vectors_checked`.

These finite tests do not establish the universal theorem. The decisive argument is the componentwise two-copy lifting lemma for a forest, together with the fact that two matching bridges in a single lifted tree component create a cycle. The cone-graph test has the identical one-apex-edge-per-component criterion. The ordinary sphere-wedge conclusion additionally uses the published matroid shellability theorem; the verification program does not reprove shellability or perform an independent originality assessment.
