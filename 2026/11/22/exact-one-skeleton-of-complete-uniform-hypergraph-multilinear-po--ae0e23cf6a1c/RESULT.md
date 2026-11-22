# Exact one-skeleton of complete uniform hypergraph multilinear polytopes

## Finding
Let \(2\le r\le n\) be integers. For every subset \(S\subseteq[n]\), let \(v_S\) have coordinate \(x_i=\mathbf 1_{i\in S}\) for \(i\in[n]\) and coordinate \(y_F=\mathbf 1_{F\subseteq S}\) for every \(r\)-subset \(F\subseteq[n]\). Define
\[
P_{n,r}=\operatorname{conv}\{v_S:S\subseteq[n]\}\subset\mathbb R^{n+\binom nr}.
\]
All \(2^n\) points \(v_S\) are distinct vertices. The full one-skeleton is characterized by the following exact rule, for distinct \(S,T\):
\[
v_Sv_T\text{ is an edge}\quad\Longleftrightarrow\quad
\max\{|S|,|T|\}\ge r\quad\text{or}\quad
|S\mathbin\triangle T|=1\quad\text{or}\quad
\bigl(|S|=|T|=r-1\ \text{and}\ |S\mathbin\triangle T|=2\bigr).
\]
Here \(S\mathbin\triangle T\) denotes symmetric difference. Equivalently, the graph is the graph-theoretic join of a complete graph on the supports of size at least \(r\) with the graph of the uniform-matroid independence polytope of rank \(r-1\) on the remaining supports. This is a graph join, not a statement that the polytopes are joined.

Write \(N=2^n\), \(M=\sum_{j=r}^n\binom nj\), and \(L=N-M\). The degree of \(v_S\), with \(k=|S|\), is exactly
\[
\deg(v_S)=\begin{cases}
N-1,&k\ge r,\\
M+n,&0\le k\le r-2,\\
M+(r-1)(n-r+2),&k=r-1.
\end{cases}
\]
In particular, the complete degree enumerator is
\[
M t^{N-1}+\left(\sum_{k=0}^{r-2}\binom nk\right)t^{M+n}
+\binom n{r-1}t^{M+(r-1)(n-r+2)}.
\]
Equal exponents are combined in the ordinary way. The total number of edges is
\[
\binom M2+ML+n\sum_{k=0}^{r-2}\binom{n-1}{k}
+\frac12\binom n{r-1}(r-1)(n-r+1).
\]
The graph has diameter \(1\) when \(r=2\), and exactly \(2\) when \(3\le r\le n\).

## Assumptions and scope
The hyperedge set consists of **all and only** \(r\)-element subsets of \([n]\). In particular, no coordinates are included for lower-degree monomials of degrees \(2,\ldots,r-1\). The result concerns the true multilinear polytope, not its standard linear relaxation. No genericity, asymptotic assumption, or fixed dimension restriction is made. All counting quantities refer to the ordinary graph of the convex polytope, and every support \(S\) labels one vertex.

## Proof
**Vertex and midpoint criteria.** The \(x\)-coordinates of \(v_S\) are the vertices of the binary cube. If a convex combination of points \(v_T\) equals \(v_S\), then each coordinate fixed to zero or one forces every support in that combination to agree with \(S\). Consequently each \(v_S\) is an extreme point. For two distinct vertices \(p,q\) of a finite polytope, their segment is an edge if and only if every convex representation of \((p+q)/2\) is supported entirely on \(\{p,q\}\). The forward implication follows from exposedness of an edge. Conversely, if the minimal face containing the midpoint had dimension at least two, the midpoint, lying in the relative interior of that face, would admit a representation involving another vertex. We use this criterion below.

**Universal adjacency from a large support.** Fix distinct \(S,T\), and suppose \(|S|\ge r\); if initially only \(T\) is large, exchange the labels. Set \(A=S\setminus T\), \(B=T\setminus S\), \(I=S\cap T\). If \(A=\varnothing\), then \(T\supsetneq S\) is large and the labels may be exchanged, so we may assume \(A\ne\varnothing\). Let \(U\) be a random support such that
\[
\mathbb E[v_U]=\tfrac12(v_S+v_T).
\]
For \(i\in I\), the indicator \(X_i=\mathbf1_{i\in U}\) is almost surely one; outside \(S\cup T\) it is almost surely zero. Every \(i\in A\cup B\) has \(\mathbb E X_i=1/2\). For \(a\in A\), choose any \(r\)-subset \(F\subseteq S\) containing \(a\). The monomial \(Y_F=\prod_{i\in F}X_i\) has mean \(1/2\), equal to \(\mathbb E X_a\), and satisfies \(Y_F\le X_a\). Thus \(Y_F=X_a\) almost surely. For any distinct \(a,a'\in A\), choose an \(r\)-subset of \(S\) containing both (possible because \(|S|\ge r\ge2\)). The preceding equality implies \(X_a=X_{a'}\) almost surely. Hence the indicators for \(A\) have a common value \(Z\in\{0,1\}\), with \(\mathbb P(Z=1)=1/2\).

If \(B\ne\varnothing\), choose an \((r-1)\)-subset \(G\subseteq S\) containing an element of \(A\). The same monomial argument, or inclusion of \(G\) in an \(r\)-subset of \(S\), shows \(\prod_{i\in G}X_i=Z\) almost surely. For \(b\in B\), the \(r\)-set \(G\cup\{b\}\) is contained in neither \(S\) nor \(T\); its midpoint monomial coordinate is therefore zero, so \(ZX_b=0\) almost surely. Since \(\mathbb E X_b=1/2=\mathbb P(Z=0)\), we have \(X_b=1-Z\) almost surely. In the case \(B=\varnothing\) there are no such indicators. Thus \(U=S\) when \(Z=1\) and \(U=T\) when \(Z=0\). All midpoint representations use exactly these two vertices, proving adjacency for every pair with a large support.

