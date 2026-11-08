# The ordinary Petersen five-cut complex is a mixed-dimensional sphere wedge

## Finding

The ordinary five-cut complex of the Petersen graph has the integral homotopy type
\[
\Delta_5(P)\simeq S^3\vee\bigvee^{5} S^4.
\]
Consequently its only nonzero reduced integral homology groups are \(\widetilde H_3\cong\mathbb Z\) and \(\widetilde H_4\cong\mathbb Z^5\). It is a pure four-dimensional complex that is not shellable.

## Assumptions and scope

Let \([5]=\{0,1,2,3,4\}\) and give the ten two-element subsets of \([5]\) their lexicographic order, indexed \(0,\ldots,9\). The Petersen graph \(P=\operatorname{KG}(5,2)\) has an edge between distinct two-subsets precisely when they are disjoint. For any set \(U\) of five graph vertices, call \(U\) **disconnected** when the induced graph \(P[U]\) has at least two connected components. Define
\[
\Delta_5(P)=\left\langle V(P)\setminus U:\ |U|=5,\ P[U]\text{ is disconnected}\right\rangle.
\]
Thus a set \(\sigma\subseteq V(P)\) is a face exactly when some disconnected five-subset is contained in \(V(P)\setminus\sigma\). The theorem concerns this ordinary cut complex, **not** the total cut complex requiring an independent five-set. All homotopy assertions are integral and nonequivariant.

## Proof

**1. Complete face enumeration.** Enumerate all \(\binom{10}{5}=252\) five-vertex subsets, and test connectedness by breadth-first search on the induced Petersen graph. Exactly 120 are disconnected. Their complements form 120 distinct four-dimensional facets, and closing downwards gives the complete face vector (including the empty face)
\[
(f_{-1},f_0,f_1,f_2,f_3,f_4)=(1,10,45,120,200,120).
\]
A second enumeration checks all 1024 possible vertex masks directly against the generator-membership predicate; it agrees for every mask. In particular, the two-skeleton is complete.

**2. A complete discrete-Morse matching.** Include the empty face and process vertices in increasing index order. At each vertex \(i\), iterate the currently unmatched faces in increasing order of (cardinality, bitmask). Whenever a face \(\sigma\) does not contain \(i\) and \(\sigma\cup\{i\}\) is an unmatched face, pair them and remove them from further consideration. This gives 238 face-poset pairs, including the empty face paired with vertex zero, and leaves eight unmatched three-faces and twelve unmatched four-faces. Reverse the direction of each paired cover relation in the full Hasse diagram, leaving every other cover relation downward. Kahn topological sorting visits all 496 faces across all 1860 incidences; hence the matching is acyclic, not merely locally compatible.

For ordinary based Morse theory, retain vertex zero instead of its pairing with the empty face, and ignore the empty face. Removing that pair cannot create directed cycles. This gives a CW model with exactly one zero-cell, eight three-cells, and twelve four-cells, and no one- or two-cells. The reduced Morse calculation below is equivalent to this based model.

**3. Exact integral attaching matrix.** Orient every simplex by increasing vertex indices and use the usual alternating boundary. Starting with the integral reduced simplicial chain complex (including the empty face in degree \(-1\)), cancel the above 238 pairs in the stated order. Each pivot is \(+1\) or \(-1\); elimination uses only integer elementary operations. The resulting differential from the twelve critical four-cells to the eight critical three-cells is the \(8\times12\) integer matrix
\[
A=\begin{pmatrix}
0&0&0&0&0&0&0&0&0&1&0&0\\
0&0&0&0&0&-1&0&0&0&0&0&0\\
0&0&0&0&0&-1&0&-1&0&0&0&0\\
0&0&0&0&1&0&0&0&0&0&0&0\\
0&0&0&1&0&0&0&0&-1&0&-1&0\\
0&0&0&0&1&0&0&0&1&0&1&0\\
0&0&0&0&0&0&0&0&0&1&1&1\\
0&0&0&0&0&0&0&-1&-1&0&0&1
\end{pmatrix}.
\]
With zero-based row and column indices, the square submatrix on rows \(0,1,2,3,4,5,6\) and columns \(3,4,5,7,8,9,10\) has determinant \(+1\). Conversely, the integer row relation \((1,1,-1,-1,0,1,-1,1)A=0\) shows its rank is at most seven. Thus \(\operatorname{rank} A=7\), and all seven nonzero Smith factors are units. These are explicit integral certificates; a rational rank computation alone would not suffice.

**4. Homotopy decomposition.** The based Morse CW model has a single vertex and no one- or two-cells, so its three-skeleton is a wedge of eight three-spheres. Each four-cell is attached by a class in \(\pi_3(\bigvee^8 S^3)\cong\mathbb Z^8\); the column of \(A\) is exactly that class under the Hurewicz isomorphism. Integral changes of basis in dimensions three and four transform \(A\) to a diagonal matrix with seven entries equal to one and all other entries zero. The seven degree-one attachments cancel seven three/four-cell pairs; the remaining one three-cell and five trivially attached four-cells form \(S^3\vee\bigvee^5 S^4\). Because the only higher cells are four-dimensional, no unexamined attaching maps remain.

Finally, pure four-dimensional shellability would force a wedge of spheres exclusively in dimension four, contradicting the nonzero \(\widetilde H_3\).

## Verification

The self-contained Python 3 standard-library program `verify.py` reproduces all face sets, both membership checks, the complete matching, the Hasse acyclicity test, the exact signed Morse matrix, the determinant and row-relation certificates, and separate ordinary simplicial boundary ranks in characteristics 2, 3, 5, 7 and 11. Run `python3 verify.py`; `verify_output.txt` contains the recorded output. The agreement of the field computations supports the calculation, while the unit-minor certificate supplies the necessary **integral** information. The finite enumeration is exhaustive because the complex has exactly ten graph vertices; no statement about larger Kneser graphs is inferred.

## Relationship to prior work

The ordinary cut-complex definition and general family results originate in Bayer et al. (2023, later published 2024). Their paper mentions the Petersen graph for the **two-cut** complex (Corollary 6.6), not its five-cut complex. Their complete multipartite and clique-prism classifications address different graph families. The continuation studies graph disjoint unions, squared paths and rectangular grids; the later grid-graph study likewise does not determine this Petersen case. Previously indexed results on the Petersen three-cut and total three-cut complexes concern different parameters and/or different definitions. General high-girth formulas requiring girth at least \(k+2\) do not apply here, since \(P\) has girth five while \(k=5\). No inspected source gives the mixed-dimensional homotopy statement or an implication yielding it.

## Limitations

The result classifies one canonical finite graph at one cut parameter. It does not determine the induced \(S_5\)-action on homology, the inclusion maps between successive cut complexes, or any larger Kneser-graph family. Exact indexed and accessible literature searches do not establish exhaustive originality; equivalent unindexed work remains possible. Independent external audit has not been carried out.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public version April 26, 2023; SIAM Journal on Discrete Mathematics **38** (2024), 1630–1675. https://arxiv.org/abs/2304.13675
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first public version July 11, 2024. https://arxiv.org/abs/2407.08158
3. H. Chandrakar, N. R. Hazra, D. Rout and A. Singh, *Topology of total cut and cut complexes of grid graphs*, arXiv:2408.07646, first public version August 14, 2024. https://arxiv.org/abs/2408.07646
