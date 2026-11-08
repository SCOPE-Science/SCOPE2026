# All interior moments and covariance signs of two-row partial-permutation polytopes

## Finding

For each integer \(n\geq1\), let \(P_n\subset\mathbb R^{2n}\) be the convex hull of all \(2\times n\) zero-one partial-permutation matrices: each row and each column has at most one \(1\). Use the standard Euclidean coordinates \((x_1,\ldots,x_n,y_1,\ldots,y_n)\). Then

\[
\operatorname{Vol}_{2n}(P_n)=\frac{1}{(n!)^2}-\frac{n}{(2n)!},\qquad
(2n)!\operatorname{Vol}_{2n}(P_n)=\binom{2n}{n}-n.
\]

The displayed **volume identity is previously known**, proved in Heuer and Striker [1, Theorem 3.8]; it serves here as the normalizing constant. The new result is an explicit closed formula for **every polynomial moment of uniform interior volume**, together with a strict covariance-sign characterization. For arbitrary exponents the finite exact formula is as follows. For arbitrary \(\alpha,\beta\in\mathbb Z_{\ge0}^{n}\), set \(A=\sum_i\alpha_i\), \(B=\sum_i\beta_i\), and
\[
Q_n(\alpha,\beta)=\frac{\prod_i\alpha_i!\,\prod_i\beta_i!}{(n+A)!(n+B)!}.
\]
For each \(j\) define \(a_j=n-1+A-\alpha_j\), \(b_j=n-1+B-\beta_j\), and
\[
C_{n,j}(\alpha,\beta)
=\frac{\prod_{i\ne j}\alpha_i!\,\beta_i!}{a_j!\,b_j!}
\sum_{p=0}^{\alpha_j}\sum_{q=0}^{\beta_j}
(-1)^{p+q}\binom{\alpha_j}{p}\binom{\beta_j}{q}
\frac{(a_j+p)!(b_j+q)!}{(a_j+b_j+p+q+2)!}.
\]
If \(X\) is uniformly distributed over \(P_n\) by \(2n\)-dimensional Euclidean volume, then
\[
\boxed{\mathbb E\prod_{i=1}^n X_{1i}^{\alpha_i}X_{2i}^{\beta_i}
=\frac{Q_n(\alpha,\beta)-\sum_{j=1}^{n}C_{n,j}(\alpha,\beta)}{\operatorname{Vol}_{2n}(P_n)}.}
\]

For \(n\ge2\), **the sign of the covariance of two distinct coordinate entries records rook attacks exactly**: covariance is strictly negative when the cells share a row or a column, and strictly positive when they lie in different rows and different columns. This sign statement concerns uniform *interior volume*, not a uniform choice of a partial-permutation vertex.

## Assumptions and scope

The polytope is full-dimensional in the ordinary \(2n\)-coordinate realization, with \(n\) an arbitrary positive integer. There is no stochastic independence assumption for its coordinates. All factorials and binomial coefficients in the formula are ordinary integer factorials and binomial coefficients, including \(0!=1\). Exponents are nonnegative integers, so the result gives all polynomial moments. The volume normalization is the standard lattice-normalized volume, namely \((2n)!\) times coordinate Lebesgue volume. No claim is made about higher-row matching polytopes or about the partial **permutohedron**, which is a different projection polytope.

## Proof

**1. Two product simplices and pairwise disjoint excluded caps.** The bipartite-matching polytope inequality description [1, Proposition 3.4] gives
\[
P_n=\left\{x_i,y_i\ge0:\ \sum_i x_i\le1,\ \sum_i y_i\le1,\ x_j+y_j\le1\ \text{for all }j\right\}.
\]
Thus \(P_n=(\Delta_n\times\Delta_n)\setminus\bigcup_j E_j\), up to measure-zero boundaries, where \(\Delta_n=\{z_i\ge0,\sum_i z_i\le1\}\) and \(E_j\) is the cap \(x_j+y_j>1\). For different \(j,k\), simultaneous membership in \(E_j\cap E_k\) would imply \(\sum_i x_i+\sum_i y_i>2\), contrary to the two row-sum bounds. Consequently, **the caps have pairwise disjoint interiors**, and subtraction requires no higher inclusion-exclusion terms.

