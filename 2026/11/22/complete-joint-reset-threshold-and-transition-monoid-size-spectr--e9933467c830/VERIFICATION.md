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

# Verification guide

`joint_spectrum.csv` is a complete table of the joint reset-length and transition-monoid-size histogram of binary four-state complete semiautomata. Its 179 data rows plus header are the exact machine-readable output certificate. The first column uses `-1` for no reset word; monoid size includes the identity.

The two supplied programs independently enumerate all \(4^8=65{,}536\) labeled ordered generator pairs. Compile and execute from a directory containing all three files:

```text
c++ -std=c++17 -O2 -o verify_transforms verify_transforms.cpp
./verify_transforms
python3 verify_subsets.py
```

Observed outputs:

```text
VERIFY_TRANSFORMS_OK: 65536 complete automata, 179 cells, 96 at threshold 9
VERIFY_SUBSETS_OK: independent histogram and two 48-element extreme orbits
```

The C++ program independently recomputes shortest constant-map depth and monoid size by breadth-first traversal of all reachable full transformations. The Python program computes monoid size by transformation closure but reset distance by a separate image-subset BFS on 15 nonempty subsets, then checks both 48-member extremal symmetry orbits by explicit state permutations and letter exchanges.

The finite state spaces make the checks exhaustive: every possible letter transition is evaluated; no random sampling or timeout-based argument is used. No statement for larger state sets is certified by these finite computations. The review status attached to this note is same-model, not independent validation.
