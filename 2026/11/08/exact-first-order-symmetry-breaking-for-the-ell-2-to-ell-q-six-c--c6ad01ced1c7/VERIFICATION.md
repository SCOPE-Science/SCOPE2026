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

The analytical proof derives the exact stationary-point reduction, an exact rational quartic factorization, and a unique-minimum argument for the logarithmic critical-point ratio. The resulting critical exponent and both equality orbits follow by exact identities, not finite numerical searches.

Standalone check: run `python verify.py`. It reports `EXACT_C6_CHECK_OK 4366`, comprising 162 exact rational polynomial assertions and 4,204 specified floating-point corroborations. The tests sample finitely many parameters and are not exhaustive for continuous exponents or input vectors. No independent mathematical audit has been performed.
