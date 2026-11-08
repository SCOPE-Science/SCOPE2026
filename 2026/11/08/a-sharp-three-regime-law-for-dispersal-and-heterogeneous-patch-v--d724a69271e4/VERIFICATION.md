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

# Reproducibility

Run `python verify.py` using Python 3 and SymPy. It solves the stationary two-by-two matrix Lyapunov equation, independently compares all three entries with the sum-difference decomposition, verifies the derivative and crossing identities symbolically, and checks extensive exact rational moment equations using covariance matrices assembled from integer Brownian-loading vectors. It also probes all monotonicity classes and the interior minimizer.

The extracted final package produced `PASS 55338 exact and boundary assertions`.

The analytical proof, not the finite assertions, establishes the infinite-parameter classifications. The checks do not certify historical priority or real-world ecological predictive accuracy. Independent audit was not performed.
