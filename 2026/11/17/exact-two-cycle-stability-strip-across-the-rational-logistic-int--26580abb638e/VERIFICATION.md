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

The accompanying scientific checker is `verify.py`, requiring Python 3 and SymPy. It symbolically verifies (i) the exact factorization of the double iterate; (ii) the discriminant and boundary values of the quadratic two-cycle factor; (iii) the symmetric derivative product; (iv) the rational endpoint quartic and invariant-domain endpoint formula. Seven sample interpolation strengths and 21 nondegenerate numerical cycle cases independently corroborate the location of each neutral threshold, the explicit cycle points and their multiplier. The completed run returned:

```
VERIFY_SYMBOLIC factorization=1 discriminant=1 boundaries=1 multiplier=1 endpoint=1 quartic=1
VERIFY_OK exact_identities=6 lambda_cases=7 two_cycle_cases=21
```

The proof's universal inequalities (monotonicity, uniqueness, endpoint ordering) are analytical; finite numerical tests do not prove them. The theorem has not undergone independent scientific review or validation. The secondary neutral multiplier alone does not prove that a period-four orbit is born there.
