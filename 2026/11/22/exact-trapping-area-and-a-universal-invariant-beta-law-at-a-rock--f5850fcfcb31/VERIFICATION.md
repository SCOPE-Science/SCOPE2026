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

# Reproducibility and mathematical limits

The theorem is proved symbolically in `RESULT.md`. To check its exact algebraic identities, finite-parameter quadratures, and convergence ratios, run `python3 verify.py` alongside the files with Python 3, SymPy and mpmath installed. The checker has no network or file input dependency and uses 65-digit working precision for its quadratures.

The checks consist of an exact saddle-energy quartic factorization, cubic fold expansion through the necessary order, explicit limiting-area evaluation, the critical prefactor, Beta density mass and mean, eight high-precision comparisons of independently expressed quadratures, strict decrease along eight sampled parameters, and endpoint scaling tests. They are **finite numerical corroboration**, not an exhaustive proof of strict decrease, total-variation convergence, or any infinity-parameter claim. The latter follow from the analytic factorization, endpoint estimates, and the convergence-in-measure argument in `RESULT.md`.

The mathematical claim concerns the undamped canonical radial flow, not the full physical impact problem. No independent mathematical audit has been performed.
