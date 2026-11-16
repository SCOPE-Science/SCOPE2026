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

The complete exact rank-incidence certificate is implemented in `verify_f15_five.py` with only the Python standard library. Run:

```sh
python3 verify_f15_five.py f15_five_incidence.json
```

The script regenerates 201 translation orbits covering all 3,003 five-subsets, and tests 40,401 representative pairs over the integer cyclotomic quotient for the primitive fifteenth roots. It confirms the full rank census, the 360 rank-two structural cases, the 201-by-201 table, and the absence of rank-one cases. Modular elimination at two primes (31 and 61) supplies an independent rank lower-bound check for every representative pair; the two-prime maximum agrees with the exact integer result. The cyclotomic zero-minor tests, not finite-field results, prove the upper bounds.

These checks prove a finite enumeration under the stated algebraic reductions. They do not establish priority over inaccessible historical literature, generalizations to other Fourier orders, or independent human validation.
