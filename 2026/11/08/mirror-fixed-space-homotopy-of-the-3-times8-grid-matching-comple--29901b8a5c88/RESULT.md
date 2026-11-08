# Mirror fixed-space homotopy of the \(3\times8\) grid matching complex

## Finding
Let \(G=P_3\mathbin{\square}P_8\) be the three-row, eight-column grid and \(X=\mathcal M(G)\) its ordinary matching complex. Let \(C(r,c)=(r,7-c)\) reverse the columns, and let \(R(r,c)=(2-r,c)\) reverse the rows. Then the geometric realization fixed-point spaces satisfy
\[
|X|^{\langle C\rangle}\simeq \bigvee^4 S^4,
\qquad
|X|^{\langle R\rangle}\simeq *.
\]
These are integral homotopy types of geometric fixed spaces, not only Euler characteristics, rational Lefschetz numbers or orbit quotients. In particular, the column-fixed space has \(\widetilde H_4\cong\mathbb Z^4\) and no other nonzero reduced integral homology, while the row-fixed space is contractible.

## Assumptions and scope
Rows are \(r\in\{0,1,2\}\), columns are \(c\in\{0,\ldots,7\}\), and grid edges join vertices at Manhattan distance one. A simplex of \(X\) is a set of pairwise vertex-disjoint graph edges. Both involutions act on the corresponding abstract simplicial complex by edge permutation. A geometric fixed point is a point of the usual barycentric realization fixed by the induced linear simplicial homeomorphism. It need not be a point in a simplex whose vertices are individually fixed. No result for unexamined grid widths is asserted.

## Proof
**Fixed-space orbit model.** For either involution \(g\), partition the edges of \(G\) into its edge-orbits. Call an orbit *admissible* when its constituent graph edges are mutually vertex-disjoint. Form a simplicial complex \(Y_g\) with one vertex for each admissible orbit and a simplex for each collection of admissible orbits whose union is a matching of \(G\). Barycentric coordinates in a geometrically \(g\)-fixed simplex must be constant on each edge-orbit, and an orbit with intersecting edges cannot carry positive weight. Assigning each admissible orbit its total barycentric weight defines a piecewise-linear homeomorphism \(|X|^{\langle g\rangle}\cong |Y_g|\), with inverse distributing that weight equally among the orbit's constituent edges. This includes orbits of size one and two.

**Finite exhaustive face models.** A deterministic enumeration constructs all \(37\) graph edges, their involution-orbits, and every set of compatible admissible orbits. For column reflection, \(Y_C\) has \(20\) vertices and exactly \(2636\) faces including the empty face; its Hasse diagram has \(10996\) incidences. For row reflection, \(Y_R\) has \(14\) vertices, \(1156\) faces including empty, and \(4828\) incidences. The independently executable, standard-library-only file `verify_mirror8.py` provides the complete enumeration algorithm rather than relying on an undocumented precomputed table.

**Acyclic Morse matchings.** Order the admissible orbit vertices as produced by the grid-edge enumeration in that file. Starting with all faces unpaired, process each orbit vertex in order, pairing every still-unpaired face not containing it with its coface obtained by adjoining it, whenever both remain unpaired. This is a matching of codimension-one incidences. The supplied checker explicitly constructs every directed Hasse incidence, reverses each matched edge, and exhaustively verifies acyclicity by topological sorting. For \(Y_C\), there are \(1314\) paired incidences, with exactly two critical \(3\)-cells and six critical \(4\)-cells, and no other critical faces. For \(Y_R\), there are \(578\) pairs and **no** critical faces, even in the augmented complex; in particular the empty face is paired. The latter is an ordinary contractibility certificate after the usual reduced-Morse interpretation. Independently, row-reflection admissible orbits split into two noninteracting copies of the path matching complex \(\mathcal M(P_8)=\operatorname{Ind}(P_7)\), which is contractible by the standard path independence-complex recurrence; their join is therefore contractible.

**Signed integral attaching degrees.** Orient each face by the increasing order of its orbit vertices. Algebraic cancellation of matched face/coface pairs yields, from dimension four to dimension three, the signed integer Morse boundary matrix (six rows indexed by the critical four-cells and two columns by the critical three-cells)
\[
\begin{pmatrix}
0&1\\
-1&0\\
1&-1\\
0&0\\
0&0\\
0&0
\end{pmatrix}.
\]
The recursion and all signs are reproduced in `verify_mirror8.py`; these coefficients are not inferred from ranks over a field. The first two rows have determinant \(1\). Since the cellular complex has only two \(3\)-cells and six \(4\)-cells above its basepoint, the two primitive, independent attaching-degree vectors cancel the two three-cells. For a wedge of three-spheres, attaching maps from \(S^3\) are completely determined by their integral degree vectors: \(\pi_3(S^3\vee S^3)\cong\mathbb Z^2\). Elementary integral changes of basis and two unit cancellations leave exactly four four-cells attached at a point. Thus \(|Y_C|\simeq\bigvee^4 S^4\). The verified empty-face pairing supplies the basepoint convention. The row case collapses to a point. Combining with the fixed-space homeomorphisms proves both assertions.

## Verification
Run `python3 verify_mirror8.py` in an otherwise empty directory containing the supplied script. The complete verified output is embedded as `verify_output.txt`. It reports face/ incidence counts, acyclic matchings, critical-cell dimensions, the exact integer Morse matrix, and a unit determinant witness. An **independent** direct simplicial boundary-matrix computation over \(\mathbb F_2\), without using the Morse boundary, returns exactly \(\widetilde\beta_4=4\) for \(Y_C\) and zero other reduced Betti numbers. The same script checks column mirrors for widths \(2,4,6\) as small boundary comparisons. The output ends `ALL_VERIFY_OK`. The result concerns finite explicit spaces, so the face enumeration is complete rather than an extrapolation from a partial sample.

## Relationship to prior work
Chauhan, Sharma and Shukla (arXiv:2609.27366, first submitted 2026-09-23) investigate nonequivariant connectivity and homology of the same family of grid matching complexes. The accessible abstract does not state geometric mirror-fixed homotopy types; the complete preprint could not be inspected and remains an overlap risk. Goyal, Shukla and Singh's earlier paper on nonequivariant \(3\times n\) matching complexes was retracted and is not used as mathematical evidence. The published *Orthogonal-reflection Lefschetz formulas for \(3\times n\) grid matching complexes* determines alternating rational homology traces of the two reflections, not their geometric fixed-point integral homotopy types. The fixed-space results here are more specific than, and do not follow from, those traces: one Euler number is compatible with many different homotopy types. Published results on reflection quotient invariants likewise do not determine geometric fixed spaces.

## Limitations
This is an exact classification of two involution fixed-point spaces for the **single** three-by-eight grid. It does not provide a formula for arbitrary widths, an equivariant splitting of the entire complex, or integral representations of the original complex's homology. Full-text access to the September 2026 preprint was unavailable, so incidental prior coverage cannot be excluded. The computation and the self-review do not constitute an independent external audit.

## References
1. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366 (first posted 2026-09-23), https://arxiv.org/abs/2609.27366.
2. *Orthogonal-reflection Lefschetz formulas for \(3\times n\) grid matching complexes*, published research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-orthogonal-reflection-lefschetz-formulas-for-3-times-n-grid-matc--c1da8c8f4653.
3. S. Goyal, S. Shukla, A. Singh, *Matching Complexes of \(3\times n\) Grid Graphs*, Electron. J. Combin. 28(4) P4.16 (2021), https://doi.org/10.37236/10496. **Retracted**; not used for proof.
