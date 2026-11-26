# Dihedral orientation and rational quotient topology of two-matching complexes of fully whiskered cycles

## Finding

For each integer \(n\ge 3\), let \(W_n\) be the graph with core vertices \(v_i\), leaves \(w_i\), rim edges \(e_i=\{v_i,v_{i+1}\}\), and pendant edges \(f_i=\{v_i,w_i\}\), with indices modulo \(n\). Let \(X_n=M_2(W_n)\) be its two-matching complex: the simplicial vertices are the \(2n\) graph edges, and a set of such edges is a face if no graph vertex has selected degree greater than two.

The natural dihedral action \(D_n=\langle r,s\mid r^n=s^2=1,\;srs=r^{-1}\rangle\), defined by \(r(v_i)=v_{i+1}\) and \(s(v_i)=v_{-i}\) (and analogously on leaves), acts on the one-dimensional integral top homology of \(X_n\) by

\[
 r_* = (-1)^{n-1},\qquad
 s_* = \begin{cases}(-1)^{(n-1)/2},&n\text{ odd},\\(-1)^{n/2},&n\text{ even}.\end{cases}
\]

More structurally, the complement \(A_n=X_n\setminus\{E_n\}\) of the full rim facet \(E_n=\{e_0,\ldots,e_{n-1}\}\) is a \(D_n\)-invariant contractible subcomplex. Its collapse gives a **dihedrally equivariant map**
\[
 X_n\longrightarrow X_n/A_n\cong |\Delta^{E_n}|/|\partial\Delta^{E_n}|\cong S^{n-1}
\]
that is a nonequivariant homotopy equivalence and induces an integral isomorphism on top homology, carrying the permutation-orientation character of the rim edges. This is not asserted to be a \(D_n\)-equivariant homotopy equivalence.

Consequently, the ordinary orbit space \(|X_n|/D_n\) has reduced rational homology of rank one in degree \(n-1\) precisely when \(n\equiv1\pmod4\), and has no reduced rational homology otherwise. The fixed-point set of the full rotation subgroup satisfies \(|X_n|^{\langle r\rangle}\cong S^0\) for every \(n\ge3\).

The nonequivariant fact \(X_n\simeq S^{n-1}\) is already known from Vega's two-matching-complex analysis. The present claim is the integral dihedral representation, invariant-facet mechanism, and quotient/fixed-set information, not rediscovery of that sphere type.

## Assumptions and scope

Every cycle is a simple \(n\)-cycle, so \(n\ge3\); all homology groups are singular/simplicial homology with indicated coefficients. The group action permutes actual graph edges, hence acts simplicially. The quotient uses the ordinary topological orbit space, **not** the homotopy quotient. The generator \(s\) uses the vertex reflection \(i\mapsto-i\), so its formula is unambiguous even at even \(n\) where two reflection classes exist. The nonzero reduced homology of \(X_n\) is \(\widetilde H_{n-1}(X_n;\mathbb Z)\cong\mathbb Z\).

## Proof

**1. Identify the faces and the invariant facet.** The only forbidden degree-three sets are
\[
 T_i=\{e_{i-1},e_i,f_i\}\quad(i\in\mathbb Z/n\mathbb Z).
\]
Thus a face is a subset of \(E_n\sqcup F_n\) containing no entire \(T_i\), where \(F_n=\{f_0,\ldots,f_{n-1}\}\). The full rim set \(E_n\) is a face, but adjoining any pendant edge violates a constraint, so it is a maximal simplex of dimension \(n-1\). Removing just this facet leaves the subcomplex \(A_n\), stable under all rim dihedral symmetries.

**2. Collapse the facet complement.** For any face \(\tau\in A_n\), put \(C=\tau\cap E_n\), which is a proper subset of rim edges. Choose the least index \(j=j(C)\) such that \(\{e_{j-1},e_j\}\not\subseteq C\). This exists because \(C\ne E_n\). Whether or not \(f_j\in\tau\), toggling \(f_j\) preserves the face condition: its only possible obstruction is the missing pair \(\{e_{j-1},e_j\}\). Pair the two faces \(\tau\setminus\{f_j\}\) and \(\tau\cup\{f_j\}\) in the augmented face poset, including the empty face. Every face of \(A_n\) belongs to exactly one pair.

