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

# Reproducibility and boundaries

The two checkers implement the same stated local ant rule with different state encodings and different symmetry-quotient methods. Run `python3 verify_direct.py` and compile/run `verify_independent.cpp` with `c++ -std=c++17 -O2 verify_independent.cpp -o verify_independent && ./verify_independent`.

`verify_direct.py` checks an explicit two-sided inverse on all 196608 states; traverses every permutation orbit; verifies that the four symmetry generators commute with the transition on every state; and uses a disjoint-set quotient by all 48 geometric operations on temporal cycles. `direct_output.txt` records period counts, symmetry types, and the exact sizes of each type.

`verify_independent.cpp` separately constructs all 196608 successors and checks indegree one at every state. It obtains period counts from a separate functional-graph traversal, then sums fixed temporal cycles under all 48 geometric operations. Burnside's formula gives each period's class count; `independent_output.txt` records the fixed-cycle sums.

The count of temporal cycles is 2480; the sum of cycle lengths is 196608; 74 is the sum of the per-period symmetry-type populations. Every least period is divisible by eight and the maximal period is 312. These computations enumerate a finite domain; they do not prove any theorem for larger tori, and they do not establish historical publication priority. Independent external mathematical validation has not been performed.
