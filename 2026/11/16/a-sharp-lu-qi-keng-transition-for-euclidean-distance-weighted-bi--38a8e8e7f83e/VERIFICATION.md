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
# Verification of the finite computations

Run `python3 CHECK.py` with a standard Python 3 interpreter after extracting it alongside the documents. The checker constructs the polynomial recurrence with exact rational coefficients; verifies the power-series coefficient identities for finite integer exponents and Taylor degrees; checks the explicit polynomial at exponent two and the coefficient degree pattern; and numerically isolates rightmost roots of selected polynomials in the interval \((-1,0)\). The mathematical proof in `RESULT.md` covers all nonnegative integer exponents and does not rely on extrapolation from these finite tests. No external independent audit has been performed.
