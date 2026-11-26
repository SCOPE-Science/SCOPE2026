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

At 1<=t<=2 the axial facet is a diamond of area 2(t-1)^2 and the diagonal facet is an octant triangle with three disjoint corners removed; for 2<=t<=3 axial facet area loses four right triangles, and the diagonal facet is a cut-corner triangle with area sqrt(3)(3-t)^2/2. Removing six disjoint caps from the octahedron or eight tetrahedra from the cube gives the two V(t) formulas. Cauchy's area formula pairs antipodal facets, giving the three axial and four diagonal symmetric generators with the specified coefficients and no residual factor of two. I enumerated determinant magnitudes using the alternate diagonal representatives (1,±1,±1); the independent sum is 8a^3+96a²b+192ab²+128b³. The replay python /workspace/reproduce_frozen.py independently factors both derivatives and gives their common t=2 value 108/125. The two displayed bijective rational substitutions give one coefficient sign change each, with opposite signs at the interval endpoints; this proves exactly one critical point in each interval. The denominators have opposite signs before cubing, producing the asserted decrease/increase/decrease. As an independent upper-bound check on [2,3], set s=3-t. The profile is (8-3s^4+3s^6/4)/(1-s³/6)^2; subtract its numerator from nine times the denominator to obtain 1-3s³(1-s)-s^6/2, at least 47/256 on [0,1] since s³(1-s)<=27/256. Hence the value 9 is unique at 1. Monotonicity, P(3/2)=127/16<8, P(2)=207/25>8 and P(3)=8 give the unique global minimum and both level-eight crossings, including no additional crossings strictly after t=2. The diagonal facet vertices for 1<t<2 are the permutations of (1,t-1,0); their centroid is (t/3,t/3,t/3) and central symmetry forces t=3/2, so the strict interval contains nonzonotopes. The independent replay confirms all displayed critical/crossing approximations; root counts are analytical, not inferred by numerical sampling. Frozen checker inspected, not run.

## originality

PASS

Best of current knowledge, the distinct result is the full two-branch classification with globally compared stationary phases and a precise strict sub-eight interval. The first-branch support function and mechanically determined volume numerator, the regular truncated octahedron value, and the endpoint values are credited as covered components. The originality verdict is not for any of those components alone.

## value

PASS

The interpolation joins two canonical solids and crosses a facet-combinatorics change, and the eight benchmark is independently motivated by the sharp zonoid bound. An exact two-regime classification detects a nonregular minimizer and a secondary maximum while isolating all sub-eight members. This is substantially more than tabulating endpoints, recomputing the regular special member, or inferring an unspecified neighborhood from continuity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
