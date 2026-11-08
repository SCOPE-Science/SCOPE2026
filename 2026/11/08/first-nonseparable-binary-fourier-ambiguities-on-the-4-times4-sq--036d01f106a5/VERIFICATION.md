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

Run `python3 CHECK.py`. All operations use exact Python integers, finite tuples, and sets; no floating-point tolerances, solver heuristics, external datasets, or unstated libraries are involved.

The checker reports respectively 1, 6, 135, and 16500 distinct autocorrelation fibers for side lengths 1, 2, 3, and 4; their singleton/double decompositions are (1,0), (6,0), (134,1), and (16488,12). No fiber has cardinality above two. For the two nontrivial side lengths, the rank-one test finds 0 and 8 double fibers consisting entirely of nonseparable masks respectively. The explicit witness is checked under both direct shift sums and an independent coefficient-pair polynomial product.

The proof is exhaustive **only** in the finite prescribed domains; it does not extrapolate to larger side lengths. Scientific self-review passed. Independent mathematical audit and external validation were not performed.
