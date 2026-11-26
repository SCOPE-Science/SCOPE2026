# Independent mathematical audit

## correctness

PASS

Kabluchko's τ_d(r) is the first point absorption of re₁ for standard variance-t Brownian motion, so r=1 matches, and Eq. (46) supplies positive and negative Mellin moments near zero. This justifies log integrability and differentiation; on any fixed circle |w|=ρ<1, the analytic right side of Eq. (49) gives each coefficient in a neighborhood of s=0. Differentiation gives M_d+log 2+ψ(d/2) on the left and F(w)=w[−2γ−2ψ((1−w)/2)]/(1−w²) on the right. In the digamma series the j-th difference is (1+w)/[(j+1)(2j+1−w)], so F is 2w/(1−w) times the resulting sum. Separate j=0, split the j>=1 factors into poles at 1 and 2j+1 and use ∑_{j>=1}1/[j(j+1)]=1. Coefficients then give 2d−1−S_d as claimed; convergence is absolute locally. For the second difference of M_d the digamma contribution is 2∫₀¹u^(d−1)(1−u)/(1+u) du, at least 4/[d(d+1)(d+2)]; the series correction is at most (2/9)3^(1−d)+(1/2)5^(1−d). At d=3 this upper bound is strictly below the lower bound and decreases by a factor at most 1/3 per step, while the lower bound retains at least half. The low cases follow independently by expanding F: the w, w² and w³ coefficients are 4log 2, π²/2, and 4log 2+(7/2)ζ(3). Subtracting the digamma terms gives the stated C₁ and C₂, both positive by the rational margins in the proof. Δ₁=2log 2>0, and Δ_d increases strictly to 2 since both the digamma increment and the series correction tend to zero. Thus no increment reaches 2. The standard digamma asymptotic and bounding j>=2 by half of 5^(1−d) give both error terms. An independent Taylor and truncated-series diagnostic through small dimensions was consistent with these analytic identities; the supplied verify.py was inspected, not executed.

## originality

PASS

The log-mean identity is an explicit coefficient extraction from Kabluchko's prior Mellin transform; neither the transform nor the formal determination of the moments is independently new. The credited result is the all-integer strict convexity and exact monotone finite-dimensional increment bounds, established by a sign comparison and low-dimensional evaluations, not supplied by the inspected transform statement, exact representations, or high-dimensional limit.

## value

PASS

The logarithmic scale is natural because raw mean absorption time is infinite. The theorem determines the direction and strict increase of the marginal cost of adding a dimension, gives a sharp strict upper bound on that cost at every finite d, and identifies its limit. Those nonasymptotic conclusions have content beyond a moment formula or a high-dimensional Gaussian limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
