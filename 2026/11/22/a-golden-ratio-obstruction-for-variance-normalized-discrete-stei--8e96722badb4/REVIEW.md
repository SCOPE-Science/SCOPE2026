# Independent mathematical audit

## correctness

PASS

Take g_A(0)=0 (the operator does not see this value). Multiplying the Stein equation by p_j telescopes by detailed balance. For each j the cut {0,...,j} realizes the total positive mass F(j)G(j+1) of the signed numerator, so the supremum is exact. The ratios of consecutive masses in the constructed laws are 1/q followed by 2^{-N}, giving the stated full support, log-concavity and finite moments. In the geometric core, F_N(j)/p_{N,j}≤(1−q)^{-1}; beyond it G_N(j+1)/p_{N,j}=ε_N/(1−ε_N). The middle cut has F_N(j)/p_{N,j}→(1−q)^{-1} and G_N(j+1)→1, giving a matching lower bound at each fixed q. For K_N=N−X_N the negative contribution to the raw second moment before normalization is ε_N(1+ε_N)/(1−ε_N)^3, and the nonnegative part converges by geometric domination. Hence σ_N→√q/(1−q). The two normalized branches cross uniquely at √q=1−q, contributing φ and only a lower bound on C_*. Independent exact spot checks agree: at (q,N)=(1/2,4), wΓ=658/481 and Var=64956226/52056225; at (1/3,3), wΓ=372/307 and Var=3312282/4618201. Replay by taking core weights a_j=q^(N−j), Z=Σa_j+ε/(1−ε), and max of S_j(Z−S_j)/(Za_j) with S_j=Σ_{i≤j}a_i and the tail supremum ε/(1−ε); for moments sum the core and add the right-tail k and k² series ε/(1−ε)^2 and ε(1+ε)/(1−ε)^3 at j=N+k. The archived checker was inspected, not executed; it evaluates rather than independently identity-checks the raw moments, and finite checks are not a limit proof. Its tail supremum initialization is valid even though the supremum need not be attained.

## originality

PASS

The exact indicator envelope is established prior art. The surviving originality is the explicit full-support moving-edge family, its optimized normalized curve, and the resulting φ obstruction to the corrected universal conjecture. Neither the general envelope nor the inspected affine optimizations already supply this quantitative obstruction.

## value

PASS

The result constrains the constant in a specific published open bound and explains a nondegenerate regime missed by the vanishing-variance example. The optimized cutoff is meaningful within the family, not an arbitrary exact numerical test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
