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

The package includes the standalone Python standard-library program `verify.py`. Invoke `python3 verify.py`. It recomputes the exact length-uniform coefficients for every dimension 2–14 in two different representations, confirms no amplification below fourteen and strict amplification at fourteen, tests explicit gradient counts for the uniform-interval law and its sharp coefficient in dimensions 2–30, and prints `ALL_INTERVAL_REVERSAL_CHECKS_PASS` on success. The theorem's uniform-in-dimension statement and its continuum lower bound require the symbolic counting and integration arguments of `RESULT.md`; finite tests are not substitutes for them. The complete exact finite results are recorded as rational fractions rather than floating-point approximations.
