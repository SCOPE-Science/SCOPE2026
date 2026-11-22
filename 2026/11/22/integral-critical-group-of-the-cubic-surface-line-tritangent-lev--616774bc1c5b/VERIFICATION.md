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

Run `python3 tritangent_levi_verify.py`. The checker requires no external packages, iterates over every triple of the 27 explicit divisor classes and confirms exactly 45 anticanonical triples. It constructs the graph Laplacian directly from these incidences, verifies the 27-vertex meeting graph's strongly regular parameters, graph connectivity, and tree count from the symbolic spectrum.

For two choices of deleted Laplacian row/column (vertex 0 or 71), and for both row-major and column-major minimum-valuation pivot searches, it obtains 3-adic valuation counts {0:42,1:10,2:5,3:14} and 5-adic counts {0:65,1:6}; all 71 reduced pivots are 2-adic units. The product of all nonunit elementary divisors agrees exactly with the tree count. Every operation is integral arithmetic modulo a fixed prime power, and no heuristic numerical eigenvalue routine is used.

The test is a reproducible finite computational certificate, not an independent expert audit; the classical blowup-to-line configuration is justified in RESULT.md. The certificate does not address historical priority.
