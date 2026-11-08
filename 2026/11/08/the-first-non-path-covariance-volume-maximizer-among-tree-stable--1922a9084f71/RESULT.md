# The first non-path covariance-volume maximizer among tree stable-set polytopes

## Finding
For a tree \(T\) on \(n\) vertices, let \(P(T)\) be the convex hull of its independent-set indicator vectors, and let \(\Sigma(T)\) be the covariance of the **uniform distribution on the distinct vertices** of \(P(T)\). Put \(D(T)=\det\Sigma(T)\). Let \(P_n\) be the path and \(B_n\) the broom formed from a path on \(n-2\) vertices by adjoining two new leaves to one endpoint, for every integer \(n\ge4\).

With Fibonacci numbers \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), set \(m=n-2\) and \(Z_j=5F_{m-j}+4F_{m-j-1}\) for \(2\le j\le m-1\). Empty products have value one. Then the following exact expressions hold:
\[
D(P_n)=\frac{\prod_{j=2}^{n}F_j^2}{F_{n+2}^{n+1}},\qquad
D(B_n)=\frac{16F_{m+1}^2\left(\prod_{j=2}^{m}F_j\right)\left(\prod_{j=2}^{m-1}Z_j\right)}{(5F_m+4F_{m-1})^{m+3}}.
\]
The path is the unique determinant maximizer (up to tree isomorphism) through four vertices, but **first fails to maximize at five**. Among the three trees on five vertices the strict order, from largest to smallest, is the broom, path, and star, with exact determinants
\[
D(B_5)=\frac{45}{235298}>D(P_5)=\frac{900}{4826809}>D(K_{1,4})=\frac{4096}{24137569}.
\]
Moreover the counterexample persists in arbitrarily large dimension: \(D(B_n)>D(P_n)\) for all sufficiently large \(n\). In fact, put
\[
\varphi=\frac{1+\sqrt5}{2},\quad q=-\varphi^{-2},\quad c=5+4/\varphi,\quad d=\frac{4-5/\varphi}{5\varphi+4}.
\]
Then the positive product converges and
\[
\lim_{n\to\infty}\frac{D(B_n)}{D(P_n)}=
\frac{400\varphi^9}{c^5}\prod_{t=1}^{\infty}\frac{1-dq^{t-1}}{1-q^t}
=1.004200807\ldots>1.
\]

## Assumptions and scope
Trees are finite, simple, unlabeled up to isomorphism in the extremal statement. The polytope \(P(T)\subset\mathbb R^n\) is full-dimensional: its vertices include the empty indicator and every singleton indicator. The distribution is uniform on these indicator vectors, **not uniform in the interior volume**. The covariance determinant measures the squared product of its principal standard deviations and hence the volume scale of the associated covariance ellipsoid. The comparison is specifically between \(P_n\) and the endpoint-fork broom \(B_n\); no all-size classification of maximizing trees is asserted.

## Proof
**A determinant identity for tree-structured independent-set measures.** Root any tree and write \(p_v=\Pr(X_v=1)\). For any edge \(uv\), the two endpoints never simultaneously occur; set \(t_{uv}=1-p_u-p_v>0\). The hard-core distribution factors over branches conditional on the parent. For a parent \(u\) and child \(v\), conditional occupancy probabilities are \(\Pr(X_v=1\mid X_u=1)=0\) and \(\Pr(X_v=1\mid X_u=0)=p_v/(1-p_u)\). The centered innovation at \(v\) is \(Y_v+p_vY_u/(1-p_u)\), where \(Y_v=X_v-p_v\); the root innovation is \(Y_r\). They are pairwise uncorrelated, their triangular transformation has determinant one, and their variances are \(p_r(1-p_r)\) at the root and \(p_vt_{uv}/(1-p_u)\) for the child. Multiplying gives
\[
\det\Sigma(T)=\prod_{v\in V(T)}p_v(1-p_v)^{1-\deg(v)}\prod_{uv\in E(T)}(1-p_u-p_v).\tag{1}
\]
Every term is positive. This factorization is an elementary specialization of general tree-model covariance factorization; its derivation is included for reproducibility and it is **not** presented as a new general graphical-model theorem.

**Exact path value.** The path independence polynomial at one is \(F_{n+2}\). Removing a vertex and its neighbors splits the path into shorter paths. Substituting the resulting Fibonacci occupancy probabilities into (1), and canceling successive factors, gives the displayed \(D(P_n)\). The same identity follows by multiplying the root-to-leaf conditional innovation variances.

