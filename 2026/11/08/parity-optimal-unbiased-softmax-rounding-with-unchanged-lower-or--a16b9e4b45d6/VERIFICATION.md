---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS: For each proper S subset of n Bernoulli rounds, the moment equations E(prod_(i in S)B_i)=prod p_i have rank 2^n-1, giving one affine parity atom coordinate q_b+(-1)^(n-|b|)*theta. Nonnegativity is precisely -alpha<=theta<=beta. In CE the -z_y expectation is theta-invariant. Its mixed forward difference equals integral of distinct-index derivative of logsumexp, which is (-1)^(n-1)(n-1)! times strictly positive product of softmax probabilities; hence unique theta endpoint by n parity, invariant in y. Fair p=1/2 endpoint supported on even parity and symmetric h asymptotic gain h/2^n+O(1) follow exactly by binomial difference. Independently computed 50 random higher-dimensional cases for proper-subset constraints and endpoint sign, and n=3 h=4 gain 0.25014236686591174. Finite examples do not establish general calculus or rank proof.

## originality

PASS

PASS, best-of-knowledge: Natarajan et al. 2022 already prove the general one-parameter (n-1)-wise-independent Bernoulli feasible law and parity bounds, and are credited. The additional global strict sign of the logsumexp n-way mixed derivative, all-label cross-entropy endpoint optimization and exact quantified gain were not stated in the read full primary independence paper nor prior ZO/low-precision work accessible. Chatelain/de Oliveira Castro full paper unavailable from authorized institutions; unindexed higher-order difference inequality applied to logsumexp could imply this theorem. This is a motivated one-shot output-logit coupling, NOT a claim about sequential stochastic rounding unbiasedness.

## value

PASS

PASS: Identifies a mathematically sharp way higher-order dependence changes a standard nonlinear loss while all lower-order Bernoulli joint distributions, means and covariances are preserved. Exact n-way mixed derivative gives a universal label-independent optimizer and quantifiable risk gap; this is a useful natural risk invariant beyond known probability coupling geometry, with no speculative actual floating point implementation guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
