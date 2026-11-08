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

# Reproducible exact checks

Execute `python3 verify.py` with Python 3. The script uses only standard-library exact integers and rational fractions. It reconstructs the defining six squarefree quartic monomials, expands the gradient under arbitrary linear parameters to test identically that each proposed plane and line is singular, deduplicates nine noncoordinate lines by primitive Plücker coordinates, and computes exact Hessian matrix ranks along all dihedral orbits.

Expected terminal result:

```text
HEXAGON_ADJOINT_EXACT_CHECKS_PASS
TWO_PLANES 2 NINE_COORDINATE_LINES 9 NINE_NONCOORDINATE_LINES 9
HESSIAN_RANKS: plane=3; coordinate_line=4; noncoordinate_line=4
```

The proof of exhaustiveness is an independent support stratification, not a finite sample. The claimed analytic normal forms use the standard holomorphic Morse–Bott lemma at generic smooth points of the singular strata. Intersection germs and embedded Jacobian scheme structure at their intersections are outside the claim.
