# The affine augmentation representation of the Paley-seventeen flag complex

## Finding
Let \(P_{17}\) be the quadratic-residue Paley graph on \(\mathbb F_{17}\), and let \(K=\operatorname{Cl}(P_{17})\) denote its ordinary flag complex, equivalently the inclusive radius-one graph-metric Vietoris–Rips complex. Let
\[
A=\{x\longmapsto ax+b:\;a\in Q,\ b\in\mathbb F_{17}\}\cong C_{17}\rtimes C_8,
\]
where \(Q\) is the group of eight nonzero quadratic residues. The **new** conclusion is the complete rational affine homology module:
\[
\boxed{\widetilde H_2(K;\mathbb Q)\cong
\ker\bigl(\mathbb Q^{17}\xrightarrow{\sum}\mathbb Q\bigr)}
\qquad\text{as }\mathbb Q[A]\text{-modules}.
\]
Equivalently, for \(g(x)=ax+b\), its degree-two homology trace is
\[
\operatorname{tr}(g\mid\widetilde H_2(K;\mathbb Q))=
\begin{cases}
16,&a=1,\ b=0,\\
-1,&a=1,\ b\ne0,\\
0,&a\ne1.
\end{cases}
\]
In particular, this is a 16-dimensional rational irreducible module on restriction to the translation subgroup (the cyclotomic augmentation module). All other positive-degree homology vanishes. The nonequivariant equivalence \(K\simeq\bigvee^{16}S^2\) is **not** claimed as new: it follows from Rinaldo and Romeo's earlier vertex-decomposability result via self-complementarity. The representation formula is the contribution.

## Assumptions and scope
The graph has vertices \(0,1,\ldots,16\), and distinct vertices \(u,v\) are adjacent exactly when their difference modulo 17 belongs to
\[
Q=\{1,2,4,8,9,13,15,16\}.
\]
The flag complex consists of the finite cliques of this graph; do not confuse it with the open-neighborhood, independence, or three-cut complexes (although self-complementarity identifies the independence complex abstractly with its flag complex). All homology representations are over \(\mathbb Q\). The group \(A\) acts on vertices through affine maps with square multipliers and therefore acts simplicially. No integral module equivalence or equivariant sphere-wedge decomposition is asserted.

## Proof
**Face structure and nonequivariant background.** Direct quadratic-residue arithmetic gives exactly 17 vertices, 68 edges, 68 triangles and no tetrahedra or higher cliques. Each edge lies in exactly three triangles, and the graph is connected. Thus \(K\) is a connected two-dimensional complex of Euler characteristic \(17\). In fact it is simply connected. For a direct finite certificate choose the 16-edge spanning tree
```
(0,1),(0,2),(0,4),(0,8),(0,9),(0,13),(0,15),(0,16),
(1,3),(1,5),(1,10),(1,14),(2,6),(2,11),(4,12),(7,8)
```
(Edges are unordered.) In the presentation of the fundamental group relative to that tree, every tree edge is trivial. Whenever the other two edges of a triangular face are trivial, its third edge is trivial too. Greedy triangle closure, with triangles in lexicographic order, trivializes all 52 remaining edges: 50 in the first full pass and two in the second. The standalone verifier reconstructs the entire proof from the quadratic-residue definition, checks the tree and every triangular relation, and confirms complete exhaustion. Hence \(\pi_1(K)=0\). As no cells have dimension above two, \(\widetilde H_2(K;\mathbb Z)\) is free; Euler characteristic yields rank 16. Hurewicz and homological Whitehead give \(K\simeq\bigvee^{16}S^2\). Separately, Rinaldo and Romeo had already proved vertex-decomposability of the *independence* complex of this graph; multiplication by any nonsquare identifies the complement with the graph, so that prior statement already implies this nonequivariant wedge result.

**The homology character.** For any simplicial automorphism \(g\), write \(c_j(g)\) for the signed trace on oriented \(j\)-simplices (orientation by increasing vertex labels). The Lefschetz identity is
\[
1+\operatorname{tr}(g\mid H_2(K;\mathbb Q))=c_0(g)-c_1(g)+c_2(g),
\]
because the only ordinary rational homology groups are \(H_0\cong\mathbb Q\) and \(H_2\cong\mathbb Q^{16}\).

