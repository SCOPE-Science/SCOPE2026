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

# Reproduction and limits

Run `python3 verify_formula.py` to recompute the full coefficients for \(n=5,6\) from the explicit star–triangle inclusion–exclusion formula and the closed minimum coefficient for \(n=5,6,7,8,9\). Also compile and execute `verify_direct.cpp` with a C++17 compiler, for example `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct`. The C++ program uses only the raw disjointness rule, enumerates all \(4^{10}\) labelings for the ten-vertex graph at \(n=5\), and independently tests the full-star singleton configurations for \(n=5,6,7\). Recorded outputs are in `verification_output.txt`.

These computations corroborate the coefficients they touch but do not test all integers \(n\). The proof of the general theorem is the elementary intersecting-family classification, the exact per-event inclusion–exclusion identity and the two-star exclusion argument in `RESULT.md`. An inaccessible or unindexed earlier mathematical source might conceivably contain the same theorem. No independent mathematical audit has been performed.
