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

# Reproduction of the exact wave-clock computations

The formula is proved in `RESULT.md`; these two implementations verify specific cases and do not establish generality.

Run `python3 checks/check_wave.py`. This uses only the Python standard library and builds a ternary matrix directly from each graph's neighbor relations, then computes exact powers and kernel ranks for the complete two-time-layer operator. It checks the exact order and all claimed nested kernel dimensions at cycle sizes 3, 9 and 27. Its actual stdout is stored in `checks/check_wave.out`.

Run `g++ -std=c++17 -O3 -o check_orbits checks/check_orbits.cpp && ./check_orbits`. This enumerates every one of 531,441 states on the triangular sunlet by a direct vertex-neighborhood transition, records each least period, and checks exact counts 1, 6,560 and 524,880. Its actual stdout is `checks/check_orbits.out`. The C++ executable itself is not required and is not distributed; the source rebuilds it.

**Limits.** Neither test enumerates all larger graph states or extension fields. The mathematical mechanism uses the exact fifth-cyclotomic matrix identity over a local polynomial ring and finite-field kernel cardinality, so it is not based on extrapolation. Independent scientific audit has not been performed.
