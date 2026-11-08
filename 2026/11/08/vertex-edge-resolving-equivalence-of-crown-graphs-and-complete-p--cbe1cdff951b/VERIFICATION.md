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

## Reproducibility

Run `python3 verify_crown_prism61.py` with Python 3 (standard library only). The program uses graph-distance matrices obtained by all-pairs shortest-path relaxation, not by assuming the theorem's distance formulas. For crown graphs with \(n=3,4,5,6\) it checks vertex and edge resolving feasibility **for every subset** and verifies their equality subset-by-subset. For \(n=4,5,6\) it independently checks vertex resolution of \(K_2\square K_n\) on the same selected subsets. It verifies the polynomial coefficients and inclusion-minimal sizes, and uses BFS to calculate TAR components directly for \(n=4,5\) at the three budgets adjacent to the connectivity threshold.

The observed result was:
`VERIFY_OK orders=3..6 subsets=5440 crown_resolving=3078 crown_prism_equivalence_n4..6=PASS all_edge_metric_sets=PASS polynomial_and_bases=PASS TAR_n4..5=PASS`.

The proof in RESULT.md, not the finite check, establishes the assertions for every permitted integer order. Previously known minimum metric dimensions are contextual rather than separately new. Independent verification remains unperformed.
