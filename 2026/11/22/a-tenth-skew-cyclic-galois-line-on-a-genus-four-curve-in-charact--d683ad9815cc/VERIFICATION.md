---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The affine chart Y=1 has t=Z/Y, X/Y=t^2, w=W/Y, and w^3=-(t^6+1). The six simple branch zeros give geometric irreducibility. The complete intersection is smooth: the quadric gradient is nonzero off its vertex (which is not on C); if W is nonzero the cubic gradient has nonzero W component, and if W=0 then X,Y,Z are nonzero and the quadric gradient has nonzero Z component whereas the cubic gradient has zero Z component. Adjunction gives the canonical embedding and genus four. On the proposed center Q=-2Z^2 and F=W^3, so it is disjoint. Independently, the projection ratio on the chart is f=t(t+1)/(1-t), of degree two on the base t-line, with the other root t'=(t+1)/(t-1). The characteristic-five identity (t+1)^6+(t-1)^6=2(t^6+1) lifts this involution as (t,w)->(t',3w/(t-1)^2); applying it twice multiplies w by 9/4=1 modulo five. It commutes with w->omega*w, so the cyclic order-six group fixes f and exhausts its function-field degree 3*2. This recovers the stated matrix action and distinguishes geometric Galoisness from arithmetic descent. The prior nine can be checked in the same chart: t->-t over t^2; t->a/t over t+a/t for a^6=1, with lift w->cw/t^2 where c in {a,-a} has c^3=1; and the two diagonal order-six actions preserving X/W or Y/W. All nine centers remain disjoint, distinct from one another, and distinct from the new center (which neither lies in Z=0 nor in W=0 and has X,Y not identically zero). The frozen script and its exact certificates were inspected, not executed.

## originality

PASS

The known nine centers are expressly prior. The claimed contribution is only an explicit geometric counterexample to extending the characteristic-zero nine-line upper bound to this reduction, not a complete characteristic-five classification. The strongest located exact line classification is characteristic zero; the same-curve maximality and quotient descriptions do not themselves give the skew projection or its sixth-order deck action. The identical indexed record is not independent coverage. No earlier positively covering statement or implication was established in the inspected material.

## value

PASS

A concrete smooth canonical genus-four failure of a sharp characteristic-zero bound is a natural boundary example. The line and cyclic degree-six projection are explicitly verifiable; the higher count is not obtained by merely reducing the known nine. The result explains the failure through a new branch involution in characteristic five and can serve as an exact test for any positive-characteristic classification. Its value is the counterexample, not a full line census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
