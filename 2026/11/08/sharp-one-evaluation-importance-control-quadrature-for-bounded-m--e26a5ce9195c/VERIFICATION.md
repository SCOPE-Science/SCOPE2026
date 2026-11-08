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

Run `python3 check.py` with Python 3 and no external dependencies. The recorded 79 checks are in `check_output.txt`; they include density mass, centering, saddle CDF and product identities, numerical quadrature for 61 discontinuous unit-step tests (each split at its jump), six monotone power functions and five alternative densities. Analytical proof, not finite testing, establishes the continuum of steps, uniqueness and worst-case over all monotone measurable functions. Numerical midpoint integration tolerance is explicitly coded.

The only required files are in this package. No external scientific audit or independent validation was performed.
