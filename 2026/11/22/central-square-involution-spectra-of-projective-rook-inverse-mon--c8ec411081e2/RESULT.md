# Central-square involution spectra of projective rook inverse monoids

## Finding

Let \(G\) be a finite group and \(n\geq 1\). Let \(\mathcal R_n(G)\) be the inverse monoid of partial \(G\)-labelled bijections of \([n]\). Its partial-inner monoid is the image of the action by conjugation on supported local corners. Write \(Z=Z(G)\) and \(\rho_G(z)=|\{g\in G:g^2=z\}|\) for \(z\in Z\).

Two positive-rank labelled maps represent the same partial inner automorphism exactly when they have the same underlying partial bijection and their labels differ by multiplication by one common element of \(Z\). Thus the rank strata have cardinalities
\[
B_{n,0}=1,\qquad B_{n,r}=\binom nr^2\frac{r!\,|G|^r}{|Z|}\quad(1\le r\le n),
\]
and the maximal subgroup at a rank-\(r\) idempotent for \(r>0\) is
\[
H_r\cong (G^r\rtimes\mathfrak S_r)/\Delta Z,
\qquad \Delta Z=\{(z,\ldots,z;1):z\in Z\}.
\]

The numbers of self-inverse elements are \(I_{n,0}(G)=1\) and, for \(1\le r\le n\),
\[
I_{n,r}(G)=\frac{\binom nr}{|Z|}
\sum_{j=0}^{\lfloor r/2\rfloor}
\frac{r!\,|G|^j}{2^j j!(r-2j)!}
\sum_{z\in Z}\rho_G(z)^{r-2j}.
\]
In this expression a zeroth power is one even if \(\rho_G(z)=0\). For an abelian label group \(A\) with \(t=|A[2]|\), the average \(|A|^{-1}\sum_{z\in A}\rho_A(z)^f\) is one for \(f=0\) and \(t^{f-1}\) for \(f\ge 1\). At rank two, \(H_2\cong A\rtimes_{-1} C_2\) and \(I_{n,2}(A)=\binom n2(|A|+|A[2]|)\). The groups \(C_4\) and \(C_2^2\) have the same \(B_{n,r}\) for all \(n,r\), but at \(n=2\) their rank-two self-inverse counts are \(6\) and \(8\).

## Assumptions and conventions

A labelled map \(u:A\to B\) consists of a bijection between subsets of \([n]\) and one label on each arrow; this label notation uses the product of labels in the order the arrows are traversed. Maps act on points by ordinary right-to-left composition. Write \(\mathcal R_B(G)\) for partial labelled bijections whose domains and images lie in \(B\). The partial inner automorphism associated to \(u\) acts from \(\mathcal R_B(G)\) to \(\mathcal R_A(G)\) as \(x\mapsto u^{-1}xu\). Its domain and range are these actual submonoids. The rank of \(u\) is \(|A|=|B|\), and the empty map has rank zero. Self-inverse means equality with the inverse in the partial-inner monoid (including its idempotents), not that the square is the global identity. No claim concerns other partial automorphisms.

## Proof

**Kernel and rank strata.** Equality of partial conjugation maps identifies their domain and range corners and hence both supports: a corner's rank-one idempotents identify the points of its support. Conjugation of those idempotents recovers the inverse of the underlying support bijection. Now let two representatives have the same underlying bijection \(\sigma:A\to B\). Index their labels \(\gamma_b,\eta_b\) by target point \(b\in B\). A matrix unit with arrow \(b\to c\) and label \(x\) is conjugated to an arrow \(\sigma^{-1}(b)\to \sigma^{-1}(c)\) with label \(\gamma_b x\gamma_c^{-1}\), by following the three arrows through \(u\), the matrix unit, and \(u^{-1}\). Equality for every loop label at \(b\) forces \(\gamma_b^{-1}\eta_b\in Z\). Writing \(\eta_b=\gamma_b z_b\), equality for a unit with label \(1\) from \(b\) to \(c\) then forces \(z_b=z_c\). This last condition is vacuous at rank one.

Conversely, if all \(z_b\) equal one \(z\in Z\), conjugation agrees on every labelled arrow. An arbitrary member of a corner can have several arrows. Conjugation applies the same endpoint and label rule to each of its arrows, and the result is determined by that collection, including the empty collection. Thus the two partial conjugation functions agree on the entire corner.

