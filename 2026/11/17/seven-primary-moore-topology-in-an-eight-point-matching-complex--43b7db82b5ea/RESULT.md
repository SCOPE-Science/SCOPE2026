# Seven-primary Moore topology in an eight-point matching-complex quotient

## Finding

Let \(M_8\) be the ordinary matching complex of the complete graph on the eight labels \(\{0,1,2,3,4,5,6,7\}\). Thus its vertices are unordered pairs of distinct labels, and its simplices are collections of pairwise disjoint pairs. The seven-cycle \(r=(0\ 1\ 2\ 3\ 4\ 5\ 6)\) fixes label \(7\) and acts simplicially. Write \(Y=|M_8|/\langle r\rangle\) for the **ordinary geometric orbit space**, not the Borel construction.

There is a homotopy equivalence of connected CW complexes

\[
Y\simeq M(\mathbb Z/7\mathbb Z,1)\vee\bigvee^{18}S^2,
\]

where \(M(\mathbb Z/7\mathbb Z,1)=S^1\cup_{\deg 7}D^2\) denotes the two-dimensional Moore space. In particular, \(\pi_1(Y)\cong\mathbb Z/7\mathbb Z\), \(H_0(Y;\mathbb Z)\cong\mathbb Z\), \(H_1(Y;\mathbb Z)\cong\mathbb Z/7\mathbb Z\), \(H_2(Y;\mathbb Z)\cong\mathbb Z^{18}\), and all higher integral homology groups vanish.

## Assumptions and scope

All spaces have their usual finite CW topology. Vertices of a simplex of \(M_8\) are edges of the complete graph, not the eight graph labels. Rotations act on each edge by translating its endpoints in \(\mathbb Z/7\mathbb Z\) while leaving label \(7\) fixed. The asserted equivalence is nonequivariant and applies precisely to this seven-cycle subgroup; it is not a homeomorphism assertion or a classification for arbitrary matching complexes.

## Proof

**1. Free action and orbit cells.** Every graph edge belongs to an orbit of exactly seven distinct graph edges under \(r\). A nonempty matching has at most four edges. An invariant matching would have to be a union of edge orbits of length seven, hence cannot exist. Since seven is prime, no nonidentity group element fixes any simplex setwise. An isotropy element fixing a point of the realization must stabilize its unique carrier simplex, so the action on \(|M_8|\) is free. It follows that the ordinary quotient has a finite \(\Delta\)-complex structure with one cell for every simplex orbit.

A matching of size \(k\) is chosen in \(8!/(2^k k!(8-2k)!)\) ways. For \(1\leq k\leq4\) these counts are \(28,210,420,105\); division by seven gives the exact quotient cell counts in dimensions zero to three:

\[
(f_0,f_1,f_2,f_3)=(4,30,60,15),\qquad\chi(Y)=19.
\]

**2. Equivariant collapse to dimension two.** Every three-edge matching leaves precisely two unused labels and therefore extends to exactly one four-edge matching, by adjoining the edge joining the unused labels. Thus each triangular face of \(M_8\) belongs to one and only one tetrahedral face. For each tetrahedron orbit, select the orbit of the triangle obtained by removing the least-indexed graph-edge vertex from the lexicographically minimal representative tetrahedron. The fifteen selected triangle orbits are distinct: if two faces of one tetrahedron were translated into one another, uniqueness of their tetrahedral extensions would force that tetrahedron to have a nontrivial stabilizer. Each chosen triangle orbit is a free two-face of its unique three-cell orbit. The quotient therefore collapses by fifteen elementary three-cell/two-cell pairs to a two-dimensional CW complex \(Y_2\) with cell counts \((4,30,45)\).

**3. Explicit attaching words.** Index the 28 graph edges by lexicographic order of pairs of labels, using indices starting at zero. Represent each simplex orbit by the lexicographically smallest sorted tuple of graph-edge indices among its seven translates. Orient each edge and triangle orbit by increasing indices in the chosen representative; transporting an oriented edge to its representative contributes the sign of the induced permutation. The oriented boundary of a triangle \((a,b,c)\) reads its three oriented edges in the order \((a,b),(b,c),(c,a)\).

