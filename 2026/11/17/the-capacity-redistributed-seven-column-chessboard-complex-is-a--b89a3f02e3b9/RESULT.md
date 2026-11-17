# The capacity-redistributed seven-column chessboard complex is a wedge of 148 five-spheres

## Finding
Let \(X=\Delta_{[7]}^{(1,2,2,3)}\) be the four-row multiple chessboard complex with one rook permitted per column and row capacities \((1,2,2,3)\). Then, integrally,
\[
X\simeq\bigvee^{148}S^5.
\]
Equivalently, \(\widetilde H_5(X;\mathbb Z)\cong\mathbb Z^{148}\), and \(\widetilde H_i(X;\mathbb Z)=0\) for all integers \(i\ne5\).

## Assumptions and scope
Columns are labeled \(1,\ldots,7\), rows are labeled \(1,\ldots,4\), and a face is any finite subset of the 28 squares containing at most one square from each column and at most \(1,2,2,3\) squares in the respective rows. The empty face is included in the augmented chain complex. The theorem is for this exact finite multiple chessboard complex, without quotienting by permutations. No infinite-family classification is asserted.

## Proof
**Finite face model.** Encode a face by a seven-digit base-five word, in which digit zero leaves a column unoccupied and digits one through four give its selected row. Retain exactly the words satisfying the four row caps. This is a bijection with the faces. Exact enumeration gives the face counts, by cardinality zero through seven,
\[
(1,28,315,1820,5670,9240,6930,1680).
\]
There are 25,684 faces including the empty face and 128,338 cover edges in their augmented Hasse diagram. Their reduced Euler characteristic is \(-148\).

**Acyclic matching.** Starting with no pairs, scan columns from first through seventh and, within each column, rows from first through fourth. For every still-unmatched valid face lacking a square in the current column, pair it with the face obtained by adding the current square whenever this coface is valid and still unmatched. This completely specifies the matching. It produces 12,644 pairs, including the pair of the empty face with one vertex. Direct topological sorting of the *entire* directed augmented Hasse graph, with matching edges oriented upwards and all other cover edges oriented downwards, visits all 25,684 nodes. Consequently the directed graph is acyclic; this is an exhaustive finite proof rather than a sample or heuristic.

Remove the empty face from the poset and leave its former partner unmatched. The remaining matching is still acyclic and has exactly one critical vertex, two critical three-simplices, 124 critical four-simplices and 270 critical five-simplices, with no other critical simplices. Forman's discrete Morse theorem yields a CW model with precisely these critical cells.

**Integral boundary certificate.** Orient every face by increasing column number. For each matched lower face \(f\) with upper mate \(g\), replace \(f\) in a boundary chain using the signed relation
\[
[f:g]\,f=-\sum_{h\in\partial g,\ h\ne f}[h:g]h,
\]
recursively until only critical faces remain; an acyclic gradient ensures termination. Here \([h:g]\in\{+1,-1\}\) is the simplicial incidence coefficient. The exact checker constructs the resulting integral Morse boundary matrices \(D_4\) of shape \(2\times124\) and \(D_5\) of shape \(124\times270\). It verifies \(D_4D_5=0\). Their integer Smith nonzero diagonal invariants are, respectively, two copies of one and 122 copies of one. Therefore \(D_4\) is onto, \(\operatorname{im}D_5=\ker D_4\) because these subgroups have equal rank and the image of \(D_5\) is primitive, and
\[
\widetilde H_5(X;\mathbb Z)=\ker D_5\cong\mathbb Z^{270-122}=\mathbb Z^{148}
\]
with all other reduced integral homology zero. The Smith forms are computed over the integers, not modulo a finite prime.

**From homology to homotopy.** The Morse CW model has one vertex and no one- or two-cells, hence is two-connected. The integral Hurewicz theorem applied successively, together with vanishing homology in degrees three and four, shows that the model is four-connected. Its fifth homotopy group maps isomorphically to \(H_5\cong\mathbb Z^{148}\). Pick 148 maps from \(S^5\) representing a basis and take their wedge. This map induces an isomorphism on all integral homology groups. Since both spaces are simply connected CW complexes, the homological Whitehead theorem makes it a homotopy equivalence, proving the claimed wedge.

## Verification
The embedded `checker.py` enumerates all 78,125 base-five words, checks each cap, constructs the complete matching and all 128,338 cover edges, verifies acyclicity by Kahn's topological sort, reconstructs both signed integer Morse matrices, checks their composition and computes full Smith normal forms. `VERIFICATION_OUTPUT.txt` gives the expected exact outputs. Re-run with Python 3 and SymPy (the `smith_normal_form` function) to reproduce the certificate. A finite exact computation is sufficient here because the theorem concerns exactly this specified finite complex; no extrapolation to other capacity vectors is used.

## Relationship to prior work
Limonchenko and Yu, arXiv:2610.37827 (first publicly submitted October 27, 2026), classify multiple chessboard homotopy types up to three rows. Their Theorem 1.2(1) classifies the *different* four-row family with capacities \((2,2,2,m-5)\), and their Theorem 1.3(1) forces two-torsion when the total capacity is \(m+1\) and at least four entries are at least two. For \(m=7\), their Example 5.6 contrasts the torsion-free complex with capacities \((1,2,2,2)\) (total seven) and the two-torsion complex with capacities \((2,2,2,2)\) (total eight). The present result treats the missing redistributed-capacity case \((1,2,2,3)\), which also totals eight but has only three rows with capacity at least two. It identifies its actual integral homotopy type, showing that simply preserving total capacity does not force the torsion in Theorem 1.3.

Reiner and Roberts (2000, Theorem 3.3) give a representation-theoretic formula for *rational* homology of general multiple chessboard complexes; any rational Betti numbers implied by that formula are acknowledged as prior coverage. The present addition is an exact integral torsion-freeness and homotopy classification, which does not follow from rational Betti data. A narrow comparable classification for capacities \((1,1,1,2)\) in an earlier research record does not cover this instance.

## Limitations
This is a single finite capacity pattern, not a four-row universal theorem; the calculation does not characterize every configuration that avoids torsion. It does not compute the natural row- or column-permutation representation on the 148 homology generators. An equivalent result absent from accessible indexes remains a priority risk. Independent mathematical auditing has not yet occurred.

## References
1. I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827 (submitted 2026-10-27), especially Theorems 1.2–1.3 and Example 5.6. https://arxiv.org/abs/2610.37827
2. V. Reiner and J. Roberts, *Minimal resolutions and the homology of matching and chessboard complexes*, Journal of Algebraic Combinatorics 11 (2000), 135–154, especially Theorem 3.3 and Section 4. https://www-users.cse.umn.edu/~rober005/chessmatch.pdf
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete Morse theorem).
