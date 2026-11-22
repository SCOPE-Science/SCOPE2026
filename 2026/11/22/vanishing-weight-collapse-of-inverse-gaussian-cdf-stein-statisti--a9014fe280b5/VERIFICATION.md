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

# Reproducibility and verification

Run `python check.py` with Python 3 and the installed `numpy`, `scipy`, and `sympy` packages. The script contains 50 assertions: exact sample values and finite plateau, the independent raw-coordinate four-function representation, symbolic moment/variance identities, two weighted finite-sample small-parameter limits, and a seeded IG Monte Carlo cross-check (7,000 replications, sample size 1200, shape 2).

Observed output: `checks_passed: 50`, exact \(C_{\mathrm{MO}}=-1/6\), \(C_{\mathrm{ML}}=0\), symbolic variance `6*r**3` where `r=1/phi`; Monte Carlo standardized mean `-0.06388419767436038`, standard deviation `0.97478286835517` and chi-square 95%-cutoff exceedance `0.046285714285714284`. The exact weighted integral contributions beyond the observed maximum are included analytically, not truncated.

The infinite-sequence result is proved in RESULT.md by a four-basis unweighted Hilbert-space argument and an ordinary one-dimensional CLT. Numerical simulation provides no independent certification and does not validate empirical power or a bootstrap. Independent audit status: not performed.
