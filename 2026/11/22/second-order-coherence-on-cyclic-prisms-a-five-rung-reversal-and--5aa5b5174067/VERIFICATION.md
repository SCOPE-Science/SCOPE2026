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
# Reproducibility and verification

The accompanying standalone `verify.py` was run in a Python environment with NumPy, SymPy and mpmath; it printed exactly `VERIFY_OK 475`. Its 475 assertions cover exact rational small-prism inverse-trace identities; Fourier comparisons against explicit full Laplacians at different positive weights and both spectral orders; the exact rational sign comparisons at sizes three, five and six and common optimizer at size four; bisection of each monotone scalar root on representative sizes up to one thousand; and second-order asymptotic, regret and scale tests up to thirty thousand rungs. It requires no network, secret data or intermediate artifacts.

The finite verifier checks reproducibility only. Proof of the infinite family is the strictly decreasing spectral root equation, the analytic all-size comparison, and the exact hyperbolic-cotangent cycle resolvent with monotone asymptotic bracketing, all supplied in `RESULT.md`. The proof does not claim a uniform finite-size explicit error bound or cover general priced prisms. Independent audit remains unperformed.
