# An index-162 integral symmetry obstruction for a multiple chessboard complex

## Finding

Let \(X=\Delta^{(2,2,2,2)}_{[6]}\) be the multiple chessboard complex with four labeled rows and six labeled columns: a face is a set of squares with at most one square in each column and at most two in each row. Its row and column permutation groups \(S_4\times S_6\) act simplicially. Put \(K=\widetilde H_5(X;\mathbb Z)\).

Let \(M_j=\mathbb Z\bigl[\binom{[6]}{j}\bigr]\) be the integral permutation lattice on \(j\)-subsets of the six columns. Define the unsigned inclusion boundary
\[
W:M_3\longrightarrow M_2,\qquad [T]\longmapsto\sum_{B\subset T,\ |B|=2}[B],
\]
and let \(L=\ker W\), equipped with its natural column-permutation action. Then:

1. \(K\) and \(L\) are free abelian of rank five. Every row permutation acts trivially on \(K\), and there is a rational \(S_6\)-module isomorphism \(K\otimes\mathbb Q\cong L\otimes\mathbb Q\cong S^{(3,3)}\), the five-dimensional irreducible representation.
2. The group of integral column-equivariant homomorphisms \(\operatorname{Hom}_{\mathbb Z[S_6]}(L,K)\) is infinite cyclic. A generator \(\Phi\) is injective and has quotient, as an abelian group,
\[
K/\Phi(L)\cong (\mathbb Z/3\mathbb Z)^3\oplus\mathbb Z/6\mathbb Z.
\]
3. Every nonzero integral column-equivariant map \(L\to K\) is multiplication of \(\Phi\) by a nonzero integer. In particular its image has index at least \(162\), with equality precisely for \(\pm\Phi\). Thus **\(K\) and \(L\) are not isomorphic as integral \(S_6\)-lattices**, despite being rationally isomorphic.

This is an integral representation statement; it is not a new assertion of the previously known nonequivariant homotopy type \(|X|\simeq\bigvee^{88}S^4\vee\bigvee^5S^5\).

## Assumptions and scope

Rows are \(0,1,2,3\), columns are \(0,1,\ldots,5\), and a six-rook facet is encoded by its lexicographically ordered row-word \(f=(f(0),\ldots,f(5))\). All row multiplicities are at most two. Orient each facet in increasing column order. The group \(S_6\) permutes the columns and acts on the oriented six-rook basis with the sign of the induced column permutation. A row permutation changes the row labels without changing this orientation. The subset permutation lattices have their usual unsigned bases. All homology and all kernels are integral unless a coefficient field is indicated. The result concerns precisely this finite complex and these two explicitly defined integral lattices.

## Proof

**1. The complete fifth-cycle lattice.** Enumerate lexicographically the \(1440\) admissible row-words \(f:[6]\to[4]\). There are \(3600\) distinct five-rook faces occurring in their simplicial boundaries. For each word, deleting the entry in column \(j\) contributes the oriented five-rook face with coefficient \((-1)^j\). Thus \(\partial_5\) is an explicitly defined \(3600\)-by-\(1440\) integer matrix. There are no six-dimensional simplices, so \(K=\ker\partial_5\).

Perform integer elimination on each boundary row, always choosing its largest nonzero column as the pivot and removing earlier pivot rows. **All \(1435\) nonzero pivot coefficients are units**; the remaining free-coordinate indices (zero-based lexicographic word ordering) are \((0,4,54,58,90)\). Back-substitution gives five integral vectors in \(\ker\partial_5\), with respective nonzero-support sizes \((768,576,576,576,576)\). Because every pivot is a unit, arbitrary integral values of the five free coordinates produce all integral kernel vectors. These five vectors are consequently an integral basis, not merely a basis over \(\mathbb Q\). The included self-contained checker constructs the entire matrix, tests every unit pivot and every boundary equation, and reconstructs this basis.

**2. The canonical comparison lattice.** Order the \(20\) three-subsets and \(15\) two-subsets lexicographically. The \(15\)-by-\(20\) incidence matrix \(W\) has rank \(15\). Exact rational elimination, followed by checking that every free-coordinate basis vector has integral coefficients, identifies the full integer kernel \(L\) of rank five; its free coordinates are \((0,1,2,4,5)\). Indeed, every integral solution has integral values at those free coordinates, and integral solutions are uniquely reconstructed from them. The rational permutation module \(M_3\otimes\mathbb Q\) decomposes as \(S^{(6)}\oplus S^{(5,1)}\oplus S^{(4,2)}\oplus S^{(3,3)}\); the surjective incidence map to \(M_2\otimes\mathbb Q\) removes the first three constituents. Therefore \(L\otimes\mathbb Q\cong S^{(3,3)}\).

**3. Exact symmetry actions.** Act on each integral basis vector of \(K\) by the five adjacent column transpositions \((0\ 1),(1\ 2),\ldots,(4\ 5)\), including the sign from reordering the six occupied columns. Read the resulting vectors in the five free coordinates to obtain integral matrices \(C_0,\ldots,C_4\). Similarly, apply the same transpositions to three-subsets and read the five free coordinates of \(L\) to obtain \(D_0,\ldots,D_4\). The explicit generator matrices are given in `verification_output.json`, and their full construction is in `verify.py`. The program verifies the involution, braid and distant-commutation relations for each set of matrices. It independently checks that the three adjacent row transpositions act as identity on \(K\). The trace of each adjacent column transposition on each lattice is \(1\).

