# Five new circles per stacking in simplicial doubles of three-spheres

## Finding
For every stacked simplicial three-sphere \(X\) on \(n\ge5\) vertices, its simplicial double \(D^2(X)\) is a connected graph, with
\[
 f_0(D^2(X))=4n-10,\qquad f_1(D^2(X))=9n-30.
\]
Consequently, its **integral homotopy type** is
\[
 \boxed{|D^2(X)|\simeq\bigvee^{5n-19}S^1.}
\]
Equivalently, \(\widetilde H_1(D^2(X);\mathbb Z)\cong\mathbb Z^{5n-19}\) and every other reduced integral homology group vanishes. Each stacking adds exactly five independent loops, for **every** choice of stacking facet.

## Assumptions and scope
A *stacked simplicial three-sphere* is formed by beginning with the tetrahedral-facet boundary of a four-simplex on five vertices and repeating the following operation: choose a tetrahedral facet \(F=\{a,b,c,d\}\), introduce a new vertex \(z\), delete \(F\) as a maximal facet, and replace it by the four tetrahedra \(\{z\}\cup(F\setminus\{u\})\), \(u\in F\). Proper faces of \(F\) remain present. These are precisely the boundary complexes obtained by stacking four-simplices, but no geometric realization is needed.

Use the simplicial double of Lesh, Schreiner and Wahl: a vertex of \(D^2(X)\) is a two-element face of \(X\); vertices \(e,e'\) span an edge exactly when \(e\cap e'=\varnothing\) and \(e\cup e'\) is a tetrahedral face of \(X\). Since \(\dim X=3\), no three double vertices form a simplex, so \(D^2(X)\) is a graph, with no higher simplices. Graph edges are unoriented and counted once. All homotopy and homology assertions are over the usual geometric realization and, for integral homology, over \(\mathbb Z\).

## Proof
**Step 1: The base graph.** For the boundary of a four-simplex, every pair of its five vertices is a face and every four-subset is a tetrahedral facet. Its double therefore has the ten two-subsets as vertices, with adjacency exactly when two two-subsets are disjoint. This is the Petersen graph, or \(\operatorname{KG}(5,2)\). It is connected: two distinct two-subsets are either disjoint and adjacent, or meet in one element and have the complement of their three-element union as a common neighbor. Each of its five tetrahedral facets contributes three edges, so it has 15 edges and first Betti number \(15-10+1=6\).

**Step 2: Exact local change under a stacking.** Let \(Y\) be the complex obtained by stacking the facet \(F=\{a,b,c,d\}\subset X\) using a new vertex \(z\). The only new edges of \(Y\) are \(za,zb,zc,zd\), so the double gains exactly four graph vertices. In the double graph, the deleted tetrahedron \(F\) previously contributed its three opposite-edge adjacencies
\[
 (ab,cd),\quad(ac,bd),\quad(ad,bc).
\]
Each new tetrahedron \(z(F\setminus\{u\})\) contributes exactly three opposite-edge adjacencies. All 12 resulting graph edges have one endpoint \(zv\), with \(v\in F\), and the other endpoint a two-element subset of \(F\setminus\{v\}\). These 12 edges are pairwise distinct, are different from all previously existing graph edges, and exhaust the new adjacencies. An opposite-edge adjacency determines its unique four-element union (the corresponding tetrahedron), so no double counting is possible. Thus the double loses 3 edges and gains 12: the net change is +9 edges.

**Step 3: Connectivity is preserved.** Consider the local replacement graph \(B_F\) on the six old pair-vertices \(ab,ac,ad,bc,bd,cd\) and four new vertices \(za,zb,zc,zd\), with the 12 incidence edges just described. This graph is connected. Indeed, any two new vertices \(zu,zv\) share as a neighbor the pair-vertex \(F\setminus\{u,v\}\); and each old pair-vertex \(uv\) is adjacent to both \(zw\) with \(w\in F\setminus\{u,v\}\). Hence all ten local vertices lie in a single connected component.

Suppose \(D^2(X)\) is connected. Any old path between old graph vertices can be transformed into a walk in \(D^2(Y)\) by replacing an occurrence of one of the three deleted opposite-edge adjacencies by a path in \(B_F\) between its old endpoints. Therefore all old graph vertices remain mutually connected. The four new vertices connect to the old ones through \(B_F\), proving that \(D^2(Y)\) is connected. This applies regardless of the facet selected. Induction starting from Step 1 proves connectivity for all stacking histories.

**Step 4: Homotopy type and counts.** After \(k=n-5\) stackings, the original edge count is \(10+4k=4n-10\), the number of tetrahedral facets is \(5+3k=3n-10\), and the double has exactly three graph edges per facet; hence its edge count is \(3(3n-10)=9n-30\), agreeing with Step 2. A connected finite graph contracts a spanning tree to a wedge of \(E-V+1\) circles. Consequently its first Betti number is \((9n-30)-(4n-10)+1=5n-19\), proving the displayed integral homotopy equivalence and all integral homology claims. No finite-sample inference enters this argument.

## Verification
The self-contained standard-library program `stacked_double_verify.py` reconstructs the four-dimensional facet-stacking operation, forms the double graph directly from opposite-edge partitions of each tetrahedron, and checks exact connected-component, vertex, edge, facet and cycle-rank counts. It examines *all stacking histories* of lengths zero to three (\(1,5,40,440\) histories at \(n=5,6,7,8\)) and 40 pseudorandom histories each at \(n=9,12,16,20\). The recorded output is in `stacked_double_output.txt`; the executable verdict is `STACKED_DOUBLE_PASS`. The exhaustive finite histories are corroboration, not the proof of the universal theorem. The proof above is combinatorial and establishes every value \(n\ge5\).

## Relationship to prior work
Lesh, Schreiner and Wahl introduced the general simplicial doubling operation and proved a weak Cohen–Macaulay connectivity bound (arXiv:2506.10436, first public 2025-06-12). Their Theorem A at dimension three and doubling parameter two yields only the weak bound corresponding to dimension zero; it does not classify these doubles or assert connectivity. The older theory of stacked polytopes supplies the stacking operation and standard face counts, neither claimed as new.

The recorded classification of doubles of cyclic four-polytope boundaries treats a *different* family of simplicial three-spheres: there is a parity obstruction to connectivity for even vertex counts. This contrasts with the stacking-preserved connectivity here. At five vertices both constructions start from the four-simplex boundary, so that base-case Petersen graph is previously covered and is not separately claimed as novel. For six or more vertices, the stacked and cyclic boundaries have different tetrahedral-facet counts, and the cyclic classification neither contains nor implies the present family. The contribution is the local connectivity-preserving replacement lemma and the resulting complete infinite-family integral homotopy classification.

## Limitations
The theorem is about first simplicial doubles of stacked three-spheres. It does not classify general nonstacked simplicial three-spheres, higher-dimensional stackings, higher tuplings, or equivariant representations. All homotopy equivalences are nonequivariant. The first public date is that of the motivating definition, not a date of the new result. A further prior paper under alternative terminology for tetrahedral opposite-edge graphs could exist; full independence and external validation have not been established.

## References
[1] Kathryn Lesh, Bridget Schreiner, Nathalie Wahl, *The double of a simplicial complex*, arXiv:2506.10436, first public submission 2025-06-12, Definition 2.1, Theorem A, and Sections 2–4. https://arxiv.org/html/2506.10436v2

[2] *Parity and dihedral homology of the doubled cyclic four-polytope boundary*, publicly accessible research record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-parity-and-dihedral-homology-of-the-doubled-cyclic-four-polytope--1160db5d31ae (RESULT.md, homotopy classification and component analysis).

[3] *Apollonian Ball Packings and Stacked Polytopes*, Discrete & Computational Geometry (2016), Section 2.4, definition and characterization of stacked polytopes. https://link.springer.com/article/10.1007/s00454-016-9777-3
