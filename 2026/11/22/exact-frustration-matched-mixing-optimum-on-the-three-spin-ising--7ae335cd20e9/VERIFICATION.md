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

# Verification

Run `python3 verify.py` using a Python 3 standard-library installation. The program constructs all eight spin states, computes continuous-time heat-bath flip rates with exact fractions for rational Boltzmann activities, and verifies the action of the full generator on the constant, three linear, three quadratic, and one cubic spin monomials. It tests 64 independent pairs of rational activities and checks 4096 monomial actions exactly.

The verification result obtained from this package's `verify.py` is:

```
GENERATOR_MONOMIAL_IDENTITIES_OK 4096
INDEPENDENT_EXACT_RATIONAL_PARAMETER_PAIRS 64
```

This finite test does not establish the universal theorem by itself. The analytic monomial-sector decomposition, spectrum comparison, monotonicity derivatives and low-temperature limit appear in `RESULT.md`; no independent audit was performed. The historical novelty assessment includes an inaccessible six-spin source and remains provisional.
