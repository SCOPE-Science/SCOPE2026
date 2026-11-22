# Mixed sphere homotopy and full symmetric-group homology of the Petersen matching complex

## Finding

Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, with vertices the ten two-element subsets of \(\{0,1,2,3,4\}\) and edges joining disjoint two-subsets. Let \(K=\mathcal{M}(P)\) be its *ordinary matching complex*: the vertices of \(K\) are the fifteen edges of \(P\), and a finite collection of these edges is a simplex precisely when no two share an endpoint. Then
\[
 K\simeq \bigvee^5 S^2\vee\bigvee^5 S^3.
\]
The five generators in each degree are integral: \(\widetilde H_2(K;\mathbb Z)\cong\mathbb Z^5\), \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^5\), and all other reduced integral homology vanishes.

The full graph automorphism group \(G=\operatorname{Aut}(P)\cong S_5\) acts simplicially on \(K\). Let \(U\cong\mathbb Q^5\) be the natural permutation representation of \(S_5\) on the five labels and let \(\operatorname{sgn}\) be its sign character. As rational \(S_5\)-representations,
\[
 \widetilde H_2(K;\mathbb Q)\cong\operatorname{sgn}\otimes U,\qquad
 \widetilde H_3(K;\mathbb Q)\cong S^{(3,2)}.
\]
Here \(S^{(3,2)}\) denotes the absolutely irreducible five-dimensional Specht representation. In particular, the ordinary topological quotient \(|K|/S_5\) is rationally acyclic, whereas \(|K|/A_5\) has the rational cohomology *ring* of \(S^2\) (not necessarily its homotopy type).

## Assumptions and scope

The matching complex is the complex of sets of *pairwise vertex-disjoint edges* of the ten-vertex Petersen graph. This is distinct from the standard matching complex \(\mathcal{M}(K_5)\), whose one-skeleton is itself the Petersen graph; it is also distinct from a two-matching complex with permitted vertex degree two. We use integral simplicial homology with the increasing order on the fifteen edges as orientations. All rational representation statements concern the natural action induced by permuting the five labels. The homotopy statement is non-equivariant; the quotient statements concern rational cohomology of ordinary topological quotient spaces.

## Proof

**Complete finite model.** List the ten two-subsets of \(\{0,1,2,3,4\}\) lexicographically and then list the fifteen unordered pairs of disjoint two-subsets. A \(d\)-simplex is an increasing \((d+1)\)-tuple of these fifteen edge IDs with pairwise disjoint endpoint sets. Exhaustive enumeration yields the face vector \((15,75,145,90,6)\), so there are \(331\) nonempty simplices and no simplices above dimension four.

**An integral discrete-Morse reduction.** Process the ordered edge-ID pivots
\[
 (1,11,9,8,2,7,0,3,14,5,4,13,10,6,12).
\]
At each pivot, among currently unpaired faces, match every available face not containing the pivot with the face obtained by adjoining it; include the empty face during this process, and omit the unique empty-face pair \((\varnothing,\{1\})\) when passing to the ordinary face poset. The resulting ordinary matching has \(160\) pairs. Explicit orientation of all unmatched cover relations downward and matched cover relations upward yields an acyclic directed graph on all \(331\) nonempty faces; an exhaustive topological-sort certificate is implemented in the accompanying `verify.py`.

Exactly eleven critical faces remain: one zero-cell, five two-cells, and five three-cells. In edge-ID notation, the critical two-cells are
\[
 (0,5,6),\;(2,7,10),\;(4,8,9),\;(5,8,9),\;(12,13,14),
\]
and the critical three-cells are
\[
 (0,4,6,10),\;(0,4,12,13),\;(0,7,10,12),\;(2,4,6,10),\;(5,6,13,14).
\]
For a matched oriented two-face \(\sigma\) paired upward to a three-face \(\tau\), the signed gradient elimination replaces \(\sigma\) using the integral equation \(\partial\tau=0\) modulo the eliminated pair. The recursive algorithm accounts for every signed gradient path, and its \(5\times5\) critical boundary from degree three to degree two is the **zero integer matrix**. With no critical one-cells, this is a CW complex with one vertex, five two-cells attached trivially, and five three-cells whose attaching maps have zero degree on every two-sphere. Since \(\pi_2(\bigvee^5 S^2)\cong\mathbb Z^5\), all five three-cell attachments are nullhomotopic. Forman's simple-homotopy theorem therefore proves the integral wedge decomposition, not just equality of Betti numbers.

