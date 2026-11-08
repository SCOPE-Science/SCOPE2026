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
# Reproducible verification

Execute `python verify_three_block_cut.py depth6_tree.json` from the directory containing the two files. This checks every edge and witness of the complete depth-six mistake tree, the exact five-star trace count, and the exhaustive seven unordered component profiles for possible six-edge forests. The Python standard library suffices.

Observed output: `THREE_BLOCK_PARTITION_CHECKS_PASS depth=6 leaves=64 queries=63 distinct_queries=8 VC_lower_traces=32 VC_upper_profiles=7`.

Optionally run `python construct_depth6_tree.py` to reconstruct the same certificate by exact dynamic programming; the verifier does not trust the constructor. The count argument for the adaptive upper bound and the graph-forest upper bound for VC are separate mathematical arguments and must not be inferred merely from passing finite tests. Historical priority and independent scientific validation remain unperformed.
