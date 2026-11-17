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

## Reproducible checks

`verify_integral_maps.py` calculates exact integer matrices for the homology map from joins of tetrahedral-boundary generators to relative link-cycle generators. It uses SymPy Smith normal form and checks row ranks and nonzero invariant factors for twenty finite configurations. The unique exceptional four-by-four two-block matrix has rank one from rank one to rank two with primitive image.

`verify_finite_homology.py` enumerates every allowed simplex through dimension five for complete bipartite shores of sizes four through six with all permitted numbers of deleted disjoint edge squares. It uses independent bitset Gaussian elimination to obtain reduced mod-two homology. The output records the exact face counts and Betti numbers at each parameter, and its last line is `ROBUST_BICLIQUE_HOMOLOGY_PASS`.

`INTEGRAL_MATRIX_OUTPUT.txt` and `FINITE_HOMOLOGY_OUTPUT.txt` are transcripts of the actual packaged scripts' executions; the scripts are executable with Python 3, and the integer-map script additionally requires SymPy. Numeric checks cover a finite range only. The uniform proof is the signed relative-chain and primitive-splitting argument in `RESULT.md`. The scientific assessments are same-model only. No independent audit was performed.
