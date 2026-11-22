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

# Reproducible verification

The central proof is analytical. Its critical identities are the independent Gamma-block and Dirichlet-proportion representation, the covariance factorization (1), the strictly positive derivative (2), the baseline beta moment (3), and the complete beta-prime large-scale trichotomy (4). These establish the result for every positive real shape and scale, including the cases in which inverse moments diverge.

The standalone file `verify_covariance.py` requires Python 3 and `mpmath` 1.3 or later. Execute:

```text
python verify_covariance.py
```

This integrates beta expectations at 45 decimal-digit precision for five distinct ordered block-total pairs, brackets each critical root, tests the strict derivative at seven scales per pair, and checks the three pairwise covariance types for eight scales in a four-dimensional positive-spherical area-uniform example. It reports **96 passed deterministic numerical assertions**, including the brackets

\[
4.258065<R(1,1)<4.258067,
\qquad
0.234848<R(1,1)^{-1}<0.234849.
\]

For the four-dimensional example with all shapes \(1/2\), at scale \(r=0.1\) the first-block, second-block, and cross-block covariances are approximately \(-0.06372764\), \(+0.00504472\), and \(-0.01174198\); at \(r=10\) they are approximately \(+0.00504472\), \(-0.06372764\), and \(-0.01174198\). An independent direct Gamma Monte Carlo stress test with 700,000 samples confirmed these signs to sampling accuracy.

**Limits of numerical checks:** The computed quadratures have not been interval-enclosed, so decimal root brackets are diagnostic rather than rigorous numerical certificates. The theorem's existence, uniqueness, strict inequalities, and universal signs do not depend on the numerical bracket or Monte Carlo experiment. Independent mathematical assessment has not been performed.
