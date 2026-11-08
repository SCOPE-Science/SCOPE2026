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

# Verification of exact reduced denominators

Run `python3 verify.py`. The script uses only integer arithmetic, `fractions.Fraction`, and binomial coefficients from the Python standard library. It reconstructs each alternating cotangent block using Newton's identities for the even- and odd-root polynomials, then applies the exact specialized affine-divisor reduction.

Observed execution:

```
BLOCK_AND_AFFINE_OK a=1 n=6 denominator=27 numerator_mod_3=1
BLOCK_AND_AFFINE_OK a=2 n=18 denominator=19683 numerator_mod_3=1
BLOCK_AND_AFFINE_OK a=3 n=54 denominator=7625597484987 numerator_mod_3=1
VERIFY_OK exact_rational_arithmetic=true finite_only=true independent_audit=false
```

The first two exact rational affine sums also match the earlier published table. The computations verify particular exponents and do not establish the claimed uniform theorem; the general proof relies on exact cyclotomic \(3\)-adic valuations and the dominance of one divisor contribution. No independent mathematical audit has been performed.
