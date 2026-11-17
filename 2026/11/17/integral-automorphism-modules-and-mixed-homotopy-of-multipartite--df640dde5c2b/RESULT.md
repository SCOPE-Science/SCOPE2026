# Integral automorphism modules and mixed homotopy of multipartite general-position complexes

## Finding
Let \(G=K_{a_1,\ldots,a_r}\) be a complete multipartite graph with \(r\ge2\), every \(a_i\ge1\), and vertex parts \(V_i\). Define \(\mathcal{GP}(G)\) as the simplicial complex of sets in *graph-geodesic general position*: no three selected vertices lie on one shortest graph path. The complex has the integral homotopy type
\[
|\mathcal{GP}(G)|\simeq\bigvee^{\sum_{i=1}^{r}(a_i-1)} S^1\ \vee\ \bigvee^{\prod_{i=1}^{r}(a_i-1)} S^{r-1}.
\]
Empty wedges are omitted. For \(r=2\), the two families of circles combine, yielding exactly \(a_1a_2-1\) circles. In particular, when \(r\ge3\) and all part sizes are at least two, the complex has nonzero homology in **two different degrees**.

The stronger new statement determines the entire integral homology action of \(\operatorname{Aut}(G)\), including permutations of equal-sized parts. For each \(i\), let
\[
I_i=\ker\!\left(\varepsilon_i:\mathbb Z[V_i]\longrightarrow\mathbb Z\right),\qquad \varepsilon_i\Big(\sum_vn_v[v]\Big)=\sum_vn_v.
\]
If \(r\ge3\), the only possibly nonzero reduced integral homology modules are
\[
\widetilde H_1\bigl(\mathcal{GP}(G);\mathbb Z\bigr)\cong\bigoplus_{i=1}^{r}I_i,
\qquad
\widetilde H_{r-1}\bigl(\mathcal{GP}(G);\mathbb Z\bigr)
\cong \left(\bigotimes_{i=1}^{r} I_i\right)\otimes\operatorname{sgn}_{\mathrm{parts}}.
\]
An automorphism maps each summand \(I_i\) to the corresponding summand on its image part. On the tensor, it applies the induced vertex bijections, reorders the factors, and multiplies by the sign of this reordering. The sign is essential even though all parts are discrete complexes.

If \(r=2\), write \(E=V_1\times V_2\) for the unordered graph edges with their canonical first/second shore convention. Let \(\mathbb Z[E]_0\) denote the integer coefficient-sum-zero sublattice. Then
\[
\widetilde H_1\bigl(\mathcal{GP}(G);\mathbb Z\bigr)
\cong \mathbb Z[E]_0\otimes\operatorname{sgn}_{\mathrm{shores}}.
\]
Here the graph automorphism permutes edges; a shore exchange also negates the resulting homology element. If the shores have unequal cardinalities, no exchange is possible. The module is not asserted to split as a sum of augmentation modules over the integers.

## Assumptions and scope
Graph distances are shortest-path distances in the original *connected* complete multipartite graph. A general-position face is allowed to be empty. A part may have one vertex. The canonical parts are the equivalence classes of the nonadjacency relation together with equality; graph automorphisms preserve their sizes and may permute equal-size classes. All homology and homotopy are ordinary nonequivariant spaces unless an integral \(\operatorname{Aut}(G)\)-action is explicitly stated; no equivariant homotopy splitting is claimed.

## Proof
**1. Exact simplicial decomposition.** Distinct vertices in different parts have distance one, while two vertices in the same part have distance two. Thus a selected triple lies on one shortest path exactly when it contains two vertices of one part and a vertex of another part. Consequently, each general-position set is either wholly contained in a single part or meets each part in at most one vertex. This description is Theorem 3.1 of Rather (2026), not a new combinatorial claim. With \(D_i\) the zero-dimensional complex on \(V_i\), put
\[
B=D_1*\cdots*D_r,\qquad A_i=2^{V_i}.
\]
Then the complete labelled complex, without omitted faces, is
\[
\mathcal{GP}(G)=B\cup A_1\cup\cdots\cup A_r,
\quad A_i\cap B=D_i,\quad A_i\cap A_j=\{\varnothing\}\quad(i\ne j).
\]
The last equality is at the abstract-complex level; geometrically the different filled part simplices are disjoint.

