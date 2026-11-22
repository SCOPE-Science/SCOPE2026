# Integral homology lattices of clique-expanded double stars

## Finding
Fix integers \(p,q\ge 2\). Let \(T\) be the double-star tree with adjacent hubs \(u,v\), with \(p\) leaves \(U\) adjacent to \(u\) and \(q\) leaves \(V\) adjacent to \(v\). For every base vertex \(x\in V(T)\), take a labeled finite set \(F_x\), with cardinality \(k_x\ge2\). Form a graph \(G\) by replacing each vertex \(x\) by a complete graph on \(F_x\), and joining all vertices of \(F_x\) to all vertices of \(F_y\) precisely when \(xy\) is a tree edge. Let \(X=\operatorname{Ind}(G)\), the ordinary simplicial independence complex.

Define \(P=\prod_{x\in U}(k_x-1)\), \(Q=\prod_{y\in V}(k_y-1)\), and \(I_x=\ker(\mathbb Z[F_x]\xrightarrow{\mathrm{sum}}\mathbb Z)\). For a leaf set \(S\), write \(T_S=\bigotimes_{x\in S}I_x\), with tensor permutations acting by the graded join sign: swapping two leaf factors incurs a minus sign.

**Homotopy classification:**
\[
X\simeq\Big(\bigvee^{PQ}S^{p+q-1}\Big)\vee
\Big(\bigvee^{k_vP}S^p\Big)\vee
\Big(\bigvee^{k_uQ}S^q\Big).
\]
If \(p=q\), the two degree-\(p\) wedges combine; the displayed equivalence is nonequivariant. All reduced integral homology is free.

**Full natural integral homology action:** Let \(\Gamma\) be the group of permutations of the colored vertices that carry each fiber bijectively to another fiber and induce an automorphism of the decorated base tree. Its action is naturally, integrally and simultaneously identified by
\[
\widetilde H_{p+q-1}(X;\mathbb Z)\cong T_U\otimes T_V,
\]
\[
\widetilde H_d(X;\mathbb Z)\cong
\mathbf 1_{d=p}\big(T_U\otimes\mathbb Z[F_v]\big)
\oplus
\mathbf 1_{d=q}\big(T_V\otimes\mathbb Z[F_u]\big),\qquad d\in\{p,q\},
\]
with zero reduced homology otherwise. Here the indicator indicates omission of a direct summand when the indicated equality fails. Fiber permutations act on each augmentation factor and on the indicated *whole permutation lattice* \(\mathbb Z[F_u]\) or \(\mathbb Z[F_v]\). Base-leaf permutations carry the usual sign on alternating join orientations. When the two sides can be exchanged, the degree-\(p\) and degree-\(q\) summands interchange; the top-degree action interchanges the two tensor blocks with sign \((-1)^{pq}\). These descriptions include arbitrary cardinality-preserving permutations of unequal leaf fibers, not just the uniform lexicographic product.

In particular, the sequence \(0\to I_u\to\mathbb Z[F_u]\to\mathbb Z\to0\) in the degree-\(q\) module does **not** split as an integral \(\mathfrak S_{k_u}\)-module when \(k_u\ge2\), even though it splits over \(\mathbb Q\). The same holds with \(u,v\) interchanged. Further, the quotient \(|X|/\Gamma\) is rationally acyclic: its reduced rational homology vanishes in every degree.

## Assumptions and scope
The base graph is precisely a double star, with \(p,q\ge2\) and each \(k_x\ge2\); no assumption of equal fiber sizes is made. A fiber is a clique, not an independent twin class, and adjacent base vertices induce complete bipartite links between their fibers. The group \(\Gamma\) is the natural fiber-preserving symmetry group, not an asserted classification of all abstract graph automorphisms. All spaces are finite geometric realizations, and all integral homology is reduced except where indicated. The formula is not asserted for a hub with zero or one leaf, for nonclique fibers, or for arbitrary forests.

