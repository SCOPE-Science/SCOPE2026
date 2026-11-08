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

The standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It enumerates all labelled undirected trees through six vertices using Prüfer codes and all root choices, assigns positive unequal rational vertex masses and heterogeneous asymmetric binary channels, checks every pairwise covariance sign, and recovers the unary-contracted forest from positive-covariance adjacency.

Run `python verify.py` from the directory containing this file and the script. The finite checker supports algebraic boundary and graph-reconstruction identities. The infinite family of all tree sizes and the sampling bound are proved analytically in `RESULT.md`, not certified by finite enumeration. No independent audit has been performed.
