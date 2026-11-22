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

The theorem is analytical. For the one-subset small-deficit event, a gap-simplex transformation gives \((m\varepsilon)^{m-1}\) exactly under uniform sampling and \((m\varepsilon)^{m-1}(J_m(f)+O(\varepsilon))\) for positive Lipschitz sampling density. For two distinct candidate subsets sharing \(k\) sample labels, \(1\le k<m\), the joint probability is bounded by a constant times \(\varepsilon^{2m-k-1}\). Counting pairs by their overlaps and applying dependency-graph Poisson approximation gives the stated total-variation error. All claims concern fixed \(m\) and fixed \(x\) as the sample size grows.

The bundled `check.py` uses Python 3 standard library only. It was executed from the actual package location with output:

```
m=2, epsilon=0.140: empirical=0.280185, exact=0.280000
m=3, epsilon=0.095: empirical=0.080515, exact=0.081225
m=4, epsilon=0.078: empirical=0.030231, exact=0.030371
PASS: 321 deterministic assertions, plus 390000 seeded Bernoulli trials
```

It verifies numerical harmonic integrals for fifteen frequencies, finite deterministic rotation and event-count equivalences, finite intensity inequalities, and seeded Monte Carlo agreement with the exact uniform one-subset probability. Simulations, finite assertions, and error tolerances cannot certify any infinite-sample conclusion. The proof and dependency bounds are the required infinite-dimensional justification. No independently verified mathematical audit has been conducted.
