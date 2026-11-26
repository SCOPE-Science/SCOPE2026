---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The probability measure and unscaled Fourier phase give T(a+Q)(rθ)=a j0(r)−Q(θ)j2(r); Euclidean polar integration multiplies each spherical average by 4π. Independently recomputed the derivative-product Gram matrix from compactly supported one-dimensional convolutions: the needed radial integrals divided by π are 1/4, 1/20, −1/28 and 11/140. No endpoint distributional masses appear since the even convolution functions are continuous and compactly supported with square-integrable weak derivatives. Fixing a real nonnegative by common phase and writing Q=U+iV gives the exact three nonconstant terms a²(6||U||²+2||V||²)/5, (4a/7)E[U(U²+V²)], and (11/35)E[(U²+V²)²] after division by π². For W=ω^TAω with A symmetric trace-free, E W²=2 tr(A²)/15, E W³=8 tr(A³)/105, and E W⁴=4(tr(A²))²/105. The degree-two projection of W² has matrix (4/7)(A²)_0 by applying the Euclidean Laplacian to the harmonic decomposition of W²; tr(A⁴)=(tr(A²))²/2 verifies its norm factor 2sqrt(5)/7. This bounds both cubic terms, and Cauchy–Schwarz bounds the quartic term. If a>0 and Q≠0, the quadratic inequality forces V=0; the maximal positive cubic moment at fixed trace norm has two equal eigenvalues and one positive simple eigenvalue, precisely the stated positive zonal class. At a=0 equality instead requires U² and V² proportional (or one zero); homogeneous polynomial factorization implies U and V proportional, giving all real harmonics up to complex scalar. The constant case is immediate. Replay: python3 /workspace/review_evidence.py, extension section, exact SymPy radial and latitudinal/azimuthal moment calculations. The code checks arithmetic identities, not sharpness or exhaustive equality; these follow analytically.

## originality

PASS

Best-of-knowledge pass for the prescribed-energy ordinary L⁴ extension profile with its joint mixed complex equality classification. Do not credit the pure degree-two equality geometry, the diagonal modal radial factor as a class of moments, or the constant–degree-two squared radial coupling as distinct advances: those components are covered by prior indexed statements. The available full-profile comparison for the mixed radial–angular norm differs in both functional and optimizing degrees. The exact inside-band ordinary profile and equality transition require different mixed quartic terms and simultaneous equality. Tang–Xu's complete Appendix B comparison remains an access risk, not evidence of absence.

## value

PASS

A full, low-harmonic-band constrained optimum gives an exact benchmark for spherical extension stability at the degree-two interaction, beyond the constant global bound and known pure-mode moment factors. The mixed cubic term changes the equality geometry in a way not captured by either the pure angular norm or a mixed radial–angular bound. No claim about unrestricted prescribed-mass extension is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
