---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each h in (0,2) the kick-then-drift M(h) is elliptic, determinant-one and preserves G_h=[[1,-h/2],[-h/2,1]]. Positive covariance and adjoint eigenmatrices exist and have full rank since an elliptic M(h) has no invariant real line. Jensen strict log-det equality forces a common invariant G_h if rho=1, which is possible only for a point-mass law; an adjoint Perron quadratic form gives uniform two-sided expected-energy rho^n bounds. The exact three-moment-coordinate transfer and analytic symmetric jitter coefficient follow from differentiation of the simple eigenvalue. Independently expanded the exact symbolic determinant det(I-T_{h,e})=-2e^2(h-e)^2(h+e)^2. The proof addresses arbitrary iid laws supported in (0,2); finite symbolic testing alone would not.

## originality

FAIL

The entire submitted result is already proved by the complete October 12, 2026 published theorem Universal mean-square energy inflation under randomized symplectic Euler steps for exactly the same kick-then-drift matrix, iid support (0,2), positive-definite dual eigenmatrix, strict rho>1, exact covariance rate, and identical weak-jitter coefficient 2h^2/(4-h^2). A separate October 12 result gives the conjugate position-first version. No surviving novel component remains.

## value

PASS

The phenomenon is independently mathematically meaningful: pointwise elliptic, energy-bounded symplectic steps can produce universal exponential expected-energy instability under nonconstant iid randomization, with a sharp weak-noise coefficient. Value cannot compensate for proved prior coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
