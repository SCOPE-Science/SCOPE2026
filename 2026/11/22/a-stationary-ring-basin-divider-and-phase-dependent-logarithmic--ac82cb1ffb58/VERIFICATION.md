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

# Verification notes

The self-contained reproduction script `check_two_cycle_basin.py` is included. In a Python environment with SymPy and SciPy, run `python check_two_cycle_basin.py`; its successful output is `TWO_CYCLE_BASIN_CHECK_OK`.

The computation checks symbolic radial/angular reductions, roots and the critical coefficient, and uses numerical quadratures and ODE integration as diagnostics for the exact real-time period and leading exit-clock constant. These finite calculations do not establish global invariant-set classification, infinite-time convergence, all-parameter uniformity or publication priority. The analytic estimates in RESULT.md are required for those conclusions. No external independent mathematical audit was performed.
