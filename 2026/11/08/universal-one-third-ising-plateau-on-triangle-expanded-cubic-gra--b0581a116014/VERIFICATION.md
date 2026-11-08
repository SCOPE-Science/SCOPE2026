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

# Exact verification
Run `python3 verify.py` in the same directory as this report. The script uses only the standard library and does not access the network.

The proof of the universal statement is analytic (the three attained local lower bounds and equality-preserving interpolation). The checker uses two distinct 12-spin constructions, testing all 4096 binary configurations in the truncated-tetrahedral case. It also exhausts the 4096-state triangle expansion of \(K_4\) and the 262144-state expansions of \(K_{3,3}\) and the triangular prism, comparing exact ground energies at multiple field and coupling values. It additionally computes both critical-state single-flip graphs and verifies their sizes, degree distributions, edge counts, and component counts.

Expected terminating output includes `UNIVERSAL_EXAMPLE_OK tetrahedron_K4`, `UNIVERSAL_EXAMPLE_OK bipartite_K33`, `UNIVERSAL_EXAMPLE_OK triangular_prism`, `TETRAHEDRON_EXACT_OK critical_114_163 flip_components_1_1`, and `ALL_EXACT_CHECKS_OK`. Each printed claim follows executable assertions. No claim of infinite computational certification or independent external scientific review is made.
