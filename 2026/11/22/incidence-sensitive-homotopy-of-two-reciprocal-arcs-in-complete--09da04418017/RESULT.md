# Incidence-sensitive homotopy of two reciprocal arcs in complete bipartite digraphs

## Finding
Fix an integer \(n\ge2\). Start with the one-way complete bipartite digraph on \(A=\{a_1,a_2\}\) and \(B=\{b_1,\ldots,b_n\}\), containing every arc \(a_i\to b_j\). Select **two different** pairs \((i,j)\) and add their reciprocal arcs \(b_j\to a_i\); retain all the original arcs. Write \(X\) for the ordinary multipath complex (vertices are directed arcs; faces are edge sets decomposing into directed vertex-disjoint paths).

All possible two-reciprocal-arc placements, up to permutations within shores, have the following **integral homotopy classification**:

\[
X\simeq
\begin{cases}
S^1\vee S^2,&\text{the reciprocal arcs have disjoint endpoints},\\
S^1,&\text{the reciprocal arcs share an endpoint and }n=2,3,\\
\displaystyle\bigvee^{n^2-5n+5}S^2,&\text{the reciprocal arcs share an endpoint and }n\ge4.
\end{cases}
\]

In the disjoint-endpoint case the natural inclusions induced by adding further \(B\)-vertices with only forward arcs are **simple-homotopy equivalences**, realized by elementary simplicial collapses: every complex for \(n\ge2\) collapses to the four-vertex base case. The conclusion concerns genuine integral homotopy types, not only mod-two Betti numbers.

## Assumptions and scope
The digraph is finite, with no loops, but may contain a pair of opposite arcs; the two new reverse arcs correspond to two distinct original bipartite edges. A multipath must have indegree and outdegree at most one at each vertex **and no directed cycle**, including a directed 2-cycle. Ordinary geometric realization is understood. We do not identify the multipath complex with the (different) oriented matching complex.

For the proof let \(p_j=(a_1,b_j)\), \(q_j=(a_2,b_j)\), and let \(F_n\) be the complex using only forward arcs. Then \(F_n\) is the one-dimensional chessboard graph on vertices \(p_1,\ldots,p_n,q_1,\ldots,q_n\), with edges \(p_jq_k\) exactly when \(j\ne k\). All forward-only faces have at most two vertices.

The three incidence patterns are: reverse arcs \(r_1=(b_1,a_1),r_2=(b_2,a_2)\) (disjoint); \(r_1=(b_1,a_1),r_2=(b_1,a_2)\) (shared source); and \(r_1=(b_1,a_1),r_2=(b_2,a_1)\) (shared target). Permutations within \(A\) and \(B\) reduce every two-pair choice to one of these patterns.

## Proof
**1. Shared endpoint: a suspension decomposition.** If the two reverse arcs are incident, they cannot belong to the same multipath: they would give indegree two or outdegree two. For each reverse arc \(r_i=(b_j,a_k)\), its link among forward arcs is the full subcomplex \(L_i=F_n-p_j\) when \(k=1\), or \(L_i=F_n-q_j\) when \(k=2\), where the notation removes the forward vertex reciprocal to \(r_i\). Indeed a forward matching and **one** reverse arc can form a directed cycle only if it contains the reciprocal forward arc, producing a 2-cycle; degree constraints introduce no other restriction. The two excluded forward vertices are incompatible with each other (they have the same source or target), so \(F_n=L_1\cup L_2\). Therefore

\[
X=(r_1*L_1)\cup (r_2*L_2),\qquad
(r_1*L_1)\cap(r_2*L_2)=J:=L_1\cap L_2.
\]

Here \(r_i*L_i\) denotes the simplicial cone. Because both covering subcomplexes are contractible and the inclusions are cofibrations, their ordinary union is homotopy equivalent to \(\Sigma J\), the unreduced suspension of the intersection.

In the shared-source pattern \(J\) has vertices \(p_j,q_j\) for \(2\le j\le n\), and an edge \(p_jq_k\) iff \(j\ne k\). In the shared-target pattern \(J\) has \(p_3,\ldots,p_n,q_1,\ldots,q_n\), with the same edge rule. In either case \(J\) has \(2n-2\) vertices and \((n-1)(n-2)\) edges. For \(n=2\) and \(n=3\), it has exactly two contractible connected components (vertices or trees), hence \(J\simeq S^0\) and \(X\simeq S^1\). For \(n\ge4\), the graph is connected, and its first Betti rank is

