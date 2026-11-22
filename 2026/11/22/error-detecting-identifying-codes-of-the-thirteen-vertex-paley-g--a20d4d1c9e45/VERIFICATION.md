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

Run the two source files in a standard Python 3 and C++17 environment:

```
python3 check_direct.py

g++ -std=c++17 -O2 -Wall -Wextra check_orbits.cpp -o check_orbits
./check_orbits
```

The recorded outputs are provided in `output_direct.txt` and `output_orbits.txt`. Both checkers were actually executed. The Python code visits every one of 8192 detector subsets and tests all directed neighborhood differences. The C++ code independently constructs the adjacent-pair forbidden 4-subsets, verifies uniqueness of each witness, counts every 5-subset's forbidden 4-subsets, and enumerates all 13 affine orbits on four-subsets and all 19 on five-subsets. Both yield 364 admissible omission tetrads and exactly 364 optimal 9-detector codes.

The 2022 published DET:IC criterion is an input definition, not a new mathematical discovery. The exhaustive finite certificate does not entail any result for other graph sizes. Scientific novelty remains provisional and no independent external audit has occurred.
