# Super-coalition partition polynomials of complete multipartite graphs

## Finding
For a finite simple graph, a **super dominating set** \(D\) has the following property: for every \(u\notin D\) there exists \(v\in D\) with \(N(v)\cap(V\setminus D)=\{u\}\). A **super-coalition partition** is an unordered partition of the vertex set into nonempty blocks, each of which fails to be super dominating, such that each block has a distinct partner block whose union is super dominating.

**Theorem.** Let \(G=K_{n_1,\ldots,n_r}\) be a labelled complete multipartite graph with \(r\ge2\), positive part sizes and \(N=\sum_i n_i\ge7\). Let \(Q\) be the graph on the same labelled vertices joining precisely the pairs lying in different parts **both of size at least two**. Write \(e=|E(Q)|\), \(m_2\) for the number of unordered pairs of vertex-disjoint edges of \(Q\), and \(t_3\) for the number of triangles of \(Q\). If \(a_k(G)\) counts unordered super-coalition partitions into \(k\) blocks, then
\[
a_2=2^{N-1}-1-N-e,\qquad
 a_3=\binom N2+(N-3)e+m_2,\qquad
 a_4=t_3,
\]
with \(a_k=0\) for every other \(k\). Thus the complete block-count polynomial is
\[
\mathcal C_G(z)=(2^{N-1}-1-N-e)z^2+
\left(\binom N2+(N-3)e+m_2\right)z^3+t_3z^4.
\]
In particular, the super-coalition number is exactly \(4\) if at least three parts have size at least two, and \(3\) otherwise (under the stated \(N\ge7\) assumption).

The coefficients require only elementary computations from the part sizes:
\[
e=\sum_{i<j:\,n_i,n_j\ge2}n_in_j,\quad
m_2=\binom e2-\sum_{v\in V(G)}\binom{\deg_Q(v)}2,\quad
 t_3=\sum_{i<j<k:\,n_i,n_j,n_k\ge2}n_in_jn_k.
\]
For example, \(K_{2,2,2,2}\) has \(e=24\), \(m_2=156\), \(t_3=32\), hence \(\mathcal C_G(z)=95z^2+304z^3+32z^4\).

## Assumptions and scope
The graph is finite, undirected, simple and **connected** by virtue of \(r\ge2\). Vertices are labelled and the partitions are **unordered**; exchanging two blocks does not create another partition. Singleton parts are permitted. The bound \(N\ge7\) is essential to this uniform coefficient formula: smaller multipartite graphs may have exceptional partitions and are not included in its asserted domain. The parameter \(m_2\) counts two-edge matchings of \(Q\), not matchings of the original complete multipartite graph.

## Proof
**1. The super-dominating-set criterion.** Put \(T=V(G)\setminus D\). The empty set and every singleton \(T\) are admissible as complements of super dominating sets (the latter because each vertex has a neighbor). Suppose \(T=\{u,w\}\). If \(u,w\) lie in the same part, a selected witness outside that part sees both, so neither is individually witnessed. If they lie in distinct parts, a witness for \(u\) must lie in the part of \(w\), and a witness for \(w\) must lie in the part of \(u\). Such selected witnesses exist exactly when both corresponding parts contain an additional vertex, i.e. when \(uw\in E(Q)\).

No \(T\) of size at least three can be admissible. Indeed, a witness \(v\in D\) for \(u\in T\) must be adjacent to \(u\) and to no other vertex of \(T\). Since \(G\) is complete multipartite, all of \(T\setminus\{u\}\) must lie in the part containing \(v\). This part contains at least two members of \(T\). Choose another \(w\) in that part: any witness for \(w\) must lie outside its part and would then see at least two vertices of \(T\), a contradiction. Therefore a union of partition blocks is super dominating exactly when its complementary blocks together comprise either zero vertices, a singleton, or an edge of \(Q\).

**2. Two blocks.** With exactly two blocks, their union is all vertices and therefore super dominating; neither block may be super dominating itself. A nontrivial unordered bipartition of \(N\) labelled vertices has \(2^{N-1}-1\) choices. A block is super dominating precisely when its complementary block is a singleton or an edge of \(Q\). This excludes exactly \(N+e\) bipartitions, with no overlap because \(N\ge7\) guarantees the complementary block of such a small block has at least five vertices. This proves \(a_2\).

