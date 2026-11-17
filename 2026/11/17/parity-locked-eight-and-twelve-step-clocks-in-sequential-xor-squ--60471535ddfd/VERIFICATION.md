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

# Reproducible checks

Run `python3 verify_matrices.py` and `python3 verify_states.py` from the directory holding the scripts. Both use only the Python standard library and construct the state transition from the stated local update rule. The first checks algebraic base-block identities, nullities, and all powers through the predicted order for \(k=1,\dots,12\). The second independently constructs graph adjacency masks, sequentially updates bits and exhaustively counts all \(74{,}896\) labelled initial states for \(k=1,\dots,5\).

Both programs finished successfully and printed the output preserved in `verification_output.txt`. A finite program cannot prove the all-parameter decomposition; the symbolic coordinate changes, seven-dimensional base matrix, Jordan-rank calculation, and power-count argument appear in `RESULT.md`. Independent mathematical validation has not been performed.
