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

# Verification

The object is the graph with ten vertices indexed by lexicographic two-subsets of five symbols, with adjacency exactly for disjoint pairs. The exact four-case update and definitions of first-entry time and least eventual period are in `RESULT.md`.

## Replay

Run these three commands in the directory containing all embedded files:

```
python3 verify_exhaustive.py
python3 verify_independent.py
python3 verify_outer_inner.py
```

`verify_exhaustive.py` enumerates exactly \(59049\) input states, constructs all successors, proves every assigned entry time by reverse traversal of the finite functional graph, and checks the whole periodic-cycle census. It also verifies the identity \(F^{126}=F^6\) over the full state set, enumerates all 120 permutations of the five ground symbols, and proves the 120 six-step states are exactly the two 60-element automorphism orbits.

`verify_independent.py` follows each input state independently in a tuple-based implementation with no borrowed successor table or cached classification. Its full table is compared against hard-coded target values. `verify_outer_inner.py` constructs the same Petersen graph through an outer pentagon, spokes and an inner pentagram, rather than through disjoint two-subsets, and compares periods and entry-layer totals.

Expected summary: primitive cycle counts \(1,80,60,30,60\) at periods \(1,3,4,5,8\); first-entry layer populations for \(t=0,1,\ldots,6\) equal \(1111,9533,21193,14492,11760,840,120\). `census.csv`, `extremal_orbits.json`, `exhaustive_result.json`, `independent_result.txt`, and `outer_inner_result.txt` give the detailed outputs actually checked.

## Limits

The enumeration is mathematically exhaustive because the finite state space is explicitly and completely traversed; neither numerical sampling nor extrapolation is used. This establishes the claimed finite-state classification, not a theorem for larger families or a guarantee that all prior literature has been found. No independent external audit has been performed.
