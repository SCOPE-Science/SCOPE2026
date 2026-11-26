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

Independently checked the geometry and volume. On any signed coordinate face orthogonal projection is obtained by adding a multiple of its normal within the face's coordinate span. For the positivity test on coordinate i, the worst signs give sum over j≠i on that face of (|x_j|/a_j + a_i|x_i|/a_j²). Adding indices only increases the sum; facets dominate edges, vertices impose nothing, and the second/third inequalities also force normalized l1 norm <1 for the full polytope. In the positive octant use first the two constraints with coefficients (1,1+s,1) and (1,1,1+s). Their polytope is a pyramid with apex U=(1,0,0) and base (0,V,VW,W) at u=0. It has normalized ratio 2/((s+1)(s+2)), since normalized ratio is six times normalized-octant volume. For s≥2 the first constraint is redundant; for s<2 its plane clips exactly U and gives cuts on U0, UV, U(VW), UW. The fractions from U along those edges are respectively (2-s)/2, (2-s)(s+1)/(s+2), (2-s)(s+2)/4, and (2-s)(s+1)/(s+2). Split the base along 0–VW: in each tetrahedron the product of the three corresponding fractions rescales removed volume, so the ratio removed is (2-s)^3/(4(s+2)). This reproduces both branches without assuming the supplied determinant sum. The clipped octant has three quadrilateral external faces and seven nonzero vertices before reflection; the unclipped octant has two triangular external faces and four nonzero vertices. Each external facet lies in its own octant since the supporting coefficient magnitudes are positive. On octant-wall vertices sign differences fill the zero-coordinate directions of the active normals; the active form(s) on the nonzero coordinates span the remaining directions. Thus these reflected nonzero vertices are genuine global vertices, with Euler giving the two edge counts. At s=2 the removed portion vanishes and the unclipped combinatorics apply. The displayed deficit factors have the stated signs, vanish only at s=1, and the branch difference gives left-minus-right third derivative 6/(4·4)=3/8. The supplied exact-rational verify.py was inspected, not run, and checks only 16 shape parameters and rational projection tests.

## originality

PASS

Pass for the stretched family: the regular kernel, its 26/48/24 face vector, and the fraction 1/4 at the single regular aspect ratio have existing coverage. The distinct results are the full metric phase diagram, ratios for other stretches, rigidity of the maximizer relative to those stretches, and the smoothness transition.

## value

PASS

The family holds the combinatorial type of the original octahedron fixed while varying its Euclidean metric. The exact threshold, different kernel face vectors, cubic onset of the volume correction and unique regular maximum describe phenomena not detectable at the single known regular point, and give a useful test family for the all-face kernel notion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
