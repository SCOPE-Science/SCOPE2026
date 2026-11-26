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

On the smooth conic the restriction of H is u⁶+λu³v³+v⁶ with six simple zeros, giving transverse coordinates and six A₂ points. Off the base points, the affine critical equations imply x³=y³. If one coordinate vanishes both do, with curve equation sλ²=1 and quadratic 3xy. Otherwise the order-three symmetry takes the point to the diagonal w; the derivative and equation give H=2wG, then w=−λ/2 and s=1/λ²−1/4. For x=w+e+d,y=w+e−d the quadratic part is 3Ue²−9U²d² with U=w²−1≠0, hence nodal. At infinity repeated binary roots force s=−1/4 and y³=1, with transverse Z derivative zero and quadratic at y=1 equal to −9(y−1)²/4−3Z². The three walls therefore exhaust the possible outer singularities; only the first two can coincide, at λ²=−4. Finiteness of the singular locus forces reducedness; a proper factorization would require at least five intersections by Bézout, impossible at unibranch cusps and at most four transverse nodes. The genus and Tjurina counts follow from g_a=10 and local δ=1 and τ=2,1. For the lift, use G+T²=H−cT³=0 in [X:Y:Z:T]; where G≠0 the inverse is T=−sqrt(s)H/G, and over G=H=0 the lifted system is smooth by transversality of dG,dH at T=0. This checks smoothness globally off walls, and gives the stated complete intersection after the linear change of coordinates. Adjunction makes it canonical. The cubic gradient with T=0, Z=0, or TZ≠0 allows a singularity only at λ²=4, s=−1/4, or s=1/λ²−1/4, respectively. The quadratic cover is branched at the zeros of a degree-six section on this smooth cubic, all simple because a multiple zero would make the covering curve singular.

## originality

PASS

Oka–Pho already give the singularity baskets and genera, and the torus lift as a method is not the distinguishing point. The verified surviving result is the wall equations with node locations and the exceptional collision in this symmetric normal form, together with its explicit bielliptic description off the walls. The closest distinct indexed diagonal pencil has a similar node census but is not the same projective family.

## value

PASS

The symmetric torus family is a concrete test of how known singularity baskets occur in parameter space. The exact exhaustive wall geometry distinguishes isolated genus-one and genus-three walls from a rational collision, and the generic involution and its branch data give a usable model of the normalized curves. Recomputing the listed baskets or genera alone would not establish this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
