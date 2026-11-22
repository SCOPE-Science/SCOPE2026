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

# Verification details

The analytic coefficient calculation in RESULT.md identifies the precise gamma ratios. The exact critical squared-weight formula and independent beta-product moment identity follow algebraically from the gamma and beta Pochhammer formulas. The Fredholm index argument establishes the spectral disk; the two-column overlap asymptotic proves the strict norm gap.

The standalone Python checker `check_mixed.py` uses only the Python standard library. Run `python check_mixed.py`. It verifies 285 exact rational beta-moment/weighted-shift relations and finite floating-point witness and gamma-ratio identities. Output: `PASS: 285 exact moment and numerical witness diagnostics`.

The numerical checks are not exhaustive, do not certify an infinite sequence and do not establish the spectral theorem by themselves. No independent mathematical audit has been performed.
