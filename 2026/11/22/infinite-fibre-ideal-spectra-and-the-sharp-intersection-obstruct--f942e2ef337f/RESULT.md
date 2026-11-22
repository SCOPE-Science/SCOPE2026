# Infinite-fibre ideal spectra and the sharp intersection obstruction for \(\omega\)-accumulation

## Finding

Let \(X\) be a nonempty topological space whose Kolmogorov quotient \(Q\) is finite. Write \(C_q\) for the equivalence class of points sharing exactly the same open neighbourhoods, and order the finite quotient by \(q\le r\) if every open neighbourhood of \(C_q\) includes \(C_r\). Let \(I=\{q\in Q:|C_q|\text{ is infinite}\}\), with the order induced from \(Q\). For any \(A\subseteq X\), define its infinite-accumulation set
\[
\Omega_X(A)=\{x\in X:\text{every open neighbourhood of }x\text{ meets }A\text{ infinitely}\}.
\]
Put \(J(A)=\{i\in I: |A\cap C_i|\text{ is infinite}\}\). Then the **complete operator normal form** is
\[
\boxed{\Omega_X(A)=\bigcup_{q\in\downarrow_Q J(A)} C_q,\qquad \Omega_X^2(A)=\Omega_X(A).}
\]
The distinct images ordered by set inclusion form a finite distributive lattice canonically isomorphic to the ideal lattice \(\operatorname{Id}(I)\), with exactly \(|\operatorname{Id}(I)|\) elements. The order-theoretic meet of two images need **not** be their set-theoretic intersection.

**Exact intersection-closure criterion.** The family \(\operatorname{im}(\Omega_X)\) is closed under ordinary set intersection if and only if, for each \(q\in Q\), the finite set
\[
I_{\ge q}=\{i\in I:q\le i\}
\]
is empty or has a least element. This condition is automatic for infinite classes \(q\in I\), but can fail for finite classes. A quotient with three classes \(q<a\), \(q<b\), \(a\parallel b\), with \(q\) finite and \(a,b\) infinite, is the smallest possible failure: the two images \(C_q\cup C_a\) and \(C_q\cup C_b\) intersect in \(C_q\), which is not an image.

**Optimal inverse realization.** Every nontrivial finite distributive lattice \(L\) occurs as \(\operatorname{im}(\Omega_X)\), ordered by inclusion, on a countably infinite space with a finite Kolmogorov quotient. In any realization the number of infinite indistinguishability classes is exactly \(|J(L)|\), the number of join-irreducibles of \(L\), and consequently the quotient has at least that many classes. Equality is attained; at that smallest quotient size the quotient order is uniquely determined up to isomorphism as the poset \(J(L)\). The one-element lattice is realized on a one-point finite space.

## Assumptions and scope

The topological space may be non-\(T_0\), may have arbitrarily large infinite indistinguishability classes, and has finitely many *classes*, not necessarily finitely many points. No separation, metrizability or countability assumption is made for the operator classification. The topology on finite \(Q\) is the Alexandrov topology of upward-closed subsets for the stated specialization order, because only finitely many distinct open sets exist. Here \(\downarrow_Q S=\{q\in Q:\exists s\in S\ (q\le s)\}\) and \(\operatorname{Id}(I)\) denotes downward-closed subsets of the *induced* order on \(I\). The lattice structure on the image is that of its inclusion **order**, not necessarily the setwise intersection/union algebra. Empty sets and singleton spaces are permitted; only the inverse realization statement for nontrivial lattices requires an infinite space.

## Proof

**1. Quotient neighbourhoods and the normal form.** Every open set is saturated under topological indistinguishability; conversely, the finite quotient topology is upper Alexandrov. Hence the least open neighbourhood of a point in \(C_q\) is \(N_q=\bigcup_{r\ge q}C_r\). By the defining property of \(\Omega_X\), that point belongs to \(\Omega_X(A)\) exactly when \(|N_q\cap A|\) is infinite. Since \(Q\) is finite, a finite union \(\bigcup_{r\ge q}(A\cap C_r)\) is infinite exactly when one summand is infinite. Such a summand has \(r\in I\) and \(r\in J(A)\); thus \(q\in\downarrow_Q J(A)\), proving the boxed operator identity for every \(A\subseteq X\).

**2. Image spectrum and idempotence.** Every subset \(J\subseteq I\) is realizable as \(J(A)\): choose an infinite subset of each \(C_j\) with \(j\in J\), and no points in other classes (choosing whole classes works). Put \(K=\downarrow_I J\). Then \(\downarrow_Q J=\downarrow_Q K\). Conversely, for any ideal \(K\in\operatorname{Id}(I)\), choose \(A=\bigcup_{k\in K}C_k\). The corresponding image is \(F(K)=\bigcup_{q\in\downarrow_Q K}C_q\). Since \(F(K)\cap \bigcup_{i\in I}C_i=\bigcup_{i\in K}C_i\), the map \(K\mapsto F(K)\) is injective and preserves and reflects inclusion. Therefore the image poset is isomorphic to \(\operatorname{Id}(I)\) and has exactly its ideal count. For any \(A\), we have \(J(\Omega_X(A))=\downarrow_I J(A)\), and a second normal-form application yields \(\Omega_X^2(A)=F(\downarrow_I J(A))=F(J(A))=\Omega_X(A)\). No infinite iteration claim is inferred from a finite sample.

