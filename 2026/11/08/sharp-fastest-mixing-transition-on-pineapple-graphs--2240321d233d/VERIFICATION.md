---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Convex group averaging over S_a×S_r reduces global SLEM minimization to p,q,s with hub budget ap+rq≤1. Full three-group quotient Laplacian has positive roots alpha_± of z²−[(a+1)p+(r+1)q]z+(a+r+1)pq, while leaf and core transverse eigenvalues are 1−q and 1−p−as. Increasing p at fixed q increases the positive quotient gap. At saturation, the exact G_(N/H)(q)=−Nr[q−(2a+1)/H]² forces alpha_-≤N/H. When r≤a, q=(2a+1)/H,p=(2r+1)/H,s=(1−p)/a attain SLEM (4ar−1)/H; for r≥a the leaf bottleneck q=1/(a+r), combined with G_u(q)<0 for q>u, forces SLEM 1−1/(a+r). Equality yields unique invariant hub-edge pair, not all non-invariant optimizers. Independent symbolic identities checked, direct full eigenspectra agreed in 100 pairs a,r=2..11. Finite tests do not prove all integers.

## originality

PASS

Best-of-knowledge PASS: earlier Boyd et al. give the SDP and symmetry framework, not the evaluated all-integer r≥2 pineapple transition; the single-leaf clique theorem is r=1. Arbitrary leaf clusters on transitive corona cores form a different graph family. Explicit discriminant-square and leaf bottleneck give a new sharp r=a transition beyond the star benchmark.

## value

PASS

The graph is a natural clique with single-hub pendant load, and its precise critical leaf count answers whether internal clique edges genuinely accelerate globally fastest uniform-stationary mixing. Exact all-size SLEM and invariant optimizer classification are mathematical spectral-design data that cannot be read from generic SDP formulations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
