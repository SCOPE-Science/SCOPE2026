# An integral hook representation for three-nonmatching complexes of thin complete bipartite graphs

## Finding
For each integer \(n\ge3\), define \(X_n\) on the \(3n\) vertices \((r,c)\), with \(r\in\{1,2,3\}\), \(c\in\{0,\ldots,n-1\}\). A set is a face if it does not contain three vertices whose row indices and column indices are each all distinct. This is the nonmatching complex \(\operatorname{BNM}_3(3,n)\). Let \(E_n=\mathbb Z^{\{0,\ldots,n-1\}}\) and \(V_n=\ker(E_n\xrightarrow{\epsilon}\mathbb Z)\), where \(\epsilon(e_c)=1\).

There is an isomorphism of **integral** \(\mathfrak S_3\times\mathfrak S_n\)-modules
\[
\widetilde H_3(X_n;\mathbb Z)\cong\operatorname{sgn}_{\mathfrak S_3}\boxtimes\bigwedge^2V_n.
\]
Every other reduced integral homology group vanishes. The rational representation is the single outer tensor product of irreducible modules \(S^{(1,1,1)}\boxtimes S^{(n-2,1,1)}\), and its dimension is \(\binom{n-1}{2}\). Thus the three-row case of the hook-character prediction for bipartite nonmatching complexes holds, with a stronger specified integral lattice.

## Assumptions and scope
The graph is the ordinary simple complete bipartite graph \(K_{3,n}\), not a graph's two-matching complex, a matching complex, or a cut complex with the graph's vertices as simplicial vertices. The two symmetric groups independently permute its row and column labels. The assertion holds for every integer \(n\ge3\), and reduced integral homology includes the zero-degree case. The homotopy type \(X_n\simeq\bigvee^{\binom{n-1}{2}}S^3\) is *previously established* by Linusson, Shareshian, and Welker (Theorem 1.4), and is an input here, not a new claim.

## Proof
**1. An established free homology group.** Linusson, Shareshian, and Welker's Theorem 1.4 gives \(\widetilde H_3(X_n;\mathbb Z)\cong\mathbb Z^{\binom{n-1}{2}}\), with all other reduced groups zero. In particular, the group is torsion-free. This step uses their full homotopy theorem, not merely a finite experiment.

**2. Three-column orientation.** For \(n=3\), the group above is free of rank one. Its row- and column-permutation actions are both sign characters. Here is an exact finite justification rather than an appeal to a conjecture: enumerate the \(2^9=512\) subsets of the nine edges and retain precisely the \(265\) faces without a three-matching (including the empty face). For any row-column permutation \(g\), compute \(T(g)=\sum_{F:gF=F}(-1)^{|F|}\operatorname{sgn}(g|F)\), with the empty face contributing \(1\). The simplicial Lefschetz formula and degree-three homology concentration imply \(T(g)=\operatorname{tr}(g|\widetilde H_3)\). The exhaustive self-contained calculation in `verify.py` checks for all \(36\) elements that \(T(\sigma,\tau)=\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)\). Since the integral module has rank one, this proves the integral action, not just a rational character.

**3. Retractions and an integral basis.** Fix column \(0\). For \(0<i<j<n\), define \(p_{ij}:X_n\to X_{\{0,i,j\}}\) by keeping columns \(0,i,j\) and sending every other column to \(0\), leaving its row fixed. This is a simplicial map: any three-matching in its image uses three distinct target columns and therefore lifts to a three-matching among three distinct original columns. Thus an admissible face cannot map to a forbidden one. This map fixes its three-column subcomplex pointwise. If \(\{i,j\}\ne\{k,l\}\), the composite of \(p_{ij}\) with the inclusion of \(X_{\{0,k,l\}}\) has image supported on at most two target columns, where the entire edge-set complex is a simplex; it induces zero in degree three. Choose a generator \(z_{0ij}\) of the top integral homology of each three-column subcomplex, compatibly with increasing column order. The homomorphism
\[
P=\bigoplus_{0<i<j<n}(p_{ij})_*:\widetilde H_3(X_n;\mathbb Z)\longrightarrow\mathbb Z^{\binom{n-1}{2}}
\]
sends these included generators to the standard coordinate basis. It is surjective. The source and target are free abelian groups of the same finite rank by Step 1, hence \(P\) is an integral isomorphism and the included classes form an integral basis.

