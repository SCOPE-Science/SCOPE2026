---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

One iteration satisfies x_new-y_new=2max(-x,0)+2a max(y,0)>=0. The invariant negative cone y<=x<=0 has affine matrix [-1,a;1,a] and both eigenvalues outside [-1,1], with affine fixed point outside cone; hence strong divergence there. Positive cone x>=y>=0 has expanding invertible matrix [1,a;1,-a] with unique fixed P=(2+1/a,1/a). In fourth quadrant x>=0>=y the map collapses to (t,t), t=x+ay-1; the remaining positive diagonal excursions return via t->(1+2a-a²)t-(a+2). If a>=2 returns descend into negative cone; if 1<=a<2 the sole fixed return is q=(a+2)/(a(2-a)), below q enters negative cone and above q diverges, with q forming the cycle. Backward preimages of special orbits are countably many affine lines/points owing to the rank-one branch; hence planar null. I independently checked the eigenvalue polynomial signs at ±1 and two-step return algebra, including a=1 and 2 endpoints; numerical simulations alone would be insufficient.

## originality

PASS

The full primary 2026 Tikjha four-partition paper studies the same general map and low cycles, but its highlighted degenerate reduction is c=a and does NOT imply all bounded orbits on c=-a. The latter has different collapsing quadrant. Search comparisons of Resultary related four-quadrant inverse-valence and c=a dynamics did not find this global all-orbit c=-a result. Priority is best of knowledge, residual unindexed literature remains.

## value

PASS

A complete global classification and measure-zero exception on a natural singular parameter slice is a substantial new qualitative constraint: it excludes all bounded aperiodic attractors and identifies exact finite survivors, not just local eigenvalue stability. It distinguishes mechanisms at the opposite singular lines of the same noninvertible planar family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
