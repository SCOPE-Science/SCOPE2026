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

The support of each coordinate-plane disk is hypot(u_i,u_j); symmetry doubles the sum. For Gaussian coordinates the independent chi radius has mean r_n and second moment n, giving the two spherical moment conversions. Single-edge second moment is 2, disjoint products have mean mu^2, and conditioning on the shared Gaussian coordinate adds Var(f(Z)) for each incident pair, counted twice. Strict increase of f on [0,infinity) gives positive covariance. In a tree the degree excesses are nonnegative integers summing to n-2; their squared sum is minimized by entries 0 or 1, and maximized by concentrating all excess, characterizing the path and star and giving (2). For the path, adjacent Rayleigh summands are one-dependent, and the sum of their covariances with the squared coordinates is mu per edge (Rayleigh third moment 3mu); the joint CLT and radial Taylor expansion therefore give 2A_n-mu B_n, centered equivalently at the exact mean. Its limiting variance is 8-3pi+8c_D, positive from c_D >= pi/16. For the star, conditional strong law plus R/sqrt(n) tending to 1 yields 2f(|Z|) without requiring independence between numerator and denominator; subtraction of the squared mean in (1) yields the variance limit. On z in [s,1], the rationalized integrand for f(s)-f(0) differs from 1/(2z) by integrable errors bounded by O(z+s^2/z^3); the tails give O(1) to the integral. Consequently t is asymptotic to x log(1/x)/sqrt(2pi) with x=s^2, giving the stated inverse and prefactor. Independent quadrature in R^3 used the angular mean at |U_1|=a of sqrt((1-U_2^2)(1-U_3^2)): (1+a^2) E(((1-a^2)/(1+a^2))^2)/pi with E the complete elliptic integral in the parameter convention. Integrating in uniform a on [0,1], multiplying by 3 and subtracting pi/2 gives 0.20884335238503713824951321 at two working precisions, and the path variance 0.24596885831091739060817555.

## originality

PASS

Support-function additivity, wedge counts, and path/star degree extremality are standard or have close geometric antecedents. On evidence available, the combined exact ambient-sphere moments for the coordinate-disk model, family limits and logarithmic lower edge are distinct; in particular the sum of coordinate-plane Rayleigh norms cannot be replaced by the line-segment support kernel. The decision is best of current knowledge, not a claim of historical priority.

## value

PASS

Width variance of a natural curved graph-indexed Minkowski sum is a precise invariant. Its reduction to one incidence count gives a sharp and usable comparison of trees, but this alone would be an elementary consequence of the covariance formula. The different path and star scales and the exact logarithmic correction at the star law's lower endpoint distinguish the disk kernel from the earlier segment analogue and give a more substantive description than the moments alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
