# A universal fifteen-vertex width transition for complete-bipartite graph associahedra

## Finding
Let \(2\le p\le q\), \(n=p+q\), \(L=[p]\), and \(R=\{p+1,\ldots,p+q\}\). Write \(\Delta_T=\operatorname{conv}\{e_i:i\in T\}\) and define the (translation-normalized) graph associahedron
\[
A_{p,q}=\sum_{\varnothing\ne U\subseteq L}\ \sum_{\varnothing\ne V\subseteq R}\Delta_{U\cup V}\ \subset\mathbb R^n.
\]
It is the standard unit tube-simplex realization of the graph associahedron of \(K_{p,q}\), with singleton point summands omitted because these only translate the polytope. Its affine hull is the hyperplane of coordinate sum \(B=(2^p-1)(2^q-1)\), equipped with the induced Euclidean metric.

For a nonempty proper subset \(S\subset[n]\), put \(s=|S\cap L|\), \(t=|S\cap R|\), and \(k=s+t\). Define
\[
W_{p,q}(s,t)=B-(2^s-1)(2^t-1)
-(2^{p-s}-1)(2^{q-t}-1).
\]
The exact minimum Euclidean width is
\[
\boxed{w_{\min}(A_{p,q})=\min_{\substack{0\le s\le p,\ 0\le t\le q\\1\le s+t\le n-1}}
W_{p,q}(s,t)\sqrt{\frac{n}{(s+t)(n-s-t)}}.}
\tag{1}
\]
This finite formula admits a complete phase classification, independent of the aspect ratio \(p/q\):

**Small phase, \(4\le n\le14\).** The minimizing cuts are exactly singleton cuts in the larger color class \(R\) and their complements; when \(p=q\), singleton cuts in either class and their complements minimize. In particular,
\[
\boxed{w_{\min}(A_{p,q})=2^{q-1}(2^p-1)\sqrt{\frac{n}{n-1}}.}
\tag{2}
\]

**Balanced phase, \(n\ge15\).** The minimizing cuts are exactly those for which
\[
\begin{split}
s&\in\{\lfloor p/2\rfloor,\lceil p/2\rceil\},\\
t&\in\{\lfloor q/2\rfloor,\lceil q/2\rceil\},\\
k&\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}.
\end{split}
\tag{3}
\]
All cuts satisfying (3) give the same value in (1). For example, take \(s_0=\lfloor p/2\rfloor\) and \(t_0=\lfloor q/2\rfloor+\mathbf1_{p\text{ odd and }q\text{ odd}}\). Then \(k_0=s_0+t_0=\lfloor n/2\rfloor\) and
\[
\boxed{w_{\min}(A_{p,q})=W_{p,q}(s_0,t_0)\sqrt{\frac{n}{k_0(n-k_0)}}.}
\tag{4}
\]

Every minimizing unit normal is exactly
\[
\boxed{\pm\frac{\mathbf1_S-(|S|/n)\mathbf1}{\sqrt{|S|(n-|S|)/n}}}
\tag{5}
\]
for one of the specified cuts; no other minimizing normals exist. In the balanced phase the number of unoriented minimizing lines is
\[
\frac12\sum_{\substack{s,t\ \text{satisfying }(3)}}\binom ps\binom qt.
\]
Finally, for every fixed \(p\ge2\),
\[
\boxed{w_{\min}(A_{p,q})\sim\frac{2(2^p-1)2^q}{\sqrt{p+q}}\qquad(q\to\infty).}
\tag{6}
\]
This is a sharp, all-aspect-ratios transition at total graph order fifteen.

## Assumptions and scope
All sums are Minkowski sums; every nonempty subset meeting both graph color classes contributes once. The omitted singleton simplices add a fixed translation and do not affect width. The graph is genuinely bipartite with \(p,q\ge2\); the star boundary \(p=1\) is not part of the claimed new classification. The Euclidean metric is intrinsic to the affine hull and has no arbitrary affine rescaling. Width in a unit direction \(u\perp\mathbf1\) is \(h_A(u)+h_A(-u)\).

