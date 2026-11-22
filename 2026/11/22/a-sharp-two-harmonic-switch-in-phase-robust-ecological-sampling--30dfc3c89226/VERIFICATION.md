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
# Verification notes

The theorem is proved by an explicit minimization of a scalar quadratic and separate global analysis of the interior and boundary branches. `checker.py` uses only the Python standard library; run it using `python3 checker.py` from this folder. It tests seven exact rational parameter identities, the algebraic switching polynomial, 60,015 grid comparisons in angular separation, and 16,000 additional seeded parameter/phase challenges, as well as both quoted illustrative probabilities. Its successful run prints `PASS`. These are finite supplementary tests; they do not certify all real parameters. Continuum correctness rests on the inequalities in `RESULT.md`.

The theorem assumes known positive harmonic amplitudes with aligned phases, positive mean at all times, equal-volume conditionally independent Poisson observations, and a phase-adversarial guarantee. This verification does not address other Fourier modes, parameter estimation, field-calibrated kinetics or general correlated observations. No independent external review, empirical validation, or mechanized proof has been performed.
