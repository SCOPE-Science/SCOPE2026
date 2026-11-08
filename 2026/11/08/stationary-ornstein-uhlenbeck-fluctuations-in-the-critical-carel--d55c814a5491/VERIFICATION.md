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

# Verification of the stationary fluctuation theorem

Run `python checker.py` with Python 3 (standard library only). It prints `PASS 945 exact rational assertions` and checks, independently of the written derivation, transition row sums, finite-state stationarity, all fixed-subset inclusion moments, the first and second count moments, and four time-lag regressions for \(n=2,\ldots,8\) and \(p\in\{1/2,1/3,2/5\}\).

The proof's non-finite checks are analytic: the conditional step variance is an explicit bounded Lipschitz function of current density, the fourth centered jump moments are bounded uniformly because one-step losses are dominated by \(\operatorname{Binomial}(n,c/n)\), stationarity gives uniformly bounded centered second moments, and the predictable quadratic variation converges in \(L^1\) uniformly on compact time intervals. Martingale functional convergence, tightness of the semimartingale decomposition, and uniqueness of the stationary Ornstein–Uhlenbeck martingale problem complete the infinite-dimensional argument. The exact time-lag covariance follows from affine conditional regression.

The limiting variance is \(c(c+2)/(2(1+c)^3)\). The result is restricted to fixed \(c>0\), stationary initialization, and bounded accelerated time intervals. Neither the checker nor the analytic result establishes a rare full-collection hitting-time law, a general nonuniform-coupon theorem, or independent mathematical certification.
