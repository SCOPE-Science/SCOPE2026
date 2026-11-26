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

For the two centered product normal laws the log likelihood ratio is affine, increasing in squared radius. Its zero yields the younger and older chi-square cutoffs Nq log(q)/(q-1) and N log(q)/(q-1) respectively; at zero reference age the laws are mutually singular. Put z=exp(-2 kappa t) and c=1-exp(-2 kappa Delta). The single-coordinate affinity has fourth power 1-[cz/(2-(2-c)z)]^2; the product affinity bounds twice the Bayes error above by exp(-Nc^2z^2/16). This proves the high-signal limit and dominates the stationary average; in the low-signal limit the affinity tends to one and total variation tends to zero. In the finite-signal window the standardized chi-square cutoffs converge to +/-c eta/(2 sqrt(2)), giving the stated risk. For p=r/(2 kappa), the scaled reference variable u=sqrt(N)z has density p N^(-p/2) u^(p-1) on (0,sqrt(N)). Integrating the limiting profile against p u^(p-1) via the Gaussian positive-part moment gives 2^(2p-1) Gamma((p+1)/2)/(sqrt(pi)c^p). These are limits for the stated regimes, not convergence for arbitrary oscillating signals. The exact exponent p/2 can be an integer at particular fixed rate ratios; 'noninteger' in the introductory prose is a generic possibility, not an additional restriction or an always-noninteger conclusion.

## originality

PASS

The stochastic model, sufficient energy statistic, Gaussian testing mechanism and closely analogous equilibrium-energy edge integral are established. The distinct contribution is the calibrated pair-of-ages experiment with sharp age resolution and averaged optimal error, not a new mixture model or new general testing method.

## value

PASS

This gives a precise resolution limit for a motivated, fully specified inverse question about a canonical regenerative model. The finite optimal test, the temporal crossover profile and its averaged error jointly quantify information lost when OU relaxation nearly erases the elapsed time. The contribution is narrow and analytically close to the known stationary energy edge, but not a relabeling of an exceedance event; the experiment distinguishes the effects of the candidate offset, relaxation and reset rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
