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

The central mathematical argument classifies each shattered comparison support by at most one outgoing query per earlier position. The all-order polynomial follows by independent counting, without computational assumptions.

For the online part, `depth8_tree.json` gives a complete binary mistake tree of depth eight. The query pairs are zero-indexed. `heap_query_indices` has 255 entries, and children of node index `r` are `2*r+1` (false) and `2*r+2` (true). `verify.py` exhaustively tests the 256 possible binary root-to-leaf paths using independently enumerated length-seven 231-avoiders. It confirms 429 possible hypotheses, making a complete depth-nine tree impossible. Direct sums of avoiding permutations establish the all-order amplification.

Run `python3 verify.py` with both companion files in the same directory. The packaged replay successfully verified the exact shattering support coefficient counts for lengths one through eight and the complete depth-eight certificate. This is a finite certificate plus a separate all-length proof; it is not an external independent audit.

Limitations: historical priority under alternative terminology is not exhaustively settled; the exact online dimension for every permutation length is not asserted.
