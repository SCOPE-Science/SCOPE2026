# Equal face vectors but unequal integral multipath homology for the Wagner and cube graphs

## Finding
Let \(W\) be the Wagner graph (the eight-vertex Möbius ladder) and let \(Q_3\) be the three-dimensional cube graph. Give every undirected edge both orientations, and let \(X(\overleftrightarrow G)\) be the simplicial complex whose vertices are directed arcs and whose faces are arc sets forming vertex-disjoint directed simple paths (no directed cycles). **Both complexes have the same nonempty face vector**, in dimensions zero through six,
\[
(24,216,928,2016,2160,1008,144),
\]
but their reduced *integral* homology differs:
\[
\widetilde H_i(X(\overleftrightarrow W);\mathbb Z)\cong
\begin{cases}
\mathbb Z^4,&i=3,\\
\mathbb Z^{41},&i=4,\\
\mathbb Z^{32},&i=5,\\
\mathbb Z^{10},&i=6,\\
0,&\text{otherwise},
\end{cases}
\qquad
\widetilde H_i(X(\overleftrightarrow{Q_3});\mathbb Z)\cong
\begin{cases}
\mathbb Z^6,&i=3,\\
\mathbb Z^{45},&i=4,\\
\mathbb Z^{36},&i=5,\\
\mathbb Z^{12},&i=6,\\
0,&\text{otherwise}.
\end{cases}
\]
Thus their integral homology groups are torsion-free, while the face vector (and hence the reduced Euler characteristic, \(15\)) fails to distinguish their homology.

## Assumptions and scope
Take the Wagner graph on \(\mathbb Z/8\mathbb Z\), with edges \(\{i,i+1\}\) and \(\{i,i+4\}\), indexed modulo eight. Take the cube graph on the binary triples, with adjacency at Hamming distance one. Label the cube vertices by their binary representations as the integers zero through seven. Both underlying graphs have eight vertices and twelve undirected edges, hence their fully bidirected versions each have twenty-four arcs. **Here “bidirected” means both opposing directed arcs are present, not the graph-theoretic notion of an independent arrow at each endpoint.**

A directed arc subset is a face precisely when (i) every vertex has at most one selected outgoing and one selected incoming arc and (ii) the resulting functional digraph is acyclic. Because of (i), condition (ii) makes its connected components directed simple paths and isolated vertices. The empty arc set is the augmented simplex of dimension \(-1\). All homology displayed is reduced simplicial homology over \(\mathbb Z\). The result is a finite classification for these two graphs; no claim about arbitrary cubic graphs or homotopy sphere-wedge decompositions is made.

## Proof
The included `verify.py` implements exact finite combinatorial procedures and checks the supplied `morse_certificate.json`. Both use the lexicographic arc order given by the sorted ordered pairs \((u,v)\) in each graph.

**Face determination.** One enumeration adds allowable arcs successively, refusing collisions in the partial incoming/outgoing maps or a newly closed directed cycle. A genuinely different enumeration chooses, for every graph vertex, either no successor or one adjacent successor, and rejects choices having repeated targets or directed cycles. The two resulting sets of bit masks agree exactly for each graph. Both have \(6497\) faces including the empty face; their face-by-dimension counts are identical and are precisely the displayed vector.

**Acyclic matching and integral reduction.** In each graph, sweep the twenty-four arc indices in increasing order. At index \(j\), pair every currently unpaired face not containing \(j\) with the currently unpaired face obtained by adding \(j\), if present. Repeat independently with decreasing index order. Every pair differs by one arc, so its signed simplicial incidence is a unit \(\pm1\). For every matching, reverse its matched Hasse edges and orient every other cover from larger to smaller face. A complete topological-sort check consumes all \(6497\) vertices and \(29160\) directed incidences: the discrete vector field has no closed gradient paths.

For the Wagner complex, each matching has \(3194\) pairs and critical-cell ranks \((15,52,32,10)\) in dimensions three to six, with no other critical cells. For the cube, each has \(3193\) pairs and critical ranks \((8,51,40,12)\). The empty face is matched, so these are *augmented*, reduced chain models.

