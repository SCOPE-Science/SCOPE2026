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

# Reproducible checks

Run `python3 checker.py` with Python 3 and standard library only. This file is a standalone verification program, not a formal proof engine.

The actual executed output was:

```
INDEPENDENT_EXACT_HILBERT_PROFILE_AND_GREEN_IDENTITY_OK 2765
ALL_CANDIDATE_EXTREMA_AND_DESIGN_DEFICITS_OK 125 125
UNIFORM_CIRCLE_BASELINE_OK 1/12
BALANCED_ANTIPODAL_EXAMPLE_OK 19/192
ALL_TWO_ATOM_CIRCLE_SOBOLEV_CHECKS_OK
```

The first test derives squared evaluation norms by integrating an explicit periodic derivative-dual profile over rational subintervals and compares them with the independently derived circle-resistance formula. It does not simply substitute the proposed maximum back into itself. The second test compares every candidate arc vertex and checks the symbolic design deficit over all tested rational profiles. These exact finite checks are useful reproducibility evidence, not an exhaustive continuum or originality proof. The continuum proof is contained in RESULT.md.
