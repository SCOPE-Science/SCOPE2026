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

# Reproducibility

Compile and run `verify_b.cpp` with a standard C++17 compiler, for example:

```
g++ -std=c++17 -O2 -Wall -Wextra verify_b.cpp -o verify_b
./verify_b
```

Expected final line: `CPP_ENUM_AND_LOCAL_PASS`. The bitmask program enumerates every four-set for \(4\le n\le23\); for each set it executes the complete synchronous rule, including stalled cases. It independently checks the closed-form local min--max arrival equation for \(4\le n\le3000\). Its finite range is explicitly bounded.

Run `python3 verify_a.py`. Expected final line: `PY_EXHAUSTIVE_PASS`. This program uses ordinary vertex sets, a separate forcing simulator, dihedral canonicalization, and complete four-set enumeration for \(4\le n\le18\); it excludes three-set forcing for \(4\le n\le11\). The C++ program uses a separate implementation and representation.

Both programs were replayed successfully from their actual packaged file bytes. Their finite experiments support the independent algebraic/combinatorial argument; neither test alone establishes the infinite statement. The arrival times in the proof are additionally checkable by substitution into the local min--max recurrence for each vertex and each type. The original 2008 source was not read in full; the literature-priority comparison has a stated residual risk. External audit has not been performed.
