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

# Verification and scope

The proof in `RESULT.md` proves the full age and radial stochastic order from a coupled partition of Poisson refresh points. Its critical strict inequality is the positive covariance of two strictly decreasing exponentials of the same nondegenerate random rate. An event with no original refresh mark and one additional mark yields the explicit lower bound. Jensen's inequality and an integrated-rate covariance estimate establish the sharp endpoint limits. The independent Gaussian time-mixture identity transfers age ordering to Brownian radial tails and moments.

Run `python3 verify.py` with the Python standard library. The program compares a two-state exact Feynman--Kac formula with independent ODE integration, independently integrates a three-state Feynman--Kac system, evaluates the strict quantitative one-extra-mark lower bound, checks stationary mean-square displacement, and compares Gaussian-tail quadrature with the exact quenched endpoint. These are bounded calculations, not proofs of the universal assertions.

The proof does not extend without new arguments to rate distributions reaching zero, correlated rate refreshes, non-Poisson refresh times, time-dependent spatial rates, or first-passage observables. There has been no independent audit.
