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

The standalone `checker.py` was executed with Python, NumPy, and SciPy. It computed the isolated-hole area by one-variable circular integration, enumerated cover counts on the boundary of a surviving disk, and enumerated the number of covering corners in the critical unit square. The completed calculation printed `SQUARE_COVERAGE_TWO_SCALE_CHECK_OK`. Sample ratios at radius deficits \(0.1,0.05,0.02,0.01,0.005\) showed convergence to the limiting constants four and eight. At the critical radius the quadratic boundary coefficient was exactly \(4\pi/3\) to enumeration precision. These computations test selected cases and do not prove a continuum statement by themselves; the exact analytic proof is in `RESULT.md`.

Independent validation has not been performed.
