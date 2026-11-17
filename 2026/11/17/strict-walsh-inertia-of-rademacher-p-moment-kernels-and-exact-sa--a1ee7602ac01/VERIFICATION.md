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

The analytical proof establishes the statement for all integer dimensions \(n\ge2\) and all real \(0<p<2\). The nonstandard step is the strict positivity of the integral \(I_{k,m}(p)\) even when \(m\) is odd; each consecutive pair of half-periods contributes a strictly positive quantity after the reflection \(u\mapsto\pi-u\). The proof explicitly verifies convergence at zero and infinity.

A standalone Python 3 script, `check_rademacher_inertia.py`, using only standard-library modules, was executed and returned:

`RADEMACHER_ABSOLUTE_POWER_DIAGNOSTICS_OK 587`

It checks finite-dimensional Walsh eigenvalues, sign patterns, and the \(p=2\) collapse, and checks direct matrix-vector multiplication for selected dimensions and exponents. These diagnostics are not a proof for arbitrary dimension or exponent. No independent mathematical audit has been performed.
