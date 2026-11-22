# A local sharpness criterion for the tree equidistant bound and a complete reduced-tree spectrum

## Finding
Let \(T\) be any finite tree with at least two vertices and bipartition \(V(T)=A\sqcup B\). A *distance-equalizer set* \(S\) requires that for every distinct \(x,y\notin S\), some \(w\in S\) satisfies \(d(w,x)=d(w,y)\). A vertex is a *leaf* if it has degree one.

**Local class criterion.** For either bipartition class \(X\in\{A,B\}\), the entire class \(X\) is a distance-equalizer set **if and only if** every degree-two vertex outside \(X\) has at least one leaf neighbor.

**Exact sharpness criterion.** Write \(m=\min\{|A|,|B|\}\). The general bipartite lower bound \(\operatorname{eqdim}(T)\ge m\) is an equality **if and only if** at least one bipartition class of size \(m\) satisfies the local class criterion. The minimum sets in this equality case are exactly those size-\(m\) bipartition classes satisfying the criterion.

**All-set rigidity and spectrum.** The family of *all* distance-equalizer sets is precisely the union of the supersets of \(A\) and the supersets of \(B\) **if and only if** every degree-two vertex of \(T\) has a leaf neighbor. In this case the complete cardinality polynomial is
\[
Q_T(z)=z^{|A|}(1+z)^{|B|}+z^{|B|}(1+z)^{|A|}-z^{|V(T)|}.
\]
In particular, this exact spectrum and sharp equidistant dimension hold for every *homeomorphically irreducible tree* (a tree without degree-two vertices). The polynomial depends only on the two bipartition sizes, not on the arrangement of branching vertices.

## Assumptions and scope
All graphs are finite simple unweighted undirected trees; \(|V(T)|\ge2\). Bipartition classes are nonempty. Cardinality polynomials count labeled vertex subsets, not orbits under tree automorphisms. An *equalizer* is not an ordinary resolving set: equality of two distances, rather than inequality, is required. Only the sharpness of the known bipartition lower bound is classified for arbitrary trees; when the bound fails, no formula for the actual minimum is asserted.

## Proof
**Lemma 1 (parity obstruction).** For any connected bipartite graph with bipartition \(A\sqcup B\), no vertex is equidistant from a vertex in \(A\) and one in \(B\): their distances have different parities. Therefore every distance-equalizer set contains \(A\) or contains \(B\). This is the previously established bipartite lower-bound principle [1].

**Lemma 2 (tree midpoint geometry).** If distinct vertices \(x,y\) of a tree have even distance, let \(v\) be the unique midpoint on their path. The vertices equidistant from \(x,y\) are exactly \(v\) and the vertices in the components reached by leaving their path at \(v\) along an off-path edge. Indeed, for any \(w\), let \(p\) be the unique intersection of the paths from \(w\) to \(x\) and \(y\) with the \(x\)-\(y\) path. Then
\[
d(w,x)-d(w,y)=d(p,x)-d(p,y),
\]
which vanishes exactly when \(p=v\). In particular, if \(v\) has degree two, \(v\) is its own pair's only equalizer.

**Necessity of the local criterion.** Fix a class \(X\), and write \(Y=V(T)\setminus X\). Suppose \(v\in Y\) has degree two and both neighbors \(a,b\in X\) are nonleaves. Pick \(x\ne v\) adjacent to \(a\) and \(y\ne v\) adjacent to \(b\). Since \(T\) is a tree, \(x,y\) are distinct and lie in \(Y\). Their unique path is \(x-a-v-b-y\), with degree-two midpoint \(v\). By Lemma 2 their only equalizer is \(v\notin X\). Hence \(X\) fails to equalize \(x,y\).

**Sufficiency of the local criterion.** Assume every degree-two vertex in \(Y\) has a leaf neighbor. Take distinct \(x,y\in Y\). Their distance is even. Let \(v\) be their midpoint. If \(v\in X\), select \(w=v\). If \(v\in Y\), then \(v\) is an interior point of the \(x\)-\(y\) path and has degree at least two. If it had degree two, its two path neighbors would both have continuations toward \(x,y\in Y\), so neither could be a leaf (the distance from \(v\) to either of \(x,y\) is at least two). This contradicts the hypothesis. Therefore \(v\) has degree at least three. Choose a neighbor \(w\in X\) off the path. Its projection to the path is \(v\), so Lemma 2 gives \(d(w,x)=d(w,y)\). Thus \(X\) is a distance-equalizer set.

