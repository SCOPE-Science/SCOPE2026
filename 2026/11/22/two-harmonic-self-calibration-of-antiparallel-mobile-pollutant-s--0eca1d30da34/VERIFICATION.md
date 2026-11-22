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

# Verification notes

The proof in RESULT.md derives all necessary and sufficient conditions algebraically for the complete stated parameter domain, without relying on numerical tests. The included `check.py` can be executed with Python 3, NumPy and SciPy and uses a fixed seed. It synthesizes 2,000 positive six-harmonic input fields, applies the analytic scan transfer factors, unknown gain/offset/position changes, and tests recovery from the first two Fourier ratios, plus four held-out modes each. It additionally tests the exact witness and the limiting phase laws. All 2,000 generated scenarios and 8,000 held-out harmonic comparisons passed in the recorded local execution. Their floating-point residuals are not error guarantees for arbitrary field measurements. No field data, calibration experiment or independent audit was performed.

The exact phase argument range is open. Zero response length and infinite response length are limiting cases, not accepted finite parameters. Feasibility is asserted only for the first two complex frequency ratios; other observed frequencies provide separate model checks. Positive gain is required to avoid a sign ambiguity. The time constant in physical seconds requires known scan speed and route circumference.
