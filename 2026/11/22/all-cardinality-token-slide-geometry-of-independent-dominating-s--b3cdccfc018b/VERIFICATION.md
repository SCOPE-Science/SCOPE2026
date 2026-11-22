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

# Reproducible verification

This result comes with three standalone checking programs, their exact captured outputs and no third-party Python dependencies. Commands below are run from the directory containing these supplied files.

1. `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_direct.cpp -o verify_direct && ./verify_direct` checks every subset of the original two-rail graph for rung orders 2–10, independently constructs slide edges from the original graph, checks size multiplicities and edges for all k, exactly two component sizes, and the claimed diameter. Its output must equal `verify_direct.output.txt` and end with `DIRECT_EXHAUSTIVE_PASS`.
2. `python3 verify_word.py` enumerates every feasible rung word and proposed gap pattern through rung order 18, tests independence and domination locally, and checks that every legal word slide corresponds to one adjacent-bit swap. Its output must equal `verify_word.output.txt` and end with `WORD_BIJECTION_AND_MOVES_PASS`.
3. `python3 verify_median.py` constructs exclusion-token path graphs for all path orders up to eight and all token counts; all-pairs BFS checks their exact distance/diameter and edge counts, and for manageable orders it checks uniqueness of the coordinatewise median among every triple. Its output must equal `verify_median.output.txt` and end with `MEDIAN_AND_DISTANCE_PASS`.

These independent finite checks are reproducible confirmations of the stated definitions, counting formulas, boundary cases, reachability and median metric. They are not themselves exhaustive over all ladder sizes. The universal proof in RESULT.md supplies the all-orders reasoning; no external certificate or independent audit is asserted.
