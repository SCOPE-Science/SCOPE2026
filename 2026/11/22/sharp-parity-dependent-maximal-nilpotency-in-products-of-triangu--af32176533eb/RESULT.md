# Sharp parity-dependent maximal nilpotency in products of triangular radicals

## Finding
Let \(J_n(q)\) be the radical of the algebra of upper triangular \(n\times n\) matrices over a finite field \(\mathbb F_q\). Independently sample uniformly \(A,B\in J_n(q)\), let \(C=AB\), and let \(\nu(C)\) be the least positive integer \(r\) for which \(C^r=0\) (in particular, \(\nu(0)=1\)).

For every prime power \(q\) and every \(n\ge3\), the maximum possible index is \(\lceil n/2\rceil\). Define
\[
s=(1-q^{-1})^2,\qquad f=1-s,\qquad \eta=1-\frac{q^2}{(2q-1)^2}.
\]
For odd \(n=2N+1\), \(N\ge1\), its exact probability is
\[
P_{2N+1}(q)=s^N.
\]
For even \(n=2N+2\), \(N\ge1\), its exact probability is
\[
P_{2N+2}(q)=2s^N-s^{2N}+(1-q^{-1})f^2\left(\sum_{d=1}^{N-1}(N-d)s^{N+d-1}+Ns^{N-1}\eta\right).
\]
Hence the exact number of ordered pairs attaining the maximum is \(q^{n(n-1)}P_n(q)\), an integer. For fixed \(q\), with
\[
C_q=(1-q^{-1})f(s+f\eta)>0,
\]
we have \(P_{2N+2}(q)\sim C_q N s^{N-1}\) and \(P_{2N+2}(q)/P_{2N+1}(q)\sim (C_q/s)N\). In particular, at \(q=2\) this ratio is asymptotic to \(N\). The parity factor is a property of two factors sampled from the nilpotent radical, not of a single uniform nilpotent matrix.

## Assumptions and scope
The matrices are labeled in the standard ordered basis, sampled independently and uniformly from \(J_n(q)\), including zero. All field orders are prime powers and all indices are positive integers. The case \(n=2\) is trivial, since every product is zero, and is deliberately excluded from the formulas. All asymptotics hold with \(q\) fixed as the dimension grows. No conditioning on the product is imposed.

## Proof
Because \(A,B\in J_n(q)\), their product lies in \(J_n(q)^2\). Therefore \(C^r\in J_n(q)^{2r}\) and \(C^{\lceil n/2\rceil}=0\). Choosing all first-superdiagonal entries of both factors nonzero produces a product attaining that upper bound.

Put \(a_i=A_{i,i+1}\), \(b_i=B_{i,i+1}\) and \(t_i=C_{i,i+2}=a_i b_{i+1}\). The \(t_i\), indexed by \(1\le i\le n-2\), are mutually independent. Each has nonzero probability \(s\), since the pairs of scalar coordinates used by different \(i\) are disjoint. Further put
\[
u_i=C_{i,i+3}=a_i B_{i+1,i+3}+A_{i,i+2}b_{i+2}.
\]
Entries on higher superdiagonals cannot contribute to the top possible nonzero power, because every factor of \(C\) shifts the column index by at least two.

If \(n=2N+1\), the only possibly nonzero entry of \(C^N\) is \((1,n)\), equal to \(\prod_{j=1}^N t_{2j-1}\). Independence proves the odd formula.

If \(n=2N+2\), the only possible nonzero entries of \(C^N\) are \((1,n-1)\), \((2,n)\), and \((1,n)\). The first two are
\[
U=\prod_{j=1}^N t_{2j-1},\qquad V=\prod_{j=1}^N t_{2j}.
\]
The last is the unique sum over paths with precisely one jump of length three:
\[
W=\sum_{j=1}^N\left(\prod_{h<j}t_{2h-1}\right)u_{2j-1}\left(\prod_{h>j}t_{2h}\right).
\]
By independence, \(\Pr(U\ne0\text{ or }V\ne0)=2s^N-s^{2N}\). It remains to calculate \(\Pr(U=V=0,W\ne0)\).

On \(U=V=0\), let \(L\) be the first zero among \(t_1,t_3,\ldots,t_{2N-1}\), and let \(R\) be the last zero among \(t_2,t_4,\ldots,t_{2N}\), with these positions numbered \(1,\ldots,N\). Their joint probability is
\[
\Pr(L=\ell,R=r)=f^2 s^{\ell-1+N-r}.
\]
Conditioned on all first-superdiagonal coordinates, \(W\) is a linear form in independent uniform second-superdiagonal coordinates of \(A\) and \(B\). Its value is uniform over \(\mathbb F_q\) if the linear form is nonzero, and is identically zero otherwise.