**4. Identify the full column action.** If \(a,b,c\) are pairwise distinct columns, choose the class \(z_{abc}\) from the corresponding three-column inclusion by transporting the chosen orientation of \(z_{012}\) along the order \((0,1,2)\mapsto(a,b,c)\). By Step 2 this class is alternating in the three ordered labels. Its \((i,j)\) retraction coordinate is zero unless \(\{i,j\}\subseteq\{a,b,c\}\). If both occur, the remaining original column is carried to \(0\), and the map is an isomorphism on that three-column subcomplex: its coordinate is the sign of that ordered bijection, by Step 2.

Set \(w_i=e_i-e_0\) for \(1\le i<n\); these form an integral basis of \(V_n\). Identify \(P\)'s coordinate class \(z_{0ij}\) with \(w_i\wedge w_j\). The coordinate rule just proved says, for all ordered triples,
\[
z_{abc}\longmapsto (e_b-e_a)\wedge(e_c-e_a)
=e_b\wedge e_c-e_a\wedge e_c+e_a\wedge e_b\in\bigwedge^2V_n.
\]
This is contraction by the all-ones functional on \(\bigwedge^3E_n\); it is equivariant for every permutation of column labels. Because the classes \(z_{0ij}\) form an integral basis, the displayed identification is an isomorphism of integral \(\mathfrak S_n\)-modules. By Step 2, every row permutation acts on all included generators by its sign, so the two factors act as stated. Finally, the rational hook identification \(\bigwedge^2 V_n\otimes\mathbb Q\cong S^{(n-2,1,1)}\) is the standard exterior-power description of the symmetric-group hook representation.

## Verification
Run `python3 verify.py` (Python standard library only). The attached `verification_output.txt` is the exact output from the embedded verifier executed in its package directory. It exhaustively checks the nine-edge case's signed Lefschetz formula for all \(36\) elements and the twelve-edge case for all \(144\) elements, verifies every simplicial retraction for \(n=3,4,5\) against every face, and checks the dimensions of the integral wedge-coordinate modules. The base enumeration is exhaustive and the general rank comes from the published theorem; the computations are not presented as evidence that testing finitely many widths proves the infinite statement.

## Relationship to prior work
Linusson, Shareshian, and Welker, *Complexes of Graphs with Bounded Matching Size* (2007/2008), prove the nonequivariant homotopy type in Theorem 1.4 and formulate the full bipartite hook-character assertion as Conjecture 1.15. The theorem here proves its \(r=k=3\) subfamily over \(\mathbb Q\), and identifies an integral lattice. Bayer et al., *On the Topology of Cut Complexes of Graphs* (2023), Theorem 28, prove a similar hook representation for the **ordinary cut complex of a complete bipartite graph**; their paper expressly describes the connection to the nonmatching conjecture as future work rather than establishing this claim. Carnero Bravo (2026) treats bounded-independence and total-cut dualities and certain Cartesian products, without deriving this row-column nonmatching module. Shan and Wang (2026) study homology under bipartite edge additions and commutative-algebra invariants for nonmatching complexes; the accessible abstract does not state this equivariant module. A full-text comparison with the Shan–Wang manuscript was unavailable and remains an overlap risk.

## Limitations
Only the family with first part size \(3\) and forbidden matching size \(3\) is resolved, not all parameters in Conjecture 1.15. The proof relies on an established 2007 nonequivariant homotopy theorem, and the finite base-character computation is provided as a reproducible exhaustive certificate. The computation and self-review have not been independently audited. There is no assertion of an equivariant homotopy decomposition or integral quotient-space homology. A full manuscript inspection of the 2026 Shan–Wang preprint was not possible; its abstract alone is not proof of absence of overlap.

## References
1. S. Linusson, J. Shareshian and V. Welker, *Complexes of Graphs with Bounded Matching Size*, J. Algebraic Combinatorics **27** (2008), 331–349, DOI:10.1007/s10801-007-0092-1. Author preprint: https://www.mathematik.uni-marburg.de/~welker/preprints/lsw.pdf (Theorem 1.4; Conjecture 1.15).
2. M. Bayer et al., *On the Topology of Cut Complexes of Graphs*, Séminaire Lotharingien de Combinatoire **89B** (2023), Article 8. https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2023/8.pdf (Theorem 28 and the subsequent comparison).
3. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, first submitted 2026-02-24, https://arxiv.org/abs/2602.21427.
4. J. Shan and Z. Wang, *Homology of non-matching complexes under edge additions and applications to their Stanley-Reisner ideals*, arXiv:2609.02621, first submitted 2026-09-02, https://arxiv.org/abs/2609.02621.