**2. Exact cap integration.** The Dirichlet simplex integral gives
\[
\int_{\Delta_n\times\Delta_n}x^\alpha y^\beta\,dx\,dy=Q_n(\alpha,\beta).
\]
On \(E_j\), substitute \(u=1-x_j\) and \(v=1-y_j\). The condition becomes \(u,v\ge0\), \(u+v<1\). The remaining \(n-1\) coordinates of the first row occupy a simplex of total capacity \(u\), and those of the second row one of capacity \(v\). Integrating them gives the factor
\[
\frac{\prod_{i\ne j}\alpha_i!\beta_i!}{a_j!\,b_j!}
\,u^{a_j}v^{b_j}(1-u)^{\alpha_j}(1-v)^{\beta_j}.
\]
Expand the two final integer powers by the binomial theorem. The resulting triangular integral is
\[
\int_{u,v\ge0,\,u+v\le1}u^{a_j+p}v^{b_j+q}\,du\,dv
=\frac{(a_j+p)!(b_j+q)!}{(a_j+b_j+p+q+2)!},
\]
which yields exactly \(C_{n,j}(\alpha,\beta)\). Subtracting the disjoint caps proves the all-degree moment formula after normalization. At \(\alpha=\beta=0\), each cap has volume \(1/(2n)!\), while the product simplex has volume \(1/(n!)^2\). This independently recovers the **known** volume identity [1, Theorem 3.8]; the new step is its extension to arbitrary monomial integrals.

**3. Covariance signs.** For \(n\ge2\), put \(q=1/\binom{2n}{n}\), \(Z=1-nq>0\), and \(T=2n+1\). On a cap \(E_j\), the substituted \((u,v,1-u-v)\) has the Dirichlet law with parameters \((n,n,1)\). Given \(u,v\), the residual rows are independent uniform scaled simplices. This determines the first and second moments from their Dirichlet moments. By row and column symmetries, writing \(\mu=\mathbb E X_{11}\), the required representatives are
\[
\begin{aligned}
\mu&=\frac{1/(n+1)-2nq/T}{Z},\\
\mathbb E X_{11}X_{12}&=\frac{1/((n+1)(n+2))-3nq/[T(T+1)]}{Z},\\
\mathbb E X_{11}X_{21}&=\frac{1/(n+1)^2-(n^2+3n+1)q/[T(T+1)]}{Z},\\
\mathbb E X_{11}X_{22}&=\frac{1/(n+1)^2-(3n+2)q/[T(T+1)]}{Z}.
\end{aligned}
\]
Set \(D=2(n+1)^2(2n+1)^2 Z^2\). Direct substitution, with subtraction of \(\mu^2\), gives
\[
\operatorname{Cov}(X_{11},X_{22})
=\frac{q}{D}\Big((n-1)(n+2)(2n+1)
-n(n+1)(2n^2+n-2)q\Big),
\]
and
\[
\operatorname{Cov}(X_{11},X_{21})
=\frac{q}{D}\Big(-(2n^4+n^3-4n^2+1)
+(2n^5+n^4-4n^3-2n^2+n)q\Big).
\]
Finally, define
\[
\begin{aligned}
F_n(q)={}&8n^2+8n+2-(2n^4+19n^3+25n^2+8n)q\\
&+(2n^5+11n^4+19n^3+10n^2)q^2.
\end{aligned}
\]
Then
\[
\operatorname{Cov}(X_{11},X_{12})
=-\frac{F_n(q)}{2(n+1)^2(n+2)(2n+1)^2Z^2}.
\]
Since the central binomial coefficient is the largest entry in its row,
\(\binom{2n}{n}\ge\binom{2n}{2}=n(2n-1)\ge n(n+1)\) for \(n\ge2\). Hence \(0<q\le1/[n(n+1)]\). The positive bracket for nonattacking cells is bounded below by
\[
(n-1)(n+2)(2n+1)-(2n^2+n-2)=n(2n^2+n-4)>0.
\]
For competing cells in a column, the absolute value of the negative bracket is bounded below by
\[
(2n^4+n^3-4n^2+1)-\frac{2n^5+n^4-4n^3-2n^2+n}{n(n+1)}
=n(2n^3-n^2-3n+3)>0.
\]
For two cells in a row, discarding the nonnegative quadratic term gives
\[
F_n(q)\ge 3(n-2)(2n+1)\ge0.
\]
The inequality is strict for \(n\ge3\); at \(n=2\) the discarded quadratic term is strictly positive. This proves every claimed covariance sign. Since all distinct entries either attack in a row or column or form a nonattacking pair, it also proves the classification.