## Proof
**1. Reduction to centered cuts, with equality.** A simplex \(\Delta_T\) has width \(\max_{i\in T}u_i-\min_{i\in T}u_i\). Minkowski width is the sum of these widths. Sort the coordinates of any nonconstant \(u\perp\mathbf1\), let \(\delta_j>0\) be its nonzero consecutive level gaps, and let \(S_j\) be the corresponding nested upper-level sets. With \(v_S=\mathbf1_S-(|S|/n)\mathbf1\), the exact identities are
\[
u=\sum_j\delta_jv_{S_j},\qquad
\operatorname{width}(A_{p,q},u)=\sum_j\delta_j W(S_j).
\]
Here \(W(S)\) counts tube simplices meeting both \(S\) and its complement. Since \(\|u\|_2\le\sum_j\delta_j\|v_{S_j}\|_2\),
\[
\frac{\operatorname{width}(A_{p,q},u)}{\|u\|_2}
\ge\min_j\frac{W(S_j)}{\|v_{S_j}\|_2}.
\]
The centered vectors of two distinct nested proper cuts are not positively collinear, so equality in the Euclidean triangle inequality forces exactly one nonzero level gap. Therefore every minimizing direction has two levels, and only centered cut directions can minimize.

**2. Exact tube counting.** There are \(B\) nonempty mixed-color subsets in total. Exactly \((2^s-1)(2^t-1)\) are wholly contained in \(S\), and exactly \((2^{p-s}-1)(2^{q-t}-1)\) are wholly contained in its complement. Consequently \(W(S)=W_{p,q}(s,t)\). Since \(\|v_S\|_2=\sqrt{k(n-k)/n}\), this proves (1).

**3. Center cuts are uniquely balanced at fixed cardinality.** For fixed \(k=s+t\), expanding the preceding expression gives
\[
W_{p,q}(s,t)=2^n-2^p-2^q-2^k-2^{n-k}-1
+g_p(s)+g_q(t),
\quad g_a(x)=2^x+2^{a-x}.
\tag{7}
\]
Each \(g_a(x)\) is strictly decreasing up to the midpoint and strictly increasing after it, attaining its minimum exactly at \(x\in\{\lfloor a/2\rfloor,\lceil a/2\rceil\}\). If \(k=\lfloor n/2\rfloor\) or \(\lceil n/2\rceil\), both midpoint minima can be attained simultaneously (choosing opposing halves when both \(p,q\) are odd). They give exactly the cut types in (3). No other cut at those total cardinalities ties.

**4. Rigorous uniform large-order comparison.** By complement symmetry assume \(1\le k\le\lfloor n/2\rfloor\), and set \(f(k)=k(n-k)\), \(k_0=\lfloor n/2\rfloor\), \(f_0=f(k_0)\). The balanced candidate has width at most \(B\sqrt{n/f_0}\). For any cut, dividing the two excluded counts by \(B\), and using \(p,q\ge2\), gives
\[
\frac{W(S)}B\ge1-\frac{16}{9}\bigl(2^{-k}+2^{-(n-k)}\bigr).
\tag{8}
\]
Indeed \((1-2^{-p})^{-1}(1-2^{-q})^{-1}\le16/9\). For \(k=1\), direct counting gives \(W(S)/B\ge1/2\). Hence a singleton is worse than the balanced candidate whenever \(f_0>4(n-1)\), which holds for \(n\ge128\).

For \(k=2\), (8) gives \(W/B>1/2\) at \(n\ge128\), while \(\sqrt{f(2)/f_0}<1/4\). For \(3\le k\le n/8\), (8) yields \(W/B>3/4\) whereas
\[
\sqrt{f(k)/f_0}\le\sqrt{\frac{n^2}{2(n^2-1)}}<3/4.
\]
Finally, for \(n/8<k<k_0\),
\[
\frac{16}{9}\bigl(2^{-k}+2^{-(n-k)}\bigr)
\le\frac{32}{9}2^{-n/8}<\frac2{n^2},
\tag{9}
\]
while \(f_0-f(k)\ge1\) implies
\[
\sqrt{f(k)/f_0}\le1-\frac{f_0-f(k)}{2f_0}\le1-\frac2{n^2}.
\tag{10}
\]
The last strict inequality in (9) holds at \(n=128\), since \(1/18432<1/8192\), and remains true as \(n\) grows: \(n^2 2^{-n/8}\) decreases for \(n\ge128\). Thus every noncentral cut is strictly wider than the balanced candidate for every \(n\ge128\). Step 3 then classifies all equality cases.

