# Poisson cycle lengths and exponential periodic mass for products of uniform finite retractions

## Finding

Let \(F_n\) and \(G_n\) be independent and uniform among all idempotent functions on \([n]\), and let \(T_n=F_n\circ G_n\). Every common fixed point is a fixed point of \(T_n\). Write \(C_{n,r}\) for the number of length-\(r\) cycles of \(T_n\) other than those common fixed points, and \(S_n=\sum_{r\geq1}rC_{n,r}\). With natural logarithms, the random point measure \(\Xi_n=\sum_{r\geq1}C_{n,r}\delta_{r/\log n}\) converges in law in the vague topology on \((0,\infty)\) to a Poisson random measure with intensity \(e^{-2t}\,dt/t\). In particular, for every \(x>0\),
\[
\lim_{n\to\infty}\Pr\left(\frac{\max\{r:C_{n,r}>0\}}{\log n}\leq x\right)
=\exp\left(-\int_x^\infty\frac{e^{-2t}}{t}\,dt\right),
\]
where the maximum is zero if no such cycle exists. Also \(S_n/\log n\) converges in law to the rate-two exponential distribution. For every fixed \(s\geq1\), the vector \((C_{n,1},\ldots,C_{n,s})\) converges in law to independent Poisson variables with means \(1,1/2,\ldots,1/s\).

For the exact conditional law of mixed factorial moments, put \(K=|\operatorname{Fix}(F_n)|\), \(L=|\operatorname{Fix}(G_n)|\), \(h=|\operatorname{Fix}(F_n)\cap\operatorname{Fix}(G_n)|\), and \(a=K-h\), \(b=L-h\). For a finitely supported collection of nonnegative integers \(q_r\), put \(m=\sum_{r\geq1}rq_r\). Then
\[
\mathbb E\left[\prod_{r\geq1}(C_{n,r})_{q_r}\;\middle|\;K,L,h\right]
=\frac{(a)_m(b)_m}{(KL)^m}\prod_{r\geq1}r^{-q_r}.
\]
Here \((v)_m=v(v-1)\cdots(v-m+1)\) is the falling factorial, with \((v)_0=1\) and \((v)_m=0\) for an integer \(0\leq v<m\).

## Assumptions and scope

An idempotent map satisfies \(f\circ f=f\), and its image equals its fixed set. Conditional on a specified nonempty fixed set, the remaining vertices independently choose their images uniformly in that set. The uniform sampling is over all labelled idempotent functions, not over the possible ranks. Composition means \(T_n(x)=F_n(G_n(x))\). The finite identity applies for \(n\geq1\), every feasible \((K,L,h)\) and the stated factorial-moment orders, including when an exclusive root set is empty. The limits are through all integers \(n\to\infty\); the logarithmic scaling is used only for \(n\geq2\). All cycle limits exclude the common fixed points.

## Proof

**1. Alternating cycles.** Fix the two fixed sets \(R_F,R_G\). Write \(A=R_F\setminus R_G\), \(B=R_G\setminus R_F\), and \(H=R_F\cap R_G\). The image of \(T_n\) lies in \(R_F\); all vertices of \(H\) are fixed. A noncommon cyclic vertex lies in \(A\) and must be carried by \(G_n\) into \(B\), since an intermediate vertex in \(H\) leads to a common fixed point. Along a cycle the intermediate vertices are distinct: two equal intermediate vertices would give equal successors on the cycle. The same argument applies across distinct cycles. Conversely an alternating cycle through distinct vertices in each of \(A,B\), using prescribed \(G_n\)-edges out of \(A\) and \(F_n\)-edges out of \(B\), gives a noncommon cycle of \(T_n\). This includes length-one cycles. The choices for all these edges are independent, with probabilities \(1/L\) and \(1/K\), respectively. For labeled cycle slots of the prescribed lengths there are \((a)_m(b)_m\) choices of the two ordered vertex tuples; divide by the \(r\) rotations in each length-\(r\) slot. The probability for all specified edges is \((KL)^{-m}\). This proves the exact factorial moments for specified root sets and hence for their sizes and overlap alone.

