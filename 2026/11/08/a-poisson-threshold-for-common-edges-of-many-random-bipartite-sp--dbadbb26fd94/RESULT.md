# A Poisson threshold for common edges of many random bipartite spanning trees

## Finding

Fix an integer \(k\ge 3\). Let \(T_1,\ldots,T_k\) be independent uniformly distributed spanning trees of the labeled complete bipartite graph \(K_{a,b}\). Let \(I=\bigcap_{j=1}^{k}E(T_j)\) and \(X=|I|\). For all integers \(1\le a\le b\), put
\[
p=\frac{a+b-1}{ab},\qquad \Lambda=abp^k.
\]
The following finite and asymptotic statements hold.

1. **Exact moments and variance control.** For every \(a,b,k\), \(\mathbb E X=\Lambda\), and \(\operatorname{Var}(X)\le\Lambda\). The second falling moment has the exact expression
\[
\begin{split}
\mathbb E[(X)_2]=ab\bigg[&(b-1)\left(p^2-\frac{(a-1)^2}{a^2b^2}\right)^k\\
+&(a-1)\left(p^2-\frac{(b-1)^2}{a^2b^2}\right)^k\\
+&(a-1)(b-1)\left(p^2-\frac{1}{a^2b^2}\right)^k\bigg].
\end{split}
\]
Here \((x)_r=x(x-1)\cdots(x-r+1)\) is the falling factorial.

2. **Sharp threshold.** Suppose \(a\to\infty\), \(b\ge a\), and write \(s_a=b/a^{k-1}\). If \(s_a\to0\), then \(\Pr(X=0)\to1\). If \(s_a\to\infty\), then \(\Pr(X>0)\to1\). If \(s_a\to\theta\in(0,\infty)\), then
\[
d_{\mathrm{TV}}\bigl(\mathcal L(X),\operatorname{Pois}(\theta)\bigr)\longrightarrow0,
\qquad \Pr(X>0)\longrightarrow1-e^{-\theta}.
\]
Thus the nondegenerate scale is \(b\asymp a^{k-1}\), quadratic for three trees and cubic for four.

3. **Spatial structure.** In the finite positive critical regime, \(\Pr(I\text{ is a matching})\to1\). Conditional on its size and on being a matching, \(I\) is *exactly* uniform among all matchings of that size in \(K_{a,b}\), for every finite \(a,b\). Equivalently, the entire edge-set law is asymptotically, in total variation, obtained by drawing \(Z\sim\operatorname{Pois}(\theta)\), then choosing a uniform \(Z\)-edge bipartite matching (with any fixed convention if \(Z>\min\{a,b\}\)).

## Assumptions and scope

All graphs are finite, simple, unweighted and labeled. Trees are independently sampled with replacement from the uniform spanning-tree distribution of the same graph. The number of trees \(k\) is fixed as \(a\to\infty\); no claim is made when \(k\) grows. The threshold statements assume \(b\ge a\); the finite exact formulas do not. A matching is an edge set with no shared endpoints. Total variation refers to the full discrete distribution, not only convergence of moments.

## Proof

**1. Inclusion determinant.** Orient each edge from the \(a\)-part to the \(b\)-part. Kirchhoff's weighted matrix-tree theorem and the matrix determinant lemma give, for any distinct edges \(F\),
\[
\Pr(F\subseteq E(T_1))=\det K_F,
\]
where \(K_F\) is the matrix of voltage differences produced by unit edge currents, restricted to \(F\). Indeed, assign conductance \(1+w_e\) to each edge \(e\in F\), and conductance one elsewhere. The ratio of spanning-tree polynomials is both \(\mathbb E\prod_{e\in F}(1+w_e\mathbf1_{e\in T_1})\) and \(\det(I+\operatorname{diag}(w_e)K_F)\). Equating the coefficient of \(\prod_{e\in F}w_e\) proves the identity. This also covers cyclic \(F\), with determinant zero.

For \(e=(u,v)\) and \(f=(u',v')\), with \(u,u'\) in the \(a\)-part and \(v,v'\) in the \(b\)-part, solving the bipartite Laplacian equations for a unit current along \(f\) gives
\[
K_{ef}=\frac{\mathbf1_{u=u'}}{b}+\frac{\mathbf1_{v=v'}}{a}-\frac1{ab}.
\]
For completeness, if \(V\) is a potential for a unit current from \(u'\) to \(v'\), the equations imply \(V(u)=\overline V_B+\mathbf1_{u=u'}/b\) and \(V(v)=\overline V_A-\mathbf1_{v=v'}/a\), where \(\overline V_A-\overline V_B=1/(ab)\). Subtraction yields the kernel. In particular every diagonal equals \(p\). Since \(K_F\) is positive semidefinite, Hadamard's inequality yields
\[
0\le\Pr(F\subseteq E(T_1))\le p^{|F|}.
\]
For \(r\) pairwise vertex-disjoint edges the kernel is \((p+1/(ab))I-(1/(ab))J\), so
\[
q_r:=\Pr(F\subseteq E(T_1))
=\frac{(a+b)^{r-1}(a+b-r)}{(ab)^r},
\qquad 1\le r\le\min\{a,b\}.
\]
This formula is an exact instance of the fixed-forest enumeration for bipartite spanning trees.

