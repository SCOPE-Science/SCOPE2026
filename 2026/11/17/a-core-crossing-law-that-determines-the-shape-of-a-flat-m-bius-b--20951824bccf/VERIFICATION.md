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

# Verification of the core-crossing law

The analytic argument is given in RESULT.md: it reduces all geodesic candidates to the nearest even and odd glide lifts, identifies the sign condition for meeting the core, integrates the explicit product density, and differentiates the resulting complete aspect-ratio law. It covers every positive width-to-core-length ratio, with equality at the branch point and limiting values established directly.

Reproducibility: `python verify_core_crossing.py` with the versions available of NumPy and SciPy. The script uses an independent quadrature transformation to handle the integrable logarithmic endpoint, checks exact closed-form probabilities at nine aspect ratios, and samples 650000 independent endpoint pairs at each of six ratios. It enumerates the actual even and odd squared distances and classifies whether the minimizing segment crosses the core. It also compares a 10001-point monotonicity grid and exact derivative matching at the branch. The script prints `MOBIUS_CORE_CROSSING_LAW_OK 650000 6` only after all checks pass.

Limits: quadrature and Monte Carlo are finite numerical corroboration, not the proof of the all-parameter formula or the uniqueness theorem. The flat-metric classification is discussed analytically and must be distinguished from extrinsic embeddability. No independent mathematical or historical audit has been performed.
