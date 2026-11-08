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

The claimed component theorem follows from the explicit normal-form and valuation-stratification proof in `RESULT.md`; computations do not establish geometric irreducibility for all lengths.

Reproduce direct counts using a C++17 compiler:

```sh
g++ -O3 -std=c++17 -o check_jets check_squarezero_jets.cpp
./check_jets
g++ -O3 -std=c++17 -o check_mixed check_mixed_chain.cpp
./check_mixed
python3 check_normal_form_centralizers.py
```

The outputs must end with `ALL_3X3_SQUAREZERO_JET_EXHAUSTIVE_TESTS_PASS`, `ALL_3X3_SQUAREZERO_MIXED_CHARACTERISTIC_TESTS_PASS`, and `ALL_3X3_SQUAREZERO_CENTRALIZER_CHECKS_PASS`. The recorded results appear in the three `.out` files. No external dataset is required. The checks are exhaustive only for the ring parameters printed. The first checker enumerates necessary residue-square-zero matrices and every lift; this is an exhaustive pruning rule, not statistical sampling. The mixed-characteristic checker uses ordinary integer multiplication modulo the ring modulus, independently of the polynomial-ring arithmetic. The centralizer checker tests the two distinct trace values in a length-two binary chain ring. The data do not verify all prime powers, all finite chain rings, or arbitrary jet length.
