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
# Finite symbolic verification

The standalone Python 3 certificate reproduces the complete inclusion-exclusion polynomial for every equality pattern of three labels at each of four vertices. Exactly 625 patterns are checked when all coordinate sizes are at least four, and 500 feasible patterns when the first coordinate size equals two. The checker expands the two universally nonnegative difference polynomials over a monomial basis with exact integer coefficients. Since the shifted variables are nonnegative for every permitted prime tuple, this finite symbolic certificate proves unbounded parameter inequalities. It also verifies explicit equality patterns for both cases.

Command: `python3 crt_four_prime_certificate.py`.

The independently obtained exhaustive pointwise maxima at coordinate sizes (2,4,6,10) and (4,6,10,12) are 157 and 361. Those examples are corroboration only. The code verifies a finite symbolic inequality and is not independent mathematical validation of its interpretation. No independent audit has been performed.
