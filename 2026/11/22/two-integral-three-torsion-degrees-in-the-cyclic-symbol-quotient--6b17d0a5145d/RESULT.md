# Two integral three-torsion degrees in the cyclic-symbol quotient of partial Latin squares

## Finding
Let \(P_3\) be the simplicial complex on triples \((r,c,s)\in(\mathbb Z/3\mathbb Z)^3\), whose faces are sets of triples that pairwise agree in at most one coordinate. Thus \(P_3\) is the complex of all labelled partial Latin squares of order three, equivalently the independence complex of the Cartesian Hamming graph \(K_3\square K_3\square K_3\). Let \(g(r,c,s)=(r,c,s+1)\) cyclically relabel the symbols, and put \(Y=|P_3|/\langle g\rangle\), the **ordinary geometric orbit space**. Then
\[
\pi_1(Y)\cong\mathbb Z/3\mathbb Z,\qquad
\widetilde H_j(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z/3\mathbb Z,&j=1,3,\\
\mathbb Z^{12},&j=4,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, this natural free cyclic quotient of a torsion-free four-dimensional sphere wedge has two distinct positive-degree order-three homology classes. The result determines integral homology and the fundamental group, **not** the complete homotopy type of the quotient.

## Assumptions and scope
Rows, columns and symbols are individually labelled by \(\{0,1,2\}\). A placement is a face precisely when no two different assignments agree in two coordinates; equivalently no row or column repeats a symbol and no cell receives two symbols. The action is **only** the simultaneous cyclic permutation of the three symbol labels, not a row permutation, column permutation, coordinate rotation, or full isotopism-group action. A setwise invariant nonempty simplex would contain the entire three-element symbol orbit of one of its vertices, violating the one-symbol-per-cell condition. The action is therefore free on the geometric realization, and its quotient has a regular \(\Delta\)-complex cell structure indexed by orbits of faces. It is not generally the ordinary abstract simplicial complex obtained by identifying orbit vertices: distinct simplex orbits may have the same projected vertex set.

For finite-chain conventions number vertices \(9r+3c+s\). Orient each independent face by its increasing *board-cell* indices \(3r+c\), which are distinct on that face. The symbol action preserves this order, so every orbit of a \(k+1\)-vertex face determines an unambiguous oriented integral \(k\)-cell. Boundary operators are signed vertex deletions followed by canonicalization under the three symbol rotations. There are no extra stabilizer coefficients because all nonempty face orbits have size three.

## Proof
**1. The free action and orbit chain model.** Enumerate every independent face by increasing vertex indices, adjoining a vertex only if it agrees in at most one coordinate with each previously chosen vertex. The cardinality face counts, including the empty face, are
\[
(1,27,270,1278,3078,3834,2412,756,108,12).
\]
Canonicalize nonempty face masks under the three symbol rotations and divide each nonempty count by three. The resulting numbers of quotient \(k\)-cells, for \(0\le k\le8\), are
\[
(9,90,426,1026,1278,804,252,36,4).
\]
This is a legitimate integral cellular chain model for the ordinary geometric quotient because the action is free and simplexwise orientation preserving. All quotient boundary compositions are checked to be zero over the integers. A separate cell-by-cell partial-assignment generator (one row/column symbol mask per board cell) obtains the same orbit counts.

**2. Exact integral chain contraction.** Use only coefficient \(\pm1\) boundary entries as pivots; each such pivot permits an integral basis change and cancellation of a consecutive pair of free chain generators. Perform the corresponding Schur-complement updates, including the adjacent boundary maps, without modular division. The standalone checker carries out 1,954 such contractions, with every pivot exactly \(+1\) or \(-1\), and independently rechecks the integral relation \(\partial^2=0\) after reduction. The remaining free chain group ranks in dimensions zero through eight are
\[
(1,1,1,1,13,0,0,0,0).
\]
The reduced differential from dimension one vanishes; from dimension two to one it is multiplication by three; dimension three to two vanishes. The dimension-four to dimension-three boundary is a single row with five entries of absolute value three, four of absolute value six, and four zero entries; its entries have greatest common divisor three. All higher groups vanish. A primitive integer change of basis converts the latter row to \((3,0,\ldots,0)\), so its kernel has rank twelve. Therefore the integral homology is exactly that stated, with no hidden extension or higher torsion.

**3. The fundamental group.** The original complex \(P_3\) has 27 vertices, 270 edges and 1,278 triangular faces. The independent triangle-filling verifier constructs an explicit spanning tree of 26 edges, and then uses the boundary relations of triangles to eliminate every remaining 244 oriented edge generators. At each stage a triangle is used only when two of its three edges have already been eliminated, so the third becomes trivial in the fundamental group. The four rounds eliminate respectively 149, 48, 41 and six edges, leaving none. Thus \(\pi_1(|P_3|)=1\). Since the cyclic symbol action is free, the quotient map is a connected regular threefold covering, with deck group \(\mathbb Z/3\mathbb Z\). Hence \(\pi_1(Y)\cong\mathbb Z/3\mathbb Z\).

## Verification
The three standalone, standard-library-only Python programs in `verification/` regenerate the finite data. Run `python3 verification/check_integral.py`: it checks quotient cell counts, all signed integral boundary compositions, every unit-pivot update, the exact residual differentials and their gcd, and prints `LATIN3_CYCLIC_SYMBOL_QUOTIENT_INTEGRAL_OK`. Run `python3 verification/check_modular.py`: using a different cell-by-cell generator and direct modular Gaussian elimination for primes two, three and five, it checks the Betti vectors \((1,0,0,0,12,0,0,0,0)\) over characteristics two and five and \((1,1,1,1,13,0,0,0,0)\) over characteristic three; it prints `LATIN_CYCLIC_QUOTIENT_MODULAR_OK`. Run `python3 verification/check_pi1.py`: it certifies the spanning-tree and triangle presentation reductions and prints `LATIN_P3_PI1_OK`. The first vector includes unreduced degree-zero rank one. These finite checks prove this fixed finite case; they do not establish an all-order theorem.

## Relationship to prior work
Hämäläinen's *Latin trades and simplicial complexes* (arXiv:0907.1481v1, 2009) constructs trade-intersection complexes of a **fixed** Latin square, not the simplicial complex of all partial squares and not this cyclic-symbol quotient. Falcón's *The set of autotopisms of partial Latin squares* (arXiv:1107.3248v1, 2011) develops permutation actions and fixed-point counting on partial squares, supplying the natural symmetry context, but does not calculate these orbit-space integral homology groups. Existing published calculations of the same underlying \(P_3\) or \(\operatorname{Ind}(H(3,3))\) establish \(P_3\simeq\bigvee^{38}S^4\); they do not classify the integral homology of its symbol-shift orbit space. That known homotopy type and the free action imply the deck group and rational Euler characteristic, but do not alone determine the integral third-homology torsion or all higher integral groups. The direct integer chain computation supplies the missing orbit-space calculation.

## Limitations
This result covers only order three and only the cyclic **symbol** subgroup. It does not assert homology for larger orders, a complete quotient homotopy type, the homology of a quotient by the full isotopism group, or an equivariant chain decomposition. The exact computational proof is independently reproducible from the embedded finite checkers; an independent external mathematical audit has not been performed. The source and prior-record comparisons do not exclude unindexed equivalent research.

## References
1. C. Hämäläinen, *Latin trades and simplicial complexes*, arXiv:0907.1481v1 (first public 2009-07-09), https://arxiv.org/pdf/0907.1481.
2. R. M. Falcón, *The set of autotopisms of partial Latin squares*, arXiv:1107.3248v1 (first public 2011-07-16), https://arxiv.org/pdf/1107.3248.
3. *Thirty-eight four-spheres in the order-three partial Latin-square complex*, public mathematical record identifier `63721f81dfe5`, 2026-10-25, https://github.com/published-finding corpus/2026.
4. *The ternary three-cube independence complex is a wedge of 38 four-spheres*, public mathematical record identifier `77e44648bda3`, 2026-11-08, https://github.com/published-finding corpus/2026.
