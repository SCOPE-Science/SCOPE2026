---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The source gives a correct two-variable supremum over x perpendicular_I y with no zero pair, and real alpha in [0,1). Set u=x+y, v=x-y; the isosceles constraint N(u)=N(v) makes the change-of-variables exact and yields Omega=(1+alpha)^2*gamma((1-alpha)/(1+alpha))/2. Separate convexity of squared norm expressions over the compact polygonal unit balls reduces gamma to pairs of eight vertices (equal to the sphere maximum). Five dihedral separation orbits reduce to the quadratic candidates F0=1+t^2, F2=(1+(sqrt(2)-1)*t)^2, and F1=1+(2-sqrt(2))*(t+t^2) for t<=1/sqrt(2), then (2-sqrt(2))*(1+t)^2. The exact support inequalities are affine on seven intervals; verifying both endpoints establishes the inequalities through each continuum interval. Exact differences establish the upper envelope at 2-sqrt(2) and 1/sqrt(2). Independently reconstructed symbolic support checks validate all 112 endpoint inequalities and algebraic identities; 384 vertex-pair reflection comparisons and the published L_YJ-prime specialization corroborate the same branches. Continuum validity comes from convexity, endpoint-dominance arguments and exact polynomial signs; finite checks do not replace an infinite proof. At alpha=0 the first plateau value matches, at both alpha transitions formulas agree, and alpha tending to 1 is not included.

## originality

FAIL

Complete prior coverage by a primary 2024 peer-reviewed paper. Let N(s,u)=max(|s|,|u|,(|s|+|u|)/sqrt(2)), r=sqrt(2)-1, and M(s,u)=max(|s|+r|u|,|u|+r|s|). These are linearly isometric: rotate N by -pi/8 and rescale the regular octagonal unit ball to Euclidean circumradius 1. Both gamma_N(t)=sup_{x,y in S} (N(x+t*y)^2+N(x-t*y)^2)/2 and the Filomat unit-sphere L_YJ-prime(1,t,M) are separately convex and attain maxima on pairs of octagonal vertices. Every vertex pair is interchanged by a dihedral reflection of the octagon; hence on such pairs N(t*x-y)=N(x-t*y). This establishes gamma_N(t)=(1+t^2)*L_YJ-prime(1,t,M) for every 0<=t<=1, with t=0 by continuity. Filomat Corollary 2.5(i)-(iii), specialized to lambda=1, mu=t, yields exactly the three gamma_N branches at thresholds t=2-sqrt(2), t=1/sqrt(2). The Yang-Li relation Omega_N(alpha)=(1+alpha)^2/2 * gamma_N((1-alpha)/(1+alpha)) then gives every claimed Omega branch and both alpha transitions. Thus the 2026 finding is a corollary of the 2024 published exact profile, despite the different written objective. The assigned RESULT.md says that the two functionals differ and that the 2024 formula does not imply gamma, but that comparison overlooks the dihedral vertex-pair swapping symmetry after a valid separately convex extreme-point reduction. Failure is based on precise implication from Corollary 2.5, not title similarity, a self-hit, or an absence-of-search argument.

## value

PASS

The isosceles-orthogonality constant Omega_X(alpha) is a motivated quantitative invariant of Banach-space geometry, and the regular octagon is a canonical non-Hilbert polyhedral plane. The exact all-parameter profile, its plateau and two distinct extremal-support transition points provide a meaningful natural benchmark beyond an isolated endpoint. Its geometric information is intrinsically useful, but it is already a mathematical consequence of the 2024 table and therefore cannot count as an original new finding. This value judgment does not rely on correctness, code or nomenclature alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
