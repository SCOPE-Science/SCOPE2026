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

The package includes `check_walsh.py`, `check_kasteleyn.py`, and `CERTIFICATE.json` as standalone exact-arithmetic artifacts. Each checker constructs the grid and the Kruskal chord basis without reading the certificate: one enumerates tilings and applies Walsh transforms, the other evaluates an independently constructed signed bipartite determinant at every one of 512 sign choices. Both require 233 zeros, least positive magnitude four, 36 tilings, Parseval \(512\cdot36\), and inverse projection kernel absolute sum 3698. The certificate contains the full 36 distinct projected matching codes and integer multiplicity histograms. No floating-point operations or sample-based extrapolation are used.

These checks establish consistency of the finite result when executed in a compatible Python 3 environment. An external mathematical audit and exhaustive historical priority review have not been performed.
