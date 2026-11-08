# An infinite family of tree line graphs not identifiable by color refinement

## Finding

**Theorem.** For every integer \(m\ge2\), there is an explicit tree \(T_m\) on \(6m+2\) vertices such that its \((6m+1)\)-vertex line graph \(G_m=L(T_m)\) and an explicit nonisomorphic graph \(H_m\) have identical color-refinement profiles at every iteration. In fact the two are equivalent in two-variable first-order logic with counting, yet have different numbers of triangles:
\[
\#K_3(G_m)-\#K_3(H_m)=4m-4>0.
\]
Consequently, although all forests are amenable to color refinement, **taking line graphs does not preserve amenability, even on trees**. The smallest displayed member has a fourteen-vertex tree, two thirteen-vertex comparison graphs, and triangle counts \(20\) and \(16\); no minimum-order assertion is made.

## Assumptions and scope

Graphs are finite, simple, undirected, and uncolored. The line graph \(L(T)\) has the edges of \(T\) as vertices and joins two exactly when their edges share an endpoint. Color refinement starts with one color, then replaces every vertex color by its current color together with the multiset of its neighbors' colors. Graphs are color-refinement equivalent when the multisets of colors in both graphs agree after every iteration of joint refinement. By the standard correspondence, this is equivalence for first-order logic with two variables and counting quantifiers (at arbitrary finite quantifier depth). A graph is *amenable* if color refinement distinguishes it from every nonisomorphic graph.

For \(m\ge2\), construct \(T_m\) from two adjacent centers \(A,B\). At each center attach \(m\) pendant edges and \(m\) internally disjoint arms of length two. This has \(2+6m\) vertices and \(1+6m\) edges. In \(G_m\), call the line-graph vertex corresponding to the central edge \(b\); call the \(2m\) direct pendant edges \(U\), the \(2m\) first edges of length-two arms \(V\), and the \(2m\) distal edges \(Z\). Label their centers by subscripts \(A,B\), with \(m\) members of each applicable family at each center.

Form \(H_m\) by deleting the two \(U\)-\(V\) edges \(u_{A,1}v_{A,1}\) and \(u_{B,1}v_{B,1}\) from \(G_m\) and adding the cross-edges \(u_{A,1}v_{B,1}\) and \(u_{B,1}v_{A,1}\). These added edges were previously absent.

## Proof

**Equitable degree partition.** In \(G_m\), degrees of \(b,U,V,Z\) are respectively \(4m,2m,2m+1,1\), distinct when \(m\ge2\). Each class has the following neighbor-count profile into \((\{b\},U,V,Z)\):
\[
\begin{array}{c|rrrr}
 &\{b\}&U&V&Z\\\hline
b&0&2m&2m&0\\
U&1&m-1&m&0\\
V&1&m&m-1&1\\
Z&0&0&1&0
\end{array}
\]
The two-edge switch does not change these counts. In particular every affected \(U\)-vertex loses one \(V\)-neighbor and gains a different \(V\)-neighbor; the same holds with \(U,V\) reversed. All other class-to-class adjacencies are unchanged. Thus the degree partition is equitable in both graphs with identical quotient matrix and class sizes \((1,2m,2m,2m)\). Because its four degree values are pairwise different, it is already the stable color-refinement partition, with corresponding colors and multiplicities equal in both graphs. Hence no iteration of color refinement distinguishes \(G_m,H_m\), and their counting two-variable theories coincide.

**Triangle deficit.** Since \(T_m\) is a tree, every triangle in its line graph comes from three distinct edges incident to a common tree vertex. The only vertices of degree at least three in \(T_m\) are its two centers, each of degree \(2m+1\). Therefore
\[
\#K_3(G_m)=2\binom{2m+1}{3}.
\]
Each deleted within-center edge in \(G_m\) belongs to exactly \(2m-1\) triangles (one for each of the other vertices in its center clique). The two deletions affect disjoint center cliques. Each added cross-edge has exactly one common neighbor of its endpoints, namely \(b\), and the two added edges cannot together participate in a triangle. Consequently
\[
\#K_3(H_m)=2\binom{2m+1}{3}-2(2m-1)+2
=2\binom{2m+1}{3}-4m+4.
\]
For all \(m\ge2\), the two graphs are nonisomorphic. As \(T_m\) is a tree and its line graph fails identification by color refinement, the claimed closure failure follows. This reasoning applies to every positive integer \(m\ge2\), not merely the tested examples.

## Verification

`verify.py` uses only the Python standard library. It constructs \(T_m\), its line graph, and the switched comparison graph for each integer \(2\le m\le6\); checks degree profiles, stable color-refinement multisets after multiple rounds on the disjoint union, the edge-switch specification, and the two exact triangle formulas. All tests passed, including the fourteen-vertex tree at \(m=2\). These finite checks corroborate the proof; the infinite family follows algebraically from the quotient matrix and triangle count.

## Relationship to prior work

Arvind, Köbler, Rattan, and Verbitsky [1] characterize graphs amenable to color refinement and prove in Corollary 10 that every forest is amenable. Their results make failure of amenability for line graphs a natural closure question. Their general characterization could in principle verify any particular example, but it does not itself state the explicit switched tree-line-graph family or its exact triangle deficit. The present construction gives explicit comparison witnesses at every size \(6m+1\) for \(m\ge2\). Color-refinement equivalence and its interpretation in two-variable counting logic are classical. A historical source with an earlier line-graph closure counterexample may exist; the literature search is not exhaustive.

## Limitations

The theorem does not claim that the exhibited thirteen-vertex graph is a smallest possible example, nor that the comparison graph \(H_m\) is itself the line graph of a tree. It demonstrates failure of global amenability, not failure of relative color-refinement identification *among* line graphs of trees. It does not assert that arbitrary tree line graphs are unidentifiable. The visible switch is an elementary construction, but the theorem supplies an infinite motivated counterfamily with explicit unbounded triangle deficit. Independent validation and exhaustive historical priority checks remain outstanding.

## References

[1] V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first submitted 2015-02-04. Especially Definition 2 and Corollary 10. https://arxiv.org/abs/1502.01255
