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

Execute `python3 check_bilateral.py` with the Python standard library. The program checks the original two-output normalized filter against its mean/contrast reduction, computes the two power-family derivative and Gaussian derivative expressions by symmetric finite differences, compares many secants with the proved bounds, tests maximizing contrasts and the unique Gaussian scalar root, and compares 90,000 pairs in several coordinate norms.

The standalone script prints `ALL_TWO_SITE_BILATERAL_CHECKS_PASS` and `DIRECT_ALL_ELL_Q_PAIR_BOUNDS_PASS_90000` when its tests succeed. The unrestricted mathematical assertions are proved in `RESULT.md` and are not inferred from finite random testing. A failed checker must be investigated before relying on any numerical evidence.

# Scope of verification

The tests use finite random sampling and finite precision, so they do not establish global maximality, uniqueness, or the if-and-only-if criterion by themselves. Those are proved by reduction to a scalar contrast map and analytic maximization. Absolute and relative numerical tolerances are used only for comparing independently evaluated formulas. No external validation is asserted.
