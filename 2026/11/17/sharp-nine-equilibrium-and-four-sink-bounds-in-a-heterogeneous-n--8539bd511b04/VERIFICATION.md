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

# Reproducible verification

Run `python check.py` in the directory containing the result. The executable uses only Python's standard library and performs exact-rational sign enclosures of the transcendental fixed-point equation, proves the three root brackets by opposite endpoint signs plus the analytic at-most-three result, bounds the three outer two-by-two characteristic polynomials, and compares rational lower and upper bounds in the full six-dimensional Rouché inequality. It uses the elementary uniform exponential bound `21*3**61/61!` for Taylor order 60 at arguments with absolute value at most three.

The printed certificate verifies nine simple positive fixed points and their exact division into four hyperbolic sinks and five unstable fixed points at the supplied parameter vector. The spectral factorization, the all-parameter nine-equilibrium/four-sink upper bounds, and hyperbolic continuation are established in `RESULT.md`; they are not inferred from any finite simulation. A separate independent review has not been performed.
