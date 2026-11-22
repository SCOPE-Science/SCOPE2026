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

# Verification summary

The code `verify.py` uses only Python 3's standard library. It computes exact rational Bernstein coefficients for the three strict separated-cell inequalities; all coefficient minima are positive. It tests the exact same-cell residual identity and the rational equality witness, and compares 3,379 rational arc residual calculations on periodic grids of 6, 7, 8, and 10 cells with the stated bound. Run with `python3 verify.py`.

Finite sample tests are not an exhaustive optimization and are not treated as a proof of the continuum bound. The written mathematical proof obtains the bound by a complete endpoint-cell case partition plus the nonnegative Bernstein basis. No independent audit has been performed.