**2. Homotopy type.** The join \(B\) is path connected since \(r\ge2\). Each \(A_i\) is contractible, and each inclusion of the finite discrete space \(|D_i|\) into \(|B|\) is nullhomotopic because the target is path connected. Replacing the attachment of \(|A_i|\) along \(|D_i|\) by its homotopy pushout, a cone on \(|D_i|\), produces one additional \(\bigvee^{a_i-1} S^1\). The attachments remain disjoint away from \(B\), so the same argument applies to all \(i\) without adding extra identifications. Since a discrete space of \(a_i\) points has reduced \(0\)-homology \(\mathbb Z^{a_i-1}\), the join formula gives
\[
|B|\simeq\bigvee^{\prod_i(a_i-1)}S^{r-1},
\]
including the contractible case when any \(a_i=1\). The displayed wedge-of-spheres formula follows. This construction is integral and homotopical, not an inference from Euler characteristic.

**3. Integral modules for \(r\ge3\).** Consider the equivariant pair \((\mathcal{GP}(G),B)\). Its relative simplicial chain groups split, naturally under permutations of the parts, into the relative groups of \((A_i,D_i)\); every cross-part simplex is already in \(B\). The long exact sequence for each pair \((A_i,D_i)\), using that \(|A_i|\) is contractible, gives
\[
H_j(A_i,D_i;\mathbb Z)=\begin{cases}I_i,&j=1,\\0,&j\ne1.\end{cases}
\]
The identification is the connecting boundary map to \(\widetilde H_0(D_i;\mathbb Z)=I_i\), and hence carries the natural permutation action with **no orientation twist**. The join \(B\) is simply connected for \(r\ge3\) (or contractible when a singleton part occurs), and its only possibly nonzero reduced homology is in degree \(r-1\). The long exact sequence of the pair therefore identifies \(\widetilde H_1(\mathcal{GP}(G))\) with \(\bigoplus I_i\) and \(\widetilde H_{r-1}(\mathcal{GP}(G))\) with \(\widetilde H_{r-1}(B)\), *integrally* and equivariantly. This is valid when \(r=3\), because the two degrees are distinct.

The reduced-chain join/Künneth isomorphism (all groups free) identifies the top homology of \(B\) with the tensor product of the zero-dimensional augmentation lattices. Swapping two degree-zero reduced cycles in a simplicial join changes the orientation by \((-1)^{(0+1)(0+1)}=-1\). Thus a part permutation contributes precisely its sign, proving the complete stated module action, including all permutations of equal-sized parts.

**4. The bipartite integral module.** For \(r=2\), set \(A=A_1\sqcup A_2\) geometrically. The pair \((\mathcal{GP}(G),A)\) has only one nonzero relative chain group in positive degrees: \(C_1(\mathcal{GP}(G),A;\mathbb Z)=\mathbb Z[E]\), generated by the cross edges, and no relative chains in degree two. The connecting homomorphism to \(H_0(A;\mathbb Z)=\mathbb Z\oplus\mathbb Z\), orienting every cross edge from the first to the second shore, sends every edge generator to \((-1,1)\). The long exact sequence gives
\[
H_1(\mathcal{GP}(G);\mathbb Z)\cong\ker\!\left(\mathbb Z[E]\xrightarrow{\varepsilon}\mathbb Z\right).
\]
Under a shore exchange, the canonical orientation of every cross edge reverses, so the induced action is the *negative* of the natural permutation of \(E\). This proves the signed integral statement. For \(a_1a_2=1\) the kernel is zero, correctly giving a point.

