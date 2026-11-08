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

# Reproduction

Execute `python3 verify.py` with Python 3 (only standard-library modules used). The program independently builds the full labeled-state continuous-time SIR generator, computes eventual infection-count distributions by exact rational first-step recursion, and compares those distributions to the conditional-triangle integral formula. Graph sizes are \(m=1,2,3,4\) and rates are \(1/2,1,2\). There are 12 coefficientwise distribution comparisons; the full test performs 95 grouped exact assertions, including normalization, means, finite variances, analytic difference identities and signs on each side of a crossover.

All 95 grouped assertions passed in the packaged-code replay. The 12 labeled-state calculations reached 18, 162, 1458 and 13122 states, respectively, at triangle counts 1, 2, 3 and 4. The maximum example has nine graph vertices. The checker requires no external data and does not assume the critical finite generating function in its labeled-state recursion.

# Analytical scope and caveats

The infinite-family proof is in `RESULT.md`: it uses a conditional product law, finite beta moments, Descartes' rule of signs and an explicit positive finite-size correction to the limiting variance difference. Exact finite checks do not by themselves establish the all-size assertions. The conditional Gaussian theorem is proved analytically, not numerically certified. Independent mathematical validation has not been performed.
