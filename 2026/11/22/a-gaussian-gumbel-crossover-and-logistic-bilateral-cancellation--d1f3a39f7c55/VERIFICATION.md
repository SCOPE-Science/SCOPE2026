---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

At fixed T an independent Brownian integral conditional on the common environment is Gaussian with variance 2A_N, so the entire cloud is a standard Gaussian cloud times an independent common scale. The upper and reflected lower extremes have joint interval probability [Phi(u)+Phi(v)-1]_+^N for standard thresholds; Mills asymptotics yield independent Gumbels at the same a_N=1/sqrt(2 log N) scale. A telegraph flip process has E[S(s)S(t)]=exp(-2 lambda |s-t|); the compensated flip martingale has bracket 4 lambda t and its rescaled jump size goes to zero, giving sqrt(lambda) B_N -> N(0,T). For t1<t2<t3<t4 the sign product expectation is exp(-2 lambda[(t2-t1)+(t4-t3)]). Thus E B_N^4=12 integral_0^T s(T-s)^2 exp(-2 lambda s) ds=O(lambda^-2), justifying the L2 Taylor remainder. Since m_N/b_N=2 log N+O(log log N), the additive shift is (delta log N/A_0) B_N plus o_P(1+log N/sqrt(lambda)); this yields the three coefficients with the stated slow-regime renormalization. The difference of magnitudes removes the common additive shift exactly; the remaining multiplicative factor tends to one for any lambda_N -> infinity, with no condition on the ratio. A difference of the independent Gumbels is log(E_2/E_1), hence standard logistic and independent of the limiting clock. The total variance is exactly 2A_0 Var(U_N)+2 Var(sqrt(A_N))(E U_N)^2. Gaussian maximum moment convergence gives Var(U_N)~pi^2/(12 log N), while Taylor with the fourth moment and the exact clock variance gives Var(sqrt(A_N))~delta^2/(4 Dbar lambda_N); this gives both stated terms. At criticality the two normalized marginal second moments converge, and their product is uniformly integrable by the normal tail bounds and the clock fourth-moment bound, so the covariance assertion is an actual covariance limit as well as the covariance of the weak limit.

## originality

PASS

Best-of-knowledge novelty lies in the evaluated simultaneous fast-clock/large-population, bilateral extreme law with explicit environmental coefficient and the variance competition, not the integrated-diffusivity normal mixture, its single-particle Gaussianization, variance decomposition, or the standard logistic identity separately.

## value

PASS

The two front magnitudes provide two complementary measurements of the same sample: their common mode retains environmental fluctuations and their signed imbalance is robust to the leading common fluctuation. The exact critical rate and the two sharp variance coefficients quantify when either source dominates. The joint prediction is appreciably stronger than single-particle Gaussianization or a one-sided maximum in a fixed environment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
