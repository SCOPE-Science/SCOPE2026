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

Itô gives almost-sure growth r·x−v x^TΣx/2 for fixed x; positive-definite Σ has leading minors (2,3,1) and unique optimizer. Four branches satisfy all KKT gradient equalities, inactive inequalities and joins at v=1/3,5/3,5. In dimension 2 the optimal lower-mean share is the clipped monotone affine function of 1/v, so re-entry impossible. Final-branch exponent (−v²+10v+2)/(9v) crosses zero at 5+3√3; v=6 yields (16/27,0,11/27) and growth 13/27 despite all isolated growth negative. Independently symbolic KKT and boundary checks passed.

## originality

PASS

The sharp minimal-dimensional entry-then-exit support phenomenon and explicit positive-definite ecological persistence witness are not inferred from inspected density-dependent ESS or parametric-QP algorithm results; general mean-variance formulation and algorithms fully credited.

## value

PASS

The natural sharp minimal number of habitats for nonnested optimal support under one scalar environmental-variance parameter is a mathematically motivated sensitivity threshold, with an exact KKT-certified positive-definite witness and a distinct stochastic persistence boundary. It is not a random tiny optimization slice; equivalence to known QP is fully acknowledged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
