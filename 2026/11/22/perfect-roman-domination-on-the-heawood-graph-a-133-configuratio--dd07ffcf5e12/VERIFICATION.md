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

The standalone `verify_support.py` checks the Fano-plane incidence construction, exhausts all 16,384 possible sets of vertices labeled two, expands the exact polynomial by binomial coefficients and checks every geometric class of the 133 optimum sets. It returns `PRD_SUPPORT_EXACT_OK`.

`verify_direct.cpp` uses a separate direct ternary-label loop over all 4,782,969 functions and checks the perfect Roman adjacency rule for each zero-labeled vertex, returning `PRD_DIRECT_EXHAUSTIVE_OK`. It independently reproduces all 19 nonzero coefficients and the four optimum-support counts.

The enumeration is exhaustive for this fixed fourteen-vertex graph. It is not a proof for arbitrary incidence graphs or an independent expert audit. No external certification has been performed.
