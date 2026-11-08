# The ordinary four-cut complex of the four-cube is a mixed-dimensional sphere wedge

## Finding
Let \(Q_4\) be the four-dimensional hypercube graph. Its ordinary four-cut complex has integral homotopy type
\[
\Delta_4(Q_4)\simeq \left(\bigvee^{25}S^{10}\right)\vee\left(\bigvee^{200}S^{11}\right).
\]
The complex has dimension \(11\), is pure, and is not shellable, because its reduced homology in dimension \(10\) is nonzero.

## Assumptions and scope
The graph vertices are the integers \(0,\ldots,15\), viewed as four-bit binary words, with an edge when two words differ in one bit. A four-subset \(T\) is *disconnected* when its induced graph is disconnected. Define \(\Delta_4(Q_4)\) to have facets precisely the complements \(V(Q_4)\setminus T\) of disconnected four-subsets. All homotopy types and homology groups are integral and nonequivariant. This is the ordinary four-cut complex, not the complex defined by complements of independent sets.

## Proof
**1. Faces.** There are \(\binom{16}{4}=1820\) four-subsets. Connected induced four-vertex sets occur in three shapes: \(64\) stars, \(192\) induced four-vertex paths, and \(24\) squares. The first count is \(16\binom43=64\). The undirected three-edge path count is \(16\cdot4\cdot3\cdot3/2=288\); \(24\) squares contribute \(4\) such paths each, leaving \(192\) induced paths. The number of squares is \(\binom42 2^{4-2}=24\). Thus \(280\) four-sets are connected and \(1540\) are disconnected, yielding exactly \(1540\) facets. The full face vector in dimensions \(0\) through \(11\) is
\[
(16,120,560,1820,4368,8008,11440,12870,11440,8008,4368,1540).
\]
The total number of faces including the empty face is \(64559\).

**2. Discrete Morse reduction.** On all nonempty faces, successively for \(i=0,\ldots,15\), pair each currently unmatched face \(\sigma\) not containing \(i\) with \(\sigma\cup\{i\}\) whenever both faces remain unmatched. The verifier constructs all \(32160\) pairs and checks the resulting oriented Hasse diagram has no directed cycle by processing every one of its \(64558\) vertices and all \(511696\) cover incidences. The only critical faces are one vertex, \(31\) ten-simplices and \(206\) eleven-simplices. By discrete Morse theory, \(\Delta_4(Q_4)\) is homotopy equivalent to a CW complex having precisely these cells; hence the only undetermined cellular map is an integer \(31\)-by-\(206\) boundary in degrees \(11\) and \(10\).

**3. Alexander-dual calculation.** Write \(K=\Delta_4(Q_4)^\vee\). A subset belongs to \(K\) if it contains no disconnected four-subset. Thus its full two-skeleton is that of the \(15\)-simplex, and its three-simplices are the \(280\) connected four-subsets. There are no higher simplices: a five-vertex induced graph all of whose four-vertex deletions stay connected is two-vertex-connected. For a bipartite graph of order five, that condition forces \(K_{2,3}\); but two vertices in \(Q_4\) have at most two common neighbors, so \(Q_4\) contains no \(K_{2,3}\). This also rules out larger simplices. A second direct finite check exhausts all \(\binom{16}{5}=4368\) five-subsets.

The integer simplicial boundary \(\partial_3^K\) has \(560\) rows (triangles) and \(280\) columns (connected four-subsets). Its columns have exactly four entries \(\pm1\). The bundled exact integer column-elimination program determines rank \(255\), obtaining a unit pivot at each step. All transformations are unimodular column operations; their transformed pivot block has determinant \(\pm1\), so the boundary image is primitive. The full two-skeleton of a \(15\)-simplex has second homology of rank \(\binom{15}{3}=455\). Consequently,
\[
\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{280-255}=\mathbb Z^{25},\qquad
\widetilde H_2(K;\mathbb Z)\cong\mathbb Z^{455-255}=\mathbb Z^{200},
\]
with no torsion and no other nonzero reduced homology. Integral combinatorial Alexander duality on \(16\) vertices gives \(\widetilde H_j(\Delta_4(Q_4);\mathbb Z)\cong\widetilde H^{13-j}(K;\mathbb Z)\), namely free ranks \(25\) in degree \(10\) and \(200\) in degree \(11\).

**4. From homology to homotopy.** In the Morse CW complex, the only nonzero-degree cellular boundary is \(\mathbb Z^{206}\to\mathbb Z^{31}\). Its free homology ranks just calculated force rank \(6\). Absence of torsion forces all six nonzero Smith invariant factors to be units. The ten-skeleton is a wedge of \(31\) ten-spheres. Since the attaching maps of eleven-cells lie in \(\pi_{10}(\bigvee^{31}S^{10})\cong\mathbb Z^{31}\), they are completely classified by those integer degrees. Unimodular changes of ten- and eleven-cell bases give six cancelling degree-one pairs, leaving \(25\) ten-spheres and \(200\) eleven-spheres. This proves the displayed integral homotopy equivalence. A pure shellable \(11\)-complex has no reduced homology below degree \(11\), so the nonzero degree-ten group proves non-shellability.

## Verification
Run `python3 proof/q4_cut_verifier.py` using Python 3.10 or newer. The script needs no external packages and checks the graph definition, the four-set connectivity by both breadth-first search and union-find, two different face-generation procedures, the complete Morse matching and directed acyclicity, the absence of higher Alexander-dual faces, and exact integral unit-pivot elimination. The reference output is `proof/q4_cut_verification.json`. The Hasse-acyclicity check is finite and exhaustive. The algebraic-topology deductions are supplied above; the computational record alone is not substituted for them.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue defined ordinary cut complexes and treated graph families including cycles, complete multipartite graphs, trees and clique prisms. Their stated Cartesian-product calculation concerns the *two*-cut complex; it does not determine this ordinary four-cut complex. Their separate paper on *total* cut complexes studies complements of independent four-sets, a different construction, and does not imply the result above. The four-cube has girth \(4\), so high-girth classifications requiring girth at least \(k+2=6\) for ordinary \(k=4\) cut complexes are inapplicable. Checked nearby results about the cube's other complexes and ordinary three-cut complexes have different face conditions. No inspected statement yielded the present mixed integral homotopy type. Absence of an indexed match is not a proof of absolute novelty.

## Limitations
This is the exact homotopy classification for one canonical graph and one cut size. It does not classify other hypercube dimensions, all cut sizes, the inclusion-induced maps between cut complexes, or the action of cube automorphisms on the two homology groups. Possible unindexed equivalents remain a bibliographic risk. No independent external mathematical audit has been performed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, first publicly submitted 2023-04-26, arXiv:2304.13675, https://arxiv.org/abs/2304.13675 .
2. The same authors, *Total Cut Complexes of Graphs*, first publicly submitted 2022-09-27, arXiv:2209.13503, https://arxiv.org/abs/2209.13503 .
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete Morse theory).
4. A. Björner, *Topological Methods*, in Handbook of Combinatorics (1995) (shellability and combinatorial Alexander duality background).
