# Scientific review

## Correctness — PASS

The group acts freely because a nontrivial row cycle cannot preserve the unique rook in a fixed occupied column. Each quotient cell is therefore a genuine orbit simplex. The two oriented triangular boundaries follow from the column ordering and provide a complete integer presentation for first homology. Eliminating the integral fundamental-cycle generators yields triple-sum relations and exactly one order-three factor once four row-difference generators are present. The \(n=3\) collapse and \(n=4\) orientable surface quotient follow directly. The proof of simple connectivity for the cover when \(n\ge5\) invokes the expressly cited 1994 theorem with its hypotheses verified. The second homology is free as a subgroup of a free two-chain group, and Euler characteristic fixes its rank. The standalone checker independently reconstructs all faces and performs exact Smith reductions through \(n=8\). Risk: a mistake in the signed cell incidences would affect the integer presentation; the checker rederives these from the raw labeled faces.

## Originality — PASS relative to inspected evidence

The 1994 source was inspected through the author-posted full text, particularly its introductions, connectivity theorem, and \(3\times4\) torus discussion. It supplies the premises but does not state the row-rotation orbit-cell presentation or the all-width quotient homology diagram. The 2004 and 2026 preprints describe underlying complexes; the modern paper was accessible only by abstract and is retained as a bibliographic risk. The closest indexed mathematical records concern rotation of **columns**, different graph complexes, or nonidentical reflection actions, so their stated results do not imply the exact present quotient. Absence of identified coverage is not a proof of global novelty.

## Mathematical value — PASS

The three-row chessboard is a standard test object for topological combinatorics. Passing to the natural smallest nontrivial subgroup of row permutations reveals a sharp, integral, **parameter-wide** transition: a rank-two free fundamental group at three columns, a surface group at four, and the nonfree abelian group of order three in every width from five onward. The explicit integer relation matrix explains the exact threshold and distinguishes a genuine order-three quotient class from torsion in the underlying complex, which is absent for all these widths. The simultaneous closed formula for the growing second-homology rank makes the result a complete natural low-dimensional classification, not an arbitrary numerical table or a restatement of shellability.

## Closest sources and residual limits

Björner–Lovász–Vrećica–Živaljević (1994), DOI 10.1112/jlms/49.1.25, supplies the key covering connectivity and the exceptional torus. Shareshian–Wachs, arXiv:math/0409054, concerns unquotiented matching and chessboard torsion. Limonchenko–Yu, arXiv:2610.37827, accessible in abstract only, is a residual novelty risk. The general formula does not identify the \(\pi_2\) module or the full homotopy type of \(Q_n\) for \(n\ge5\).

Self-review: passed. Independent audit: not yet performed.
