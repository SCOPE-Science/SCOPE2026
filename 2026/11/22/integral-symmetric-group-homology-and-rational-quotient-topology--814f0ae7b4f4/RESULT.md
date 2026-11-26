# Integral symmetric-group homology and rational quotient topology of partial-partition complexes

## Finding

For integers \(n\ge2\) and \(j\ge1\), define \(D_n\) to be the simplicial complex with vertices the nonempty subsets of \([n]=\{1,\ldots,n\}\), whose simplices are families of mutually disjoint subsets. The natural label-permutation action of \(S_n\) acts simplicially. Write \(m_r(\lambda)\) for the number of parts of size \(r\) of an integer partition \(\lambda\vdash n\). Put

\[
H_\lambda=\prod_{r\ge2}(S_r\wr S_{m_r(\lambda)})\subseteq S_n,
\qquad
\varepsilon_\lambda=\bigotimes_{r\ge2}\operatorname{sgn}_{S_{m_r(\lambda)}}.
\]

Here the factors \(S_r^{m_r}\) inside each wreath product act trivially on the rank-one lattice \(\mathbb Z_{\varepsilon_\lambda}\), and \(S_{m_r}\) acts by sign. There is an integral isomorphism of \(S_n\)-modules

\[
\boxed{\widetilde H_{j-1}(D_n;\mathbb Z)
\cong
\bigoplus_{\substack{\lambda\vdash n\\\ell(\lambda)=j,\ \min(\lambda)\ge2}}
\operatorname{Ind}_{H_\lambda}^{S_n}\mathbb Z_{\varepsilon_\lambda}.}
\]

Consequently the quotient by all label permutations has complete reduced **rational** Betti numbers

