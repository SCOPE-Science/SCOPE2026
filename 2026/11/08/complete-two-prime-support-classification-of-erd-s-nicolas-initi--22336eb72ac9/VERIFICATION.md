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

The standalone Python 3 script `verify.py` uses exact integer arithmetic. Its saved-run output was:

```
VERIFY_OK
full_prefix_cases= 8000
positive_prefix_instances= 5
three_adic_straddles= 323
three_adic_formula_tests= 336
exact_integer_arithmetic=True
```

The main grid checks every sorted proper-divisor prefix for 20 choices of dyadic exponent, 10 choices of odd-prime exponent, and 40 odd primes below 181. An independent test verifies that adjacent proper divisors straddle the target in the excluded ternary cases. The last test checks exact formulas at the three critical prime-power cutoffs.

These computations cover only the stated finite grid. Universal exclusions follow from the written inequalities and exact consecutive-divisor identities, not from assuming experiments are exhaustive over all integers.
