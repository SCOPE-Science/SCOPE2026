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

Run `python3 verify.py` from the extracted package directory. The verifier uses Python's standard library and exact integer arithmetic. It independently enumerates the residues counted by the second Schemmel totient for every integer from 1 to 500, compares the resulting iterate sums, tests 1776 prime powers with primes at most 10000 and powers at most 10 million, checks the sharp surplus and equality cases, and enumerates the odd-input fiber at value 3 up to 100000.

Observed output:

```
VERIFY_OK
direct_definition_n=1..500
prime_power_cases= 1776
prime_bound=10000 power_bound=10000000
minimum_positive_surplus= 2 at [(7, 1), (11, 1), (17, 1)]
fiber_L2_equals_3= [5, 9, 15] searched_n<100000
exact_integer_arithmetic=True
```

The unrestricted classification is a proof from elementary divisibility and iteration identities, not an extrapolation from tested inputs. The program does not independently assess historical priority.
