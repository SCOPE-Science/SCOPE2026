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

# Reproduction and limits

Execute `python check.py` with Python 3 standard library. The checker constructs the inverse convolution kernel from \(\sum_{j=0}^{N-1}(-1)^j\delta_j\) at each odd cycle length between 3 and 101 and each depth between 1 and 9. It independently checks the antiperiodic recurrence, verifies exact identity after applying all smoothing steps, and tests the four exact low-depth norm formulas. Additional tests examine the zigzag recurrence, finite Fourier multipliers and sampled convergence rates.

A successful run reports 1,149 structural/inverse/norm assertions (some counted assertions bundle multiple integer comparisons). Finite computation does not prove the all-order theorem, which relies on the group-ring identity, polynomial recurrence and Euler polynomial Riemann-sum argument. Numerical checks do not certify infinite-dimensional or large-order behavior. Independent audit: not performed.
