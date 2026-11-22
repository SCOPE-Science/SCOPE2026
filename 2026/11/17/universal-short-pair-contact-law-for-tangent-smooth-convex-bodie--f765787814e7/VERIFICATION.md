---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For two compact convex bodies touching at exactly one point with positive C3 curvature, close cross-body pairs must approach that contact. In normal-depth and tangent coordinates X_y=√r t-rv/2, Y_y=√r t+rv/2, X_x=-g_-(X_y)-ru and Y_x=g_+(Y_y)+rw, the exact four-dimensional Jacobian is r^{7/2}. The tangential boundary separation divided by r tends to k t² with k=(κ_-+κ_+)/2, giving the compact limit domain (λ+kt²+u+w)²+v²<1. Dominated convergence gives L1 of unnormalized densities and, after normalization, total variation for λ<1. Integrating over q=kt², u,w≥0 gives F_k(λ)=8/(3√k)∫_λ^1(h-λ)^{3/2}√(1-h²)dh; at λ=0 the Beta integral is 4B(5/4,3/2)/(3√k). Dirichlet(1/2,1,1) follows from q^{-1/2} simplex density, and H²~Beta(5/4,3/2); the edge coefficient follows B(5/2,3/2)=π/16. Independent numerical quadrature of F_1(0) and its beta representation agreed to ~3e-11 absolute; not a proof.

## originality

PASS

Area-pair distance convolution and overlap formulas are classical, but same-body or shared-edge polygon settings are not this unique positively curved tangency event. The claimed exponent, conditional total-variation contact marks and gap crossover are not supplied by the compared primary results without a new local scaling argument; inaccessible Sheng 1985 prevents absolute priority certification.

## value

PASS

Short distances between independently area-uniform points in barely touching convex bodies are natural rare events. The noninteger 7/2 exponent, local curvature dependence, complete beta–Dirichlet conditional geometry and sharp O(r) separation crossover form a reusable contact asymptotic, not an arbitrary numeric special case or a generic convolution identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
