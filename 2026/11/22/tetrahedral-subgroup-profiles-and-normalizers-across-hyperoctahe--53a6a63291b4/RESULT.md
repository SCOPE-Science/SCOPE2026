# Tetrahedral subgroup profiles and normalizers across hyperoctahedral groups

## Finding
For every integer \(n\ge 0\), let \(B_n=C_2\wr S_n\), the group of signed permutations on \(n\) coordinates, with \(B_0\) trivial. Every subgroup \(H\le B_n\) isomorphic to \(A_4\) is uniquely described up to \(B_n\)-conjugacy by a **faithful seven-type profile** \(\boldsymbol m=(m_0,\ldots,m_6)\in\mathbb N^7\) of size \(\sum_i d_i m_i=n\), where
\[
(d_0,\ldots,d_6)=(1,3,3,4,6,6,12),\qquad (c_0,\ldots,c_6)=(2,6,2,2,4,4,24)
\]
and faithfulness means \(m_2+m_3+m_4+m_5+m_6>0\). For a subgroup of profile \(\boldsymbol m\), its **exact normalizer order** is
\[
|N_{B_n}(H)|=24\prod_{i=0}^{6}c_i^{m_i}m_i!.
\]
Writing \(C_n\) for the number of conjugacy classes of these subgroups and \(E_n\) for the total number of embedded subgroups, one obtains
\[
\sum_{n\ge0}C_nz^n=\frac{1}{(1-z)(1-z^3)^2(1-z^4)(1-z^6)^2(1-z^{12})}-\frac{1}{(1-z)(1-z^3)},
\]
\[
\sum_{n\ge0}\frac{E_n}{2^nn!}z^n=\frac1{24}\left[\exp\left(\frac z2+\frac{2z^3}3+\frac{z^4}2+\frac{z^6}2+\frac{z^{12}}{24}\right)-\exp\left(\frac z2+\frac{z^3}6\right)\right].
\]
The sequence \(C_n\) is a quasipolynomial of *least period exactly twelve* and degree six, with
\[
C_n=\frac{n^6}{15552\cdot 6!}+O(n^5).
\]
Its initial terms for \(n=0,1,\ldots,15\) are \(0,0,0,1,2,2,6,8,9,16,21,23,38,46,51,74\); the corresponding total embedded counts for \(n=0,\ldots,9\) are \(0,0,0,1,12,50,1500,18795,164136,3878532\).

## Assumptions and scope
Work with ordinary finite groups, no choice of coefficient field. Identify \(B_n\) with the permutation group of signed symbols \(\{\pm1,\ldots,\pm n\}\) commuting with central sign-reversal, or equivalently with \(n\times n\) signed permutation matrices. A subgroup of type \(A_4\) means an *embedded* subgroup isomorphic to the alternating group on four letters, not merely an abstract quotient or a chosen embedding map. Two embeddings related by precomposition with \(\operatorname{Aut}(A_4)\) have the same image; this is explicitly accounted for in the normalizer computation. The seven types below classify signed transitive actions on coordinate pairs.

## Proof
**1. Signed transitive actions.** Let \(G=A_4\). An embedding \(G\hookrightarrow B_n\) acts on the \(n\) two-element sign pairs, and the signed-pair set decomposes into transitive blocks. For each block, choose one pair with stabilizer \(K\le G\) and choose one of the two signs on it. The action of \(K\) on these signs is a homomorphism \(\chi:K\to C_2\). Conversely, the pair \((K,\chi)\) induces such a signed \(G\)-set with \([G:K]\) coordinate pairs. Two induced sets are isomorphic precisely when their \((K,\chi)\) data are conjugate under \(G\). Therefore, multisets of conjugacy classes of pairs \((K,\chi)\) classify signed \(G\)-representations up to conjugacy by \(B_n\).

**2. The seven types and their centralizers.** The complete list of subgroup types of \(A_4\) is \(A_4,V_4,C_3,C_2,1\). The following table records the sign character, block degree and block-centralizer order. The character of \(V_4\) labeled nontrivial can be any one of its three nonzero characters, which are conjugate under the \(C_3\) quotient of \(A_4\).

