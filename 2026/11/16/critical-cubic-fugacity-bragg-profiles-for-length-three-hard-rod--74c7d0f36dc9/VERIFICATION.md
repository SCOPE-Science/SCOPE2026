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

# Reproducibility and proof checks

The standard-library file `check.py` is self-contained. Run it with `python check.py`. It enumerates all admissible configurations for small cycles, checks the exact gap-composition count and finite Fourier covariance against independent state sums, and compares finite volume Fourier intensities against the limiting integral and factorial-series expressions. It reports `PASS 111 finite assertions` when complete.

The mathematical proof in `RESULT.md` handles the infinite family: a factorial dominating sequence controls the critical defect weights, a stars-and-bars collision bound controls the limiting gap placements, and boundedness of normalized Fourier amplitudes permits passage to the expectation. The central Dirichlet identity is proved symbolically from the exact second-moment formula. The numerical checks only test finite cases and finite truncations; they do not establish uniqueness or priority of the result and are not an external certification.

The limit requires fixed positive activity coefficient and fixed integer frequency offset. Neither arbitrary varying coefficients nor all Fourier frequencies are claimed.