**4. The complete space of equivariant maps.** An arbitrary integral equivariant map \(L\to K\) is represented by a five-by-five integer matrix \(Q\) satisfying all five equations \(C_iQ=QD_i\). Form these \(125\) integer linear equations in the \(25\) entries of \(Q\). Exact rational row reduction has rank \(24\), leaving a one-dimensional rational solution space. Its primitive integer generator, in the bases above, is
\[
Q=\begin{pmatrix}
3&1&2&2&4\\
-3&-2&-1&-4&-2\\
-3&-2&-4&-1&-2\\
3&4&2&2&1\\
-3&-2&-1&-1&1
\end{pmatrix}.
\]
Its entries have greatest common divisor one. Consequently the only integral matrices on the rational line \(\mathbb Q Q\) are exactly the integer multiples of \(Q\). This proves \(\operatorname{Hom}_{\mathbb Z[S_6]}(L,K)\cong\mathbb Z\) with generator \(Q\); in particular, there cannot be a hidden integral equivariant isomorphism represented by a different change of basis.

**5. Index and invariant factors.** The exact determinant is \(\det Q=-162\). To obtain the full additive quotient, compute the gcds of *all* minors of each order \(1\) through \(5\), giving the Smith diagonal
\[
\operatorname{SNF}(Q)=\operatorname{diag}(1,3,3,3,6).
\]
This proves the quotient formula and index \(162\). The general equivariant map \(kQ\) for nonzero \(k\in\mathbb Z\) has index \(162|k|^5\), establishing exact minimality. Since \(\det Q\ne0\), it also gives the rational equivariant isomorphism of the first statement.

## Verification

The included `verify.py` uses only the Python 3 standard library. Run `python3 verify.py` in the same directory as the supplied `verification_output.json`. The program exhaustively constructs every six-rook facet and its complete signed boundary, proves the integral basis with unit pivots, constructs the full three-to-two subset incidence matrix and its integral kernel, generates and checks all adjacent symmetric-group generator matrices and the row action, solves all \(125\) intertwiner equations over exact fractions, and computes the integral determinant and Smith factors using gcds of every square minor. It prints a JSON object with `"status":"PASS"` only after every assertion succeeds. `verification_output.json` is the captured result of executing this exact script.

The proof uses complete finite exact computations and standard permutation-module decomposition; finite sampling, floating-point rank computations and assertions inferred from a timeout are not used.

## Relationship to prior work

Limonchenko and Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, first available October 27, 2026, establish broad multiple-chessboard homotopy and torsion results, including the seven-column order-two-torsion example with capacities \((2,2,2,2)\). Their article supplies the natural nearby setting but does not state the six-column integral symmetry comparison here.

A published exact six-column computation, *Four capacity-two rows on six columns: a torsion-free mixed-dimensional chessboard wedge* (November 17, 2026), already establishes the nonequivariant \(88\)-four-sphere and \(5\)-five-sphere classification; its result explicitly leaves the full symmetric-group action undetermined. This known rank-five homology is an input and **not** claimed as new. The earlier *Integral pairing-lattice symmetry of a balanced four-row multiple chessboard complex* concerns five columns and a distinct rank-three homology degree. Neither statement provides the present index-\(162\) integral comparison for six columns.

The rational decomposition is compatible with the established rational representation-theoretic treatment of chessboard homology by Reiner and Roberts, and the inclusion-kernel lattice belongs to the classical theory of subset incidence maps, including the work of Rónyai. Equivariant Koszul duality in Kustin's work relates certain integral homology objects but does not, from the available statements, compute this specific primitive intertwiner and index. The contribution is the explicit **integral** lattice distinction, not the abstract existence of rational Specht modules or incidence kernels.

## Limitations

The theorem determines the complete integral \(S_4\times S_6\) action only in fifth homology and only for the specified four-by-six multiple chessboard complex. It does not determine the integral fourth-homology action, an equivariant homotopy splitting, or analogous lattice indices for other capacity profiles. The quotient description is as an abelian group; no full quotient-module presentation is asserted. The particular comparison lattice is defined intrinsically as the three-to-two-subset incidence kernel, not claimed to be the unique possible integral form of the rational Specht representation. A general equivariant description hidden in uninspected published text remains a priority risk. Independent mathematical validation has not been performed.

## References

1. I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827v1, first public 2026-10-27, https://arxiv.org/abs/2610.37827 .
2. *Four capacity-two rows on six columns: a torsion-free mixed-dimensional chessboard wedge*, published mathematical record, 2026-11-17, https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-four-capacity-two-rows-on-six-columns-a-torsion-free-mixed-dimen--6426dc910f3d/RESULT.md .
3. *Integral pairing-lattice symmetry of a balanced four-row multiple chessboard complex*, published mathematical record, 2026-11-17, https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-integral-pairing-lattice-symmetry-of-a-balanced-four-row-multipl--cb4d18162d1c/RESULT.md .
4. V. Reiner and J. Roberts, *Minimal resolutions and the homology of matching and chessboard complexes*, Journal of Algebraic Combinatorics 11 (2000), 135–154, https://doi.org/10.1023/A:1008728115910 .
5. L. Rónyai, *Specht modules and incidence matrices*, Annales Universitatis Scientiarum Budapestinensis, Sectio Computatorica 56 (2024), 305–317, https://doi.org/10.71352/ac.56.305 .
6. A. R. Kustin, *An explicit, characteristic-free, equivariant homology equivalence between Koszul complexes*, Communications in Algebra 36 (2008), 3263–3316, https://doi.org/10.1080/00927870802107140 .
