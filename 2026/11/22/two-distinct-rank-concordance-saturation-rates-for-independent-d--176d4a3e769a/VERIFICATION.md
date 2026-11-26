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

Orientation reverses both coefficients by the factor sigma, and the all-lag no-zero-sum condition eliminates all ties simultaneously. I reconstructed the Spearman constant without the cited occupation identity. For one positively oriented walk with ranks R_i, the future-minus-past inversion count for R_i-i gives sum_i i(R_i-i) = -sum_inv(i,j)(j-i); since the squares of the ranks sum to the squares of the time indices, sum_i(R_i-i)^2 = 2 sum_inv(i,j)(j-i). For each fixed lag, the length-normalized inversion count converges by the iid shift ergodic theorem. Inversions past lag m are dominated by the stationary forward sum of the corresponding lag-weighted indicators, whose mean tends to zero by p(k) <= q^k. Thus each single-walk squared displacement sum divided by n converges to 2 sum_k k p(k). To pass to the two-walk squared rank difference, the windowed displacements can be approximated in empirical L^2 by the stationary two-sided displacements: at fixed m the interior errors are bounded by all-lag tails past m with second moments tending to zero, and the 2m boundary terms vanish by the finite fourth moments and Borel–Cantelli. Their two-walk cross average converges to zero by Cauchy–Schwarz and the ergodic theorem, since the two stationary walks are independent and each past/future difference has mean zero. This proves the factor 12 with the exact Spearman denominator. Kendall counts the exclusive-or of the two inverted comparisons at each lag, giving its stated probability and the factor 4; the unweighted stationary tail bound justifies summing all lags. At least one p(1)>0 makes both limits positive because each p(1)<1. With both walks monotone after orientation, both errors vanish identically. These are pathwise limits under the stated moments and no ties, not limits for iid observations of the levels.

## originality

PASS

The distinct contribution is the almost-sure two-rate result with its exact lag-probability constants under oriented nonzero drift, no ties and the exponential-moment condition. The directly comparable rank-correlation theorem is centered and distributional. The generic rank identities and one-walk occupation identity do not by themselves give the two pathwise limits.

## value

PASS

A shared time ordering of independent trending series can make both sample rank measures saturate. Quantifying two different powers and their nondegenerate constants distinguishes statistics that look identical at the limit; it also identifies how inversion lengths matter for Spearman but not Kendall. That is a specific benchmark for comparing rank methods on nonstationary paths, beyond the qualitative warning about trends.

The dated certificate retains the supplied scientific assessment, sources and limitations.
