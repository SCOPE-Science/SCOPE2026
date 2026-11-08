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

# Verification of the exact conductor and normalization-defect formulas

The general proof consists of five independent steps: identify the normalization; prove the exact monomial criterion \(u(a)\ge q(b)\); pass from all \(y\)-shifts to the conductor condition \(u(a)\ge Q(b)\); count the missing monomial basis using residues modulo \(\lambda_i\); and sum numerical-semigroup blocks when \(m=n+1\). Each quantifier and parameter boundary is specified in `RESULT.md`.

Execute the accompanying Python 3 script as `python3 verify_normalization.py`. It directly enumerates generator decompositions instead of assuming the gap criterion, and checks 138 finite parameter tuples. The observed output is:

```
NORMALIZATION_DEFECT_AND_CONDUCTOR_FINITE_CHECK_OK 138
```

The script only corroborates a finite portion of the result. It is not an exhaustive enumeration of all coprime pairs or all dimensions. Historical priority and independent scientific assessment have not been certified. A relevant 2018 paper's full text was not accessible; see `RESULT.md` for its identifier and the resulting priority limitation.
