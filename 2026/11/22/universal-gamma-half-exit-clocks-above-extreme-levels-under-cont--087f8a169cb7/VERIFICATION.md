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

Run `python verify.py` using Python 3 with no third-party packages. The checker verifies finite Laplace-component partial-fraction weights and their first four exact even-moment coefficient identities for several rational contraction strengths; finite-high-level tail comparisons; quadrature of the independent exponential overshoot with the Brownian first-exit survival function over a multi-parameter grid; and the limiting Gamma-half mean. Its counted assertions are reported by the checker itself.

The proof in `RESULT.md` supplies the all-threshold asymptotics. The finite computational tests are supplementary and do not certify a universal infinite-domain statement. The exact complete-reset equality follows directly by conditioning the two-sided Laplace invariant law and the first independent Poisson reset clock. Independent mathematical assessment has not been performed.
