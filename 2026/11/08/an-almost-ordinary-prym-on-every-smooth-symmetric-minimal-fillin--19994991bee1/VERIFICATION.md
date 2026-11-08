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

The accompanying exact Python/SymPy programs reconstruct the displayed defining forms directly and run over characteristic three. `verify_geometry.py` checks all four product affine charts for smoothness, all three quotient-plane charts, the quotient pullback identity, distinct branch points, the complete normalized quartic candidate set, and the common diagonal-projective orbit. `verify_hasse.py` extracts both complete Hasse–Witt matrices from the square of the respective equations, checks their exact coefficient entries, the rank-eight minor, zero determinant, characteristic polynomial of the genus-nine matrix, and invertible quotient matrix.

Successful replay output:

```
CURVE_SMOOTH_ALL_FOUR_CHARTS_PASS
QUARTIC_QUOTIENT_SMOOTH_ALL_THREE_CHARTS_PASS
EIGHT_DISTINCT_RAMIFICATION_POINTS_PASS
SYMMETRIC_SMOOTH_QUARTIC_CENSUS_PASS 24 6 1_ORBIT
SIXTEEN_RATIONAL_POINTS_FILLING_PASS
GENUS_NINE_HASSE_MATRIX_PASS rank=8 stable_rank=8 a=1
PLANE_QUARTIC_HASSE_MATRIX_PASS rank=3 ordinary
PRYM_ISOGENY_INVARIANTS_PASS dimension=6 p_rank=5 a=1
```

All calculations are finite exact computations on the specified polynomials. The conclusions about geometric smoothness use ideal-theoretic unit certificates, and the curve and Prym invariants use the stated cohomological and isogeny theorems. The programs do not establish historical priority, a complete zeta function, or an independent mathematical audit.
