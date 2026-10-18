# Exact negative area–return covariance for uniform Dyck excursions

## Finding

Let \(n\ge1\) and choose a Dyck path with \(n\) up-steps and \(n\) down-steps uniformly from the \(C_n=\frac1{n+1}\binom{2n}{n}\) possibilities. Write its step heights as \(H_0=0,H_1,\ldots,H_{2n}=0\), so consecutive heights differ by one and all heights are nonnegative. Let
\[
A_n=\sum_{j=0}^{2n-1}H_j,
\qquad
R_n=\#\{j\in\{1,\ldots,n\}:H_{2j}=0\}.
\]
Thus \(R_n\) counts completed primitive excursions, including the terminal return, but not the initial time-zero visit. Then
\[
\boxed{\operatorname{Cov}(A_n,R_n)
=\frac{6\,4^n/C_n-2(2n+1)(n+3)}{n+2}.}
\]
The covariance vanishes at \(n=1\) and is strictly negative for every \(n\ge2\). It has the sharper asymptotic expansion
\[
\operatorname{Cov}(A_n,R_n)
=-4n+6\sqrt{\pi n}-6+O(n^{-1/2}).
\]
The corresponding Pearson correlation satisfies
\[
\boxed{\operatorname{Corr}(A_n,R_n)
\sim -\frac{2}{\sqrt{10/3-\pi}}n^{-1/2}.}
\]

## Assumptions and scope

All probabilities are with respect to the uniform distribution on the finite set of Dyck paths of *semilength* \(n\). Area is the total unscaled height at the beginning of each step (equivalently the Euclidean area under the piecewise-linear walk). It is related to the customary diagonal-lattice area by \(A_n=2\,\mathrm{area}_{\mathrm{lattice}}+n\). The endpoint return is counted. Covariance is computed before any normalization. The correlation is undefined at \(n=1\), where both variables are constant, and the asymptotic correlation concerns \(n\ge2\).

## Proof

Let \(F(z,q)=\sum_{n\ge0}\sum_{d\in\mathcal D_n}z^nq^{A(d)}\), where \(\mathcal D_n\) is the set of Dyck paths of semilength \(n\). A primitive component has the form \(U d D\) with \(d\in\mathcal D_{k-1}\); its area is \(A(d)+2k-1\). Therefore its area-generating series is
\[
P(z,q)=zq F(zq^2,q),\qquad F(z,q)=\frac1{1-P(z,q)}.
\]
Mark the number of primitive components by \(u\). The exact joint series is
\[
G(z,q,u)=\sum_{n\ge0}\sum_{d\in\mathcal D_n}
 z^nq^{A(d)}u^{R(d)}=\frac1{1-uP(z,q)}.
\]
All derivatives below are formal power-series derivatives; coefficient extraction is legitimate because each size has finitely many paths.

