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

# Reproduction and limits
Run `python check_shadowing_two_regime.py` with a standard Python 3 interpreter. The finite checker uses deterministic random inputs and verifies 5,972 coordinate/norm assertions. No additional packages are required. The exact formula has a separate analytical derivation in RESULT.md: uniform upper bounds are supplied by convergent forward/backward series or a coordinate-defined split correction, and matching lower bounds use arbitrarily long forcing paths. Finite tests neither enumerate all errors nor establish the universal theorem. Independent mathematical validation has not been performed.
