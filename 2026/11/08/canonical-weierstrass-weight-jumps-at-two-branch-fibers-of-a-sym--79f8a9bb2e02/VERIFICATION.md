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

Adjunction for a smooth (2,2,2,2) complete intersection in P^5 yields K=O_C(2), degree16 and genus17, with 17 canonical quadratic sections (X0²,X1² and 15 mixed monomials). At R0 the five odd-in-w sections w f_a(w²), slopes a=0,±1,±t, have vanishing orders 1,3,5,7,9 via Vandermonde. The remaining 12 even-w sections split into seven even-z and five odd-z terms. Their exact 7×7/5×5 jet determinants contain coprime factors Q(t) and P(t), respectively; the next minors are nonzero at each relevant root. Thus generic and exceptional 17-entry valuation sequences produce weights 23/27. Reciprocal polynomials prove same at R1. Direct exact-rational independent odd-jet determinant evaluations at t=2,3 and both even-jet determinants at t=2,3 matched the specified formulas, with independent polynomial gcd, squarefree, t=0,±1 exclusion, and 17-entry weight sums 23,27,27. These point checks are corroboration; full all-t proof is the formal binomial-series determinant identities and gcds in inspected VERIFY.py plus the geometric local-parameter argument. No square-root branch zero on fiber because forbidden parameters excluded.

## originality

PASS

Hidalgo–Leyton-Álvarez prove a general Weierstrass-weight lower bound, specialized to 21 for (k,n)=(2,5), attaining equality on dense open full moduli. Their inspected full text does not give the 23/27 weights and exact 12-parameter polynomial discriminant on the highly symmetric genus-17 subfamily. Published nearby Humbert-Edge findings concern zeta/Newton polygons over finite fields, not canonical vanishing sequences over complex parameters. Best-of-knowledge the particular jet stratification is distinct, with specialized older curve literature as residual risk.

## value

PASS

A complete canonical vanishing-sequence classification at 32 naturally distinguished ramification points, including an exact 12-marked-parameter exceptional locus, is a natural geometric invariant of a high-genus curve family. It refines generic Weierstrass lower bounds by explicit nontrivial jump discriminants, and separates P versus Q mechanisms while showing the same weight. This is a meaningful natural classification, not an arbitrary tiny parameter table or a general numerical experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
