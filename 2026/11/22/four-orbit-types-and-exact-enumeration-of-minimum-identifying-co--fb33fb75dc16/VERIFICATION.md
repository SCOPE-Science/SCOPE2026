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

# Direct and structural finite checks

The accompanying `verification/verify_n6_direct.cpp` enumerates every nine-element subset of the 36 square cells of the six-by-six rook graph. It first filters subsets with an empty row or column (the proof shows these cannot be optimal at even order \(n\ge6\)); it then checks all 36 closed-neighborhood identification signatures **directly**, with no component-type prefilter, and records the component shapes of every success. It was compiled with `g++ -std=c++17 -O3` and executed, producing:

```
candidates=94143280 identified=1252800 four_types=86400,518400,518400,129600
```

The separate `verification/verify_n6_structural.cpp` checks the elementary degree and isolated-edge characterization, and then independently verifies all 36 signatures for every structurally allowed candidate. It produces exactly the same four counts. The third `verification/verify_n4_boundary.py` scans all 8,008 size-six subsets of the four-by-four rook graph and obtains 2,208 valid codes; its configurations include an empty-side case, which is intentionally excluded from the theorem.

The computations are finite consistency checks, not an independent infinite proof. All universal statements, small-order exclusions, and factorial counts rest on the detailed argument in `RESULT.md`. No independent scholarly audit is represented by these program runs.
