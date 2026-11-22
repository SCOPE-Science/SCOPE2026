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

# Verification procedures

Run `python3 verify.py` with Python 3.10+ using only its standard library. It checks exact polynomial identities for the integer Erlang-delay subfamily using rational coefficients, strict one-sign-change slope polynomial signs, 165 positive-rate crossovers, and high-precision decimal brackets for the explicit two-stage example.

Observed output: `PASS 2398 assertions; exact coefficient signs; 165 two-crossing samples; k=2 rigorous decimal brackets`.

Finite tests are corroboration, not exhaustive proof of infinitely many shapes or parameters. The full real-gamma-shape classification is proved in `RESULT.md` through the strict monotonicity of an explicit reciprocal-hazard integral and an exact derivative identity; these critical steps have no numerical approximation. No independent external validation has been performed.
