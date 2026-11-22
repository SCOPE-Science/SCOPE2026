# Nilpotent equivariant endomorphisms: an orbit-type forest product and reconstruction of the table of marks

## Finding

Let \(G\) be an arbitrary finite group and \((X,*)\) a finite pointed \(G\)-set, where \(*\) is fixed by \(G\). Put \(z_*(x)=*\) and let \(\nu_G(X,*)\) count the pointed \(G\)-equivariant self-maps \(f\) with \(f^k=z_*\) for some positive integer \(k\). Write, up to equivariant isomorphism,
\[
X=\{*\}\sqcup\bigsqcup_{i\in I}m_i(G/H_i),\qquad m_i\geq1,
\]
with the \(H_i\) pairwise nonconjugate. Other fixed points are included as copies of \(G/G\). Set
\[
h_{ij}:=|\operatorname{Hom}_G(G/H_i,G/H_j)|=|(G/H_j)^{H_i}|,
\qquad w_i:=h_{ii}=|N_G(H_i):H_i|,
\qquad R_i:=1+\sum_{j\ne i}m_jh_{ij}.
\]
Then the exact all-action formula is
\[
\boxed{\nu_G(X,*)=\prod_{i\in I}R_i(R_i+m_iw_i)^{m_i-1}.}
\]
The empty product equals one. In particular, for a homogeneous pointed \(G\)-set, \(\nu_G(\{*\}\sqcup m(G/H),*)=(1+m|N_G(H):H|)^{m-1}\).

The same nilpotent counts on pointed unions of only two nonbase transitive orbits determine the **entire table of marks** of \(G\), given the isomorphism classes and cardinalities of its transitive \(G\)-sets. More explicitly, for a transitive type \(U=G/H\), define \(\nu(U,U)=\nu_G(\{*\}\sqcup U\sqcup U,*)\), with two distinct copies, and for distinct types \(U,V\) define \(\nu(U,V)=\nu_G(\{*\}\sqcup U\sqcup V,*)\). Then
\[
\nu(U,U)=1+2|\operatorname{End}_G(U)|,\qquad
\nu(U,V)=1+|\operatorname{Hom}_G(U,V)|+|\operatorname{Hom}_G(V,U)|.
\]
For nonisomorphic transitive finite \(G\)-sets there cannot be nonzero hom-set cardinalities in both directions; the only possible nonzero direction runs from the larger orbit to the smaller one. If they have the same cardinality, both hom sets are empty. Hence these two-orbit nilpotent counts recover every \(h_{ij}\), including its orientation, and thereby every fixed-point mark \(|(G/H_j)^{H_i}|\).

## Assumptions and scope

All groups and sets are finite. Maps preserve the selected basepoint and commute with the left \(G\)-action. Nilpotence is with respect to the zero \(z_*\) in the **pointed** endomorphism monoid; it does not mean pointwise nilpotence of a linear operator. No freeness, commutativity, transitivity or faithfulness assumption is imposed on the action. A hom-set cardinality counts maps, not conjugacy classes. The finite-group hypothesis is used critically to exclude proper equivariant self-quotients of a transitive orbit and cyclic chains through unequal orbit types.

## Proof

**Equivariant orbit maps.** A \(G\)-map from \(G/H_i\) to \(G/H_j\) is uniquely determined by the image \(y\) of the coset \(H_i\). Such an image is admissible exactly when \(hy=y\) for every \(h\in H_i\); the number of choices is \(h_{ij}\). When the two transitive orbits are isomorphic, every equivariant map is an isomorphism; in particular, \(h_{ii}=|N_G(H_i):H_i|\). If distinct orbit types admit a map from the first to the second, the first orbit has strictly more points: a transitive equivariant map is surjective, and equality of finite cardinalities would force an isomorphism. Thus the directed graph of distinct orbit types having a nonzero hom-set is acyclic, with orbit sizes strictly decreasing along its edges.

**Nilpotence criterion.** Every pointed equivariant self-map selects, for each nonbase source orbit, exactly one destination orbit (or \(*\)) and one admissible equivariant restriction. Since a source orbit maps surjectively onto its destination, \(f^k=z_*\) holds for some \(k\) if and only if every path in the resulting finite directed orbit graph reaches the distinguished root \(*\); equivalently, no directed cycle remains among nonbase orbits. A directed cycle can only involve copies of one isomorphism type: all edges between distinct types decrease orbit cardinality. Conversely, if each isotypic block has no internal directed cycle, every path strictly descends between blocks until eventually reaching the basepoint. Thus the cycle-avoidance conditions for different types are independent.

**Single-type weighted forest count.** Fix one orbit type \(i\) occurring \(m=m_i\) times. For each labeled source copy, a map to the basepoint or to a different orbit type has exactly \(R=R_i\) choices, independent of choices for other sources. For every *different* target copy of the same type there are \(w=w_i\) isomorphisms. A map from a copy to itself, even by a nonidentity automorphism, creates a one-cycle of orbit labels and is excluded. Thus permissible restrictions are in bijection with rooted directed forests on \(m\) labeled vertices, with each root given one of \(R\) external exit labels and each internal directed edge one of \(w\) labels.

Adjoin one absorbing sink and give edges from each vertex to the sink weight \(R\) and edges from a vertex to any *other* vertex weight \(w\). The directed matrix-tree theorem says the total weight of arborescences directed toward the sink equals the determinant of the \(m\times m\) reduced outgoing Laplacian
\[
L=(R+mw)I_m-wJ_m.
\]
The all-ones vector has eigenvalue \(R\), and its codimension-one complement has eigenvalue \(R+mw\); the determinant therefore equals \(R(R+mw)^{m-1}\). Here \(R\geq1\), so no singular or zero-weight exception is needed. Multiplying these independent factors over the isomorphism types establishes the formula; with no nonbase orbits, the only pointed map is \(z_*\).

