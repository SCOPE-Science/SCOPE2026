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

# Finite verification

The proof uses two independently implemented exhaustive algorithms, no sampling. The exact input graphs are in `graph_data.json`; the expected 708,588-state histograms and explicit sharp witnesses are in `counts.json`.

Run from the directory containing the four verification artifacts:

```sh
python3 verify_reverse.py
c++ -O2 -std=c++17 -Wall -Wextra verify_forward.cpp -o verify_forward
./verify_forward
```

`verify_reverse.py` builds the entire functional digraph of the θ=2 map, removes indegree-zero states, confirms the only cycle survivor is the all-zero fixed state, and computes exact hitting times in reverse topological order. It separately backtracks to establish triangle-freeness and chromatic number four of the specified graphs.

`verify_forward.cpp` independently assembles the update rule and graphs; for every initial state it directly steps to zero by the claimed cutoff, compiles the first-hit histogram and finds sharp witnesses. It also replays primitive θ=1 three-cycles on both graphs and the four-phase θ=2 orbit on \(K_{4,4}\).

Expected Grötzsch first-rest counts at times 0–5: `1,2047,51361,87116,36202,420` (sum 177147); expected Chvátal counts at times 0–6: `1,4095,117272,237555,151450,20160,908` (sum 531441). First maximum-delay ternary-encoded state 1089 and 120 respectively. Both finite enumeration programs were executed from these source files and matched all counts.

The result is an exhaustive computational proof only for the labelled graphs and rule specified. Neither checker is an independent external scientific audit, and no unbounded graph family is asserted.
