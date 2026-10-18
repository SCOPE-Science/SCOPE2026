---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For F=(e1,e2/sqrt2,e2/sqrt2), T_F T_F*=I and norm ||T_F||=1; K=diag(1,1/2) invertible and its lower K-frame inequality holds. The family V_c(x1,x2)=(x1,(1/2+c)x2/sqrt2,(1/2-c)x2/sqrt2) obeys T_F V_c=K, and V_c*V_c=diag(1,1/4+c²). Thus every |c|<=sqrt3/2 has ||V_c||=1; the bound ||K||<=||T_F|| ||V|| proves global minimality. Distinct c yield distinct controlled duals; c=0 is reduced by range inclusion and others add synthesis kernel. Exact rational test c=0,1/4,1/2,3/4 independently confirmed equal minimal norm. Source Proposition 3.7 indeed quantifies over identity controls.

## originality

FAIL

Decisive broader published counterexample logically refutes this exact unrestricted uniqueness assertion as a special case, despite the new manuscript targeting another cited proposition and using a different normalized frame. A correct but already covered refutation is not original under the same implication standard.

## value

FAIL

The general misconception is meaningful and the present matrices are correct, but the published 3-vector family already diagnoses exactly the norm-minimizer versus reduced-solution distinction in the same identity-control subcategory. Changing the source proposition and a Parseval rescaling adds no independent mathematical classification, obstruction, or unresolved invariant beyond that covered fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
