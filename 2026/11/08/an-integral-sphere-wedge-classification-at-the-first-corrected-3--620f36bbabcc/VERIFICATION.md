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

# Reproducibility and limits

Compile the supplied `verify.cpp` using `g++ -O3 -std=c++17 verify.cpp -o verify` and run `./verify 9`. To reproduce the adjacent-width sanity check run `./verify 8`. The checked execution output is in `verify_output.txt`; the width-nine run ends `ALL_VERIFY_OK`.

The program constructs all nonempty graph matchings, applies the sequential edge-toggle face matching, tests global acyclicity on every directed face-poset incidence with an exact topological sort, and uses signed integer coefficients to compute all 49 critical-nine-cell boundaries in a basis of the 212 critical eight-cells. Unit pivots are checked in integer arithmetic, with no modular substitute. It checks the face-count Euler sum against the resulting wedge count.

The computation is exhaustive for this particular 3-by-9 graph, using substantial memory (approximately 800 MB in the checked run); it is not an all-width proof. The code terminates if an incidence, acyclicity condition, Euler value, or unit cancellation fails. Scientific interpretation follows the proof in `RESULT.md`. No external independent validation has been performed.
