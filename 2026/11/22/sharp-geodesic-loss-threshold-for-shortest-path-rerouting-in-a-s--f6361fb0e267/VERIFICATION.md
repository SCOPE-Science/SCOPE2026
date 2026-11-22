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
# Reproducibility and verification

Run `python3 verify.py` from a directory containing the supplied standalone script. The script imports only Python standard-library modules and enumerates labelled permutations and the corresponding monotone paths in the Boolean cube.

The checks reconstruct the admissible one-vertex rerouting graph for each of 28 parameter pairs with \(2\le n\le8\) and \(1\le k<n\). They verify vertex, edge and degree formulas, connectivity, the interior witness length and exact distance six, and Kendall versus graph-distance equality at the two extreme layers through \(n=6\). For all \(n\le6\), another construction independently derives the edges by comparing full cube vertex sequences and omitting exactly one interior vertex, confirming the adjacent-swap interpretation. In the checked instances, no assertion failed.

The script does not enumerate all reconfiguration paths for arbitrary \(n\), does not search all literature, and is not an infinite proof. The result's infinite-parameter correctness rests on the explicit mathematical proof in `RESULT.md`. The separately stated historical-priority risks are not resolved by this computation.
