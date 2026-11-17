---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Rotational invariance and first-Hermite STFT overlap diagonalize the operator with λ_n=∫ e^-u u^{n−1}(u−n)²/n! du. For R=s+L/2 and n=R+x√R, fixed-area symmetric integration and Stirling give L/√(2πR)[f(x)+R^-1/2g(x)+O(R^-1)] with f=x²e^-x²/2, g=f(x)(x³−3x)/6. f has exactly two positive global maxima x=±√2 of height 2/e and strict negative curvature. At these points the correction is ±(2/e)(√2/6), so M_-−M_+=2L/(3e√π R)+O(R^-3/2)>0. Chernoff tails exclude remote n and a differentiable peak perturbation plus lattice rounding gives optimizing n=R−√(2R)+O(1). Independent symbolic substitution confirmed the opposite ±√2/6 corrections. The other positive peak persists as local max. θ etc irrelevant. Reproducing normalization requires ∑_n Poisson(u,n)(u−n)²/u=1; user-supplied code checks finitely, proof uses exact variance identity.

## originality

PASS

Best-of-knowledge relative to earlier established mathematics: the signed 1/R selection for k=1 is absent from the Gaussian annulus and general Hermite–Laguerre machinery. A separate, apparently subsequent same-day Resultary all-fixed-orders theorem mathematically contains this as k=1, but explicitly identifies the first-Hermite calculation as prior work; it is a generalization of the target, not evidence that target was already covered when first established. Exact priority/time order remains a caveat.

## value

PASS

The first excited Hermite localization operator has a natural two-shoulder near-degeneracy unresolved at leading order; the exact signed correction and norm comparison give a sharp spectral selection rule useful for polyanalytic localization. The mathematical point is motivated, not merely an arbitrary eigenvalue computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