**Small supports form the uniform-matroid independence polytope.** Every monomial coordinate \(y_F\) is nonnegative. Hence
\[
P_{n,r}\cap\Bigl\{\sum_{|F|=r}y_F=0\Bigr\}
=\operatorname{conv}\{v_S:|S|\le r-1\},
\]
a face affinely isomorphic, via the \(x\)-projection, to
\[
Q_{n,r-1}=\left\{x\in[0,1]^n:\sum_i x_i\le r-1\right\}.
\]
The equality with the convex hull of all binary supports of cardinality at most \(r-1\) follows from integrality of this one-row uniform-matroid polytope; alternatively, every nonbinary vertex of the displayed system would have two fractional coordinates that can be perturbed, or one fractional coordinate while the sum constraint is tight at an integer right-hand side, both contradictions.

For distinct small supports \(S,T\), at their midpoint the coordinate bounds are tight exactly on \(S\cap T\) and on the complement of \(S\cup T\). The rank inequality is tight exactly when both supports have cardinality \(r-1\). If it is slack, the minimal face dimension equals \(|S\triangle T|\). If it is tight, the minimal face dimension equals \(|S\triangle T|-1\). (In the tight case there are at least two free coordinates, one of each sign.) A segment is an edge precisely when the midpoint belongs to a one-dimensional face. Hence the only small-small edges are single-coordinate flips and exchanges between distinct top-rank supports differing in two coordinates. As this is a face of \(P_{n,r}\), these are exactly the small-small edges in the full polytope.

**Counts and diameter.** Every large vertex is adjacent to all other \(N-1\) vertices. A small vertex below the top rank has \(n\) neighbors within the small face by coordinate flips; a small top-rank vertex has \(r-1\) downward flips plus \((r-1)(n-r+1)\) top-rank exchanges, totaling \((r-1)(n-r+2)\). Add the \(M\) large neighbors for the degree formula. Cube edges below rank \(r-1\) contribute \(n\sum_{k=0}^{r-2}\binom{n-1}{k}\), and top-rank exchanges contribute \(\binom{n}{r-1}(r-1)(n-r+1)/2\). The other edges lie inside the complete large stratum or join it to the small stratum, giving the total edge formula. For \(r=2\) the small graph consists of the empty support and all singletons, all mutually adjacent by the exchange rule, making the entire graph complete. For \(r\ge3\), the small supports \(\varnothing\) and \(\{1,2\}\) are not adjacent, but every large vertex is their common neighbor. The diameter is therefore exactly two.

## Verification
The standalone pure-Python program `verify_skeleton.py` builds all lifted Boolean vertices using integer coordinates, classifies every unordered pair by the theorem, compares its midpoint integer signature with the signatures of all other pairs, and checks the predicted degrees and exact edge counts for every \(2\le r\le n\le7\) plus \((n,r)=(8,4)\). Every predicted nonedge has a distinct pair with the same midpoint; every predicted edge has a unique two-vertex midpoint signature among unordered pairs. These finite exact checks corroborate the classification but are not used as an all-parameter proof; the preceding midpoint and minimal-face arguments cover all \(n,r\).

## Relationship to prior work
Del Pia and Xu (2026) study adjacency and diameters of general multilinear polytopes, characterize adjacency in the standard relaxation by a contracted hypergraph, and show that multilinear-polytope adjacency is harder in general. Their general diameter bound \(n\) does not determine the exact graph of the present **complete exact-degree-\(r\)** family. Del Pia and Khajavirad (2015/2017) study facets and liftings for multilinear polytopes, including a different **full rank-\(r\)** hypergraph containing every degree between two and \(r\), rather than only degree \(r\). The graph-theoretic join, universal vertices, exact degree enumerator, and diameter-two equality established here are not asserted in the inspected source sections. Padberg's classical Boolean-quadric adjacency criterion covers the \(r=2\) case but does not determine the higher-degree exact-r-only structure. These comparisons are mathematical statements, not guarantees of historical priority.

## Limitations
The exact formula depends essentially on including **every** \(r\)-subset, and it does not extend automatically to sparse or mixed-degree hypergraphs. No claim is made about the standard relaxation's graph, total facet structure, or the best possible pivot count of a prescribed algorithm. The finite checker independently confirms only small parameters; the proof is analytical and all-dimensional. Priority against inaccessible or unindexed combinatorial optimization literature is not conclusively settled, and no independent audit has been performed.

## References
- A. Del Pia and Z. Xu, *The One-Skeleton of Multilinear Polytopes and Their Standard Relaxations*, arXiv:2611.15785v1, first posted November 11, 2026. https://arxiv.org/abs/2611.15785
- A. Del Pia and A. Khajavirad, *A Polyhedral Study of Binary Polynomial Programs*, Optimization Online preprint, 2015, revised 2016; published 2017. https://optimization-online.org/wp-content/uploads/2015/02/4782.pdf
- M. W. Padberg, *The Boolean Quadric Polytope: Some Characteristics, Facets and Relatives*, Mathematical Programming 45 (1989), 139–172. https://doi.org/10.1007/BF01589099
