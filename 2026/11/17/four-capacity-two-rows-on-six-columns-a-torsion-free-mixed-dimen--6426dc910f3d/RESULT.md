# Four capacity-two rows on six columns: a torsion-free mixed-dimensional chessboard wedge

## Finding

Let \(X=\Delta_{[6]}^{(2,2,2,2)}\) be the multiple chessboard complex with four rows and six columns: a face is a collection of occupied squares containing at most one square in each column and at most two in each row. Its geometric realization has the **integral homotopy type**

\[
|X|\simeq \bigvee^{88}S^4\vee\bigvee^{5}S^5.
\]

In particular, \(X\) is pure of dimension five, is not shellable, and has torsion-free integral homology: \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^{88}\), \(\widetilde H_5(X;\mathbb Z)\cong\mathbb Z^5\), and all other reduced groups vanish. The result concerns this exact natural board, not all four-row capacity assignments.

## Assumptions and scope

Rows are labelled \(0,1,2,3\), columns \(0,1,\ldots,5\), and each position \((i,j)\) receives bit index \(4j+i\) in an ordinary integer bitmask. The empty face is included in finite chain calculations but excluded from the ordinary nonempty face-poset matching. Coefficients in the homotopy statement are integral; no field assumption is used. Every face extends to a six-rook face because the four rows have combined unused capacity \(8-k\) after \(k\le6\) placements, at least the \(6-k\) still-empty columns, and no additional restriction prevents choosing one available row for each column.

## Proof

**1. Exact face census.** Each column is assigned either an empty choice or one of four rows, subject to at most two uses of each row. The resulting complete counts of nonempty faces, in dimensions zero through five, are

\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(24,240,1200,3060,3600,1440).
\]

Thus there are exactly \(9564\) nonempty faces and Euler characteristic \(84\).

**2. A complete discrete Morse matching.** In order, use the zero-based bit positions

`11,13,0,1,15,3,6,5,20,9,12,8,21,16,4,22,10,14,18,19,23,17,2,7`.

At each position pair every *currently unmatched nonempty face* not containing that bit with the face obtained by adding the bit, whenever the latter is a valid unmatched face; then remove both from further consideration. No face is paired twice. The enclosed verifier constructs all \(42{,}960\) nonempty Hasse cover relations, reverses the \(4727\) matched arrows and topologically sorts the resulting entire directed graph. All \(9564\) vertices are visited, proving that the matching is acyclic. Its critical faces are precisely one vertex, \(96\) four-faces, and \(13\) five-faces. Discrete Morse theory gives a CW complex with exactly those cells and no other cells.

**3. Exact integral attaching matrix.** Orient each simplex by increasing bit index. For every critical five-face, compute its ordinary signed boundary. Whenever a four-face \(u\) is matched upward to a five-face \(v\), substitute the signed relation \(\partial v=\varepsilon u + R\), with \(\varepsilon\in\{\pm1\}\), to eliminate \(u\) by \(u=-\varepsilon R\). Acyclicity makes this substitution terminate. Terms supported on four-faces matched downward to three-faces vanish under the Morse projection. The resulting critical-five-to-critical-four cellular differential is an *integer* \(96\)-by-\(13\) matrix with \(360\) nonzero entries and Smith diagonal

\[
\underbrace{1,\ldots,1}_{8\text{ entries}},
\underbrace{0,\ldots,0}_{5\text{ entries}}.
\]

All computations and orientations are reconstructed by `verify.py`; no numerical floating-point rank or finite-field extrapolation is needed for this integral statement.

**4. Homotopy conclusion.** Since the CW model has just one zero-cell and cells in dimensions four and five, its four-skeleton is a wedge of \(96\) four-spheres. Attaching maps of five-cells lie in its fourth homotopy group, canonically \(\mathbb Z^{96}\) by Hurewicz. Integral elementary basis changes in both the four- and five-cell groups are realized by homotopy equivalences of the corresponding sphere wedges. Therefore the Smith diagonal expresses eight cancelling degree-one five/four cell pairs, leaving \(96-8=88\) four-spheres and \(13-8=5\) five-spheres, establishing the displayed equivalence.

As the original complex is pure five-dimensional and has nonzero homology in dimension four, it cannot be pure shellable (a pure shellable complex has reduced homology concentrated in its top dimension).

## Verification

Run `python verify.py` with Python 3 and SymPy as specified in `requirements.txt`. The executable checks the face counts, constructs the entire matching and directed Hasse graph, performs a complete acyclicity topological sort, constructs the exact signed Morse differential and its integer Smith normal form, and independently recomputes simplicial boundary ranks over the prime fields of orders two, three, and five. It prints `CHESSBOARD_4X6_CAP2_MORSE_PASS` only after every assertion succeeds. `verification_output.txt` is the output actually obtained by executing the embedded program.

## Relationship to prior work

Limonchenko and Yu, *Homotopy types and torsion in homology of generalized chessboard complexes* (first public 27 October 2026, arXiv:2610.37827), classify generalized chessboard complexes with at most three rows and give two explicit families with four and five rows. Their four-row torsion family has capacities \((2,2,2,m-5)\) and \(m\ge7\), and their capacity redistribution theorem shows an integral order-two summand for \((2,2,2,2)\) with **seven** columns. Here the same row capacities with **six** columns have an explicitly proved torsion-free, non-shellable, mixed-sphere homotopy type. The row/column capacities, not merely the number of board cells, distinguish these complexes. The classical ordinary chessboard/matching complexes and four-row complexes with capacities \((1,1,1,2)\) are different objects and do not entail the present exact classification.

## Limitations

The conclusion is nonequivariant and pertains only to the exact four-row six-column object with capacities two and one respectively. It does not determine the full symmetric-group action, nor assert a phase diagram for all numbers of columns. The previously published seven-column torsion result is cited, not claimed as new. Searches cannot rule out an implicit, unindexed, or unpublished equivalent computation; only the introductory classification statements of the closest 2026 source were materially accessible during this investigation, not its complete proof section.

## References

1. I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827v1 (first posted 2026-10-27), https://arxiv.org/abs/2610.37827 . Theorems 1.1–1.3 and introductory classification.
2. D. Jojić, S. Vrećica and R. Živaljević, *Symmetric multiple chessboard complexes and a new theorem of Tverberg type*, arXiv:1502.05290 (2015), https://arxiv.org/abs/1502.05290 . Background on multiple chessboard complexes.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. Discrete-Morse CW reduction.
