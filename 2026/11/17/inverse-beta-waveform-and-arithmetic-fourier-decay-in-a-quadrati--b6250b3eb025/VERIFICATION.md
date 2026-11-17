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

Analytical checks: substitute the two first integrals into the vector field; transform half-flight time integrals into the symmetric Beta(1/3,1/3) CDF; derive crossing jets through order six by power-series substitution; show the coordinate series contains only powers divisible by three; apply repeated Fourier integration by parts including the order-nine remainder. Exact phase-factor cancellation proves the integer-frequency conclusions. The program `check.py` is numerical diagnostic evidence, not a substitute for these arguments.

Reproduce the diagnostic with `python check.py` (Python 3; NumPy and SciPy required). It evaluates the actual inverse-beta waveform at 131072 equally spaced times, Fourier coefficients in three parameter regimes, and exact balanced half-turn antisymmetry. This finite computation does not certify infinite Fourier estimates, which rest on the analytic argument. Independent audit has not been performed.
