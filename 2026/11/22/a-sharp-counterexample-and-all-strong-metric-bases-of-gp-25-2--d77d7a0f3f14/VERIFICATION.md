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

# Reproducibility of the \(GP(25,2)\) result

The package contains two standalone source files. No unpublished data or external services are required to reproduce the exact finite checks.

The first was compiled with `g++ -O2 -std=c++17 gp25_independent.cpp -o gp25_independent` and executed with `./gp25_independent`. It generated the graph and breadth-first-distance matrix; checked all \(1225\) unordered vertex pairs against direct strong resolution for an explicit \(34\)-vertex witness; verified the full MMD difference table; and exhaustively enumerated the relevant independent-set cardinalities by monotone backtracking. Its output was:

```
uu=125 vv=50 cross=0 direct_pairs=1225 unresolved=0
independent U6=25 U7=0 V10=5 V11=0
minimum strong metric dimension=34 minimum bases=125
```

The independent Python implementation was executed with `python3 gp25_crosscheck.py` and used its own shortest-path construction, MMD checks, translated outer-layer enumeration, and pentagon-product inner-layer enumeration. Crucially, it also tested all \(125\) proposed strong resolving sets against the original distance definition. Its output was:

```
MMD edges 175 anchored outer six 6 anchored outer seven 0 outer maxima 25 inner maxima 5 strong metric bases 125
```

The outer finite certificate checks each of the \(2002\) possible five-subsets and \(3003\) six-subsets of the precisely identified fourteen candidates after fixing vertex zero by translation. The inner finite certificate considers all \(3125\) ways to choose two vertices from each of five explicitly given vertex-disjoint five-cycles. Both searches are exhaustive within the fully specified \(50\)-vertex graph. The general MMD/vertex-cover equivalence has a separate mathematical proof in the result document.

**Limits:** The checks certify no unbounded family of generalized Petersen graphs and do not independently establish historical novelty. Independent scholarly audit has not been performed.
