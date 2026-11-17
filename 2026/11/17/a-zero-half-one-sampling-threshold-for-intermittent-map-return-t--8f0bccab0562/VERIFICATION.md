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

# Verification and reproducibility

The independent-seed first-return survival function is derived from the published inverse-iterate identities for Li's map, then coupled exactly to the integer part of a shifted exponential power. The two error controls are the unit-floor bound and the gamma upper-tail cutoff. The analytical proof uses gamma concentration, the gamma central-limit theorem, union/Markov bounds, and a direct one-sided variance estimate.

Run `python verify.py` in an environment with SciPy. It checks 63 exact survival probabilities, four central gamma windows, four critical variance/extreme-event exponent inequalities, and seven strict side-regime cutoff conditions. No Monte Carlo convergence inference replaces the proof.

This verification is a same-model calculation and does not constitute independent mathematical audit. The result is for independent normalized-uniform initial points on a parameter-dependent inducing base; it is not a single-trajectory limit.