For the identity, the right-hand side is \(17-68+68=17\), so the trace is \(16\). For a nonzero translation, every orbit of the vertex permutation has length 17, hence no face of size one, two or three is setwise fixed. Thus the Lefschetz sum is zero and the homology trace is \(-1\).

For \(a\ne1\), the affine map has exactly one fixed vertex. The multiplicative order of \(a\in Q\) is 2, 4 or 8. If the order is 4 or 8, no edge or triangle can be preserved setwise (other vertex orbits have length at least four), giving chain traces \((c_0,c_1,c_2)=(1,0,0)\) and homology trace zero. For \(a=-1\) (order two), direct residue arithmetic gives precisely four fixed unordered edges, each with orientation reversal, and four fixed triangles consisting of the unique fixed vertex and a swapped pair, also each with orientation reversal. Thus \((c_0,c_1,c_2)=(1,-4,-4)\); the Lefschetz sum is again 1 and the homology trace is zero. Every affine involution is a translation-conjugate of \(x\mapsto-x\), so the counts apply to all 17 of them. This determines the character on all 136 group elements.

**Identification of the representation.** The rational permutation module \(\mathbb Q^{17}\) on the graph vertices has character equal to the number of fixed vertices. Its augmentation kernel therefore has character equal to that number minus one: \(16\) for identity, \(-1\) for a nontrivial translation and \(0\) when \(a\ne1\). This is exactly the computed homology character. Rational representations of a finite group in characteristic zero are semisimple, and equality of characters implies isomorphism. Restriction to the translation subgroup is the degree-16 irreducible rational cyclotomic representation, since its characteristic polynomial on a nonzero translation is \(1+t+\cdots+t^{16}\).

## Verification
The standalone standard-library script `verify_paley17.py` reconstructs the graph and all cliques up to size four; checks all 68 triangles and each edge's three triangular cofaces; verifies the listed spanning tree and every step in the 52-edge triangle-closure certificate; recomputes the triangle boundary ranks over four independent prime fields; checks all 136 signed affine Lefschetz traces against the augmentation character; and separately checks the \((1,-4,-4)\) involution trace for every affine involution. Its output is included in `verification_output.txt` and reproduced on replay.

## Relationship to prior work
Rinaldo and Romeo [2] explicitly establish vertex-decomposability for the Paley-17 independence complex. Because the graph is self-complementary, their work already implies the nonequivariant homotopy type of the flag complex: the 16-sphere bouquet is **not a novelty assertion here**. However, vertex-decomposability and Cohen–Macaulayness do not determine how the affine group acts on homology.

Saleh, Titz Mite and Witzel [1] compute graph-distance Vietoris–Rips homotopy of Platonic solids; their scope does not include Paley graphs. Cioabă and collaborators [3,4] study strongly regular graph clique complexes, first homology and Laplacian spectra; the inspected statements and summaries do not identify the 136-element affine action on \(H_2\). Separate calculations on the Paley-17 *open neighborhood* complex concern a different construction, while published Paley-29 flag-complex torsion results concern a different graph order. The distinction among complexes and the already-covered nonequivariant statement is essential.

## Limitations
The theorem concerns only the ordinary flag complex of the Paley graph of order 17 and the rational module for its 136-element affine automorphism group. It does not assert an integral equivariant basis, an equivariant wedge splitting, an all-Paley theorem, or a new nonequivariant homotopy classification. The small finite proof is exhaustive for this defined graph, not an extrapolation to infinite families. Highly related 2025 and 2026 strongly regular graph papers were compared at the level of accessible statements and abstracts rather than thoroughly by all appendices; an unindexed or fuller stronger equivariant result remains a residual priority risk.

## References
[1] N. Saleh, T. Titz Mite and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388, first posted 2023-02-28; *Innovations in Incidence Geometry* 21 (2024), 17–34, DOI: 10.2140/iig.2024.21.17.

[2] G. Rinaldo and F. Romeo, *2-dimensional vertex decomposable circulant graphs*, arXiv:1807.05755, first posted 2018-07-16; see Example 1.5 on the Paley graph of order 17.

[3] S. M. Cioabă, K. Guo, C. Ji and M. Mim, *Clique complexes of strongly regular graphs, their eigenvalues, and cohomology groups*, arXiv:2508.05871, first posted 2025-08-07; *Linear Algebra and Its Applications* 730 (2026), 152–197.

[4] S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328, first posted 2026-06-25.
