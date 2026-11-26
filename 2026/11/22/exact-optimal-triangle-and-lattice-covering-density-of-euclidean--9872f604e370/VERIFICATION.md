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

Use consistently oriented signed area, affine separately in the three vertices, to express any triple in the hull of the two disks as a convex combination of pure disk triples. For a base in one disk whose line is at distance d from its center, the chord length is at most 2sqrt(r²−d²); the opposite disk contributes height at most 2a|n_x|+r+d, with n the chord normal. Equality at a>0 needs a horizontal normal, a full exterior chord and the opposite axial extreme point. Maximizing F(d)=sqrt(r²−d²)(2a+r+d) gives the unique interior root of r²−2d²−(2a+r)d=0. Substituting d=r/2 already strictly exceeds the best single-disk area when a>0. The two pure maximizing triples are disjoint as geometric vertex sets; a nontrivial convex mixture at a vertex would require two distinct maximizing pure triples sharing the other two vertices. This rules out extra flat-edge maxima. The hexagon conv(T,−T) has levels 0 and ±h and half-width u−(u−w)|y|/h, with u=a+r, w=a+rc, h=rs. Neighboring staggered lattice rows have summed half-width u+w on each intervening height, exactly the spacing between alternating centers; the hexagons tile. The determinant is 2h(u+w), and the Bambah–Rogers theorem as stated by Kallus (pp. 2–3) confirms the upper bound for origin-symmetric planar convex domains and the precise covering-det convention. Substitution of the stadium area gives the density. Envelope differentiation yields η′=2s(π−2−2c)/(π+4t)²>0, because 0<c≤1/2; c→0 at infinity and c=1/2 at the disk endpoint give the asserted limits and inverse uniqueness. The disk has a continuum of equilateral optimizers, not two. The frozen checker and verification notes were inspected but not executed; random witnesses cannot certify either extremum or lattice optimality.

## originality

PASS

The general covering-triangle theorem, its hexagonal lattice mechanism and the disk case are prior. The supported distinct part is the unrestricted exact stadium triangle optimization and two-maximizer rigidity, which evaluate the previously general covering relation on this family and give its strictly monotone density profile. The inspected close geometric records concern a different polygon, body or objective.

## value

PASS

The stadium is a natural continuous family from a disk toward a long nearly tiling shape. The sharp unrestricted triangle solution and rigidity give an exact optimal lattice-covering benchmark for the entire family, with an attainable lattice, strict aspect-ratio ordering, and sharp limiting densities. This evaluates a natural optimization invariant, beyond restating the covering correspondence, without implying a result for nonlattice coverings or classification of all optimal lattices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
