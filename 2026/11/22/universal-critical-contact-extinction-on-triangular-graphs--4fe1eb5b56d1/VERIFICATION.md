---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducible checks

Run `python verification/exact_grouped.py 5 6` with Python 3.10 or later. Each output line gives the order, total weight, number of first-step groups, first-hit histogram (times 0 through 4), and the least base-three state label attaining time four, with the pairs in lexicographic order and the first pair at the least significant digit. For both orders, the exact partition and multiplicities are justified in `RESULT.md`; the integer computation accounts for all labelled initial configurations. The explicit edge-set witnesses in that file can also be checked directly.

The unchanged `verification/direct_forward.cpp` and `verification/functional_graph.cpp` implement ungrouped direct iteration and functional-graph traversal. At orders 5 and 6 they provide alternative ways to reproduce the histograms and maximum depths, respectively. The arbitrary-order recurrent classification cited in `RESULT.md` is background, and no large-order settling-time bound is inferred from the census.
