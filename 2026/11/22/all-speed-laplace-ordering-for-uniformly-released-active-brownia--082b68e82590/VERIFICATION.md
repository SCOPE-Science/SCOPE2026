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

The theorem is proved analytically in `RESULT.md` using the killed Dirichlet resolvent, a bounded skew-adjoint symmetrization, a positive spectral measure, a zero-kernel argument and elementary functional inequalities.

Run `python verify.py` in Python 3 with NumPy, SciPy and mpmath. The actual test execution produced `PASS: 415 deterministic assertions`. Tests include finite-dimensional independent inversion of the nonsymmetric generator versus the Stieltjes resolvent over two orientation-diffusion values, three discount values and seven speeds, strict signed derivative checks through fifth order, reciprocal concavity, and an analytic one-dimensional fixed-heading exit solution averaged by numerical quadrature. The interval calculation recovers the coefficient \(-L^4/(90D^3)\) after uniform angular averaging.

Limits: finite matrices and quadrature do not prove the infinite-domain, all-discount, all-speed or all-derivative claims. In particular, strict spectral support away from an atom at zero is established by the directional trace proof, not by discretization. The first-passage Laplace ordering is not pointwise ordering of survival curves. No independent mathematical validation has been conducted.
