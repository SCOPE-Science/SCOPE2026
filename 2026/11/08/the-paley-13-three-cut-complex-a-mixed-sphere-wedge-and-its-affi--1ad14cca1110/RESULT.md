# The Paley-13 three-cut complex: a mixed sphere wedge and its affine homology character

## Finding
Let \(P_{13}\) be the Paley graph on \(\mathbb F_{13}\), with distinct vertices \(u,v\) joined when \(v-u\) is a nonzero square. Let \(X=\Delta_3(P_{13})\) be the **ordinary** three-cut complex, whose facets are complements of disconnected induced triples. Then
\[
X\simeq S^7\vee S^7\vee S^8.
\]
In particular, its reduced integral homology consists of \(\widetilde H_7(X;\mathbb Z)\cong\mathbb Z^2\) and \(\widetilde H_8(X;\mathbb Z)\cong\mathbb Z\), with all other reduced groups zero. Although \(X\) is pure of dimension nine, it is nonshellable.

There is more precise equivariant information. The affine group
\[G=\mathbb F_{13}\rtimes(\mathbb F_{13}^{\times})^2\cong C_{13}\rtimes C_6\]
acts on \(X\) by \(u\mapsto au+b\), where \(a\) is any nonzero square and \(b\in\mathbb F_{13}\). On rational reduced homology every translation acts trivially. If \(m\) is the multiplier \(u\mapsto4u\), a generator of the order-six multiplier subgroup, then
\[
\widetilde H_7(X;\mathbb Q)\cong\mathbb Q(\zeta_3),\qquad
\widetilde H_8(X;\mathbb Q)\cong\mathbb Q_{\mathrm{sgn}}
\]
as rational representations of the affine group, with the translation subgroup trivial: \(m\) acts on the first as multiplication by a primitive cube root of unity, and on the second as multiplication by \(-1\). The representation statement concerns homology, not an equivariant wedge decomposition.

## Assumptions and scope
Take vertex labels \(0,1,\ldots,12\). The set of nonzero squares modulo thirteen is \(Q=\{1,3,4,9,10,12\}=\{\pm1,\pm3,\pm4\}\). For a three-subset \(T\), its induced graph is connected precisely when it contains at least two edges. Thus a subset \(F\subseteq\mathbb F_{13}\) belongs to \(X\) if and only if the complement contains a three-subset spanning at most one edge. There are exactly 143 such disconnected triples, each giving a ten-vertex facet.

This is neither the total three-cut complex (which uses independent triples only) nor a neighborhood, flag, or independence complex. The finite graph and all group actions are specified without reliance on a graph database. The full face vector in dimensions zero through nine is
\[(13,78,286,715,1287,1716,1716,1287,637,143).\]

## Proof
**1. Exhaustive face model and acyclic matching.** The accompanying standalone `verify.py` builds \(P_{13}\) from its quadratic residues. For each of the \(\binom{13}{3}=286\) triples, it checks whether the induced graph has at most one edge and marks all faces of the complementary nine-simplex (of cardinality ten, geometric dimension nine). A second algorithm compares the resulting membership flag for each of the \(2^{13}=8192\) subsets directly with the disconnected-triple condition. Both agree. There are 7879 faces including the empty face.

Use the following completely deterministic matching on the augmented face poset. Initially every face is unmatched. For \(v=0,1,\ldots,12\), in increasing binary-mask order, match each still-unmatched face \(F\) with \(F\cup\{v\}\) whenever \(v\notin F\), \(F\cup\{v\}\in X\), and the latter is still unmatched. Remove both matched faces from subsequent steps. This first makes 3934 disjoint pairs on the augmented face poset. Discard the pair between the empty face and the vertex \(\{0\}\), and remove the empty face. The resulting ordinary matching contains 3933 pairs and has one critical vertex \(\{0\}\). Its other eleven critical faces are six eight-vertex masks
\[
510,\ 1662,\ 3294,\ 3510,\ 4926,\ 6558
\]
and five nine-vertex masks
\[
3578,\ 3834,\ 6010,\ 7610,\ 8114.
\]
Here a mask \(t\) represents \(\{j:2^j\text{ occurs in the binary expansion of }t\}\). Thus the eleven positive-dimensional critical cells have dimensions seven and eight; the additional critical vertex supplies the CW basepoint.

For each face-cover relation, direct the arrow upward if it is a matched pair and downward otherwise. The program reconstructs all 50076 nonempty face-cover relations, then topologically sorts this entire directed graph. All 7878 nonempty face nodes are reached. Therefore the ordinary matching is acyclic, not merely locally well-formed. Discrete Morse theory supplies a CW model with one basepoint, six seven-cells, and five eight-cells, with no others.

**2. Integral attaching matrix.** Orient simplices by increasing vertex labels. The signed incidence of a codimension-one face obtained by deleting the \(i\)-th vertex is \((-1)^i\), with indices starting at zero. A matched seven-cell is eliminated using the signed boundary of its matched eight-cell; recursively following only upward matches in adjacent degrees gives the Morse differential from dimension eight to seven. In the sorted critical-mask bases just displayed, the exact integer matrix is
\[
D=\begin{pmatrix}
0&-1&0&1&1\\
0&1&1&0&0\\
-1&-1&0&0&0\\
1&0&0&1&1\\
0&0&-1&0&-1\\
0&0&0&-1&0
\end{pmatrix}.
\]
The verifier computes this matrix directly from the actual matching, rather than reading a predetermined result. All six five-by-five minors vanish; the four-by-four minor on zero-based rows \((0,1,2,4)\) and columns \((0,1,2,3)\) equals \(+1\). Hence \(D\) has rank four, all its four nonzero Smith factors are units, and its homology is \(\mathbb Z^2\) in degree seven and \(\mathbb Z\) in degree eight.

