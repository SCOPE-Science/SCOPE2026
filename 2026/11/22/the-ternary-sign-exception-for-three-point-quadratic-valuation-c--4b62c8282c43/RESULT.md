# The ternary sign exception for three-point quadratic valuation cumulants

## Finding

Let \(p\) be an odd prime, let \(c\) be a positive integer divisible by \(p\), and let \(s\ge1\) be an integer. Put \(Q_c(n)=n(n+1)+c\), and let \(X_i(n)=\nu_p(Q_c(n+i p^s))\) for \(i=0,1,2\). In the limiting law for uniformly sampled \(0\le n<N\), or equivalently for Haar input in \(\mathbb Z_p\), the three variables have common mean \(\mu=2/(p-1)\). Their connected third cumulant is
\[
\kappa_{p,s}=\mathbb E[(X_0-\mu)(X_1-\mu)(X_2-\mu)]
=\frac2{(p-1)^3}\left[p^2-2p+3-\frac{3s(p^2-1)+p^2-2p-5}{p^s}\right].
\]
It is **negative exactly at \((p,s)=(3,1)\)**, when it equals \(-1/3\); it is strictly positive otherwise. It increases strictly with \(s\) for each fixed \(p\) and tends to \(2(p^2-2p+3)/(p-1)^3\). The mixed moments and cumulant of the finite uniform integer samples converge to these values.

In contrast, the two-polynomial root-collision formula [1] gives the same strictly positive covariance for each of the three distinct pairs:
\[
\operatorname{Cov}(X_i,X_j)=\frac{2(p+1)(1-p^{-s})-4}{(p-1)^2}.
\]
The third cumulant thus detects a sign reversal at the first ternary scale that is not visible in the signs of the pairwise covariances. The exact valuation law is used below as a consequence of the pairwise collision laws in this particular setting, not as a separate originality claim.

## Assumptions and scope

The shifts are exactly \(0,p^s,2p^s\). For each integer input, \(Q_c(n)>0\) because \(n(n+1)\ge0\); hence all the valuations are finite. When using Haar points, disregard the finite set where an argument vanishes. No claim is made for arbitrary shift triples, for \(p=2\), or for constants outside the stated class.

## Proof

**Pairwise input and the common clipped variable.** The reduction of \(Q_c\) is \(x(x+1)\), with simple roots at \(0,-1\). A root lifts uniquely to a \(p\)-adic root \(a\), and the valuation on its residue class is \(\nu_p(x-a)\), since the other factor is a unit. Each corresponding root pair for two shifted polynomials is separated at depth exactly \(s\): the difference is \(\pm p^s\) or \(\pm2p^s\). Other root pairs have different residues. With two matches of depth \(s\), the two-polynomial collision law [1] yields the marginal tail \(\Pr(X_i\ge j)=2p^{-j}\) for \(j\ge1\), and, for each pair, equality when clipped at \(s\) and disjointness of the events \(X_i>s\) and \(X_j>s\). These support facts also follow directly from equality of the depth-\(s\) balls and disjointness of the corresponding depth-\((s+1)\) balls.

Thus \(Y=\min(X_i,s)\) is the same for all three coordinates. Set \(U_i=(X_i-s)_+\). Then \(U_iU_j=0\) for \(i\ne j\) and \(YU_i=sU_i\). In particular, the pairwise support and single-coordinate tails **determine** the trivariate law here: the diagonal at \(0\) has mass \((p-2)/p\); at \(1\le j<s\) it has mass \(2(p-1)/p^{j+1}\); each permutation of \((j,s,s)\), \(j>s\), has mass \(2(p-1)/p^{j+1}\); and the remaining mass at \((s,s,s)\) is \(2p^{-s}-3(2p^{-(s+1)})=2(p-3)/p^{s+1}\). There are no other cells. At \(p=3\), the last diagonal cell vanishes. These are cylinder probabilities and therefore natural densities. After clipping at any \(k\ge1\), each cell depends only on \(n\bmod p^k\), so multiplying its clipped probability by \(p^k\) gives the exact residue census.

