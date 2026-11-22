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

# Computational and analytical verification

The exact critical control, derivative identities, and cubic flip coefficient are presented with proofs in RESULT.md. Execute `python3 CHECK.py` with Python 3.9 or newer; it requires no third-party dependencies and uses high-precision Decimal arithmetic. It reconstructs the first- and higher-derivative expressions from the logarithmic derivative, independently solves the prime-two equations by bracketing, evaluates return multipliers, and checks critical and large-exponent constants for six integer exponents. These diagnostics support but do not establish the stated all-real-beta theorem. They do not test global basin claims (none are made). Self-review is passed; independent audit has not been performed.
