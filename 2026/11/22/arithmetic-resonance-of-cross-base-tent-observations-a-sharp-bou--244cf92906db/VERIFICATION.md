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

The centered tent has Fourier cosine coefficient −2/(π²q²) at positive odd q and zero otherwise, by integrating its two linear pieces; the series is absolutely convergent. With A=ga, B=gb, orthogonality requires q=bℓ and q′=aℓ. This is compatible with both frequencies odd exactly when a and b are odd, in which case summing over odd ℓ with the cosine-product integral 1/2 gives 1/(48a²b²). In particular the variance is 1/48. For the cross-sum, the reduced denominator squared is exp(2∑_p |jv_p(m)−kv_p(n)| log p). For independent bases the real prime-exponent vectors cannot be proportional: integer vectors with nonzero proportionality would have rational proportionality and equal positive powers. Their weighted ℓ¹ separation has a strictly positive minimum on j+k=1, so the double series has geometrically small tails in either index; its nonnegative terms include the positive j=k=0 term. For dependent bases write m=t^r,n=t^s with coprime r,s by prime factorization. At d=rj−sk the weight is t^(−2|d|)/48, suppressed for even t unless d=0. Integer solution pairs for a fixed d extend by (s,r); intersecting their parameter intervals with the square gives N/max(r,s)+O_d(1), uniformly bounded above by N/max(r,s)+1. Summable weights justify passage to the limit; their sum is 1 or (t²+1)/(t²−1) depending on parity. As a separate check, at (m,n)=(2,3) only j=0 contributes, giving limit 3/128; at m=n=2 exactly N terms contribute, giving N/48. All claims use the same uniform seed. The supplied exact-integration checker and reproducibility notes were inspected, not executed; they test pair identities on a finite range, not the infinite dichotomy.

## originality

PASS

The supported distinct contribution is the exact long-time shared-seed cross-base covariance classification and its quantitative rates/slopes. The triangle observable and the single-pair Fourier calculation are standard ingredients, not separately credited as a new GCD integral technique. A same-day circular-tent record has the identical tent building block, whereas an earlier resonance record uses a different statistic and independent seeds; neither gives the claimed cross-covariance law.

## value

PASS

The exact shared-seed cross-covariance detects multiplicative dependence even though every marginal is Lebesgue stationary; the even/odd common-base slopes distinguish exact diagonal-only resonance from summable off-diagonals. The classification answers a natural covariance question for expanding maps, with a positive finite independent-base limit rather than a mere upper bound. It does not establish process independence or a joint limit theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
