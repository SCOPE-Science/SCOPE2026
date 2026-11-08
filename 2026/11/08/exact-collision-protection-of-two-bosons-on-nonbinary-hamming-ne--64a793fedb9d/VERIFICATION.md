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

Run `python formula_replay.py` for exact integer/rational coefficient checks. The standard-library program reproduces the dark dimensions and distance-resolved capture fractions of six finite networks and evaluates the \(d=2\) rational specializations for thirteen alphabet sizes.

Run `OPENBLAS_NUM_THREADS=1 python matrix_replay.py` with `numpy` installed, as specified in `requirements.txt`. This independently constructs the full bosonic symmetric Hamiltonian, computes its eigenspace-wise collision span, checks the bright projector's idempotence and its action on every collision-diagonal basis vector, and compares the six example cases with the exact fractions.

The finite numerical spectral tolerance is \(10^{-7}\); its results are corroborations, not a general proof or certified interval arithmetic. The all-dimension proof is the Fourier-sector argument in `RESULT.md`. The checks do not address imperfect detectors, finite-time decay, or interactions. Independent scientific auditing has not been performed.
