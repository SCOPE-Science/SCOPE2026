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
# Reproducibility and proof boundaries

Run the following from a directory containing all three files:

```sh
python3 orbit_census.py
python3 generator_closure.py
python3 direct_composition.py
```

These are ordinary Python 3 programs requiring only the standard library. The first computes conjugacy orbit counts for all degrees one through six and checks the exact labeled and multiset counts by root rank and involution transposition count; the second computes generated semigroup closures for degrees five and six, recovering all 511 and 3427 monoid endomorphisms from generating sets of sizes 10 and 16, respectively; the third compares the compressed multiplication rule with explicit composition of maps on transformations in the five-point case.

The check programs must terminate with `UNITAL_ENDOMORPHISM_ORBIT_CHECKS_PASSED`, `UNITAL_GENERATOR_CLOSURE_CHECKS_PASSED`, and `DIRECT_COMPOSITION_CHECKS_PASSED`, respectively. All-degree correctness rests on the structural proof and the cited classical classification, not on extrapolation of those finite calculations. No independent mathematical audit, third-party validation, or machine proof of the infinite statement has been performed.
