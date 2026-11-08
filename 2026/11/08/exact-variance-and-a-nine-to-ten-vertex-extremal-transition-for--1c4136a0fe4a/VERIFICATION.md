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

# Verification of exact finite overlap variance

The mathematical proof computes \(H_{ef}=\delta_{i=k}/b+\delta_{j=l}/a-1/(ab)\) by Laplacian eigenspaces; uses the two-edge transfer-current determinant \(p^2-H_{ef}^2\); sums the three classes of unordered edge pairs; and proves the fixed-order maximum by a complete monotonicity argument plus an exact cubic sign comparison. These steps establish all integer graph orders. In particular the finite checker is not a surrogate for an infinite proof.

The accompanying `checker.py` uses an independent combinatorial path: it enumerates every edge subset of the appropriate size, rejects cyclic or disconnected subsets, counts the resulting spanning trees, then computes the edge inclusion and overlap moments by exact `Fraction` arithmetic. For all \(1\le a,b\le4\), it checks the known tree total, individual edge rates, every two-edge rate, overlap mean, and overlap variance. It additionally checks the unique fixed-order maximizing bipartition for \(4\le n\le150\), and strict decreasing variance from the smaller part of size two when \(n\ge10\). This gives **836 exact assertions**, all passing in the packaged run.

To reproduce, run `python3 checker.py`; only the Python standard library is used. Tested calculations do not establish historical priority, and the exact formulas are not claimed for weighted or non-bipartite graphs.
