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

The finite marked hub-fire expression is evaluated by `fire_star_verify.py`, using no external Python modules. The checker constructs the exact killed-leaf polynomial over three formal exponential variables, integrates each monomial by its two positive decay denominators, and compares every fire-size probability to an independently generated absorbing continuous-time Markov chain on states (hub occupied/vacant, number of occupied leaves). Exact rational Gauss–Jordan elimination is used on the generator, not simulation or floating-point integration.

Run `python fire_star_verify.py`. The checked cases are \(1\le n\le5\) and lightning rates \(1/4,1/3,1/2,2/3,3/2,2\); all 30 distributions match coefficient by coefficient, are normalized, and assign positive mass to each possible hub-fire size. This finite checker is supplementary to, not proof of, the all-\(n\) and continuum statements.

The analytic verification establishes (i) regeneration at hub fires, (ii) the independent killed-leaf factorization, (iii) convergence of the aggregate ignition hazard at \(\lambda_n=c/n\), (iv) uniform exponential-convolution survival tails at fixed \(c\), and (v) renewal-reward convergence of stationary age and occupancy. The covariance limit uses exchangeability and bounded moment convergence. The explicit endpoint limits follow from the time-changed hazard and the fact that \(1-e^{-E}\) is uniform on \((0,1)\) for \(E\sim\operatorname{Exp}(1)\).

Historical-priority comparisons do not constitute an independent audit. No claim about all-event fire sizes, arbitrary graph topologies or independent scientific certification is made.
