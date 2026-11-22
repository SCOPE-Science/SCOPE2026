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

# Verification of the ring-torus near-diameter law

Analytical verification: the maximizing pairs form precisely one circle of antipodal outer-equator pairs. The squared chord deficit has transverse Hessian diagonal values \(4r(R+r),4rR,2(R+r)^2\) in orthonormal local displacement coordinates and no cubic Taylor term. The resulting ellipsoid-volume constant, together with the surface-area probability density, yields the formula stated in `RESULT.md`. The first neglected probability term is \(O_{R,r}(\varepsilon^{5/2})\). Differentiation of the fully normalized shape coefficient proves a unique critical point at ratio \(5/2\).

Computational verification: run `python3 verify_torus_tail.py` with Python 3 (no third-party dependencies). The program numerically integrates the exact conditional azimuth angle law, not the local quadratic approximation, for three ring-torus aspect ratios and two small distance cutoffs; it separately checks the shape minimum and derivative signs. Recorded success: `VERIFY_TORUS_DIAMETER_TAIL_OK 20`. Finite quadrature cannot replace the global analytic uniqueness, asymptotic error or historical-originality arguments.

Scientific scope: full smooth embedded ring tori only, with independent uniform-area points and Euclidean ambient chords. The constant is not claimed to be a uniform estimate near the horn or zero-tube degeneracies. Historical originality and independent mathematical validation remain unperformed and are not implied by these numerical checks.
