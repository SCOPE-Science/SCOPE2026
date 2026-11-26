---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The two valuations and continuous 2-adic interpolation statement in RESULT.md lines 3–15 are proved. The binomial-polynomial values are integral on Z₂ by density, so each series term is divisible by 2^k uniformly. The convergent dilogarithm identity at z=2 gives L=0 via log(−1)=0. The cubic coefficient A is a unit: k=4 contributes −11/3 and the lower valuation bound is at least one for all other nonzero summands. At height h≥4, truncate at k=4h≤2^h; the quadratic-and-higher product remainder has total valuation at least 4h−2≥3h+1, and the tails of the original series, x²L and x³A all vanish modulo 2^(3h+1). Separately reconstructed exact polynomials at heights 2 and 3 reduce after division by 2^(3h) to u²+u³+u⁴ and u³ modulo two, respectively; the latter has odd common denominator 99225. Lucas parity, extended by continuity, justifies the omitted k=5,6 or k=9 terms. Euler's generating-function transformation at z=2 and density give d(−x−1)=−d(x), so the second valuation follows without a separate expansion. Index zero is excluded from the first identity. Replay: independent_check.py and independent_check_output.txt in the bounded reproduction accompanying this review; the frozen artifacts were inspected, not executed. The asserted extension is a valuation for the specified 2-adic function, not an independently verified global analytic-regularity claim.

## originality

FAIL

Both exact valuation arms and their interpolation are covered by distinct indexed exact results, including the proof mechanism of the vanishing dyadic dilogarithm and odd cubic coefficient. Lengyel's original paper only conjectures the exact values; it is not the basis for rejection. Indexed equivalent coverage does not establish historical priority or dependence.

## value

FAIL

Resolving Lengyel's conjectures is a worthwhile arithmetic problem, but the exact resolution and central method are already covered by the indexed results, and the claimed extension to 2-adic indices is immediate from continuity. No distinct new valuation, controlled unit invariant or other independently valuable remainder is established here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
