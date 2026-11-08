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

The companion file `theta_exact_check.py` was executed with the installed Python standard library and returned:

```
EXACT_KIRCHHOFF_POISSON_AND_ENERGY_OK 8190
MAXIMAL_MIDPOINT_AND_LONGEST_PATH_OK
SHARP_EQUILATERAL_AND_CYCLE_SHAPE_BOUNDS_OK
ALL_PARALLEL_PATH_SOBOLEV_CHECKS_OK
```

For each tested positive rational collection of lengths, path and point, the checker constructs a piecewise-quadratic function with a unit derivative jump at the sample location, Kirchhoff matching at both shared endpoints, and zero arclength mean. It checks exact equality of that function's evaluation, derivative energy, and the proposed analytical kernel. It independently verifies the sharp midpoint and graph-shape bounds on its finite sample. A separate analytic proof proves the result for all real positive lengths; the checker cannot certify the infinite statements on its own.

The finite enumeration uses \(2\le r\le5\), each length chosen from positive rational alternatives with position choices at the endpoints, the midpoint and two other interior fractions. The circle case and the strict multi-path case are both represented. No external numerical packages, remote services or unprovided files are needed.
