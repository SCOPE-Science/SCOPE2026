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

Run `python3 verify.py` with Python 3 standard library. Executed on the embedded verifier source with output:

```
VERIFY_OK residue_cases=29 primitive_residue_pairs=123 perfect_matching_comparisons=2703 prime_power_cases=112 divisibility_checks=900 exact_rational=yes
DENSITY n=4 value=2/3
DENSITY n=8 value=1/3
DENSITY n=27 value=3/4
DENSITY n=81 value=1/2
DENSITY n=108 value=1/12
DENSITY n=243 value=1/4
```

The verifier uses exact integer/rational arithmetic, directly enumerates periodic residue constraints, independently checks perfect matchings through a mask dynamic program for the tested examples, and compares the formula on prime powers and divisibility chains. The mathematical argument proves the result for all \(n\); finite checks do not establish its universal scope.
