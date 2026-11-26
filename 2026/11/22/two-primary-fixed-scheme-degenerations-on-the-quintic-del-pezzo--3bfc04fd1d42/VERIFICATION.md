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

I reconstructed the renormalizations from the marked points: the 4-cycle formula uses the ordering with new first three x,∞,0 (using the inverse cycle convention instead gives the same equalizer), and the double transposition normalizes by z↦x/z. For the 4-cycle in x=uv,y=v the fixed condition first gives v=u/(u−1); clearing the other unit denominator gives P=u(u²−2u+2). In Z[u]/P, u−1 is a unit since P(1)=1; modulo u²−u+1 the polynomial P reduces to 1, so the other eliminated denominator is a unit as well. The open fixed equations force x=2 and y²−2y+2=0; there is no interior characteristic-two point. The only invariant boundary crossing is D13∩D24, represented by u=v=0. Thus the open equalizer computation includes all geometric support and determines the full scheme, finite free of rank 3, with fiber k[u]/u³ at 2. For h, the (1,1) chart gives the claimed product (a,b)F, F=a−2−b. It equals (a,b)∩(F) integrally because F restricts to the nonzero divisor −2 on the section. It is the product, not the intersection of the specialized ideals, that base changes to characteristic two: putting t=a+b gives (at,t²), so t survives and is annihilated by the maximal ideal at the collision. For global support the two swapped crossings of h lie over (0,0) and (∞,∞), where the charts have the equalizer (u−v). The only invariant components are D12=E11, on which a↦a/(a−1) fixes a=0,2 but not infinity, and D34, the strict transform x=1, on which y↦1/y fixes y=±1 and exchanges 0,∞. The y=1 point is the section, and y=−1 lies on the curve (the two points coalesce in characteristic two). The noncollision point with y=−1 lies in the ordinary unblown chart and has ideal x−y² since y is a unit. Elsewhere on the curve the equalizer is likewise the graph, a section of projection to y isomorphic to P1 over Z. These charts therefore cover all fixed support, including infinitesimal structure. The field counts and zeta functions follow from the roots of (u−1)²+1 and from the section adding one rational point only when disjoint. The frozen finite checker was inspected, not used as proof of field-uniform claims.

## originality

PASS

The ambient automorphism and boundary descriptions are prior results. The local embedded algebra for h also occurs in a distinct indexed record for a single transposition; the novelty here is not that isomorphism class in isolation. The supported distinct content is the two specified integral equalizers, including the global double-transposition curve and section and the finite flat four-cycle degeneration. The distinct record does not give those equalizers.

## value

PASS

The two cycle types are natural automorphisms of the split integral moduli surface, and the exact schemes distinguish distinct wild behaviors invisible to fixed-point counts: a finite flat triple point versus a curve with an embedded length-one part. The attached component and colliding section are identified integrally, not just at a selected prime or in a local germ already considered in isolation. This is useful data for constructing wild fixed strata and comparing arithmetic fibers; no claim is made about all twists or quotient singularities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
