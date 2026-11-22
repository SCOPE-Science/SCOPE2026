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

- Direct algebra verifies the four branch images and full-covering transition matrix in RESULT.md for every strict admissible real parameter.
- The transpose transfer recurrence gives a closed vector exactly for each nonnegative integer horizon.
- `python3 checker.py` checks 42 rational parameter pairs across 11 survival horizons using independent exact-rational inverse-image interval recursion and confirms two non-reflection-related fixed-width examples have different conditional terminal weights.
- The finite checker does not prove infinite-horizon results; those follow from the symbolic matrix identity and simple normalization in RESULT.md.
- Endpoints and the discontinuity affect a Lebesgue-null set only; no unsupported exhaustive search or independent audit is claimed.
