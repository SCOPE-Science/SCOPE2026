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

# Reproducibility and limits

Run `python k5_forest_verify.py` in an environment satisfying `requirements.txt`. The verifier reconstructs all forests on five labeled vertices, all strict nonempty forest flags, the orbit representatives for every dimension and the integer boundary maps. It verifies the chain-complex equations and full Smith diagonals, then builds the complete fundamental-group presentation from quotient two-cells and performs twenty-five generator-eliminating Tietze transformations.

`CHECKS.txt` is the recorded output obtained by executing the exact embedded source. Neither that output alone nor rational ranks alone establish the homotopy statement; the accompanying written proof supplies the no-inversions justification for the orbit-cell structure and the Hurewicz–Whitehead argument. The scope is the ordinary quotient under all five-vertex permutations, not arbitrary matroids or other graph orders. An independent audit remains outstanding.
