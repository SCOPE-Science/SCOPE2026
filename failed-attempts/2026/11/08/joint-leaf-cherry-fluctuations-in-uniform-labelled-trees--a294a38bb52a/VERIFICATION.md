---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The Prüfer word proves the two leaf moments. Deleting two prescribed leaves of a cherry leaves a uniform shorter tree conditioned on its center being a leaf, so its other leaves are exactly the absent symbols in an (n−4)-draw sample from n−3 eligible labels. This gives A_n and the mixed moment. Distinct centers and leaf pairs give six disjoint labels for n≥5. For n≥7 the two centers cannot attach to each other, so there are (n−6)^(n−6) extensions via a tree on the remaining labels and two choices of attachment vertex; the ordered unequal-pair contribution is B_n. For n=6 the centers attach directly and reproduce the 0^0 convention. The diagonal is A_n, not 2A_n. The stated finite-size lower bound follows from q_n≥e^(−1), a_n≤e^(−1+3/(2n)+1/n²), and n x_n/(1−x_n)≤30/13 for n≥6; at n=5 the bracket is 11/25. Expanding logs to the first order yields the displayed A_n and B_n corrections, covariance bracket 2−4/e, and the three scaled variance/covariance limits. The determinant and correlation simplify as claimed. For the martingale CLT, reattaching i from j to k changes degrees only at j,k. A changed cherry center is among i,j,k or adjacent to an endpoint crossing leaf status; each such endpoint has at most two neighbors across the before/after trees. This gives a size-independent Lipschitz bound. The affected centers are within distance 1 of {j,k} in the original tree; the adjacent degrees needed to evaluate their change lie within distance 2, with the new edge between two already touched vertices. Two endpoint sets at distance at least 5 therefore give additive changes, as required by the published definition. For any nonzero linear combination the variance is asymptotically a positive constant times n, giving the two criterion terms O(n^(−1/2)) and O(n^(−1/4)); Cramér–Wold applies. Independent replay via python /workspace/reproductions/frozen_checks.py (second check) censuses connected edge subsets at n=5,6,7 and matches all five exact moments without Prüfer decoding. The original checker and recorded verification were inspected, not executed; neither finite enumeration proves the CLT.

## originality

FAIL

There is verified broader exact coverage of the advertised mixed moment, covariance, strict sign and limiting off-diagonal entry. Moreover, the full stated joint Gaussian limit and every matrix entry are direct specializations of an explicit joint fringe-subtree theorem, up to bounded root effects. The corrected raw cherry second moment fixes a real printed error, but is the identity E C²=E[C(C−1)]+E C applied to two already evaluated counts. No distinct surviving central claim remains.

## value

FAIL

The natural joint statistic and correction of the printed diagonal are useful exposition. But the submitted contribution adds no independent mixed-moment or fluctuation theorem beyond the stronger exact pendant-star and fringe-tree results. The sole finite correction follows immediately from the earlier distinct-pair count plus the earlier mean; it does not establish a separate mathematical invariant or previously unresolved regime. A standalone note flagging the misprint would be distinct from claiming the frozen joint result as a new finding; no repair is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
