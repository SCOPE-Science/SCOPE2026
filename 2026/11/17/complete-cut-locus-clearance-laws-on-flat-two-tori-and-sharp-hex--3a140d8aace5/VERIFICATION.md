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

# Reproducibility and checks

Run `python check_cut_clearance.py` after installing NumPy (see `requirements.txt`). This script independently integrates the six Voronoi-eroded facet inequalities by polygon clipping, tests Gauss-reduced parameters throughout all branch regimes, and performs finite Monte Carlo nearest-lattice sampling. The deterministic execution printed:

`PLANAR_TORUS_CUT_CLEARANCE_OK 158 29 6 max_clip_error 6.994e-15 max_dominance_defect 2.220e-16`

Checks cover the formula in rectangular, rhombic, square, equilateral and generic skew cases. The numerical clipping, simulations and finite parameter sweep do not prove universal quantifiers, uniqueness, or historical priority. The accompanying written proof supplies the analytic argument and cites standard geometric inputs; independent external audit has not been performed.
