# Independent mathematical audit

## correctness

PASS

Averaging over base automorphisms preserves feasibility and cannot increase the spectral norm, giving the two-orbit family with a+db≤1. The symmetric two-by-two block at core eigenvalue lambda has eigenvalues 1−a−b lambda/2 ± sqrt(a²+(b lambda/2)²). Upper modes decrease with lambda, and every positive-core-eigenvalue block has nonnegative trace because lambda≤2d, so the positive eigenvalue of that block dominates its negative modulus. The only extra mode is 1−2a at lambda=0. For nonzero interior a the upper mode at alpha decreases strictly with b, and optimizing at b=(1−a)/d gives the scalar F with F''=c²/[a²+c²(1−a)²]^(3/2)>0. The stated stationary point satisfies the unsquared sign equation and a≤1/2, so the extra mode is dominated there. Strictness gives uniqueness in the two-orbit family only. In terms of s=sqrt(alpha/d), the same solution is gap s²/(2+2s+s²), pendant probability s(1+s)/(2+2s+s²), and core probability (2+s)/[d(2+2s+s²)], using the factorization D=(1−s/2)(2+2s+s²). The K2, balanced bipartite, complete-graph and small-s limits follow; the certificate is analytic, not the recorded finite verifier. Its sampled matrices are symmetric as matrices but may be non-invariant under the graph automorphisms; the script was inspected, not executed.

## originality

FAIL

Two distinct indexed theorems supply the complete nontrivial family. First, the multi-leaf discrete-time theorem 9e788ca7bde4 specializes at r=1 to the exact three formulas in the correctness check and strictly strengthens the conclusion with global holding and pendant-weight rigidity. Second, the same-day price-optimal continuous-time theorem eed5b428788a has an exact reduction here, not just analogous notation: choose base-edge price 2, pendant price 1, budget n. Every feasible stochastic chain has total corresponding expenditure at most n by summing the core row constraints, hence its spectral gap is at most the continuous-time optimum. The orbit-uniform continuous-time optimizer has a+db=1 and gives exactly the same three expressions. Its positive-core-eigenvalue Laplacian blocks have trace at most 2, so the other eigenvalue is at most 2 minus the optimal gap; the remaining radial Laplacian eigenvalue is 2a≤1. Thus the continuous-time bound is attained also for the discrete-time SLEM. Orbit uniqueness descends from continuous-time uniqueness. K2 is the already known P4 path chain. This is mathematical coverage, not an allegation about who found it first; the later catalogue publication date of the multi-leaf theorem is not evidence that it was prior to the frozen text.

## value

FAIL

The formula is intrinsically informative, but the frozen contribution is an exact parameter specialization of the broader leaf theorem, and also follows from the matching price-budget result by an elementary block trace check. The P4 boundary and the displayed asymptotics give no distinct research contribution. No genuinely surviving submitted claim warrants a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
