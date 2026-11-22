# Simultaneous permutation normalization of ternary perfect evolution algebras

## Finding

Let \(E\) be any finite-dimensional perfect evolution algebra over \(\mathbb F_3\), with natural basis \((e_1,\ldots,e_n)\) and invertible structure matrix \(A\), whose \(j\)-th column expresses \(e_j^2\). There is a **single diagonal change of natural basis** after which every algebra automorphism is represented by a permutation matrix. Equivalently, the full automorphism group is, in one natural basis, a subgroup \(H\leq S_n\), and the transformed structure matrix commutes with each permutation matrix in \(H\). This simultaneous statement holds without any transitivity, symmetry, or support assumption on \(A\).

As a counting consequence, put \(z_\lambda=\prod_{j\ge1}j^{m_j}m_j!\) for a partition \(\lambda\vdash n\), where \(m_j\) is the number of its parts of size \(j\). If \(P_\lambda\) is a permutation matrix of cycle type \(\lambda\), then the number of isomorphism classes of perfect evolution algebras of dimension \(n\) over \(\mathbb F_3\) is

\[
I_n=\sum_{\lambda\vdash n}\frac{|C_{\mathrm{GL}_n(3)}(P_\lambda)|}{2^{\ell(\lambda)}z_\lambda}.
\]

In particular, \(I_1=1\), \(I_2=7\), \(I_3=249\), \(I_4=63{,}985\), and **\(I_5=124{,}108{,}129\)**. The reduction of the general orbit count to centralizer orders is a ternary-field specialization; the independent structural assertion is the *simultaneous normalization of the whole automorphism group*. The general orbit-counting principle itself was known previously [1].

## Assumptions and scope

An evolution algebra is a commutative (not necessarily associative) algebra with a basis \(e_1,\ldots,e_n\) satisfying \(e_ie_j=0\) for distinct indices. It is perfect if \(E^2=E\), equivalently its structure matrix \(A\) is invertible. All algebras are considered over exactly \(\mathbb F_3\), and automorphisms are \(\mathbb F_3\)-linear algebra automorphisms. No algebraic closure or scalar extension is taken. The theorem concerns the whole **finite rational automorphism group**, not the automorphism group scheme over other fields.

## Proof

**1. Monomiality.** For a perfect evolution algebra the squares \(e_1^2,\ldots,e_n^2\) form a basis. If \(U\) is an automorphism matrix, the equation \(U(e_i)U(e_j)=0\) for \(i\ne j\) and independence of those squares imply that columns \(i\) and \(j\) of \(U\) have disjoint supports. Invertibility forces one nonzero entry in each row and column. Thus \(U=P D\) for a permutation matrix \(P\) and diagonal \(D\), with diagonal entries in \(\{1,-1\}\). Applying the automorphism to all squares gives \(UA=A(PD)^{(2)}=AP\), since \(D^2=I\) over \(\mathbb F_3\). Consequently

\[
U=APA^{-1}.
\]

The map \(U\mapsto P\) is an injective group homomorphism on the automorphism group: if \(P=I\), then \(U=I\). Write its image as \(H\le S_n\), and let \(U_h\) be the unique corresponding monomial automorphism.

**2. A common simultaneous normalization.** The representations \(h\mapsto U_h\) and \(h\mapsto P_h\) are conjugate by \(A\); hence their fixed-vector spaces have the same dimension. The fixed-vector space of the permutation representation \(P\) is the space of vectors constant on each \(H\)-orbit of \(\{1,\ldots,n\}\), with dimension the number of orbits. As each \(U_h\) is monomial with underlying permutation \(P_h\), its action preserves the coordinate subspace on each such orbit. Each nonzero fixed vector on a *transitive* orbit has no zero coordinates: if one coordinate vanished, monomial transitivity would force all of them to vanish. The fixed space for each transitive orbit has dimension at most one, since a fixed vector is uniquely determined by one coordinate. The total fixed-space dimension equals the total number of orbits, so each orbit contributes exactly one dimension. Choose a nonzero fixed vector on each orbit and combine them into a vector \(v\) with **all** coordinates nonzero. Let \(T=\operatorname{diag}(v_1,\ldots,v_n)\). For every \(h\), the equality \(U_hv=v\) and the monomial support condition imply \(T^{-1}U_hT=P_h\). This is a *single* \(T\) working for every \(h\). The natural basis \(e'_j=v_j e_j\) has new structure matrix \(A'=T^{-1}A\), because \(v_j^2=1\). Thus \(P_hA'=A'P_h\) for all \(h\), as claimed.

**3. Fixed structure matrices under natural-basis changes.** The natural-basis change group is \(B_n=(\mathbb F_3^\times)^n\rtimes S_n\), of order \(2^n n!\). Its action on \(\mathrm{GL}_n(3)\) is \(A\mapsto (PD)^{-1}AP\), because every entry of \(D\) squares to one. Fixed matrices therefore satisfy \((PD)A=AP\), so there are \(|C_{\mathrm{GL}_n(3)}(P)|\) fixed matrices when \(PD\) is similar to \(P\), and none otherwise. For each cycle of \(P\) the product of the signs on that cycle is either \(+1\) or \(-1\). If every cycle product is \(+1\), diagonal conjugation changes \(PD\) into \(P\). Conversely, a negative-sign cycle contributes no fixed vector to \(PD\), while an ordinary permutation cycle contributes exactly one fixed vector; therefore similarity forces all cycle products to be positive. There are precisely \(2^{n-\ell(\lambda)}\) sign assignments with this property. Burnside's formula and the conjugacy-class size \(n!/z_\lambda\) give