If \(R>L\), every coefficient vanishes. If \(R<L\), some coefficient is necessarily nonzero: select a position strictly after \(R\) and no later than \(L\), using a surviving odd or even first-superdiagonal product as needed. If \(R=L\), the only potentially surviving summand has index \(L\); its two coefficients are \(a_{2L-1}\) and \(b_{2L+1}\), multiplied by nonzero factors. Conditioned on \(t_{2L-1}=t_{2L}=0\), each of these two scalar coefficients is zero with probability \(q/(2q-1)\), and the two events are independent. Therefore the probability of a nonzero linear form in the diagonal case is exactly \(\eta\).

Summing \(r<\ell\) (with \(d=\ell-r\)) gives \(f^2\sum_{d=1}^{N-1}(N-d)s^{N+d-1}\). Summing \(r=\ell\) gives \(Nf^2s^{N-1}\eta\). Multiplication by the nonzero probability \(1-q^{-1}\) of a uniform field element establishes the even formula.

Finally,
\[
\sum_{d=1}^{N-1}(N-d)s^d=\frac{Ns}{1-s}+O_q(1).
\]
The first term \(2s^N-s^{2N}\) is lower order than \(Ns^{N-1}\). Substitution yields \(C_q=(1-q^{-1})f(s+f\eta)\), and division by \(P_{2N+1}(q)=s^N\) proves the parity-ratio limit. This completes the argument.

## Verification
The attached standalone `verify.py` recomputes the rational formula and independently enumerates the first two relevant matrix superdiagonals, including the exact top-power entry, in four small configurations. A separate enumeration of first-superdiagonal configurations computes the rank of the remaining linear form without enumerating second-superdiagonal entries. Both independent approaches agree with the formula at all tested parameters, including \(P_4(2)=19/32\), \(P_4(3)=200/243\), \(P_6(2)=111/512\), \(P_6(3)=10112/19683\), and \(P_8(2)=575/8192\). Run `python3 verify.py` without third-party packages; expected output is in `verification_output.txt`. Exhaustive tests at finite sizes do not prove the all-size formula; that follows from the combinatorial argument above.

## Relationship to prior work
Kambites and Steinberg (2005, Sections 3–4) analyze structural decompositions of triangular-matrix semigroups, the source setting for the nilpotent radical studied here, but not the two-factor highest-nilpotency probability. Fuchs and Kirillov (2022, Sections 1, 3 and Appendix) compute Jordan-type counts for a **single** uniformly sampled strictly upper triangular matrix, a different distribution. The published result *Maximal nilpotency index in products of random upper triangular matrices* (2026) studies factors drawn from the **full** upper triangular semigroup, conditioned that their product is nilpotent, and tests the different extremal event \(\nu(AB)=n\); its own assumptions explicitly exclude already-nilpotent factors. Neither of those statements determines the new probability for two factors both in \(J_n(q)\), where the maximum drops to \(\lceil n/2\rceil\). Bachman, Baeth and Gossell (2014) study factorizations in the nonsingular triangular semigroup over domains, which excludes our nilpotent factors. We do not claim newness of the filtration inclusion \(J_n(q)^aJ_n(q)^b\subseteq J_n(q)^{a+b}\) or of the known uniform single-matrix Jordan counts.

## Limitations
The result determines only the maximal possible nilpotency-index probability, not the entire Jordan-type distribution or lower-index probabilities. It is restricted to two independent uniformly sampled factors in the strict triangular radical over a finite field. Published priority beyond the sources compared remains open; in particular, an undiscovered factorization-weighted enumeration could imply the formula. No independent mathematical audit has been performed.

## References
1. M. Kambites and B. Steinberg, *Wreath product decompositions for triangular matrix semigroups*, arXiv:math/0512024v1 (1 December 2005), Sections 3–4. https://arxiv.org/pdf/math/0512024
2. D. Fuchs and A. Kirillov, *Jordan types of triangular matrices over a finite field*, arXiv:2204.00066v1 (31 March 2022), Sections 1, 3 and Appendix. https://arxiv.org/pdf/2204.00066
3. *Maximal nilpotency index in products of random upper triangular matrices*, published published-finding corpus mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-maximal-nilpotency-index-in-products-of-random-upper-triangular--3038b4056c47
4. D. Bachman, N. R. Baeth and J. Gossell, *Factorizations of upper triangular matrices*, Linear Algebra and its Applications 450 (2014), 138–157. https://doi.org/10.1016/j.laa.2014.02.038
