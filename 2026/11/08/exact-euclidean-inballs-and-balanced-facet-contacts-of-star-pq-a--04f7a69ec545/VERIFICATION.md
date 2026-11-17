---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The original conv of 3m+1 ordered star incidence pairs is exactly the positive leaf cone with sum_i max(u_i,v_i)<=1, because each leaf pair decomposes into three vertex contributions. Its 2m coordinate and 2^m upper inequalities are all facet-defining. Projecting normals into the true two-block sum-zero affine tangent space gives coordinate norm a=sqrt(m/(m+1)) and upper norm sqrt((m+2s(m-s))/(m+1)). Permutations and block-swap average any maximizing ball to uniform leaves t; balancing the two sharp facet distances gives r=1/(ma+b), t=ar. The lower bounds plus every balanced upper inequality force each leaf variable to t, proving uniqueness, including m=1. Numerical unrestricted-center LP checks independently reproduced m=1..9.

## originality

PASS

Existing PQ adjacency-polytope papers focus on volume and Ehrhart h* geometry, while the earlier symmetric-edge star and cosmological star inball results concern different convex hulls and metric realizations. The later same-star PQ Löwner-ellipsoid record studies an enclosing rather than inscribed ellipsoid. A matching direct source is the assigned Resultary record itself. Complete exact inward inradius, unique incenter and facet-contact classes are best-of-knowledge novel.

## value

PASS

The unique inball in the canonical ordered-incidence star family, the exact weighted projected-normal computation, and balanced-parity contact count are natural complete metric invariants, with all dimensions treated and a nontrivial contrast between 2m+2^m facets and the contacting subset. The invariant is motivated independently of any computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
