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

# Verification record

The standalone `CHECK.py` uses NumPy and SciPy. Running `python CHECK.py` from this package performed 86 successful finite diagnostic assertions. These compare the Fourier primitive with independently integrated forcing terms; the finite-rate exact second moment with a direct exponential-age integral; the near-critical formula with finite-rate calculations; and the limiting site probabilities and Bessel second-moment normalizations. Reported numeric constants correspond to the first positive zero of the Bessel function `J0` with normalized hopping and frequency.

The analytical proof, including limits for all lattice sites and all positive sufficiently small reset rates, is given in RESULT.md. Finite numerical diagnostics alone cannot validate infinite-time laws, originality, or the sharp all-parameter necessity and sufficiency. No independent scientific audit has been performed.
