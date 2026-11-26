# Independent mathematical audit

## correctness

PASS

For the specified independent exchangeable snapshots, E[DAD]=qA+(p−q)diag(A). Applying this to A=HXH in the two projector modes gives the stated nonnegative transfer matrix. Symmetrization preserves expected trace at every step, and a nondecaying Perron positive-semidefinite mode decomposes into deterministic rank-one inputs, proving the all-start criterion in both irreducible and reducible cases. With B_1=[p+(n−1)q]/n and B_2=[(n−1)p+q]/n, one has LB_1+aB_2=p+qG and B_1B_2−(n−1)(p−q)²/n²=pq; this gives the stated determinant factor pη²KF(η). Strict objective descent gives stability near zero. The first root is in (0,2) for q>0 and equals 2 at q=0. Any stable larger step would give a positive-definite expected quadratic contraction certificate, which by the quadratic dependence on η is also strict at every smaller positive step; this rules out later reentry. For fixed p, ∂_qF<0 up to 2, proving strict threshold decrease. Integer convexity of B(B−1) at fixed E[B]=np forces support on the adjacent sizes for equality, including the single-size integer endpoint, and exchangeability fixes the law. The descent ceiling comes from E[DHD]=(p−q)I+qH; F evaluated there has sign q(p−q), with equality only at the two feasible endpoints. Independently substituting n=4,c=p=1/2 gives 12/(5+sqrt(10)) for size two and 8/(4+sqrt(6)) for Bernoulli. At p=1/n the optimal boundary is 2; inserting q=p² and taking c up to 1 gives the stated ordered gain limit.

## originality

PASS

Credit is for passing from Bernoulli to the exact exchangeable-law criterion and uniquely optimizing its upper endpoint at fixed expected batch size. It is not for the Bernoulli formula, use of covariance lifting, pair-inclusion matrices or uniform fixed-size sampling themselves. Neither the inspected Bernoulli theorem nor the indexed four-coordinate comparison supplies that classification and optimization.

## value

PASS

Many sampling laws have the same expected work. The sharp criterion reduces their comparison to a pair-inclusion moment and identifies a unique optimal distribution even for noninteger expected work. The strict gain over Bernoulli and exact distinction from universal one-step descent make this a useful benchmark for synchronous sampling, not merely a new way to compute a sufficient bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
