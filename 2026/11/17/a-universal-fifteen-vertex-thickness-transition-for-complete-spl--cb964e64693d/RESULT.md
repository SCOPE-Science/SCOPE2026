# A universal fifteen-vertex thickness transition for complete split graph associahedra

## Finding

Let \(c,m\ge2\), \(n=c+m\), and let \(G=K_c\vee\overline{K_m}\) be the complete split graph with a clique of \(c\) vertices and an independent class of \(m\) vertices. In \(\mathbb R^n\), set
\[
P_{c,m}=\sum_{\substack{\varnothing\ne I\subseteq V(G)\\G[I]\text{ connected}}}\Delta_I,
\qquad \Delta_I=\operatorname{conv}\{e_i:i\in I\}.
\]
All widths below are intrinsic Euclidean widths in the hyperplane parallel to \(H=\{u:\sum_i u_i=0\}\). Put
\[
B=(2^c-1)2^m,\quad h=\lfloor n/2\rfloor,\quad q=\lfloor m/2\rfloor,
\quad T=B-2^h-2^{n-h}+2^q+2^{m-q}.
\]
Then the exact minimum width is
\[
\boxed{\operatorname{width}_{\min}(P_{c,m})=
\begin{cases}
\dfrac B2\sqrt{\dfrac n{n-1}},&4\le n\le14,\\[6pt]
T\sqrt{\dfrac n{h(n-h)}},&n\ge15.
\end{cases}}
\]
There is no tie between these regimes. For \(n\le14\), every minimizing unoriented normal is the centered indicator of a singleton in the independent class, and there are exactly \(m\) such directions. For \(n\ge15\), every minimizing unoriented normal is the centered indicator of a subset \(A\subset V(G)\) for which
\[
|A|\in\{h,n-h\},\qquad
|A\cap\overline{K_m}|\in\{q,m-q\}.
\]
Conversely every such subset minimizes. In particular **both the entire vertex set and its independent class are as evenly bisected as parity allows**. The number of unoriented minimizing normals is
\[
\frac12\sum_{\substack{a+b\in\{h,n-h\}\\b\in\{q,m-q\}\\0\le a\le c}}\binom ca\binom mb,
\]
where each *distinct* admissible pair \((a,b)\) is included once.

## Assumptions and scope

The graph is labelled but only the class sizes matter. The clique and independent class each have at least two vertices; this excludes the star and complete-graph boundary families. Every connected induced vertex set contributes one **unscaled** coordinate simplex. Singletons are retained but have zero directional width. The ambient metric is the standard Euclidean metric, restricted to the affine hull. We classify all minimizing directions modulo sign; vectors parallel to \((1,\ldots,1)\) are ignored because they are orthogonal to the affine hull.

## Proof

**1. Reduction to two-level cuts.** Order the coordinates of a nonzero \(u\in H\) as \(u_{\pi(1)}\le\cdots\le u_{\pi(n)}\). Define gaps \(d_j=u_{\pi(j+1)}-u_{\pi(j)}\ge0\) and the centered indicator vectors \(v_j=\mathbf1_{\{\pi(j+1),\ldots,\pi(n)\}}-\frac{n-j}{n}\mathbf1\), which have squared norms \(j(n-j)/n\). The support-width identity for a simplex gives
\[
w(P_{c,m},u)=\sum_{j=1}^{n-1}d_j C(A_j),\qquad
u=\sum_{j=1}^{n-1}d_jv_j,
\]
where \(A_j=\{\pi(1),\ldots,\pi(j)\}\) and \(C(A)\) counts connected induced sets meeting both \(A\) and its complement. Consequently
\[
\frac{w(P_{c,m},u)}{\|u\|}\ge
\min_{\varnothing\ne A\subsetneq V}\frac{C(A)}{\sqrt{|A|(n-|A|)/n}}.
\]
The inequality follows from the triangle inequality for \(\sum_jd_jv_j\). Equality in that triangle inequality requires a single nonzero gap: distinct centered nested cut indicators are not positive scalar multiples. Thus *all* minimizing normal vectors are two-level centered cut indicators, and the displayed cut minimum is exact.

**2. Exact tube count.** Let \(A\) contain \(a\) clique vertices and \(b\) independent vertices, and set \(k=a+b\). The connected subsets other than independent-class singletons are exactly the subsets meeting the clique. Their total number, including singletons in the clique, is \(B\); the number lying in \(A\) is \((2^a-1)2^b\), and the number lying in the complement is \((2^{c-a}-1)2^{m-b}\). Therefore
\[
C(a,b)=B-(2^a-1)2^b-(2^{c-a}-1)2^{m-b}
=B-2^k-2^{n-k}+2^b+2^{m-b}.
\]
For fixed \(k\), the last two terms are minimized precisely when \(b\) lies as close to \(m/2\) as allowed by \(0\le b\le m\) and \(0\le k-b\le c\). For central cut sizes \(k\in\{h,n-h\}\), both nearest integers \(q,m-q\) that yield admissible \(a=k-b\) are attained. Hence the smallest central crossing count is \(T\), with exactly the central equality cases stated above.