A spanning tree in the one-skeleton of \(Y_2\) comprises edge-orbit indices \(1,2,4\) (zero-based). Contracting this tree leaves one vertex, \(27\) oriented one-cells, and \(45\) two-cells. The complete initial list of attaching words, with identifiers one larger than the orbit indices and signs indicating inverse orientation, is in `certificate.json`; `verify.py` reconstructs it from the graph and checks the boundary conventions.

There are \(26\) successively verified generator-relator eliminations. Each uses a two-cell whose cyclically written attaching word contains one particular generator exactly once, solves that relation for the generator, replaces occurrences in the remaining attaching words, and deletes the generator and that two-cell. These are elementary homotopy equivalences of presentation two-complexes: homotope the other attaching maps using the chosen disk, then collapse its once-traversed one-cell with that disk. The complete ordered elimination list and substituted words are in `certificate.json` and are replayed by `verify.py`.

After these moves one one-cell remains, denoted \(x\), and exactly \(19\) two-cells remain. Their attaching words are powers of \(x\) with ordered exponents

\[
(-7,7,0,7,0,0,14,7,7,7,7,-7,-7,7,-7,0,14,7,0).
\]

The first attaching map \(x^{-7}\) yields \(M(\mathbb Z/7\mathbb Z,1)\); since its fundamental group is cyclic of order seven, all the other eighteen attaching maps \(x^{7j}\), including the constant maps with exponent zero, are nullhomotopic there. Attaching a two-cell by a nullhomotopic map to a connected CW complex adds a wedged \(S^2\) up to homotopy. This proves the displayed homotopy equivalence and all its stated consequences.

## Verification

`verify.py` uses only the Python standard library. Run `python3 verify.py --check certificate.json` in the directory containing these two files. The checker exhaustively enumerates all \(763\) nonempty simplices, verifies all seven-element orbits, the uniqueness of extension of each three-edge matching, fifteen distinct elementary free-face pairs, the quotient oriented boundary identities, the spanning tree and all \(26\) word eliminations, and checks the final \(19\) attaching exponents. `verification_output.txt` contains the output recorded from the checker replay. The certificate is finite and exhaustive; it is not an extrapolation from small cases.

As a separate arithmetic cross-check, the resulting two-dimensional quotient has Euler characteristic \(19\), and its integral homology gives \(1-0+18=19\). The known integral homology \(\widetilde H_2(M_8;\mathbb Z)\cong\mathbb Z^{132}\) has compatible Euler characteristic \(133=7\cdot19\), but that earlier computation is not used to infer the quotient's homotopy type.

## Relationship to prior work

Jonsson's paper on matching-complex torsion (first verified public preprint: March 26, 2012) tabulates the integral homology of \(M_8\), giving free rank \(132\) in degree two, and analyzes different symmetric-group chain actions. It does not supply the present ordinary orbit-space homotopy equivalence in the inspected introduction, results, or \(M_8\) tables. Mondal, Mukherjee and Saha's discrete-Morse paper (first arXiv version: May 4, 2023) develops the nonequivariant topology, particularly that of \(M_7\). Their inspected statements are not an integral homotopy classification of this \(C_7\)-quotient. The homotopy type of a quotient is not determined by the integral homology of the covering complex.

## Limitations

No homeomorphism or canonical wedge splitting is claimed, and no conclusion is asserted for arbitrary prime cycles, arbitrary subgroups of the eight-label permutation group, or other matching complexes. The finite elimination certificate confirms this specified CW presentation; the interpretation as a homotopy equivalence uses the standard topology of cellular collapses and attaching-map homotopies. The literature comparison does not establish absolute priority against unpublished or differently indexed results.

## References

- Jakob Jonsson, *More Torsion in the Homology of the Matching Complex*, arXiv:1203.5658, version 1 publicly posted March 26, 2012, https://arxiv.org/abs/1203.5658 .
- Anupam Mondal, Sajal Mukherjee and Kuldeep Saha, *Topology of matching complexes of complete graphs via discrete Morse theory*, arXiv:2305.02973, first posted May 4, 2023, https://arxiv.org/abs/2305.02973 .