\[
\frac1{2^n n!}\sum_{\lambda\vdash n}\frac{n!}{z_\lambda}\,2^{n-\ell(\lambda)}|C_{\mathrm{GL}_n(3)}(P_\lambda)|
=\sum_{\lambda\vdash n}\frac{|C_{\mathrm{GL}_n(3)}(P_\lambda)|}{2^{\ell(\lambda)}z_\lambda}.
\]

**4. Exact centralizers.** Factor \(X^j-1\) over \(\mathbb F_3\) for every part \(j\) of \(\lambda\). If an irreducible polynomial \(f\) appears in the elementary divisors with exponents given by a partition \(\mu_f\), let \(d_f=\deg f\), let \(\mu'_f\) be its conjugate partition, and let \(m_t(\mu_f)\) count its parts of size \(t\). The centralizer's group of units has exact order

\[
\prod_f 3^{d_f\sum_r(\mu'_{f,r})^2}
\prod_{t\ge1}\prod_{s=1}^{m_t(\mu_f)}(1-3^{-sd_f}).
\]

To see this, regard the permutation module as a direct sum of cyclic \(\mathbb F_3[X]\)-modules; the endomorphism algebra splits by primary factors, has dimension \(d_f\sum_r(\mu'_{f,r})^2\) on the \(f\)-primary factor, and its semisimple quotient is \(\prod_t M_{m_t(\mu_f)}(\mathbb F_{3^{d_f}})\). Invertibility is exactly invertibility in every block of this quotient, giving the displayed factors. This standard finite-module calculation remains valid when \(3\mid j\) and the factors of \(X^j-1\) repeat.

For \(n=5\), exact rational-arithmetic evaluation gives:

| Cycle-type partition \(\lambda\) | Centralizer order | \(z_\lambda\) | Contribution to \(I_5\) |
|---|---:|---:|---:|
| \((1,1,1,1,1)\) | 475,566,474,240 | 120 | 123,845,436 |
| \((1,1,1,2)\) | 48,522,240 | 12 | 252,720 |
| \((1,1,3)\) | 69,984 | 6 | 1,458 |
| \((1,2,2)\) | 539,136 | 8 | 8,424 |
| \((1,4)\) | 768 | 4 | 48 |
| \((2,3)\) | 648 | 6 | 27 |
| \((5)\) | 160 | 5 | 16 |

The last column sums to \(124{,}108{,}129\), proving the stated fifth-dimensional count.

**5. Characteristic boundary.** This normalization does not hold over every finite field. Over \(\mathbb F_4\), the perfect two-dimensional evolution algebra \(e_1^2=e_2\), \(e_2^2=e_1\) admits the nontrivial diagonal automorphism \(e_1\mapsto \alpha e_1\), \(e_2\mapsto\alpha^2e_2\) for \(\alpha\in\mathbb F_4^\times\) of order three. A nonidentity diagonal automorphism remains diagonal after every diagonal basis change, so it cannot be converted into a nonidentity permutation matrix. This refutes an unrestricted-field extension.

## Verification

Run `python3 verify.py` with Python 3 and no external packages. It computes centralizer orders using monic factorization of \(X^j-1\) over \(\mathbb F_3\), verifies the integer formula for dimensions one through five and the seven-row fifth-dimensional table, and independently enumerates all invertible structure matrices in dimensions one through three. In those dimensions it enumerates each full monomial automorphism group and tests a single diagonal sign normalization for all its elements, as well as the complete natural-basis isomorphism-orbit counts. The small checks establish finite evidence; the all-dimensional conclusions follow from the preceding proof, not from extrapolation.

## Relationship to prior work

Wei and Zou [1] establish the general monomial-orbit description and Burnside enumeration for all finite fields and explicit counts through dimension four. Thus the underlying orbit action and the general counting method are **prior art**. The novelty assessed here is the all-dimensional **simultaneous untwisting of the entire automorphism group for \(\mathbb F_3\)**, including nontransitive actions, and its explicit centralizer-only arithmetic specialization, with a fifth-dimensional evaluated example. Elduque and Labra [2] establish the monomial automorphism framework and an exact sequence involving diagonal automorphisms. Costoya, Mayorga and Viruel [3] investigate automorphism permutation representations and transitivity restrictions, but their stated main results are different from simultaneous diagonal normalization for all ternary perfect evolution algebras. The independent fifth-dimensional number is a derived evaluation, not claimed to supersede [1]'s general formula.

## Limitations

No full classification of individual fifth-dimensional isomorphism representatives is asserted. The proof concerns automorphisms defined over \(\mathbb F_3\), not over extension fields. The F4 example shows that the exact simultaneous-normalization conclusion fails for arbitrary fields. The centralizer-count specialization and numerical evaluation are consequences of the known general orbit framework, and may independently be recoverable from [1]. Earlier statements using the language of monomial representations, cocycle trivialization, or natural-basis gauges may exist despite the source comparisons; publication priority needs external expert verification. No independent mathematical validation or external certification is asserted.

## References

[1] Yangjiang Wei and Yi Ming Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368, first submitted 2023-10-18, https://arxiv.org/abs/2310.12368, DOI: 10.1016/j.laa.2023.06.006.

[2] Alberto Elduque and Alicia Labra, *Evolution Algebras, Automorphisms, and Graphs*, Journal of Algebra and Its Applications (2021); public 2019 manuscript available at https://www.math.uci.edu/~brusso/ElduqueAutoGraph.pdf.

[3] Cristina Costoya, Pedro Mayorga, Antonio Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, Mediterranean Journal of Mathematics 22 (2025), article 149, https://doi.org/10.1007/s00009-025-02924-0.
