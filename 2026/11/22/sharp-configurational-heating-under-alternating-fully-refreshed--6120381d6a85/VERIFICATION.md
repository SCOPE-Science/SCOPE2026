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

# Verification and limits

Run `python verify.py` after installing the optional symbolic-checking dependency with `python -m pip install -r requirements.txt`. The script uses exact symbolic reductions for seven critical identities, verifies two independent rational examples, compares 120 independently propagated full two-state BAOAB covariance cycles with the closed forms, and performs 15,000 supplementary interior-domain inequality checks.

Observed output:

```
PASS: 7 exact symbolic identities
PASS: 6 exact rational phase moments
PASS: 120 direct 2x2 matrix-covariance comparisons
PASS: 15,000 finite-domain supplementary inequalities
All checks passed. Global bounds and uniqueness are proved analytically in RESULT.md.
```

The theorem's infinite-domain and sharpness statements depend on the analytic positivity and fixed-sum argument in `RESULT.md`; finite checks do not certify them. The analysis does not evaluate nonperiodic schedules, finite thermostat memory, general potentials, or equal-physical-time observables. Publication priority has not been independently certified.
