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

## Reproduce the exact finite proof

Run `python3 verify.py` with Python 3.8 or later (no external dependencies). The checker directly constructs every obstruction modulus for \(x=2,\ldots,230\), removes only provably redundant multiples, checks all three-position CRT compatibility triples, and derives the two complete ordinate residue classes. The checker then directly tests the original divisibility definition for both six-point certificates. An additional small-range direct ordinate scan checks the representation on an independent route; that small scan is diagnostic only.

Compile and execute `verify_independent.cpp` using `c++ -O2 -std=c++17 verify_independent.cpp -o verify_independent && ./verify_independent`. The separate implementation reconstructs all input moduli and checks the first-coordinate boundary and the exact two terminal compatibility triples; it also independently tests six-point invisibility.

The mathematical reduction in `RESULT.md`, not a program log alone, proves that these exhaustive finite checks cover *all* positive ordinates. The CRT argument and source code are entirely integer exact. Nothing beyond the two-by-three shape and the stated polynomial is certified.
