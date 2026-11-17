# Five integral three-spheres in the second independence complex of \(\mathrm{KG}(6,2)\)

## Finding
Let \(G=\mathrm{KG}(6,2)\), the fifteen-vertex Kneser graph on two-subsets of a six-element set, with adjacency defined by disjointness. Let \(X=\operatorname{Ind}_2(G)\) consist of vertex subsets whose induced connected components each have at most two vertices. Then
\[
 X\simeq\bigvee^{5} S^{3}.
\]
Consequently its reduced integral homology equals \(\mathbb Z^5\) in degree three and vanishes in all other degrees. This is a statement about homotopy type, not only Betti numbers.

## Assumptions and scope
The ground set is exactly \(\{1,2,3,4,5,6\}\); the vertices of \(G\) are all fifteen unordered two-element subsets, ordered lexicographically. A pair of graph vertices is joined if and only if their two-element labels are disjoint. No loops or multiple edges are allowed. For a face \(F\subseteq V(G)\), the induced graph \(G[F]\) has components of order at most two if and only if each selected vertex has at most one selected neighbor. All quantification and all computational enumeration refer to this fixed finite graph.

## Proof
**1. Exact face criterion.** Number the graph vertices in lexicographic order by indices \(0,\ldots,14\). Represent each nonempty candidate face by its fifteen-bit characteristic mask \(m\). For every selected index \(i\), count the selected indices \(j\) for which the corresponding two-subsets are disjoint. This count is the degree of vertex \(i\) inside \(G[F]\). A finite simple graph has all components of order at most two exactly when all these degrees are at most one. Thus this test is necessary and sufficient for face membership, without a sampling assumption.

**2. Complete enumeration.** Apply the criterion to every integer mask in the inclusive range \(1\) to \(2^{15}-1\). Exactly 746 masks pass, with numbers of faces in dimensions zero through five equal to
\[
 (15,105,260,255,96,15).
\]
As a logically separate face test, enumerate all forbidden three-vertex sets whose induced graph has at least two edges (195 such triples), and verify that a mask passes the degree test exactly when it contains none of those triples. This tests all \(2^{15}-1\) nonempty masks.

**3. Fully specified matching.** Start with all nonempty faces unmatched. For pivots \(i=0,1,\ldots,14\), in that order, scan the currently unmatched face masks in increasing numerical order. Whenever \(m\) does not contain bit \(i\) and both \(m\) and \(m\cup\{i\}\) are currently unmatched faces, match these two faces and remove both from further consideration. Every pair differs in exactly one vertex, so this is a legitimate partial matching of the face Hasse diagram. It has exactly 370 pairs and six critical faces, with masks
\[
 1,\ 5664,\ 10784,\ 19488,\ 28736,\ 29184.
\]
The first is a zero-cell and each other mask has four set bits, hence dimension three.

**4. Exact acyclicity.** For every Hasse covering relation between nonempty faces \(\sigma\subset\tau\), direct it from \(\sigma\) to \(\tau\) when that pair belongs to the matching, and from \(\tau\) to \(\sigma\) otherwise. There are exactly 2580 such covering relations. The standalone verifier constructs all of them, applies this orientation, and removes all 746 vertices of the directed graph by topological sorting. Since a finite directed graph permits such a complete topological ordering if and only if it is acyclic, the matching is acyclic. This is an exhaustive finite certificate, not an inference from random trials.

**5. Integral homotopy conclusion.** The acyclic-matching theorem of discrete Morse theory gives a CW complex homotopy equivalent to \(X\), with one zero-cell, five three-cells and no other cells. Its three-cell attaching maps land in its zero-skeleton, a point, so the CW complex is the wedge of exactly five three-spheres. The conclusion holds integrally and is stronger than matching mod-two Betti numbers.

## Verification
Run `python3 verify.py` with standard-library Python 3. The program reconstructs the graph and all masks, compares two independent face-membership tests, forms the deterministic matching, and exhaustively checks acyclicity across all Hasse covers. It also independently reduces every mod-two simplicial boundary matrix and verifies the reduced Betti vector \((0,0,0,5,0,0)\). The recorded output is in `verification_output.txt`. The actual program and output are embedded with this report, and no external data, randomness, or computational service is required.

## Relationship to prior work
The nonflag complex \(X\) is a \(P_3\)-devoid or second-independence complex in the terminology developed by Taylan (arXiv:1501.06754v1, first public January 27, 2015). Taylan proves classifications for paths, cycles and forests, not the triangle-bearing Kneser graph here. Braun (arXiv:0912.0720v1, first public December 3, 2009) determines ordinary independence complexes of *stable* Kneser graphs; those complexes require induced degree zero and use a proper stable-vertex subgraph, so his results do not imply the present calculation. Feng and Wang (arXiv:2404.10566v1) investigate ordinary independence complexes of Kneser graphs and their symmetric-difference Rips description; their results concern pairwise intersecting families, rather than induced-degree-at-most-one families. Chau, Ellis, Friedgut and Lifshitz (arXiv:2312.06370v1) study extremal induced maximum degree in asymptotic parameter regimes, not the homotopy type of this simplicial complex.

This fixed graph is the first \(\mathrm{KG}(n,2)\) with a triangle: three pairwise disjoint two-subsets require six ground elements. It therefore provides a natural boundary case beyond the Petersen graph \(\mathrm{KG}(5,2)\). Closely related indexed calculations of the neighborhood and intrinsic Čech complexes of \(\mathrm{KG}(6,2)\) concern different simplicial complexes and do not imply this theorem.

## Limitations
The assertion is specific to \(\mathrm{KG}(6,2)\). It makes no classification claim for larger Kneser graphs, no equivariant homotopy statement, and no simplicial homeomorphism claim. Public indexing and available primary-text comparisons cannot exclude every unindexed equivalent calculation; definitive publication priority remains open. An independent mathematical audit has not been performed.

## References
1. B. Braun, *Independence Complexes of Stable Kneser Graphs*, arXiv:0912.0720v1 (December 3, 2009); Electronic Journal of Combinatorics 18 (2011), P118, DOI:10.37236/605.
2. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1 (January 27, 2015).
3. Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566v1 (April 16, 2024).
4. H. T. Chau, D. Ellis, E. Friedgut and N. Lifshitz, *On the maximum degree of induced subgraphs of the Kneser graph*, arXiv:2312.06370v1 (December 11, 2023).
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
