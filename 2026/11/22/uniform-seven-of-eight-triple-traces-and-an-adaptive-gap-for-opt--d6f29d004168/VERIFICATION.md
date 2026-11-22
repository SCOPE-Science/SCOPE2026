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

# Reproduction and limits

The mathematical proof is in `RESULT.md`. In a clean directory containing the package files, use:

```
python3 verify_python.py
c++ -std=c++17 -O2 -Wall -Wextra verify_cpp.cpp -o verify_cpp
./verify_cpp
```

The two programs independently generate the 16-vertex binary graph, exhaustively enumerate candidate dominating subsets, classify all 40 minimum sets, tabulate every pair and all 560 triple supports, and evaluate the adaptive decision-tree recurrence. Each outputs `PASS`; the captured outputs appear in `verified_python.txt` and `verified_cpp.txt`. The eight-leaf witness is checked explicitly. The C++ program reports 28,409 memoized subfamilies. The Python program separately checks the geometric multiplicities, which add to 560.

The proof is finite and exhaustive: all 65,536 subsets of a 16-point universe are within scope. Neither program claims completeness in a different cube dimension. Historical-priority evidence is limited by lack of access to the full 2000 small-covering-code classification. No independent mathematical audit has occurred.
