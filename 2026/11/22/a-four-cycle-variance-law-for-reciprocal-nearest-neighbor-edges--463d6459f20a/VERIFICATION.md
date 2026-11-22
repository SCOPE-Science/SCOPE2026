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

# Reproducible checks

Execute `python VERIFY.py` under Python 3 with no third-party packages. This checks the individual and two-edge formulas by exact enumeration of edge-weight orderings for every graph on two, three and four vertices, then on a fixed collection of sparse five- and six-vertex graphs. It also checks exact rational means and variances for paths and cycles of orders 5 through 50 and for complete bipartite graphs, including the four-cycle correction, and verifies two girth-five cubic hosts.

Observed output from the delivered script:
```
VERIFY_OK 11732 assertions
REGULAR_FORMULA_OK 13598 assertions total
```

The proof for arbitrary finite graphs is the conditional two-dimensional integral in RESULT.md. No finite enumeration can certify the universal quantifier independently of that argument. The bibliographic comparison is bounded by the accessible text and leaves an explicit possible-priority risk.
