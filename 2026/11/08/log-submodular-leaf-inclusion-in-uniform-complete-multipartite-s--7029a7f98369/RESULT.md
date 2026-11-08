# Log-submodular leaf inclusion in uniform complete-multipartite spanning trees

## Finding
Let \(G=K_{n_1,\ldots,n_k}\) be a complete multipartite graph with \(k\ge2\), all \(n_i\ge1\), and \(N=\sum_i n_i\ge3\). Choose a spanning tree \(T\) uniformly from all spanning trees of \(G\), and write \(L(T)=\{v:\deg_T(v)=1\}\). For every vertex set \(S\subseteq V(G)\), define \(F(S)=\Pr(S\subseteq L(T))\). Write \(V_i\) for the \(i\)-th part, \(d_i=N-n_i\), and \(s_i=|S\cap V_i|\). Then

\[
F(S)=\left(\frac{N-|S|}{N}\right)^{k-2}
\prod_{i=1}^{k}\left(\frac{d_i-(|S|-s_i)}{d_i}\right)^{n_i-1}.
\tag{1}
\]

Nonnegative powers at zero use the ordinary empty-product convention \(0^0=1\). In particular \(F(\varnothing)=1\) and \(F(V(G))=0\).

**All-set negative lattice inequality.** For every \(S\subseteq V(G)\) and distinct \(u,v\notin S\),

\[
F(S\cup\{u,v\})F(S)\ \le\ F(S\cup\{u\})F(S\cup\{v\}).
\tag{2}
\]

For \(k\ge3\), (2) is strict whenever both single-addition probabilities on the right are nonzero. For \(k=2\), (2) is always an equality if \(u,v\) lie in different parts, and is strict if they lie in the same part, the other part has at least two vertices, and both right-side probabilities are nonzero; otherwise it is an equality. Therefore the full leaf family obeys the upper-orthant inequality

\[
\Pr(A\cup B\subseteq L(T))\le\Pr(A\subseteq L(T))\Pr(B\subseteq L(T))
\tag{3}
\]

for all disjoint vertex sets \(A,B\). In particular distinct leaf indicators have strictly negative covariance when \(k\ge3\). In the bipartite case, leaf indicators from different parts are pairwise independent; same-part pairs have strictly negative covariance precisely when both parts have at least two vertices (the star degeneracy gives zero). These assertions concern **all-one inclusion events**, not full negative association for arbitrary increasing functions of disjoint leaf subfamilies.

## Assumptions and scope
The graph is finite, simple, undirected, and unweighted. Its parts are nonempty and pairwise completely joined, and \(N\ge3\). A leaf is a degree-one vertex of the sampled *tree*, not a degree-one vertex of the underlying graph. The statements quantify over every vector of positive part sizes, every subset \(S\), and every distinct pair outside \(S\). No asymptotic limit or independence across unrelated leaf events is assumed. The two-vertex tree \(K_{1,1}\) is excluded because its two endpoints are both leaves and the leaf-grafting decomposition used below has a separate trivial case.

## Proof
**Step 1: the classical tree count.** For \(G=K_{n_1,\ldots,n_k}\), its Laplacian acts by multiplication by \(d_i=N-n_i\) on the \((n_i-1)\)-dimensional space of vectors supported in \(V_i\) with coordinate sum zero. On the part-constant subspace it has nonzero eigenvalue \(N\) with multiplicity \(k-1\), and a single zero eigenvalue. Kirchhoff's matrix-tree theorem consequently gives

\[
\tau(G)=N^{k-2}\prod_{i=1}^{k}d_i^{n_i-1}.
\tag{4}
\]

This is a known enumeration, not a claimed new counting formula.

**Step 2: forced leaves and the exact product.** Fix \(S\) and let \(R=V(G)\setminus S\), with \(m=|R|\). Assume first that \(m\ge2\) and \(G[R]\) is connected. A spanning tree with all vertices of \(S\) leaves consists uniquely of a spanning tree on \(R\), together with one edge from each \(x\in S\) to a vertex of \(R\). Indeed no two leaves are adjacent in any tree of order at least three. Every \(x\in V_i\cap S\) has exactly \(m-(n_i-s_i)=d_i-(|S|-s_i)\) allowable attachments. Thus

\[
\tau(G)F(S)=\tau(G[R])\prod_i\bigl(m-n_i+s_i\bigr)^{s_i}.
\tag{5}
\]

Apply (4) to the nonempty parts of \(G[R]\). Equivalently, retaining all \(k\) part indices, each empty part contributes a cancelling factor \(m^{-1}\); for \(m>0\), this writes

\[
\tau(G[R])=m^{k-2}\prod_i\bigl(m-n_i+s_i\bigr)^{n_i-s_i-1}.
\]

Multiplication by the attachment choices leaves the fixed exponents \(n_i-1\); division by (4) proves (1). If \(G[R]\) has a single nontrivial independent part, both sides of (5) vanish and the right of (1) has a zero to a positive power. If \(m=1\), the only possible tree has the remaining vertex as its star center. This is possible precisely when its original part had size one, and the right of (1) gives the corresponding probability \(1/\tau(G)\); otherwise both sides are zero. If \(m=0\), the event is impossible for \(N\ge3\), and (1) is zero: either \(k\ge3\) makes its first factor zero, or \(k=2\) and at least one exponent \(n_i-1\) is positive. This proves the formula in all boundary cases.

