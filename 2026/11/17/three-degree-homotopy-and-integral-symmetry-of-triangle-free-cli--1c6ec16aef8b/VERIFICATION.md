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

# Reproducible scientific checks

Execute `python3 verify_clique_join.py` with Python 3.11 or another recent version of the Python standard library. The source file and the exact resulting stdout are included as `verify_clique_join.py` and `verification_output.txt`. The printed success marker is `TRIANGLE_FREE_CLIQUE_JOIN_EXACT_PASS`.

The checker independently generates graph edges and triangular obstructions; it does not use the displayed face-decomposition formula to select simplices. In six cases, it enumerates all subsets and computes exact reduced boundary ranks over the field of two elements using bitsets; all ranks match the ranks predicted by the integral homotopy theorem. It also calculates signed Lefschetz traces of simplicial vertex-permutation actions on every face, including the reduced empty face, and compares these with the predicted exterior-power character formulas. It checks all 144 automorphisms in the smallest graph and 111 additional automorphisms in the remaining five graphs.

The field-two checks cannot exclude torsion of other prime orders in untested settings. Torsion-freeness for all parameters is proved by the homotopy pushout and free integral join homology argument in `RESULT.md`, not inferred from the checks. The checker does not independently establish the infinite theorem or identify a topological orbit-space homotopy type.
