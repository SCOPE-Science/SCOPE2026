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

Reviewed RESULT.md:5–39, VERIFICATION.md and check_derangement_first_zero.py. The unnormalized real/complex convolution multipliers are sums of d_n signs. The simultaneous-label symmetry and exactly n edges per derangement give each allowed edge marginal 1/(n−1); averaging (−1)^t >= 1−2t gives the claimed signed lower bound, with equality exactly when no two selected edges co-occur. For n>=4 two allowed edges in distinct rows and columns extend to a derangement: the residual square board has at least two rows, each missing at most one distinct column, so Hall holds for singletons and for sets of two or more rows. Hence equality is equivalent to being a star, with unique center for k>=2. The count for k>=2 is in the n>=4 star-characterization clause (as in the proof and limitations); it is not valid for n=3, k=2, where there are 9 minimizers, not 6. Repeating the n>=4 qualifier in the count sentence would remove ambiguity. The even-n nonvanishing follows from odd derangement count by the recurrence, including n=2. At odd n, only off-diagonal size >=(n−1)/2 can cancel, and stars exactly reach zero there. Diagonal support cannot occur at minimum full weight. The first layer at n=3 has six singletons. Independent replay: python3 /workspace/branches/replay_frozen_review.py 5 used a sign-product expansion and inclusion–exclusion on residual diagonals. Exhaustive layers: 0..2 at n=3, 0..3 at n=4,6,7, 0..4 at n=5. The odd first-zero layers have 6, 60 and 280 zeros, respectively. These finite checks corroborate the proof, rather than establish the infinite claim.

## originality

PASS

Credit prior unsigned derangement counts, pair extendibility, the fixed order-five absolute spectrum, and close cancellation results for other incidence families. The supported distinct result is the all-order signed weight minimum through row length, its exact equality geometry, and the resulting first-zero layer within the off-diagonal perfect-matching family. No compared source states a stronger result having that conclusion as a specialization.

## value

PASS

The minimum weight of a Fourier zero measures precisely the first degree at which this natural incidence codebook loses information under convolution. The signed envelope goes beyond detecting singularity: it determines the worst multiplier at each sparse weight up to a full row and exactly identifies all most vulnerable supports. The order-variable equality classification, rather than an isolated spectrum table or the parity check, gives this result its value. Higher-weight nullity and quantitative recovery norms do not follow.

The dated certificate retains the supplied scientific assessment, sources and limitations.
