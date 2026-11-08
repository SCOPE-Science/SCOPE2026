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

# Reproducibility notes

With Python 3 and only the standard library, execute `python3 verify.py`. The checker uses exact fractions and verifies two independently constructed stopping-time laws: one via absorbing suffix-state transitions and one via formal rational-series coefficients. It also enumerates binary words up to ten symbols for selected probabilities and checks conditional cumulative distribution inequalities at every sampled horizon.

Observed execution result: `PASS: 4657 exact assertions; independent state DP and word enumeration`.

The finite tests cover sampled run lengths, rational Bernoulli probabilities and finite horizons, not all parameter values. The proof in RESULT.md establishes the all-parameter claim by an exact generating-function factorization, a likelihood-ratio argument on the finite residual, and an optimal ordered coupling. Independent validation has not been performed.