**Full rational action.** Every permutation of the five labels induces a signed permutation on each oriented simplicial chain group. Let \(B_2=\operatorname{im}(\partial_3)\), of rank \(79\). Exact modular elimination identifies \(79\) independent columns of \(\partial_3\) and \(79\) pivot rows. Their invertible square submatrix gives the induced trace of each of the \(120\) automorphisms on \(B_2\), computed independently modulo \(1009\) and \(1013\). Because the trace of a finite-order rational operator is an integer in \([-79,79]\), either of these moduli uniquely recovers the integer trace; the two reconstructions agree. Alternating exact chain-trace identities then give the homology characters.

For conjugacy types \(1^5,2\,1^3,2^2\,1,3\,1^2,3\,2,4\,1,5\), the ordered pairs \((\chi_2,\chi_3)\) are, respectively,
\[
 (5,5),\;(-3,1),\;(1,1),\;(2,-1),\;(0,1),\;(-1,-1),\;(0,0).
\]
These satisfy \(\chi_2(g)=\operatorname{sgn}(g)\,|\operatorname{Fix}_{\{0,1,2,3,4\}}(g)|\), which identifies the degree-two representation. The degree-three character equals the permutation character on two-element subsets minus the five-point permutation character, giving \(S^{(3,2)}\). Its normalized squared character norm is \(1\), proving absolute irreducibility. The degree-two character norm is \(2\), corresponding to its sign and four-dimensional signed-standard constituents.

**Quotients.** For a finite group action on a finite simplicial complex, rational cohomology of the ordinary quotient identifies with group-invariant rational cohomology via averaging/transfer. Both reduced characters have zero \(S_5\)-average; restricted to \(A_5\), the degree-two character has average \(1\) and the degree-three character average \(0\). Hence \(|K|/S_5\) is rationally acyclic and \(|K|/A_5\) has one rational generator in degree two and none in other positive degrees. The cohomology ring is that of \(S^2\) because there is no room for a positive-degree product.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter (no additional packages). The standalone checker exhaustively reconstructs the full simplicial complex, all matching pairs, acyclicity of the oriented Hasse graph, the five-by-five exact integer Morse boundary, and the character of all \(120\) automorphisms with two distinct modular reconstruction primes. It independently tests all conjugacy classes, both subgroup averages, and the irreducibility character norms. Its recorded run is `verification_output.txt`, ending in `PETERSEN_MATCHING_MIXED_WEDGE_CHARACTER_PASS`. The finite exhaustive proof uses the transparent enumeration of all matching faces and group elements; the code is part of the argument and should be rerun independently for formal reproducibility. The homotopy deduction from the checked finite Morse model is mathematical, not a finite-sample extrapolation.

## Relationship to prior work

Wachs [1] surveys classical matching complexes of complete graphs and bounded-degree variants. In particular, the classical complex \(\mathcal{M}(K_5)\) is the Petersen graph as a *one-dimensional complex*, and its results cannot be substituted for the matching complex of the Petersen graph itself. Marietti and Testa [2] give recursive homotopy methods for matching complexes of **forests**; the Petersen graph has cycles and is outside that theorem. Zaslavsky [3] analyzes Petersen automorphisms and matchings, but not the integral homotopy type or the full homology action of the simplicial complex of all matchings. The claim here is the combined integral homotopy decomposition and full rational \(S_5\)-module classification for \(\mathcal{M}(P)\), including the rational quotient consequences; classical definitions, general methods, and Petersen automorphism facts are not asserted as new.

## Limitations

The result is confined to the ordinary matching complex of this specific graph. The homotopy equivalence is non-equivariant; no equivariant homotopy inverse is asserted. The quotient results hold with rational coefficients only and do not determine integral torsion or quotient homotopy types. This is a reproducible exact finite calculation plus a standard homotopy argument, not independent mathematical validation. Existing unindexed literature could contain an equivalent computation, and comparison with it remains a publication-priority risk.

## References

[1] M. L. Wachs, *Topology of Matching, Chessboard, and General Bounded Degree Graph Complexes*, Algebra Universalis 49 (2003); freely accessible preprint, https://www.math.miami.edu/~wachs/papers/tmc.pdf.

[2] M. Marietti and D. Testa, *A Simple Uniform Approach to Complexes Arising from Forests*, arXiv:0705.1461v1 (first publicly posted 2007-05-10), https://arxiv.org/abs/0705.1461.

[3] T. Zaslavsky, *Six Signed Petersen Graphs, and Their Automorphisms*, Discrete Mathematics 312 (2012), arXiv:1303.3347; full author manuscript https://people.math.binghamton.edu/zaslav/Tpapers/6sp.pdf.
