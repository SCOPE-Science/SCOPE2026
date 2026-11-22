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

# Verification details

`CHECKER.cpp` can be compiled with `g++ -std=c++17 -O2 CHECKER.cpp -o checker && ./checker`. The complete Walsh transforms in binary matrix sizes two, three, four and five have respectively 4, 64, 4096 and 1,048,576 characters, and the checked valuation exponents are 0, 1, 3 and 6. The program verifies each frequency's congruence and that no coefficient vanishes.

`CHECKER.py` can be run with `python3 CHECKER.py`; it independently checks the rank-character formula, diagonal projection and direct character sums for every frequency up to size four, and samples the size-five diagonal formula. Both programs returned PASS in their current versions. The infinite-size assertion is proved algebraically in `RESULT.md`; finite experiments alone would not establish it.

Independent audit has not been performed. The checks do not cover other fields or arbitrary forbidden-entry patterns.
