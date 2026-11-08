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

# Verification record

Run `python verify.py` with Python 3, SymPy and NumPy from the extracted file directory. The reproduced output was:

```
VERIFY_OK symbolic_identities=5 exact_parameter_cases=121 noninvariant_competitors=2700
```

The five algebraic checks evaluate the exact discriminant square, the threshold root identity, the threshold derivative, the comparison to the star gap, and the saturated hub budget. The 121 parameter cases independently construct full stochastic matrices for \(2\le a,r\le12\), compare complete matrix eigenvalues with the quotient and transverse decomposition, and verify the claimed SLEM. The 2700 non-invariant samples compare independent feasible edge assignments on smaller graphs against the formula. These experiments are supplementary and do not establish a universal optimization theorem, exhaustive optimizer classification, or independent verification. The general claim rests on the explicit analytic inequalities in `RESULT.md`.
