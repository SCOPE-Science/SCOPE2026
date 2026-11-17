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

# Verification and limits

The included `verify.py` uses only the Python 3 standard library. It derives Hermite polynomial differentiation identities using exact integer coefficient arrays, locates positive roots by recurrence and bisection for degrees 1–30, checks strictly decreasing positive critical amplitudes, and tests both parity correction formulas and the first-even-zero expansion at larger degrees.

Observed successful output:

```
EXACT_HERMITE_DIFFERENTIATION_IDENTITIES_PASS 30
ALL_POSITIVE_HERMITE_CRITICAL_ROOTS_AND_SHARP_STEPS_PASS 30
PARITY_CORRECTIONS_AND_FIRST_POSITIVE_ZERO_ASYMPTOTICS_PASS
ALL_GAUSSIAN_BV_HERMITE_COEFFICIENT_CHECKS_PASS
```

This is finite diagnostic evidence, not an infinite verification or independent audit. The unrestricted mathematical conclusion is proved analytically in `RESULT.md`. The result applies to globally finite-variation functions that need not belong to Lebesgue \(L^1(\mathbb R)\).
