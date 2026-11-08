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

# Reproducibility and verification

Run `python verify.py` with Python 3.9 or later; the checker has no third-party dependencies.

The checker implements (a) 8,000 exact rational tests of the polynomial identity controlling the Rayleigh-quotient difference, (b) 40,000 deterministic-seed floating-point comparisons of directly normalized iterates and the analytic sign criterion, (c) 36 circular-grid probability comparisons using 20,000 equally spaced angles per case, and (d) square-root endpoint constant tests at three scales.

The expected concluding line begins `VERIFY_OK`. These finite checks identify implementation and algebra mistakes but cannot establish all-parameter or distributional statements. Those require the exact difference identity, the fact that the two-sweep vector never vanishes for a non-eigenvector start, and the arcsine distribution of squared coordinates of a uniform point on a circle. The proof in `RESULT.md` supplies these independent analytic arguments.

The coefficients are assumed exact, with no adaptive search, parameter learning, floating-point stability or continuation beyond the displayed second iterate. No independent mathematical audit has been performed.
