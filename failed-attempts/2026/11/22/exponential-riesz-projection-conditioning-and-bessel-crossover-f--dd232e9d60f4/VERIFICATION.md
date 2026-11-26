---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

On complex ell2, C_t=D(I-tS)^(-1) is compact and its nonzero spectrum is the listed eigenvalues; the accumulation point 0 is also in the spectrum. The least nonzero coordinate identifies the eigenvalue and the triangular recursion leaves one free coordinate. The stated right and left vectors solve their eigen-equations and pair to one, ruling out a generalized chain and giving the rank-one Riesz projector. Parseval and the circle automorphism with its boundary Jacobian give the exact ratio of squared norms, hence the stated formula. The integral for W_m has a single nondegenerate maximum on the circle at zero; the quadratic coefficient t/(1+t)^2 gives the displayed fixed-t Gaussian prefactor and relative O_t(1/m). In the regime m t_m bounded, the factorial majorant gives convergence of the finite sum to I0(2 tau) and the prefactor tends to one. For t=0 the projections are orthogonal. Completeness follows because orthogonality to the system annihilates all Taylor coefficients of an analytic function at t. The biorthogonals give minimality, while the growing coordinate projection norms preclude any Schauder ordering or bounded similarity to a normal or scalar-type spectral operator. No conclusion is asserted at t=1.

## originality

FAIL

The exact quantitative result is mechanically implied by the published biorthogonal eigenvector coefficients and tabulated identities, and both scales are specializations of a single stronger classical uniform asymptotic. With x=t², the left squared norm is F(-m,-m;1;x); the right is F(m+1,m+1;1;x). Euler's transformation gives their exact ratio (1-x)^(-2m-1), and DLMF 18.5.8 at alpha=beta=0 gives ||P_m(t)||=(1-t²)^(-1/2) L_m((1+t²)/(1-t²)), where L_m is the Legendre polynomial. DLMF 14.15.13, uniform for xi>0, already gives L_m(cosh xi)=(xi/sinh xi)^(1/2) I0((m+1/2)xi)(1+O(1/m)). For xi=log((1+t)/(1-t)), this gives both the exact critical profile and, via 10.40.1, the fixed-t prefactor and rate. Uniform boundedness of coordinate or spectral projections then gives the structure obstructions directly. No exact prior operator-theoretic wording is alleged; the rejection is based on this explicit chain of standard equalities and a stronger prior asymptotic, not the title similarity of an indexed Fock result.

## value

FAIL

Projection conditioning for compact nonnormal operators is a motivated invariant. Here the evaluated invariant is already determined by the published binomial eigenvectors and the tabulated transformations, and the two regimes split a known stronger uniform estimate. The remaining basis and similarity properties are routine consequences of projection unboundedness, not a distinct structural result. A restatement as a Legendre law or as a boundedness obstruction would not remedy this.

The dated certificate retains the supplied scientific assessment, sources and limitations.
