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

`coefficients.json` stores the exact integer coefficient arrays obtained from the full finite domain of six independently chosen three-element permutations. Run `python3 verify.py` to regenerate all four enumerators, check all 46,656 labeled profiles, verify all rational formulas by polynomial multiplication and verify the signs of their derivatives. Run `c++ -O2 -std=c++17 verify_independent.cpp -o verify_independent && ./verify_independent` to recompute all four enumerators with a separate implementation.

The computations use exact integers and exhaustive loops, not simulation. They apply only to the \(3\times3\) complete strict preference domain; the finite certificate does not validate claims for larger markets or heterogeneous dispersion parameters. No independent external scientific audit is asserted.
