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

# Verification of calibrated polygonal affine flows

Run `python verify.py` with Python 3, SymPy, NumPy, and SciPy. The script is self-contained and reads no external numerical files.

The symbolic part expands the actual planar affine vector field in the geometric edge basis and verifies the normal and tangential calibration identities. The numerical part selects two different admissible pentagons, constructs the physical affine field directly, integrates 1280 intramode point/time evaluations, checks 50 cumulative first-return steps, and independently compares event times. The tested radial domain is \(0<r<3.25\) for \(a=0.8\) and modal speeds \((1.1,1.3,0.9,1.7,1.2)\). A successful run reports:

`VERIFY_OK symbolic_vector_identity=True local_ode_checks=1280 full_cycle_step_checks=50 polygon_shapes=2 forward_radius=3.25 shape_invariant_event_times=True`

This finite verification neither replaces the proof for all star-shaped polygons nor verifies any statement about the exterior of the invariant domain. The proof is provided in `RESULT.md`. This record has not undergone an independent audit.
