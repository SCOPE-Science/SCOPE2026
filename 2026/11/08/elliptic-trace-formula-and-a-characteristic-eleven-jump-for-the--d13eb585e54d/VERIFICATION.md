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

## Reproducible checks
Run `python verify_sextic_energy.py` from this directory. It directly computes the ordered sextic-graph pair-sum histogram and its exact squared energy, evaluates the two character sums and the intersection-root count separately, and tests the independent quartic-curve point count for seventeen prime fields and three quadratic extension fields. The exact integer/rational checks pass with `SEXTIC_GRAPH_EXACT_ENERGY_CHECKS_PASS`.

## Analytic checks and limits
The proof is by polynomial factorization, quadratic-character point counts, and inclusion–exclusion for all finite fields of characteristic greater than five. The squarefree-cubic assertions are restricted to characteristics other than eleven; characteristic eleven is computed separately. Exhaustive small-field computations do not prove an infinite-family claim, and the exact energy does not establish an unrestricted sharp extension norm. Independent mathematical validation has not been performed.