\[
\boxed{\dim_{\mathbb Q}\widetilde H_{j-1}(|D_n|/S_n;\mathbb Q)
=\#\{\lambda\vdash n:\ell(\lambda)=j,\ \lambda_1>\cdots>\lambda_j\ge2\}.}
\]

The bivariate generating function, with \(t\) recording ground-set size and \(u\) recording homological degree plus one, is

\[
\sum_{n\ge2}\sum_{j\ge1}
\dim_{\mathbb Q}\widetilde H_{j-1}(|D_n|/S_n;\mathbb Q)\,t^n u^j
=\prod_{r\ge2}(1+ut^r)-1.
\]

In particular the quotient has nonzero rational reduced homology in degree \(j-1\) precisely for \(n\ge j(j+3)/2\). The first quotient class in degree two occurs at \(n=9\), from distinct block sizes \(2,3,4\).

## Assumptions and scope

All complexes are finite; homology is reduced integral homology unless \(\mathbb Q\) is explicitly specified. Empty and singleton ground sets are excluded to avoid augmented-degree conventions. \(S_n\) acts by permuting labels, not by arbitrarily permuting vertices of the complex. The induced-module formula includes every homological degree; terms indexed by an empty set of integer partitions are zero. The quotient statement concerns rational homology of the underlying geometric orbit space, not integral quotient homology and not its homotopy type.

## Proof

**1. The exposed-facet coordinate map.** Let \(\mathcal P_{n,j}\) be the set of set partitions \(F=\{B_1,\ldots,B_j\}\) of the entire ground set, with \(|B_i|\ge2\) for every block. Each \(F\) is a maximal \((j-1)\)-simplex of \(D_n\): its blocks already exhaust \([n]\), so there is no nonempty vertex disjoint from all blocks. Choose an orientation of each such facet. For a \((j-1)\)-cycle \(z\), take its signed coefficients on these facets. This gives an integral homomorphism

\[
\Phi_j:\widetilde H_{j-1}(D_n;\mathbb Z)\longrightarrow
\bigoplus_{F\in\mathcal P_{n,j}}\mathbb Z[F].
\]

Because no selected facet has a coface, none can occur in a boundary of a \(j\)-chain; hence the coefficients depend only on the homology class.

**2. Primitive cycles and bijectivity.** For each \(F\), choose \(b_i\in B_i\). Denote the oriented zero-simplex at vertex \(B\) by \([B]\), and form the reduced chain

\[
z_F=([B_1]-[\{b_1\}])*\cdots*([B_j]-[\{b_j\}]),
\]

where \(*\) is the oriented simplicial join product. The two vertices in each factor intersect, while vertices in different factors are disjoint. Thus they form a simplicial cross-polytope boundary; each zero-chain has zero augmentation, so \(\partial z_F=0\). Exactly one simplex in \(z_F\) is a full, no-singleton partition: the facet \(F\) itself, appearing with signed coefficient one. Orient \(F\) accordingly. Then \(\Phi_j([z_F])=[F]\).

Gottstein's nonpure shelling theorem for this same containment-order complex proves that \(\widetilde H_{j-1}(D_n;\mathbb Z)\) is free abelian of rank \(|\mathcal P_{n,j}|\) [1, Theorem 5.2]; his cross-polytope basis uses specified choices of representatives [1, Theorem 5.3]. The freeness and rank statement is the only nonequivariant input needed here. The preceding unit-coordinate construction makes \(\Phi_j\) surjective, so it is an integral isomorphism.

**3. Equivariance and the stabilizer sign.** The coefficient map is natural under relabelling, provided the target basis is treated as **oriented**, not unsigned, facets. A permutation fixing a set partition \(F\) permutes blocks of each repeated size \(r\); its action on the orientation line of \(F\) is exactly the sign of that block permutation. Permutations of elements *within* a block have sign \(+1\), because they fix the vertex representing that whole block. Blocks of unequal sizes cannot be permuted by a stabilizer. Hence the stabilizer character is \(\varepsilon_\lambda\), and the signed oriented-facet module on each orbit of block-size type \(\lambda\) is the indicated integral induced lattice. Summing over all orbits proves the first displayed formula. Equivalently, the character at \(\sigma\in S_n\) is the signed count of \(\sigma\)-fixed no-singleton set partitions with \(j\) blocks.

**4. Quotients and strict partitions.** Barycentrically subdivide the finite complex, making the group action admissible. Its rational quotient chain complex identifies with rational coinvariants, which equal invariants by averaging; averaging is exact in characteristic zero. Hence

\[
\widetilde H_{j-1}(|D_n|/S_n;\mathbb Q)
\cong\bigl(\widetilde H_{j-1}(D_n;\mathbb Q)\bigr)^{S_n}.
\]

By Frobenius reciprocity, an induced summand contributes one invariant line exactly when its stabilizer sign character is trivial. This holds precisely when no block size repeats, namely \(m_r(\lambda)\le1\) for every \(r\). Distinct-part integer partitions are counted by the displayed product. The least sum of \(j\) distinct integers at least two is \(2+3+\cdots+(j+1)=j(j+3)/2\). Every larger sum is possible by increasing the largest part. This proves the sharp threshold.

## Verification

The accompanying standard-library program `verify.py` independently enumerates all faces and complete non-singleton partitions for \(2\le n\le7\). It checks all displayed cross-polytope boundaries and their integral unit facet coordinates. For every conjugacy-cycle type of each \(S_n\), it compares the exact augmented-chain Lefschetz trace (computed from **all** simplices and orientation signs) with the trace predicted by the signed non-singleton-facet module. It separately checks the strict-partition quotient counts. There are 52 faces for \(n=4\) and 4,140 for \(n=7\). Every finite check passes; the unbounded theorem follows from the proof, **not** from this finite experiment.

For instance, \(\widetilde H_1(D_4;\mathbb Z)\) is the rank-three signed oriented-facet lattice on the three partitions of type \((2,2)\). Its rationalization is the standard \(S_4\)-representation, with traces \(1,-1,-1\) on a transposition, double transposition and four-cycle, respectively. It is not the standard integral root lattice \(\{x\in\mathbb Z^4:\sum_i x_i=0\}\): the signed facet lattice has coinvariants \(\mathbb Z/2\mathbb Z\), since the facets form a single orbit with an orientation-reversing stabilizer, while the root lattice has zero coinvariants, since all \(e_i-e_j\) with \(i\ne j\) represent one class and \((e_1-e_2)+(e_2-e_3)=e_1-e_3\). These coinvariants need not equal integral homology of the orbit space. The quotient has zero degree-one rational homology in this case, despite the original rank three.

## Relationship to prior work

Gottstein [1] defines the containment-order partial-partition complex, establishes a nonpure shelling, computes all ordinary Betti numbers, constructs a non-equivariant cross-polytope homology basis, and proves that the full simplicial automorphism group is \(S_n\). Those results are **used**, not claimed anew here. The present claim adds the full integral \(S_n\)-module in every degree, with its stabilizer signs, and the resulting exact rational orbit-space Betti series and sharp cutoff. The signs are essential: an unsigned permutation module would falsely predict an invariant for each non-singleton block-size type.

Piterman and Welker [2] study refinement-ordered decomposition posets in a more general monoidal setting; these are not by definition the containment-order complex used here. A related published study of **geometric fixed-point spaces** of partial-partition complexes [3] concerns fixed loci of subgroup actions, rather than the geometric quotient or its oriented homology module. Neither inspected statement supplies the displayed induced integral module or the strict-partition quotient series. Related unindexed results, alternative chain models or later revisions may still exist.

## Limitations

This is a homology representation and rational quotient-homology calculation; it does not determine the quotient's integral torsion, ring structure, homotopy type or equivariant embedding dimension. The proof uses the previously established nonequivariant homology theorem [1]. The bibliographic comparison is bounded by the accessible primary text and published record summaries, and is not a proof of priority.

## References

[1] M. J. Gottstein, *The Partial Partition Complex*, arXiv:2311.11190v2, https://arxiv.org/abs/2311.11190v2. Sections 4, 5 and 7 (especially Theorems 5.2, 5.3, 7.1).

[2] K. I. Piterman and V. Welker, *Posets arising from decompositions of objects in a monoidal category*, arXiv:2401.09280, https://arxiv.org/abs/2401.09280, subsequently published in Forum of Mathematics, Sigma.

[3] *Fixed spaces of partial-partition complexes under transitive and Young symmetries*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-fixed-spaces-of-partial-partition-complexes-under-transitive-and--cedead413a18.
