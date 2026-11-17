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

The Gaussian core determinant is a nonzero polynomial, hence a.s. invertible. A regular nonzero isotropic point of any indefinite symmetric quadratic form has local |t|^(-p) divergence for p>=1. For arbitrary 1<=k<n, conditioning on k-1 eigenvector-near Gaussian columns preserves both signs in the Schur residual with positive probability; Tonelli gives divergence. For k=n-1, rank-one hyperplane identity and regular spherical coarea show t^-1 tail, finite moments exactly for p<1, and two-level beta law. Independent near-full matrix identities and arcsine computations corroborate.

## originality

PASS

The previously known deterministic instability of signed Nyström approximation and spherical-quadratic density methods do not establish the all-sketch (1<=k<n) unconditional Gaussian infinite-moment result. The conditional indefinite Schur-residual argument plus near-full spherical inverse law is a distinct mathematically useful statement, subject to possible unindexed precedence.

## value

PASS

For all indefinite nonsingular real symmetric inputs, changing Gaussian sketch dimension cannot repair nonintegrable unmodified Nyström error. This gives a natural exact algorithmic risk boundary, a sharp near-full heavy-tail coefficient and practical mathematical justification for stabilized-core methods, while deliberately excluding finite-precision promises.

The dated certificate retains the supplied scientific assessment, sources and limitations.