**2. Root sizes and overlap.** The weight of fixed-set size \(k\) is \(w_n(k)=\binom nk k^{n-k}\), for \(1\leq k\leq n\). For \(1\leq k<n\),
\[
\frac{w_n(k+1)}{w_n(k)}=\frac{n-k}{k(k+1)}\left(1+\frac1k\right)^{n-k-1}.
\]
The ratio is decreasing: both the prefactor and the base decrease, and the nonnegative exponent also decreases. For fixed \(c>0\), at integers \(k=c n/\log n+O(1)\), its logarithm is \((1/c-1)\log n+O(\log\log n)\), by expanding \(\log(1+1/k)\) and the prefactor. Thus for any fixed \(0<\varepsilon<1\), ratios at and below the rounded lower threshold \((1-\varepsilon)n/\log n\) are at least \(n^\delta\), and ratios starting one step before the rounded upper threshold \((1+\varepsilon)n/\log n\) and above are at most \(n^{-\delta}\), with some \(\delta>0\) for sufficiently large \(n\). Each outer tail is bounded by a geometric sum times the weight of its adjacent interior term and is therefore negligible relative to the total weight. Hence \(K\log n/n\) and \(L\log n/n\) converge in probability to one.

Given \(K,L\), the fixed sets are independent uniform subsets; their overlap is hypergeometric with mean \(KL/n\) and variance at most that mean. Since \(KL/n\) is of order \(n/(\log n)^2\) with probability tending to one, conditional Chebyshev implies \(h/(KL/n)\to1\) in probability. For \(q_n=ab/(KL)=(1-h/K)(1-h/L)\), these estimates yield
\[
\min(a,b)\sim_{\Pr} n/\log n,\qquad -\log(q_n)\log n\ \xrightarrow{\Pr}\ 2.
\]
Here \(X_n\sim_{\Pr} Y_n\) means \(X_n/Y_n\to1\) in probability, and the logarithm of \(q_n\) is used only on the event \(a,b>0\), of probability tending to one. Indeed each of \(h/K,h/L\), after multiplication by \(\log n\), converges to one in probability, and \(-\log(1-u)=u+O(u^2)\) near zero.

**3. Poisson spectrum.** The first factorial moment gives
\[
\mathbb E[C_{n,r}\mid K,L,h]\leq q_n^r/r.
\]
For \(m=O(\log n)\), on the event that \(a,b\) are of order \(n/\log n\),
\[
\frac{(a)_m(b)_m}{(ab)^m}=1+O(m^2/\min(a,b)),
\]
uniformly over that range. This follows from the products of \(1-i/a\) and \(1-i/b\). For finitely many disjoint compact length intervals \(I_j\) in \((0,\infty)\), expand the mixed factorial moments of \(\Xi_n(I_j)\) as sums over ordered slots of cycle lengths. At fixed factorial orders all terms have total length \(O(\log n)\). The exact identity and the last estimate show that conditionally the mixed moments differ by \(o_{\Pr}(1)\) from the product powers of the means \(\sum_{r/\log n\in I_j}q_n^r/r\). These sums converge in probability to \(\int_{I_j} e^{-2t}\,dt/t\) by the overlap estimate and Riemann sums. All the conditional mixed moments at the fixed orders are bounded by the corresponding products of \(\sum_{r/\log n\in I_j}1/r\), bounded as \(n\to\infty\). Thus the unconditional mixed factorial moments converge as well. The multivariate factorial-moment criterion for Poisson laws gives convergence of these joint counts; these intervals, with boundary of zero intensity and bounded mean counts on compacts, give vague convergence to the Poisson random measure. For any fixed collection of short lengths the same argument with total length fixed gives independent Poisson limits of means \(1/r\).