**5. The complete finite remainder.** The included `verify.py` exhaustively checks **every** integer \(4\le n\le127\), \(2\le p\le q\), \(p+q=n\), and every pair \((s,t)\) with \(0\le s\le p\), \(0\le t\le q\) and \(1\le s+t\le n-1\). Squared widths differ only by the positive common factor \(n\); it compares exact integers \(W(s,t)^2 k'(n-k')\) and \(W(s',t')^2 k(n-k)\), and compares complete sets of minimizers with (2) and (3). The certificate checks 3,906 bipartitions and 5,870,718 cut-parameter profiles, without randomization or floating-point tolerances. This proves the small phase and fills the complete range up to 127. Combined with Step 4 it proves the theorem for every permitted \(p,q\).

For (6), fixing \(p\) and letting \(q\to\infty\) makes both excluded balanced mixed-subset fractions \(o(1)\), so \(W(s_0,t_0)\sim B\sim(2^p-1)2^q\), and \(\sqrt{n/f_0}\sim2/\sqrt n\).

## Verification
Run `python verify.py` in the directory containing this result. The checker explicitly iterates all finite parameter tuples, independently counts crossing connected subsets on small boards, and checks the rational inequalities initiating the analytic tail. Its observed output was

`BICLIQUE_ASSOCIAHEDRON_WIDTH_CHECKS_PASSED finite_profiles=3906 exact_cut_profiles=5870718 exact_cross_comparisons=5866812 independent_tube_cut_tests=1438 bound_checks=3`

The large-order proof is the symbolic argument in Step 4. The finite certificate covers all smaller orders; it is not presented as evidence for unexamined orders.

## Relationship to prior work
Postnikov's Minkowski-sum realization and the graphical nested-fan framework of Padrol, Pilaud, and Poullot supply the standard polytope construction and supporting-face formulas. Cardinal, Pournin, and Valencia-Pabon examine graph associahedra of bicliques but calculate the **graph distance on the one-skeleton**, not Euclidean support width. A published result on the same standard biclique realization determines the **inradius and closest facets**, a different extremal problem; its conclusion does not entail a minimum directional width or its minimizers. A separate graph-zonotope inradius result uses a coarea reduction for edge segments, supplying a related technique but not the tube-subset counts or sharp phase classification here.

The previously studied star boundary \(p=1\) has an analogous minimum-width crossover at total graph order fifteen, but a star is not a genuine biclique \(p,q\ge2\). The star theorem cannot determine the genuine-biclique cut weights, competition among all color splits, or the universality of the transition across arbitrary aspect ratios.

## Limitations
The width and classification are specific to the unit tube-simplex Minkowski realization. General affine realizations with the same graph-associahedron face lattice may have different widths. The theorem excludes \(p=1\), noncomplete bipartite graphs, weighted tube sums, and alternative norms. A possible equivalence under older terms such as generalized-permutohedron thickness remains a historical-priority risk; no independent literature-priority certification is claimed.

## References
1. Jean Cardinal, Lionel Pournin, and Mario Valencia-Pabon, *Diameter estimates for graph associahedra*, arXiv:2106.16130, first submitted 2021-06-30, Annals of Combinatorics 26 (2022), 873–902.
2. Arnau Padrol, Vincent Pilaud, and Germain Poullot, *Deformation cones of graph associahedra and nestohedra*, arXiv:2109.09200, first submitted 2021-09-19, European Journal of Combinatorics 107 (2023), 103594.
3. Alexander Postnikov, *Permutohedra, associahedra, and beyond*, arXiv:math/0507163, International Mathematics Research Notices (2009), 1026–1106.
4. Published mathematical result, *Singleton facets determine the inball of every genuine complete-bipartite graph associahedron*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-singleton-facets-determine-the-inball-of-every-genuine-complete--472aa0e35fff.
5. Published mathematical result, *Euclidean inradius of weighted graphical zonotopes is a cut expansion constant*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-euclidean-inradius-of-weighted-graphical-zonotopes-is-a-cut-expa--cb1eceb082ab.
