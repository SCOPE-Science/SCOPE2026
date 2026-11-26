---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Analytical and computational verification

The two sharp frame-bound formulas and finite-redundancy optimizer premises come from Faulhuber–Shafkulovska, arXiv:2204.02917, §8. Differentiated uniform expansions in the bounded additive strip give the two individual optimizer offsets, and value expansions give their compact-uniform loss profiles. The earlier condition-number optimizer offset is used as an input; evaluating the two loss profiles there yields the two positive regret coefficients.

The accompanying `check_gabor.py` uses Python 3 and `mpmath`. The script covers five redundancy values for the bounded-strip expansions and optimizer checks, four sample truncated Walnut multipliers at each of the two extremizing phases, and both scaled regret coefficients. Some of its tests also check the prior condition-number asymptotic. The expected successful output is `GABOR_HIGH_DENSITY_CHECKS_PASS 76`. Finite numbers and truncations are diagnostics, not universal tail certificates, proofs of the limits, or priority evidence.
