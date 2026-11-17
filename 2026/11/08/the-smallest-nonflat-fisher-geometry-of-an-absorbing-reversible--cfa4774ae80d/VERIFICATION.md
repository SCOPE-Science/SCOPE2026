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

For weighted path 0-1-2-3, a,1,b, absorb 0 start 1, u=a/(1+a), w=u/(1+b), the complete first-hit law is Bernoulli atom at 1 followed by a geometric time with parameter w on odd later times. The conditional Bernoulli/geometric Fisher tensor is diagonal diag(1/[u(1-u)],(1-u)/[w²(1-w)]), determinant 1/[uw²(1-w)]>0. Coordinates x=2arcsin√u and y=log[(1-√(1-w))/(1+√(1-w))] give dx²+cos²(x/2)dy² and curvature -f/f=1/4. Independently checked the a=b=1 Jacobian pullback equals [[5/12,-1/6],[-1/6,1/6]]. Three-vertex path has ≤1 independent weight ratio; triangle full-law factorizes as independent geometric stopping count and Bernoulli parity, producing a flat 2D product metric. Therefore minimum four vertices is justified.

## originality

PASS

Best-of-knowledge: inspected actual primary statements for possible coverage by equivalence and implication, not just matching titles. The zero-inflated geometric Fisher parameter family plus textbook warped-metric curvature formulas may make the calculation accessible, but they do not assert the graph realization or show that every graph of at most 3 vertices has no curved rank-two full-law metric. Any alleged full-law rank-one assertion in Kimura cannot imply the positive-curvature result.

## value

PASS

A graph-size-minimal, exactly curved full-hitting-time Fisher manifold corrects misleading rank-one intuition while distinguishing full distribution from a fixed-time score. The explicit nonzero K=1/4 and flat rank-two smaller triangle give substantive information-geometric boundary, not a routine reparametrization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
