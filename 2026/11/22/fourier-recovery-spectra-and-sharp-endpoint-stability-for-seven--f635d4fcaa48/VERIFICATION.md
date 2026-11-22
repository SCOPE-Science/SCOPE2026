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

# Verification procedure and limits

The included source files `verify_all_masks.cpp`, `verify_permutation_polynomials.py`, and `verify_spectral_projection.py` are standalone and do not read external data. Execute them in a directory that contains the three files:

```
python3 verify_permutation_polynomials.py
python3 verify_spectral_projection.py
c++ -O3 -std=c++17 verify_all_masks.cpp -o verify_all_masks
./verify_all_masks
```

The permutation checker independently enumerates 5040 permutations, confirms 133 functions for which both the function and its difference from the identity permute the field, and verifies the explicit 35-plus-98 classification. The C++ checker exhaustively visits all 85,900,584 seven-point sets (with integer bit-mask direction arithmetic), recovering exactly 56, 5488, 123480, 6324528 and 79447032 masks at blind-direction levels 7, 3, 2, 1 and 0. The cyclotomic checker obtains 18 zeros, eighteen squared multipliers of 7, twelve of 14 and one of 49; it then computes the 49 projection-kernel rational coefficients and their endpoint norm 193/49. All three completed successfully in the present verification.

The full proof of the all-mask histogram and the optimality over *arbitrary* projections is mathematical, not an empirical conclusion from the checkers. These tools are finite exact checks of specified equalities and exhaustive finite classifications; they do not establish any assertion beyond the stated finite domain or historical novelty.