To compute the integral Morse differential, take signed simplex boundaries in ascending arc-index order. A critical face projects to itself, a matched upper face to zero, and a matched lower face \(b\), paired with the upper face \(U\), satisfies
\[
P(b)=-\langle\partial U,b\rangle^{-1}
\sum_{t\in\partial U,\ t\ne b}\langle\partial U,t\rangle P(t).
\]
Here the summation is over codimension-one faces with their signed boundary coefficients; the acyclic matching makes this recursion well-founded. Consequently \(\partial^{\mathrm{Morse}}=P\partial\) on critical cells. This is integral algebraic discrete-Morse cancellation: each eliminated incidence has coefficient \(\pm1\), so it preserves integral chain homotopy type.

For Wagner, the only nonzero Morse differential is \(\partial_4:\mathbb Z^{52}\to\mathbb Z^{15}\), which has rank \(11\) with all nonzero Smith invariant factors equal to \(1\). Both \(\partial_5\) and \(\partial_6\) vanish exactly. For the cube, the nonzero Morse differentials have ranks \(2\) in degree four and \(4\) in degree five; the degree-six boundary vanishes. All nonzero Smith factors in both calculations are units. The checker establishes this over the integers using only elementary unimodular row and column operations, explicitly rejecting any remaining nonzero block. These facts give the stated ranks by taking kernels modulo images and exclude integral torsion.

## Verification
`morse_certificate.json` contains, for both graphs and both arc orders, the ordered arc sets, critical-face masks, shapes and all nonzero signed entries of the three Morse boundary matrices. `verify.py` reconstructs every face, all Hasse incidences, each matching, each gradient projection and each integral boundary coefficient, then compares the regenerated certificate with the embedded one. It additionally computes the ranks of the *unreduced* simplicial boundary matrices independently over \(\mathbb F_2\) and \(\mathbb F_3\):
\[
\begin{array}{c|rrrrrr}
 &\partial_1&\partial_2&\partial_3&\partial_4&\partial_5&\partial_6\\\hline
W&23&193&735&1277&842&134\\
Q_3&23&193&735&1275&840&132
\end{array}
\]
The same rank vectors occur in both coefficient fields. They agree with the integral Morse models and provide an independent check, though agreement over two fields alone would not rule out torsion at other primes. **The integral unit-diagonal reductions provide that stronger conclusion.**

To reproduce, place `verify.py` and `morse_certificate.json` in the same directory and run `python3 verify.py morse_certificate.json`; the complete expected output appears in `verification_output.txt`. Python's standard library is sufficient.

## Relationship to prior work
The multipath complex and its face-poset interpretation are developed by Caputi, Collari, Di Trani and Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (first publicly submitted August 9, 2022). Their explicit homotopy calculations treat directed paths, polygons, some small grids and transitive tournaments, not the fully bidirected Wagner graph. Caputi, Collari and Ramos, arXiv:2401.01248v1, prove a matching-complex comparison restricted to digraphs without directed cycles; it does not apply because every edge here yields a directed two-cycle. Caputi, Collari and Smith, arXiv:2601.05670v1, treat fully bidirectional paths and polygons, not the eight-vertex cubic graphs here.

A previously available computation of the cube's integral multipath homology is used as the comparison baseline; its figures are recomputed directly in the attached verifier. The new calculation is the Wagner integral homology **together with** the exact face-vector equality and homological distinction. The ordinary edge-matching complex and Morse complex of the Wagner graph have different definitions; their known homology does not determine the arc-set multipath complex. A known general description of top-dimensional multipath homology via Hamiltonian cycles already accounts for the top-degree summands; the distinguishing information here includes all lower integral degrees and the common face vector.

## Limitations
This is not a full integral homotopy-type classification: integral homology does not determine higher attaching maps or an equivariant decomposition. It is not a new all-parameter formula for cubic graphs, nor a proof that arbitrary multipath complexes are torsion-free. Literature and indexed-record searches are not a proof of uniqueness; a genuinely equivalent unindexed calculation would supersede the originality assessment. Reproduction checks mathematical calculations on the stated finite models; they do not constitute independent human review.

## References
1. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1, August 9, 2022. https://arxiv.org/abs/2208.04656
2. L. Caputi, C. Collari and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248v1, January 2, 2024. https://arxiv.org/abs/2401.01248
3. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, January 9, 2026. https://arxiv.org/abs/2601.05670
