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

The two standalone checkers are `verify_subset.py` (Python 3, Kneser pairs) and `verify_petersen_gp.cpp` (C++17, generalized Petersen model). Execute:

```sh
python3 verify_subset.py
g++ -std=c++17 -O2 verify_petersen_gp.cpp -o verify_petersen_gp
./verify_petersen_gp
```

The first prints `PASS_PETERSEN_LINE_LTD_SET_32768`, full coefficients and orbit profiles, and exact radius and diameter. The second prints `PASS_PETERSEN_LINE_LTD_GP_32768` and `MINIMA 110 THREE_PATH_FOREST 110 EXCHANGE_EDGES 210 RADIUS 6 DIAMETER 7`. These markers were obtained in an actual execution of the packaged source. Both explicitly inspect all 32768 subsets, the full equivalence of the six-vertex selected-code predicate to the three-path forest condition over all 5005 six-subsets, and all 110 exchange BFS origins. The independent graph constructions are crosschecked for an explicit graph isomorphism. No computations beyond the stated finite domain or independent external audit are claimed.
