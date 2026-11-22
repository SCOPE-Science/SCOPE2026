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

# Verification

Run `python CHECK.py` with Python 3 and SymPy. The script independently derives the normalized forward-generator ratio, verifies the Beta normalization of the forced reset density, checks the exact endpoint/interior maximizers, the unique scale-optimized rate, and the quartic origin and universal shell identities. It also evaluates 1,875 exact rational representative inequalities across dimensions, exponents and scales. The mathematical proof, rather than finite computation, covers all stated parameters.

The exact stationary law follows from the renewal-resolvent representation for independent complete Poisson resets. No independent scientific audit has been performed.
