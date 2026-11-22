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

For H=S+hJ, det H=ab(1−c²)+h² and tr(H^T H)=a²+b²+2ab c²+2h². The two positive singular values obey sum sqrt((a+b)²+4h²), difference sqrt((a−b)²+4ab c²), producing exactly the displayed norm when d>0. Sym(H^-1)=H^-T S H^-1 gives positive definite if c<1; at c=1,h≠0 its rank-one kernel violates the injective-map paramonotone criterion. For c=1,h=0 graph inverse of (a+b)uu^T has domain Ru and affine u-perp fibers; direct pairing proves paramonotonicity. Near aligned cancellation det=ab sin²θ+t², numerator→a+b; R=I−(I+H)^−1 is analytic, first differential q[[0,bθ−t],[bθ+t,0]], norm q(b|θ|+|t|), with O((|θ|+|t|)²) uniform local remainder. Independent four-parameter samples of exact matrix singular norms passed; finite checks only corroborate universal algebra.

## originality

PASS

Best-of-knowledge O PASS with concrete primary statements compared against the full claim and retained residual priority risks; inaccessible abstracts are not treated as conclusive NOT_COVERING. 

## value

PASS

Nonparamonotone summands producing a paramonotone parallel sum, and crossing to an unbounded multivalued relation while its resolvent remains sharply Lipschitz, form a natural model for maximal-monotone operator splitting and conditioning. The two-parameter quadratic blow-up versus linear resolvent regularity is more than the qualitative kernel criterion, though derived in a deliberately tractable 2×2 class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
