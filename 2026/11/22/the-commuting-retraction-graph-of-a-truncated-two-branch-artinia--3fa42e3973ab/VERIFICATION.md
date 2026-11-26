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

Assessment of the corrected RESULT.md at /workspace/repairs/4/RESULT.md. The frozen long-branch proof inferred u^j=y^j merely from a leading y coefficient of one; e.g. (y+y²)^2≠y² in k[y]/(y⁴) in odd characteristic. This was a gap in the proof, not a counterexample to the classification. The replacement uses P(x)=f(y), P(y)=cx+g(y), g=y+h with h∈(y²). The relation fg=0 forces f=ts because g is y times a unit. P²(y)=P(y) then gives h(g)=-ct s; substitution by g is a unitriangular automorphism fixing s, so h=-ct s. The proposed maps respect the relations and fix their images, of the stated ranks. For the other tangent cases: zero tangent and idempotence force the radical image into all powers of the radical; full tangent gives an automorphism; in the short case the tangent of the image identifies with the image tangent line because B∩m²=P(m²). Nilpotence then gives generation by P(x), whose square vanishes iff its polynomial part has order at least ceil(N/2), even in characteristic two. Substitution shows that HH′ equality requires t=u and then c=d, and LL′ equality requires h=g and then a=b. In the mixed case equality on x requires h=-ts and equality on y requires a=-c; the two composites are the unital augmentation. Thus H has one distinct partner, graph and clique counts follow, and the ordered total is T+2(2(T−2)+1+q²) for T=2+q²+q^{floor(N/2)+1}. An independent finite check at q=2,N=4 enumerated all ordered generator-image candidates in the maximal ideal, testing defining relations and idempotence; it gave 14 maps, ranks 1:1, 2:8, 4:4, 5:1, and four edges and four isolates on the 12 nontrivial vertices. It does not replace the all-field argument. Frozen verifier and log were inspected but not executed; the verifier checks the ordered total by the edge-count identity rather than independently testing all pairs including the universally commuting endpoints.

## originality

PASS

For the repaired, unchanged claim, the closest prior gives all endomorphisms of exactly this family but explicitly leaves composition laws untreated; the other plausible results classify automorphisms, ideal orbits, or retractions of a different algebra. The classification with its exact commuting criterion survives the proof repair and the bounded prior comparison.

## value

PASS

The repaired result classifies all split algebra projections of a natural truncated local fiber product, and goes beyond listing admissible images: it determines exactly which projections are compatible by composition. The unique mixed partner and onset of isolated short projections at N=4 distinguish genuine structure not visible in total endomorphism counts or in the automorphism group.

The dated certificate retains the supplied scientific assessment, sources and limitations.
