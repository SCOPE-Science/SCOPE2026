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

## Reproduction

Run `python3 verify.py` from this directory; the script uses only the Python standard library and a fixed pseudo-random seed. It checks 972 exact rational identities and 4,200 randomized cases across the derivative formula, matrix-scaling update, derivative maximizer, global Lipschitz inequality, Birkhoff comparison, and reverse-sweep ordering. The final package is also tested after extraction.

## Limits

Finite tests and central differences are diagnostic only, not certification of all real inputs; the quantified proof is given in RESULT.md. Central-difference rounding error is controlled by a numerical tolerance, not treated as exact equality. No independent audit has been performed.
