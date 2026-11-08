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

# Reproduction and mathematical limits

Run `python3 verify.py` using Python 3 standard library only. The checker independently constructs the transition matrix for a continuous-time finite-state voter process, tests the edge-expanded generator expression over all states of all labeled connected graphs through five vertices, then solves exact-rational finite absorbing-chain Dirichlet linear systems for representative cases.

The tested output is:
```
VERIFY_OK graphs=771 generator_assertions=54452 exact_absorption_chains=18
```

This finite check does not certify all graph sizes or uncountably many real preferences. Those cases are covered by the self-contained analytic graph-generator/Walsh-coefficient proof in RESULT.md. The computation checks finite examples, algebraic normalization, and negative tests for nonalternating preferences. It is not a formal proof assistant or independent external validation. The tested model has only the two unanimous absorbing states because all discordant copying rates are positive.
