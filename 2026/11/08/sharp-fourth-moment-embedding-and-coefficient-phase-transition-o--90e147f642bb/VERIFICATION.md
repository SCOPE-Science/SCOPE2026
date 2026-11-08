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

Run `python check_johnson4.py` from this folder, using Python 3 standard library only. The script performs exact Fraction computations, enumerates \(638\) two-level test cases over \(4\le n\le14\) and \(2\le k\le n-2\), directly computes sample-sum second and fourth moments over all subsets, compares the moment polynomial, verifies the phase expression against every two-level pattern, and constructs exact extremizing examples for all tested parameters, including odd \(n\). Its output ends `ALL_FIRST_JOHNSON_FOURTH_MOMENT_CHECKS_OK` when assertions hold.

The proof additionally requires an all-dimensional constrained-Hessian argument given in RESULT.md; the checks are finite corroboration, not exhaustive certification of arbitrary real coefficient vectors. A historical-equivalence search cannot establish absolute novelty. Independent audit: not performed.
