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
# Verification record

The included `verify.py` uses only Python 3 standard-library modules. It checks, for integers \(1\le k\le120\), both the exact rational formula for \(a_k/a_{k-1}\) and the strict coefficient inequality \(7a_k<a_{k-1}\); it also checks the sharp first and second normalized coefficients. Separately, the program uses a Gauss–Legendre grid in the spherical height coordinate and trapezoidal periodic azimuthal quadrature to reconstruct primal support volumes from the tangent Hessian and polar volumes from the reciprocal-cubed support. The evaluations at \(\varepsilon=0,0.2,0.5,0.8\) agreed with the respective exact primal-volume formula and polar power series to better than \(10^{-10}\) relative to the unit-ball volume.

The program does not numerically prove positive curvature at every parameter or globally certify all infinitely many coefficient inequalities. Those statements are instead proved algebraically in `RESULT.md`, with the endpoint handled by continuity. The Santaló-center argument relies on the exact symmetries of the support function and the standard uniqueness theorem; numerical checks are not used to infer it.

Independent mathematical audit has not been performed.
