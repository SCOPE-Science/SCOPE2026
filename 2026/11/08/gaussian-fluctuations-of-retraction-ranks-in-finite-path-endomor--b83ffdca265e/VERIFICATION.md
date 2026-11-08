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

The executable `verify.py` performs direct exhaustive enumeration of graph endomorphisms for each integer \(2\le n\le11\), applies the idempotency equation and records all image ranks. It independently computes each candidate rank polynomial by adjacency-walk dynamic programming. The two computations agreed for all ten sizes and the run terminated with `VERIFY_OK`.

Additional exact dynamic-programming calculations of rank histograms for \(n=30\), \(100\), and \(300\) returned mode/mean values \((6,6.60287)\), \((9,10.28334)\), and \((14,15.24143)\), respectively. These observations are not used as proofs of the asymptotic law.

The proof uses an exact path-retraction bijection, the explicit sine eigenbasis of a path adjacency matrix, uniform spectral-remainder estimates, and a one-dimensional Laplace local limit. Those nonfinite arguments, including the tail estimates, are written in `RESULT.md`. No independent mathematical audit has been performed.
