---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Given the whole sign path, rows are independent, and each row's mean is the parity mean (1−2p_n)^binom(S_n,d), with empty product 1. The strong law for S_n/n and conditional Hoeffding give H_N/N→ρ almost surely; Fubini disintegrates this over environments. The bracket of the fixed-environment martingale is H_{N−1}+1, with deterministic diagonal brackets, so the bounded-jump functional CLT applies (uniform bracket convergence on compact rescaled time intervals follows from the partial-sum strong law). For all S_n, replacing the falling factorial and log by their leading terms incurs O(n^−1) for fixed d, including d=1. Taylor expansion gives slope −f′(1/2)/2=a since S_n/n−1/2=−X_n/(2n), and the fourth-moment bound gives a total L² error O(log N). The harmonic weights sum to N, their squares sum to 2N−h_N by summing min(r,s)/(rs), and their maximum h_N is o(sqrt(N)); Lindeberg gives the stated history Gaussian. Conditional characteristic functions of the bounded centered row noise converge almost surely to the deterministic characteristic function with variance 1−ρ²; bounded convergence permits multiplication by the varying unit-modulus characteristic factors of the history statistics. Conditional orthogonality and L² error control also establish the moment limits, not merely convergence in distribution. The bounded bracket shift and finitely many clipped probabilities do not change these limits.

## originality

PASS

The two-walk Brownian limit and the use of the bracket are within existing theory. The supported distinct claim is the joint second-order annealed law and the explicit degree-dependent variance at fixed positive Brownian correlation; neither the inspected general criteria nor the closest static-coefficient results supply it.

## value

PASS

The formula identifies a concrete mechanism hidden by the first-order Brownian covariance: different interaction degrees tuned to the same ρ yield strictly different bracket variance rates. It gives a usable second-order invariant and separates conditional coefficient noise from the history contribution, rather than just exhibiting two models with the same correlation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
