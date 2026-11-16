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

# Verification and limits

The included `CHECK.py` is standalone alongside `requirements.txt`. Running `python CHECK.py` in the saved package returned `THREE_TONE_GAUSSIAN_CHECKS_PASSED 212`. It checks the exact Gaussian transform identity in two forms, derivative factorization, the first eleven nontrivial power-series coefficients, sample global intensity profiles by numerical peak extraction, uniqueness and signs of the noncentral critical point across representative parameters, numerical critical curves for ten amplitudes, and both critical scaling laws. A separate adaptive quadrature calculation confirms the short-time Fourier integral at representative frequencies. The explicit calculation is a finite check; no finite grid proves the all-parameter theorem. The actual proof is the convergent sign-variation argument in `RESULT.md`.

Scientific scope: deterministic phase-opposed three-tone signals with a Gaussian window, at the specified time. The computed maxima include tiny peaks of arbitrarily low height. No claim is made about noisy detection, other phases or global time-frequency ridges. The manuscript of a closely related two-tone 2026 source was not read in full, and priority remains subject to that risk. No independent mathematical audit has been performed.
