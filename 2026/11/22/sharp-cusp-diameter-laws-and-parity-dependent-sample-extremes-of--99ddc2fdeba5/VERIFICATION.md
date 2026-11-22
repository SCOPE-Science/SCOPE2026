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

The standard-library Python program `verify_hypocycloid.py` re-evaluates the geometric parameterization rather than using any precomputed probability table. Run `python3 verify_hypocycloid.py` from this directory. At the tested settings it reports `VERIFY_OK 21658 deterministic checks` plus six pairs of asymptotic and numerically integrated constants. The tests cover arclength inversion, every cusp position, the adjacent-side halfplane bound, diameter upper bounds, all four cusp branch combinations, and near-diameter numerical midpoint integrations for six distinct cusp counts. The geometry and stochastic limit proofs are written in `RESULT.md`; the computations corroborate but do not replace them.

Test scope: integer cusp counts 3–10 for geometric checks; 3–8 for pair-tail quadrature at one strictly positive deficit; finite random samples at 3–7; and a finite list of values for the three-cusp exponential survival. The infinite-parameter theorems follow analytically from the stated expansions and probability convergence, not the test counts. The scientific review is same-model only; independent audit has not been performed.
