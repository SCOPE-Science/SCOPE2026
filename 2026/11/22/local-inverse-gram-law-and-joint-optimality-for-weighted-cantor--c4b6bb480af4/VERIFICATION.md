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

The all-depth proof is an exact block inversion and row-norm induction. The standalone `CHECK.py` constructs complete finite Fourier evaluation matrices from digit strings rather than using the block recurrence; it computes their inverse rows, determinants, spectral inverse Frobenius norms, and finite design optima. The saved program returned `INDEPENDENT_WEIGHTED_CANTOR_INVERSE_TRACE_CHECKS_PASSED 2045`.

The tests cover eight base-gap pairs and depths up to four, plus the middle-third case up to depth five and finite digit-choice enumeration in six base-gap pairs. They also check alias-induced singularity. Finite floating-point computations do not certify all depths; that conclusion comes only from the symbolic proof in `RESULT.md`. No external or independent validation has been performed.
