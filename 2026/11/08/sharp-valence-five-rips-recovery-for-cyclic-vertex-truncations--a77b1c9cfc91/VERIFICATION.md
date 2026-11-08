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

Run `python3 verify.py` with Python 3 and no external packages. The program independently builds the cyclic port graph, computes shortest-path distance-two adjacency, enumerates maximal cliques, reconstructs simplices and exact binary boundary ranks, checks the simplicial projection and its edge-fiber cross adjacency condition, and tests the degree-six six-star obstruction. The recorded output `verification_output.txt` ends with `CYCLIC_TRUNCATION_RIPS2_CHECKS_OK 39 examples` after verifying 39 connected triangle-free input graphs and an independent degree-six counterexample. Finite binary homology alone does not establish torsion-freeness or unrestricted homotopy types; the mathematical proof supplies those conclusions.

# Scope limits

The accepted theorem concerns graph-metric Rips scales one and two for finite connected triangle-free base graphs of maximum valence five, and a single uniform-sharpness witness at valence six. No calculations of higher scales are asserted, and no independent external mathematical validation has been performed.