**Inverse assertion.** With two copies of the *same* type, the forest factor specializes to \(1+2w_i\), so its nilpotent count extracts the diagonal mark. For two different types \(i,j\), there are exactly three mutually exclusive forms of nilpotent orbit maps: both orbits go to \(*\), the first goes to the second while the second goes to \(*\), or the reverse. These contribute respectively \(1,h_{ij},h_{ji}\). A nonzero hom-set between nonisomorphic transitive finite \(G\)-sets can only run from the orbit of larger cardinality to the smaller one; equal-sized nonisomorphic types admit none. Consequently known orbit cardinalities distinguish the possible direction and recover both values individually. The entries are precisely the usual fixed-point marks, so the full table of marks is reconstructed.

For completeness, the sharp largest possible nilpotency index when at least one nonbase orbit is present is \(\max_{C}\sum_{i\in C}m_i\), where \(C\) ranges over chains of orbit types under existence of a proper equivariant quotient. Indeed, every nilpotent orbit path visits at most all copies of each of a chain of types; for a maximizing chain, direct all its copies sequentially to the next copy or next type and finally to \(*\), while sending other orbits directly to \(*\). Such orbit maps exist by the hom-set criterion. When \(X=\{*\}\), the unique nilpotency index is one.

## Verification

An independent exhaustive Python checker constructs cosets of explicit groups, enumerates every pointed equivariant map from the admissible images of orbit representatives, directly composes each map on **all points** for a number of iterations equal to the total point count, and compares the actual nilpotent count with the product formula computed independently from fixed-point sets. It checks 16 mixed examples for \(C_2,C_3,C_4,S_3\), plus every diagonal and mixed two-orbit probe for \(S_3\). A further \(C_2\times C_2\) example verifies that different equal-cardinality orbit types contribute zero cross-hom counts. The computed recovered table for \(S_3\), ordered by stabilizer orders \(1,2,3,6\), is
\[
\begin{pmatrix}6&3&2&1\\0&1&0&1\\0&0&2&1\\0&0&0&1\end{pmatrix}.
\]
For \(S_3\) with orbit multiplicities \((2,1,1,1)\) in this order, direct enumeration yields \(532\) nilpotent pointed equivariant endomorphisms out of \(8664\) pointed equivariant endomorphisms, agreeing with the product \(133\cdot2\cdot2\cdot1=532\). The executable checker is `check_nilpotent.py`; run `python3 check_nilpotent.py` using Python 3 and no third-party dependencies. Its success sentinel is `POINTED_G_SET_NILPOTENCE_CHECKS_PASSED`.

These finite tests corroborate, but do not replace, the all-finite-group combinatorial proof. No computer enumeration of all finite groups is claimed.

## Relationship to prior work

Castillo-Ramírez and Ruiz-Medina, *The relative rank of the endomorphism monoid of a finite \(G\)-set* (arXiv:2203.12158, first posted 23 March 2022), establish the fundamental orbit-map and wreath-product structure and classify relative generating rank. Their Lemma 3 and Proposition 9 supply relevant ingredients; their main theorem does **not** count maps whose powers reach a distinguished fixed point. Ruiz-Medina, *Cardinalities in finite monoids of \(G\)-equivariant functions* (arXiv:2503.03772), counts unrestricted maps, units and elementary collapsings, not the acyclic nilpotent subfamily. Ruiz-Medina and Lara-Gómez, *Green relations over finite monoids of \(G\)-equivariant functions* (arXiv:2503.14511), study Green classes and elementary collapsings, not this nilpotent factorization. Related published regular-element image profiles count a distinct condition: the regularity census does not determine the nilpotent map count or the weighted-forest factorization. The directed matrix-tree theorem and the classical table of marks are prior standard results, used rather than claimed as new.

The new synthesis is the uniform product for arbitrary orbit-type mixtures and the short-probe reconstruction of every table-of-marks entry from nilpotent endomorphism counts. A specialized older result on nilpotent elements of wreath products, if available, could imply the homogeneous specialization, and a general finite-category forest theorem could imply the product formally. Such potential implicit coverage is a residual priority risk and is not ruled out by a failed keyword search.

## Limitations

The formula concerns **pointed** finite \(G\)-sets; without a selected fixed point, there need not be a zero endomorphism. It counts maps, not their conjugacy classes, exact nilpotency-index fibers or simultaneous nilpotent tuples. The inverse theorem presupposes the indexing and cardinalities of transitive orbit types, and reconstructs the table of marks, **not** necessarily the isomorphism class of the finite group: nonisomorphic groups may share a table of marks. Publication priority is qualified by the limitations of accessible literature and by possible implicit coverage under other terminology. No independent mathematical audit has been conducted.

## References

1. A. Castillo-Ramírez and R. H. Ruiz-Medina, *The relative rank of the endomorphism monoid of a finite \(G\)-set*, arXiv:2203.12158, originally submitted 23 March 2022. https://arxiv.org/html/2203.12158v3
2. R. H. Ruiz-Medina, *Cardinalities in finite monoids of \(G\)-equivariant functions*, arXiv:2503.03772, first posted 4 March 2025. https://arxiv.org/abs/2503.03772
3. R. H. Ruiz-Medina and V. M. Lara-Gómez, *Green relations over finite monoids of \(G\)-equivariant functions*, arXiv:2503.14511, first posted 10 March 2025. https://arxiv.org/abs/2503.14511
4. GAP Reference Manual, Chapter 70, *Tables of Marks*, definition and subgroup fixed-point interpretation. https://gap-system.github.io/gap/doc/ref/chap70.html
5. Directed matrix-tree theorem (classical); used in its standard weighted out-Laplacian form.
