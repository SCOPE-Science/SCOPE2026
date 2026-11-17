# The sevenfold rotation quotient of the seven-point matching complex has cyclic fundamental group of order twenty-one

## Finding

For the complete graph \(K_7\) on the residues \(\mathbb Z/7\mathbb Z\), let \(M_7=\mathcal M(K_7)\) be the simplicial complex of matchings, and let \(r\) translate every ground-set vertex by one. Then the ordinary quotient of its geometric realization,
\[
 X=|M_7|/\langle r\rangle,
\]
has
\[
\boxed{\pi_1(X)\cong\mathbb Z/21\mathbb Z},\qquad
\boxed{H_j(X;\mathbb Z)\cong
\begin{cases}
 \mathbb Z,&j=0,\\
 \mathbb Z/21\mathbb Z,&j=1,\\
 \mathbb Z^2,&j=2,\\
 0,&j\ge3.
\end{cases}}
\]
The fundamental-group identification, rather than only its abelianization, is part of the result. In particular the two-dimensional quotient is neither simply connected nor a Moore space of the first homology group.

## Assumptions and scope

Vertices of \(K_7\) are labeled \(0,1,\ldots,6\). A vertex of \(M_7\) is an unordered pair \(\{a,b\}\), and its simplices are collections of pairwise vertex-disjoint pairs. The rotation sends \(\{a,b\}\) to \(\{a+1,b+1\}\), with residues taken modulo seven. No special subdivision or twisted quotient is intended: \(X\) is the ordinary topological quotient. Fundamental groups use any basepoint (the space is connected). The calculation is integral and is restricted to seven ground-set vertices and this cyclic action.

## Proof

**Free action and quotient cells.** Every nonidentity element of \(C_7\) generates the seven-cycle on the ground set. Its orbit on any edge of \(K_7\) has size seven. A stabilized nonempty simplex would be a union of complete seven-edge orbits, whereas a matching on seven vertices has at most three edges. Thus the action has no fixed point, including barycenters of faces. The quotient has one cell for each orbit of open simplices, with orientation inherited from increasing lexicographic edge labels. The exhaustive face counts of \(M_7\) are \((21,105,105)\), and all nonempty face-orbits have size seven. Hence the quotient has \((3,15,15)\) cells in dimensions \((0,1,2)\).

**Attaching presentation.** Number the \(21\) edges lexicographically as \(E[0],\ldots,E[20]\). Number an orbit by the lexicographically least increasing sequence of its edge indices. The accompanying certificate `cell_presentation.txt` lists all three vertex orbits, fifteen edge orbits \(A[0],\ldots,A[14]\), and fifteen triangle orbits \(B[0],\ldots,B[14]\). The orbit one-cells \(A[1]\) and \(A[2]\) form a spanning tree and are contracted. For any oriented triangle with vertices \((a,b,c)\), its boundary word is the concatenation of oriented orbit edges \((a,b),(b,c),(c,a)\), reduced by immediate inverse cancellation. The fifteen exact words are in the certificate. Their exponent sums independently coincide with the signed integral cellular boundary matrix.

Choose, successively, generators with exactly one occurrence in a defining relator; solve that relator for the generator, substitute in all remaining words, and freely and cyclically reduce. These are reversible noncommutative Tietze moves. The generator indices eliminated, in order, are

`4, 0, 8, 9, 3, 13, 10, 6, 12, 7, 5, 14`.

Only \(A[11]\) remains, and the relators reduce to \(A[11]^{-21}\), the identity and \(A[11]^{-42}\). Therefore
\[
 \pi_1(X)\cong\langle u\mid u^{21}=1,\ u^{42}=1\rangle\cong\mathbb Z/21\mathbb Z.
\]
This explicitly proves that no nonabelian fundamental-group relations remain: the conclusion is not inferred merely from Smith normal form.

**Integral homology.** The quotient is connected (its one-skeleton has a spanning tree). Hurewicz gives \(H_1(X;\mathbb Z)\cong\pi_1(X)^{\mathrm{ab}}=\mathbb Z/21\mathbb Z\). The complex is two-dimensional, so \(H_2(X;\mathbb Z)\) is a subgroup of the free cellular group \(C_2(X;\mathbb Z)\), hence free. Its Euler characteristic is \(3-15+15=3\). Since the rational first Betti number is zero, \(3=1+\operatorname{rank}H_2\), which proves \(H_2\cong\mathbb Z^2\). Higher homology vanishes for dimension reasons. This argument determines integral groups; it does not infer torsion-freeness from finite-field experiments.

## Verification

The included standard-library program `verify_m7_rotation.py` enumerates all matchings, their rotation orbits, the cellular boundary matrices, a spanning tree and attaching words. It checks \(\partial_1\partial_2=0\), performs all Tietze eliminations on noncommuting words, and verifies the final exponents. Its output appears in `verification_output.txt`. Independent arithmetic cross-checks find \(\operatorname{rank}_\mathbb Q\partial_1=2\), \(\operatorname{rank}_\mathbb Q\partial_2=13\), and \(\operatorname{rank}_{\mathbb F_3}\partial_2=\operatorname{rank}_{\mathbb F_7}\partial_2=12\) while the ranks modulo two and five are thirteen. The nonabelian relator elimination, not the rank calculation, is the fundamental-group certificate. Reproduce with `python3 verify_m7_rotation.py` using Python's standard library.

## Relationship to prior work

Shareshian–Wachs (first public preprint September 3, 2004, building on Bouc), Jonsson, and Mondal–Mukherjee–Saha study the matching complexes themselves, including \(H_1(M_7;\mathbb Z)\cong\mathbb Z/3\mathbb Z\) and \(H_2(M_7;\mathbb Z)\cong\mathbb Z^{20}\). These are established background facts, not claimed as new. The free sevenfold covering explains conceptually why seven-primary information can appear in the quotient; its precise nonabelian \(\pi_1\) and complete quotient homology require the additional attaching-word calculation. Bate–Everitt–Ford–Ramos examine symmetric-group homology representations of matching complexes, not the fundamental group of this ordinary cyclic orbit space. No inspected source asserted an implication yielding the identified fundamental group of this quotient.

## Limitations

The result is for the specified sevenfold action only; it does not classify other subgroup quotients, the equivariant homotopy type of \(M_7\), or the full homotopy type of \(X\). Its exact fundamental-group presentation does not establish an explicit wedge/Moore decomposition. Unindexed or inaccessible equivalent literature remains a publication-priority risk. The proof and certificates are computationally finite and fully specified but have not undergone independent mathematical review.

## References

- J. Shareshian and M. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, first public arXiv submission 2004-09-03, https://arxiv.org/abs/math/0409054.
- J. Jonsson, *Exact Sequences for the Homology of the Matching Complex*, https://arxiv.org/abs/1203.5641.
- A. Mondal, S. Mukherjee and K. Saha, *Topology of matching complexes of complete graphs via discrete Morse theory*, https://arxiv.org/html/2305.02973v5, especially Theorem 1.3.
- M. Bate, B. Everitt, S. Ford and E. Ramos, *Homology of matching complexes and representations of symmetric groups*, https://arxiv.org/abs/2312.13750.
