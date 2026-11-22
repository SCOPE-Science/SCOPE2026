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

The standalone `verify_catalan5_recovery.py` runs using standard Python 3 and prints `CATALAN5_AFFINE_WALSH_ZERO_LOCUS_AND_SHARP_PROJECTION_PASS` on success. It checks the 42 paths by two enumerators, all 1024 signed multipliers via three independent exact constructions, the 256-pattern parity table, the affine zero equations, Parseval, the gap, Fourier inversion, and the kernel's exact absolute mass \(7/4\). The mathematical proof separately explains why averaging any projection onto the translation-invariant range preserves the range and cannot increase endpoint norm. No higher-semilength extrapolation or external mathematical audit is claimed.
