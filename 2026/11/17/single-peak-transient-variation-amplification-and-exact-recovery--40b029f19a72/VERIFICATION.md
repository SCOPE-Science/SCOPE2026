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

# Reproduction and scope

Run `python3 check_three_site_heat.py` using Python 3 with only the standard library. The checker independently evaluates the original Markov heat via stochastic-matrix uniformization, then compares it with the two spectral gradient-column formulas over 350 deterministic random positive-rate and weight selections. It tests the initial-slope incompatibility, the one-peak formula, strict contraction of the opposite column, unique positive recovery root (via bisection), and exact-algebra golden-ratio identity.

Observed output:

```
INDEPENDENT_MARKOV_UNIFORMIZATION_350_CASES_PASS
SINGLE_PEAK_AND_UNIQUE_RECOVERY_CHECKS_PASS
EXACT_GOLDEN_RATIO_RECOVERY_IDENTITY_PASS
ALL_THREE_SITE_HEAT_CHECKS_PASS
```

Numerical uniformization tests are not proofs for arbitrary rates or times. The proof in `RESULT.md` handles the unrestricted positive-real parameter domain analytically. No external independent mathematical audit has occurred.
