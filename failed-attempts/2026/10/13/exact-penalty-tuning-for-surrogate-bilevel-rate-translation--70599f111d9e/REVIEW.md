# Independent mathematical audit

## correctness

PASS

The conditional scalar minimization is correct. If p and x are the surrogate iterates, the nonnegative squared penalty gives ||x−p||<=sqrt(2 theta_phi/rho); the surrogate outer gap bounds omega(p)−omega*, and the common Lipschitz constant on a set containing p and x bounds omega(x)−omega(p). Substitution gives the stated U. For S=sqrt(2(b1+b0/rho)), U'=a1−ell b0/(rho^2 S), and when b0>0, U''=ell b0(4b1 rho+3b0)/(rho^4 S^3)>0. With a1>0 the derivative goes from −infinity to a1; the unique stationary point must be the minimum. Squaring its equation is reversible because both sides are positive and yields the stated quartic; the stationary identity ell S=2a1 rho+2a1 b1 rho^2/b0 gives the minimum and cube-root special case. For a1=0<b0 the infimum is a0+ell sqrt(2b1) at infinity; for b0=0<a1 the same infimum is approached only at zero; for both zero the expression is constant, including b1=0. Attribution needs a correction: the matching Proposition 1(iii) and Remark 2 are in arXiv v3, not the cited v1. Application by citation to that proposition is on its coercive, g1-real-valued branch (not the g2-only alternative); the pointwise certificate there does not supply common ell. Correctness concerns the explicitly affine, common-ell scalar problem, not universal applicability to the source algorithms.

## originality

PASS

The exact optimizer/minimum/endpoint formulas were not already stated or established by a stronger mathematical finding in the inspected sources. The underlying bound, its affine rho-dependence, and the suggestion to minimize it are already present in Shtern–Taiwo v3. Only the particular explicit algebraic conclusions are distinct in the comparison; their routine derivation is a value issue, not evidence that a prior document states them.

## value

FAIL

The penalty tradeoff is genuinely motivated, but the frozen contribution starts after the substantive choices have been assumed: a common Lipschitz bound and four affine coefficients. On that scalar expression the quartic is just the first-derivative equation with positive factors cleared and squared, the convexity is an elementary sign calculation, and the endpoint cases follow by dropping a term. No new estimate, applicability criterion for common ell, or nonroutine analysis of actual surrogate certificate dependence is established. Selecting the matching publication version or adding examples would not change the routine nature of this deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
