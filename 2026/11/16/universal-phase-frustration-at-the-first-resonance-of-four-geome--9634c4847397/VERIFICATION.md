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

The standalone `verify_geometric_first_resonance.py` was executed from the package source before packaging. It uses the Python standard library to generate exact integer Fourier coefficients by multinomial expansion. Gaussian-unit coefficient powers have exact complex-integer arithmetic; their squared moduli are integral. It confirms phase-independence through half-order \(b\), the three-collision identity for bases two through five on all 256 Gaussian-unit phase arrays per base, all 16 binary phase arrays through base six, and the exact character-phase upper bound. Expected output: `EXACT_FIRST_RESONANCE_CHECKS_PASS 1129`.

The unrestricted minimum for every integer base follows from the displayed analytical completion of the square and the exhaustive three-fiber collision classification; finite tests are corroboration, not completeness over all bases or all phases. The root-of-unity obstruction is proved independently by the rational-algebraic-integer argument. No independent external audit or formal proof-system certification has been performed.
