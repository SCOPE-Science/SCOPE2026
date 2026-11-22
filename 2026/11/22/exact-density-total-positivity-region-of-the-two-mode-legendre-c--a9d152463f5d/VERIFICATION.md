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

# Verification of the density-TP2 theorem

Run `python3 verify.py` with Python 3 and the SymPy package. The checked source is the complete standalone `verify.py` supplied with this result.

Observed output:

```
VERIFICATION_OK rational_checks 12141 b_min -0.01823725421878943192327994
```

Symbolic assertions establish the polynomial determinant identity, the exact squared-boundary factorizations and the monotonicity derivative. Exact rational arithmetic checks the candidate inequalities on a finite grid and exhibits excluded examples. The full range of real coefficients and locations is proved analytically in `RESULT.md`; enumeration alone cannot establish those universal claims.

The historical novelty comparison uses the 2023 original preprint, the accessible full-text 2024 article, a 2025 follow-up, an earlier published exact copula-validity analysis, and the general density-total-positivity literature. Priority outside inspected sources is not independently certified.
