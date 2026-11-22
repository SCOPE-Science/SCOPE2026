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

# Verification and proof boundaries

Run `python3 verify.py` using Python's standard library. Expected text: `VERIFY_OK general_inequality_checks=26460 recommended_checks=1400`. The tests check many rational rank fractions, integer budgets, scale choices, logarithmic oracle decisions and exact normalized risk ratios. No random Monte Carlo estimate is used as a certificate.

The infinite-family proof rests on \(Nb^2=(m/2)a^2\), the elementary inequalities \(a/(1+a)\le\log(1+a)\le a\) for nonnegative arguments, the standard Gaussian fourth moment, and exact minimal-polynomial termination of Lanczos on a two-eigenvalue matrix. The substantive limitation is that best rank approximations are assumed available at the assigned nominal cost; this is a mathematical benchmark rather than a finite-precision complexity result. Public source comparisons establish only best-knowledge non-coverage, not publication independence.