The standard inverse-semigroup partial-inner construction gives an inverse monoid as this image. With right-to-left composition, conjugation by \(u^{-1}\) in the displayed direction reverses multiplication; indexing the same image by \(u^{-1}\) instead preserves multiplication and gives the same fibers up to inversion. For each positive rank the common-label action is free, so choosing both supports, a bijection, and a label tuple modulo this action gives \(B_{n,r}\). Empty support gives the single rank-zero element. At a given support the representatives of the corresponding maximal subgroup are exactly the labelled permutations of that support. The common-label subgroup \(\Delta Z\) is central in their wreath product: its labels commute with every coordinate and are invariant under permutation. Using the multiplication-preserving indexing gives the displayed local quotient.

**Self-inverse classes.** Equality with the inverse forces domain and image to coincide. At such a support, the representative's underlying permutation must square to the identity, and the labelled square must have the same central label \(z\) at every point to represent the local identity. This is also sufficient, by the kernel description. A permutation with \(j\) transpositions and \(f=r-2j\) fixed points has \(r!/(2^j j!f!)\) realizations. For a prescribed \(z\), on each transposition the first label \(a\) may be chosen arbitrarily and the other is forced to be \(a^{-1}z\). Centrality ensures that the reverse product is also \(z\). At each fixed point the label must square to \(z\), giving \(\rho_G(z)\) choices. These choices are independent and give \(|G|^j\rho_G(z)^f\). At positive rank a qualifying representative has a unique common square label. Summing over \(z\) before dividing by \(|Z|\) is necessary in general: multiplying all labels by a common element of \(Z\) can change \(z\), but preserves the set of qualifying representatives. Freeness gives the division by \(|Z|\), and choosing the single support gives \(\binom nr\).

**Abelian case and the example.** The squaring homomorphism of \(A\) has a kernel of size \(t\), so there are \(|A|/t\) fibers of size \(t\) and all others are empty. This gives the moment simplification. For rank two, the map \((a,b)\mapsto ab^{-1}\) identifies \(A^2/\Delta A\) with \(A\), and transposition acts by inversion. The abelian subgroup contributes \(t\) elements with square one and the other coset contributes all \(|A|\) of its elements. The rank formulas depend only on \(|A|=|Z(A)|\), whereas the two abelian groups of order four have \(t=2\) and \(t=4\), giving the separation.

## Verification

The accompanying `check_projective_rook.py` uses finite multiplication tables for \(C_2,C_3,C_4,C_2^2,S_3,Q_8\). It enumerates labelled partial bijections for \(n\le 3\), compares projective-label classes and direct self-inversion with the formulas, and tests conjugation signatures on all labelled matrix units for \(n\le 2\) and for \(n=3\) with \(C_2,S_3\). The rule proved above explains why those signatures determine the actions on larger-rank corner elements as well. See `verification_output.txt` for the recorded replay; the command is `python3 check_projective_rook.py`, with no third-party packages. For example, at \(n=3\), the rank and self-inverse strata are respectively \((1,54,648,1296)\) and \((1,12,66,136)\) for \(S_3\), and \((1,36,576,1536)\) and \((1,12,84,208)\) for \(Q_8\). These are finite checks; the proof establishes the formulas for all parameters stated.

## Relationship to prior work and limitations

The partial-inner construction and its general relation to the central congruence for inverse semigroups are prior work [1, 2], including the unlabelled symmetric inverse monoid in [1, Remark 3.11]. The contribution here is the explicit common-label quotient for labelled rook maps, together with the central-square distribution and the separation of equal rank counts. Ordinary wreath-product power classifications [4] concern a different count: the projective count here sums over square roots of the diagonal central subgroup, then divides by its common-label action. Absolute involutions of projective complex reflection groups [5, §4] instead satisfy \(g\overline g=1\). For example, the class of \(\operatorname{diag}(1,i)\) modulo common fourth-root scalars is an absolute involution, but the square of the representative is not a scalar matrix. These distinctions do not establish absolute publication priority for the enumerator. The result does not classify all element orders or conjugacy classes.

## References

1. J. Araújo, W. Bentz, M. Kinyon, J. Konieczny, A. Malheiro and V. Mercier, *The Inverse Monoid of Partial Inner Automorphisms of a Semigroup*, arXiv:2605.00041, https://arxiv.org/abs/2605.00041.
2. M. Kinyon and D. Stanovský, *Abelianness and centrality in inverse semigroups*, arXiv:2209.13805, https://arxiv.org/abs/2209.13805.
3. C. H. Houghton, *Embedding inverse semigroups in wreath products*, Glasgow Mathematical Journal 17 (1976), 77–82, DOI:10.1017/S0017089500002767.
4. R. Kundu and S. Mondal, *Powers in the wreath product of \(G\) with \(S_n\)*, arXiv:2010.04954, https://arxiv.org/abs/2010.04954.
5. F. Caselli, *Involutory reflection groups and their models*, arXiv:0905.3649, https://arxiv.org/abs/0905.3649.