| Type | Stabilizer \(K\) | Sign character \(\chi\) | Degree \(d_i\) | Centralizer \(c_i\) |
|---:|---|---|---:|---:|
| 0 | \(A_4\) | trivial | 1 | 2 |
| 1 | \(V_4\) | trivial | 3 | 6 |
| 2 | \(V_4\) | nontrivial | 3 | 2 |
| 3 | \(C_3\) | trivial | 4 | 2 |
| 4 | \(C_2\) | trivial | 6 | 4 |
| 5 | \(C_2\) | nontrivial | 6 | 4 |
| 6 | \(1\) | trivial | 12 | 24 |

To see the centralizer orders, a signed equivariant self-bijection of the induced transitive action chooses a new stabilizer-compatible pair, a coset in \(N_G(K,\chi)/K\), and one of two signs. Consequently its centralizer in the signed permutation group has order \(2[N_G(K,\chi):K]\). The normalizers for the seven stabilizer-character pairs have respective orders \(12,12,4,3,4,4,12\), giving \(c_i=2,6,2,2,4,4,24\). For multiple identical transitive blocks, the equivariant self-bijections additionally permute those blocks, giving the complete centralizer
\[
|C_{B_n}(G)|=\prod_{i=0}^6c_i^{m_i}m_i!.
\]
There is no mixing between nonisomorphic transitive blocks.

**3. Faithfulness and subgroup normalizers.** The kernel of the induced signed block \((K,\chi)\) is \(\bigcap_{g\in G}g\ker(\chi)g^{-1}\). It contains the nontrivial normal subgroup \(V_4\) for types 0 and 1. It is trivial for each of types 2–6: for type 2 the three conjugate order-two kernels intersect trivially, while the subgroups \(1,C_2,C_3\) are core-free. Thus a direct sum is faithful precisely when its profile contains a type numbered at least 2. The faithful representations of \(G\) yield the embedded subgroups.

The quotient \(\operatorname{Aut}(G)\cong S_4\) acts on the seven signed transitive isomorphism classes and fixes **each** of them: the subgroup types are intrinsic, and the three nontrivial \(V_4\) characters already belong to one inner-conjugacy orbit. Hence for every automorphism \(\alpha\) of \(G\), a given representation is signed-conjugate to its precomposition with \(\alpha\). For a faithful image \(H\), the conjugation map \(N_{B_n}(H)\to\operatorname{Aut}(H)\) is therefore surjective, with kernel \(C_{B_n}(H)\). Since \(|\operatorname{Aut}(A_4)|=24\), this proves the normalizer formula. It also shows that the faithful profiles, not any further quotient of their set, classify embedded subgroup conjugacy classes.

**4. Enumeration.** Allowing arbitrary nonnegative multiplicities for the seven types yields \(\prod_{i=0}^6(1-z^{d_i})^{-1}\). Precisely the profiles supported on types 0 and 1 are nonfaithful, giving \([(1-z)(1-z^3)]^{-1}\). Their difference is the stated conjugacy-class series.

Every subgroup of profile \(\boldsymbol m\) has orbit length \(|B_n|/|N_{B_n}(H)|=2^nn!/[24\prod_i c_i^{m_i}m_i!]\) under conjugation. Summing these orbit lengths over faithful profiles yields the embedded-subgroup exponential series. Its full exponent is \(\sum_i z^{d_i}/c_i=z/2+2z^3/3+z^4/2+z^6/2+z^{12}/24\); the nonfaithful exponent is \(z/2+z^3/6\). This establishes both generating identities with no uncounted labeling or automorphism factors.

