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

# Verification

The theorem's exact quantifiers, event definitions, endpoints and sign claims are proved in `RESULT.md`. The file `check_window.py` is a standalone SciPy diagnostic checking the normalized Gamma/exponential density and cumulative functions, their two and one crossings, exact crossing residuals, finite-width sign intervals, monotonicity in window width, and the large-shape critical-width limit. It passed 59,007 assertions in the recorded execution.

The finite diagnostics cannot establish uniqueness over an infinite domain. This is instead established analytically by the two density crossings, the single cumulative crossing, and two strictly decreasing equal-height companion-distance functions. The central-limit argument is used only for the asymptotic coefficient, not to certify finite-shape crossings. No independent review or external certification has been conducted.
