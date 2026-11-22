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

The analytical argument is self-contained: characterize the unique constrained minimizer by strict convexity, reduce by its support-stabilizer group, use finite-field character orthogonality to obtain the three Fourier levels and optimize the resulting quartic. The explicit cubic root is checked by substitution. The program `artifacts/check_certificate.py` computes independent character transforms for five prime-field instances and tests the normalized extremizer and objective. These finite numerical checks are supplementary and do not certify infinitely many field sizes. No independent audit has been performed.
