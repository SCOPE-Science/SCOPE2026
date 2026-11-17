# Integral pairing-lattice symmetry of a balanced four-row multiple chessboard complex

## Finding

Let \(X\) be the simplicial complex of placements of rooks on a board of four labeled rows and five labeled columns, with at most two rooks in any row and at most one rook in any column. The natural row- and column-permutation group \(S_4\times S_5\) acts simplicially. Write \(\mathcal P\) for the three unordered perfect pairings of the four row labels, and \(\mathbb Z[\mathcal P]\) for their integral permutation lattice. Then
\[
\widetilde H_3(X;\mathbb Z)\cong\mathbb Z[\mathcal P]\boxtimes\operatorname{sgn}_{S_5}
\]
**as an integral \(\mathbb Z[S_4\times S_5]\)-module.** Thus the Klein-four subgroup of \(S_4\) acts trivially, the induced quotient \(S_4/V_4\cong S_3\) permutes the three generators, and every odd column permutation negates them.

For the same complex, an exact finite discrete-Morse certificate establishes the nonequivariant integral homotopy type
\[
|X|\simeq\left(\bigvee^3 S^3\right)\vee\left(\bigvee^{42}S^4\right).
\]
Its degree-four **rational** symmetry module decomposes multiplicity-free as
\[
\widetilde H_4(X;\mathbb Q)\cong
\bigl(S^{(3,1)}\boxtimes S^{(3,2)}\bigr)
\oplus\bigl(S^{(2,2)}\boxtimes S^{(3,1,1)}\bigr)
\oplus\bigl(S^{(2,1,1)}\boxtimes S^{(2,2,1)}\bigr),
\]
where \(S^{\lambda}\) is the rational Specht module for the indicated symmetric group. No integral decomposition of the rank-42 fourth-homology lattice is claimed.

## Assumptions and scope

Rows are numbered \(0,1,2,3\) and columns \(0,1,2,3,4\). Each of the twenty cells \((i,j)\) is a vertex of \(X\). A set of cells is a face if and only if every column count is at most one and every row count is at most two. Its dimension is the number of chosen cells minus one. The empty face is included in the augmented face complex. Oriented simplices use increasing row-major bit order \(5i+j\); this fixes all integral signs.

The assertion concerns ordinary nonequivariant homotopy and equivariant homology; no equivariant homotopy splitting is asserted. The \(S_4\times S_5\) action preserves the constraints, so the module structures are intrinsic to the object. The integral permutation lattice is stronger information than its rational character, which alone cannot determine the integral form.

## Proof

**1. Finite face census and certified acyclic matching.** Choose any \(k\) columns and one row per chosen column, rejecting assignments in which a row is used three times. This generates every simplex exactly once. An independent loop over all \(2^{20}\) binary cell masks proves agreement. The resulting face counts by cardinality from zero to five are \((1,20,160,600,1020,600)\), including the empty face. For a reproducible matching, process the twenty cell bits in column-major order, and at each bit match all as-yet-unmatched faces not containing that bit to their cofaces obtained by adjoining it, whenever both remain; process lower faces by cardinality and then increasing mask. There are \(1178\) pairs and exactly \(45\) unpaired faces: three of dimension three, forty-two of dimension four, and none in any other degree. The \(9220\) codimension-one incidences are oriented downward except for matched incidences, which are reversed. The accompanying program topologically sorts this *entire* directed Hasse diagram, consuming all \(2401\) vertices. This is an exhaustive acyclicity proof for the stated finite complex, not an inference from sampling. The empty face is paired, leaving the usual based Morse CW model.

**2. Integral Morse boundary and homotopy.** The three critical three-face masks are \((393312,395296,396288)\), in increasing order. For a three-face \(f\) paired upward to a four-face \(u\), write \(\epsilon(u,f)=\pm1\) for its signed incidence and recursively substitute
\[
R(f)=-\epsilon(u,f)\sum_{h\subset u,\ |h|=4,\ h\ne f}\epsilon(u,h)R(h).
\]
For critical three-faces, \(R\) is the corresponding coordinate vector; for three-faces paired downward, \(R\) contributes no critical coordinate. Acyclicity guarantees that this exact integer recursion terminates. Applying it to all boundaries of the forty-two critical four-faces yields a \(42\times3\) integer Morse matrix whose **126 entries are zero**. The reduced CW complex has a point, three three-cells, and forty-two four-cells. Its three-skeleton is \(\bigvee^3 S^3\). Since \(\pi_3(\bigvee^3S^3)\to H_3(\bigvee^3S^3;\mathbb Z)\) is an isomorphism, each attaching map has degree vector zero and is nullhomotopic. Hence the displayed integral wedge decomposition follows.

**3. Integral cycles and the row-pairing module.** For each of the three critical three-faces, start with its oriented simplex and cancel its two-dimensional simplicial boundary recursively using the matched pairs of two-faces with three-faces. The resulting three integral cycles have supports of sizes \(16,24,57\). The program checks every coefficient of their original simplicial boundaries is zero. After cancelling the upward three-to-four matching pairs, their coordinate vectors are the three standard basis vectors, so they represent an integral basis of \(H_3(X;\mathbb Z)\). To compute permutations, apply each row/column relabeling to these signed chains and project using the same integer matching recursions. Every one of the \(24\) row permutations and \(120\) column permutations is checked.

