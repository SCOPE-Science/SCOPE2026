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

For a row, the four real projective lines containing its nonzero outcomes have inclusive masses a,a,b,b; all line-event intersections for the full matrix are the all-zero matrix, which is counted four times instead of once. This proves the law, also at p=1. Below 2/3 use b>a² to bound F′/(2m) by −a^(m−1)+a^(2m−2)<0; at 2/3 the derivative is still negative. Above 2/3, b/a increases and the normalized derivative H has H′≥3(1−m/3^(m−1))>0 and diverges at 1, proving the unique interior root. The square case expands to 1−2p²+3p⁴/2. For δ=p_m−2/3, the root equation bounds 3δ by exp(−3(m−1)δ), so mδ²→0. Its logarithm gives x+log x=log m+o(1) with x=3mδ; the derivative of the left side is ≥1, proving x=W(m)+o(1). Then (3a)^m→0 and (3b)^m→1, giving 2·3^(−m) and both comparisons. Independently enumerated all 9^m signed/zero row configurations with rational weights for m=2,3,4 and each of p=1/3,2/3,1; all nine masses matched. The frozen check.py lines 10–86 were inspected, not run; its wider reported finite checks are distinct from the audit proof.

## originality

PASS

The distinct result is the exact signed-ternary law and its unique interior optimum, including the shift from 2/3 and optimized coefficient. Binary rank restoration already exhibits a close two-column Lambert-W mechanism; neither that mechanism in general nor the dense Rademacher endpoint is credited as new. The inspected stronger-looking sources do not give the signed result or entail it by rescaling or changing parameters.

## value

PASS

Fixed dimension two is the first nontrivial exact rank-loss benchmark with competing vanishing-column and proportional-column mechanisms. Optimizing this natural obstruction gives exponential improvement over dense independent signs and a factor of two over plugging in the limiting optimal density. The scale of that difference makes the boundary-layer calculation useful beyond the elementary line count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
