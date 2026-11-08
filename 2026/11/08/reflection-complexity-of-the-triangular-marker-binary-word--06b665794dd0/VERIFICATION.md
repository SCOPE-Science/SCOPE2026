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

The proof classifies all distinct length-\(n\) factors according to the number of ones and counts exactly those nonpalindromic factors whose reversals also occur. The generating-function simplification establishes the result for all \(n\ge0\).

Run `python3 verify.py` from this directory. The program has no third-party dependencies and reconstructs a sufficient prefix containing every length-\(n\) factor, then checks direct quotient counts, the ordinary complexity, the paired-reversal counts, and the six residue formulas for \(n=0,\ldots,120\) and \(n=150,200,250\). The program reported `PASS: 124 exhaustive finite factor-language tests; n=0..120,150,200,250`.

Finite factor enumeration is not an infinite proof; the general statement depends on the separate all-length factor-classification argument. Independent scientific validation is not performed.
