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

# Verification evidence

The stand-alone `verify_triangular_graph.py` enumerates all \(\binom n2\) base edges, builds each closed neighborhood as the set of edges sharing at least one endpoint with a center, and directly tests every Boolean trace on every support of size one through four for each integer \(2\le n\le10\). It compares the trace counts to the theorem coefficient formulas. This is computational corroboration; the proof in RESULT.md excludes larger supports for all parameters.

Observed output from the independent run:

```
n 2 |V| 1 coefficients (1, 0, 0, 0, 0)
n 3 |V| 3 coefficients (1, 0, 0, 0, 0)
n 4 |V| 6 coefficients (1, 6, 0, 0, 0)
n 5 |V| 10 coefficients (1, 10, 30, 0, 0)
n 6 |V| 15 coefficients (1, 15, 105, 60, 0)
n 7 |V| 21 coefficients (1, 21, 210, 770, 0)
n 8 |V| 28 coefficients (1, 28, 378, 1960, 2520)
n 9 |V| 36 coefficients (1, 36, 630, 4284, 7560)
n 10 |V| 45 coefficients (1, 45, 990, 8400, 18900)
ALL_TRIANGULAR_CLOSED_NEIGHBORHOOD_CHECKS_PASS 9 graphs 265023 supports
```

The checker uses only the Python standard library. Its finite test is not a replacement for the structural necessity-and-sufficiency proof and does not prove historical novelty.
