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

Differentiating the local cubic with prescribed endpoint curvatures gives the stated A,B weights, and derivative matching gives the tridiagonal curvature recurrence. Reflecting the secants across each end node makes their backward differences odd there; convolution with the even Green kernel G_k=(−r)^|k|/(2√3), r=2−√3, gives zero endpoint curvature. The finite restriction is the unique natural-spline solution by diagonal dominance. For the whole-line derivative row the coefficient of D_k is δ_{k0}+A(G_k−G_{k+1})+B(G_{k−1}−G_k). The central weight is positive since A−B≥−1, and the noncentral weights have geometric tails: their polynomial factors are (1+r)A−(1+1/r)B and (1+1/r)A−(1+r)B. The former changes from positive to negative at u_+, the latter from negative to positive at u_−, by their quadratic roots; summing the absolute tails gives √3−3(√3−1)u² on the left, 6u(1−u) in the middle, and the reflected left expression on the right. This is at most √3, including both endpoints. Affine reproduction applied to the midpoint of the minimum and maximum secants gives the monotonicity threshold (√3+1)/(√3−1)=2+√3, including equality. Independently, on n=2m cells with secants 1,R, set w_j=(−1)^(j+1)S″(j)/(6(R−1)). Then −w_(j−1)+4w_j−w_(j+1)=1 and w_0=w_n=0. Solving gives w_j=[1−(r^j+r^(n−j))/(1+r^n)]/2, hence S′(0)=1−(R−1)w_1. This gives the stated continuant formula via a_m=(1+√3)(r^(−m)−r^(m+1))/2 and w_1=a_(m−1)/(a_m−a_(m−1)). As n→∞, w_1→(1−r)/2, so for every R above the critical contrast a finite member fails monotonicity; putting R=−1 in the same linear recurrence gives the signed-data norm limit √3. Neither sharpness argument requires attainment by a single finite grid.

## originality

PASS

The inspected literature supplies local Hermite monotonicity tests, modified derivative rules and standard cardinal-spline tools. The nearest Resultary record establishes a sharp bound for four knots. None of the inspected sources implies the claimed sharp arbitrary-length natural-spline secant-to-derivative envelope with a compatible finite endpoint witness.

## value

PASS

It answers when the standard natural cubic fit preserves shape without changing the interpolant, a natural practical question about increasing data. The exact derivative amplification also applies to signed disturbances of secants. The sharpness mechanism identifies an endpoint failure for a simple family, explaining why a guarantee based on small fixed grids can overestimate the safe contrast.

The dated certificate retains the supplied scientific assessment, sources and limitations.
