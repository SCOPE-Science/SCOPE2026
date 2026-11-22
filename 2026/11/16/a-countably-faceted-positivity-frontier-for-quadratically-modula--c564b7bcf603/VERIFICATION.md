---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Fourier multiplication by cos theta and cos2theta gives coefficient q^(k^2) [1+alpha q cosh(2 tau k)+beta q^4 cosh(4 tau k)]. With y_k increasing and cosh(4tau k)=2y_k^2-1, the entire PSD test is a countable family of affine inequalities alpha>=L_k(beta), beta>=0 (beta<0 fails as k grows; beta=0 forces alpha>=0). At each given vertex (alpha_n,beta_n), exact polynomial factorization 2(y-y_n)(y-y_(n+1))/(1+2y_n y_(n+1)) proves positivity at ALL discrete frequencies, zeros only at neighbors and every line segment exposed. End ray follows F(y_j)=(y_j-1)[-1+beta q^4(2y_j+1)]; vertices exhaust the boundary. On each interval -h=a_n+b_n beta, the minimum of -h/sqrt beta occurs at beta=a_n/b_n in the interval asymptotically, and convexity as a function of sqrt beta puts maximum at endpoints; yields exactly the stated two asymptotic constants. All admissible spectra are eventually strictly positive, giving Vandermonde finite-site strictness; a spectral zero obstructs C-universality, while all-positive spectrum gives trigonometric-polynomial density. Independently exact rational vertex/facet checks corroborate selected n and q.

## originality

PASS

Distinct two-parameter multiplicative perturbation of theta heat kernel is not implied by positive-definite cone generalities, one-harmonic geodesic-exponential staircase, or exponential-of-two-cosines positivity. Material comparison found no earlier same exact cone and sharp cusp; best-of-knowledge PASS, leaving theta/covariance historical risk.

## value

PASS

The exact countably infinite exposed positive-type cone is a structural classification, not an arbitrary grid sample. The two distinct sharp square-root cusp constants and finite-site SPD versus nonuniversality give nontrivial spectral/approximation features that a researcher may directly need for signed covariance modulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
