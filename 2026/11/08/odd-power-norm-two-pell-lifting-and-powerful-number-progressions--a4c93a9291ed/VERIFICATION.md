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
# Exact verification notes

Run `python3 verify.py` using the Python standard library. The package's verifier calculates norm-two powers in two different ways: algebraic binary exponentiation by the integral norm-one multiplier and a direct binomial expansion. These agree in \(30\) cases across three source multipliers and ten odd indices each. Nine further higher odd-power coefficient cases cover \(r=1,2,3\) for each multiplier. All tested norm equations, valuations, and powerful-number progressions agree.

The program prints:

```
VERIFY_OK exact_cases=39 m=[7,23,31] odd_power_levels=1,2,3 second_multiplier=23
M7 r1 X=11427 Z=617
M23 r1 X=15191131279719638885 Z=137720427724123513
```

The universal proof relies on the integral norm-one multiplier, the binomial valuation bound, and the modulo-eight parity obstruction. No finite computation was treated as an exhaustive test of infinitely many multipliers or exponent levels. Independent mathematical audit and full historical-priority certification have not been performed.
