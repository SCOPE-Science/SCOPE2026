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

Conditional on coverage by j sensors the number of timely reports is Binomial(j,p), giving the stated f_j. Write m_j for the length with multiplicity exactly j. Counting all sensor arclength yields m_1+2m_2+3m_3=3ell and the objective C P=3ell f_1+a m_2+b m_3, where a=f_2-2f_1 and b=f_3-3f_1. If the union fills the circle up to null sets, 3ell<=C forces m_2=m_3=0. Otherwise an uncovered point cuts the circle into a line at which none of the footprints wraps. Order the equal-length intervals by starts. Any double or triple coverage belongs to the middle interval, because its endpoints lie between the outside endpoints of the other two. Thus m_2+m_3<=ell, and disjoint, two coincident plus one disjoint, and all coincident attain all three vertices. The linear maximization over that triangle is therefore exact even though not all interior points need be attained. The coefficients satisfy a=p^2(2theta-1), b-a=p^2((4-3p)theta-(2-p)). For 0<p<1 the latter vanishes at theta_c strictly between 1/2 and 1; at 1/2 b=-p^3/2. The maximizing triangle faces are respectively the disjoint vertex, the m_3=0 edge, the double-only vertex, the m_2+m_3=ell edge, and the triple vertex as theta increases through the two ties. Since the equality conditions refer only to feasible footprints, this gives the stated iff assertions; m_3=ell implies all three arcs coincide up to endpoints. Half-length successive shifts also attain the double-only vertex with three distinct positions. With two receivers there is just one overlap coefficient and no intermediate phase. For the stated example p=4/5, theta=5/8, ell/C=1/4 the three exact vertex values are 0.225, 0.265 and 0.233. The uploaded endpoint-sorting checker was inspected but not run; the analytic comparison covers the sparse boundary 3ell=C and the full parameter domain. Correlated signals or real source and propagation models are outside scope.

## originality

PASS

Best-of-knowledge pass for the exact global three-arc phase diagram and complete tie conditions. Overlap algebra, co-location and confirmation thresholds are known; the inspected closest results do not provide the sharp three-footprint multiplicity restriction or the intermediate all-placement optimum for this objective.

## value

PASS

The strictly optimal double-only phase is qualitatively different from both no overlap and complete co-location, and disappears with only two receivers. The exact maximum and all placement tie criteria give a useful baseline beyond a comparison of a few hand-picked layouts; distinct instruments can achieve the intermediate optimum without co-location. It is a bounded idealized design classification, not an earthquake-station deployment recommendation or an actual false-alarm optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
