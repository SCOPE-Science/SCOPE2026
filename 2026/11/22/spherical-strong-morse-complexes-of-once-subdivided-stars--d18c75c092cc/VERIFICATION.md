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

# Verification

The standalone `verify_spider.py` uses only the Python standard library. It enumerates every vertex order on the once-subdivided star for one to four arms, computes the unique-earlier-neighbor strong matching for each order, and compares the inclusion-maximal generated faces with the full closed-form facet description. It subsequently checks every dominated-vertex deletion for the ranks at least two and verifies that the remaining maximal faces are precisely the full facet set of the cross-polytope boundary. Each comparison and every domination condition is asserted in code.

Replay: `python3 verify_spider.py`. Observed output:

```
n=1 gradients=4 maximal_facets=3
n=2 gradients=16 maximal_facets=6
n=3 gradients=64 maximal_facets=11
n=4 gradients=256 maximal_facets=20
VERIFY_OK: exhaustive vertex orders and dominated-vertex reductions, n=1..4
```

The number of distinct gradients is not the number of filtration orders; every filtration order is visited, and gradients may repeat. Finite checks do not establish the all-rank theorem. The result's argument proves the face decomposition and the strong collapses uniformly for all ranks at least three. The exact integral symmetry action follows from the oriented join cycle, not from numeric rank comparisons. Independent mathematical validation has not been performed.
