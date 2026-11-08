# The matching complex of the three-by-seven grid is a wedge of 55 six-spheres

## Finding
For the rectangular Cartesian grid \(G=P_3\square P_7\), the ordinary matching complex satisfies the integral homotopy equivalence
\[
|\mathcal M(G)|\simeq\bigvee^{55}S^6.
\]
Here vertices of \(\mathcal M(G)\) are the edges of \(G\), and a set of these vertices is a simplex exactly when its graph edges are pairwise disjoint. This is an exact finite homotopy classification, not an extrapolation to arbitrary grids.

## Assumptions and scope
The graph has vertex set \(\{0,1,2\}\times\{0,1,\ldots,6\}\) and edges joining pairs at Manhattan distance one. There are 21 graph vertices and 32 graph edges. Sort graph edges by scanning first row, then column, adding the downward edge if present and the rightward edge if present. A simplex is recorded by the 32-bit mask of its graph edges. All integral coefficients and signs use increasing edge-index orientation.

## Proof
**Exact face enumeration.** The complete face family is generated recursively by appending higher indexed graph edges that have no endpoint in common with any already chosen edge. Recursion includes the empty face. This exhaustive algorithm yields exactly 196785 faces, with the cardinality distribution
\[
(f_{-1},f_0,\ldots,f_9)=(1,32,426,3080,13254,35004,56456,53588,27688,6716,540).
\]
All these counts are recomputed by the attached `verify_grid7.py`, which checks the exact graph adjacency, rather than consulting a precomputed face table.

**Explicit acyclic matching.** Initialize a set of all faces. Process the 32 graph-edge indices in ascending order. For the current index, consider every still-unmatched face \(\sigma\) omitting that edge. If adjoining this edge gives another still-unmatched face, pair the two faces and remove both from further consideration. Each pair is a codimension-one incidence. The attached verifier reconstructs every pair and orients each covering relation in the Hasse diagram downward, except that the matched incidences are oriented upward. Kahn topological sorting visits all 196785 faces, proving that the matching is acyclic. One matched pair contains the empty simplex and a vertex; deleting the empty simplex and this pair makes that vertex critical. Direct topological sorting of the resulting nonempty Hasse diagram visits all 196784 nonempty faces. Hence the ordinary non-augmented Morse matching leaves exactly one critical zero-cell, 59 critical six-cells, and four critical seven-cells, and no other critical cells.

**Integral Morse boundary.** Give a face the ordered orientation of its selected edge indices. For a codimension-one facet \(\tau\subset\eta\), the simplicial incidence sign is \((-1)^q\), where \(q\) is the zero-based index of the deleted vertex. For each lower element \(\tau\) of a matched pair \((\tau,\eta)\), eliminate \(\tau\) using the relation \(\partial\eta=0\) in the degree-preserving chain projection, with coefficient \(-\langle\partial\eta,\tau\rangle\langle\partial\eta,\tau'\rangle\). For an upper element of a matched pair the chain projection in its degree is zero, and for a critical face it is its basis generator. Acyclicity makes the recursive elimination terminating. This is standard algebraic discrete Morse cancellation: each eliminated incidence is a unit \(\pm1\), so the Morse chain complex is integrally chain-equivalent to the original chain complex and its boundary coefficients are the signed gradient-path sums.

The verifier computes the complete integer matrix from the four critical seven-cells to the 59 critical six-cells. The submatrix in zero-based critical-six-cell rows \((5,9,15,16)\), with columns in ascending critical-seven-cell order, is
\[
\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},
\qquad\det=1.
\]
Thus the four attaching classes are primitive and independent in \(\pi_6(\bigvee^{59}S^6)\cong\mathbb Z^{59}\), since the lower skeleton of the Morse CW complex is exactly one point with 59 six-cells. The corresponding integral change of basis is realized by a self-homotopy equivalence of the six-sphere wedge. Four seven-cells can consequently be cancelled up to homotopy, leaving a wedge of 55 six-spheres. This argument proves integral homotopy, stronger than a Betti-number calculation.

## Verification
Run `python3 verify_grid7.py` using Python's standard library. This regenerates the 196785 faces, 98361 augmented matching pairs, full directed Hasse acyclicity, the 59-by-4 signed Morse matrix, the explicit unit minor, an independent mod-two rank check, and the reduced Euler-characteristic checksum. The complete generated output appears in `grid7_verify_output.txt` and ends with the token `GRID7_MORSE_OK` at its start. In particular, the row/column counts and integer determinant derive from the code, not a finite statistical experiment. The complete finite enumeration suffices because the stated theorem is about one finite simplicial complex.

## Relationship to prior work
Chauhan, Sharma and Shukla (2026) prove connectivity and homology bounds for all three-row grids and motivate the still-unproved general wedge classification. The present result proves an exact integral homotopy equivalence for one specified seven-column graph; it does not claim the general conjecture. Goyal, Shukla and Singh (2021) originally claimed a much stronger all-length homotopy classification, but the published article explicitly states it was retracted and its March 2025 corrigendum identifies an invalid use of non-induced-subgraph inclusion maps. Its retracted conclusion is not relied upon. Matsushita's 2019 result concerns two-row grids, not this three-row case.

## Limitations
No theorem is asserted for grids with other numbers of columns, for periodic boundary conditions, or for representation theory. The 2026 primary preprint's accessible abstract was checked; its complete text could not be retrieved through available full-text routes. Thus an unindexed, valid identical finite proof remains an originality risk. Independent mathematical audit has not been performed.

## References
- Pratiksha Chauhan, Anchal Sharma and Samir Shukla, *Homology of matching complexes of 3-by-n grid graphs*, arXiv:2609.27366v1 (first public 2026-09-23), https://arxiv.org/abs/2609.27366.
- Shuchita Goyal, Samir Shukla and Anurag Singh, *Matching complexes of 3-by-n grid graphs*, *Electronic Journal of Combinatorics* **28** (2021), P4.16, retraction and March 2025 corrigendum, https://doi.org/10.37236/10496.
- Takahiro Matsushita, *Matching Complexes of Small Grids*, *Electronic Journal of Combinatorics* **26** (2019), P3.1, https://doi.org/10.37236/8480.
- Robin Forman, *Morse theory for cell complexes*, *Advances in Mathematics* **134** (1998), 90–145.