**4. Largest cycle and total mass.** Fix \(0<\eta<2\) and write \(\ell=\log n\). With probability tending to one, \(q_n\leq e^{-(2-\eta)/\ell}\). On this event, the conditional probability of any length greater than \(M\ell\) is bounded by
\[
\sum_{r>M\ell}\frac{q_n^r}{r}\leq\sum_{r>M\ell}\frac{e^{-(2-\eta)r/\ell}}{r},
\]
whose limit at fixed \(M>0\) is \(\int_M^\infty e^{-(2-\eta)t}\,dt/t\). This tends to zero as \(M\to\infty\). Applying the compact-window limit first on \((x,M]\) and then removing the tail proves the formula for the largest cycle.

For total mass, restrict first to \(\varepsilon\leq r/\ell\leq M\). The scaled mass there converges in law to the sum of the corresponding limiting points, since the boundary has zero intensity. The conditional expected scaled mass below that window is at most \(\varepsilon+1/\ell\), using \(r\mathbb E[C_{n,r}\mid K,L,h]\leq1\). On the high-probability overlap event above, the expected scaled mass beyond \(M\) is at most \(\ell^{-1}\sum_{r>M\ell}e^{-(2-\eta)r/\ell}\), with limit \(e^{-(2-\eta)M}/(2-\eta)\). Markov's inequality controls both discarded parts. The limiting sum of all points is finite almost surely since the mean of the sum is \(\int_0^\infty e^{-2t}\,dt\). The truncated convergence and tail estimates give convergence to that full sum. Its Laplace transform at \(s\geq0\) is
\[
\exp\left(\int_0^\infty (e^{-st}-1)\,e^{-2t}\,\frac{dt}{t}\right)=\frac{2}{2+s},
\]
by the elementary Frullani integral. This is the rate-two exponential law.

## Reproduction and limitations

The supplied standard-library verifier `verification/check_cycles.py` can be run from the record package. It enumerates idempotent maps through \(n=5\), including 40,207 ordered pairs across those sizes, and compares directly extracted noncommon cycle moments with the formula in each feasible root-size/overlap stratum. This checks the finite identity on that bounded range, not the infinite limits. Vague convergence does not imply convergence of the total cycle count; the intensity is not integrable near zero. Transient branches and common-root mass are outside the cycle claim.

## Relationship to prior work

The labeled count \(\sum_k\binom nk k^{n-k}\) is classical. The independent Poisson \(1/r\) short-cycle limits are the same numerical laws as for uniform permutations and in a number of permutation-product models, but those laws alone do not yield logarithmic cycle scales or exponential total mass here. Unrestricted bipartite mappings are a natural comparison: in the present model an alternating edge can instead fall in the common fixed set and kill a noncommon orbit. The root-rank and overlap laws quantify that loss, resulting in the factor \(e^{-2t}\) on the logarithmic scale. Unrestricted transformations, iterations and compositions, and products of involutive permutations are also related but do not impose this random common-root mechanism.

## References

1. J. Hansen and J. Jaworski, *Large components of bipartite random mappings*, Random Structures & Algorithms 17 (2000), 317–342. https://doi.org/10.1002/1098-2418(200010/12)17:3/4%3C317::AID-RSA7%3E3.0.CO;2-7
2. W. F. Brown and P. M. Higgins, *Finite full transformation semigroups as collections of random functions*, Glasgow Mathematical Journal 30 (1988), 203–211. https://doi.org/10.1017/S0017089500007230
3. R. Dalal and E. Schmutz, *Compositions of random functions on a finite set*, Electronic Journal of Combinatorics 9 (2002), R26. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v9i1r26
4. M. Lugo, *The cycle structure of compositions of random involutions*, arXiv:0911.3604. https://arxiv.org/abs/0911.3604
5. M. S. Kammoun and M. Maïda, *A product of invariant random permutations has the same small cycle structure as uniform*, arXiv:1910.04031. https://arxiv.org/abs/1910.04031
6. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009. https://ac.cs.princeton.edu/home/AC.pdf
