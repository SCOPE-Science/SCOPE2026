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

The derivation proves the exact recurrence-entry time for every cycle length at least three. The two supplemental implementations are independent finite consistency tests:

- `check_functional_graph.py` constructs the complete deterministic transition graph and independently computes distance to a recurrent component, for sizes 3 through 14.
- `check_direct.cpp` runs the original bit-flip-and-move dynamics, checks unicycle recurrence at every pre-entry time and at entry, for sizes 3 through 13.

Both programs executed successfully. Their exact stdout captures are supplied as `functional_graph_output.txt` and `direct_output.txt`.

Run with `python3 check_functional_graph.py`; compile the other with `g++ -std=c++17 -O2 -Wall -Wextra check_direct.cpp -o check_direct` and run `./check_direct`. Only Python's standard library and a C++17 compiler are used. Exhaustive tests of bounded lengths are not substitutes for the all-length proof. No independent external audit has been performed.
