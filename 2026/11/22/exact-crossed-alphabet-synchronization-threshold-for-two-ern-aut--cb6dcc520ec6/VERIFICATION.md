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
# Verification

Run `python3 verify_bfs.py` and `python3 verify_structure.py` in the directory containing these files. The full subset-product BFS is exhaustive for each \(n=2,\ldots,9\), and checks no shorter word exists in those **finite** cases. The separate direct-action program tests the formula, explicit witnesses and intermediate image invariants for \(n=2,\ldots,50\), and the exact LCS formula by dynamic programming for \(n=2,\ldots,30\). The captured outputs are `bfs_output.txt` and `structure_output.txt`.

The proof for arbitrary \(n\) is the human-readable trajectory-count, common-subsequence run-skipping and explicit image-invariant argument in `RESULT.md`. Neither test's finite range is used to infer the infinite statement. The underlying general product bounds are cited, but the exact special-family threshold and its proof are self-contained. Independent expert audit has not been performed.
