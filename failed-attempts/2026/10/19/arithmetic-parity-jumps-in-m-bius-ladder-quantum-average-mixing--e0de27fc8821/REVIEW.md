# Independent mathematical audit

## correctness

PASS

For N=2n the characters give λ_k=2cos(πk/n)+(−1)^k. Cesàro averaging kills unequal energies, so Fourier orthogonality yields μ_q=N^(−1) times the number of ordered equal-energy pairs with k+l=q modulo N, using invariance of each energy class under changing sign. Diagonal pairs cover every even q. The opposite-parity equation is cos(πo/n)−cos(πe/n)=1. For a=2cos(πo/n), both a and a−2 are cyclotomic integers with conjugates between −2 and 2. Every conjugate of a−1 lies in [−1,1]. If nonzero its integral norm forces every factor to have modulus one, so a−1=±1; the zero case gives a=1. The a=2 case would make the odd index zero. For the remaining values, folding the indices into [0,n] gives o=n/2, e=n at n≡2 mod 4, or o=n/3, e=2n/3 at n≡3 mod 6. Restoring signs and adding modulo N gives respectively {n/2,3n/2} and {n/3,n,5n/3}, both exclusively odd. The congruences are disjoint, n=3 is included, and the complementary Fourier modes span the kernel. A separate exact test (exact_support_check.py) compared energy classes modulo Φ_(2n) and the resulting index sums for all 118 orders n=3,…,120. This is finite corroboration; the norm and Fourier arguments prove the uniform result. The uploaded verify.py was inspected, not executed.

## originality

FAIL

The exact rank and kernel are mechanically implied by the earlier same-graph, all-order spectral classification in Resultary cb5ec968b69e and the standard average-mixing projector formula. The earlier statement names both colliding Fourier index pairs, not merely the congruence classes or multiplicities. Consequently taking the signed sums of those pairs yields the entire claimed odd support without any new classification. The frozen proof gives a useful elementary alternative to the earlier arithmetic proof, but does not establish distinct theorem-level originality for the stated rank and kernel. This is a concrete implication finding, not an access-based failure or an assertion that the prior finding explicitly printed the rank.

## value

FAIL

The unweighted ladder and its mixing nullspace are natural, and the formula is a useful way to summarize the known spectrum. In the frozen scope, however, the exact arithmetic obstruction was already resolved, and the full proposed invariant is obtained by the standard projector identity plus two explicit modular sums from the earlier labeled classes. It is not an independently unresolved exact invariant under the stated value criterion. The simpler argument for an existing collision lemma does not establish a distinct valuable remainder of the frozen rank theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
