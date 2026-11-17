# A universal three-sphere wedge theorem for high-girth non-matching complexes

## Finding
**Theorem.** Let \(G=(V,E)\) be any finite connected simple graph with at least one edge and girth at least six (with infinite girth for a forest). Let \(\nu(F)\) denote the matching number of the edge-induced subgraph \((V,F)\) for \(F\subseteq E\), and set
\[
\operatorname{NM}_3(G)=\{F\subseteq E:\nu(F)\le2\},\qquad b=|E|-|V|+1.
\]
Then, including trees with \(b=0\),
\[
\boxed{|\operatorname{NM}_3(G)|\simeq\bigvee^{\binom{b+1}{2}}S^3.}
\]
Here a wedge of zero spheres denotes a point. Thus the only potentially nonzero reduced integral homology group is \(\widetilde H_3\cong\mathbb Z^{\binom{b+1}{2}}\). No bipartiteness, regularity or upper bound on the number of vertices is assumed.

## Assumptions and scope
Graphs are finite, simple, undirected and connected, with \(|E|\ge1\). A graph without cycles has girth infinity. The vertices of \(\operatorname{NM}_3(G)\) are *edges of the graph*, not vertices of the graph: simplices are edge collections having no three pairwise disjoint edges. All realizations and homotopy equivalences are ordinary nonequivariant CW homotopy equivalences; coefficients in the displayed integral homology statement are \(\mathbb Z\). For an intermediate spanning subgraph \(H\), write \(b(H)=|E(H)|-|V(H)|+1\), and \(E_H(v)\) for its incident-edge set.

## Proof
**1. Two-cover characterization.** Any selected edge subgraph \((V,F)\) with \(\nu(F)\le2\) contains no odd cycle: the ambient graph has no odd cycle shorter than seven, and a cycle of length at least seven has a matching of size at least three. The selected subgraph is therefore bipartite. By König's matching–vertex-cover theorem, \(\nu(F)\le2\) if and only if some set of at most two vertices meets every edge of \(F\). This characterization applies to every subgraph of \(G\), including nonbipartite \(G\) itself.

**2. One-matching complex.** For a connected triangle-free graph \(H\) with at least one edge, set \(M(H)=\{F\subseteq E(H):\nu(F)\le1\}\). Every nonempty pairwise-intersecting edge family in a triangle-free simple graph is a subset of a single vertex-star. Hence \(M(H)=\bigcup_{v\in V(H)}\Delta(E_H(v))\). Intersections of two distinct nonempty star simplices are one vertex if their graph vertices are adjacent, and empty otherwise; no three distinct stars have nonempty intersection. The simplicial nerve lemma consequently gives \(M(H)\simeq H\simeq\bigvee^{b(H)}S^1\). All star simplices belong to the same component of \(M(H)\).

**3. Trees yield contractible complexes.** Suppose a tree \(T\) has a leaf \(v\), neighboring vertex \(a\), and leaf edge \(e=av\). Put \(H=T-v\). For \(H\) with at least one edge, the link of the vertex \(e\) in \(\operatorname{NM}_3(T)\) is
\[
\operatorname{lk}_e=\bigcup_{w\in V(H)}\Delta(E_H(a)\cup E_H(w)).
\]
Indeed a two-vertex cover of a face together with \(e\) includes \(a\) or \(v\); if it includes \(v\), the other cover vertex alone covers all edges of the face in \(H\), which is also covered by \(a\) and that vertex. Conversely every displayed simplex gives a two-cover \(\{a,w\}\). The link is a cone with any fixed edge in the nonempty set \(E_H(a)\) as apex. Therefore adjoining the cone on this contractible link leaves the homotopy type of \(\operatorname{NM}_3(H)\) unchanged. The single-edge tree has a point as its complex. Leaf induction proves contractibility for every nontrivial tree.

**4. The edge-insertion link.** Let \(H\) be a connected spanning subgraph of \(G\), and let \(e=ab\in E(G)\setminus E(H)\). The girth assumption forbids paths in \(H\) from \(a\) to \(b\) of lengths two, three or four. Put \(A=E_H(a)\) and \(B=E_H(b)\), two nonempty disjoint sets of graph edges. The link \(L_e=\operatorname{lk}_{e}\operatorname{NM}_3(H+e)\) is, by Step 1,
\[
L_e=K_a\cup K_b,\qquad K_a=\bigcup_{w\in V(H)}\Delta(A\cup E_H(w)),\quad K_b=\bigcup_{w\in V(H)}\Delta(B\cup E_H(w)).
\]
Each \(K_a\) is a cone with any edge of \(A\) as apex, and likewise \(K_b\) is a cone. We claim the **exact simplicial intersection** is
\[
K_a\cap K_b=M(H)\cup\Delta(A\cup B),\qquad M(H)\cap\Delta(A\cup B)=\Delta(A)\sqcup\Delta(B).
\]
Every star face belongs to both \(K_a\) and \(K_b\). The simplex on \(A\cup B\) belongs to \(K_a\) (choose \(w=b\)) and \(K_b\) (choose \(w=a\)). Conversely, take a face \(F\) in both but not in \(M(H)\). If it contains no edge of \(A\), then membership of \(K_a\) makes \(F\) a star, impossible; the same argument gives an edge of \(B\). Choose \(ax\in F\cap A\) and \(by\in F\cap B\). If another selected edge \(h\in F\setminus(A\cup B)\) existed, membership in \(K_a\) forces it to intersect \(by\), while membership in \(K_b\) forces it to intersect \(ax\). Necessarily \(h=xy\), producing the forbidden three-edge path \(a-x-y-b\). Thus \(F\subseteq A\cup B\), as claimed. Since no edge of \(A\) intersects an edge of \(B\) (otherwise \(a,b\) have a common neighbor), the second intersection formula follows.

