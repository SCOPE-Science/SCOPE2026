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

Run `python3 checker.py` with a standard Python 3 installation; no external packages are required. The source recomputes four independent unit-circle coefficients from a fixed seed, forms all three original complex autocorrelations directly, and separately evaluates the independent two-variable arcsine formula. It checks the symbolic Barker atom by comparing the integral with the exact rational value, and checks six numeric CDF thresholds against 100,000 direct trials plus near-atom values. `checker_output.txt` stores one recorded successful execution. Universal correctness follows from the derivation in RESULT.md, not the finite sample or quadrature. No formal external certificate, independent audit, or infinite computational verification is claimed.
