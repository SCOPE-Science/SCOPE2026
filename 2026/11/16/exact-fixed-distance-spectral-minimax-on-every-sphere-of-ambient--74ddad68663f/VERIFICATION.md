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

# Reproducibility

The complete normalized Gegenbauer proof appears in `RESULT.md`; it is valid for every integer ambient dimension at least five and every harmonic degree. The supplementary standard-library verifier `check_hypersphere_fixed_step.py` has been run successfully and returned `PASS 59232 exact rational assertions for ambient dimensions 5..100`.

The checks cover low-degree formulas, the exact fourth moment, spectral parity, 160 harmonic degrees, and a rational grid of two-degree lower bounds. They are not offered as finite certificates for infinitely many degrees or dimensions. The decisive higher-degree bound is the analytic fourth-moment inequality in `RESULT.md`.

No independent mathematical audit has been performed.