In the critical-coordinate basis, the three vectors
\[
(-1,1,0),\qquad(0,-1,0),\qquad(0,1,-1)
\]
form a unimodular matrix of determinant \(-1\). Under row permutations they transform exactly as the three pairings \((02|13),(03|12),(01|23)\), respectively. Every column permutation acts on all three vectors by its sign. This proves the asserted *integral* module identification, including its integral lattice, not merely a rational isomorphism.

**4. Degree-four rational character.** Because the only reduced homology groups are in degrees three and four, the reduced simplicial Lefschetz formula for any \((\rho,\kappa)\in S_4\times S_5\) is
\[
\operatorname{tr}((\rho,\kappa)|H_4(X;\mathbb Q))
=\sum_{F:\ (\rho,\kappa)F=F}(-1)^{|F|-1}\operatorname{sgn}((\rho,\kappa)|_F)
+\operatorname{sgn}(\kappa)\,|\mathcal P^{\rho}|.
\]
The empty face contributes \(-1\), and signs on nonempty fixed faces use the orientation of their cells. The program computes this class function for every pair of cycle types (five row types and seven column types). Its scalar products with the product Specht characters, computed independently by rim-hook removal, are exactly one for the three constituent pairs in the statement and zero for all others. Their dimensions \(15+12+15=42\) agree with the integral Morse calculation.

## Verification

Run `python3 verify.py` from this package, using only Python 3 standard-library modules. The program rebuilds the complete faces with two independent methods; verifies every matching, every Hasse incidence and global acyclicity; evaluates all signed Morse coefficients; constructs and checks three integral cycles; exhaustively checks all group elements on degree-three integral homology; computes the thirty-five degree-four Lefschetz class values and their irreducible character scalar products; and independently calculates all mod-two boundary ranks. The expected output is `verification_output.json`, and the final status is `PASS`. The reproducible result is specific to four rows and five columns. Neither a floating-point computation nor an extrapolation from smaller boards is involved.

For orientation, the same deterministic matching gives wedges of \(3,9,23,45\) spheres, respectively in dimensions \(0,1,2,3\), for one through four columns with the same four row bounds; the five-column case first has nonzero homology in two distinct positive degrees within this sequence. These smaller cases are checked, not asserted as a general infinite-column theorem.

## Relationship to prior work

Limonchenko–Yu [1] define these complexes and prove comprehensive homotopy results through three rows, plus particular four- and five-row torsion families. Their Theorem 1.1 does not include four rows, and their four-row torsion family in Theorem 5.5 begins at seven columns. Their Proposition 2.2, based on Kustin's duality [3], relates the present homology to a complementary bounded-degree complex. That complement is the ordinary degree-at-most-two edge-set complex of \(K_{4,5}\), for which a public exact homotopy computation [4] gives \(42\) six-spheres and \(3\) seven-spheres. Thus **the nonequivariant homology ranks are not asserted to be new independently of this existing result and duality**; the additional contribution is the explicit *integral* \(S_4\times S_5\)-module and its unimodular pairing-lattice basis. The duality in [3] is equivariant but, without an explicit computation of the complementary integral action, does not supply this lattice identification. The same complementary homotopy statement [4] expressly does not provide an equivariant splitting or action.

Reiner–Roberts [2] gives a general characteristic-zero homological representation framework; the degree-four rational Specht decomposition here is an explicit verified specialization and is not claimed independently to supersede that general theorem. A different six-column complex with the same row bounds is not an implication of the five-column symmetry module. The provenance of the group-action result is a new exact integral chain computation, not a new name for the previously known Betti numbers.

## Limitations

Only the specified four-row five-column complex is classified equivariantly. An integral decomposition of \(H_4\), an equivariant wedge-of-spheres equivalence, maps between different column counts, and generalized four-row formulas are not established. The primary 2008 equivariant Koszul-equivalence article was accessible at abstract level but not in full; possible differently formulated integral module calculations remain a bibliographic risk. The claims are proved by finite complete algorithms whose standalone code and output are included; no external or independent mathematical validation is asserted.

## References

[1] I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827, first public version October 27, 2026. https://arxiv.org/abs/2610.37827

[2] V. Reiner and J. Roberts, *Minimal resolutions and the homology of matching and chessboard complexes*, Journal of Algebraic Combinatorics 11 (2000), 135–154. https://www-users.cse.umn.edu/~rober005/chessmatch.pdf

[3] A. R. Kustin, *An Explicit, Characteristic-Free, Equivariant Homology Equivalence Between Koszul Complexes*, Communications in Algebra 36 (2008), 3263–3316, doi:10.1080/00927870802107140.

[4] *A mixed-dimensional sphere wedge for the two-matching complex of* \(K_{4,5}\), publicly indexed mathematical result, November 1, 2026, which gives the nonequivariant homotopy type \(\bigvee^{42}S^6\vee\bigvee^3 S^7\). Its RESULT.md was inspected in full; no integral automorphism action was asserted.
