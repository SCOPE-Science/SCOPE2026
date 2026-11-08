# Exterior sixth-power symmetry in ninth Kneser-complex homology

## Finding

For every integer \(m\ge 6\), let \(X_m=\operatorname{Ind}(\operatorname{KG}(3,m-6))\). The symmetric group \(S_m\) relabels the ground set, acting simplicially on \(X_m\). There is a natural primitive embedding of integral modules
\[
\bigwedge^{6}\mathbb Z^m\ \longhookrightarrow\ \widetilde H_{9}(X_m;\mathbb Z),
\]
which is a direct-summand inclusion of underlying abelian groups (not asserted to split equivariantly). It becomes an isomorphism after tensoring with \(\mathbb Q\):
\[
\widetilde H_{9}(X_m;\mathbb Q)\cong_{\mathbb Q[S_m]}\bigwedge^{6}\mathbb Q^m.
\]
The ninth rational homology is therefore multiplicity-free: for \(m\ge7\), its irreducible Specht constituents are \(S^{(m-5,1^5)}\) and \(S^{(m-6,1^6)}\), each once. For \(m=6\), it is the one-dimensional sign representation. The character of a label permutation \(g\) with disjoint cycles \(c\) is
\[
\chi_9(g)=[t^6]\prod_{c\in\operatorname{Cyc}(g)}\bigl(1-(-t)^{|c|}\bigr).
\]
For any subgroup \(H\le S_m\), let \(Y_{m,H}=|X_m|/H\) be the geometric orbit space. Its degree-nine rational Betti number is exactly
\[
\dim_{\mathbb Q}\widetilde H_9(Y_{m,H};\mathbb Q)=\frac1{|H|}\sum_{g\in H}[t^6]\prod_{c\in\operatorname{Cyc}(g)}\bigl(1-(-t)^{|c|}\bigr).
\]
In particular, the full-label quotient has zero degree-nine rational homology.

## Assumptions and scope

Here \([m]=\{1,\ldots,m\}\), and the vertices of \(X_m\) are the three-element subsets of \([m]\); a set of vertices is a face when its members have pairwise nonempty intersection. We use integral reduced simplicial homology and ordinary geometric fixed and quotient spaces. The ground-set action is the full label-permutation action, not the graph automorphism group of an unrelated complex. The primary subject is simplicial homology and its symmetry representation (MSC2020: 55U10). The lowest instance \(m=6\) is included; the irreducible two-summand assertion begins at \(m=7\).

## Proof

**1. Geometric cycles indexed by six-element supports.** Fix a six-element subset \(S\subseteq[m]\). The twenty triples in \(S\) come in ten complementary pairs. Within \(S\), two triples are disjoint precisely when they are complementary, so the induced complex \(X_S\) is the join of ten copies of \(S^0\), i.e. the boundary of a ten-dimensional cross-polytope. Give its top fundamental cycle \(z_S\) the orientation induced by the increasing order on \(S\) and by a reference orientation of the ten-coordinate cross-polytope.

**2. Explicit integral separation.** For the six symbols \(1,2,3,4,5,6\), use the ten triples
\[
123,\ 124,\ 135,\ 136,\ 145,\ 146,\ 156,\ 256,\ 345,\ 346.
\]
Here three-digit strings denote triple labels, not integers. They form a pairwise-intersecting family choosing exactly one triple from each complementary pair. It has no two-element transversal: if a transversal contains \(1\), its other element would need to belong to all three of \(256,345,346\), whose intersection is empty; without \(1\), its elements would need to cover all the edges \(23,24,35,36,45,46,56\), including the vertex-disjoint triangle on \(3,5,6\) and the edge \(24\), which requires at least three vertices. Thus any triple containing an element outside the six-symbol support intersects that support in at most two elements and is disjoint from some selected triple. Any unselected triple entirely inside the support is complementary to a selected one. Consequently the selected ten triples form a maximal nine-simplex \(\sigma_S\) of the entire \(X_m\).

Let \(\omega_S\) be the integral elementary cochain evaluating to \(1\) on the appropriately oriented \(\sigma_S\) and to \(0\) on every other nine-simplex. Since \(\sigma_S\) belongs to no ten-simplex, \(\delta\omega_S=0\). The union of its ten triples is exactly \(S\), so \(\sigma_S\) appears in \(z_T\) only if \(S=T\). Orient the fundamental cycle to ensure
\[
\langle[\omega_S],[z_T]\rangle=\delta_{S,T}.
\]
Therefore the map \(\Phi_m\) from the free abelian group on six-subsets to homology, sending \(S\) to \([z_S]\), has an explicit integral left inverse given by the evaluations against these cochains. Its image is an abelian direct summand and hence primitive. These cochain and cycle constructions are the same substantive independence mechanism used in Feng--Wang's lower-bound theorem [1]; the lower bound and the primitive separation are acknowledged as prior coverage, not as the new contribution.

**3. Rational completeness.** Feng's recent homology theorem [2, Section 6] proves
\[
\dim_{\mathbb Q}\widetilde H_9(X_m;\mathbb Q)=\binom m6.
\]
There are precisely \(\binom m6\) linearly independent six-support cycles by Step 2, hence they form a rational basis. No claim of integral torsion-freeness follows: finite torsion may remain outside the primitive free summand.