**5. Quasipolynomial degree and least period.** The class series is rational with denominator a product of \(1-z^d\) for \(d\mid12\), hence its coefficients form a quasipolynomial with period dividing twelve. The pole at \(z=1\) has order seven, and its leading Laurent coefficient is
\[
\frac{1}{1\cdot3\cdot3\cdot4\cdot6\cdot6\cdot12}=\frac1{15552}.
\]
The subtracted nonfaithful term has only a double pole at one. Any other twelfth root of unity produces a pole of order at most five, so the leading coefficient is \(1/(15552\cdot6!)\) and the error is \(O(n^5)\). At each primitive twelfth root the \(1-z^{12}\) factor has a genuine simple pole, no other factor vanishes, and the subtracted term is analytic. Thus these primitive twelfth-root contributions cannot cancel; the least quasipolynomial period is exactly twelve.

## Verification
The standalone Python 3 program `verification.py`, requiring no third-party packages, uses exact rational generating functions and exhaustive signed-permutation multiplication. It checks all conjugacy-class and embedded-subgroup coefficients through \(n=12\), independently enumerates all group-member generator pairs of orders three and two with their product of order dividing three through \(n=6\), and independently reconstructs subgroup conjugacy orbits through \(n=4\). The generator-pair enumeration counts each embedded \(A_4\) exactly 24 times (eight elements of order three times three involutions), while the orbit calculation explicitly conjugates the actual 12-element subgroups. The program outputs `A4_HYPEROCTAHEDRAL_PROFILE_NORMALIZER_AND_SUBGROUP_CENSUS_VERIFIED n<=12; brute B_n n<=6`. Finite checks are reproducibility evidence, not substitutes for the general proof in the preceding sections.

## Relationship to prior work
Zibrowius (2022) studies conjugacy classes of **individual involutions** in finite Coxeter groups. Marberg and Zhang (2022) classify perfect involution **representation models** for finite Coxeter groups, including type B. Bernhardt et al. (2021) classify conjugacy classes and centralizers of **individual wreath-product elements**. These do not state the embedded tetrahedral-subgroup profile and normalizer theorem. Schlage-Puchta (2011), building on Müller (2000), provides general homomorphism counting machinery for finite groups into wreath products; in particular, the *embedded-subgroup exponential generating function alone* can be recovered by group-action specialization and is **not claimed as a new general mechanism**. The assessed distinct claim is the complete explicit seven-type faithful image classification with its simultaneous subgroup normalizers, conjugacy-class series and exact quasipolynomial period. The same method can be applied to other small finite source groups, but no such extension is claimed here.

## Limitations
The theorem concerns the standard signed permutation action of type B and embedded subgroups isomorphic to \(A_4\), not arbitrary subgroups, arbitrary Coxeter types, or representations over other coefficient groups. The finite exhaustive checks stop at \(n=6\); the infinite-family statement uses the written orbit and normalizer proof. Although relevant publications and indexed claims were inspected, the absence of a previously published equivalent of the explicit tetrahedral normalizer census cannot be established conclusively by search. In particular, older general wreath-product representation classifications may contain an unlocated equivalent specialization. Independent scientific audit has not been performed.

## References
1. M. Zibrowius, *Dual involutions in finite Coxeter groups* (first public version 2022-02-09), https://arxiv.org/abs/2202.04463.
2. E. Marberg and Y. Zhang, *Perfect models for finite Coxeter groups* (first public version 2022-01-03), https://arxiv.org/abs/2201.00748.
3. J.-C. Schlage-Puchta, *Homomorphisms from a finite group into wreath products*, Archiv der Mathematik 96 (2011), 27–30, open-access manuscript https://biblio.ugent.be/publication/1848757/file/1848765.pdf.
4. T. Müller, *Enumerating representations in finite wreath products*, Advances in Mathematics 153 (2000), 118–154, as cited in Schlage-Puchta (2011).
5. D. Bernhardt, A. C. Niemeyer, F. Rober, and L. Wollenhaupt, *Conjugacy classes and centralisers in wreath products* (2021), https://arxiv.org/abs/2107.04645.
6. L. Klawuhn and K.-U. Schmidt, *Transitivity in wreath products with symmetric groups* (first public version 2024-09-30), https://arxiv.org/abs/2409.20495.
