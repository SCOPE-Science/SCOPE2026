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
# Verification of the cube affine-projection theorem

## Analytic proof checks

The normalized Gram matrix for the basis \(1,y_1,\ldots,y_d\) is diagonal with entries \(1,1/3,\ldots,1/3\). Inversion gives \(K(x,y)=1+3x\cdot y\). A conditional uniform integral proves strict vertex-only evaluation maxima and the exact quadratic increment formula. Signed-kernel tests determine all norming inputs and the sharp positivity defect. An Irwin--Hall positive-part identity gives an exact rational sum. Fourier absolute-moment and local-density expansions with explicit small-frequency and tail controls establish the claimed two-term asymptotic for all large dimensions.

## Reproducible executed computation

From the same package directory run `python3 check_cube_affine.py` with Python 3.9 or later. The program uses only the standard library. It independently integrates the piecewise polynomial density in exact rational arithmetic for 18 dimensions, compares with the finite binomial expression, checks small-dimensional fractions, proves positivity of the listed central B-spline densities by exact calculation, and reports finite asymptotic diagnostics. The observed final line is `ALL_CUBE_AFFINE_PROJECTION_CHECKS_PASSED`.

## Limits

All finite computational checks are non-exhaustive for unbounded dimension and do not establish the strict inequality or asymptotic remainder by themselves. The universal results depend on the analytical proof in RESULT.md. There is no independent mathematical audit.