**4. The orientation character on a six-support sphere.** A permutation of the six labels acts on the twenty triple-coordinate vectors and commutes with the complementation involution. The anti-invariant real subspace under complementation has dimension ten and is the cross-polytope's signed-coordinate representation. The sign of its determinant is the induced action on top integral homology. For a transposition \(g=(12)\), exactly eight triples are fixed, while no triple satisfies \(g(T)=S\setminus T\), since the remaining four labels are individually fixed by \(g\). Thus the trace of \(g\) on the anti-invariant subspace is \((8-0)/2=4\). A ten-dimensional involution with trace \(4\) has exactly three eigenvalues \(-1\), so its determinant is \(-1\). All transpositions are conjugate and generate the six-label symmetric group. The orientation character of a six-support sphere is therefore exactly the sign character.

**5. Exterior-power equivariance.** Orient \(z_S\) by transport of the base sphere orientation along the increasing bijection from \([6]\) to \(S\). The calculation in Step 4 shows that for every label permutation \(g\),
\[
 g_*[z_S]=\operatorname{sgn}(g|_S^{\rm ordered})[z_{gS}],
\]
where \(g|_S^{\rm ordered}\) is the permutation obtained by comparing the increasing orders of \(S\) and \(gS\). This is exactly the action of \(S_m\) on wedge basis elements \(e_{s_1}\wedge\cdots\wedge e_{s_6}\) of \(\bigwedge^6\mathbb Z^m\). Hence \(\Phi_m\) is an integral equivariant primitive embedding, and by Step 3 it becomes the claimed rational isomorphism.

**6. Character and quotient consequences.** For a permutation with a cycle \(c\) of length \(d\), the determinant polynomial on its permutation-coordinate subspace is \(\det(I+tP_c)=1-(-t)^d\). Multiplying over cycles and taking the coefficient of \(t^6\) gives the full ninth-homology character. Write the permutation representation as the trivial line plus the standard augmentation representation; exterior powers give \(\bigwedge^6\mathbb Q^m\cong\bigwedge^6 U_m\oplus\bigwedge^5 U_m\). The standard hook Specht identifications provide the two irreducible constituents (the first term vanishes at \(m=6\)).

Finally, after barycentric subdivision the finite group action is without inversions. Rational cellular chains of the quotient agree with coinvariants of cellular chains of \(X_m\). Coinvariants are exact over \(\mathbb Q\) for a finite group, and their dimensions equal those of invariants, giving the subgroup character average. Neither hook constituent is trivial, so the full symmetric quotient has zero ninth rational homology.

## Verification

The standalone \(\texttt{verify.py}\) checks all \(720\) label permutations on a six-support cross-polytope have the determinant character predicted by sign; explicitly constructs the \(1024\)-facet oriented fundamental nine-cycle and verifies its entire simplicial boundary vanishes; checks its transformation under all \(15\) transpositions; verifies global maximality of the displayed nine-simplex on every six-element support for ground-set sizes \(6\) through \(10\); and compares exterior-power character traces with cycle-product coefficients. Its reproducible output is supplied in \(\texttt{verify_output.txt}\). These finite checks do not replace the unrestricted proofs or the independently cited infinite-dimensional rational Betti theorem.

## Relationship to prior work

Feng and Wang [1, Lemma 9 and Theorem 10] already exhibit globally maximal simplices inside six-support cross-polytopal spheres and dual cochains, proving independent top homology classes. Feng [2, Section 6] determines the complete rational Betti numbers, and explicitly identifies the embedded six-support spheres as natural degree-nine generators in Section 7. Taken together these results supply the underlying rational basis. The distinct claim here is the integral orientation character of its label symmetry, the natural exterior-power module and two-hook Specht decomposition, and the resulting complete ninth rational homology formula for all subgroup orbit spaces. No novelty is claimed for the preceding basis count or for the general representation-theoretic exterior-power identity independently of these spaces.

## Limitations

The classification concerns degree nine of the complexes of pairwise intersecting triples. It does not determine their degree-six symmetry representations, integral torsion outside the indicated primitive lattice, torsion of quotient homology, or their complete equivariant homotopy types. The subgroup quotient formula is rational, not integral. The primitive integral embedding is not claimed to split equivariantly over \(\mathbb Z\). Previously unindexed equivalent equivariant computations cannot be excluded.

## References

[1] Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566, first posted 2024-04-16. In particular, Lemma 9 and Theorem 10, and their explicit cocycle proof.

[2] Z. Feng, *The rational homology of independence complexes of Kneser graphs on triples*, arXiv:2610.17394, first posted 2026-10-12. In particular, Section 6 (ninth rational Betti number) and Section 7 (six-support spheres and open integral questions).

[3] Standard characteristic-zero Specht theory: \(\bigwedge^j U_m\cong S^{(m-j,1^j)}\) for the standard permutation augmentation representation, a familiar hook representation identity used here only after the geometric module has been identified.
