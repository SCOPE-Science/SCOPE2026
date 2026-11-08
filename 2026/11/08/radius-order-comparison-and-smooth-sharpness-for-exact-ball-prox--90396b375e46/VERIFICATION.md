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

# Reproducible evidence

Run `python verify.py` using the Python standard library. The deterministic script performs 960 numerical comparisons of independent positive-definite diagonal quadratic ball-proximal trajectories with independently ordered radius schedules, then finds examples attaining \(N_1=d\) in dimensions \(2\) through \(7\) using the explicit geometric stiffness family. The high-precision Decimal scalar-multiplier bisection solves the exact quadratic KKT equations to a specified numerical tolerance; its successful output starts with `VERIFY_OK`. It verifies test instances only, not all possible radii, real dimensions or all positive parameters.

The universal mathematical evidence is the analytic argument in RESULT.md: (i) unique positive multiplier and nonnegative coordinates, (ii) monotonicity of scalar prox outputs and displacements, (iii) comparison of multipliers for ordered vectors and radii, (iv) strict transformed coordinate \(\ell_1\)-length budget and (v) inductive singular-hierarchy smooth quadratic construction. No external proof certification or independent audit is claimed.