**Exact broom value.** Write the path spine as vertices \(0,\ldots,m-1\), with two additional leaves adjacent to \(m-1\). Let \(Z_j\) count independent sets on the induced suffix beginning at spine vertex \(j\), with both fork leaves included. The fork-end initial values are \(Z_{m-1}=5\), \(Z_m=4\), and \(Z_{m+1}=1\); backward deletion recurrence gives \(Z_j=5F_{m-j}+4F_{m-j-1}\), and \(Z_0=5F_m+4F_{m-1}\). For spine vertex \(i\le m-2\), the occupied and unoccupied probabilities are respectively \(F_{i+1}Z_{i+2}/Z_0\) and \(F_{i+2}Z_{i+1}/Z_0\). For the fork center they are \(F_m/Z_0\) and \(4F_{m+1}/Z_0\); each fork leaf has occupied probability \(2F_{m+1}/Z_0\). The probability neither endpoint of a spine edge \((i,i+1)\) is occupied is \(F_{i+2}Z_{i+2}/Z_0\); for each fork edge it is \(2F_{m+1}/Z_0\). Substituting into (1), respecting the center's degree three, cancels to the displayed \(D(B_n)\) with denominator \(Z_0^{m+3}\). The expressions also work at \(m=2\) under the empty-product convention.

**First failure.** Every tree on at most three vertices is a path. There are two trees on four vertices, a path and a three-leaf star, with determinants \(9/8192>64/59049\). At five vertices there are exactly three unlabeled trees: the path, the three-degree endpoint-fork broom, and the four-leaf star. Direct substitution into (1) gives the three rational values displayed above; cross multiplication proves their strict order.

**Infinite persistence and rigorous sign.** Binet's formula \(F_t=\varphi^t(1-q^t)/\sqrt5\) and \(5F_t+4F_{t-1}=c\varphi^t(1-dq^{t-1})/\sqrt5\) transform the exact finite determinant ratio into a product whose limit is the displayed infinite product. Absolute convergence follows from \(|q|<1\) and \(0<d<1\). The lower-bound certificate in `verify.py` bounds \(\varphi\) between the rational numbers \(1618033988749894/10^{15}\) and \(1618033988749896/10^{15}\), bounds each of the first 25 product factors outward by rationals, and bounds the remaining tail from below by
\[
1-\frac{d_{\mathrm U}a_{\mathrm U}^{25}+a_{\mathrm U}^{26}}{1-a_{\mathrm U}},
\]
where \(a_{\mathrm U}=\varphi_{\mathrm L}^{-2}\) and \(d_{\mathrm U}=(4-5/\varphi_{\mathrm U})/(5\varphi_{\mathrm L}+4)\). The purely rational final lower bound exceeds \(1.0042008072>1\). Its derivation uses \(\prod(1-u_i)\ge1-\sum u_i\) for \(u_i\in[0,1]\). Thus the limit is strictly greater than one, proving the eventual inequality.

## Verification
Run `python3 verify.py` with Python's standard library. It independently enumerates all independent sets for the path and broom at each size from four through twelve, checks the determinant product identity against the closed Fibonacci formulas with exact rational arithmetic, checks all three five-vertex shapes, and evaluates the strictly positive infinite-limit lower bound using rational inequalities. It does not claim to enumerate all trees of arbitrary order or replace any infinite argument.

## Relationship to prior work
Aliniaeifard, Benedetti, Bergeron, Li and Saliola (arXiv:1804.00360) establish structural properties of stable-set polytopes and their one-skeleta. Independence-polynomial recurrences on trees, including the linear-time algorithm in Kadrawi and coauthors (arXiv:2201.00432), provide the counting background. Loh and Wainwright (2013; arXiv:1212.0478) establish sparsity of tree-structured binary inverse covariance, while Nguyen and Berg (arXiv:1112.3501, especially their equations (4), (10)--(11)) give exact general tree-model covariance-precision relations. Those broader graphical-model results account for the general determinant factorization used as a **lemma**, not for a claimed discovery. The specific metric comparison of the path with endpoint-fork trees, first failing size, closed determinant ratio, and strictly positive asymptotic gap are the proposed contribution.

## Limitations
No extremal theorem for every tree on \(n\ge6\) vertices is claimed. The analytic argument establishes eventual superiority of the broom, but not a sharp finite threshold for that inequality. A numerical estimate for the limiting ratio is only explanatory; strict positivity is certified independently by rational bounds. Historical priority remains subject to further comparison with literature on tree-model determinant optimization and hard-core partition functions; generic inverse-covariance sparsity is explicitly prior work. The covariance is vertex-uniform, not the inertia tensor for continuous volume in the polytope.

## References
1. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, and F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360 (first posted 2018-04-02), https://arxiv.org/abs/1804.00360.
2. O. Kadrawi and coauthors, *A Linear Algorithm for Computing Independence Polynomials of Trees*, arXiv:2201.00432 (2022), https://arxiv.org/abs/2201.00432.
3. P.-L. Loh and M. J. Wainwright, *Structure estimation for discrete graphical models: Generalized covariance matrices and their inverses*, Annals of Statistics 41 (2013), 3022--3049, arXiv:1212.0478, https://arxiv.org/abs/1212.0478.
4. H. C. Nguyen and J. Berg, *Bethe-Peierls approximation and the inverse Ising model*, arXiv:1112.3501 (2011), https://arxiv.org/abs/1112.3501.
