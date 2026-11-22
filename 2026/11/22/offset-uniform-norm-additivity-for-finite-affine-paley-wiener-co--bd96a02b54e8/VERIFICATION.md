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

The exact Fourier transform of real-affine composition and the unitary logarithmic-coordinate map have been checked directly. The finite-packet overlap identity follows by integrating overlaps of translated intervals; the weakly-null property proves the essential-norm lower bound. The zero-offset upper bound follows from full-line Fourier multiplier theory. The phase criterion follows by expanding the triangle-defect identity and applying one-parameter Kronecker density. The example \((1,2,4)\) is verified by an exact quadratic maximization.

`witness_check.py` is executable with standard Python and checks finite-window witnesses for both resonant and nonresonant cases. A successful run prints `PALEY_MELLIN_OFFSET_WITNESS_OK 2148 resonant= 1.677050983125 generic= 2.284457050376 window= 2.283034713861`. Numerical witnesses do not replace the proof and do not establish any all-parameter result. No independent mathematical audit has been performed.
