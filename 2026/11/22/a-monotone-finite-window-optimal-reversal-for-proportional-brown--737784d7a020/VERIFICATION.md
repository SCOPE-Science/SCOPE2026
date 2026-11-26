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

Conditioning on the stationary two-sided Poisson clock gives a centered Brownian integral with mean conditional variance, averaged over the clock, 2D times integral_0^infinity exp(-r(1-a^2)s) ds. Contraction on a common future clock gives uniqueness. Conditioning on a future clock yields E[X_t|X_0=x]=xE[a^N_t]=x exp(-r(1-a)t), valid also for negative a and a=0. Integrating the resulting stationary covariance over the observation square gives the exact variance with dimensionless tau=rT and b=1-a. The logarithmic objective derivative is H=R-mu, with R=1/(2-b)-1/b and mu the mean with density proportional to (tau-s)e^(-bs) on (0,tau); partial_b H=R'+Var(s)>0. H(1)<0, and at 4/3, R=1/b>mu because the nonconstant decreasing weight (tau-s)_+ strictly lowers the exponential mean. This proves global uniqueness and the claimed open interval. The text's final inference in Step 3 can be made explicit: smooth strict ordering alone does not imply a pointwise strict derivative, but Leibniz differentiation gives partial_tau mu=Cov(s,1/(tau-s))>0 for the same density. The endpoint term vanishes and the covariance is finite and strictly positive by the two-independent-copies identity for increasing functions on a nondegenerate interval. So a_*'=-partial_tau mu/(R'+Var(s))<0 at every tau; no change to the theorem is needed. The small-tau weighted mean is tau/3+O(tau^2) uniformly on the root interval. At large tau it is 1/b-1/(b^2 tau)+O(tau^-2) there, and (R-1/b)'(4/3)=27/8, which gives the 1/(6 tau) correction with the stated sign. The long-time rate 4D/[r^2 b^2(2-b)] minimizes at 4/3 and the ratio is 27/32; the snapshot variance minimizes at a=0 instead. Independent replay: python3 /tmp/opencode/brownian-window-replay.py (mpmath, 60 decimal digits, bisection of the closed objective derivative), confirms all eleven sampled root signs and ordering and gives -0.1351710457598, -0.2539189487560, -0.3145204058622 at tau=1,3,10. The deposited path simulation was inspected, not run: the Brownian bridge variance D duration^3/6 is correct; the stationary start is accurately truncated, not exactly infinite-series stationary. Neither finite exercise proves the continuum result.

## originality

PASS

The exact signed resetting model and signed exponential covariance are known, and the finite variance formula itself follows by ordinary covariance integration. The supported increment is the complete optimizer over negative and nonnegative multipliers at every finite duration, its strictly signed derivative in duration, endpoint rates and exact optimal asymptotic gain, not a new resetting process or covariance formula.

## value

PASS

Estimating the mean signed position is a natural use of a finite stationary trajectory; reset rescaling changes snapshot amplitude and correlation time in opposite directions. The theorem quantifies the design tradeoff for every observation length, proves a unique strictly negative optimum and exact horizon ordering, and gives asymptotic and short-window design scales. The novelty and value do not depend on the generator or integrating one exponential, or on treating a Monte Carlo match as a proof. The conclusion is specific to this loss and signed instantaneous resets, not a claim about first passage, entropy or optimal protocols in general.

The dated certificate retains the supplied scientific assessment, sources and limitations.
