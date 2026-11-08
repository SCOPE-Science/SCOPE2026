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

Run `python checker.py` after installing SymPy. The checker exhausts every simple undirected labelled graph on 2–6 vertices, uses exact connectivity and characteristic-polynomial calculations, compares leading eigenvalues by rigorous rational root isolation and polynomial greatest-common-divisor checks, then classifies exceptional graphs under every vertex permutation. It asserts the reported connected-graph totals and degree-heuristic failure counts, and prints the complete exceptional-class certificate in `COUNTS.json` format.

The verification run produced 1, 4, 38, 728 and 26704 connected labelled graphs at orders 2–6. No max-degree vertex was suboptimal through order 4; 150 labelled graphs at order 5 had at least one suboptimal maximum-degree tie (three isomorphism classes); and 540 labelled graphs at order 6 had no optimal maximum-degree vertex (two classes). Actual computations cover only these orders. The habitat-corridor adjacency model is a stylized spectral-capacity proxy and is not a stochastic population-persistence probability. Historical priority has not been independently checked.