## Verification

The self-contained exact-rational script `verification/check_rook_moments.py` checks the formula against an independent method: weighted Ehrhart counting. For every positive integer dilation \(t\), it enumerates integer points satisfying the row and column inequalities and computes weighted sums of selected coordinate monomials. The leading coefficient of the resulting weighted Ehrhart polynomial equals the corresponding Lebesgue integral. Finite differences recover that coefficient using integer arithmetic; no numerical integration or reliance on the cap decomposition is used in this second computation. Explicit checks cover \(n=1,2,3\) for selected moments through degree three and \(n=4\) for volume. The script also checks every covariance sign class when \(n=2,3\).

The script prints `TWO_ROW_ROOK_EXACT_CHECKS_PASSED 31`. Its finite checks support the all-\(n\) proof but cannot substitute for it. Normalized volumes \(1,4,17,66\) for \(n=1,2,3,4\) agree with Table/Figure 1 of [1].

## Relationship to prior work

Heuer and Striker [1, Section 3, Proposition 3.4 and **Theorem 3.8** in the 2022 revision] established the inequality description and **proved** normalized volume \(\binom{2n}{n}-n\) for all \(n\) by an Ehrhart argument (the manuscript states this was an earlier conjecture, subsequently proved by an anonymous referee). The known volume result is **not claimed as original**. The new contribution is the explicit simultaneous evaluation of every interior monomial moment and the rigorous, all-\(n\) sign classification for different entries. These are not consequences of knowing only the volume or Ehrhart polynomial. Behrend and collaborators [2] determine volumes and Ehrhart formulas for **partial permutohedra**, obtained by projection from matrix polytopes. Their projection is not volume preserving and their results do not imply the matrix-polytope volume or its interior moments. General techniques for moments of polytopes, such as [3], can in principle compute special cases but do not state this two-row formula or the sign classification. The result is distinct from covariance computations for uniform *vertices* of square matching polytopes: sampling vertices does not equal sampling interior Lebesgue volume.

## Limitations

The two-row hypothesis is essential for the easy disjoint-cap decomposition: with three or more rows, the forbidden column events are not generally pairwise disjoint. The exact formula may become computationally costly for large exponents, though every sum is finite. The structural sign law is asserted in the canonical Euclidean indicator coordinates; it is not invariant under arbitrary affine changes of coordinates. The proof does not establish a corresponding full covariance sign theorem for all rectangular matching polytopes. The source proves the volume identity; no novelty is asserted for that fact. Although inspected full text and indexed records did not yield a covering evaluated all-degree moment law or covariance-sign classification, older or differently indexed literature could affect the priority of those new assertions. Independent mathematical auditing has not been performed.

## References

[1] Dylan Heuer and Jessica Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, first publicly submitted 2020-12-17, Section 3, especially Proposition 3.4, Figure 1 and **Theorem 3.8 (proved in the March 2022 revision)**. https://arxiv.org/abs/2012.09901

[2] Roger E. Behrend, Federico Castillo, Anastasia Chavez, Alexander Diaz-Lopez, Laura Escobar, Pamela E. Harris and Erik Insko, *Partial permutohedra*, arXiv:2207.14253, first submitted 2022-07-28, Sections 2 and 4–5. https://arxiv.org/abs/2207.14253

[3] Nick Gravin, Dmitrii V. Pasechnik, Boris Shapiro and Michael Shapiro, *On moments of a polytope*, arXiv:1210.3193, first submitted 2012-10-11, Analysis and Mathematical Physics 8 (2018), 255–287. https://arxiv.org/abs/1210.3193
