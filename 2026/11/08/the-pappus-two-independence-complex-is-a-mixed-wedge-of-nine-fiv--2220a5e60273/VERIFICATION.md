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

# Reproducible exact checks

Run `python3 verify_pappus_ind2.py` using Python 3.10 or newer. The verifier requires only the Python standard library and directly builds the graph from its LCF sequence. It uses two admissibility algorithms and confirms identical augmented face sets, all face counts, graph degrees and the complete edge list.

The first vertex-toggle discrete-Morse matching has 10,321 pairs and ten critical cells of dimensions five and six. The second, deterministically reordered matching has 10,320 pairs and twelve critical cells in those dimensions. Both independently undergo full 120,240-incidence Hasse-graph topological-sort acyclicity tests. Two integer gradient algorithms, based respectively on direct unit-pivot elimination and backward projection, agree exactly on both signed Morse boundary matrices.

The first boundary vanishes, and the second has primitive rank one. Exact Euler-characteristic comparison and the five-dimensional Hurewicz isomorphism yield the integral homotopy statement. `verification_output.txt` records a successful complete run terminating `ALL_CHECKS_PASS`. These computations are exhaustive for the stated finite object, not for any unbounded graph class. They have not received independent external validation.