## Proof
**1. An exact three-piece cover.** Regard every \(F_x\) as a discrete zero-dimensional simplicial complex. Set
\[
A_U=\mathop{*}_{x\in U}F_x,\qquad A_V=\mathop{*}_{y\in V}F_y,\qquad A=A_U*A_V,
\]
\[
B=F_u*A_V,\qquad C=F_v*A_U.
\]
Every independent set either uses only leaf fibers, contains one vertex in the hub fiber \(F_u\) and then may use only leaf fibers on the opposite side \(V\), or contains one vertex in \(F_v\) and then may use only leaves \(U\). Consequently \(X=A\cup B\cup C\), with \(A\cap B=A_V\), \(A\cap C=A_U\), and \(B\cap C\) having empty realization. In particular \(C\cap(A\cup B)=A_U\).

**2. Homotopy splitting.** The map \(A_V\hookrightarrow A\) is nullhomotopic because it lies in the cone obtained by adjoining any vertex of a fiber on side \(U\). It is also nullhomotopic in \(B\), using any hub-color vertex in \(F_u\). The cofibration pushout for two nullhomotopic inclusions gives \(A\cup B\simeq A\vee B\vee\Sigma A_V\). Next \(A_U\hookrightarrow A\cup B\) is nullhomotopic because its map into \(A\) is coned off by a vertex on side \(V\). Attaching \(C\) similarly yields
\[
X\simeq A\vee B\vee C\vee\Sigma A_V\vee\Sigma A_U.
\]
All the intersections involved are connected since \(p,q\ge2\), so no disconnected-basepoint correction is required. Each \(F_x\) has \(\widetilde H_0(F_x;\mathbb Z)=I_x\) and is a wedge of \(k_x-1\) zero-spheres. The integral join Künneth formula yields \(A_U\simeq\bigvee^{P}S^{p-1}\), \(A_V\simeq\bigvee^{Q}S^{q-1}\), and \(A\simeq\bigvee^{PQ}S^{p+q-1}\). Likewise \(B\simeq\bigvee^{(k_u-1)Q}S^q\) and \(C\simeq\bigvee^{(k_v-1)P}S^p\), proving the wedge formula.

**3. The integral group modules, without an equivariant wedge assumption.** The subcomplex \(A\) is \(\Gamma\)-invariant, and \(A\) has reduced homology only in degree \(p+q-1\). Since \(p+q-1>\max(p,q)\), the long exact sequence of \((X,A)\) canonically identifies \(\widetilde H_{p+q-1}(X)\) with \(\widetilde H_{p+q-1}(A)=T_U\otimes T_V\), and identifies each lower-degree homology group with the corresponding relative group of \((X,A)\).

In the relative simplicial chain complex, the two hub pieces are disjoint after the leaf-only subcomplex is quotiented. Thus \(C_*(X,A)\cong C_*(B,A_V)\oplus C_*(C,A_U)\). Orient each relative simplex as \([c,z_1,\ldots,z_s]\), with its hub-color vertex \(c\) first. Deleting \(c\) lands in the factored-out leaf subcomplex; the other faces give the augmented leaf boundary. Therefore
\[
H_d(B,A_V;\mathbb Z)\cong
\begin{cases}T_V\otimes\mathbb Z[F_u],&d=q,\\0,&d\ne q,\end{cases}
\]
and symmetrically \(H_d(C,A_U)\cong T_U\otimes\mathbb Z[F_v]\) for \(d=p\), with zero groups otherwise. These are canonical integral \(\Gamma\)-module descriptions; the ordering convention for relative simplices makes hub exchange interchange the relative summands without a hidden suspension sign. The orientation of the top join gives \((-1)^{pq}\) on interchange of the two leaf blocks, while any leaf transposition contributes a negative sign to the corresponding tensor permutation. No claim of an equivariant homotopy splitting is needed.

