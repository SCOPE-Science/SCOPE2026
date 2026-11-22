# A sharp degree-sum threshold for consecutive-star decompositions of complete bipartite graphs

## Finding

For an integer \(k\ge3\), let \(\mathcal S_k=\{K_{1,k},K_{1,k+1}\}\). Define \(c_k^{\mathrm{bi}}\) as the least integer \(c\) such that every nonempty complete bipartite graph \(K_{a,b}\) with \(a,b\ge1\) and minimum edge degree-sum \(\sigma(K_{a,b})=a+b\ge c\) admits an edge decomposition whose blocks belong to \(\mathcal S_k\). A decomposition may use only one of the two allowed star sizes.

**Theorem.** For every integer \(k\ge3\),
\[
c_k^{\mathrm{bi}}=k^2-1.
\]
More precisely, for all positive integers \(a,b\) satisfying \(a+b\ge k^2-1\), the edges of \(K_{a,b}\) partition into copies of \(K_{1,k}\) and \(K_{1,k+1}\). The family
\[
K_{k-1,\,k(k-1)-1}
\]
is not decomposable and satisfies \(a+b=k^2-2\). Thus the threshold is sharp at **every** \(k\ge3\).

## Assumptions and scope

All graphs are finite, simple and undirected, and all star blocks are edge-disjoint subgraphs, not necessarily induced. Every edge belongs to exactly one star block; a star center may support several blocks. The statement concerns *unprescribed multiplicities* of the two consecutive star sizes: it does not assert that a prescribed number of each size can be achieved, or that both sizes must occur. The two shores of \(K_{a,b}\) are nonempty, and the roles of \(a\) and \(b\) may be interchanged to assume \(1\le a\le b\).

Orient each edge toward its leaf (outward from its star center). A graph admits the required decomposition exactly when it has an orientation in which every vertex outdegree belongs to the additive semigroup
\[
H_k=\{uk+v(k+1):u,v\in\mathbb Z_{\ge0}\}.
\]
Indeed, the outgoing edges at each vertex can then be partitioned into disjoint groups of the indicated cardinalities. This equivalence does not prescribe the numbers of stars of either size.

## Proof

**1. Arithmetic of the two consecutive sizes.** Write \(n=qk+r\), where \(q\ge0\) and \(0\le r<k\). Then
\[
n\in H_k\quad\Longleftrightarrow\quad r\le q.
\]
If \(r\le q\), explicitly write \(n=(q-r)k+r(k+1)\). Conversely, any representation \(n=uk+v(k+1)\) can be rewritten after Euclidean division \(v=tk+r\) as \(n=(u+v+t)k+r\), hence the quotient is at least the remainder. In particular, every \(n\ge k(k-1)\) belongs to \(H_k\), whereas \(k(k-1)-1\notin H_k\). Also, whenever \(T\ge k(k-1)\), putting
\[
L=\left\lceil\frac{T}{k+1}\right\rceil,\qquad J=T-kL
\]
gives integers \(0\le J\le L\), so \(T=(L-J)k+J(k+1)\). To justify this last assertion, write \(T=qk+r\) with \(q\ge k-1\ge r\); then \(T\le q(k+1)\), whence \(L\le q\), making \(J\ge0\); and \(T\le L(k+1)\) gives \(J\le L\).

**2. Easy orientations.** Suppose \(a\le b\). If \(b\in H_k\), orient every edge from the \(a\)-vertex shore toward the \(b\)-vertex shore; each vertex of the first shore then has allowable outdegree \(b\), while each vertex of the second shore has outdegree zero. If \(a\in H_k\), reverse all the edges instead. In either case a star decomposition exists.

**3. The case in which neither shore size belongs to \(H_k\).** Assume \(a,b\notin H_k\), \(a+b\ge k^2-1\), and \(a\le b\). Since every integer at least \(k(k-1)\) is represented and \(b\notin H_k\), we have \(b\le k(k-1)-1\). If \(a\le k-1\), then \(b\ge k(k-1)\), a contradiction. Because \(k,k+1\in H_k\), it follows that \(a\ge k+2\).

Write \(b=qk+r\). Nonrepresentation gives \(1\le q<r\le k-1\). Put \(T=b(a-k)\). Since \(a\ge k+2\) and \(b\ge(a+b)/2\ge(k^2-1)/2\),
\[
T\ge2b\ge k^2-1\ge k(k-1).
\]
Define \(L=\lceil T/(k+1)\rceil\) and \(J=T-kL\); Step 1 gives \(0\le J\le L\). Moreover,
\[
aq(k+1)-T=kb-a(r-q)\ge b\bigl(k-r+q\bigr)>0,
\]
because \(a\le b\) and \(1\le r-q\le k-1\). Therefore \(L\le aq\). Allocate \(L\) indistinguishable slots among the \(a\) vertices of the first shore, at most \(q\) slots to each. Upgrade \(J\) of those slots from length \(k\) to length \(k+1\), giving prescribed nonnegative integer row outdegrees \(d_1,\ldots,d_a\) satisfying
\[
d_i\in H_k,\qquad d_i\le q(k+1)\le qk+r=b,\qquad
\sum_{i=1}^{a}d_i=kL+J=b(a-k).
\]
The inequality \(q(k+1)\le b\) uses \(q<r\).

