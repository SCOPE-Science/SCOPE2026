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

# Reproducibility

Execute the self-contained Python 3 scripts `verify_paths.py` and `verify_pruning.py` in any directory, without parameters or installed dependencies. The expected terminal markers are `VERIFY_PATHS_OK` and `VERIFY_PRUNING_OK`. Both scripts enumerate exactly \(2^{11}=2048\) states and fail on any mismatch against their stated count arrays.

`verify_paths.py` independently constructs the Grötzsch graph by the Mycielski prescription, builds each majority successor with bit masks, traces successor paths and detects cycles, records the entire first-entry-time and eventual-period table and the complete orbit-basin histogram, checks that all 30 last-layer states reach unanimity, and checks the spatial-dihedral plus bit-complement orbit classification.

`verify_pruning.py` starts with a separately entered twenty-edge list, calculates successor bits from signed neighbor majorities, removes all nonperiodic states by iterative indegree-zero pruning, and then labels the reverse-pruned states by recurrent cycle and depth. Its assertions also check the sharp identities \(F^9=F^7\) and \(F^8\ne F^6\). No sampling, stochastic approximations or external data are involved.

This procedure proves the stated claim only on the specified 11-vertex graph; the absence of an external independent review remains a limitation.
