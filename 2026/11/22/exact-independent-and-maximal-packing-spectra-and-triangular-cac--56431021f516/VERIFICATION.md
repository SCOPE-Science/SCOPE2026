---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A k-packing has its 2k half-open endpoints strictly increasing in [1,n+1], and consecutive pairing is an inverse; the even binomial part gives the count and degree. Substituting z=-tan^2(theta) gives cos((n+1)theta)/cos(theta)^(n+1), with exactly the asserted degree-many distinct zeros at finite negative z. A packing is maximal iff no vacant vertex is nonadjacent to the entire occupied union: a witness would itself be an addable singleton. Thus end gaps are 0 or 1 and internal gaps 1 or 2, giving t^(2k-1)(1+t)^(k+1)/(1-t)^k and the stated sum. Odd optimum uses all minimal lengths and gaps. For even n, comparing omission labels r<t changes endpoint-list positions r through t-1, hence exactly one paired block iff both labels belong to a common triple (2i-1,2i,2i+1). This proves every edge, not merely connectedness; a chain of m triangles has diameter m, including m=1. Independent interval enumeration for n=1–10 matched both coefficient lists and full labeled optimum edge sets. Frozen source verification reports a separate n<=12 run; its script was inspected, not executed.

## originality

PASS

The supported contribution is the size-refined maximal-packing spectrum together with the exact one-exchange geometry of optimum packings of path blobs. The blob graph, analogous packing reductions, and the maximal totals are covered; no separate novelty is credited for the even-binomial enumerator or its elementary zeros.

## value

PASS

Path bases are a natural benchmark for the blob-graph packing reduction. The bivariate answer distinguishes maximal packing sizes hidden by totals or maximum cardinality, and the full optimum-exchange classification gives an exact parity change, bottleneck vertices, and distances. This substantive content goes beyond the elementary independence count and reproducing a tribonacci sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
