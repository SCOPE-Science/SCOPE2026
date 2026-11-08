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

Compile the included `VERIFY.cpp` with a C++17 compiler, for example `c++ -O2 -std=c++17 VERIFY.cpp -o verify`, and run `./verify`. It constructs rook-graph adjacency masks independently of the component classification, enumerates every nonempty subset on the eleven indicated boards, tests open-neighborhood total domination and inclusion-minimality, and directly tests all component types. It compares each size count against a separately coded labeled-component recurrence for the coefficient-extraction formula.

The actual check returned:

```
VERIFY_OK instances=11 examined_subsets=51745605 minimal_sets=17045 component_types=PASS coefficients=PASS square_6x6=PASS
```

The exhaustive cases are \((2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(4,6),(5,5)\), and an additional nonexhaustive recurrence check covers \((6,6)\). Exhaustiveness applies only to these finite parameter choices, not to the infinite theorem. The proof in `RESULT.md` establishes the unrestricted statement.
