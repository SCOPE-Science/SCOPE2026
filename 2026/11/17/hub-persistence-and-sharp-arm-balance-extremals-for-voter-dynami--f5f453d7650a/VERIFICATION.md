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

# Reproduction checks

The analytic proof is in `RESULT.md`; the executable checks below are finite corroboration, not an infinite proof.

Run with Python 3:

```bash
python direct_ctmc_check.py
python interface_extremal_check.py
```

`direct_ctmc_check.py` requires NumPy and SciPy as specified in `requirements.txt`; `interface_extremal_check.py` uses only the Python standard library. Captured stdout is provided in `direct_ctmc_check.out` and `interface_extremal_check.out`. The first program builds the labelled peripheral configurations directly and solves the finite killed continuous-time voter generator rather than using the domain-wall formula. It covers 16 chosen spider profiles. The second uses rational first-step equations on path-interface states and verifies the arm-balance extremes by enumerating all integer compositions for 40 parameter choices, with 108 additional exact-rational interface tests.

The formula is asserted for all integer \(k\ge1\) and all positive integer arm lengths; the proof covers this infinite domain. Computation does not establish full historical priority, and independent validation has not been performed.
