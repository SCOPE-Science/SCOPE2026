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

The accompanying standalone `verify.py` uses only the Python standard library. Running `python3 verify.py` recomputes all unsigned four-dimensional zonotope minor sums exactly, including the dependence on the tilt, and checks the resulting phase identity on 512 rational parameter pairs. All determinant roots are exhaustively collected from the finite coefficient pairs, so chamber-affinity is a symbolic conclusion. The exact sign analysis in `RESULT.md` is the proof for the continuum and is not replaced by sample tests.

Full source coordinates and the assumptions \(t\ge0\), \(z\in\mathbb R\) are given in `RESULT.md`. The arbitrary-dimensional lift uses only Cartesian products with unit cubes. No independent mathematical validation has been performed.
