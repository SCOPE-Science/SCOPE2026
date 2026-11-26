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

Steiner centering subtracts the length times the squared midpoint offset from each transverse chord's second moment and preserves the centroid. For a triangle the chord-length tent of projected width w has peak 2A/w and cubic integral 2A³/w², including the limiting one-sided tent when projections tie. Equilateral covariance is I₂/8 at circumradius one (the covariance of a uniform triangle centered at zero is one twelfth the sum of the outer products of its three vertices), so only the width term A³/(6w²) varies. Width attains the diameter exactly for the three side-parallel axes. The peak 3/2 and symmetric projected endpoints give the asserted rhombus and a first loss I(T)/8. For the second step I independently reconstructed the branch formula: set t=tan θ, z=bt/a, r=a²/b². In the unnormalized projection the middle interval [0,az] has constant chord length L=2b(1+t²)/(1+z), and its midpoint varies linearly from 0 to p=bz(1−rz)/(1+z). The outer segment [az,a] has length decreasing linearly from L to zero and midpoint moving from p to q=−brz. Integrating gives 2aL/(1+t²)² times [zp²/3+(1−z)(p²/4+pq/6+q²/12)]. Inserting r=4/3, and r=3/4 after exchanging diagonals, gives exactly the two rational profiles in the record; continuity covers z=0,1. Differentiation gives the asserted quintic with opposite sign for the short-branch loss derivative; Q′≥244z²−96z+80>0 on [0,1] and Q(0)=−44<0<Q(1)=113. For the other branch I recomputed the degree-12 Bernstein coefficients of the comparison polynomial using the binomial conversion in line 96. With common denominator 27720 their numerators in order are 13804560,17255700,17519460,15879150,12810336,8578640,3837540,226170,967120,11464236,39900420,97835430,200803680; each is positive and the minimum is 359/44. The short branch at 1/2 therefore beats the whole long branch; its unique optimum is interior. Reflection yields two and only two unoriented axes per first choice. An independently implemented geometric fiber quadrature gives second loss 0.013159943950027, angle about 24.2245534° from the short diagonal and total fraction 0.165522118304365, consistent with the exact formulas. The quadrature is corroboration, not the all-angle proof.

## originality

PASS

The chord identity, monotonicity, and general symmetrization tools are prior. The supported distinct claim is the full rhombus branch comparison and resulting exact second-axis classification and total loss for the equilateral greedy procedure. The indexed rectangle law is a distinct record, not an equivalent classification.

## value

PASS

The equilateral triangle is a canonical isotropic initial shape, and its exact greedy update leaves the triangle class. The result gives a sharp benchmark for repeated Steiner symmetrization based on loss of area inertia. The symmetry-breaking second optimum, quantified through a strict global comparison, cannot be read from either diagonal symmetry or an orientation average.

The dated certificate retains the supplied scientific assessment, sources and limitations.
