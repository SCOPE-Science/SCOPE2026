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

# Verification record

## Reproduction

Run `python3 check_two_tail.py` with Python 3. The checker uses only standard-library `fractions.Fraction` for exact finite certificate arithmetic, plus standard mathematical functions for separately marked numerical convergence diagnostics.

The checker examines every \(n=3,\ldots,37\) and every integer \(m\in\{0,\ldots,n\}\). At the rational values \(q=13/8\), \(h=1/1000\), it verifies the strict triangle-free rectangle inequalities, exact count split, pairwise Fibonacci domination of the rectangles, and the quadratic completion-of-the-square identity for three rational pairs of exponent slopes. The script reports 19,744 counted groups of finite validations. For four larger \(n\) in the asymmetric log-Laplace family with \(\alpha=2\), \(\beta=1\), it also computes the probability of the explicit rectangle event and compares its logarithmic rate with the fixed-ratio prediction.

A successful recorded run reported:

```
n=24 m=16  log(rectangle)/n^2=-0.37146190  geometric-q target=-0.16183594 true exponent=-0.16040394
n=40 m=27  log(rectangle)/n^2=-0.27593052  geometric-q target=-0.16183594 true exponent=-0.16040394
n=75 m=50  log(rectangle)/n^2=-0.21457169  geometric-q target=-0.16183594 true exponent=-0.16040394
n=120 m=80  log(rectangle)/n^2=-0.19099108  geometric-q target=-0.16183594 true exponent=-0.16040394
PASS: 19744 exact finite assertions and 4 double-Pareto lower-event calculations
```

## Proof checks and limits

The finite computation is **not** an exhaustive check of the infinitely many sample sizes, every distributional density, or every ratio \(q>\varphi\). The infinity claims rest on the analytical proof: the consecutive-triple reduction, Fibonacci pair growth, uniform deterministic two-sided energy bound, global log-density envelopes, a free integrable density factor for the upper bound, explicit positive-probability rectangles for the lower bound, and compactness for the conditional large-deviation principle.

The exact result applies to every fixed positive threshold, with no assumed uniformity over a threshold sequence that changes with sample size. Neither an independent proof assessment nor a formally verified proof is claimed.
