# A logarithmic edge-metric crossover for complete-bipartite Hansen polytopes

## Finding
Let \(F_{p,q}(z)\) count the undirected edges of the canonical Euclidean Hansen polytope \(H_{p,q}\) by their squared Euclidean lengths. For all integers \(2\le p\le q\),
\[
\boxed{F_{p,q}(z)=(p2^p+q2^q)z+2(1+z^4)((1+z)^p-1)((1+z)^q-1)+2^pz^{p+4}+2^qz^{q+4}.}
\]
Consequently, the number of edges is
\[
|\mathcal E_{p,q}|=p2^p+q2^q+4(2^p-1)(2^q-1)+2^p+2^q.
\]
The largest squared edge length is \(p+q+4\), attained by exactly two edges. The squared diameter of the entire vertex set is \(4(q+1)\), attained by an antipodal pair in every largest color class, and is strictly larger than the squared length of every edge.

Choose an edge uniformly at random and denote its squared Euclidean length by \(X_{p,q}\). Along every sequence of integers \(q\to\infty\), \(2\le p\le q\), for which \(2^p/q\to c\in[0,\infty]\),
\[
\boxed{\frac{X_{p,q}}{p+q}\Longrightarrow \frac{1}{1+4c}\delta_0+\frac{4c}{1+4c}\delta_{1/2}.}
\]
For \(c=\infty\) this means \(\delta_{1/2}\). In particular, when \(2^p/q\) tends to a finite positive constant, both the unit-length edges and edges of squared length asymptotic to \((p+q)/2\) occupy positive limiting proportions. The crossover is on the scale \(p\asymp\log_2q\).

## Assumptions and scope
The graph is the complete bipartite graph \(K_{p,q}\), with disjoint color classes \(L,R\) of integer sizes \(2\le p\le q\). A stable set is a subset of one color class, with the empty set counted once. Use standard orthonormal coordinates in \(\mathbb R^{p+q+1}\), not a differently rescaled but affinely equivalent Hansen realization:
\[
H_{p,q}=\operatorname{conv}\{v_{\varepsilon,S}=\varepsilon(1,\mathbf1_S):\varepsilon\in\{+1,-1\},\ S\subseteq L\text{ or }S\subseteq R\}.
\]
All claimed edges are one-dimensional faces (not merely segments joining vertices), counted as unordered pairs. In the generating polynomial, \(z\) marks the *squared* length and coincidences of exponents combine automatically. The asymptotic statement holds for every integer sequence satisfying the ratio limit, including \(c=0\) and \(c=\infty\).

## Proof
**Step 1: complete edge classification.** Put \(P=\operatorname{STAB}(K_{p,q})=\operatorname{conv}([0,1]^L\times\{0\}\cup\{0\}\times[0,1]^R)\). Its vertices are the indicator vectors of stable sets. Edges on the same sign layer of the twisted prism are exactly edges of \(P\). Each of the two coordinate cubes is a face of \(P\), so within one class the edges join subsets differing in exactly one element. For two nonempty stable sets in different classes, an objective positive on their selected coordinates, negative on the remaining coordinates, and rescaled to give their supports equal positive value exposes exactly those two vertices; thus all such cross-class pairs are edges. The empty set is adjacent only to singleton stable sets. The same-layer edge classification follows.

For opposite sign layers, a segment joining \(v_{+,S}\) to \(v_{-,T}\) is exposed as an edge precisely when some linear functional \(a\cdot x\) on \(P\) has *unique* maximizer \(\mathbf1_S\) and *unique* minimizer \(\mathbf1_T\). Indeed choose the coefficient on the leading coordinate so that the maximum on the plus layer equals the maximum of the opposite functional on the minus layer. The strictness of both extrema is necessary and sufficient for the exposed face to have exactly these two vertices.

If \(S,T\) are nonempty and belong to different color classes, prescribe large positive scores on the elements of \(S\), large negative scores on the elements of \(T\), and sufficiently small scores on the remaining coordinates: the specified maxima and minima are unique. If \(S,T\) belong to the same class, unique maximum/minimum within its full cube require them to be complementary subsets of that entire class; conversely one can choose strict positive/negative signs within that class and sufficiently small scores on the other class so that these extrema are unique. This also covers the empty-versus-full cases: choose appropriately dominant negative or positive scores within the full class and strictly signed smaller scores on the other class. If one set is empty and the other is a proper subset of a class, the empty set cannot be the unique maximum or minimum while the proper subset is the opposite extremum. Hence the opposite-layer classification is exhaustive.

**Step 2: lengths and multiplicities.** Each cube of dimension \(p\) has \(p2^{p-1}\) edges; there are two signs, and similarly for dimension \(q\). This yields \((p2^p+q2^q)z\). On each sign layer, cross-class pairs of subset sizes \(k\ge1\), \(\ell\ge1\) contribute \(2\binom pk\binom q\ell z^{k+\ell}\). Across signs the corresponding pairs have squared length \(4+k+\ell\) and contribute \(2\binom pk\binom q\ell z^{4+k+\ell}\). Finally for a color class of size \(m\in\{p,q\}\), every ordered complementary subset pair \((S,S^c)\) determines one opposite-sign undirected edge of squared length \(m+4\), and there are \(2^m\) such edges. Summing binomial coefficients gives the displayed polynomial and its value at \(z=1\).

