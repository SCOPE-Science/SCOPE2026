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

The analytic proof establishes the bound and the full set of equality cases for arbitrary admissible integers. To replicate finite checks run `python verify_inball.py` with SciPy installed. The checker solves 2,380 unsymmetrized Chebyshev linear programs for parameters with 8 through 21 ground elements, compares each numerical optimum to the three-barrier formula, and independently constructs feasible block-constant centers. Output: `ELEMENTARY_SPLIT_INBALL_PASS cases=2380 winning={'0': 605, 'L': 898, 'U': 877}`. These finite experiments are not a proof for unbounded parameters. No external audit has been conducted.
