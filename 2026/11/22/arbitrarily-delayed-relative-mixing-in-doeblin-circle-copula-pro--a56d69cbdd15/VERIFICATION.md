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

The theorem is proved analytically in `RESULT.md`: normalization and stationarity, independent-regeneration decomposition, Fourier spectrum, Fourier-coefficient asymptotic, generalized Young sufficiency, Fejér-kernel necessity, exact even-lag supremum, and boundary pole.

The standalone `CHECK.py` was run with Python 3 and `mpmath` in the same extracted scientific package; it printed `ALL NUMERICAL CONSISTENCY CHECKS PASSED`. The checks cover three exact rational two-step identities, three numerical Fourier asymptotics, the sign and ordering of a positive finite Fourier series, two divergent truncated critical integrals, and five rational threshold indices. The finite tests check calculations and do not certify the proof's universal quantifiers.

The first public source is arXiv:2204.04336, initially submitted 2022-04-09. Comparison with the 2025 follow-up and earlier copula mixing work is in `RESULT.md` and `REVIEW.md`. No independent mathematical review or external formal certification has been performed.
