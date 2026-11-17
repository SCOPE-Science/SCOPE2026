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

The analytical proof uses a Fourier multiplier representation, Pauli-matrix anticommutation, an exact scalar maximization, and elementary convex support-function geometry. In particular, the two mass transitions are proved by the maximum and minimum of the same explicitly displayed quadratic. Boundary nonattainment is proved by the measure-zero Fourier maximizer set.

The supplementary script `check_numerical_range.py` (Python 3, NumPy) passed 2,206 assertions under the exact output `DIRAC_NUMERICAL_RANGE_DIAGNOSTICS_OK 2206`, checking grids of Fourier symbols and angular support functions, the paired radius formulas and the flat-face support slopes. Numerical grid checks do not establish infinite-dimensional bounds or exhaust all masses and directions; those follow from the proof.

The status above records only the current scientific review, not an independent validation.
