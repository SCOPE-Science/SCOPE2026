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

# Reproducibility and checks

Run `python verify_building.py --census census.json` with Python 3.9+ (the program uses integer `bit_count` and only the standard library). The run verifies Fano line sets, 168 collineations, polarity involution, all 336 group permutations and incidence preservation. It constructs the complete 336-by-336 group table and inverses, exhaustively enumerates every subgroup of the index-two collineation group, exhaustively adjoins coset elements satisfying the normalizer/square conditions, and checks closure/inverses in all 413 resulting subgroups. It forms and checks all 23 conjugacy classes. It calculates geometric fixed-point subgraphs after edge subdivision for every conjugate subgroup. Fixed-graph component counts and cycle ranks give the claimed five homotopy types and subgroups totals. Compare exact stdout to `verifier_output.txt` and exact generated census to `census.json`.

The proof of exhaustive subgroup coverage is explained in `RESULT.md`: every subgroup of the collineation group has a finite generating chain; all extensions across an index-two group are of the form \(H\sqcup Ht\) with \(tHt^{-1}=H\) and \(t^2\in H\). All original fixed vertices and flag-midpoint fixed vertices are tested by their defining predicates. The comparison with general fixed-subbuilding theory and research limitations are in `RESULT.md` and `REVIEW.md`.

No external or independent mathematical validation is asserted. The complete program and exact census are embedded beside the documentation, without a dependence on another package or unpublished intermediate results.
