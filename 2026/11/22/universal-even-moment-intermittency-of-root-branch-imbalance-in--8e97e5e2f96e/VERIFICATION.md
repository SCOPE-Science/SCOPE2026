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

# Verification scope

Run `python3 verify_moments.py` in this directory with Python 3. The checker uses only standard-library integer and rational arithmetic. It verifies the exact two-branch generator on low monomials, confirms polynomial closure of moment identities, and matches the leading exponential coefficients against the beta-factorial formula for orders one through six. The observed run passed 284 assertions.

The proof of the all-order asymptotic uses a last-root-event identity, independent Yule family moments and a dominated-convergence argument, all shown in RESULT.md. The finite tests do not replace or independently certify that proof. No external/independent mathematical audit has been performed.
