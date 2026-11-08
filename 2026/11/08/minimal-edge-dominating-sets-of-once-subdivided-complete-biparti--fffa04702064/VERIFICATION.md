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

# Verification of the stated polynomial

Run `python verify.py` with a recent Python 3 interpreter (3.9+) using only the standard library. The program implements the actual subdivided graph's edge adjacency and separately enumerates predicted incidence configurations, cross-checking the complete families and polynomial coefficients for eleven small bipartition-size pairs. It also tests seven larger predicted families directly, verifies the upper missing-cardinality interval for a finite rectangular range, and checks star boundary values.

Observed return:

`VERIFY_OK exact_cases=11 exhaustive_subsets=403028 exact_minimal_sets=1334 additional_cases=7 generated_tested=138494 all_coefficients=PASS all_families=PASS upper_gaps=PASS stars=PASS`

For the exhaustive cases, the 403,028 total edge subsets are all evaluated against the original domination definition and every single-edge deletion. For larger cases the 138,494 generated sets are checked, **not** every edge subset. The tests provide finite corroboration only; the general polynomial and the unbounded gap follow from the proof. The archival literature-priority check is provisional; no independently performed audit is asserted.
