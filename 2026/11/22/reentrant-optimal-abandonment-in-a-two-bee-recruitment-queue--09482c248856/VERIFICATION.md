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

# Verification of the conditional finite-state result

Run `python verify.py` with Python 3 and SymPy. The independent transient generator uses four nonabsorbing states: searching with and without the first fed scenter; waiting with and without that scenter. The donor's service of a fed bee makes no state change and is correctly thinned. All clocks are independent and exponential under the stated reduced-chain assumptions.

The checker recomputes the expected hitting time by exact matrix inversion and compares it to the rational formula, checks its derivative polynomial and endpoint means, proves the exact critical discriminant identity, tests radical optimizers at three rational parameter regimes, and performs 60 independent rational inverse-generator comparisons. The packaged checker was run successfully from its current file path. The infinite parameter conclusion rests on the analytic quadratic sign proof in RESULT.md, not the finite test grid.

The computed theorem is **not** a certificate of the spatial velocity-jump model, an empirical prediction, or an independent external audit. No external validation has been performed.
