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

# Verification of the adjacent-swap diameter

The mathematical proof appears in `RESULT.md` and applies for every integer \(n\geq1\). It is self-contained and does not assume that a finite census can prove an infinite theorem.

To reproduce independent finite tests with only Python 3 and a C++17 compiler:

```sh
python3 verify_enumerate.py
c++ -std=c++17 -O2 -Wall -Wextra verify_prefix.cpp -o verify_prefix
./verify_prefix
```

`verify_enumerate.py` enumerates all permutations, filters by direct forbidden-triple search, generates adjacency exchanges, and performs BFS from *every* vertex for orders 1 through 8. `verify_prefix.cpp` generates only permissible prefixes, builds the adjacent-swap graph independently, checks full diameters through order 8, and tests the explicit diametral witness at orders 9 and 10. The two algorithms use different methods of generating states and validating avoidance.

Expected complete all-source diameters at orders 1–8 are `0,1,4,7,12,17,24,31`; constructed witness distances at orders 9 and 10 are `40,49`. Success markers are `EXHAUSTIVE_321_ADJACENT_SWAP_DIAMETERS_PASS` and `PREFIX_ENUMERATION_321_SWAP_METRICS_PASS`.

**Limits.** Both programs prove only finite claims when combined with their plainly readable exhaustive loops. Their output is a consistency check on, not a replacement for, the all-order mathematical argument. No independent audit or external formal verification has been performed.
