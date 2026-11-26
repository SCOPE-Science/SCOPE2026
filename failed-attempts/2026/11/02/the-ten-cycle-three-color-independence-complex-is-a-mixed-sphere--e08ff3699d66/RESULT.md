# The ten-cycle three-color independence complex is a mixed sphere wedge

## Finding
Let \(G=C_{10}\times K_3\) be the categorical product, with vertex set \(\{0,\ldots,9\}\times\{0,1,2\}\) and adjacency \((i,a)\sim(j,b)\) precisely when \(i-j\equiv\pm1\pmod{10}\) and \(a\ne b\). Its independence complex satisfies
\[
\operatorname{Ind}(G)\simeq S^5\vee S^5\vee S^5\vee S^6.
\]
Thus the reduced **integral** homology is \(\mathbb Z^3\) in degree \(5\), \(\mathbb Z\) in degree \(6\), and zero in other degrees. In particular this explicitly identified graph product has no homology torsion.

## Assumptions and scope
All complexes are finite abstract simplicial complexes; an independent set is a subset containing no adjacent pair. The categorical product is not the Cartesian or lexicographic product. The result concerns precisely the 30-vertex graph \(C_{10}\times K_3\), not all cycle lengths, all color numbers or equivariant actions. Homotopy equivalence is ordinary (non-equivariant) homotopy equivalence over the integers.

## Proof
Order the thirty vertices by \((i,a)\mapsto 3i+a\). Enumerate independent sets by starting with the empty set and, at vertex \(v\), retaining every current set and adjoining \(v\) to every set disjoint from its neighbor set. Induction on \(v\) proves this is exactly the collection of independent subsets of the first \(v+1\) vertices, with no omissions or repetitions. Excluding the empty face yields 216257 simplices. Their full face vector in dimensions \(0\) through \(14\) is
\[
(30,375,2560,10545,27456,46385,52080,40245,22460,9594,3330,955,210,30,2).
\]

On the face poset, process pivot vertices \(v=0,1,\ldots,29\). For every still-unpaired independent set \(\sigma\) that omits \(v\) and whose extension \(\sigma\cup\{v\}\) is also unpaired, match those two simplices and remove both from further consideration. Pairs at one pivot are disjoint, so there is no choice dependence within a pivot. The executable `CHECKER.py` reconstructs this entire matching, verifies all 1,502,070 face-cover relations, directs unmatched covers downward and matched covers upward, and exhaustively topologically sorts the directed Hasse graph. It visits all 216257 faces, proving that the matching is acyclic, not merely that it has few critical faces. There are 108121 matched pairs and exactly one critical vertex, eight critical five-simplices and six critical six-simplices. The critical five-simplices, encoded as sums of vertex bit masks, are

`6303768, 6303784, 6311960, 6311976, 10498072, 10498088, 10506264, 10506280`.

The critical six-simplices are

`153166112, 153239696, 306221344, 306331720, 612405392, 612442184`.

By discrete Morse theory, the complex is homotopy equivalent to a CW complex consisting of one zero-cell, eight five-cells and six six-cells. Use increasing vertex order for each simplex orientation. The signed Morse differential from degree six to degree five is obtained by the usual gradient-path substitutions: a matched lower face \(\sigma\) of an upper face \(\tau\) is replaced by minus the other oriented facets of \(\tau\), divided by its coefficient \(\pm1\); a five-face that is the upper member of a four-to-five pair contributes zero; a critical five-face is kept. Acyclicity makes the recursion finite. In the above critical-cell orders, this gives the **integer** matrix
\[
\partial^{\mathrm{Morse}}_6=
\begin{pmatrix}
0&0&0&0&0&0\\
-1&0&0&0&0&1\\
0&0&1&-1&0&0\\
1&0&-1&0&0&0\\
0&1&0&0&-1&0\\
0&0&0&0&1&-1\\
0&-1&0&1&0&0\\
0&0&0&0&0&0
\end{pmatrix}.
\]

The six nonzero rows form the oriented vertex-edge incidence matrix of a connected hexagon: every column has one \(1\) and one \(-1\), and the six vertices are connected. Its rank is five. The minor on rows two through six and columns one through five has determinant \(+1\). Hence its five nonzero integral Smith factors are all units. The cellular homology is \(\widetilde H_5=\mathbb Z^{8-5}=\mathbb Z^3\), \(\widetilde H_6=\mathbb Z^{6-5}=\mathbb Z\), with all other reduced groups zero.

Finally the Morse CW complex is four-connected, with cells in degrees five and six only (besides the base vertex). The attaching maps of its six-cells lie in \(\pi_5(\bigvee^8S^5)\cong\mathbb Z^8\), where the Hurewicz map is an isomorphism. Integral unimodular changes of the five-cell and six-cell bases reduce the attaching vectors to five independent degree-one maps and one zero map. Cancelling the five unit pairs gives exactly the asserted wedge of three five-spheres and one six-sphere. This upgrades the integral homology calculation to a homotopy classification.

## Verification
Run `python3 CHECKER.py` using Python 3 standard library only. It reconstructs all original faces, verifies every matched and unmatched covering relation by a global directed-DAG check, computes signed gradient paths and their integer Morse matrix, checks the hexagonal incidence property, and calculates a \(+1\) determinant by fraction-free Bareiss elimination. The terminal marker is `C10K3_INTEGRAL_MORSE_HOMOTOPY_OK`. Independent finite checks of the face complex after ordinary free-face collapses gave the same Betti vector over \(\mathbb F_2\) and \(\mathbb F_3\): dimensions three and one in degrees five and six, respectively. Such field computations are supporting checks; the integral assertion follows from the exact Morse differential.

## Relationship to prior work
Antolín Camarena and Carnero Bravo (first posted July 23, 2023) calculated the independence-complex homotopy types of several categorical-product families and proved homology concentration results for other cycle lengths. Their discussion explicitly includes \(C_{10}\times K_3\) among examples with nonzero free homology in two consecutive dimensions, but asks whether this family always has torsion-free homology. The present result resolves the **integral homotopy type of this particular listed case**; it does not resolve that all-parameter question. Earlier work of Goyal, Shukla and Singh treats other complete-graph products and generalized Mycielskians, not this 30-vertex instance. A previously reported computation for \(C_7\times K_4\) concerns a different graph and does not imply this homotopy type. No universal torsion-freeness theorem is claimed.

## Limitations
This is a finite-case homotopy theorem, supported by an exhaustive reproducible discrete-Morse certificate. It does not establish torsion-freeness for general \(C_k\times K_n\), an equivariant decomposition, or persistent homology. A complete bibliographic novelty guarantee is not asserted; equivalent results absent from the inspected sources may exist.

## References
1. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, first public arXiv version July 23, 2023, arXiv:2307.12401; *Homology, Homotopy and Applications* 26 (2024), 349–373, DOI 10.4310/HHA.2024.v26.n2.a17. In particular, section 3.2, its homology concentration theorem, and its question on torsion.
2. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, *Contributions to Discrete Mathematics* 16 (2021), DOI 10.55016/ojs/cdm.v16i3.71284.
3. R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145. Standard acyclic face-poset matching and CW reduction framework.
