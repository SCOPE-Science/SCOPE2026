---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Every base has either r handle or r-1 handle plus one of t tail elements. The Bernoulli K tail count has p=tr/(d+tr), d=s-r+1. Total covariance is orthogonal sum of uniform-subset handle projector, tail one-hot projector, and rank-one p(1-p)vv^T on v=(-1_s/s,1_t/t). This gives stated positive lambda_handle,lambda_tail,lambda_bridge and a 1-dimensional kernel. Explicit positive ratios prove bridge strictly smaller than both, and difference of handle/tail equals ((r-1)(d(t-2)-(r-2)))/(s(s-1)), giving crossover. Direct substitution yields three proportional scalings. Independently enumerated all bases and exact rational covariance for parameter tuples (3,2,2),(4,2,2),(5,4,3),(6,2,4),(6,6,2), verifying eigenvectors and eigenvalues.

## originality

PASS

Best-of-knowledge: a complete Euclidean uniform-vertex covariance operator for panhandle bases, including strict bridge minimum, exact handle/tail crossing and three-scale anisotropy, is distinct from inspected Ehrhart/volume and generic correlation bounds.

## value

PASS

The uniform vertex covariance is a natural inertia/anisotropy invariant of a standard matroid polytope. An exact spectrum with crossovers and quadratic condition growth informs probabilistic base-sampling and geometry, not merely rebranding Ehrhart coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
