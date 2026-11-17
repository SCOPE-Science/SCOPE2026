# Exact Euclidean distance spectrum of caracol unit-flow polytopes

## Finding

For every integer \(n\ge3\), let \(G_n\) be the caracol directed graph on \(1,\ldots,n+1\), with consecutive edges \((i,i+1)\), source shortcuts \((1,i)\) for \(3\le i\le n\), and sink shortcuts \((i,n+1)\) for \(2\le i\le n-1\). Its unit source-to-sink flow polytope \(\mathcal F_n\) is realized in the standard Euclidean edge-coordinate space; the distances below are **not** distances after an arbitrary affine equivalence to an order polytope.

Put \(L=n-1\), let \(H_L(z)=\sum_{\{u,v\}}z^{\|u-v\|_2^2}\), where the sum is over unordered **distinct** vertices of \(\mathcal F_n\), and write \(\binom a2=a(a-1)/2\). The full squared-distance histogram has the following closed, \(O(n)\)-term form:

\[
\begin{aligned}
H_L(z)={}&\sum_{d=1}^{L-1}(L-d)\bigl(z^4+2z^{d+2}\bigr)\\
&+2\sum_{a=1}^{L-2}\binom{L-a}{2}\bigl(z^{a+2}+z^{a+4}\bigr)\\
&+2\sum_{d=2}^{L-1}(d-1)(L-d)z^{d+4}\\
&+3\sum_{g=2}^{L-2}(g-1)\binom{L-g}{2}z^{g+4}.
\end{aligned}
\]

Empty sums vanish. This describes all distance values **and their exact multiplicities**, with possible collisions in powers of \(z\) automatically added. There are \(M=L(L+1)/2\) vertices, and \(H_L(1)=\binom M2\). The exact mean squared Euclidean distance of two uniformly selected distinct vertices is