Cross-class edges have maximum squared length \(p+q+4\), with exactly the two opposite-sign pairs joining the full left set to the full right set, in opposite orientations. All cube and within-class complementary edges are shorter because \(p,q\ge2\). Every vertex lies at distance at most \(\sqrt{1+q}\) from the origin, and two antipodal full-class vertices realize distance \(2\sqrt{1+q}\); this proves the diameter claim and its strict edge gap.

**Step 3: the logarithmic limit.** Write the numbers of unit cube edges, cross-class edges, and complementary opposite-layer edges as
\[
C_{p,q}=p2^p+q2^q,\quad M_{p,q}=4(2^p-1)(2^q-1),\quad B_{p,q}=2^p+2^q.
\]
If \(2^p/q\to c<\infty\), then \(p=O(\log q)\), so \(p2^p/(q2^q)\to0\); consequently \(C_{p,q}/(q2^q)\to1\), \(M_{p,q}/(q2^q)\to4c\), \(B_{p,q}/(q2^q)\to0\). If \(c=\infty\), the cross-class edges dominate: \(C_{p,q}/M_{p,q}\to0\) and \(B_{p,q}/M_{p,q}\to0\), since \(p2^p/(2^{p+q})\le p/2^q\to0\) and \(q2^q/(2^{p+q})=q/2^p\to0\).

Conditioned on a uniformly selected cross-class edge, its endpoint set sizes are independent \(\operatorname{Binomial}(p,1/2)\) and \(\operatorname{Binomial}(q,1/2)\), each conditioned to be nonzero; its squared length is their sum or their sum plus four, each with probability one half. If cross-class edges carry nonvanishing limiting mass, then \(p\to\infty\) and \(q\to\infty\). Binomial concentration yields \(X_{p,q}/(p+q)\to1/2\) conditionally on that class. Cube edges have squared length one, and complementary edges have vanishing probability. The stated two-atom weak limit follows.

## Verification
A standalone exact integer-arithmetic checker, `verify_hansen.py`, constructs every vertex, derives common-tight-facet intersections from the complete clique-inequality system, and independently classifies edges by the dimension of the resulting minimal faces. It compares every pairwise adjacency decision and the full squared-length histogram against the closed formula. It also verifies the maximum edge length and its multiplicity, for twenty explicit size pairs through \(p=q=6\), totaling 106,380 unordered vertex pairs. Running the script prints `HANSEN_EDGE_METRIC_EXACT_PASS configurations=20 tested_pairs=106380`. This finite test is supporting evidence only: the all-size theorem and asymptotic result are proved above.

## Relationship to prior work
Hansen's original construction (1977) uses an affinely equivalent sign-coordinate realization; Euclidean lengths depend on that choice, so the realization used here is stated explicitly. Aprile–Cevallos–Faenza (2017), Section 3.2, studies the standard twisted-prism presentation and face-number trade-offs. Aliniaeifard–Benedetti–Bergeron–Li–Saliola (2018), especially its 1-skeleton theorems, treats stable-set polytopes before the twisted-prism lift; it does not assert this lift's metric edge distribution. Freij–Henze–Schmitt–Ziegler (2012/2013) studies Hansen face-number bounds for split graphs; complete bipartite graphs with both parts nontrivial are not split graphs. The present claim is the exact *Euclidean length-weighted* 1-skeleton of a bipartite Hansen family and the resulting logarithmic edge-length phase limit. The general construction and elementary geometry of exposed edges are prior ingredients, not asserted to be new.

## Limitations
The result assumes the standard orthonormal twisted-prism embedding; it is not invariant under arbitrary affine changes. Its metric theorem concerns two nonempty graph color classes and integer parameters \(2\le p\le q\), not arbitrary graph families. The limit classifies weak convergence of rescaled squared lengths but does not give second-order fluctuations within the long-edge class. The mathematical proof is self-contained; historical novelty is provisional because unindexed papers or a stronger general graph result could contain an equivalent characterization. Independent mathematical verification has not been performed.

## References
1. A. B. Hansen, *On a Certain Class of Polytopes Associated with Independence Systems*, Mathematica Scandinavica 41 (1977), 225–241. https://doi.org/10.7146/math.scand.a-11716
2. M. Aprile, A. Cevallos, Y. Faenza, *On 2-Level Polytopes Arising in Combinatorial Settings*, arXiv:1702.03187, first public 2017-02-10, Section 3.2. https://arxiv.org/abs/1702.03187
3. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, F. Saliola, *Stable Set Polytopes and Their 1-Skeleta*, arXiv:1804.00360, first public 2018-04-02. https://arxiv.org/abs/1804.00360
4. R. Freij, M. Henze, M. W. Schmitt, G. M. Ziegler, *Face Numbers of Centrally Symmetric Polytopes Produced from Split Graphs*, arXiv:1201.5790 (2012), Electronic Journal of Combinatorics 20(2) (2013), P32. https://arxiv.org/abs/1201.5790
