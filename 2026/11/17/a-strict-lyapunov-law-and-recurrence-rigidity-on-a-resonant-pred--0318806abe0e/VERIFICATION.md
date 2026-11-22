---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For m>1,d>0 the specified a,b,k give exact x_next=x(1-e), y_next=y(1+k e) with e=mx+ay-(m-1), and e_next=e(1-mx+dy). On each strictly positive step -1/k<e<1 and weighted AM-GM makes x^k y strictly decrease unless e=0. I independently simplified the three exact algebraic identities. Strict monotonicity excludes nonfixed recurrent and all positive periodic points. Forward-positive orbits have d/k<H<m, hence bounded; positive limiting Lyapunov value keeps both coordinates away from axes, forces e_n->0 and intersects the equilibrium line in at most two points, and vanishing increments force a single limit. V=0 implies min(x_n,y_n)->0, not coordinatewise convergence. The tangent eigenvalue is 1 and the normal eigenvalue 2-m+(a+d)y; the strict normal contraction interval is exactly max(0,(m-3)/(a+d))<y<(m-1)/(a+d). Local attraction is to the segment, not to an isolated point. No global quadrant invariance or endpoint nonlinear classification is claimed.

## originality

PASS

On inspection of the original Type-2 model, its resonant equilibrium problem is explicitly singular; the strict global monomial Lyapunov principle and positive-orbit convergence are separate nonlinear conclusions. Resultary comparisons concern different maps or weaker period-two results. Best-of-knowledge PASS with documented inaccessible related source.

## value

PASS

A global recurrence rigidity theorem for a natural singular parameter surface of a named predator-prey map fills the gap between local multipliers and all forward-positive dynamics. The strict Lyapunov mechanism, sharp normally contracting subsegment and precise boundary alternative are structural, not a routine eigenvalue calculation or arbitrary numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
