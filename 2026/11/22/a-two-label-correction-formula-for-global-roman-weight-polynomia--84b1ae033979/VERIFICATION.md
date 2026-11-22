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

# Verification and limits

Run `python3 verify.py`: compares all complete bivariate generating polynomials by exhaustive three-label enumeration for rim lengths 3 through 9, including a separate transfer trace and two exact integer specializations, against the closed formulas. Run `g++ -O3 -std=c++17 verify_minima.cpp -o verify_minima && ./verify_minima`: second independently written finite enumeration checks minimum weights and their multiplicities for rim lengths 3 through 12. Code paths are standalone and have no external data dependencies.

The infinite all-order assertions are proved in `RESULT.md` by classifying rim-two supports and by strict lower bounds. Finite computations are corroboration, not replacement for infinite proof. Inaccessible full prior work can affect novelty/priority, not the internal logical proof; no external independent mathematical audit has occurred.
