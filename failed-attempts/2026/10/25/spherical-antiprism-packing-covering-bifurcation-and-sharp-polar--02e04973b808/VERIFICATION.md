---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a horizontal direction the support of either ring is attained at one vertex or at two consecutive vertices. A nonhorizontal facet normal with nonzero horizontal projection must therefore tie an adjacent pair in one ring with the nearest opposite-ring vertex; at half-step there is exactly one such vertex. Vertical normals give the caps. The triangular plane with unnormalized normal (1,0,s(1-c)/(2h)) has constant s(1+c)/2. The origin is interior since the two rings span three dimensions and their equally weighted mean is zero. For any supporting direction realizing the inradius m, the point mu is in the polytope and at least one unit-normal facet inequality there is active. Cauchy–Schwarz and b_i >= m imply b_i=m and that facet normal equals u. Thus the two, 2n+2 and 2n counts exhaust the minimizers. Squaring the lateral-to-polar ratio gives the unique switch at h²=c/(1+c); differentiation gives the lateral turning point (1-c)/(3-c), strictly below the switch. The shortest same-ring and opposite-ring chords are strictly decreasing and increasing respectively, so their equality gives the packing maximum. Substituting yields the claimed height gap and asymptotics. The uploaded checker is a finite supporting-plane and chord enumeration with floating tolerances; its 2412 is a reported counter, not a universal certificate; code inspected, not executed.

## originality

FAIL

An earlier public Resultary record proves the covering profile, sharp switch, uniqueness and covering optimum in the larger arbitrary-twist family, and at half-step separately derives the identical equal-edge height and the exact coincidence criterion. The remaining displayed contact counts and asymptotic loss are immediate consequences of its facet and height formulas, not an independent new theorem.

## value

FAIL

The two-ring optimization is a worthwhile problem, but the submitted contribution repeats its earlier stronger solution. The new presentation of a facet count and the π/4 loss uses no new obstruction, estimate or case and is a short corollary of that solution; no independently valuable original remainder was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