\[
(n-1)(n-2)-(2n-2)+1=n^2-5n+5.
\]

Every connected finite graph is a wedge of its first Betti number of circles. Suspending gives the asserted integral two-sphere wedge.

**2. Disjoint reverse arcs: uniform domination.** Set \(r_1=(b_1,a_1)\) and \(r_2=(b_2,a_2)\). For each \(j\ge3\), every multipath face containing \(p_j\) can also be enlarged by \(r_1\) (unless it already contains \(r_1\)), and every face containing \(q_j\) can also be enlarged by \(r_2\). Indeed the degree restrictions permit these insertions. The only possible directed cycles are the two reciprocal 2-cycles and the 4-cycle using \(p_2,q_1,r_1,r_2\). A face containing \(p_j\) for \(j\ge3\) contains neither \(p_1\) nor \(p_2\); one containing \(q_j\) contains neither \(q_1\) nor \(q_2\). Thus the respective insertion cannot create a cycle. Consequently \(\operatorname{link}(p_j)\) is a cone with apex \(r_1\), and \(\operatorname{link}(q_j)\) is a cone with apex \(r_2\). These are dominated simplicial vertices. Deleting them via elementary collapse pairs, in any order, leaves the full subcomplex on \(p_1,p_2,q_1,q_2,r_1,r_2\), namely \(X_2\). This explicitly proves a collapse \(X_n\searrow X_2\) for every \(n\ge2\) and proves the simple-homotopy statement for all inclusions \(X_n\hookrightarrow X_{n+1}\).

**3. Identify the disjoint base.** The only two-faces of \(X_2\) are the four triangles on the four vertices \(\{p_2,q_1,r_1,r_2\}\). Together with their subfaces these form the boundary of a tetrahedron, hence an embedded \(S^2\). The only remaining vertices \(p_1,q_2\) and edges \(p_1q_2\), \(q_2r_1\), \(p_1r_2\) form an additional path between two distinct points of the sphere, with interior disjoint from it. Attaching such a path to a simply connected sphere has homotopy type \(S^2\vee S^1\). This finishes the classification.

## Verification
The accompanying standalone `verify.py` reconstructs all multipath faces directly from indegree/outdegree and acyclicity, for each of the three reverse-arc incidence patterns and every \(2\le n\le10\). It checks downward closure, the complete mod-two Betti profile, both incident-link cone decompositions, intersection graph component and edge counts, and every claimed dominated-vertex extension in the disjoint case. It also reconstructs exactly the tetrahedral boundary and attached path in the base case. The recorded independent program run reports 27 parameter/pattern cases passing. These finite checks confirm local combinatorics but are **not** used as a substitute for the uniform combinatorial proof above.

## Relationship to prior work
Caputi, Collari, Di Trani, and Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (first public 2022-08-09), §3.2 Theorem 3.7, calculate the Euler characteristic of the **one-way** complete bipartite digraph, exploiting its chessboard matching complex. That result does not determine what happens when two reverse arcs, and hence 2-cycles, are introduced. Caputi, Collari, and Di Trani, *Combinatorial and topological aspects of path posets*, arXiv:2110.11206, develops general multipath complexes and examples, not the present three-way incidence classification. Caputi, Celoria, and Collari, *Monotone cohomologies and oriented matchings*, arXiv:2203.03476, studies a distinct simplicial object. Caputi, Collari, and Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, concern fully bidirected paths and polygons, rather than the partial reciprocal completion of a complete bipartite digraph. Related calculations for fully bidirected bicliques concern a **different graph family**; knowing its homotopy type does not imply that of these two-reverse-arc subdigraphs.

## Limitations
The theorem fixes the smaller shore at exactly two vertices and inserts exactly two reciprocal arcs. No formula is claimed for three or more reverse arcs or for a larger source shore. The simple-collapse assertion is for the disjoint case; for the incident cases only the asserted homotopy equivalence and integral homology consequences are proved. Search-based originality cannot exclude all unindexed equivalent formulations, and no independent scientific validation has been performed.

## References
1. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1, 2022, https://arxiv.org/abs/2208.04656.
2. L. Caputi, C. Collari, S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, arXiv:2110.11206, https://arxiv.org/abs/2110.11206.
3. L. Caputi, D. Celoria, C. Collari, *Monotone cohomologies and oriented matchings*, arXiv:2203.03476, https://arxiv.org/abs/2203.03476.
4. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, https://arxiv.org/abs/2601.05670.
