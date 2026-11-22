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

# Mathematical and computational verification

The exact point-evaluation Riesz kernel was derived from the unique affine correction enforcing the zeroth and first Lebesgue moments. `check.py` reconstructs its Gram polynomial via symbolic interval integration, verifies the derivatives and every centring identity, checks the rational 0.00041 confinement threshold and the location/monotonicity endpoint inequalities, and solves the uniquely bracketed sextic root to 60 digits. It also compares 1,830 rational-grid pairs as corroboration. The global statement does not depend on the finite grid; it is proved with rational inequalities on the full location continuum and the uniqueness of a crossing of the two Rayleigh lower bounds.

Run `python3 check.py` with Python 3 and SymPy; a PASS report confirms the reproducible finite tests but is not a substitute for the proof in RESULT.md. The theorem is confined to real functions, two equally weighted values, two integral moments, second-derivative energy, and one unit interval. There is no independent mathematical audit, no formal proof-assistant verification and no claim of exhaustive historical-priority verification.
