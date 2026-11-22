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

# Reproduction

Run `python verify.py` with Python 3 and the packages indicated by `requirements.txt`. The verifier evaluates exact SymPy identities for the central numerator, denominator, and leading series; verifies coefficient inequalities for indices 4 through 99; independently solves the three-point original kernel matrix at 90-decimal-digit precision for 360 seeded pairs of node positions and inverse lengthscales; and checks 12 flat-limit approximations and both subcritical signs, including critical-boundary positivity.

Observed output:

```
PASS: 4 symbolic identities/series, 96 positive series coefficients, 372 high-precision linear-system and limit checks; both subcritical signs.
critical spacing: 0.5227744249483388654303021719919786604726
```

The global theorem is proved by the analytic strict-integrand inequality and the positive-coefficient power-series induction in `RESULT.md`. Finite computation is not interpreted as an infinite-domain certificate. An independent mathematical audit and literature-priority certification have not been performed. The proof does not determine the number of central-weight zeros at subcritical spacing.
