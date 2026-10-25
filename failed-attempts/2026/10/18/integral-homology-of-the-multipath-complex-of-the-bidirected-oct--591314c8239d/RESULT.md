# Integral homology of the multipath complex of the bidirected octahedron

## Finding

Let \(O=K_{2,2,2}\) be the octahedral graph, with six vertices grouped in three independent pairs. Replace each undirected edge of \(O\) by both directed arcs, producing \(\overleftrightarrow O\). Let \(X=\mathcal X(\overleftrightarrow O)\) be the multipath simplicial complex: its vertices are directed arcs, and a set of arcs is a simplex if its selected digraph is a disjoint union of directed simple paths, with isolated graph vertices allowed. Then the full reduced integral homology is

\[
\widetilde H_j(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z^3,&j=2,\\
\mathbb Z^{92},&j=3,\\
\mathbb Z^{32},&j=4,\\
0,&\text{otherwise}.
\end{cases}
\]

In addition, \(X\) is simply connected, so \(\pi_2(X)\cong\mathbb Z^3\) by the Hurewicz theorem. These statements do **not** assert that \(X\) is a wedge of spheres.

## Assumptions and scope

Label the vertices \(0,1,2,3,4,5\) and declare the nonedges to be \(\{0,1\},\{2,3\},\{4,5\}\). The directed arcs are exactly the ordered pairs \((u,v)\) with \(u,v\in\{0,\ldots,5\}\) and \(\lfloor u/2\rfloor\ne\lfloor v/2\rfloor\). There are 24 such arcs. A face is a selection with every vertex of in-degree and out-degree at most one and with no directed circuit. The result covers this fixed finite simplicial complex, not arbitrary complete multipartite digraphs, and concerns integral homology and simple connectivity rather than full homotopy type or persistence.

## Proof

**(1) Finite model and complete enumeration.** Every disjoint union of directed simple paths on six graph vertices uses at most five arcs. It is therefore exhaustive to examine every subset of the 24 possible arcs of cardinality zero through five and retain exactly those with in-degree/out-degree at most one and without a directed circuit. A direct graph-theoretic circuit test (follow each vertex's unique outgoing successor if present) gives the augmented face counts, ordered by simplex dimension \(-1,0,1,2,3,4\):

\[
(1,24,192,616,744,240).
\]

There are exactly 24 maximal three-dimensional faces and 240 maximal four-dimensional faces. The face set has 1,817 elements counting the empty face.

**(2) An explicit acyclic partial matching.** Order the 24 arcs lexicographically by their ordered endpoint pairs, indexed from zero. Use the fixed sequence of arc indices

`(10,17,12,16,0,19,5,23,21,3,20,1,6,15,8,7,22,13,4,18,2,14,9,11)`.

Initially declare every nonempty face active. For each pivot index, traverse active face bitmasks in ascending integer order. Whenever an active face omits the pivot and its union with the pivot is also active, pair these two faces and remove them from the active set. This specifies 844 disjoint adjacent-dimensional pairs. To verify acyclicity, orient each face-poset cover from the larger face to the smaller one, reversing precisely the 844 matched covers. Kahn's elimination visits every vertex of this directed Hasse graph, whose 6,408 covers are all constructed explicitly in the supplied verifier. Therefore the matching is acyclic. Its critical cell counts in dimensions \(0,1,2,3,4\) are

\[
(1,0,3,92,32).
\]

Forman's discrete Morse theorem supplies a CW model for \(X\) having exactly these cell counts. In particular, the CW model has one zero-cell and no one-cells, hence \(\pi_1(X)=0\).

**(3) Exact rational ranks.** Form the usual signed oriented simplicial boundary matrices in increasing lexicographic-arc order; for an oriented simplex with arc indices \(i_0<\cdots<i_k\), its boundary has coefficient \((-1)^j\) upon deleting \(i_j\). Use augmentation in degree zero. Exact Gaussian elimination over \(\mathbb Q\), using rational coefficients rather than floating point, gives the boundary ranks in degrees \(0,1,2,3,4\):

\[
(1,23,169,444,208).
\]

Subtracting the incoming and outgoing boundary ranks from the face counts gives reduced rational Betti numbers

\[
(0,0,3,92,32).
\]

**(4) Integral conclusion without assuming torsion-freeness.** In dimensions \(2,3,4\), the numbers of critical Morse cells are exactly the corresponding rational Betti numbers, and in dimensions zero and one the Morse model has respectively one vertex and no one-cells. Hence every rational differential in the Morse cellular chain complex must be zero: any nonzero differential would decrease the dimension of rational homology below the number of Morse cells in some degree. Each cellular differential is an integer matrix, and an integer matrix vanishing after extension of scalars to \(\mathbb Q\) is identically zero over \(\mathbb Z\). Thus the integral cellular Morse differentials all vanish, giving the asserted free integral homology groups. Finally, simple connectivity together with the fact that the first nonzero reduced homology is in degree two yields the stated \(\pi_2\) via Hurewicz.

## Verification

The accompanying executable `verify_octahedron.py` uses only the Python 3 standard library. Running `python3 verify_octahedron.py` reconstructs all faces, tests face closure, checks maximal faces, rebuilds the stated partial matching, verifies all 6,408 oriented covers are acyclic, computes every signed augmented boundary rank by exact rational elimination, and asserts all numerical values above. Its expected final banner is `VERIFIED_OCTAHEDRAL_MULTIPATH_HOMOLOGY`. No third-party libraries, precomputed certificates, or external files are required. The argument that zero rational Morse differentials force zero integral Morse differentials is mathematical and does not depend on sampling coefficients.

## Relationship to prior work

Caputi, Collari, Di Trani and Smith introduce multipath complexes and analyze a number of graph families. Their complete-bipartite computation concerns consistently directed arcs from one part to the other, rather than all arcs in both directions of a complete three-partite graph. Later work on bidirectional polygons treats a different family, with different allowable arc configurations. Work on cycle-free chessboard complexes treats more general arc-selection constraints, including the complete directed graph, but does not by itself give the homology of this particular forbidden-pair subcomplex. Furthermore, the ordinary matching complex and the discrete-Morse matching complex of the octahedral graph have different simplex definitions from this directed-arc multipath complex. No implication from those established results to the integral groups above is used here.

## Limitations

The classification is for one canonical six-vertex bidirected graph; the verification is exhaustive because its finite face universe has a proved size bound. The CW model contains cells in adjacent dimensions, and zero Morse boundary does not rule out nontrivial attaching maps (including Hopf or Whitehead phenomena); consequently a sphere-wedge decomposition or a complete homotopy type is **not** established. The supplied program is a transparent finite proof checker, not a machine-checked formal proof. An unindexed prior classification of the identical complex remains possible.

## References

1. L. Caputi, C. Collari, S. Di Trani and J. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (first public version 2022-08-09), https://arxiv.org/abs/2208.04656.
2. L. Caputi, C. Collari and J. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (first public version 2026-01-09), https://arxiv.org/abs/2601.05670.
3. S. Vrećica and R. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252, https://arxiv.org/abs/0710.5252.
4. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
