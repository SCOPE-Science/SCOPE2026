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

The infinite-series identity and its tail bound are proved analytically in RESULT.md, as are the diffuse triangular-array central limit theorem, the iid-length specialization, and the explicit one-spike counterexample. The direct checker is an independent finite consistency test, not a substitute for these arguments.

Run `python weighted_zonogon_check.py` (requires Python, NumPy, SciPy) from the directory containing that standalone file. The checker compares the determinant sum with convex hull areas and perimeters of all subset sums; checks a large finite Fourier partial sum; estimates means and Laplace transforms using a fixed random seed for equal, binary-length, and single-spike arrays; and distinguishes their theoretical limits. For a single spike, the finite-sample mean is centered using the finite value of the squared-weight sum, not its asymptotic value.

Unproved limits: no rate of weak convergence, no density formula for arbitrary non-diffuse weight arrays, no moment convergence under only a finite second radial moment, and no universality under non-Haar directions. The computed sample statistics are corroborations only. Independent audit: not performed.
