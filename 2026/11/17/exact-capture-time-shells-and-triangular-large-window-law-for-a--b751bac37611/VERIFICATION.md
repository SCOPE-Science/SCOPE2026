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

# Verification notes

The proof establishes an exact integer-square factor map, an exhaustive nonnegative rank table and the strict one-step descent law. A lattice count gives every area shell; a deterministic error bound gives the macroscopic limiting distribution and its Wasserstein-1 estimate.

The bundled `check.py` was executed with Python, returning `QUARTER_TURN_EXACT_LATTICE_AND_SHELL_CHECK_OK`. It checks the square map and fourth iterate at exact rational test points, rank descent on 251,001 integer square labels, and the first 80 pairs of shell counts. These checks are finite and do not certify the global theorem on their own.

The domain excludes all integer grid lines. The proof does not assert a unique extension to grid-line points. Publication-priority risk remains for inaccessible complete literature; independent audit has not been performed.