**4. The non-splitting and quotient consequences.** The \(\mathfrak S_{k_u}\)-invariants of \(\mathbb Z[F_u]\) consist of multiples of \(\sum_{c\in F_u}c\), whose augmentations are multiples of \(k_u\). Hence there is no equivariant integral section of the augmentation to \(\mathbb Z\); rational averaging does furnish one. Each nonzero homology summand contains at least one leaf augmentation factor \(I_x\), on which the independent full color-permutation group \(\mathfrak S_{k_x}\) has no rational invariants. Thus \(\widetilde H_*(X;\mathbb Q)^\Gamma=0\). Finite-group transfer after barycentric subdivision identifies this invariant space with \(\widetilde H_*(|X|/\Gamma;\mathbb Q)\), proving rational acyclicity.

## Verification
Two self-contained standard-library Python scripts are included. `check_double_star.py` reconstructs every independent face and augmented simplicial boundary for seven uniform-fiber examples: \((p,q,k)=(2,2,2),(2,2,3),(2,3,2),(3,2,2),(3,3,2),(2,4,2),(2,3,3)\). It computes exact finite-field boundary ranks modulo \(2\) and \(101\) and checks the predicted reduced Betti numbers. It also checks signed reduced Lefschetz numbers of hub-color transpositions, leaf-color transpositions, leaf-position exchanges, and balanced hub exchanges on five examples. `check_weighted.py` independently enumerates three unequal-fiber cases and tests their Betti numbers over the same two fields. Run `python3 check_double_star.py` and `python3 check_weighted.py` from a directory containing both scripts; the captured execution output is embedded as `CHECKS.txt`. The proof above, not those finite computations, establishes the statements for all allowed parameters over \(\mathbb Z\).

## Relationship to prior work
Okura's 2021 work proves the wedge-of-spheres phenomenon for lexicographic products over non-star forests and explicitly calculates the path-base case; it also gives a leaf-reduction decomposition. Okura's 2023 polyhedral-join theorem supplies a broad nonequivariant wedge theorem and a second path-family formula. These results subsume the *qualitative* wedge property and are not represented as new. Neither inspected theorem gives the weighted double-star degree multiplicities or identifies the **unsplit integral natural permutation lattices** together with the hub-switch sign. Vander Meulen and Van Tuyl's earlier lexicographic-product paper addresses shellability and vertex decomposition, not these equivariant homology groups. Related indexed results for higher-independence or multipath complexes of double stars concern different simplicial functors; indexed cyclic clique expansions use a cycle base, not this tree. The claim is specifically the explicit all-weights homotopy ranks and, decisively, the integral \(\Gamma\)-module identification.

## Limitations
An unindexed equivalent equivariant calculation could exist; exhaustive bibliographic uniqueness is not asserted. The natural nonequivariant decomposition is largely accessible from previously published splitting tools; the distinguishing information is the integer symmetry-lattice identification. Finite modular verifications do not certify integral torsion or infinite-size assertions independently of the proof. The rational quotient calculation does not claim integrally acyclic or contractible orbit spaces. Only fiber-preserving symmetries are classified, and no generalization to arbitrary forest bases is claimed.

## References
1. K. Okura, *Independence Complex of the Lexicographic Product of a Forest*, first posted 2021-09-09, arXiv:2109.04181, https://arxiv.org/abs/2109.04181 (especially Theorem 1.2, Theorem 3.1, Section 4).
2. K. Okura, *On the Homotopy Type of the Polyhedral Join over the Independence Complex of a Forest*, first posted 2023-03-21, arXiv:2303.11984, https://arxiv.org/abs/2303.11984 (Theorems 1.1--1.4 and Section 5).
3. K. N. Vander Meulen and A. Van Tuyl, *Shellability, vertex decomposability, and lexicographical products of graphs*, first posted 2015-05-12, arXiv:1505.02838, https://arxiv.org/abs/1505.02838 (Theorem 1.1 and Section 2).
