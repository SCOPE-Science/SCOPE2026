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

The mathematical proof uses (i) the transient negative-binomial generating function of a linear birth-death-immigration chain; (ii) independent local Poisson reset-age mixing; (iii) an infinite-microstate product limit; (iv) a critical-limit Laplace transform; (v) moment uniformity from nonnegative factorial cumulants; and (vi) dominated convergence on a rescaled fitness integral.

Run `python checker.py` using Python 3 and the `mpmath` library to repeat 17 numeric and algebraic consistency assertions. The exact symbolic moment anchors are \(\mathbb EY=1\), \(\mathbb EY^2=3\), and \(\mathbb EY^3=19\). The numerical checks do not establish the infinite-asymptotic theorem and are not represented as independent validation.

Limits: the population distribution is defined by first sending the independent microstate count to infinity, then approaching criticality through positive excess death rates, and only then studying the high-occupation tail. The strictly critical finite-state highest-fitness site is not stationary and is excluded. The closest published same-model pair-crowding result's accessible index summary does not establish complete statement-by-statement nonoverlap with its unavailable full text.
