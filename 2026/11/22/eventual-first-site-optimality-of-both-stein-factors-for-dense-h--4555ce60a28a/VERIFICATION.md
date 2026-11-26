---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The rate balance is w b(m)p_m=d(m+1)p_(m+1); telescoping gives the stated size-site formula, and g(0)=0 fixes the increment at site zero. The polynomial product gap b(m)-d(m)>b(0) for m≥1 follows from d(0)=0 and a strictly positive coefficient of positive degree when r≥2. Induction using a_m d(m)=a_(m-1)b(m-1) proves T_m<T_0 for m≥1, while T_m>1/b(m) there. For the signed increment coefficients, the region j<m has strictly negative limiting coefficients, the site j=m has limit 1/b(m)>0, and the entire remaining tail has one sign with total converging to T_(m-1)-T_m. This gives H_m=1/b(m)+max(0,T_(m-1)-T_m)<T_0: if the max term is positive use T_m>1/b(m), and otherwise use strict growth of b. For uniformity choose the split m(1-w)≤1 or >1. In the first regime w^(-m)≤e^2 for w≥1/2 and the factor is O((m+1)/b(m)); in the second, the degree bound and geometric moments give G_(m+1)/p_m=O((1-w)^(-1))=O(m), again giving O((m+1)/b(m)). This vanishes for r≥2, and adjacent size bounds control the increment tail. A finite number of strict noninitial comparisons then yields eventual simultaneous exact maximization at site zero; the singleton and its complement attain it. All arguments include c=1 and fixed nonzero offsets. The recorded 6,156 assertions are finite evidence; the source script was not executed. A separate exact coefficient spot check at (r,c,kappa,w)=(2,1,(0,0),9/10) gives both site-zero factors 1 and the next size and increment factors 19/40 and 3/4; it is not a proof of the uniform limit.

## originality

PASS

DeSalvo supplies the exact general size-site representation, not the eventual optimum or the simultaneous sharp increment theorem. The same-day two-row zero-offset size result is genuine subclass coverage, acknowledged in the frozen record. The supported distinct claim is simultaneous first-site eventual equality for both factors throughout the fixed-parameter degree-r family.

## value

PASS

This answers the dense-regime question for both sharp indicator factors in the stated multirow integer-shape setting and goes beyond limits: it identifies a single exact maximizing site eventually over the whole unbounded state space, with a specified maximizing test event. The exact constants are usable in Stein bounds without optimizing over sites or events in that regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
