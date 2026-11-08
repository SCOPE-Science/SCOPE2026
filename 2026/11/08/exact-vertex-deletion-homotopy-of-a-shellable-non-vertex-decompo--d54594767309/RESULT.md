# Exact vertex-deletion homotopy of a shellable non-vertex-decomposable circulant

## Finding

Let \(G=C_{16}(1,4,8)\), and let \(K=\operatorname{Ind}(G)\). For **every** vertex \(v\) of \(G\), its simplicial deletion \(D_v=\operatorname{del}_K(v)=\operatorname{Ind}(G-v)\) satisfies

\[
D_v\simeq S^2.
\]

More precisely, the inclusion of the link \(L_v=\operatorname{lk}_K(v)\) into the deletion induces a **primitive surjection**

\[
H_2(L_v;\mathbb Z)\cong\mathbb Z^2\ \longrightarrow\ H_2(D_v;\mathbb Z)\cong\mathbb Z,
\]

whose kernel is a rank-one direct summand. This is the local homotopy behavior of the familiar shellable-but-not-vertex-decomposable well-covered circulant. The previously proved shellability of \(K\) is not claimed as new.

## Assumptions and scope

Vertices are the residues \(\mathbb Z/16\mathbb Z\). An unordered pair of **distinct** vertices is an edge of \(G\) precisely when its difference modulo \(16\) belongs to \(\{1,4,8,12,15\}\). For any finite simple graph \(T\), the independence complex \(\operatorname{Ind}(T)\) has all edge-free vertex subsets as faces, including the empty face. For a vertex \(v\), deletion means faces not containing \(v\); link means sets disjoint from \(v\) whose union with \(v\) is a face. All homotopy equivalences and homology groups have their ordinary topological and **integral** meanings. The quantifier is every one of the sixteen vertices, by cyclic rotation.

## Proof

**1. Exhaustive finite complexes.** Enumerate all \(2^{16}\) subsets in the above cyclic graph. A separate inductive inclusion/exclusion construction gives the same independent-set family. The full complex has face vector, in dimensions \(-1,0,1,2,3\),

\[
(1,16,80,144,80).
\]

At vertex \(0\), the deletion \(D\) has \((1,15,70,117,60)\) and its link \(L\) has \((1,10,27,20,0)\). The link enumeration also agrees with \(\operatorname{Ind}(G-N[0])\).

**2. Acyclic matching for the deletion.** The standalone verifier constructs a combinatorial matching by repeatedly choosing a vertex that has the largest number of available toggle pairs (ties broken by the largest vertex label), deleting all such pairs, and repeating until none remain. It converts the empty-face pair into one ordinary critical zero-cell, reverses all matched nonempty face-cover relations and confirms acyclicity by complete directed-Hasse topological sorting on all \(731\) covering relations. The resulting ordinary discrete-Morse CW complex has **one zero-cell, two two-cells and one three-cell**, and no other cells. In the deterministic orientation inherited from increasing vertex labels, its entire signed boundary from dimension three to two is

\[
\partial_3=\begin{pmatrix}-1\\0\end{pmatrix}.
\]

Because there are no one-cells, the two-skeleton is \(S^2\vee S^2\). The attaching map of the three-cell has a primitive homotopy class \((-1,0)\in\pi_2(S^2\vee S^2)\cong\mathbb Z^2\), where the isomorphism is Hurewicz. Up to a homotopy equivalence of the wedge, this is a degree-one attachment to one sphere, leaving exactly \(S^2\). Forman's theorem transfers this homotopy type to \(D\).

**3. The link and inclusion.** The same exact procedure on \(L\), with all \(114\) nonempty covering relations checked for acyclicity, leaves one zero-cell, one one-cell, and three two-cells. Its complete integral Morse boundary is

\[
\partial_2=\begin{pmatrix}1&0&1\end{pmatrix}.
\]

The degree-one attaching map kills the only one-dimensional loop and the remaining two independent two-cells yield \(L\simeq S^2\vee S^2\). By the existing shelling of \(K\) in [2], its reduced homology is concentrated in degree three. The above face vector has reduced Euler characteristic \(-1\), so the standard homotopy consequence of pure shellability is \(K\simeq S^3\). Since \(K=D\cup(v*L)\) and \(D\cap(v*L)=L\), the integral Mayer–Vietoris long exact sequence includes

\[
0\longrightarrow H_3(K;\mathbb Z)\cong\mathbb Z
\longrightarrow H_2(L;\mathbb Z)\cong\mathbb Z^2
\longrightarrow H_2(D;\mathbb Z)\cong\mathbb Z
\longrightarrow H_2(K;\mathbb Z)=0.
\]

Consequently, the link-to-deletion map is surjective with primitive rank-one kernel. Rotations \(i\mapsto i+v\) induce simplicial isomorphisms between every vertex's deletion and link, establishing the result uniformly.

## Verification

Run the self-contained \`verify_c16_deletion.py\` with Python 3; its standard output is supplied as \`verification_output.txt\`. Exact tests cover all \(2^{16}\) vertex masks, two independent face-enumeration constructions, all directed covering relations, integer signed gradient projections for both Morse boundaries, mod-two simplicial boundary ranks \((14,56,60)\) in degrees \((1,2,3)\) for the deletion and \((9,18,0)\) for the link, and all sixteen cyclic shifts. The deleting and linking matching pair counts are respectively \(129\) and \(26\). The complete computation ends with \`ALL_CHECKS_PASS\`. The integral conclusions rely on the signed matrices, **not** on the mod-two check.

## Relationship to prior work

Adam Van Tuyl publicly introduced the particular shellable/non-vertex-decomposable circulant on September 11, 2014 [1]. Earl, Vander Meulen and Van Tuyl [2, Theorem 6.1(iii)] proved shellability, lack of vertex decomposability, and the deletion's face and \(h\)-vectors; the latter is \((1,11,31,18,-1)\). This already proves the failure of Cohen–Macaulayness of every vertex deletion, but it does **not** determine its integral homotopy type or the link-to-deletion map. The authors' lexicographic-product extension [3] addresses an infinite family of shellable/non-vertex-decomposable graphs, without supplying this local integral homotopy computation. The full-complex \(S^3\) observation is already implied by [2] and is not counted as novel here. The local \(S^2\) classification and primitive inclusion identify the actual surviving homology class behind the published obstruction rather than repackaging the known \(h\)-vector. No general statement about other circulants is asserted.

## Limitations

The result is for the named sixteen-vertex circulant and its individual vertex deletions only. It does not prove the proposed classification for any lexicographic product or larger circulant, nor does it determine an explicit coordinate basis for the primitive kernel. A complete search cannot exclude equivalent unpublished or unindexed homotopy calculations. The verification is computational and subject to ordinary implementation review; independent mathematical audit has not been performed.

## References

[1] A. Van Tuyl, *Flag complexes that are shellable but not vertex decomposable*, MathOverflow question 180666, posted September 11, 2014, https://mathoverflow.net/questions/180666.

[2] J. Earl, K. N. Vander Meulen, A. Van Tuyl, *Independence complexes of well-covered circulant graphs*, arXiv:1505.02837v1 (May 11, 2015), especially Theorem 6.1, https://arxiv.org/abs/1505.02837.

[3] K. N. Vander Meulen, A. Van Tuyl, *Shellability, vertex decomposability, and lexicographical products of graphs*, arXiv:1505.02838v1 (May 12, 2015), https://arxiv.org/abs/1505.02838.
