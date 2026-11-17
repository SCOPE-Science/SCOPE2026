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

# Reproducibility and verification

Use a C++17 compiler and Python 3; the files do not need external packages or input datasets. Run the following from the root of the extracted package:

```sh
c++ -std=c++17 -O2 src/temporal_column_core.cpp -o rule54_core
./rule54_core > core_actual.txt
cmp core_actual.txt certificates/column_core.txt
c++ -std=c++17 -O2 src/independent_scc.cpp -o rule54_scc
./rule54_scc > scc_actual.txt
cmp scc_actual.txt certificates/independent_scc.txt
python3 src/direct_ring.py > direct_actual.txt
cmp direct_actual.txt certificates/direct_ring.txt
```

The first program enumerates the directed temporal-column graphs for heights 1, 3, 5, 7, 9 and 11, pruning zero-indegree or zero-outdegree vertices to the complete recurrent core, and validates that every core vertex has degree one in both directions. The independently structured second program constructs successors from the original Rule 54 eight-case truth table, then applies Kosaraju's strongly connected-component algorithm and reports all recurrent component sizes. The third program directly evolves all configurations on each cyclic ring of length three through eleven, obtains the least temporal periods, and checks two explicit eleven-site witnesses.

**Expected exact checks:** The largest graph has 4,194,304 vertices and 4,192,256 directed edges. The successive core cycle-length multisets are \((1)\) at heights 1, 3, 5, 7 and 9 and \((1,11,11)\) at height 11. Both graph programs reproduce those values exactly. The direct simulation corroborates the eleven-site orbit count and smaller-ring results but does not by itself establish any all-circumference assertion.

**Proof versus computation:** The correctness of the graph/closed-walk bijection and of zero-degree pruning is mathematical. Exhaustive deterministic programs verify the finite but large graph classification on which the all-circumference conclusion depends. The complete source and output are provided for reproducibility, without claiming an independent external proof or formal verification. These tests do not classify higher odd periods, general transient behavior, or historical publication priority.
