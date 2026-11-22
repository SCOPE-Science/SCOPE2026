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

# Reproducibility of the quadratic-Hessian cap theorem

The finite-check script \(\texttt{check_hessian.py}\) is contained alongside the scientific result. Run \(\texttt{python check_hessian.py}\) after installing \(\texttt{numpy}\) and \(\texttt{sympy}\); the observed successful final line was \(\texttt{HESSIAN_CAP_CHECKS_PASS 115}\). It checks the exact symbolic polynomial primitives for a free positive dimension parameter, three beta-moment normalizations and the tensor trace identity. It separately integrates all twenty-five entries of the full degree-two Hessian concentration Gram matrix in dimension three at nine polar cutoffs, using tensor-valued evaluations and Gauss–Legendre/azimuthal quadrature.

The complete all-dimensional theorem is not inferred from finite quadrature. Its proof requires the projected Riemannian Hessian identity, the three-sector orthogonal symmetry split and the exact integration-by-parts boundary differences proved in RESULT.md. The checker has only two packages as dependencies. Numerical integration is not an independent mathematical certification; independent audit has not been performed.
