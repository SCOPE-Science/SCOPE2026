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

# Reproducibility

`verify_bounds.py` is a self-contained Python 3 / NumPy consistency checker for the stated two-alias fiber formula. Invoke `python verify_bounds.py`. It constructs each complex fiber matrix independently of the closed-form bound routine, verifies 6,720 random fiber eigenvalue enclosures and 5,760 endpoint corner fibers across dimensions two to five, checks the sharp coordinate design in dimensions two, four, and seven, verifies the singular balanced-direction case, and independently diagonalizes a finite periodic Fourier sampling matrix on an \(8\times8\) torus to check normalization.

The direct saved-file execution reported:

```
CHECK_OK random_fibers= 6720 endpoint_fibers= 5760
CHECK_OK minimax 0.29289321881345254 1.7071067811865475 2.414213562373095
CHECK_OK cyclic_torus=8x8
```

The infinite-dimensional assertion, all possible real unit directions, uniformity over Fourier fibers, uniqueness of the optimal design and asymptotic collision law are proved analytically in `RESULT.md`. Finite numerical checks alone are not certificates for those universal assertions. The norm convention and data weights must remain as stated; changing them alters the numerical constants.
