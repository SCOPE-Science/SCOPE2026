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

The package contains `verify.py`, which requires the standard Python library only. Run `python verify.py` to check exact modular row-space equality for the original quadratic derivative generators and the four asserted normal forms in characteristics \(2,3,5,7\) with \(4\le n\le10\), and to enumerate finite-field supports in twenty of these cases. The observed output is:

```
QUADRATIC_IDEAL_SPAN_EQUALITIES_OK 112
FINITE_FIELD_SUPPORT_CHECKS_OK 20
ALL_FOUR_CASES_COVERED [('axes', 68), ('axes_diagonal', 21), ('quadratic_double', 8), ('star_planes', 15)]
CERTIFICATE_OK
```

The expected identities are justified in the written proof by a four-cycle quotient and its determinant, independently of the finite tests. The quotient radical and Cohen–Macaulay arguments prove the global geometric assertions. Finite-field point enumeration does not certify radicality and modular span testing across bounded dimensions does not prove the all-parameter statement. No independent audit has been performed.
