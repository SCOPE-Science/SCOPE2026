---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The known Gaussian localization identity makes H(Ω)=double integral over Ω of exp(-pi|z-w|^2). Converting to squared-radius coordinates yields smooth upper-limit integrals. Expanding the two radial upper limits yields cross-boundary Gaussian circle convolution e^-2A I_|n|(2A), and self-boundary term -e^-2A I1(2A) after radial differentiation of the disk potential via divergence theorem. The n=0 constraint is removed by exact area conservation; n=1 cancels as translations. Bessel ratio derivative r_k′=1-(2k+1)r_k/x-r_k^2 plus r_k<1 initially proves strict I_{k+1}<I_k for k>=1; n=2 thus uniquely minimizes positive curvature. Standard Bessel asymptotics yield c(A)=A+O(A^2), c(A)~3/(8 sqrt(pi) A^(3/2)). Independent quadrature of the double Gaussian boundary energy for two areas and four angular modes confirms expansion, but each fixed u has only pointwise o(epsilon^2) remainder; not a uniform global stability proof.

## originality

PASS

Nicola–Riccardi prove global disk maximality and quantitative HS deficit, but the inspected primary text does not exhibit this complete angular Fourier–Bessel disk Hessian and exact least-mode coefficient. Prior Resultary shape-Hessian works concern optimized top eigenvalues and Ky Fan sums, not squared HS norm; same location geometry is not same functional.

## value

PASS

Exact spectral curvature resolves local stability anisotropy of a widely studied localization functional, identifies the least expensive ellipse-like deformation and gives sharp aperture scaling. It refines existing global rearrangement bounds with a natural mode-resolved invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
