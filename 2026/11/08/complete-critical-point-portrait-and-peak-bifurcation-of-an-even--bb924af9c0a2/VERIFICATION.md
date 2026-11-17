---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Writing H=e^{-(x²+y²)}(cosh(2ax)+cos(2ay))/2 yields xD=a sinh(2ax), yD=-a sin(2ay). If xy≠0, sinh(2ax)/(2ax)>1 while -sin(2ay)/(2ay)≤1: impossible. Imaginary roots y=-a tan(ay) are uniquely isolated by strict monotonicity on the stated half-periods, with Hessian signs (+,-); simple cosh zeros have Hessian 2a² exp(-|z₀|²)I. On real axis x=a tanh(ax) has positive solution only for a>1; the origin Hessian is (2(a²-1),-2(a²+1)), with -x⁴/6 at a=1. Global inequality H(x+iy)≤e^{-x²}cosh²(ax) proves the global maxima without a numerical scan. Independently differentiated the logarithm and checked the quartic series symbolically.

## originality

PASS

Best-of-knowledge PASS. Abreu (2022) proves statistical critical-point intensity laws for white-noise Gaussian entire functions and supplies the generic covariant derivative, not the deterministic balanced two-coherent-state Morse portrait. The 2001 Miranowicz–Bajer–Wahiddin–Imoto cat paper concerns Wehrl/Husimi phase densities and entropy; the exact deterministic complete planar Hessian/zero/saddle classification is not established by the material available. Searches of Fock, Husimi and even-coherent spectrogram variants found no theorem implying these all-a critical-point counts, but the 2001 full text remained inaccessible, creating genuine priority risk.

## value

PASS

PASS. An exactly solvable canonical balanced coherent-cat spectrogram has infinitely many zeros/saddles and a sharp, nontrivial peak-pitchfork at dimensionless separation a=1. A complete global critical portrait, exact no-off-axis theorem and quartic transition resolve a natural signal geometry question beyond local root plots, although unbalanced and multimode variants remain open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
