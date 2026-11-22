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

# Reproduction

Run `python3 verify_quadratic_shattering.py`. It calculates the proposed coefficients for ranks two through four, then independently compares the support characterization with actual Boolean traces for every four-dimensional support of size at most three and every six-dimensional support of size at most three. It also checks 150 random supports of sizes four, five and six for each parity in dimension six, using a fixed reproducible seed.

Compile `verify_dim6.cpp` using `c++ -O2 -std=c++17 verify_dim6.cpp -o verify_dim6` and run `./verify_dim6`. This separately enumerates every point concept and every six-dimensional query support of cardinality zero through four, for both parity classes, and checks the exact coefficient counts, including the exceptional Lagrangian degree. The expected terminal markers are `QUADRATIC_PARITY_SHATTER_PASS` and `DIM6_ALL_SUPPORTS_K_LE4_PASS`.

These exact finite checks were executed successfully against the included source files. The all-dimensional claims rest on the proof in `RESULT.md`; no computation beyond dimension six is asserted to be exhaustive. The C++ verifier and Python verifier are separate implementations but do not constitute independent external validation.
