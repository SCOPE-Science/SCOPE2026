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

For continuous positive data the unsymmetrized ratio expectation is one half of E[min/max], and the stated U-statistic has this expectation. Writing s2=EX² makes the fitted numerator mA+(s2−2m²)B−m²/2; direct integration for Beta(a,1) gives a(a−1)/[2(a+1)(2a+1)]. Scale invariance gives the entire uniform scale family. Near (1,1) the Beta integrals extend analytically using bounded kernels and integrable dominating powers of each endpoint. Differentiation along the two log-density scores yields 1/12 and (19−2π²)/12; the analytic implicit-function theorem gives a unique local branch a(b) with slope 2π²−19, with non-Gamma support. Independently differentiating the numerator at zero and adding both pairwise projections gives the stated fitted influence function. At uniform it is 3x−3x²+2x log x with variance 3/10−7/12+8/27=7/540. At the matching Gamma, scale invariance permits Gamma(3,1); exact factorial integrals of the squared exponential polynomials give 37/2592. The requisite fourth moments for the sample-second-moment CLT exist under both laws (finite second moment alone would not justify a general CLT). For central two-sided Gamma calibration that refits by moments, null-variance continuity at shape 3 follows from continuous conditional kernel means and uniform moment bounds on a compact shape interval; the stated consistent calibration has asymptotic scaled cutoffs ±z√(37/2592). The alternative variance therefore gives 2Φ(−z√(185/168))≈0.0397113 at 5%. The original uncensored preprint allows generic consistent estimates; moment fitting is the explicitly selected variant here, and this power does not follow from its printed plug-in asymptotics or an unrefitted implementation. Its fixed-parameter projection at Gamma(3,1) differs and has variance 521/324. The frozen checker was inspected, not run.

## originality

PASS

The exact source scalar statistic is prior; the supported contribution is a bounded-support non-Gamma zero family, the analytic Beta continuation and sign law, and exact fitted variance and central refitted power calculations. The source's assertion that the scalar is nonzero under every alternative is contradicted for the explicitly scoped moment fit, not inherited from the pointwise fixed-point identity. The nearest distinct catalogue hits are analogous blind families for other statistics, not implications for this one.

## value

PASS

A published scalar goodness-of-fit procedure can miss a familiar bounded-support alternative even though its fitted Gamma matches both moments. The analytic neighborhood shows robust nonidentification on an explicit two-shape slice rather than a single coincidence. Accounting for refitting changes the null asymptotics and gives a reproducible subnominal rejection limit with direct consequences for calibration. This is not a criticism of the separate squared-residual omnibus test and does not claim censoring or finite-sample conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
