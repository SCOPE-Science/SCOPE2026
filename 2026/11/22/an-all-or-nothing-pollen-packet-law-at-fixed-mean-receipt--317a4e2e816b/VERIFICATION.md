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

For deterministic integer packet size k, m=ceil(r/k) and a=λ/r give λ/k≤ma. The Poisson upper tail is strictly increasing in the positive mean (the derivative at mean μ is Pr(Pois(μ)=m−1)), so S_k≤Q_m(a), with equality to the relevant Q at k=1,r. For 1<k<r, 1<m<r; when k>r, the one-packet score strictly decreases. Coupling Pois(na) plus Pois(a), the loss in Q_{n+1}−Q_n is exactly X=n,Y=0; gains are X=n+1−j,Y≥j for 2≤j≤n+1. Dividing by Pr(X=n), each shared positive factor is a^(−(j−1)) times the product of 1−ℓ/n for 0≤ℓ≤j−2 and is nondecreasing in n; each increase of n adds a strictly positive new term. This gives strictly increasing normalized differences. An interior integer index with incoming difference nonpositive lies strictly below the left endpoint unless it is immediately after a flat minimum, in which case it is strictly below the right endpoint; if its incoming difference is positive all subsequent differences are positive. Equivalently a valley with at most one flat step cannot contain an interior endpoint-maximizing tie. For the two surviving sizes, the sign of S_r−S_1 is the sign of 1−exp((r−1)λ/r)/P(λ). The log derivative of that ratio increases strictly from −1/r to 1−1/r by the reciprocal positive-power-ratio argument, the ratio starts at one and diverges, and there is exactly one positive return to one. At λ=r+x√r the monad tail tends to Φ(x), while the packet probability tends to 1−e^(−1); strict signs on both sides of that quantile bracket the unique root. The proof covers r=2, integer sizes beyond r, and the sole two-way tie. The shipped checker was inspected, not executed; its tolerance-based finite grid is not a proof of strictness. No heterogeneous-packet or empirical botanical validation is implied.

## originality

PASS

The supported distinct claim is strict global endpoint optimality for this integer fixed-mean threshold problem and the diagonal Poisson valley supporting it, together with the exact switching budget and asymptotic. Accessible centered-gamma results address fixed additive offsets, and the closest allocation/optimization analogues change the observable or the optimization direction. Unavailable botanical full texts remain residual risk, not evidence of noncoverage.

## value

PASS

The proof explains why intermediate deterministic aggregation cannot improve a fixed-budget Poisson quorum probability, even in the divisibility cases where Poisson mean comparison alone is equality. The discrete valley is a useful quantitative shape constraint on a basic family of gamma CDFs; the unique switch and its √r displacement resolve the decision across all thresholds and budgets. This is a stylized model classification, not a prescription for changing real pollen delivery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
