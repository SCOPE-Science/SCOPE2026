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

# Reproducibility and limits

The evidence consists of the analytic calculations in `RESULT.md` and the standalone Python 3 program `verify.py`. The program uses only the standard library (`math`, `cmath`), and was executed from the actual source package directory. It prints `PASS 127 independent arithmetic checks`. It evaluates the complex harmonic derivative of the deterministic density, integrates its squared deviation from unit slope with Simpson quadrature, compares an independently assembled complex mode-lag ratio to the closed form, and tests the sharp-asymptotic coefficients for several increasing mode numbers.

The polynomial root and approximate constants in the theorem are also independently checked arithmetically. These calculations verify selected points only; they do not establish all-positive-mode uniqueness or an infinite asymptotic. The proof supplies positivity of the cost, localization of maximizers, strict concavity near the limiting optimum, and the uniform expansions needed for that conclusion. No external/independent audit was performed.
