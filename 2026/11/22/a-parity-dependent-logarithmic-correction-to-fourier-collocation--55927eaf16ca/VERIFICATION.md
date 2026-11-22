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

# Reproducibility and scope of evidence

Run `python verify.py` with Python 3 and `mpmath` in the directory containing the script. It evaluates the exact finite Fourier sums, an independently constructed periodized-Gaussian expression, and omitted high-frequency tails with 135-decimal-place arithmetic. In the completed run, 346 finite assertions passed, including selected even/odd grid sizes, full positivity checks over every grid separation for the selected late timesteps, mass conservation, and explicit negative near-antipodal entries at early times.

The finite tests corroborate but are **not** an exhaustive proof for all grid sizes and all real times. The proof of the \(O(N^{-2})\) two-parity expansion is the uniform tail bound (including all subsequent times) plus the explicit negative witness in `RESULT.md`. All source-comparison and publication-priority qualifications are stated in `REVIEW.md`.

No independent audit has been performed.
