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

# Verification

Run `python3 verify.py` with Python 3. The standalone source requires no third-party modules. It recomputes every monomial of weight 13 in weights (2,3,5,7,8), verifies the intrinsic lattice coordinates and a determinant-one submatrix, enumerates all supporting primitive facet inequalities from 126 four-point subsets, and checks every nonempty proper face as an intersection of the eight facets. Exact rational row reduction identifies precisely two fixed points and their connecting edge as the non-Q-Gorenstein faces.

Verified output:

```
WEIGHT_13_TORIC_CHECKS_PASS
monomials 9 dimension 4 facets 8 vertices 8
face_vector (8, 19, 19, 8)
non_Q_Gorenstein_faces [(2,), (2, 6), (6,)]
Gorenstein_fixed_point_indices [0, 1, 3, 5, 7, 8]
```

This finite, exhaustive polytope check supports the exact mathematical statement for the fixed weight-13 variety. It does not certify novelty, independent review, or assertions about other weights. The published identification of the projective variety with the normal toric variety of the monomial polytope is used as an input.
