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

For the ordinary joint MLE the location and scale score equations kill H(0) and H'(0) exactly, leaving the t^2 coefficient equal to the residual mean of h(y)=y^2 tanh(y/2)/2-y. For moments the leading coefficient is just minus the residual mean of g. Under the null, differentiating the population Stein identity gives centering of the raw frequency derivatives; their second-moment bounds and the one-dimensional Sobolev inequality give O_P(1) Taylor bounds for sqrt(n) H on [-1,1]. Root-n parameter errors times polynomial sample averages preserve these bounds for the fitted process. For |t|>1, the centered raw sum has second moment at most (1+|t|)^2, and the fit perturbation is stochastically bounded by O_P(1)(1+t^2). Integrating these Gaussian tails leaves no factor n, so the reduction is valid along every deterministic a_n tending to infinity. The regular logistic MLE expansion follows from the smooth likelihood, nonsingular information (odd location and even scale scores with positive variances), and concavity in inverse-scale/intercept coordinates; the moment expansion follows by the delta method. Parity removes both scale corrections in the leading means. Location gives influences g-X/3 and h-((pi^2-6)/6)g. The logistic beta integral and Stein identities give the stated positive variances; independent uniform-CDF quadrature reproduced them and the Gaussian-weighted multipliers 0.057086432202785874 and 4.8514073649406617. The scalar CLT, squaring and the zeroth/fourth Gaussian integrals give the two sharp limits, not just sequential limits.

## originality

PASS

The distinct claim is the estimator-specific arbitrary-rate joint null limit with sharp powers and explicit constants for the same logistic Fourier–Stein test. Fixed-weight prior theory establishes the statistic and fitted null framework, not the shrinking-frequency regime. The strongest analogous large-weight studies inspected use different test processes or a different order of limits.

## value

PASS

The same established test has two genuinely different rates depending only on how its nuisance parameters are fitted. The exact MLE cancellation explains the difference, and the sharp normalization and constants give a usable null calibration regime without selecting a sample-size-dependent growth window. This does not rest on a tiny numerical gain or on claiming improved test power.

The dated certificate retains the supplied scientific assessment, sources and limitations.
