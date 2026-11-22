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

# Verification details

`checker.py` executed with Python 3 and no third-party packages. It reports 542 exact-rational conditional-intensity enumerations for \(k\in\{2,3,4\}\), plus nine reproducible seeded simulations as finite diagnostics. Run with `python checker.py` from this directory.

The infinite assertions depend on an exact conditional-intensity identity, the binomial strong concentration estimate, a localized martingale-convergence argument for the logarithmic strong law, and the bounded-increment martingale central limit theorem. The complete hypotheses and normalization are written in `RESULT.md`. Checks of finite histories cannot substitute for the infinite proof. Independent external validation has not been performed.
