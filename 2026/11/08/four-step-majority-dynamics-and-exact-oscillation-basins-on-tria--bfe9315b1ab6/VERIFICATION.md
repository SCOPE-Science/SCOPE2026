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

# Computational verification

The analytical theorem and all-size counts follow from the local transition table and the multinomial proof. The following finite tests are corroborating checks only.

`check_states.cpp` uses explicit graph-neighborhood bitmasks and synchronous neighbor-majority updates. Compiling with `c++ -std=c++17 -O3 check_states.cpp -o check_states` and running `./check_states` reproduces `states_output.txt`. It exhaustively checks all \(4{,}793{,}488\) labelled states for blade counts one through seven, including each first periodic-entry time, least eventual period, and the four-step cutoff.

`check_macro.py` uses only four integer blade-type counts and a derived symbolic transition map. Running `python3 check_macro.py` reproduces `macro_output.txt`. It proves equality between symbolic transitions and the category table at every macrostate for blade counts one through sixty; all counts are exact integers. The independent cross-comparison of output numbers at blade counts one through seven is captured in `crosscheck_output.txt`. The programs have disjoint core representations and do not share a transition function.

The verification does not test an infinite number of graph sizes, and the classical prior-art comparison is not independently audited. No external mathematical certification is asserted.
