---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The normalized analytic outer q-th root G has H² norm one since qp=2 and inner multiplication preserves boundary modulus. Writing x=|G(0)|>0, Parseval gives |G'(0)|≤sqrt(1-x²). Schwarz–Pick and the product rule then give the objective (1-rho²+q rho t)/(1+t²)^(q/2) for t=sqrt(x^(-2)-1). The sign of its derivative is the sign of rho-(1-rho²)t-(q-1)rho t². For rho>0 it changes once, at the claimed root in (0,1/sqrt(q-1)]; for rho=0 the unique maximum is at zero. For 0<rho<1 equality requires a disk automorphism for I, a linear polynomial for G, and matched phases in their derivative terms; the displayed factors have exactly those phases, the linear factor is outer because t<1, and the norm is one. The endpoint equalities reduce to the Schwarz lemma and constant G at rho=0, and constant I and the linear G at rho=1. The stationarity polynomial evaluated at 2 rho/q is -rho(q-2)(q-2rho²)/q², so the envelope derivative (q t-2rho)/(1+t²)^(q/2) is positive for rho>0. Implicit analyticity and oddness of t at zero give t=rho+O(rho³), yielding the claimed quadratic expansion; evaluating the envelope derivative at one gives the other expansion. If f(a)=0, I=B_a J gives rho≤|a|, and strict increase forces constant J in equality when a≠0. Its phase parameter is eta=-|a|/a; at a=0 equality means a multiple of z by a unit scalar.

## originality

FAIL

The frozen problem conditions on a different quantity than Brevig–Grepstad–Instanes, but the proper comparison applies their stronger exact fixed-origin first-coefficient frontier to the outer factor (or, for a prescribed zero, to the quotient by its Blaschke factor), not to the original f. Their Theorem 12 and Corollary 13 then give the sharp formula and equality cases by elementary support maximization. Strict increase and the stated endpoint expansions are elementary calculus consequences of that same formula. There is no verified claim of an earlier statement worded with the same parameter; this is verified implication, not a title match.

## value

FAIL

Prescribing a zero is a natural problem, and the record gives a concise, correct direct proof. But the quantified loss and exact extremizers come from the known first-jet frontier by norm-preserving division or inner–outer factorization, phase alignment, and a single scalar optimization. The additional monotonicity and endpoint coefficients are routine calculus of the resulting formula; no independently useful exact result not mechanically implied by the prior frontier survives as stated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
