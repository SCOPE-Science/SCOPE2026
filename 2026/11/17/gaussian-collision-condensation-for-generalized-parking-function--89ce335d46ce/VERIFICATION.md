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

# Reproducibility and verification

The standalone Python 3 standard-library file `verify.py` independently constructs all candidate permutation vertices and maximizes the objective over those vertices in all \(2^n n!\) equiprobable Gaussian signed-rank chambers. It verifies the exact probability at every vertex and the simultaneous \(r\)-direction collision moment sums for \(r=2,3,4\), for every \(n=2,3,4,5\) and three parking parameter vectors in each dimension. All 12 cases passed.

Stable logarithmic arithmetic separately evaluates the moment sums for \(n=100,400,1600,6400\) and \(r=2,3,4\). The numerical ratios to the predicted sharp constants approach one, and the collision-conditioned rank variances divided by \(n^{1/r}\) approach \(1/r\). These are finite cross-checks, not proof of an all-\(n\), fixed-\(r\) limit.

For the mathematical proof for arbitrary positive integer parking vectors and every fixed integer \(r\ge2\), read `RESULT.md`: exact signed-rank optimization and cone sums, a decreasing-ratio saddle estimate with Gaussian local expansion, the finite-population correction and the resulting conditional Gaussian limit. The finite cone census itself was already known through partial-permutohedron work and is expressly credited. Independent validation has not been performed.