This matching is acyclic. Along an alternating gradient path, the selected rim-edge set can only stay unchanged or shrink, since matched moves change only a pendant edge. In a closed path it must therefore stay fixed, keeping the same chosen toggle \(f_j\). But after an upward matched move that adds \(f_j\), a distinct downward move retaining the rim set cannot remove \(f_j\); the resulting face still contains \(f_j\) and is the **upper** face of its matched pair, so no next upward matched move is possible. A closed alternating path cannot exist. By elementary acyclic-matching/discrete-Morse theory, this complete matching including the empty simplex leaves one ordinary zero-cell and no other critical cell; \(|A_n|\) is contractible. This uses neither finiteness extrapolation nor an unproved collapse certificate.

**3. Pass to the invariant quotient.** The geometric realization is \(|X_n|=|A_n|\cup|\Delta^{E_n}|\), with intersection \(|\partial\Delta^{E_n}|\). Since \(A_n\hookrightarrow X_n\) is a CW cofibration and \(|A_n|\) is nonempty and contractible, collapsing it to a point is an ordinary homotopy equivalence. All dihedral symmetries preserve \(A_n\), so the quotient map is \(D_n\)-equivariant. The induced action on the single copy of \(\mathbb Z\) in top homology is the orientation sign of the permutation of the \(n\) rim edges.

**4. Compute the signs.** Rotation sends \(e_i\mapsto e_{i+1}\), an \(n\)-cycle, so \(r_*=(-1)^{n-1}\). Reflection sends \(e_i\mapsto e_{-i-1}\). Its fixed rim edges solve \(2i\equiv-1\pmod n\): exactly one if \(n\) is odd, none if \(n\) is even. As an involution of \(n\) objects, its sign is \((-1)^{(n-1)/2}\) or \((-1)^{n/2}\), respectively. These signs give the full integral one-dimensional \(D_n\)-representation.

**5. Quotients and full-rotation fixed points.** For a finite group acting simplicially, barycentric subdivision removes inversions; averaging over \(\mathbb Q\) identifies the rational homology of its ordinary orbit space with the invariant rational homology of the original complex. For even \(n\), rotation acts as \(-1\), so no positive-degree invariant remains. For odd \(n\), rotation acts as \(+1\), and the reflection has sign \((-1)^{(n-1)/2}\), equal to \(+1\) precisely for \(n\equiv1\pmod4\). This proves the quotient assertion, including vanishing in all other degrees. Finally, full rotation is transitive on the \(n\) rim edges and separately on the \(n\) pendant edges. A fixed point's barycentric support must be a union of these two orbits. Each full orbit is a face, but their union is not. Hence the only fixed points are the barycenters of the full rim simplex and the full pendant simplex: exactly a discrete two-point space \(S^0\).

## Verification

The included standalone `verify.py` independently enumerates all faces for \(3\le n\le8\), confirms the explicit matching has one unmatched full-rim facet and pairs every other face, and computes the **signed**, not merely unsigned, simplicial Lefschetz numbers of rotation and reflection. It also checks the two rotation-invariant support orbits. The counts of (augmented) faces are \(45,161,573,2041,7269,25889\), and all checks pass. This computation is finite corroboration; the all-size result follows from the matching and quotient proof above.

## Relationship to prior work

Vega's *2-Matching Complexes* (first arXiv posting September 23, 2019; relevant HTML version January 28, 2021), Proposition 3.7 and Theorem 3.9, proves the already-known nonequivariant sphere homotopy for fully whiskered cycles by discrete-Morse methods. It neither states the integral dihedral homology character nor computes the ordinary dihedral quotient's rational homology or full-rotation geometric fixed locus. The invariant facet-complement quotient above identifies those missing structures. Singh's results on bounded-degree complexes of forests concern acyclic underlying graphs and do not imply the cyclic group action. Dihedral characters of ordinary wheel matching complexes and bounded-independence complexes of cycles are about different complexes and their formulas do not determine the present two-matching action. The character depends on a rim-edge orientation representation absent from the non-equivariant sphere statement.

## Limitations

No integral homology groups of the nonfree dihedral orbit spaces are determined, and the collapse map is **not** claimed to be a \(D_n\)-equivariant homotopy equivalence. The exact fixed loci of proper rotation subgroups and individual reflections are not classified. Equivalent unindexed equivariant computations could exist. No independent audit has been performed.

## References

- Julianne Vega, *2-Matching Complexes*, arXiv:1909.10406 (submitted 2019-09-23), especially Proposition 3.7 and Theorem 3.9 in version 2 (2021-01-28), https://arxiv.org/html/1909.10406v2 .
- Anurag Singh, *Vertex decomposability of complexes associated to forests*, arXiv:2101.05534 (2021-01-14), https://arxiv.org/html/2101.05534v1 .
- Anurag Singh, *Bounded degree complexes of forests*, arXiv:1910.12793 (2019-10-28), https://arxiv.org/abs/1910.12793 .