**3. Exact finite base, including the sharp switch.** For every \(4\le n\le63\), every \(2\le c\le n-2\), and every \(0\le a\le c\), \(0\le b\le m\) with \(0<a+b<n\), the file `verify.py` checks the following integer inequality:
\[
C(a,b)^2D_\star\ge C_\star^2 k(n-k),
\]
where \((C_\star,D_\star)=(B/2,n-1)\) for \(n\le14\) and \((C_\star,D_\star)=(T,h(n-h))\) for \(n\ge15\). It checks equality **if and only if** the claimed singleton or doubly-balanced cut condition holds. These are 750,605 exhaustive cut-type checks over 1,830 parameter profiles, all in exact integer arithmetic; there is no sampling or floating-point comparison. The formula is therefore proved for the entire finite range, including its strict transition.

**4. Uniform tail.** Now let \(n\ge64\). Complementation permits \(1\le k\le h\). Write \(L=h(n-h)=\lfloor n^2/4\rfloor\). Since \(c\ge2\), \(B\ge3\cdot2^{n-2}\). From the expression above, for \(2\le k\le h\),
\[
\frac{C(a,b)}B\ge1-\frac43(2^{-k}+2^{k-n}).\tag{1}
\]
The central candidate has \(T\le B\). We prove that for every \(1\le k<h\),
\[
\frac{C(a,b)}B>\sqrt{\frac{k(n-k)}L},\tag{2}
\]
which makes every noncentral cut strictly wider than even the upper bound \(B\sqrt{n/L}\) for the central width.

For \(k=1\), a singleton independent vertex contributes exactly \(B/2\) crossing tubes, while a clique singleton contributes \(2^{n-1}>B/2\). Since \(L>4(n-1)\) when \(n\ge64\), (2) holds. For \(2\le k\le3\), (1) gives \(C/B>2/3-(4/3)2^{-32}>0.66\), whereas \(\sqrt{k(n-k)/L}\le\sqrt{12n/(n^2-1)}<0.44\). For \(4\le k\le n/4\), (1) gives \(C/B>11/12-(4/3)2^{-32}>0.91\), whereas \(\sqrt{k(n-k)/L}\le\sqrt{3n^2/[4(n^2-1)]}<0.87\). Finally, for \(n/4<k<h\), (1) gives \(C/B\ge1-(8/3)2^{-n/4}>1-2/n^2\), using \(2^{n/4}>(4/3)n^2\) for all \(n\ge64\). Since \(L-k(n-k)\ge1\), the competing norm ratio is at most \(\sqrt{1-4/n^2}\le1-2/n^2\). This proves (2) in every case.

Only central cuts remain, whose exact minimizers were classified in step 2. Combined with step 3, this proves the formula and all equality cases for every \(c,m\ge2\).

## Verification

The bundled standalone `verify.py` uses only Python 3 and built-in arbitrary-precision integers. Execute `python verify.py` in the directory containing that file. It checks all 1,830 parameter profiles of total order 4 through 63, 750,605 admissible cut types and their exact equality conditions. It independently enumerates connected subsets for 392 additional small-order cut types to verify the symbolic crossing-count formula. The expected status line is `SPLIT_GRAPH_WIDTH_PASS profiles=1830 exact_cuts=750605 min_cuts=4116 direct_tube_tests=392 threshold_n=15`. Beyond order 63 the proof is the analytical estimate in step 4, not extrapolation from a finite table.

## Relationship to prior work

Cardinal, Pournin and Valencia-Pabon study the *skeleton graph diameter* of complete split graph associahedra and describe their broom-search-tree model. Their metric is the minimum number of edge rotations, not Euclidean thickness of a specified realization. Padrol, Pilaud and Poullot establish the nested fan and the unscaled tube-simplex Minkowski realization, but their deformation-cone results do not determine this width threshold. Related exact width results for simplex-sum stellohedra, complete-bipartite graph associahedra and complete-graph associahedra concern different tube families: the present two-parameter split graph with \(c,m\ge2\) is none of these. Their common fifteen-vertex threshold neither supplies the split-graph cut count nor the double-balance equality classification.

## Limitations

The formula is specific to the unit tube-simplex realization, not to arbitrary affine-equivalent realizations or arbitrary deformations with the same face lattice. It excludes \(c=1\) and \(m=1\), for which separate boundary-family results are available. The historical-priority comparison covers inspected primary papers and accessible research records, not every unpublished or inaccessible source. Independent mathematical validation has not been performed.

## References

- J. Cardinal, L. Pournin and M. Valencia-Pabon, *Diameter estimates for graph associahedra*, arXiv:2106.16130, first public version June 30, 2021. https://arxiv.org/abs/2106.16130
- A. Padrol, V. Pilaud and G. Poullot, *Deformation cones of graph associahedra and nestohedra*, arXiv:2109.09200, first public version September 19, 2021, especially Theorem 2.2. https://arxiv.org/abs/2109.09200
