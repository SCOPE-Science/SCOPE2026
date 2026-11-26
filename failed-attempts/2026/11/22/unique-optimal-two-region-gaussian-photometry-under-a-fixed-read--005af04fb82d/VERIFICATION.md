---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The independent Poisson means are F P_i+b A_i and the rank-two Fisher determinant is the square of P_1 A_2-P_2 A_1 divided by the product of the means. At zero flux this gives the stated contrast squared divided by b^2 x(1-x). At fixed area, subtracting the density on the circular boundary from the integrand proves strict radial rearrangement, with equality only for the centered disk or its outer-annulus counterpart when optimizing absolute contrast. h_c is positive by strict concavity. Differentiating its normalized square gives the stated N_c. The bracket in N_c'' has one interior zero, so N_c' decreases then increases, has positive endpoint values, and is negative somewhere; N_c therefore has one interior sign change, located below 1/2 by its midpoint sign. The corrected score expansion at small c follows by expanding h_c through its cubic term and differentiating locally near 1/2; convergence there follows uniformly by the interpolation-error bound. At large c, the rescaled objective is bounded by min(sqrt(2y),sqrt(2/y)) for x<=1/2, proving compactness of maximizers away from zero and infinity, and the locally uniform limit has one positive maximizer. Read CHECK.py and frozen verification notes; no uploaded code run. The private replay `python /workspace/branches/review_recomputation.py` solves the independent centroid equation at c=2, yielding x*=0.346194657007580329935381 and b^2 det=0.177214945627438059623455, and confirms the illustrative limiting radius. The record is mathematically correct for the claimed local Fisher limit, not finite flux.

## originality

FAIL

The distinct earlier Resultary record 8fb3895d60c4 already solves the identical scalar optimization, not merely a similarly named design or a problem with a shared root. In its notation J_L(u)=L/(u(L-u))*[1-exp(-u)-(u/L)(1-exp(-L))]^2. With L equal to the photometry c and u=Lx, one has Q_c(x)=L J_L(u) exactly. Its proof classifies the unique optimum, its location below half, and its large-L law. The small-L coefficient is a direct expansion of its explicit optimality equation. Strict Gaussian rearrangement transfers this pre-existing optimizer to the unordered disk/annulus geometry. This is established overlap, independent of any uncertainty about external quantization literature.

## value

FAIL

The two-count photometry constraint is natural and the result may be useful as an application note, but it resolves no distinct substantial mathematical gap: the exact classifications of cutoffs and the limiting scale transfer from an earlier identical dimensionless problem. The remaining disk/annulus identification is a fixed-area rearrangement and the small-field coefficient is a first Taylor correction of the known centroid equation. The numerical sample is the previous L=2 optimum rescaled. No independently valuable mathematical remainder in this frozen scope justifies a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
