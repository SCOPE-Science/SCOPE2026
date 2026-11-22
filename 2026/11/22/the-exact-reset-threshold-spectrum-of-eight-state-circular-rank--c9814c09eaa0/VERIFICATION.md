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

# Verification evidence

The code is standard C++17 and Python 3; no third-party packages or data downloads are needed. In the delivery directory, `python3 verify_spectrum.py` compiles and executes the two exhaustive enumerators, confirms every count against `spectrum.csv`, and performs an independent Python BFS for the unique maximal representative. The complete checks succeeded with:

```
VERIFIED 31 threshold entries; 670608 orbits; 5362560 labeled maps; extremal length 36
EXTREMAL_RESET_WORD baaaaabaaaabaaaaaabaaaaabaaaaabaaaab
```

**Completeness of search:** Every map is an eight-digit output tuple. The first program visits all \(8^8=16{,}777{,}216\) tuples, filters by image cardinality six, retains the lexicographically smallest cyclic conjugate, then searches all reachable nonempty subsets. The second program recursively builds only maps that can have final image cardinality six, visits every such tuple once, and independently searches all reachable nonempty subsets using a separate image computation. The second program also directly counts half-turn-invariant maps to convert its labeled histogram into rotation-class counts by Burnside's lemma. Neither program uses a sampling or search-depth cutoff. The Python witness search separately checks the extremal distance 36.

**Boundaries:** Reset threshold \(-1\) means no reset word; it does not mean a word of negative length. No result for nine-state automata, other ranks, or arbitrary alphabet permutations is inferred. Executable finite enumeration is not a substitute for an infinite-family proof. Independent mathematical audit remains unperformed.
