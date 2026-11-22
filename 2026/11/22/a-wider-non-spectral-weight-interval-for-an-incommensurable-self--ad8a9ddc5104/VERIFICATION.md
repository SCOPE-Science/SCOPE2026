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
The finite certificate uses `verify_differences.py` in this package. Execute with `python3 verify_differences.py` and a standard Python 3 interpreter; no network or third-party packages are required.

The two complete finite translation sets are computed by the exact recurrence and shown to have cardinalities 48620 and 4368. The bitset difference computation determines their first missing nonnegative difference as 3163277 and 92381. Thus, together with symmetry, the required full intervals in the difference sets are established. All four root-bracketing inequalities and both overlap-point inequalities are checked over exact rational numbers. The analytic implication from these certificates to non-spectrality is supplied in RESULT.md and depends on Parseval and the positive Dirichlet-polynomial atom bound, not on a finite numerical extrapolation.

The computation does not establish spectrality at any remaining weight. Independent mathematical audit has not been performed.