**2. Exact first and second moments.** For each edge \(e\), let \(Z_e=\prod_{j=1}^k\mathbf1_{\{e\in T_j\}}\). Independence of the trees implies \(\mathbb EZ_e=p^k\), and therefore \(\mathbb EX=abp^k\). For distinct edges \(e,f\),
\[
\mathbb E(Z_eZ_f)=(p^2-K_{ef}^2)^k\le p^{2k}=\mathbb EZ_e\,\mathbb EZ_f.
\]
Thus all distinct \(Z_e,Z_f\) are nonpositively correlated and \(\operatorname{Var}(X)\le\sum_e\operatorname{Var}(Z_e)\le\Lambda\). Distinct ordered edge pairs sharing only their \(a\)-endpoint, sharing only their \(b\)-endpoint, or sharing neither number \(ab(b-1)\), \(ab(a-1)\), and \(ab(a-1)(b-1)\), respectively. Substituting the three off-diagonal kernel values yields the displayed second falling moment.

**3. Factorial-moment sandwich and Poisson law.** For every fixed integer \(r\ge1\) and all sufficiently large \(a,b\) with \(r\le\min\{a,b\}\), consider ordered selections of \(r\) distinct edges. There are \((a)_r(b)_r\) selections with no shared endpoints, each present in all \(k\) trees with probability \(q_r^k\). Every other selection has probability at most \(p^{kr}\). Therefore
\[
(a)_r(b)_r q_r^k\le\mathbb E[(X)_r]\le (ab)_r p^{kr}\le\Lambda^r.
\]
If \(b/a^{k-1}\to\theta\in(0,\infty)\), then \(b/a\to\infty\), \(\Lambda\to\theta\), and, for every fixed \(r\),
\[
\frac{(a)_r(b)_r}{(ab)^r}\to1,
\qquad\frac{q_r}{p^r}=\frac{(a+b)^{r-1}(a+b-r)}{(a+b-1)^r}\to1.
\]
Consequently \(\mathbb E[(X)_r]\to\theta^r\). This establishes convergence of point probabilities, not merely moments: for each fixed \(j\ge0\), the finite binomial inversion identity is
\[
\Pr(X=j)=\frac1{j!}\sum_{\ell\ge0}\frac{(-1)^\ell}{\ell!}\mathbb E[(X)_{j+\ell}],
\]
where the summands beyond the finite support are zero. For bounded \(\Lambda\), their absolute values are dominated by \(\Lambda^{j+\ell}/(j!\ell!)\); dominated convergence gives \(\Pr(X=j)\to e^{-\theta}\theta^j/j!\). Since the limiting mass is one, the convergence is in total variation on \(\mathbb N_0\).

For the two extreme regimes, note the exact identity
\[
\Lambda=\frac{b}{a^{k-1}}\left(1+\frac{a-1}{b}\right)^k.
\]
When \(b\ge a\), the parenthesized factor lies between one and \(2^k\). Hence \(\Lambda\to0\) in the subcritical regime, giving \(\Pr(X>0)\le\Lambda\to0\). In the supercritical regime, \(\Lambda\to\infty\), and Chebyshev's inequality with \(\operatorname{Var}(X)\le\Lambda\) gives \(\Pr(X=0)\le1/\Lambda\to0\).

**4. Geometry of the critical intersection.** At finite positive \(\theta\), the expected number of unordered pairs of distinct common edges sharing at least one endpoint is at most
\[
\frac{ab(a+b-2)}2 p^{2k}=\frac{a+b-2}{2ab}\Lambda^2\longrightarrow0.
\]
Markov's inequality shows that \(I\) is a matching with probability tending to one. The action of \(S_a\times S_b\) preserves the joint law of the trees and acts transitively on size-\(r\) bipartite matchings. Hence the conditional uniformity is exact. Combine this symmetry with total-variation convergence of the cardinality and the vanishing nonmatching probability to obtain the stated total-variation approximation for the entire edge set.

## Verification

The standalone file `check.py` independently enumerates all spanning trees for seven small bipartite graphs and compares every one-, two-, and three-edge inclusion probability with an exact rational kernel determinant. It separately enumerates complete tuples of three or four trees for small graph sizes, checks the exact first and second falling moments, and checks factorial-moment bounds in finite critical-window examples. Run `python3 check.py`; the expected output is `VERIFY_OK 2175 exact assertions`. The analytic inequalities and all infinite-limit arguments above, not the finite tests, establish the theorem.

## Relationship to prior work

Dong and Ge's 2021 preprint provides a general forest-containment formula for complete bipartite spanning trees. Its fixed-matching instance agrees with \(q_r\); it does not consider intersections of multiple independently sampled trees or a Poisson threshold. Bóna, Burghart and Wagner (first public preprint 2025) establish a two-tree Poisson limit on complete multipartite graphs under *positive limiting proportions* of all vertex classes. Their separate observation about \(k\ge3\) trees concerns complete graphs, for which the intersection is empty with high probability. Neither statement entails the nondegenerate \(k\ge3\) unbalanced-bipartite regime. Bender and Canfield (1999) treat uniform random embeddings of fixed graphs into complete graphs rather than trees sampled from a fixed unbalanced bipartite graph with a common preserved bipartition; their labeling model and mean scale differ.

## Limitations

The theorem fixes \(k\ge3\) and requires \(a\to\infty\); it makes no rate claim for total-variation convergence and does not assert a Poisson limit for growing \(k\), fixed \(a\), or intersections of general graph families. Its originality comparison concerns the cited accessible sources and does not certify exhaustive historical priority. An independent mathematical audit has not been performed.

## References

- F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294, first public 2021-03-09; Journal of Graph Theory 101 (2022), 79–94. https://arxiv.org/abs/2103.05294
- M. Bóna, F. Burghart and S. Wagner, *On the intersection of pairs of trees*, arXiv:2501.18570, first public 2025-01-30; Sections 2 and 4 and Remark 2 in the 2026-09-09 revision. https://arxiv.org/html/2501.18570v4
- E. A. Bender and E. R. Canfield, *Intersections of Randomly Embedded Sparse Graphs are Poisson*, Electronic Journal of Combinatorics 6 (1999), R36. https://doi.org/10.37236/1468
