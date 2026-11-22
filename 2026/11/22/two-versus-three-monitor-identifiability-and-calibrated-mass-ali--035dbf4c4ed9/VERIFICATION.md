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

The accompanying `checker.py` is a standalone Python 3 standard-library diagnostic. It was run from this package and reported `PASS 4215 checks`. It uses 150 deterministic parameter sets, tests the two-monitor cross-side alias at six positive times per monitor, checks reconstruction from three known-onset post-release times, and tests the exact same-mass logarithmic collision. Its numerical tolerances are specified in the script.

The universal continuum statements do not follow from 150 test cases: they follow from the three-coefficient log-trace identity, a strict squared-distance ratio for upstream sources, exact cross-side coefficient matching, and quadratic interpolation from three sensor coordinates. The proof covers all noncoincident sensor/source configurations in the claimed positive-parameter ranges. Temporal onset must be separately observed before the three-sample reconstruction applies.

Full-text historical priority is not independently certified. No empirical detector noise or finite-domain behavior has been validated.
