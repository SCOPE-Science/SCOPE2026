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

The exact first integral y²/(1+3x²)+[log(1+3x²)-2/(1+3x²)+2]/9 was independently differentiated against dx/dt=(1+3x²)y and dy/dt=-x-x³+3xy², yielding identically zero. U is even and strictly increasing for x>0, so all E>0 levels are compact noncritical ovals. Original-time quadrature uses |dx/dt|=P^(3/2)*sqrt(E-U), and T=4I_0, M_q=I_q/I_0. Under v=U(x), g_q(v)=x^(q-1)*sqrt(P)/(2(1+x²)); near v=0 it is ~v^((q-1)/2)/2, and at infinity ~sqrt(3)x^(q-2)/2. The Abel kernel gives integrable q<2 beta constants, critical q=2: M2~3E, and q>2: M_q~A_E^(q-2)*sqrt(pi E/[2(q-2)]). A_E~exp((9E-2)/2)/sqrt(3); T~4/sqrt(3E); the density is sqrt(3)/(2P^(3/2)). Crucially fixed q precedes E->infinity. I checked the beta normalization at q=0 and the use of physical rather than reparametrized time.

## originality

PASS

The same cubic system is already a known global center, so novelty is restricted to its original-time occupation limit and sharp entire fixed-q moment transition. Comparison with the full defining classification and related Cauchy/log occupation examples reveals no implication of these constants. Best-knowledge PASS with nonexhaustive priority risk.

## value

PASS

A complete original-time occupation measure and its fixed-q moment spectrum for a recognized cubic global center are natural dynamical invariants. The transition at q=2, high-energy period shrinkage despite exponentially increasing amplitude, and distinct asymptotic coefficients supply nontrivial physically interpretable information beyond a center existence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
