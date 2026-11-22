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

# Reproducibility checks

The mathematical proof uses only the finite first three levels of the definition of one-point-extension rank relative to triangle-free graphs. A nonedge pair has four admissible adjacency signatures and an edge pair has three. Triangle-freeness forces nonadjacency of the common witness with both exclusive witnesses, so the full nonedge pair automatically produces a rank-one edge partner. This argument applies to finite and countable hosts.

Run `python3 checker.py` from a directory containing the extracted package files; there are no dependencies beyond the Python standard library. The checker independently computes rank at most three by the defining pair/singleton recursion, tests the four-profile nonedge characterization, and constructs the entire labelled orbit of fourteen rooted templates. These are compared as exact sets over all 32768 simple six-vertex graphs, 5789 of which are triangle-free. It reports 2292 qualifying labelled graphs and nine isomorphism classes, with exact orbit sizes and automorphism orders. `CENSUS.csv` lists every unlabelled canonical shape and its orbit size.

The census is exhaustive only for six-vertex graphs. General host-size bounds and the finite forbidden induced basis are established by the separate structural proof in `RESULT.md`, not by extrapolating the finite computation. The work has not received independent external validation, and a search-based originality comparison cannot prove priority over all unknown literature.
