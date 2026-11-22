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

# Exact checks and scope

The standalone programs `verify_subset.c` and `verify_windows.c` are complete source files, requiring only a conforming C11 compiler and its standard library.

```
cc -O2 -std=c11 -Wall -Wextra verify_subset.c -o verify_subset
./verify_subset
cc -O2 -std=c11 -Wall -Wextra verify_windows.c -o verify_windows
./verify_windows
```

`verify_subset` enumerates all 65,536 ordered rule pairs, constructs all eight labeled transitions and 256 deterministic subset transitions for each, and performs closure to decide if any forbidden pair word exists. It checks the exact length histogram 708, 8,552, 38,436, 15,920, 1,776, 144 and the three homogeneous-status classes. It explicitly tests a missing word first occurring at length five and one onto pair containing a non-onto homogeneous rule.

`verify_windows` independently enumerates all 4,096 possible 12-bit input windows for every pair, identifies reachable 10-bit outputs, and counts their prefixes of lengths 2, 4, 6, 8 and 10; its exact histogram agrees with the first program.

The all-length theorem relies on the explicit labeled-graph equivalence and exhaustive finite subset-state closure, not on the independent five-pair enumeration alone. No randomized experiment, floating-point tolerance, or assumed infinite-time behavior is used. Independent mathematical audit has not been performed.
