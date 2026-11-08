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

Both included standard-library programs were executed directly from the checked artifact workspace. `check_matrix.py` calculated exact finite-field matrix powers and Gaussian-elimination nullities for 49 ordered shore pairs and 24 positive time indices each (1,176 comparisons); its identity tests included each claimed global order. `check_direct.py` independently enumerated all 597,051 vertex-pair states over the prime field for three complete bipartite graphs, advancing neighbor sums rather than multiplying a transition matrix. Both programs passed, and their captured outputs are `matrix_output.txt` and `direct_output.txt`.

These finite computations cannot establish the theorem for unbounded shore sizes or extension fields. The proof in RESULT.md derives the relevant invariant factors for all allowed graph sizes and then performs exact fixed-space counting. Its two essential nonstandard checks are the rank-determined nilpotent adjacency partitions and the occurrence of nonscalar size-two Jordan blocks when the shore-size product is one modulo three. The former follows from the first three adjacency powers and their ranks; the latter follows from the nonscalar companion block for each of the two simple nonzero adjacency eigenvalues. No external independent audit was conducted.
