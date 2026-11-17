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

The two sample paths solve the same autonomous smooth polynomial flow exactly and have constant equal speed and minimal period 2π. In real Hilbert H=L²(circle,C²), the parallelogram identity proves every minimizer of equal-weight orbit-distance squared lies at a midpoint of optimally shifted pair samples, so no hidden higher-harmonic minimizer exists. Cross correlation cosφ-a²cos2φ=a²+x-2a²x² is a strictly concave quadratic in x=cosφ, proving one mean for a<=1/2 and exactly two inequivalent means for a>1/2; variance and optimizer gap follow algebraically. At m0=(e^{it},0), each best phase shift is exactly zero; yet C_a''(0)=4a²-1>0 makes nearby midpoint classes strictly better when a>1/2, so algorithm fixed point is not even a local minimum. Independently checked rational amplitudes and curvature sign.

## originality

PASS

The quotient midpoint reduction and generic phase-aligned nonuniqueness are old. The earlier October 26 Resultary two-lobe planar family has a different k=2 Fourier correlation and threshold ε²=2/5, and it allows distinct planar flows; it does not give the current pair of *different orbits in one polynomial flow*, constant-speed normalization equality, sharp a=1/2 classification and exact arithmetic-initialization fixed-nonminimum gap. Full Hering–Kuehn source remained inaccessible and is a real priority risk.

## value

PASS

A completely worked two-real-orbit dynamical example where the global phase-quotient Fréchet mean bifurcates from unique to two classes, while a natural deterministic alternating alignment algorithm stays forever at a demonstrably nonlocal-minimum. It separates optimization geometry from representation and arc-length sampling effects.

The dated certificate retains the supplied scientific assessment, sources and limitations.
