# Ordinary three-cut complexes of Möbius ladders are uniform sphere wedges

## Finding

For every integer \(n\ge 4\), let \(M_{2n}\) be the Möbius ladder on \(V=\mathbb Z/(2n)\mathbb Z\), with cycle edges \(\{i,i+1\}\) and opposite-vertex edges \(\{i,i+n\}\). Its **ordinary** three-cut complex satisfies the integral homotopy equivalence
\[
\boxed{\Delta_3(M_{2n})\simeq\bigvee^{\,2n(n-4)+1}S^{2n-4}.}
\]
In particular, the cases \(n=4,5,6,7\) give \(S^4\), \(\bigvee^{11}S^6\), \(\bigvee^{25}S^8\), and \(\bigvee^{43}S^{10}\), respectively. The result does **not** concern the total three-cut complex.

## Assumptions and scope

All graphs are finite and simple. The ordinary three-cut complex \(\Delta_3(G)\) has facets \(V(G)\setminus T\), over three-element subsets \(T\) for which the induced graph \(G[T]\) is disconnected. The combinatorial Alexander dual \(X=\Delta_3(G)^\vee\) consists of the vertex sets \(A\subseteq V\) such that **every** three-element subset of \(A\) induces a connected graph. A two-element subset automatically belongs to \(X\).

The graph \(M_{2n}\) is cubic and triangle-free for \(n\ge4\). Write \(N=2n\). All congruences on vertex labels below are modulo \(N\). The claimed homotopy equivalence is nonequivariant and integral. No shellability assertion is made.

## Proof

**Step 1: classify the dual simplices.** A three-vertex graph is connected exactly when it contains at least two edges. Consequently, \(A\in X\) precisely when the nonedges of \(G[A]\) form a matching. Every vertex of such an \(A\) has at least \(|A|-2\) neighbors inside \(A\). Since the ambient graph is cubic, \(|A|\le5\). Equality \(|A|=5\) would force every induced degree to be exactly three, and hence the missing edges would form a perfect matching on five vertices, an impossibility. Thus \(\dim X\le3\).

If \(|A|=4\), every vertex of \(G[A]\) has degree at least two. Since the graph is triangle-free, each degree equals two and \(G[A]\) is a four-cycle. The only four-cycles of the Möbius ladder for \(n\ge4\) are
\[
S_i=\{i,i+1,i+n,i+n+1\},\qquad 0\le i<n.
\]
Indeed, the ambient rim has length at least eight, rungs form a matching, and a four-cycle using rungs must use exactly two rungs and their two connecting rim edges. There are exactly \(n\) tetrahedral faces of \(X\). Each connected triple is a two-edge path, uniquely specified by its central vertex and two of the three neighbors. Hence there are \(2n\binom32=6n\) triangular faces. Precisely four per square lie in a tetrahedron; the remaining \(2n\) are the straight rim triples
\[
T_i=\{i-1,i,i+1\},\qquad 0\le i<2n.
\]
All pairs are faces of \(X\), so its face vector by cardinality is \((1,2n,\binom{2n}{2},6n,n)\).

**Step 2: elementary collapses of the dual.** First, for every rim triple \(T_i\), delete the triangle \(T_i\) together with its free edge \(\{i-1,i+1\}\). This edge has no other triangular coface (it is the distance-two rim diagonal, distinct from every square diagonal when \(n\ge4\)). These \(2n\) collapses are disjoint.

For each \(0\le i<n\), abbreviate \(a=i\), \(b=i+1\), \(c=i+n\), \(d=i+n+1\). First remove the tetrahedron \(\{a,b,c,d\}\) along its free face \(\{a,b,c\}\). The squares have distinct triangular faces. After all tetrahedra have been removed, perform these three successive collapses in every square:
\[
(\{a,b,d\},\{a,b\}),\qquad
(\{a,c,d\},\{a,d\}),\qquad
(\{b,c,d\},\{b,c\}).
\]
Here the ordered pair specifies the removed triangle and its free edge. The rim edge \(\{a,b\}\) occurs in no remaining triangle outside this square; the diagonals \(\{a,d\}\) and \(\{b,c\}\) likewise have no coface after the preceding removals. Squares may share a rung edge, but no rung is selected as a free face, so this overlap does not invalidate any collapse. These are therefore genuine elementary simplicial collapses, for every \(n\ge4\).

