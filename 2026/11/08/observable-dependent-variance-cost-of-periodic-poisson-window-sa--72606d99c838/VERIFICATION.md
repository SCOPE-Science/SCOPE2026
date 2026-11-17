---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

A unit-length sliding window always has Poisson(λ) marginal. For overlap λJ_v(t), the two-window Poisson generating function is exp(λJ_v zu) after Charlier centering, giving exact diagonal covariance delta_rs r!λ^r J_v^r. Orthogonal L² expansion and Tonelli give a finite nonnegative infinite variance series; one-dependent stationary integrals across integer time periods establish CLT and variance for merely L² observables. Average_t J_v=1-v; convex Jensen makes uniform η minimal, with strictness for every nonzero higher Charlier component and every nonconstant Fourier mode of η. For h=(n)_2, the r=1,2 modes and Parseval reproduce the exact published Fourier penalty; for h=n variance is λ. Independently checked Charlier covariance at λ=3/2 and overlap=2/5 (exact 153/25) and harmonic penalty numerically.

## originality

PASS

The October 18 published Poisson-window result ALREADY supplies the exact second-factorial-moment Fourier penalty, its unique optimal uniform intensity, linear-observable invariance and the associated CLT: none of that is new. The SURVIVING statement uniformly handles every square-integrable Poisson count observable with the exact Charlier-mode sum and an iff characterization of equality for nonconstant intensity, including merely measurable bounded rates. The earlier theorem explicitly limits its scope to the quadratic estimator and does not state or imply this all-observable classification without additional spectral orthogonality and Jensen reasoning.

## value

PASS

The practically motivated open question is whether arbitrary nonlinear count observables lose efficiency under periodic modulation even when the Poisson target and linear estimator remain unchanged. Extending a known single quadratic Fourier penalty to an exact positive Charlier-spectrum formula for ALL Poisson L² observables and an iff affine equality characterization is a mathematically useful design principle, not a routine re-labeling of the quadratic formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
