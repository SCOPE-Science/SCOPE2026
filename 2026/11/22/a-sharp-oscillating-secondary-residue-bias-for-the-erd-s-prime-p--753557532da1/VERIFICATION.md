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

# Reproducibility checks

Execute `python3 check_bias.py` with Python 3 standard library. The arithmetic checker independently builds exact prime-power quotient sums and Fourier weights for each integer from one through 20,000, including the separate reduction for multiples of three. It also verifies 64 local prime-power values and 30 Euler-series coefficients.

The output is `PASS: 20,000 exact integer residue identities, 64 prime-power checks, and 30 Euler coefficients`.

These computations test identities that enter the proof but are not a substitute for the analytic steps. The proof of the \(X/\log X\) asymptotic invokes the classical Selberg–Delange theorem under its usual fixed-complex-exponent hypotheses; the prime-factor correction is checked algebraically in RESULT.md. Product nonvanishing and limiting oscillation follow from exact mathematical arguments, not finite testing. Independent audit: not performed.