**3. Three blocks.** For an unordered partition \(\{A,B,C\}\), the union \(A\cup B\) is super dominating precisely when the omitted block \(C\) is either a singleton or a two-vertex edge of \(Q\). Thus each block has a coalition partner if and only if at least two of the three blocks are of these special types. Since \(N\ge7\), at most two can be special; the third has size at least three, and is not super dominating because its complement is a union of the two special blocks of total size at least two, with the sole possible exception of two singletons that form an edge of \(Q\). We count separately:

(a) Two singleton blocks \(\{u\},\{w\}\), not forming an edge of \(Q\): \(\binom N2-e\) choices. If they were an edge of \(Q\), the third block would itself be super dominating and the partition invalid.

(b) One singleton and one two-vertex edge of \(Q\), disjoint: \((N-2)e\) choices. The remaining block has \(N-3\ge4\) vertices, so none of the blocks is super dominating.

(c) Two disjoint two-vertex edges of \(Q\): \(m_2\) choices. The remaining block has \(N-4\ge3\) vertices, and none of the three blocks is super dominating.

All configurations give the coalition property: each small special block partners with the large residual block, whose complement is the other special block. Therefore \(a_3=(\binom N2-e)+(N-2)e+m_2\).

**4. Four or more blocks.** If \(k\ge5\), any union of two blocks leaves at least three nonempty blocks outside it. The complement has at least three vertices and cannot be the complement of a super dominating set, so no partnership is possible. If \(k=4\), any valid partnership leaves two blocks whose union must contain exactly two vertices and be an edge of \(Q\); those two blocks are necessarily singletons. To give each of the four blocks a partner, at least three singleton blocks are required, with the fourth containing \(N-3\ge4\) vertices. The three singleton vertices must be pairwise adjacent in \(Q\), since each singleton must partner the large block, leaving the other two singleton vertices as its omitted \(Q\)-edge. Conversely any triangle in \(Q\) yields exactly one such partition, proving \(a_4=t_3\). No individual block is super dominating because all singleton complements are large and the large-block complement consists of three vertices.

**5. Numerical parameters and maximum.** Every unordered two-edge matching is an unordered pair of distinct edges minus pairs sharing a vertex. Every triangle of \(Q\) takes one vertex from each of three distinct non-singleton parts. These observations give the displayed formulas. The three-block count is strictly positive for \(N\ge7\), and the four-block count is positive precisely with three non-singleton parts; hence the stated super-coalition number.

## Verification
The included standalone `verify.py` defines super domination directly using original vertex neighborhoods and enumerates unordered set partitions without invoking the structural theorem. It checks every connected multipartite part-size profile of orders \(7\) and \(8\), three additional profiles of order \(9\), the smaller six-vertex boundary case \(K_{2,2,2}\), and the eight-vertex example. A successful run prints `VERIFY_OK 38`. This is finite corroboration; the preceding arguments prove the theorem for unbounded part sizes.

## Relationship to prior work
Alikhani and Ghanbari, *Super Coalition Number in Graphs* (2026, arXiv:2607.22686), define super-coalition partitions, provide general bounds and analyze paths, cycles, complete graphs, stars, wheels and friendship graphs. A prior published mathematical finding, *All super dominating sets of complete multipartite graphs* (published-finding corpus, 2026), already gives the underlying necessary-and-sufficient complement criterion; the present statement does not claim this criterion itself as new. Instead it enumerates **all partitions** into coalition classes, a different combinatorial object, and derives the matching/triangle coefficients and a sharp four-block threshold. The abstract of the motivating preprint and the summary of that finding were accessible, but their complete primary texts were not successfully retrieved for comparison; this creates an explicit historical-priority risk.

## Limitations
The theorem excludes orders below seven, which exhibit separate finite boundary behavior. It treats connected complete multipartite graphs rather than arbitrary graphs, and labelled vertices rather than automorphism classes. The evaluation of the full source preprint was limited to accessible bibliographic/abstract material. No independent mathematical audit or exhaustive historical priority certification has been performed.

## References
1. S. Alikhani and N. Ghanbari, *Super Coalition Number in Graphs*, arXiv:2607.22686 (first public date indexed 2026-07-15), https://arxiv.org/abs/2607.22686 .
2. *All super dominating sets of complete multipartite graphs*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-all-super-dominating-sets-of-complete-multipartite-graphs--315739371089 .