**5. Homotopy type of the link.** The two nonempty simplices \(\Delta(A)\), \(\Delta(B)\) are disjoint in the geometric realization, and they lie in the same connected component of \(M(H)\). The homotopy pushout obtained by attaching the contractible simplex \(\Delta(A\cup B)\) along its two disjoint contractible subcomplexes adds one independent loop to \(M(H)\). Thus
\[
K_a\cap K_b\simeq M(H)\vee S^1\simeq\bigvee^{b(H)+1}S^1.
\]
Since \(K_a,K_b\) are contractible and their intersection is connected, the homotopy pushout of the two cones gives
\[
L_e\simeq\Sigma(K_a\cap K_b)\simeq\bigvee^{b(H)+1}S^2.
\]
These equivalences use inclusions of simplicial subcomplexes (CW cofibrations), so ordinary homotopy pushout statements apply.

**6. Induction on cycle rank.** Choose a spanning tree of \(G\) and insert its \(b\) remaining edges in any order. At a stage \(H\subseteq G\), the new complex is exactly
\[
\operatorname{NM}_3(H+e)=\operatorname{NM}_3(H)\cup_{L_e}(e*L_e).
\]
By Step 3 the starting complex is contractible. Inductively suppose \(\operatorname{NM}_3(H)\) is a wedge of three-spheres, hence is two-connected. From Step 5, \(L_e\) is a wedge of two-spheres; every map \(L_e\to\operatorname{NM}_3(H)\) is nullhomotopic because \(\pi_2(\operatorname{NM}_3(H))=0\). Attaching the cone therefore yields
\[
\operatorname{NM}_3(H+e)\simeq\operatorname{NM}_3(H)\vee\Sigma L_e\simeq\operatorname{NM}_3(H)\vee\bigvee^{b(H)+1}S^3.
\]
The successive previous cycle ranks are \(0,1,\ldots,b-1\). Thus the total sphere count is \(1+2+\cdots+b=\binom{b+1}{2}\). As all equivalences are integral CW homotopy equivalences, the integral homology conclusion follows. \(\square\)

## Verification
The standalone standard-library program `checks/verify.py` constructs faces independently both by exhaustive three-matching avoidance and by existence of a two-vertex cover. It computes exact mod-two reduced homology for nine distinct girth-at-least-six graphs, and checks the **entire simplicial** edge-insertion link formula and both constituent-cover/intersection formulas for each of the chord additions in the tests. The tested graphs include a path, cycles of lengths six through nine, a cycle with a leaf, a three-arm theta graph, two six-cycles meeting at a vertex, and two six-cycles joined by a bridge. All nine checks passed, including two graphs with cycle rank two and predicted three three-spheres. The program's captured output is `checks/verify_output.txt`. Finite computation is corroboration only: Steps 1–6 prove the theorem for every permitted graph and over \(\mathbb Z\).

## Relationship to prior work
Shan and Wang (2026, Theorems 2.1 and 2.3) prove injectivity of top non-matching homology under bipartite edge additions and the existence of a nonzero top-dimensional class under a long-cycle hypothesis; neither yields the exact integral homotopy type, uniform multiplicity, or nonbipartite scope established here. Holmsen and Lee (2020) give general Leray-number upper bounds, while Linusson–Shareshian–Welker classify complete and complete-bipartite graph cases.

Two previously available uniform theorems give exactly the same binomial count but study **different** complexes: the total-three-cut Alexander dual \(\{S\subseteq V(G):\alpha(G[S])\le2\}\) for high-girth graphs, and the three-robust clique complex \(I_3(G)\) for bipartite graphs. Their simplicial vertices are \(V(G)\), whereas the present non-matching complex is on \(E(G)\); identification with \(I_3(L(G))\) does not apply those results because line graphs of graphs having degree at least three contain triangles. Earlier individual matching-avoidance calculations for the Heawood, Möbius–Kantor, Pappus, and Nauru graphs are encompassed, not claimed as new special cases. The new contribution is an all-parameter **edge-link suspension and two-cover proof** for matching-avoidance complexes, even for nonbipartite high-girth graphs.

## Limitations
The theorem requires connected simple graphs of girth at least six and matching threshold three. It does not determine higher thresholds, edge-cut variants, functorial/equivariant identifications, or the homotopy type for graphs with triangles, four-cycles, or pentagons. Known individual instances are not new by themselves. Bibliographic searches and targeted full-text comparisons cannot exclude unindexed equivalent statements; independent mathematical validation has not been performed.

## References
1. J. Shan and Z. Wang, *Homology of non-matching complexes under edge additions and applications to their Stanley–Reisner ideals*, arXiv:2609.02621 (first public 2026-09-02), especially Theorems 2.1–2.3. https://arxiv.org/abs/2609.02621
2. A. F. Holmsen and S. Lee, *Leray numbers of complexes of graphs with bounded matching number*, arXiv:2003.11270 (2020). https://arxiv.org/abs/2003.11270
3. S. Linusson, J. Shareshian, and V. Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345 (2004). https://arxiv.org/abs/math/0410345
4. *Cycle-rank homology of total three-cut complexes of high-girth graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-cycle-rank-homology-of-total-three-cut-complexes-of-high-girth-g--9341d892cb0d
5. *A three-sphere wedge theorem for robust clique complexes of all connected bipartite graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-three-sphere-wedge-theorem-for-robust-clique-complexes-of-all--8d06720b1a2b
6. *Three-nonmatching complexes of square bouquets: sphere splitting and integral symmetry*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-nonmatching-complexes-of-square-bouquets-sphere-splitting--841d62e758ac
