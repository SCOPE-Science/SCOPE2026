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

The accompanying standard-library `check.py` independently enumerates the torus weights and the proposed modular characters through degree 199. It also constructs actual finite-field evaluation matrices from nonzero radial coefficients at rational test radii for degrees one through eight; harmonic coefficient recurrences are checked with exact rational arithmetic.

Replay with `python3 check.py`; the expected successful line is `TORUS_KNOT_INTERPOLATION_OK 199 exact residue classifications 8 independent finite-field evaluation matrix ranks`.

The finite tests do not establish the general theorem; the all-degree proof rests on the exact square parametrization, the lattice-congruence argument, and harmonicity recurrence in RESULT.md. The checker uses rational radii only for its finite tested degrees; the theorem's radius-independent generic condition and universal transcendental choice are proved analytically. No independent audit has been performed.
