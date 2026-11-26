---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

At zero flux the only real eigenmodes are the normalized dark sines from nontrivial Fourier pairs: dissipativity forces zero trap amplitude, and a pair has exactly one such direction. They also satisfy K_0^* d_k=E_k d_k, so their orthogonal complement reduces K_0 and has strictly negative imaginary spectrum. This justifies algebraic simplicity, not only a one-dimensional eigenspace. At small nonzero total flux Fourier energies are distinct and each plane wave sees the trap, so all modes decay. The two colliding energies have half-gap Delta=(2/n)sin(2pi k/n) phi+O(phi^3) up to sign. Multiplying the rank-one secular equation by (z-mu)^2-Delta^2 gives an analytic equation with z-derivative 2i gamma/n at the dark energy. Its root shift is (n/2)(h(E,0)-i/gamma)Delta^2+O(phi^3), giving the stated decay rate. The leading integrated contribution for each dark branch is its squared projected source amplitude divided by twice that rate. The other branch cross terms are bounded by distinct limiting frequencies, and the fast sector by a uniform finite-dimensional contour estimate. If every dark overlap vanishes, the perturbed slow amplitudes are O(phi), which suffices for bounded lifetime, not merely a zero scaled limit. Parseval on cyclic intervals evaluates the sine sum as a(n-a)/2 for odd n and b(m-b) for even n before the gamma/2 factor. The only zero coefficients are precisely the stated sites. An independent finite-flux Lyapunov calculation corroborated both parities and a bounded antipode with residual below 1.8e-11 in the tested cases.

## originality

FAIL

A distinct exact odd-ring Resultary formula directly includes every odd-size coefficient and the bounded trap case. More importantly, its Step 2 exact site-source spectral formula uses only equal-magnitude Fourier overlaps and simple energies, with no odd-size assumption. Applying that identity to the even Fourier pairs yields exactly the even site-resolved coefficient and the bounded exceptions; the even publication's mixed-source law alone would not suffice. The frozen proof's use of resonance projectors rather than this identity does not change coverage of the stated lifetime law. This is a mathematical coverage finding, not a determination of chronology from the paths.

## value

PASS

A position-resolved threshold between bounded capture time and a quantitative inverse-square divergence is useful for comparing transport on finite rings. The parity and distance dependence are visible neither from the presence of dark states alone nor from a mixed-source average. The spectral proof explains the separate roles of source overlap and the leakage rate. The judgment of usefulness does not make the mathematically covered law original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
