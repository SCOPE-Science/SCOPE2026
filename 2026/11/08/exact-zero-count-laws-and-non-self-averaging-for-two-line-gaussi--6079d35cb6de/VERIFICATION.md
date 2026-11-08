---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and bounds

The standard-library script `CHECK.py` can be run as `python CHECK.py`. It tests direct nonzero Gaussian-STFT cancellation at formula-predicted zeros, spacing, exponential-ratio CDF and density, a separate analytic smoothed-PSD differentiation identity, and exhaustive phase bins for the exact Bernoulli count moments. The proof in `RESULT.md`, not the finite test grid, establishes all-parameter validity. The double-Gaussian nonzero condition holds almost surely; the frequency event has probability \(p\in[0,1]\) and includes boundary values. No independent scientific audit or publication-priority verification has been performed. The comparison with the 2026 colored-noise paper is limited by its PSD-function assumption, which excludes the atomic spectral measure here.