The result is a graph \(H\), with all \(2n\) original vertices and
\[
\binom{2n}{2}-2n-3n=2n(n-3)
\]
edges. The \(n\) rungs and the \(n\) unremoved rim edges \(\{i+n,i+n+1\}\), for \(0\le i<n\), form a connected spanning subgraph. Thus \(H\) is connected. Its first Betti number is
\[
|E(H)|-|V(H)|+1=2n(n-4)+1=:r_n,
\]
and the explicit collapses prove \(X\simeq H\simeq\bigvee^{r_n}S^1\).

**Step 3: transfer from dual to the ordinary cut complex.** Integral combinatorial Alexander duality on \(N\) vertices gives
\[
\widetilde H_j(\Delta_3(M_{2n});\mathbb Z)
\cong\widetilde H^{N-j-3}(X;\mathbb Z).
\]
The only nonzero group is therefore \(\widetilde H_{N-4}\cong\mathbb Z^{r_n}\). Every facet of \(\Delta_3\) is complementary to three vertices, so its dimension is \(N-4\). As \(X\) has no face with more than four vertices, the cut complex contains the full \((N-6)\)-skeleton of the \((N-1)\)-simplex, and is consequently \((N-7)\)-connected. Here \(N\ge8\). Its vanishing homology in the next two degrees, followed by the Hurewicz theorem in succession, shows that it is actually \((N-5)\)-connected. Choosing integral generators in degree \(N-4\), the resulting map from \(\bigvee^{r_n}S^{N-4}\) induces a homology isomorphism between simply connected CW complexes; Whitehead's theorem makes it a homotopy equivalence. Substituting \(N=2n\) completes the proof.

## Verification

The standalone `verify_mobius_cut.py` constructs \(X\) independently from connected triples and verifies every listed elementary collapse, including literal free-face tests. For each \(4\le n\le13\), it confirms the dual face vector, all collapses, the connected residual graph, and the rank formula. For \(4\le n\le7\), it exhaustively compares both characterizations of dual membership against the actual ordinary cut facets for every one of the \(2^{2n}\) subsets, and checks the cut Euler characteristic. For \(n=4,5,6\), an independent mod-two simplicial boundary reduction gives the predicted cut homology. These finite tests corroborate, rather than replace, the uniform proof above.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue introduce ordinary cut complexes and develop homotopy theory for trees, cycles, complete multipartite graphs, and other classes [1]; their sequel studies disjoint unions, squared paths and rectangular grids [2]. Neither inspected work gives the stated classification of Möbius ladders. Agarwal and Basak explicitly list the cut-complex topology of Möbius ladders as a question for further study [3, Problem 19]; their theorems concern independence and perfect-matching complexes.

A separately indexed result for the **ordinary** three-cut complexes of circular ladders \(C_n\square K_2\) has the same sphere number \(2n(n-4)+1\) for \(n\ge5\). The circular ladder and Möbius ladder are distinct graphs: their bipartiteness is opposite for every \(n\). That result, by itself, does not imply the present twisted-ladder classification. Likewise a separately indexed **total** three-cut result on Möbius ladders studies a different simplicial complex, with different homotopy dimensions. The present local collapses also lie outside square-edge-disjoint hypotheses used in related general cut-complex work, since every rung belongs to two four-cycles.

## Limitations

The proof applies to the ordinary three-cut complexes only, and only for \(n\ge4\). It gives their nonequivariant integral homotopy types, not explicit equivariant representations, shellings, or the homotopy types for other cut parameters. The direct finite computations stop at the ranges stated; no infinite statement is inferred from the tests. The literature comparison cannot exclude unindexed or inaccessible equivalent results, and independently conducted audit has not been performed.

## References

[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first publicly posted 2023-04-26, https://arxiv.org/abs/2304.13675.

[2] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first publicly posted 2024-07-11, https://arxiv.org/abs/2407.08158.

[3] A. Agarwal, B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601, first publicly posted 2026-08-31, https://arxiv.org/abs/2608.30601.