**3. Pointwise intersection boundary.** Let \(K,L\subseteq I\) be ideals. Their image sets obey \(F(K)\cap F(L)\supseteq F(K\cap L)\). Equality for all ideals holds precisely when every \(q\in Q\) with \(I_{\ge q}\ne\varnothing\) has a least element. Indeed, if it has a least element \(i_q\), then \(q\in F(K)\) is equivalent to \(i_q\in K\): if some \(j\in K\cap I_{\ge q}\) exists, \(i_q\le j\) and downward closure puts \(i_q\) in \(K\). This yields the equivalence for intersections. Conversely, if \(I_{\ge q}\) has no least element, finiteness gives two members \(a,b\) without a common lower bound inside \(I_{\ge q}\) (otherwise pairwise downward directedness would yield a least member by finite induction). Take ideals \(K=\downarrow_I a\) and \(L=\downarrow_I b\). The point \(q\) is in \(F(K)\cap F(L)\), but not in \(F(K\cap L)\). Any image equal to the intersection would have intersection with the infinite classes \(I\) exactly \(K\cap L\), forcing it to be \(F(K\cap L)\), a contradiction. The stated three-class fork realizes this obstruction. For \(|Q|\le2\), a nonempty set \(I_{\ge q}\) cannot contain two incomparable minimal members, so the obstruction needs at least three quotient classes.

**4. Optimal representation and rigidity.** By the finite Birkhoff representation theorem, each nontrivial finite distributive lattice \(L\) is order-isomorphic to \(\operatorname{Id}(J(L))\), where \(J(L)\) is its poset of nonzero join-irreducibles. Take \(Q=J(L)\) with the upper-set topology, and replace every \(q\in Q\) by a disjoint countably infinite indistinguishability class, with open sets exactly the unions indexed by upper sets of \(Q\). This gives a countably infinite space, \(I=Q\), and Step 2 identifies its \(\Omega\)-image order with \(L\). For any other realizing space, Step 2 gives \(L\cong\operatorname{Id}(I)\); join-irreducibles of an ideal lattice are precisely the principal ideals of elements of \(I\). Thus \(I\cong J(L)\) and its cardinality is forced. As \(I\subseteq Q\), the smallest quotient has exactly \(|J(L)|\) classes; equality forces \(Q=I\) and therefore fixes its order isomorphism type. The trivial lattice is realized by a finite singleton and has no infinite classes.

## Verification

`python3 verify.py` enumerates all finite labelled partial orders on one through four points and every choice of infinite-class subset. For all 3,670 combinations, it checks the order-ideal/image bijection, the idempotence identity, and the necessity and sufficiency of the intersection-closure criterion. It also verifies the explicit three-class counterexample. The output is `VERIFY_OK cases=3670 non_intersection_closed=229`. This program works with symbolic infinite-class flags: the unbounded cardinality step is proved in Step 1, not by finite approximation. The finite Birkhoff theorem is used as stated, not computationally re-established.

## Relationship to prior work

Montacute's *Halo Semantics for Modal Logic* [1] identifies the purely nonstandard modality with infinite accumulation, proves its general closure and transitivity properties, and studies modal completeness. These results are premises here, not claimed as new. Published work [2] builds a different countable \(T_0\) Alexandrov realization of transitive Kripke frames with restrictions on valuations; it does not classify images for spaces with **finite indistinguishability quotient and arbitrary subsets** or the intersection-closure boundary. Related studies [3] classify idempotence and transfinite ranks for prefix trees, where the quotient is generally infinite, and [4] compute derivative tails on ordinal Alexandrov chains. Neither entails the present finite-quotient image classification, intersection criterion, or optimal distributive-lattice realization. Birkhoff's representation theorem is classical and explicitly credited; the new content is the exact identification of the halo operator's image, the extra intersection obstruction, and its optimal inverse finite-quotient realization.

## Limitations

This result applies only to spaces with finite Kolmogorov quotient. In particular, an infinite \(T_0\) Alexandrov space can have different derivative behavior and may not satisfy \(\Omega^2=\Omega\). The image is distributive only as an ordered family, not always as a sublattice of the power-set lattice with the inherited meet. Although the quotient order of a minimum-sized inverse realization is unique, the cardinalities of its infinite fibres need not be. The result does not compute the number of inequivalent formulas for arbitrary valuations or claim any new proof of finite Birkhoff representation. Older equivalent operator-image descriptions not identified in the searched literature remain possible.

## References

[1] Yoàv Montacute, *Halo Semantics for Modal Logic*, EPTCS 447 (2026), 623–635; first public arXiv version 2026-06-30, https://arxiv.org/abs/2606.31885, DOI:10.4204/EPTCS.447.35.

[2] *Countable Alexandrov fibre realization of transitive modalities by \(\omega\)-accumulation*, published research result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-countable-alexandrov-fibre-realization-of-transitive-modalities--4f79ea6818be/RESULT.md.

[3] *A sharp branching criterion and every countable stabilization rank for omega accumulation on prefix trees*, published research result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-sharp-branching-criterion-and-every-countable-stabilization-ra--a8c31bfdd467/RESULT.md.

[4] *Ordinal-block normal form for the infinite-accumulation modality on Alexandrov chains*, published research result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-ordinal-block-normal-form-for-the-infinite-accumulation-modality--5e33e921fd1b/RESULT.md.

[5] G. Birkhoff, classical finite distributive lattice representation theorem, \(L\cong\operatorname{Id}(J(L))\).
