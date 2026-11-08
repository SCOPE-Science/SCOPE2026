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

# Mathematical verification

The exact one-step drift and martingale cross-bracket can be reconstructed from the explicitly specified parent-label mixture in RESULT.md. The paired-degree coefficient recurrence yields \(Q_\alpha\), and the linear drift of each degree-count vector yields the covariance resolvent \((3-z-w)^{-1}\). The rational simplification and the low-degree coefficient formula are purely algebraic.

Running `python3 verify.py` from this directory completed **649 exact rational assertions**. Tests included six rational values of the sharing parameter (including the two endpoints), equality of the two bivariate rational series through degree seven in each variable, the \((0,0)\), \((0,1)\) and \((1,1)\) coefficients, a covariance-minor identity, and conditional innovation covariances enumerated across small parent-state arrays. Test inputs and output count are printed by the standalone script. The finite arrays used in conditional-bracket tests need not be reachable as actual trees because the parent-choice algebra holds for arbitrary aligned degree arrays.

A separate finite simulation sanity check on 15,000 pairs of trees with 1,000 vertices per pair at several sharing probabilities produced covariance estimates close to the analytic first coefficients within sampling precision. The simulation is not a mathematical certificate and is not needed to replay the proof.

The almost-sure paired-degree limit and Gaussian joint limit rely on the stated stochastic-approximation and martingale-CLT arguments. In particular, finite coefficient arithmetic and Monte Carlo cannot establish a central limit theorem. This result does not establish an infinite-dimensional degree-profile topology or exact finite-sample Gaussianity. Independent mathematical audit and definitive historical-priority assessment have not been performed.