**5. Character consequences.** A within-part automorphism \(g\) fixing each part induces the rational character
\[
\operatorname{tr}(g\mid\widetilde H_1)=\sum_{i=1}^r (f_i(g)-1),\qquad
\operatorname{tr}(g\mid\widetilde H_{r-1})=\prod_{i=1}^r (f_i(g)-1)
\]
when \(r\ge3\), where \(f_i(g)\) counts fixed vertices in part \(i\). For part permutations, the first trace sums only over setwise fixed parts, while the second is multiplied by the sign of the part permutation and combines the return-map traces around its cycles. The precise integral module formulas above—not the rational characters alone—are the assertion. For example, for \(K_{2,2,2}\) the first and second reduced homology are \(\mathbb Z^3\) and \(\mathbb Z\). The full automorphism group \( (C_2)^3\rtimes\mathfrak S_3\) acts on the latter one-dimensional lattice by the product of its three within-part flip signs and the sign of its permutation of the three parts. In particular, swapping two entire parts reverses the integral two-sphere class, a distinction invisible to the general-position counting polynomial.

## Verification
The standalone Python 3 script `gp_multipartite_check.py` constructs graph distances by breadth-first search, enumerates all general-position faces from the forbidden triple condition without assuming Rather's face classification, and calculates mod-two simplicial boundary ranks. It checks 15 multipartite size profiles, including singleton parts, bipartite exceptional cases and equal-size part permutations. It also directly evaluates the signed Lefschetz trace of 480 full graph automorphisms against the integral module prediction; every comparison passed. Exactly 641 nonempty faces were enumerated across the 15 profiles. Invoke `python3 gp_multipartite_check.py` and compare with `gp_multipartite_check.out`.

The finite checks are not proofs of integral torsion-freeness, arbitrary dimensions or all group actions; those follow from the chain-level and homotopy arguments above. The certificate uses no external libraries.

## Relationship to prior work
Anand, Chandran, Changat, Klavžar and Thomas (arXiv:1812.08460, first submitted 20 December 2018) already give a general geodesic-position characterization in terms of induced clique components and distance-constant partitions, which can be specialized to the present family. Rather (arXiv:2603.06930, first submitted 6 March 2026) explicitly proves the exact two-family face characterization of complete multipartite *general-position sets* and derives their counting polynomial. That fundamental input is credited here and **not claimed as new**; his inspected full paper does not formulate an integral homotopy type or any automorphism homology action. The survey by Chandran, Klavžar and Tuite (arXiv:2501.19385, first submitted 31 January 2025) surveys graph general-position invariants, rather than the integral homology modules established here.

A related previously published computation, *Mixed-dimensional integral homotopy of geodesic-avoidance complexes of clique bouquets*, gives a join of discrete spaces with one *central* star attached. Its first Betti rank is \(\sum_i a_i-1\), whereas the present multipartite complex attaches the **different part simplices** separately, with first Betti rank \(\sum_i(a_i-1)\); the two constructions do not have the same homotopy in general. That result does not furnish the present full-automorphism integral modules. Other known integral representations for unrelated multipartite-induced complexes concern different face predicates and do not imply this classification.

## Limitations
The family is restricted to complete multipartite graphs and their ordinary graph-geodesic general-position simplicial complexes. The face classification itself is known and is not a novelty claim. The homotopy wedge splitting is not asserted equivariantly; the automorphism result is a strict integral *homology-module* identification. No classification is given for deleted cross edges or arbitrary joins. Finite checks do not establish the infinite assertion. Closely related unindexed topological treatments or future independent priority checks may change the novelty assessment. 

## References
1. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930v1, first publicly submitted 2026-03-06, https://arxiv.org/abs/2603.06930; full inspected v3 HTML https://arxiv.org/html/2603.06930v3, Theorems 3.1 and 3.4.
2. U. Chandran S. V., S. Klavžar and J. Tuite, *The General Position Problem: A Survey*, arXiv:2501.19385v1, first publicly submitted 2025-01-31, https://arxiv.org/abs/2501.19385; full inspected v5 HTML https://arxiv.org/html/2501.19385v5.
3. B. S. Anand, U. Chandran S. V., M. Changat, S. Klavžar and E. J. Thomas, *Characterization of general position sets and its applications to cographs and bipartite graphs*, arXiv:1812.08460v1, first submitted 2018-12-20, https://arxiv.org/abs/1812.08460, Theorem 3.1.
4. *Mixed-dimensional integral homotopy of geodesic-avoidance complexes of clique bouquets*, publicly indexed mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-mixed-dimensional-integral-homotopy-of-geodesic-avoidance-comple--225b533c1864 (RESULT.md inspected).
