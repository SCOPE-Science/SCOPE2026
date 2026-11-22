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

A standard C++17 compiler is the only dependency. Build and run the supplied `checker.cpp`:

```sh
c++ -std=c++17 -O2 -Wall -Wextra -pedantic checker.cpp -o checker
./checker
```

Compare with `check_output.txt`; the last line should be `VERIFY_OK`. The program checks all \(4,037,913\) permutations at lengths one through ten, not a sample. Independent *algorithms* compare bitmask distances and rectangle-count distances for each base and every gap pair. Assertions also prove orbit disjointness and exact coverage of every ten-point failure. The persisted nonunimodality for every larger \(n\) follows from the written border-strip argument; finite tests through length 25 check that formula only on some examples.

The observed output does not certify any unexamined order beyond ten, and no claim of an external/independent audit is made. A source-matching comparison cannot exclude unindexed equivalent historical work.
