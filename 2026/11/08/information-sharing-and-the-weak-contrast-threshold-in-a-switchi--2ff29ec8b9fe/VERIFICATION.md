---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Conditional on the two-sided common switching process, the positions are independent N(0,V) and V lies between the two harmonic variances with beta-type stationary density. Radial sufficient statistics satisfy log(T_k/k)=W+Z_k with Z_k=log(chi_k^2/k); the conditional-independence information identity gives I(groups n;m)=F_n+F_m-F_(n+m). Gamma entropy h(Z_k)=0.5 log(4*pi*e/k)+o(1) and entropic approximate-identity arguments yield the fixed-contrast logarithm and constant. Under epsilon_n->0, log variance scaled by epsilon converges to Beta(a,b) and sqrt(n)Z_n to N(0,2), giving the specified critical Gaussian-channel MI; its small-signal term is tau^4 Var(B)^2/8. Boundary cases equal stiffness give zero MI, small n epsilon^2 gives zero and large n epsilon^2 the displayed logarithm. Independently integrated the a=b=1, mu1=2,mu2=1 entropy constant and checked log chi-square Stirling numerics. Nontrivial uniform entropy/tail control is given as an analytic lemma, rather than inferred from weak convergence alone.

## originality

PASS

The primary stochastic-trap paper derives the shared random Gaussian-variance mixture and correlation structure, not the submitted exact information identity or weak-contrast scaling law. Clarke–Barron regular Bayesian-mixture theory covers the generic one-parameter leading log-growth mechanism but not this model-specific finite-k chi-square entropy identity, explicit constant, beta-shaped crossover and quartic weak-signal threshold.

## value

PASS

Exact mutual information between large noninteracting groups quantifies a dependence invisible to position covariance. The n*epsilon^2 detectability threshold distinguishes weak common noise from independent particles, with an explicit non-Gaussian beta Gaussian-channel profile and a calculable sharp constant. The calculation is naturally motivated by shared-environment many-particle statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
