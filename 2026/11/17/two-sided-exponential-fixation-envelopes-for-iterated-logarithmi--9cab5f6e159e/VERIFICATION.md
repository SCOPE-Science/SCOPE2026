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

# Reproduction

Run `python3 verify.py` in a directory containing the accompanying embedded checker. It uses only the Python standard library and checks binomial probability normalization, endpoint absorption, strict finite interior exponential bounds and analytical sign conditions for sample parameters. It also verifies the explicit upper bound against numerically determined absorption probabilities.

The universal conclusion is an analytic theorem in `RESULT.md`. Finite tests neither certify all degrees nor cover all real parameter values. No independent external audit has been performed.
