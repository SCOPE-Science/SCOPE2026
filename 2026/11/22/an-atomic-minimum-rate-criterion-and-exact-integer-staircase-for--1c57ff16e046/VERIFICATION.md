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

# Verification and limits

`python3 checker.py` ran in a Python 3 standard-library environment and printed `PASS: 10469 supplementary assertions`. The program tests the exact two-point threshold and its positive and negative regimes, numeric integer optima, hundreds of randomly generated finite mixtures, second-derivative sign calculations, strict-concavity behavior within numerical tolerance, first-derivative and variance identities, and an atomless uniform intensity example. All supporting code is included here. No source file or external input is needed to run it.

The universal conclusions are **analytic**, not extrapolations from finite testing. The decisive proof dependencies are: (i) tilted variance makes the log Laplace exponent strictly concave; (ii) the departure function's derivative is strictly negative; (iii) its limit is \(c\lambda_0+\log q\) for a positive endpoint atom and negative infinity if the endpoint atom is absent; and (iv) the adjacent-integer value difference increases from negative at feasibility to positive at large budgets when an interior residence optimum exists. The contradiction proof that an atomless Laplace exponent forces an unbounded gap between its value and tangent explicitly covers arbitrary nonnegative nondegenerate rate laws with finite mean.

Numerical checks cannot certify the statement for all distributions or rule out all prior literature. The all-deadline sign, zero-atom boundary, exact staircase, and uniqueness rely on the provided mathematical proof. Numerical floating-point comparisons within about \(2\times10^{-11}\) are treated as ties to avoid claiming machine precision proves strict inequalities at asymptotically very large observation times. No independent external audit or empirical field validation has been conducted.
