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

# Verification notes

The analytic proof uses the last possible excitation time and a first-front collision exclusion. The actual reproducibility programs are `verify_exhaustive.cpp` and `verify_structural.py`.

Run the commands in the directory containing the two source files:

```
g++ -std=c++17 -O3 -Wall -Wextra verify_exhaustive.cpp -o verify_exhaustive
./verify_exhaustive
python3 verify_structural.py
```

The captured independent outputs are `checks/exhaustive.txt` and `checks/structural.txt`. The C++ program simulates all \(5,764,801\) labelled states in the largest tested instance, and the Python program compares both the extremal-state predicate and the full polynomial coefficients on smaller instances.

These experiments are finite and do not establish the infinitely many parameter cases. The general proof appears in `RESULT.md`. Historical-priority checks were limited to accessible sources; independent mathematical validation has not been performed.
