# A 1081-circle simplicial double of the regular 600-cell

## Finding

Let \(P\subset\mathbb R^4\) be the regular 600-cell with tetrahedral facets, and let \(X=\partial P\) be its abstract boundary simplicial complex. Define its *simplicial double* \(D^2(X)\) to have as vertices the edges of \(X\); a collection of \(k+1\) such edges is a \(k\)-simplex precisely when the edges are pairwise vertex-disjoint and their union is a \((2k+1)\)-simplex of \(X\).

**Theorem.** The double \(D^2(\partial P)\) is a connected, 5-regular graph with 720 vertices, 1800 edges and girth six, and

\[
|D^2(\partial P)|\simeq\bigvee^{1081}S^1.
\]

Consequently \(\pi_1(|D^2(\partial P)|)\) is the free group of rank 1081, \(\widetilde H_1(-;\mathbb Z)\cong\mathbb Z^{1081}\), and all other reduced integral homology groups vanish.

## Assumptions and scope

The 600-cell is the usual convex regular four-polytope with Schläfli symbol \(\{3,3,5\}\). Faces of the double are defined by the Lesh–Schreiner–Wahl construction, *not* by graph-theoretic bipartite doubling or the full matching complex. Since \(\partial P\) is three-dimensional, its double has dimension at most one: three pairwise disjoint original edges would require a five-simplex, which does not exist. A double edge is therefore exactly a pair of *opposite edges* in one tetrahedral facet. The assertion is a finite exact classification; no family of other polytopes or symmetry representation is asserted.

## Proof

1. Put \(\varphi=(1+\sqrt5)/2\) and realize the 600-cell at circumradius two using the 120 standard points of the following three types: eight coordinate placements of \((\pm2,0,0,0)\), all sixteen sign choices of \((\pm1,\pm1,\pm1,\pm1)\), and the 96 even permutations of \((0,\pm1,\pm\varphi,\pm(\varphi-1))\). These are the standard Coxeter coordinates also tabulated by MathWorld. Use the order \(A,B,C\) and within each family the explicit lexicographic generation in `verify_600.py`. All coordinate arithmetic is carried out in \(\mathbb Z[\varphi]\), with the relation \(\varphi^2=\varphi+1\).

2. For two distinct vertices \(u,v\) on the radius-two sphere, the short edges of the 600-cell are precisely the pairs satisfying \(\langle u,v\rangle=2\varphi\). Exact enumeration gives 720 such edges, and every coordinate vertex has 12 neighbors. It enumerates exactly 600 four-cliques. To distinguish actual polytope facets from merely combinatorial cliques, for every listed four-clique \(F\), set \(s_F=\sum_{v\in F}v\). Direct exact sign tests establish

\[
\langle s_F,u\rangle\le4+6\varphi\quad\text{for all 120 vertices }u,
\]

with equality *if and only if* \(u\in F\). Thus each listed clique is an exposed tetrahedral facet. The standard 600-cell has exactly 600 tetrahedral facets; hence this is the complete facet set. As corroboration, these facets contain 1200 distinct triangles, each in exactly two facets.

3. Each tetrahedron has exactly three unordered pairs of opposite edges. Enumerate those pairs and identify an original edge with a vertex of the double. Exact enumeration establishes 720 double vertices, 1800 *distinct* double edges and five neighbors at every double vertex. There are no higher-dimensional simplices by the dimensional argument above.

4. Connectivity is the substantive step: `spanning_tree.json` contains an explicit spanning-tree parent array indexed by the *lexicographically sorted 720 original edges*. It has a unique root at index zero; for each of the other 719 entries the indicated parent is an actual opposite-edge neighbor in the double, and iterating parents reaches index zero without a cycle. The standard-library verifier reconstructs all original facets and double incidences independently of the parent array, checks every parent relation and path, and also recomputes a breadth-first-search tree. Thus the double is connected. Exhaustive graph-distance checks also give girth exactly six.

5. A connected finite graph with \(V\) vertices and \(E\) edges deformation-retracts after contracting a spanning tree to a wedge of \(E-V+1\) circles. Here

\[
E-V+1=1800-720+1=1081.
\]

This proves the complete homotopy and integral homology claims. The last reduction is topological, not an inference from finite-field homology.

## Verification

The bundled self-contained files are `verify_600.py`, `spanning_tree.json`, and `verify_output.txt`. On Python 3, run `python verify_600.py` from the directory containing all three. It prints `exact_arithmetic_certificate=PASS`. The implementation uses integer pairs for algebraic numbers \(a+b\varphi\), integer-only exact sign comparisons in \(\mathbb Q(\sqrt5)\), exhaustive four-clique generation, 600 supporting-hyperplane tests against all 120 vertices, 719 spanning-tree parent checks and an all-root girth search. The explicit certificate, not a floating-point approximation, proves connectivity. The separate numerical convex-hull check used during development agreed on the entire facet set, but is not required for this proof and is not cited as an independent certificate.

## Relationship to prior work

The definition of doubling and a general weak connectivity bound come from Lesh, Schreiner and Wahl, arXiv:2506.10436, originally public 12 June 2025. Their general result does not determine the double of the 600-cell, its connectivity, or its integral first Betti number. Published calculations for doubles of cyclic four-polytope boundaries and stacked three-spheres concern different facet systems; their formulas cannot be specialized to the regular 600-cell. The well-known 120-vertex, 720-edge **skeleton graph** of the 600-cell is a different object from the 720-vertex opposite-edge double classified here. The numerical data about the 600-cell itself are classical; the proposed new assertion is the connectedness and resulting exact homotopy type of its simplicial double.

## Limitations

The computation concerns this one regular 4-polytope and the ordinary nonequivariant homotopy type. It does not determine the induced 600-cell symmetry representation, torsion in finite-group quotients, or higher-tupling operations. The proof relies on an executable finite exact certificate and the standard geometric identification of the 600-cell. An equivalent result under a different graph name cannot be excluded by literature searches; mathematical verification and publication priority have not been independently audited.

## References

1. K. Lesh, B. Schreiner and N. Wahl, *The double of a simplicial complex*, arXiv:2506.10436 (first public version 12 June 2025), https://arxiv.org/abs/2506.10436 ; full text https://arxiv.org/html/2506.10436v2 .
2. E. W. Weisstein, *600-Cell*, MathWorld, https://mathworld.wolfram.com/600-Cell.html (standard coordinates and facet/edge counts).
3. E. W. Weisstein, *600-Cell Graph*, MathWorld, https://mathworld.wolfram.com/600-CellGraph.html (distinguishes the original graph).