\[
\frac{H_L'(1)}{\binom M2}=\frac{2(3L^2+35L+18)}{15(L+2)}.
\]

For \(n=3\), the squared diameter is \(4\) and there is one diametral pair. For every \(n\ge4\),

\[
\operatorname{diam}(\mathcal F_n)^2=n+2,
\]

and exactly \(2(n-3)\) unordered pairs attain it. They consist, for each \(3\le t\le n-1\), of the pair of paths \([2,n]\) and \([t,t]\), and the pair of paths \([2,t]\) and \([t,n]\), where \([i,j]\) denotes the directed route \(1\to i\to i+1\to\cdots\to j\to n+1\). The diameter graph on polytope vertices is thus one star with \(n-3\) leaves, together with \(n-3\) isolated edges and further isolated vertices.

If \(U_n,V_n\) are distinct uniformly sampled vertices and \(D_n^2=\|U_n-V_n\|_2^2\), then

\[
\frac{D_n^2}{n-1}\ \xrightarrow{\mathrm d}\ \operatorname{Beta}(2,3),\qquad
\sup_{x\in\mathbb R}\left|\Pr\left(\frac{D_n^2}{n-1}\le x\right)-F(x)\right|=O(n^{-1}),
\]

where \(F(x)=0\) for \(x\le0\), \(F(x)=6x^2-8x^3+3x^4\) for \(0<x<1\), and \(F(x)=1\) for \(x\ge1\). The continuous density is \(12x(1-x)^2\) on \((0,1)\). The classical beta law for a sum of Dirichlet spacings is used as a step; it is **not** independently claimed as a new probability distribution.

## Assumptions and scope

The graph has exactly the specified edges and no parallel edges. A unit flow is nonnegative, with net flow \(+1\) at vertex \(1\), net flow \(-1\) at vertex \(n+1\), and net flow zero at every intermediate vertex. All vector norms are the standard ambient Euclidean norms of edge-flow coordinates. The polynomial is for unordered distinct **vertices**, not uniform interior volume points and not distances in the one-skeleton graph metric. The graph is acyclic, so its unit-flow vertices are precisely the indicators of directed source-to-sink paths. These paths are uniquely indexed by \((i,j)\) with \(2\le i\le j\le n\). All assertions hold over the real numbers and for every integer \(n\ge3\).

## Proof

**Vertex parametrization and the distance identity.** Since the graph is acyclic, every unit flow is a convex combination of source-to-sink path indicators: repeatedly extract a path from any positive flow until all flow is exhausted. Conversely each path indicator is extreme: its coordinates are zero off that path, and the flow constraints force the value one on each of its path edges. Every path is \([i,j]\) as above. The edge set of its indicator consists of the distinct source edge \((1,i)\), distinct sink edge \((j,n+1)\), and the chain edges \((k,k+1)\) for \(i\le k<j\). Hence for two paths \([i,j]\) and \([k,\ell]\),

\[
\left\|p_{i,j}-p_{k,\ell}\right\|_2^2
=\bigl|[i,j)\mathbin\triangle[k,\ell)\bigr|
+2\mathbf1_{i\ne k}+2\mathbf1_{j\ne\ell},
\]

with \(\bigl|[i,j)\mathbin\triangle[k,\ell)\bigr|\) the number of integer chain steps in the symmetric difference. This follows from \((1-0)^2=1\) independently in each edge coordinate and disjoint types of edges. Write the \(L\) possible endpoints as \(0,1,\ldots,L-1\) in what follows, which only translates the indices.

**Complete disjoint-pair classification.** For any pair of different intervals, the multiset of their four endpoints has exactly two, three, or four different values. If the four endpoint values are \(t_1<t_2<t_3<t_4\), all three possible unordered pairings into two intervals have chain symmetric-difference length \(g=(t_2-t_1)+(t_4-t_3)\); both source and sink edges differ, so the squared distance is \(g+4\). Fixing \(g\) gives \(g-1\) choices of positive outer gaps, and \(\binom{L-g}{2}\) choices of the middle gap and translation. This supplies the last line of \(H_L\), including the factor three.

With three distinct endpoints \(t_1<t_2<t_3\), write \(a=t_2-t_1\), \(c=t_3-t_2\). The six unordered path pairs using those three values exactly are

\[
\begin{array}{lll}
([t_1,t_1],[t_2,t_3]):c+4,&([t_2,t_2],[t_1,t_3]):a+c+4,&([t_3,t_3],[t_1,t_2]):a+4,\\
([t_1,t_2],[t_1,t_3]):c+2,&([t_1,t_2],[t_2,t_3]):a+c+4,&([t_1,t_3],[t_2,t_3]):a+2.
\end{array}
\]

Here the values after each colon are squared distances. For fixed \(a\), summing the remaining positive gap \(c\) and translation gives \(\binom{L-a}{2}\), and the symmetrical \(c\) terms double this contribution. For fixed \(d=a+c\), there are \(d-1\) gap splits and \(L-d\) translations. These are exactly the second and third lines of \(H_L\).

With exactly two endpoint values \(t_1<t_2\), the three different pairs of paths \([t_1,t_1]\), \([t_1,t_2]\), \([t_2,t_2]\) yield squared distances \(t_2-t_1+2\), \(t_2-t_1+2\), and \(4\). There are \(L-d\) endpoint pairs of gap \(d\), giving the first line. The cases are exhaustive and disjoint, so the polynomial is exact. Substitution at \(z=1\) and differentiation yield the asserted vertex-pair count and mean; the sum simplifies to \(L(L-1)(L+1)(3L^2+35L+18)/60\).

**Diameter and rigidity.** For four distinct endpoints \(g\le L-2\), so squared distance is at most \(L+2\). For three distinct endpoints, the greatest possible value is \(a+c+4\le L+3\). For two distinct endpoints, squared distance is at most \(\max\{4,L+1\}\). For \(L\ge3\), the maximum is therefore \(L+3=n+2\), and equality can occur only in the two \(a+c+4\) configurations with \(t_1=0\), \(t_3=L-1\), and intermediate \(t_2\) arbitrary and strictly between. There are \(L-2=n-3\) choices of intermediate index, yielding the two stated pairs per index. For \(L=2\), direct inspection gives squared diameter four. A diametral pair of arbitrary points of a polytope must consist of vertices: if either point were a nontrivial convex combination of distinct vertices, strict convexity of squared Euclidean distance in that point would yield a vertex at strictly greater distance. The diameter statements therefore apply to the full polytope, not just its vertex set.

**Quantitative limit.** For each interval, sample two independent uniforms on \([0,1]\) and sort them. Independent intervals produce four independent original endpoints; if these four uniforms are sorted into \(T_1<T_2<T_3<T_4\), the Lebesgue measure of the symmetric difference is always \((T_2-T_1)+(T_4-T_3)\), regardless of the pairing. The five spacings including the boundary spacings have the uniform \(\operatorname{Dirichlet}(1,1,1,1,1)\) law, so this sum has \(\operatorname{Beta}(2,3)\) distribution.

To couple to the discrete model, quantize the continuous endpoints with \(\lfloor LU\rfloor\) and sort. The resulting discrete interval law differs in total variation by exactly \((L-1)/(L(L+1))\) from the uniform law on weakly ordered endpoint pairs; thus two intervals cost at most \(2/L\) in total variation. Quantization changes the symmetric-difference measure by at most \(4/L\), and the two source/sink corrections contribute at most \(4/L\) to the normalized squared distance. Conditioning two uniformly sampled discrete paths to be distinct changes their joint law by at most \(1/M\) in total variation. The \(\operatorname{Beta}(2,3)\) density is bounded by \(16/9\); shifting its argument by \(8/L\), together with these total-variation estimates, proves Kolmogorov error \(O(1/L)=O(1/n)\).

## Verification

The standalone `verify_caracol.py` reconstructs the actual directed graph's edge indicators independently, enumerates their symmetric differences for every order \(3\le n\le16\), and compares each entire squared-distance histogram with the displayed polynomial. It checks the histogram's total mass, its rational mean, the complete labelled diametral-pair equality locus, and asymptotic-distribution CDF discrepancies at five larger dimensions. The exact exhaustive portion covers 25,704 unordered path pairs and 132 distinct per-order coefficient levels. The analytical proof, rather than finite enumeration, establishes the theorem for every dimension.

To reproduce, execute `python verify_caracol.py` with standard Python 3. The program uses no external modules, and all integer counts and rational expectations are checked exactly.

## Relationship to prior work

Benedetti, González D'León, Hanusa, Harris, Khare, Morales, and Yip introduced the caracol flow-polytope family and studied its lattice-normalized volumes and related enumeration. Jang and Kim proved caracol Ehrhart-like volume identities. Their graph and flow definitions agree with the objects here, but the present result concerns the **ambient Euclidean metric on edge-flow coordinates**, not normalized volume. The known affine equivalence to the rectangle order polytope does not determine this metric unless the affine map is proved to be an isometry; no such metric implication is used. Related published findings on Euclidean inballs of complete directed-flow polytopes and on Pitman–Stanley polytope diameters treat different geometric problems or different graphs and do not supply this four-endpoint metric enumeration.

## Limitations

The result does not cover other netflow vectors, positive edge rescalings, arbitrary directed graphs, distances between uniform interior points, or graph-geodesic distances in the one-skeleton. The beta distribution is a classical order-statistic identity; only its application together with the exact finite metric spectrum of this flow polytope is asserted here. A relevant priority search found no statement subsuming the exact polynomial, but exhaustive historical novelty cannot be established from indexed searches alone. No independent mathematical audit has been performed.

## References

1. C. Benedetti, R. S. González D'León, C. R. H. Hanusa, P. E. Harris, A. Khare, A. H. Morales, M. Yip, *A Combinatorial Model for Computing Volumes of Flow Polytopes*, arXiv:1801.07684, first posted 2018-01-23; Transactions of the American Mathematical Society 372 (2019), 3369–3404. https://arxiv.org/abs/1801.07684
2. J. Jang and J. S. Kim, *Volumes of Flow Polytopes Related to Caracol Graphs*, arXiv:1911.10703, first posted 2019-11-25; Electronic Journal of Combinatorics 27 (2020), P4.21. https://arxiv.org/abs/1911.10703
3. M. Yip, *A Fuss-Catalan Variation of the Caracol Flow Polytope*, arXiv:1910.10060, first posted 2019-10-22. https://arxiv.org/abs/1910.10060
