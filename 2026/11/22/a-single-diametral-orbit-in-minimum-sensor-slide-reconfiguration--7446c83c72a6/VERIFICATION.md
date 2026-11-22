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

# Reproduction and limits

Run `python3 check_gp.py`, `python3 check_cayley.py`, and `python3 check_symmetry.py` using Python 3.9 or later. They require only the standard library; run from the directory containing the scripts. Machine-readable expected summaries are `gp_output.json`, `cayley_output.json`, and `symmetry_output.json` respectively. Each checker independently recomputes its assertions, so the saved summaries are not the source of correctness.

`check_gp.py` enumerates all 24 singletons, 276 pairs and 2,024 triples, computes the exact power-domination closure, constructs both configuration graphs, verifies their connectivity by complete BFS, and inspects all 165,600 unordered pairs. `check_cayley.py` independently presents the same graph on permutations of four values, verifies its isomorphism with the generalized Petersen model, computes the closure by sequential forcing, and constructs edges by pairwise comparison. `check_symmetry.py` verifies all 144 relabelling-and-coordinate automorphisms and the exact orbit of 72 diametral pairs.

The scripts establish a finite theorem for this exact graph and move model. They do not certify results for other graph sizes or independent external review.