Set \(t=\sqrt{1-4z}\) with constant term one and \(C(z)=F(z,1)=\frac{2}{1+t}\). The primitive series is \(P(z,1)=zC(z)=\frac{1-t}{2}\). Differentiating the two defining identities with respect to \(q\), setting \(q=1\), and solving gives the unusually simple primitive-area identity
\[
\left.\partial_qP(z,q)\right|_{q=1}
=\frac{z}{1-4z}.
\]
Indeed, writing \(B=\left.\partial_qF\right|_{q=1}\), the equations are \(B=C^2P_q\) and \(P_q=z(C+2zC'+B)\); using \(C=1+zC^2\) yields the displayed expression. In particular the sum of areas over all primitive paths of semilength \(k\) is exactly \(4^{k-1}\), for every integer \(k\ge1\).

Differentiate \(G\) at \(q=u=1\). With subscripts recording the variables differentiated, the three series for total area, total return count and their mixed product are
\[
G_q=\frac1{t^2}-\frac2t+C,
\quad G_u=C^2-C,
\quad G_{qu}=(2C-1)G_q
=\frac3{t^2}-\frac{10}t+5C+2C^2.
\]
The final equality follows by substituting \(C=2/(1+t)\) and simplifying. Coefficient extraction uses \([z^n]t^{-2}=4^n\), \([z^n]t^{-1}=\binom{2n}{n}\), \([z^n]C=C_n\), \([z^n]C^2=C_{n+1}\), and \(\binom{2n}{n}=(n+1)C_n\). Consequently,
\[
\mathbb E A_n=\frac{4^n}{C_n}-2n-1,
\qquad\mathbb E R_n=\frac{3n}{n+2},
\]
\[
\mathbb E(A_nR_n)
=3\frac{4^n}{C_n}-10n-5+2\frac{C_{n+1}}{C_n}.
\]
Subtracting the product of means, with \(C_{n+1}/C_n=2(2n+1)/(n+2)\), yields the announced exact covariance.

To prove its sign for all sizes, set
\[
K_n=\frac{(2n+1)(n+3)C_n}{3\,4^n}.
\]
The covariance is \(\frac{6\,4^n}{(n+2)C_n}(1-K_n)\). Now \(K_1=1\), and the Catalan ratio implies
\[
\frac{K_{n+1}}{K_n}=1+\frac{n}{2(n+2)(n+3)}>1
\quad(n\ge1).
\]
Hence \(K_n>1\) for every \(n\ge2\), giving strict negativity with no unverified limiting argument.

For the correlation, a second differentiation gives
\[
\left.\partial_q^2 F\right|_{q=1}
=t^{-2}+\tfrac12t^{-3}-4t^{-4}+\tfrac52t^{-5},
\qquad
\left.\partial_u^2 G\right|_{q=u=1}=2z^2C^5.
\]
Extracting coefficients and subtracting the squares of the means yields the exact variances
\[
\operatorname{Var}(A_n)
=\frac{(n+1)(2n+1)(5n+3)}{3}-\left(\frac{4^n}{C_n}\right)^2,
\]
\[
\operatorname{Var}(R_n)
=\frac{2n(n-1)(2n+1)}{(n+2)^2(n+3)}.
\]
These are strictly positive for \(n\ge2\). Stirling's formula gives \(C_n=\frac{4^n}{\sqrt\pi n^{3/2}}(1-\frac9{8n}+O(n^{-2}))\). The exact expressions therefore imply
\[
\operatorname{Var}(A_n)=(10/3-\pi)n^3+O(n^2),
\quad\operatorname{Var}(R_n)=4+O(n^{-1}),
\]
\[
\operatorname{Cov}(A_n,R_n)
=-4n+6\sqrt{\pi n}-6+O(n^{-1/2}).
\]
Since \(10/3-\pi>0\), dividing by the product of standard deviations establishes the stated correlation asymptotic.

## Verification

Running `python3 verify.py` with Python's standard library independently enumerates all \(82{,}499\) Dyck paths of semilengths \(1\) through \(11\), comparing direct rational moments to the displayed formulas. The program separately extracts coefficients from the simplified generating functions for \(150\) semilengths and checks the closed covariance, signs and ratio identity with exact rational arithmetic. These finite checks support the algebra but are not substituted for the infinite proof above.

## Relationship to prior work

The Dyck-area generating series is classical. Janson's 2007 Brownian-area survey gives the probabilistic area background, not a discrete joint area/return covariance. Kobayashi, Sato, Hoshi and Morita (2015, Section 3) explicitly enumerate the number of zero returns, without combining it with area in the portion inspected. Blanco and Petersen (2012) analyze area jointly with a **different** statistic, the noncrossing-partition rank. Petersen (2019, Chapter 10) already supplies both the prime-component decomposition and the area-refined Catalan functional equation; adjoining a variable for the prime count is therefore a standard generating-function step, not claimed as novel here. The potentially new assertion is the derived exact mixed covariance, its **universal strict negative sign**, and the nonzero linear covariance alongside a vanishing \(n^{-1/2}\)-order correlation. Exact historical priority has not been independently established.

## Limitations

This is an exact finite-Catalan-model theorem, not a general statement about arbitrary conditioned walks, Catalan-weighted models, or continuous Brownian excursions. An asymptotically vanishing correlation does not imply independence. General Catalan bivariate identities may yield the covariance indirectly even if they do not display the sign or asymptotic cancellation. The result has self-review only and no independent audit.

## References

1. Svante Janson, *Brownian excursion area, Wright's constants in graph enumeration, and other Brownian areas*, Probability Surveys 4 (2007), 80–145, initial public arXiv posting 2007-04-18, https://arxiv.org/abs/0704.2289.
2. Saul A. Blanco and T. Kyle Petersen, *Counting Dyck paths by area and rank*, arXiv:1206.0803, 2012, https://arxiv.org/abs/1206.0803.
3. Kingo Kobayashi, Hajime Sato, Mamoru Hoshi and Hiroyoshi Morita, *A Walk on Random Walks Through the Symbolic Method*, 2015, Section 3, https://www.researchgate.net/publication/282737543_A_WALK_ON_RANDOM_WALKS_THROUGH_THE_SYMBOLIC_METHOD.
4. T. Kyle Petersen, *Inquiry-Based Enumerative Combinatorics*, Springer, 2019, Chapter 10, https://doi.org/10.1007/978-3-030-18308-0.
5. FindStat, statistic St000011, the number of touch points of a Dyck path, https://www.findstat.org/StatisticsDatabase/St000011/.