**Cumulant calculation.** The tail sums give \(\mu=2/(p-1)\) and \(e=\mathbb E U_i=2/(p^s(p-1))\). From the disjoint excess terms,
\[
\begin{aligned}
\mathbb E[X_iX_j]&=\mathbb E[Y^2]+2se,\\
\mathbb E[X_0X_1X_2]&=\mathbb E[Y^3]+3s^2e,\\
\mathbb E[Y^d]&=2\sum_{m=1}^s\frac{m^d-(m-1)^d}{p^m}.
\end{aligned}
\]
For the second raw mixed moment the resulting sum is \(2(p+1)(1-p^{-s})/(p-1)^2\). For the third, the infinite sum of \((3m^2-3m+1)p^{-m}\) is \((p^2+4p+1)/(p-1)^3\). In subtracting the tail after \(s\), translate \(m=s+j\); the summand polynomial becomes \((3j^2-3j+1)+3s(2j-1)+3s^2\). The last term is canceled by \(3s^2e\) after restoring the factor of two. The third raw mixed moment is therefore
\[
\frac{2}{(p-1)^3}\left[p^2+4p+1-\frac{3s(p^2-1)+p^2+4p+1}{p^s}\right].
\]
Subtract three times \(\mu\) times the raw pair moment and add \(2\mu^3\) to obtain \(\kappa_{p,s}\). Subtracting \(\mu^2\) from the raw pair moment gives the stated covariance; its numerator is at least \(2(p+1)(1-1/p)-4>0\) for \(p\ge3\).

**Sign and dependence on scale.** At \(s=1\) the cumulant is \(2[p(p-1)(p-5)+8]/[p(p-1)^3]\), negative at \(p=3\) and positive at every prime \(p\ge5\). Its successive difference is
\[
\kappa_{p,s+1}-\kappa_{p,s}=\frac{2[3s(p^2-1)+p^2-5p-8]}{p^{s+1}(p-1)^2}.
\]
The bracket is at least \(4p^2-5p-11\), which is positive for \(p\ge3\). Since \(\kappa_{3,2}=2/9\), there are no other negative cases or zero cases. The limit follows because \(sp^{-s}\to0\).

**Integer averages.** For \(0\le n<N\) the valuations are bounded by \(L=O_{p,c,s}(\log(N+2))\), and the empirical proportion with \(X_i\ge j\) is at most \(2p^{-j}+2/N\), by the two root classes modulo \(p^j\). Summing the third-power differences over levels bounds \(\mathbb E_N[X_i^3\mathbf 1_{X_i>J}]\) by \(O_p((J+1)^3p^{-J})+O_{p,c,s}((L+1)^3/N)\). This bound accounts for the endpoint term \(J^3\Pr_N(X_i>J)\) as well. The same geometric tail bound without the error applies to Haar measure. On the region where the maximum coordinate exceeds \(J\), any degree-three or lower nonconstant coordinate monomial is at most the cube of that maximum, itself bounded there by \(\sum_i X_i^3\mathbf 1_{X_i>J}\). For fixed clipping depth, empirical moment convergence follows from periodic residues. Taking first \(N\to\infty\) and then \(J\to\infty\) proves convergence of all mixed moments used in the cumulant, including the means.

## Verification

`verify_triple.py` uses only Python 3 and checks the exact clipped law, including both regimes \(k\le s\) and \(k>s\), against direct integer polynomial evaluations. The recorded check covers 400 parameter-and-depth histograms and 1,396,368 index triples. This verifies finite instances of the input law, not the infinite cumulant formula or its sign proof, which follow from the calculations above.

## Relationship to other work and limitations

The bivariate collision theorem [1] yields the pairwise covariance and, because the common clipped value and disjoint excesses follow from the pairwise supports, also entails the auxiliary trivariate valuation law here. This special implication does not hold for arbitrary joint distributions. The two Resultary records share a date, which does not establish temporal order. The distinct conclusion considered here is the evaluation of the connected third cumulant with its unique ternary negative case and monotonicity in the lag scale. One-coordinate valuation trees for odd-prime quadratics [2] and factor-product valuation trees [3] provide related context. The comparison does not certify historical priority or exclude unindexed computations or relevant multivariate-local-zeta results.

## References

1. *A root-collision law for joint polynomial valuations and a quadratic covariance trichotomy*, Resultary, 2026-11-22, Finding and Proof §2, [record](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-root-collision-law-for-joint-polynomial-valuations-and-a-quadr--f6b288710442).
2. W. Boultinghouse, E. Hammett, S. Hu, O. Kozhushkina, R. Snyder, J. Trulen, *The \(p\)-Adic Valuation Trees for Quadratic Polynomials for Odd Primes*, [arXiv:2309.16637](https://arxiv.org/abs/2309.16637), Theorem 1.1.
3. D. Snyder, *Products of \(p\)-Adic Valuation Trees*, [arXiv:2308.11718](https://arxiv.org/abs/2308.11718), §6; *The PUMP Journal of Undergraduate Research* 7 (2024), 299–322.