More strongly, the seven-skeleton of the Morse CW model is a wedge of six seven-spheres. The attaching maps of the eight-cells are classified by their integer degree vectors because \(\pi_7(\bigvee^6 S^7)\cong\mathbb Z^6\) by Hurewicz. Unimodular row/column operations on \(D\) therefore correspond to homotopy-preserving changes of attaching bases; four unit pairs cancel and the remaining two seven-cells and one eight-cell attach trivially. This proves the stated **integral homotopy equivalence**, not just homology. It also implies nonshellability: a pure shellable nine-dimensional complex could only have reduced homology in degree nine.

**3. Rational affine character.** Every affine map \(u\mapsto au+b\) with \(a\in Q\) preserves the graph and thus acts simplicially on \(X\). Its reduced Lefschetz number is the alternating signed sum over setwise-fixed simplices, with the augmented empty face contributing \(-1\). For a fixed simplex the sign is the parity of the permutation induced by the map on its ordered vertex set. Exhaustive signed enumeration for every one of the 78 affine maps gives, for multipliers \(a=1,3,4,9,10,12\), respectively,
\[
\widetilde L(a)=(-1,2,0,2,0,-3),
\]
and each value is independent of the translation parameter \(b\). Since reduced homology is nonzero only in degrees seven and eight,
\[\widetilde L(a)=-\operatorname{tr}(a\mid H_7(X;\mathbb Q))+\operatorname{tr}(a\mid H_8(X;\mathbb Q)).\]
A nontrivial rational representation of a cyclic group of prime order thirteen has dimension at least twelve; therefore the translations act trivially in both ranks one and two. The multiplier \(4\) has order six, with \(4^3=12=-1\). At \(a=12\) the Lefschetz value \(-3\), together with \(\dim H_7=2\) and \(\dim H_8=1\), forces traces \(+2\) and \(-1\), respectively. Thus the one-dimensional \(H_8\)-character is the sign character of \(C_6\), sending its generator \(4\) to \(-1\). The value \(\widetilde L(4)=0\) then forces trace \(-1\) on \(H_7\). A rational two-dimensional finite-order operator of order dividing six and trace \(-1\) has characteristic polynomial \(t^2+t+1\); it is the primitive cubic cyclotomic representation. The other four observed traces follow from these two characters, giving a cross-check of the entire action.

## Verification
Run `python3 verify.py` using Python 3 and only its standard library. The attached `verification-output.txt` gives the complete expected output. The checker independently verifies all 8192 subset-membership decisions; the combinatorial Alexander-dual face vector \((13,78,143,78)\); every face cover and matching arrow; the full directed acyclicity certificate for the ordinary matching; the signed integral Morse matrix; its exhaustive maximal minors and a unit rank-four minor; and the signed Lefschetz numbers for all 78 affine maps. Assertions stop execution on any mismatch. The finite exhaustive graph construction, rather than a few sampled reductions, establishes this particular finite theorem. No extrapolation to a larger prime is attempted.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduce ordinary cut complexes and analyze chordal graphs, cycles, complete multipartite graphs, trees and clique prisms; their general face-count and shellability tools provide background, but do not calculate this strongly regular Paley graph's three-cut homotopy or homology action [1]. Their sequel treats disjoint unions, squared paths and grid graphs, not Paley graphs [2]. A further treatment of total cut and cut complexes for rectangular grids does not cover this graph [3].

Related exact three-cut results for the icosahedral graph and for graphs without four-cycles likewise do not imply the displayed Paley-13 statements: the Paley graph contains triangles and many four-cycles and is not isomorphic to the icosahedral graph. The original graph's nontrivial affine symmetry also makes its degree-separated rational representation a distinct invariant. Searches under Paley graph, order thirteen, circulant \(C_{13}(1,3,4)\), connected-triple Alexander dual, and three-cut aliases did not identify an already published exact calculation. Lack of a search hit is evidence of noncoverage only among inspected sources, not a proof of universal priority.

## Limitations
No family-wide theorem for all Paley graphs is claimed, nor an equivariant wedge decomposition. The rational representations do not by themselves determine a complete integral equivariant CW model. There has been no independent mathematical audit; related uncatalogued literature remains a possible originality risk. Results here depend on the finite exhaustive calculations and their explicit matching and integer differential, all supplied for reproduction.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public 2023-04-26), especially Sections 2, 5–7; published SIAM J. Discrete Math. 38 (2024), 1630–1675.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first public 2024-07-11), especially Sections 3–6.
3. H. Chandrakar, N. R. Hazra, D. Rout, A. Singh, *Topology of total cut and cut complexes of grid graphs*, arXiv:2408.07646 (first public 2024-08-14).
4. Standard discrete Morse theory and combinatorial Alexander duality, as developed in algebraic topology and simplicial-complex references.