**4. Realizing the outdegrees.** We claim that there is an \(a\times b\) zero-one matrix with row sums \(d_1,\ldots,d_a\) and every column sum equal to \(a-k\). This follows directly from Gale--Ryser: the row totals equal the column totals, and for every \(1\le t\le a\) the sum of the \(t\) largest row sums is at most
\[
\min\{tb,\,b(a-k)\}=\sum_{j=1}^{b}\min\{t,a-k\},
\]
since each \(d_i\le b\) and the entire sum is \(b(a-k)\). Thus the required binary matrix exists. (Equivalently, the corresponding bipartite degree sequence is graphical.)

Orient edges from the first shore to the second exactly at entries equal to one. The first-shore vertices then have outdegrees \(d_i\in H_k\). Each second-shore vertex has exactly \(a-(a-k)=k\) outward edges, also in \(H_k\). The orientation in Step 1 now partitions into the allowed star blocks, proving sufficiency for every \(a+b\ge k^2-1\).

**5. Sharpness.** Take \(a=k-1\) and \(b=k(k-1)-1\). Every vertex on the \(b\)-vertex shore has degree \(a<k\), so no required star can be centered there. All \(b\) edges incident with each first-shore vertex must therefore lie in stars centered at that vertex. This would require \(b\in H_k\), contradicting Step 1. As \(a+b=k^2-2\), no smaller uniform integer degree-sum threshold works. \(\square\)

## Verification

Run `python3 verify_stars.py` with a standard Python 3 installation. It checks the semigroup characterization against direct two-generator enumeration in 70,319 cases; constructs and verifies explicit zero-one orientations in 3,221 nontrivial shore-size cases and additional large-parameter boundary cases; independently tests small instances by a complete dynamic program over all possible column masks; and confirms the sharp obstruction for 47 values of \(k\). It prints `VERIFY_OK` on success. These finite tests only corroborate the all-parameter proof. The proof uses the classical Gale--Ryser criterion, not the tests, to establish existence for arbitrary parameters.

## Relationship to prior work

Hajebi and Javadi, *Parameterized Complexity of Star Decomposition Problem*, arXiv:2411.13348v1 (first public 2024-11-20), formulate heterogeneous-length star decompositions via orientations and prove complexity results, including hardness for instances on complete bipartite graphs with prescribed multiplicities. That paper motivates the present question: its computational results concern fixed lists of star counts, whereas the present theorem gives a sharp uniform **existence threshold with freely chosen counts** for exactly two consecutive lengths. Their general orientation principle is reused, but their hardness result neither supplies nor contradicts this special existence theorem.

Harangi, *Star decompositions via orientations*, arXiv:2506.05194v1 (2025-06-05), studies uniform-length stars in random regular graphs, rather than consecutive lengths in every biclique. Tarsi's classical expansion sufficient condition, discussed in both the recent literature and earlier by Cameron--Horsley, covers certain sufficiently expanding instances with appropriate multiplicities; it does not give the sharp universal degree-sum threshold including the highly unbalanced bicliques and the boundary obstruction here. Earlier work on single-length decompositions and path-plus-star designs has different block restrictions.

Lee, *Star decomposition of complete multipartite graphs*, arXiv:2611.24973v1 (first public **2026-11-17**), independently formulates exactly the two-length degree-sum problem, proves the complete multipartite threshold at \(k=3\), and leaves higher-rank multipartite thresholds open. That later paper is compared as relevant contemporary work, not used as a premise of the theorem. Its described multipartite bound \(9\) at \(k=3\) does not give the exact biclique threshold \(8\), and its broader unsolved multipartite questions do not automatically imply the all-\(k\) biclique result.

## Limitations

This proves the threshold for **complete bipartite graphs only**, not complete graphs, all complete multipartite graphs, or arbitrary graphs. The multiplicities of the two star sizes are not prescribed. The proof is constructive up to a standard bipartite degree-sequence realization, but does not minimize either star count or characterize all decompositions. Novelty is assessed against the inspected literature and searches and may be revised by earlier unindexed work; no independent mathematical audit has been performed. The full texts of some historical sources on single-length decompositions were not exhaustively examined; their quoted theorems are compared through accessible primary literature.

## References

1. S. Hajebi and R. Javadi, *Parameterized Complexity of Star Decomposition Problem*, arXiv:2411.13348v1, first posted 2024-11-20. https://arxiv.org/abs/2411.13348
2. V. Harangi, *Star decompositions via orientations*, arXiv:2506.05194v1, first posted 2025-06-05. https://arxiv.org/abs/2506.05194
3. J. Lee, *Star decomposition of complete multipartite graphs*, arXiv:2611.24973v1, posted 2026-11-17, supporting comparison only. https://arxiv.org/html/2611.24973v1
4. T. W. Shyu, *Decomposition of complete bipartite graphs into paths and stars with same number of edges*, Discrete Mathematics 313 (2013), 865–871, DOI:10.1016/j.disc.2012.12.020.
5. *Multidecompositions of the Balanced Complete Bipartite Graph into Paths and Stars*, 2013, DOI:10.1155/2013/398473. https://onlinelibrary.wiley.com/doi/10.1155/2013/398473
6. D. Cameron and D. Horsley, *Decompositions of complete multigraphs into stars of varying sizes*, arXiv:1807.10738 (2018), https://arxiv.org/abs/1807.10738
