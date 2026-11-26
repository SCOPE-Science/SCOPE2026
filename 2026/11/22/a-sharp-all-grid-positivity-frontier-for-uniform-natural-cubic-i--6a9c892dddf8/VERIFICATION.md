---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Independently verified the finite-tail formulas and the strict all-grid certificate. Set θ=arcosh(2), D=sinh(nθ), and F=a sinh((k+1)θ)−b sinh(kθ)>0 for an interior evaluation. For source index v≤j the combined inverse row aG[j,v]+bG[j+1,v] equals (−1)^(j+v) F sinh(vθ)/(sinh(θ)D). On the left tail an interior data index i has coefficient 6(−1)^(j+i)F sinh(iθ)/(sinh(θ)D) because the interior second-difference matrix equals the curvature matrix minus 6I. The endpoint i=0 instead contributes (−1)^j F/D when j>0. Taking the odd-index-distance terms gives the factor cosh(jθ)−1: its step-j-to-j+2 increment is 6 sinh((j+1)θ)/sinh(θ), and its bases are 0 and 1. Reflection gives the right tail. An interior central coefficient has its positive cubic baseline, e.g. (1−t)^3, plus six times the positive combined inverse row at its index. At a left boundary cell the endpoint coefficient is 1−t−bG[1,1]>0 since G[1,1]<2−√3<1/2 and b/(1−t)=t(1+t)<2; the right boundary is reflected. The two-knot case is linear and knots have zero negative mass. Algebraically, for X=r^j,Y=r^k, (1−r²X²Y²)C_a=[(1−X)²(1−r²Y²)−r(1−Y)²(1−X²)]/2, and C_b is the reflection. Independently expanding these expressions and changing basis in exact Q(√3) reproduced all nine listed Bernstein coefficients. Their positivity away from (0,0) for finite X,Y proves N<3c/4, while X,Y→0 and t=1/2 proves sharpness. Constant reproduction gives norm 1+2N and pointwise minimum m−(M−m)N, so the displayed contrast is equivalent and equality gives strict positivity on every finite grid.

## originality

PASS

To the best of current knowledge, the distinct result is the proven strict uniform upper bound over every finite equally spaced natural grid, including endpoint cells, with sharpness along growing grids and the equivalent sharp positive-data contrast. Beatson–Chacko explicitly study the same finite operator (Method E) and its selected-grid norms; those numerical results and the previously known infinite-cardinal constant are not original here. The accessible primary report does not establish the claimed strict inequality uniformly in grid length.

## value

PASS

An exact threshold on ordinary nodal data range is motivated by whether standard natural interpolation can create spurious negative values without using a shape limiter. Uniformity and strictness at every finite length, together with constructive failure above the threshold, are substantive beyond computing a few norm values. This value judgment does not settle priority.

The dated certificate retains the supplied scientific assessment, sources and limitations.
