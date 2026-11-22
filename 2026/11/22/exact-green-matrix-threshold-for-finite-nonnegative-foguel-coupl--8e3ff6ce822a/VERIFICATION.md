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

The proof in `RESULT.md` reconstructs the positive-matrix comparison, the half-line Green kernel, the singular-value Schur test, and the exact endpoint asymptotics. The standalone checker `checks/check_foguel.py` was run from this package and passed 151 supplemental numerical comparisons of positive finite-band matrices, matrix-unit secular curves and the exact two-way polynomial identity. Run `python checks/check_foguel.py` with Python 3, NumPy and SciPy. Matrix compressions approximate but cannot prove infinite spectral inequalities, and the independent audit has not occurred.
