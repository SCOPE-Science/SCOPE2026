---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Every triangular side proportion p_i is in (0,1/2), and alpha_i=1-p_i is the perimeter fraction of the two sides incident to vertex i. For fractional corner gap M_i=min_j(1-lambda_i(X_j)), the threshold neighborhood has exactly P alpha_i t/N arclength for 0<=t<N; for fixed joint thresholds the disjoint corner neighborhoods give joint survival (1-sum alpha_i t_i/N)^N and independent Exp(alpha_i) limits. The unique full-area inscribed triangle is T; compactness localizes each near-maximal sampled triangle to distinct parent vertices. Barycentric multilinearity yields signed area/A=1-sum u_i+O((sum u_i)^2). A near-corner candidate and a matching maximizing-triple lower bound yield Z_N-sum NM_i=o_P(1). Telescoping the determinant from identity bounds the normalized deficit by 2 sum M_i, including coincident selected corner indices, and exponential marginal tails give uniformly bounded moments of every order, proving fixed positive-real moment convergence. The exact survival for rates r+-d, e^-rt(cosh dt+(r/d)sinh dt), increases strictly with d>0; equal-sum pair averaging and majorization place alpha between (2/3,2/3,2/3) and (1,1/2,1/2), with correct strict/equality/degenerate cases. Finally mu=sum t_i, variance=sum t_i^2, sum alpha_i=2 imply elementary symmetric e2=q and e3=q/2, so the cubic recovers the side proportions. These are analytic arguments, not inferences from finite trials.

## originality

PASS

The final claim concerns a maximum among all sample triples on a fixed triangle boundary, whose N-scaled loss is a hypoexponential sum with three corner rates, plus sharp whole-distribution bounds and two-moment shape inversion. Reading the closest mathematical source statements distinguishes this from (i) circle/ellipse U-max Weibull laws, (ii) full sampled-convex-hull missed area of order N^-2, and (iii) the area law of a single boundary-random triple. The exact same candidate has a Resultary cross-post dated 2026-11-08, which is not an independent precursor. No inspected earlier result entails this final joint claim. This is best-of-knowledge, not historical proof.

## value

PASS

Maximal 3-point area from a boundary sample is a canonical extremal geometric statistic, different from the area of its entire random hull. Its N^-1 corner-gap law is qualitatively unlike circular U-max Weibull extrema and planar polygonal hull-area N^-2 asymptotics. A sharp simultaneous stochastic comparison over all triangle shapes and recovery of the three unordered side proportions from only two limit moments are natural, exact and independently usable classifications. The six-extreme-point reduction gives a practical finite-sample computational link; it is elementary supporting structure, not the sole claimed value. The result makes no unsupported claim about finite-sample estimation stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
