---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Gaussian STFT of two nonzero Gaussian spectral amplitudes is an exact sum of two shifted Gaussian frequency factors times phases. Modulus equality fixes one Ω; phase cancellation produces a uniform translated time lattice with spacing 1/Δ. Log ratio of iid exponential squared moduli gives Ω logistic of location μ and scale 1/(4πΔ), independent of the uniform relative phase U. Counting one translated lattice in [a,a+T) gives floor(ΔT)+Bernoulli(frac ΔT); retaining all points iff Ω belongs to J gives N=H(floor ΔT+B), independent H. Thus variance p u(1−u)+p(1−p)(ΔT)^2 and almost sure N/T→ΔH. Fresh deterministic exact STFT cancellation residual <8e−16 and high-precision logistic density integral 1 confirm normalization; the proof, not numerics, proves all parameters.

## originality

PASS

PASS best-of-knowledge: colored noise spectrogram first-intensity theorem assumes PSD function rather than pure atomic two-line spectral measure; its expectation does not imply joint counting distribution/variance. Classical two-term exponential zeros are periodic but the precise logistic random line, independent phase and non-self-averaging fluctuation contrast are not located in same-model published results.

## value

PASS

A sharp natural atomic-spectrum boundary case for Gaussian spectrogram zero statistics, giving full nonergodic random geometry and exact finite-window zero counts, and separating bounded full-band zero fluctuations from quadratic band-filtered variance. Offers a principled counterexample to extrapolating PSD-function mixing behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
