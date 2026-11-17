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

`python check.py` requires only the Python standard library and outputs `ALL_VARIATION_GAIN_CHECKS_PASS` after passing both independently derived impulse-kernel checks and an exact-rational nonmonotonicity certificate.

The rational certificate uses a finite section of radius seven at each of the two rational smoothing parameters. It checks the residual of the *whole-lattice* five-point operator after zero extension, so the resulting norm bounds apply to the genuine infinite inverse rather than a finite-system surrogate. For comparison, the complex-root calculation checks the full resolvent recurrence to floating-point accuracy and absolute kernel mass. Additional finite-input tests probe convolution and continuum scaling; they do not independently prove the theorem's infinite assertions.

The exact weak- and strong-smoothing limits, operator sharpness, negativity of the impulse response and first-negative-index scale are established by the analytical proof in RESULT.md. The numerical constant is a closed expression, not fitted to experiments. Historical originality is not independently certified.
