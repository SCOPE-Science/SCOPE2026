---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The motion-invariant unoriented line law has normal-angle and offset density dphi dp and mass P on lines meeting a convex polygon by Cauchy. Nonadjacent compact edges have positive separation; for t below all adjacent vertex sin(interior-angle)*minimum incident side length, a short chord meets exactly two incident edges. At a vertex of interior angle theta=pi−alpha, line offset h, incidence cosines a,b, chord length d=h sin(theta)/(ab). Integrating admissible offsets over the normal sector gives measure t q(alpha), with q(alpha)=(1−alpha cot(alpha))/2. Thus exactly F_K(t)=(t/P)sum q(alpha_i) for 0≤t<t0(K), not just an asymptotic. Differentiate q twice: q''(alpha)=(sin(alpha)−alpha cos(alpha))/sin^3(alpha)>1/3 since auxiliary g=3(sin−a cos)−sin³ has g(0)=0 and g'=3 sin(a)[a−sin(a)cos(a)]>0. Strong convexity with mean exterior turn 2pi/m gives excess ≥(1/6)sum(alpha_i−2pi/m)^2, equality precisely equiangular. For m divisible by 4, alternating exterior turns 2pi/m±m^-2 and unit edge lengths form a centrally symmetric strictly convex closed polygon, with defect/variance→1/6, showing global sharpness. Independent angular integrals and curvature checks confirm normalizations only.

## originality

PASS

The initial Crofton chord density is already implicit in the general polygon chord-distribution formulas of Harutyunyan–Ohanyan and García-Pelayo and is excluded from novelty. The retained result is the exact optimal side-count-independent quadratic stability of that density, with all equality and near-sharpness classes. A superficially identical 1/6 coefficient appears in previously published *boundary arclength endpoint pair* distance/shortcut results, but those measure a different sampling law and depend on f(alpha)=alpha/sin(alpha) rather than q(alpha)=(1−alpha cot(alpha))/2; neither theorem implies the Crofton q-stability as stated. Gates 1987 full text unavailable; historical priority remains qualified.

## value

PASS

The initial slope of the motion-invariant line-chord distribution is a directly measurable inverse-geometric statistic. The sharp uniform angular stability inequality converts that single measurement into a rigorous lower signal controlling total squared exterior-angle variation, in every convex polygon size. Distinct sharpness shapes and equality class make this a motivated quantitative inverse theorem, not the known chord formula repackaged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