**Consequences.** Lemma 1 gives the lower bound \(m\) and forces every size-\(m\) equalizer to be a bipartition class of that size. The local criterion is therefore exactly the criterion for attaining that lower bound, including the case \(|A|=|B|\).

If every degree-two vertex has a leaf neighbor, the local criterion holds for both \(A\) and \(B\). Distance-equalizer sets are upward-closed under adding vertices, so every set containing either class works, and Lemma 1 excludes every other set. Conversely, if the family contains all supersets of either class, the two classes themselves work, forcing every degree-two vertex on both sides to have a leaf neighbor. For each class, count supersets by selecting an arbitrary subset of the opposite class. The only set counted twice is \(V(T)\); subtraction proves the displayed polynomial. A tree without degree-two vertices satisfies the hypothesis vacuously. \(\square\)

## Verification
Two different standalone checkers accompany the proof. `verify_trees.cpp` constructs every labeled tree by Prüfer sequences through seven vertices (plus 500 deterministic tests through twelve vertices), computes distance-equalizer feasibility directly from breadth-first-search distance tables for every vertex subset, and compares with the local class criterion, the sharpness condition, and the complete all-set description in its stated range. It reports `TREE_LOCAL_EQUALIZER_VERIFY_OK trees=18748 part_classes_valid=19090 both_classes_valid=5991`.

Independently, `verify_midpoints.py` reconstructs trees using a different Prüfer implementation, checks the conditions with direct shortest-path distances and complete subsets, and reports `TREE_MIDPOINT_INDEPENDENT_OK 1616`. The universal theorem follows from Lemmas 1–2 and the midpoint argument, not from the finite tests. Reproduce with `g++ -O3 -std=c++17 verify_trees.cpp -o verify_trees && ./verify_trees` and `python3 verify_midpoints.py`.

## Relationship to prior work
González, Hernando, and Mora [1] introduced distance-equalizer sets, proved that any equalizer of a bipartite graph contains an entire partite class, and left the general tree case as an open direction. Their exact path formulas use progression-free subsets, and their bistar formulas do not give this all-tree sharpness characterization or spectrum.

A previously published classification of three-edge balanced spiders [3] has a strict gap between the equidistant dimension and the smaller bipartition class; it treats a different special family. A later tree-conjecture discussion [4] supplies the elementary unique-midpoint obstruction for degree-two vertices, but does not establish the converse for arbitrary trees, the precise bipartition-bound sharpness criterion, or the complete polynomial for all trees meeting the criterion. The proof here combines parity, midpoint geometry, and the off-path branch alternative to obtain an iff statement across **all** trees. The 2024 general complexity/lexicographic-product paper [2] does not cover this tree characterization.

## Limitations
This is not an exact formula for the equidistant dimension of every tree: if both size-minimal bipartition classes fail the local criterion, more elaborate equalizers may be needed. The stated all-set polynomial applies precisely when every degree-two vertex has a leaf neighbor; it is not asserted for subdivided paths with long degree-two corridors. Both computational checks are finite corroboration only. Independent scientific and publication-priority audits remain unperformed; equivalent results in unindexed literature cannot be excluded.

## References
1. A. González, C. Hernando, M. Mora, *The Equidistant Dimension of Graphs*, arXiv:2107.10805v1 (2021-07-22), *Bull. Malays. Math. Sci. Soc.* 45 (2022), 1757–1775. https://arxiv.org/abs/2107.10805 ; https://doi.org/10.1007/s40840-022-01295-z .
2. A. Gispert-Fernández and J. A. Rodríguez-Velázquez, *The equidistant dimension of graphs: NP-completeness and the case of lexicographic product graphs*, *AIMS Mathematics* 9 (2024), 15404–15421. https://doi.org/10.3934/math.2024744 .
3. *Equidistant dimension and all bases of balanced three-edge spiders*, published research record (2026-10-12): https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-equidistant-dimension-and-all-bases-of-balanced-three-edge-spide--fe03141beba1 .
4. *Tree equidistant dimension conjecture*, MathDB community discussion (2026-08-27), https://mathdb.com/p/351395/tree-equidistant-dimension-conjecture .
