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

# Verification record

The full proof is in `RESULT.md`. The executable checks below are supplementary, self-contained finite tests, not an independent audit and not an infinite proof.

With C++17 and Python 3 available, run:

```
g++ -std=c++17 -O3 -Wall -Wextra verify_burning.cpp -o verify_burning
./verify_burning
python3 verify_tiling.py
```

`verify_burning.cpp` independently generates the graph, computes all-pairs distances by breadth-first search, then exhaustively checks every strict ordered ignition sequence in \((n,k)=(5,3),(10,4),(17,5)\); exact accepted counts are 20, 120 and 816.

`verify_tiling.py` independently constructs the cyclic partitions and checks all resulting strict legal schedules for \(k=3\) through \(7\), with expected totals 20, 120, 816, 6240, 53280. At \(k=3,4,5\), it also reconstructs every source-replacement edge and obtains respectively 10, 60 and 408 isolated two-vertex components.

The programs have been executed successfully from these exact source files before packaging. Infinite claims rely on the capacity, interval-tiling, core-coverage and exchange-uniqueness arguments, which have separately been reconstructed. The numerical checks are exhaustive only for the stated finite graphs. No external expert or independent scholarly validation is claimed.
