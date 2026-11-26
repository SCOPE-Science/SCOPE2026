# The integral label-and-inversion character of a partial-injection commuting complex

## Finding
For every integer \(n\ge2\), let \(I_n\) be the symmetric inverse monoid of partial injections on \([n]\). Write \(a_{ij}\) for the rank-one square-zero partial injection defined only at \(i\) and taking \(i\) to \(j\), for \(i\ne j\). Let \(K_n\) be the clique complex whose vertices are the \(a_{ij}\) and whose nonempty faces are sets of pairwise commuting distinct such partial injections.

Conjugation by label permutations and semigroup inversion act on \(K_n\), giving an action of \(S_n\times C_2\). The **integral equivariant homology theorem** is
\[
\widetilde H_k(K_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z_{\chi_n},&k=n-2,\\
0,&k\ne n-2,
\end{cases}
\qquad
\chi_n(\sigma,\varepsilon)=\operatorname{sgn}(\sigma)(-1)^{(n-1)\varepsilon},
\]
where \(\varepsilon\in\{0,1\}\) records whether all partial injections are inverted. In particular, inversion reverses the integral homology generator for even \(n\) and fixes it for odd \(n\), whereas every transposition of labels reverses that generator. The homotopy type of the underlying complex is the sphere \(S^{n-2}\); **that nonequivariant sphere result is a previously known fact for directed bipartite graph complexes, not claimed here as new**.

## Assumptions and scope
The group \(S_n\) acts by \(\sigma a_{ij}\sigma^{-1}=a_{\sigma(i),\sigma(j)}\), and the nontrivial element of \(C_2\) acts by \(a_{ij}\mapsto a_{ji}\). These actions commute, preserve commutation and act simplicially. All homology groups are reduced integral simplicial homology, including \(\widetilde H_0\) for \(n=2\). No assertion is made about the commuting clique complex on elements of larger rank.

## Proof
**1. Commuting faces.** The composite \(a_{ij}a_{k\ell}\) is nonzero only if one of the target/source equalities \(j=k\) or \(\ell=i\) holds (according to the multiplication convention). For distinct arcs both composites, when nonzero, are different singleton partial injections; thus
\[
a_{ij}a_{k\ell}=a_{k\ell}a_{ij}\quad\Longleftrightarrow\quad j\ne k\ \text{and}\ \ell\ne i.
\]
Consequently a nonempty face is precisely a nonempty set of directed edges whose sets of sources and targets are disjoint. In particular its sources and targets are nonempty. The maximal faces are the complete directed bipartite edge sets \(S\times T\) with \(S\sqcup T=[n]\), both parts nonempty; hence there are \(2^n-2\) maximal faces.

**2. Equivariant poset comparison.** Let \(Q_n\) be the poset of nonempty faces of \(K_n\), ordered by inclusion. Let \(P_n\) be the poset of ordered pairs \((S,T)\) of disjoint nonempty subsets of \([n]\), ordered coordinatewise by inclusion. The source/target map \(f:Q_n\to P_n\) is order-preserving and \(S_n\times C_2\)-equivariant (the second factor exchanges the two components). For each \((S,T)\in P_n\), the inverse image of its lower ideal consists of all nonempty edge subsets of \(S\times T\). This is the nonempty face poset of a simplex and is contractible. The poset-fiber homotopy theorem therefore gives a homotopy equivalence \(|\Delta Q_n|\simeq|\Delta P_n|\) induced by \(f\). Since \(f\) is equivariant, its induced isomorphism on **integral homology is equivariant**. Note that no equivariant strengthening of the fiber theorem is needed: the underlying homology isomorphism already commutes with the action.

**3. Mixed faces of a cross-polytope.** The \((n-1)\)-sphere \(X=\{x\in\mathbb R^n:\sum_i|x_i|=1\}\) is the boundary of the cross-polytope. Its face poset is indexed by disjoint pairs of positive- and negative-coordinate supports. The subposet \(P_n\) indexes exactly the *mixed-sign* faces, with both supports nonempty. Let \(F_+\) and \(F_-\) denote the all-nonnegative and all-nonpositive opposite closed facets of \(X\). Their union is a simplicial subcomplex \(A\). The induced subcomplex of the barycentric subdivision of \(X\), on barycenters of faces outside \(A\), is \(\Delta P_n\). The standard barycentric-coordinate retraction of \(X\setminus A\) onto this induced subcomplex discards barycentric coordinates belonging to faces in \(A\) and renormalizes the remaining coordinates. Every point of \(X\setminus A\) has a positive total of retained coordinates. The construction is equivariant under coordinate permutations and simultaneous sign reversal.

**4. An explicit equivariant sphere retraction.** A point of \(X\setminus A\) has at least one positive and one negative coordinate. Put \(m(x)=\frac1n\sum_i x_i\). The maps
\[
H_t(x)=\frac{x-tm(x)\mathbf1}{\sum_i|x_i-tm(x)|},\qquad 0\le t\le1,
\]
remain in \(X\setminus A\): subtracting \(tm(x)\), which lies between the minimum and maximum coordinates, never removes both signs. At \(t=1\) the coordinate sum is zero, while points of sum zero are fixed for every \(t\). Thus this is a strong deformation retraction onto \(X\cap V\), where \(V=\{x:\sum_i x_i=0\}\cong\mathbb R^{n-1}\), an \((n-2)\)-sphere. The homotopy commutes with coordinate permutations and the simultaneous sign reversal \(x\mapsto-x\).

**5. Integral character.** Coordinate permutation \(\sigma\) fixes the orthogonal line \(\mathbb R\mathbf1\) pointwise and has determinant \(\operatorname{sgn}(\sigma)\) on \(\mathbb R^n\); it therefore has determinant \(\operatorname{sgn}(\sigma)\) on \(V\). The antipodal map on its unit sphere has degree \((-1)^{\dim V}=(-1)^{n-1}\). Hence the action on the orientation lattice \(\widetilde H_{n-2}(X\cap V;\mathbb Z)\cong\mathbb Z\) is precisely \(\chi_n\). The equivariant homology isomorphism from step 2 transfers this character to \(K_n\), proving the theorem and the vanishing of all other reduced groups.

## Verification
The standalone `verify.py` implements partial-injection compositions and enumerates all faces for \(2\le n\le5\), comparing their exact mod-two boundary ranks with those of a sphere. It independently calculates Lefschetz traces for the identity, a transposition, a full label cycle, inversion, and their products; all match the predicted integer homology character. These finite checks corroborate but do not replace the arbitrary-\(n\) proof, which is integral rather than merely mod-two.

## Relationship to prior work
Araújo, Bentz and Konieczny study commuting graphs, clique numbers and commutative subsemigroups of \(I_n\). Jonsson's *Simplicial Complexes of Graphs*, chapter on directed bipartite digraphs, already identifies the nonequivariant sphere homotopy type of the corresponding digraph complex. That topological classification is **not** a novelty claim here. The claimed increment is the exact **integral \(S_n\times C_2\)-module** on its top reduced homology, identifying separately the label-sign and arrow-reversal signs for all \(n\). The result is compared with algebraic-semigroup clique work and directed graph complex topology, not solely by title search.

## Limitations
The inaccessible full text of Jonsson's most relevant chapter could contain an equivalent group-action calculation; this is an explicit literature-priority risk. Published summaries confirm the nonequivariant sphere result but cannot rule out an earlier equivariant refinement. The result does not address integral higher homology of the full commuting complex of \(I_n\) or other inverse monoids. Independent mathematical review has not been performed.

## References
- J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, 2008, Chapter 15, “Directed Variants of Forests and Bipartite Graphs,” pp. 205–215, DOI: 10.1007/978-3-540-75859-4_15. Original thesis appeared in 2005 (exact first-public day not verified); the 2007-11-15 print publication date is publisher-verified.
- J. Araújo, W. Bentz, J. Konieczny, “The Commuting Graph of the Symmetric Inverse Semigroup,” arXiv:1205.1664, initially submitted 2012-05-08.
- D. Quillen, “Higher Algebraic K-Theory I,” 1973, the classical poset-fiber homotopy theorem; used as a standard proof tool rather than as novelty.