**Step 3: log-submodularity.** Consider a general nonnegative factor \(H_C(S)=(c-|S\cap C|)^a\) with an integer exponent \(a\ge0\), defined on vertex subsets with \(c\ge|C|\). For distinct \(u,v\notin S\), its two single-addition factors multiply to at least its no-addition factor times its two-addition factor. If both additions are in \(C\), this follows from

\[
(c-r-1)^2-(c-r)(c-r-2)=1
\]

where \(r=|S\cap C|\) and \(c-r\ge2\). If at most one addition is in \(C\), the two products agree. All factors are nonnegative, so raising to \(a\) and multiplying preserves the inequality, including zero boundaries.

The numerator of (1) is the product of precisely these factors: take \(C=V(G)\) with exponent \(k-2\), and for each part \(i\) take \(C=V(G)\setminus V_i\) with exponent \(n_i-1\). The fixed positive denominator does not affect the comparison. This proves (2). If \(k\ge3\), the factor with \(C=V(G)\) contributes a strict inequality whenever \(F(S\cup\{u\})F(S\cup\{v\})>0\), because \(m\ge2\). When \(k=2\), only the two complementary-part factors remain. If \(u,v\) lie in different parts, neither factor sees both additions and equality holds. If they lie in the same part, the factor corresponding to the other part sees both, and its exponent is positive exactly when that other part has size at least two, establishing the stated complete equality classification.

**Step 4: upper-orthant and pairwise consequences.** Where \(F(S)>0\), (2) says that \(F(S\cup\{u\})/F(S)\) is nonincreasing as other required-leaf vertices are added. Iterating this inequality yields (3); zeros follow by monotonicity. At \(S=\varnothing\), (2) compares the joint leaf probability with the product of marginals, and Step 3 yields all strictness and equality assertions. This completes the proof.

## Verification
The standalone `verify_leaf_inclusion.py` computes the rational product (1) for all vertex subsets of 127 nonisomorphic part-size profiles with \(3\le N\le10\), tests every two-addition inequality, checks its strictness for \(k\ge3\) when the right side is positive, and independently enumerates spanning trees as edge subsets for 54 small profiles. It reports 666,620 exact checks passed. Its independent enumerator does not use the tree-count formula. These finite computations check the algebra and boundary cases but do not replace Steps 1–4, which prove the results for arbitrary sizes.

A useful counterpoint is the cycle \(C_5\): a uniform spanning tree deletes one uniformly chosen edge, making each vertex a leaf with probability \(2/5\) and adjacent vertices jointly leaves with probability \(1/5\). Their covariance is \(1/25>0\). Thus the negativity theorem is genuinely a property of multipartite geometry, not of all uniform spanning trees.

## Relationship to prior work
The classical multipartite spanning-tree count (4) is known. The 1994 bijection of Eğecioğlu–Remmel develops multivariate weights and studies leaf asymptotics; Lewis (1999) studies degree distributions; Remmel–Williamson (2002) gives multipartite spanning-tree generating functions; Dong–Ge (2022) and Li–Chen–Yan (2023) count trees containing fixed forests, and Wang–Ge (2026) gives a further determinant formulation. These enumerative works offer broad routes to degree coefficients. The distinct claim here is the uniform **all-subset log-submodularity inequality with a strict/equality classification**, deduced from a forced-leaf product and discrete concavity; it is not an assertion that degree-count formulas or all marginal probabilities were previously unknown. No equivalent negativity theorem was identified in the inspected accessible primary material or targeted searches. The 1994, 1999, and 2023 texts were not all available in full; historical priority of the inequality therefore carries a documented residual risk.

## Limitations
The assertion does not establish the full negative-association property for arbitrary increasing functions of disjoint leaf groups. It does not apply to a weighted nonuniform spanning-tree law, arbitrary graphs, or degree thresholds other than exactly one. The expression is exact only for the stated unweighted multipartite graphs. The independent checker exhausts only finite small instances. The possible implication from older multipartite degree-generating functions remains a literature-priority limitation, not a mathematical assumption in the proof.

## References
1. D. Li, W. Chen, W. Yan, *Enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest*, Journal of Graph Theory 104 (2023), 160–170. First publicly published March 30, 2023. https://doi.org/10.1002/jgt.22954
2. J. B. Remmel and S. G. Williamson, *Spanning Trees and Function Classes*, Electronic Journal of Combinatorics 9 (2002), R34. https://doi.org/10.37236/1650
3. Ö. Eğecioğlu and J. B. Remmel, *A Bijection for Spanning Trees of Complete Multipartite Graphs*, Congressus Numerantium 100 (1994), 225–243. https://sites.cs.ucsb.edu/~omer/personal/abstracts/multipartite.html
4. R. P. Lewis, *The number of spanning trees of a complete multipartite graph*, Discrete Mathematics 197–198 (1999), 537–541. https://doi.org/10.1016/S0012-365X(98)00260-X
5. F. M. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, Journal of Graph Theory 101 (2022), 79–94. https://doi.org/10.1002/jgt.22812
6. W. Wang and J. Ge, *On enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest*, arXiv:2602.03602 (February 3, 2026). https://arxiv.org/abs/2602.03602
