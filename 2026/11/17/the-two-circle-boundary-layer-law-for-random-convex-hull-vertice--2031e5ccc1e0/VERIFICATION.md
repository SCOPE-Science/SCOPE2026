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

# Verification of the two-circle boundary-layer law

The exact finite configuration criterion is derived algebraically from supporting normals; it was compared with a direct Euclidean convex hull computation on random outer/inner circle configurations. Poisson nearest-neighbor convergence and two-location asymptotic independence are mathematical steps established in RESULT.md, not simulation inferences.

The executable checker evaluates the two-dimensional crossover integral by adaptive quadrature, checks its numerical endpoints and compares the integral against Monte Carlo at several sample sizes and parameters. The \(L^2\) theorem and sharp scaling require the proof and are not verified by finite experimentation alone.

Run `python check_two_circle_hull.py` after installing the packages in `requirements.txt`. No external data or network access is required.

Independent audit: not performed. The result is a self-review with documented historical-priority limitations.
