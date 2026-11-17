# Ninety-eight four-spheres at the six-column boundary of a four-row multiple chessboard family

## Finding

Let \(X=\Delta_{[6]}^{(1,2,2,2)}\) be the simplicial complex of rook placements on four labelled rows and six labelled columns, with at most one rook in row one, at most two in each other row, and at most one rook in each column. Then the **integral homotopy type** is

\[
|X|\simeq \bigvee^{98}S^4.
\]

Consequently \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^{98}\) and all other reduced integral homology groups vanish. Although \(X\) is pure of dimension five, it is not shellable, and it has no integral homology torsion.

## Assumptions and scope

Rows and columns are distinguishable. A face is a set of squares containing no repeated column and using each row within its specified capacity. The empty set is a face, but it is excluded from the ordinary Forman matching on the nonempty face poset. The assertion concerns this exact six-column complex, equivalently any permutation of the four row capacities, not all four-row chessboard complexes.

This is the six-column boundary case of the parameter pattern \((2,2,2,m-5)\). The previously studied family starts at \(m\ge7\); substituting \(m=6\) gives the present capacities after a row permutation.

## Proof

**Exhaustive finite, integer-valued combinatorial certificate.** Encode the square in row \(r\in\{0,1,2,3\}\) and column \(c\in\{0,1,2,3,4,5\}\) by bit \(4c+r\) in a 24-bit integer. A nonzero mask represents a face exactly when no column has two set bits and row counts respect \((1,2,2,2)\). Both independent exhaustive enumerations in `verify_chessboard.py` (one recursive in columns and one recursive in rows) produce precisely the same 6,309 nonempty masks. Their face counts, in dimensions zero through five, are

\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(24,225,1020,2250,2160,630).
\]

All maximal faces contain six squares: any face of size at most five omits a column; because the sum of row capacities is seven, some row still has unused capacity, allowing a rook in an omitted column. Hence the complex is pure five-dimensional.

Here is a fully specified finite acyclic-matching algorithm. Initialize the set of unmatched faces to all nonzero masks. Process the 24 bit indices in the order

```
17,3,22,21,16,14,4,6,10,12,18,7,13,20,8,0,2,9,23,1,11,15,19,5
```

For each index \(v\), scan the unmatched masks in increasing integer order. If the current mask \(F\) does not contain bit \(v\), and both \(F\) and \(F\cup\{v\}\) remain unmatched, pair those two faces and remove both. The checker independently confirms that every pair has codimension one and no face appears in two pairs.

This produces 3,105 disjoint pairs, leaving **one zero-dimensional critical face and 98 four-dimensional critical faces, with no other critical faces**. To certify acyclicity, orient every cover edge of the nonempty-face Hasse diagram from larger to smaller face, reversing precisely the matched edges. A complete topological sort visits all 6,309 vertices of this oriented diagram, which has 27,090 directed cover edges. A topological ordering of all vertices exists if and only if a finite directed graph is acyclic. Thus the matching is an acyclic discrete-Morse matching, not merely a proposed set of pairings.

Forman's discrete Morse theorem yields a CW model with exactly one zero-cell and 98 four-cells, and no other cells. The attaching map of every four-cell has target the unique zero-cell, so it is constant. Therefore the CW model is exactly a wedge of 98 four-spheres. The construction and its homotopy conclusion are integral and require no field-rank inference. The equality of the actual enumerations and the exhaustiveness of the topological sort are evaluated by the standalone executable checker, whose exact output is included.

Finally, a pure shellable five-dimensional simplicial complex can have reduced homology only in degree five. Since this complex has nonzero fourth integral homology, it is not shellable.

## Verification

Run `python3 verify_chessboard.py` using Python 3 with no third-party dependencies. The output is recorded in `verification_output.txt`. The program verifies all 6,309 faces by two independent constructions; 3,105 matching pairs; 27,090 Hasse incidences; topological-sort acyclicity on all faces; critical dimensions; Euler characteristic 99; and independent mod-two boundary ranks, which give the same fourth reduced Betti number 98. The matching list is deterministically reconstructed from the specified vertex order; its serialized SHA-256 is also printed as a concise fingerprint. Modular calculations are corroboration only, not an integral proof.

## Relationship to prior work

Limonchenko and Yu (first public October 27, 2026) analyze a four-row family with capacities \((2,2,2,m-5)\) for \(m\ge7\), obtaining Moore-space torsion phenomena; their Theorem 5.5 does not include the six-column endpoint. Their Theorem 1.3 requires at least four row capacities of size two to force the indicated two-torsion, whereas this case has only three. The present exact integral wedge decomposition fills this natural boundary case of their parameter pattern, without extending their torsion theorem.

Reiner and Roberts study rational homology and commutative-algebra syzygies of generalized chessboard complexes; rational Betti-number calculations do not themselves determine this integral homotopy equivalence. Jojić, Panina, Vrećica and Živaljević establish discrete-Morse connectivity statements under different inequalities, but these do not give this endpoint's complete homotopy type.

## Limitations

This classification is for exactly four rows with capacities \((1,2,2,2)\), six unit-capacity columns, and its row-relabelled equivalents. No result is claimed for other capacity patterns or more columns, nor for an equivariant homotopy splitting. Exhaustive machine-assisted checking is part of the finite proof; the finite certificate is complete rather than an experiment extrapolated to a parameter family. A matching computation with different encodings should independently reproduce the exact critical-cell census. Prior literature could contain an implicit equivalent calculation not detected in the inspected sources; independent audit has not been performed.

## References

1. I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827v1, first submitted 2026-10-27. https://arxiv.org/abs/2610.37827v1 . In particular Theorems 1.2, 1.3, 5.5 and Example 5.6.
2. V. Reiner and J. Roberts, *Minimal resolutions and the homology of matching and chessboard complexes* (2000), especially Theorem 3.3 and Section 4.
3. D. Jojić, G. Panina, S. Vrećica and R. Živaljević, *Generalized chessboard complexes and discrete Morse theory*, arXiv:2003.04018, especially Theorem 6.1. https://arxiv.org/abs/2003.04018 .
4. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145, discrete-Morse acyclic-matching theorem.
