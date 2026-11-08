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
# Reproducibility and limits

Run `python checker.py` using Python 3.9 or newer, with only the standard library. The checker regenerates every distinct edge concept from the vertex-to-edge Boolean map for \(3\le n\le10\), exhaustively tests every edge support, compares the result with cyclic \(111\)-avoidance, calculates the coefficients using marked-zero compositions, and independently computes the exact Littlestone dimension for \(3\le n\le9\) by recursive splitting of finite version spaces.

The expected last line is `CYCLIC_INDUCED_EDGE_SUPPORT_PASS`. The checker was run successfully from its source file. Exact complexity for arbitrary cycle lengths is established by the unrestricted mathematical proof in `RESULT.md`, not by a finite enumeration. In particular, the online value for lengths congruent to two modulo three is not claimed.
