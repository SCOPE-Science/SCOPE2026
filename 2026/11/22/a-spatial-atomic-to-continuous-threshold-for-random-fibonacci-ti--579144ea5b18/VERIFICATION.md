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

# Mathematical verification

Reproduce the finite checks with `python3 check.py` from the directory containing `check.py`. The script uses only Python 3's standard library and does not need internet access or downloaded source papers. It independently enumerates placement-bit subsets for the checked finite instances and compares their spatial histograms to the binary-carry formula using exact fractions. It also tests the exact finite mean, the exact doubling boundary for geometric weights, and integer geometric ratio-three weights. Selected limiting masses are compared numerically at a finite truncation and should be interpreted as diagnostics only.

The verified replay returned `PASS 726 exact finite assertions / asymptotic diagnostic comparisons` followed by `PASS cumulative 845`. Exact finite enumerations do not establish the infinite-scale theorem; the infinite-scale claims are justified by the ratio-limit argument, discrete total-variation convergence and binary-expansion weak convergence in `RESULT.md`.

No independent external mathematical audit has been performed, and priority beyond the inspected material remains open.
