---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Standard Brownian ring target Laplace transform plus renewal formula yields F(y)=[cosh(sqrt y)/(1-p+p cosh(sqrt(by)))-1]/y. Independent symbolic series re-expansion verifies exact A1=P1/24, A2=-P2/720; polynomial elimination P2-(5b(6p-1)/2)P1=-(3b^3p-5b+2)/2 reduces to Q(b)=b^3+15b²-16b+4. Q has exactly one physical root b in (0.4,0.45), p=(5b-2)/(3b³) in (0,1); the other root p>1. The cubic coefficient H(b)/(5670b^8) is strictly positive by certified rational interval, with nonzero control Jacobian; implicit function yields y_loc=sqrt(epsilon/(3 C_*))+O(epsilon), a strict local, not global, minimum. Independent SymPy and rational checks corroborate exact proof.

## originality

PASS

Julián-Salgado et al., same reset model and the exact same physical tricritical coordinate, previously reported its approximate location numerically and derivative equations. The added algebraic defining cubic, proof of uniqueness of the physical solution, nondegenerate positive cubic and transverse local-onset coefficient are not given in the read primary text. Best-of-knowledge PASS limited to these exact analytic refinements, not discovery of the tricritical phenomenon.

## value

PASS

The triple vanishing of low-order reset-rate derivatives is a natural criticality threshold for two-site Brownian search. Exact algebraic uniqueness plus a certified positive cubic and nonzero control Jacobian distinguishes genuine tricritical onset from a numerical table, and gives a quantitative local square-root law. The result neither overclaims global optimization nor attributes the earlier discovery of the coordinate to itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
