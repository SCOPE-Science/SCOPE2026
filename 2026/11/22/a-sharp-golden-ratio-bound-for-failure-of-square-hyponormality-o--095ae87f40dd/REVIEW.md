# Independent mathematical audit

## correctness

PASS

A two-step shift has disjoint outgoing supports for different origins, so its commutator is diagonal-minus-rank-one on each two-step child set, with nonnegative uncoupled root entries. Write s=sum |b_j|² and X_j=|d_{j,1}|². The one-step block at the fork gives sum |b_j|²/X_j≤1, with b_j=0 when X_j=0. Monotone ray weights make the fork's grandchild block and later ray blocks positive semidefinite. For the stem block entering the fork, Cauchy–Schwarz gives ||S²e_u||²=sum |b_j|²X_j≥s², dominating the squared incoming two-step stem weight; the preceding stem junction follows from |a|²≤s and stem monotonicity. Thus a root fork has zero defect, and when there is a parent only the first-ray-vertex block can be negative. It is bounded below by diag(X_j²)-sbb*. Normalizing the quotients |b_j|²/X_j to a probability measure, with total mass μ≤1 and mean ρ, the affine majorant for x/(x²+δ) implies s sum |b_j|²/(X_j²+δ)≤μ²[2ρ/σ−(ρ/σ)²]≤1. The factorization is confirmed by coefficient matching: 2σ=1+2α, 2σδ=α², δ+σ²=2α+α². With masses q=(1−σ)/(1−α) at α and 1−q at 1, both inequalities are equalities; constant ray weights sqrt(X_j) and stem weights sqrt(σ) are admissible at norm one. The kernel vector b_j/(X_j²+δ) belongs to l² even for countably many rays since δ>0. Scaling changes the commutator by the fourth power of the norm. Replay square_order_bound() in /workspace/branches/independent_replay.py checks the scalar coefficients and the two-dimensional exact sharpness determinants; the countable operator proof does not rely on finite checks.

## originality

PASS

The root/non-root qualitative distinction and local tests are prior, as are positive-weight examples with nonhyponormal squares. The supported distinct result is the exact best normalized negative-part norm, with attainment on every specified non-root fork including countably infinite valence. Neither the retrieved sufficient and necessary positivity tests nor the older explicit examples carry out this extremization. No matching prior additive bound for ordered positive operators was established in the bounded additional comparison.

## value

PASS

The smallest branching geometry where squaring can break hyponormality is a motivated setting for quantifying failure, not just finding an example. The best bound and two-level positive-weight attainment show exactly how large an error a normalized square can incur even with arbitrarily many rays. The scalar argument is also informative beyond this setup: for 0≤A≤B≤I and any x with <x,Ax>>0, the rank-one compression R_x=(Ax)(Ax)*/<x,Ax> obeys R_x≤A and R_x x=Ax. Writing R_x=ξξ* with ξ=B^(1/2)η, ||η||≤1, the same affine majorant by functional calculus bounds ||ξ||²<ξ,(B²+δI)^(-1)ξ> by one. Thus the mechanism controls the broader order defect too; this ancillary observation is not a separate priority claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
