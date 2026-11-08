# Parabolic automorphism counts and exact socle characters for modular abelian group algebras

## Finding
Let \(p\) be prime, let \(k=\mathbb F_q\) with \(q=p^e\), and let \(G=\prod_{i=1}^{d}C_{p^{s_i}}\), with \(d\ge1\) and all \(s_i\ge1\). Write \(A=kG\), set \(N=p^{\sum_i s_i}\), and define
\[
n_h=\#\{i:s_i=h\},\qquad K_i=N-p^{\sum_{j=1}^{d}\max(s_j-s_i,0)}.
\]
Only finitely many \(n_h\) are nonzero. The full \(k\)-algebra automorphism group has cardinality
\[
\boxed{|\operatorname{Aut}_k(A)|=q^{\sum_i K_i-\sum_h n_h^2}\prod_{h:n_h>0}\prod_{j=0}^{n_h-1}(q^{n_h}-q^j).}
\]
More precisely, its action on \(\mathfrak m/\mathfrak m^2\), for the unique maximal ideal \(\mathfrak m\), is the full block parabolic \(P\) consisting of invertible matrices \(M=(m_{ji})\) with \(m_{ji}=0\) when \(s_j>s_i\). The tangent map splits by linear substitutions, with kernel of order
\[
q^{\sum_i K_i-\sum_i c_i},\qquad c_i=\#\{j:s_j\le s_i\}.
\]
The largest normal \(p\)-subgroup of \(\operatorname{Aut}_k(A)\) has order \(q^{\sum_iK_i-\sum_hn_h^2}\), and the corresponding quotient is \(\prod_h\operatorname{GL}_{n_h}(k)\).

Write \(x_i=g_i-1\), where \(g_i\) is a generator of the corresponding cyclic factor, and let \(z=\prod_i x_i^{p^{s_i}-1}\) span the one-dimensional socle of \(A\). If \(L_h\) denotes the diagonal Levi block of the tangent matrix at height \(h\), then
\[
\boxed{\phi(z)=\left(\prod_h\det(L_h)^{p^h-1}\right)z.}
\]
The image of this character in \(k^\times\) is exactly the subgroup of order
\[
\boxed{\frac{q-1}{p^{\gcd(e,s_1,\ldots,s_d)}-1}.}
\]
All scalars in its image have equal-size fibers. In particular, every algebra automorphism fixes the socle pointwise exactly when \(e\mid s_i\) for all \(i\).

## Assumptions and scope
The automorphisms are unital, \(k\)-linear algebra automorphisms; the coefficient field is fixed pointwise. The group \(G\) is a finite **abelian** \(p\)-group and \(p\) is the characteristic of \(k\). The word "automorphism" always refers to the group algebra as an algebra, **not** just automorphisms of the underlying finite group. The ring is
\[
A\cong k[x_1,\ldots,x_d]/(x_1^{p^{s_1}},\ldots,x_d^{p^{s_d}}).
\]
Its monomial basis has exponents \(0\le \alpha_j<p^{s_j}\). The ideal \(\mathfrak m=(x_1,\ldots,x_d)\) is the unique maximal ideal. The socle is annihilated by \(\mathfrak m\), and its displayed generator \(z\) is a nonzero basis element.

## Proof
**1. Exact allowed generator images.** Any algebra endomorphism is uniquely specified by images \(f_i\in A\) of the \(x_i\) with \(f_i^{p^{s_i}}=0\). The characteristic-\(p\) Frobenius identity gives
\[
\left(\sum_\alpha u_\alpha x^\alpha\right)^{p^{s_i}}
=\sum_\alpha u_\alpha^{p^{s_i}}x^{p^{s_i}\alpha}.
\]
Nonzero monomials on the right are distinct, so no cancellation is possible. A monomial \(x^\alpha\) has nonzero \(p^{s_i}\)-th power precisely if \(\alpha_j=0\) when \(s_j\le s_i\), and \(0\le\alpha_j<p^{s_j-s_i}\) when \(s_j>s_i\). There are exactly \(p^{\sum_j\max(s_j-s_i,0)}\) such monomials, including \(1\). Thus the vector space of permissible \(f_i\) has dimension \(K_i\); every permissible \(f_i\) lies in \(\mathfrak m\).

**2. The parabolic tangent image.** The coefficient of \(x_j\) in \(f_i\) can be nonzero exactly when \(s_j\le s_i\). Hence the tangent matrices are block triangular for the ordering by increasing heights; the diagonal blocks have sizes \(n_h\). For any such invertible matrix, the associated linear substitutions \(x_i\mapsto\sum_jm_{ji}x_j\) respect the pure-power relations, so they define endomorphisms. Because the induced map on \(\mathfrak m/\mathfrak m^2\) is invertible, the endomorphism is surjective: its image generates \(\mathfrak m\) modulo \(\mathfrak m^2\), and successively modulo all powers of \(\mathfrak m\). Since \(A\) is finite dimensional, it is an automorphism. These linear substitutions yield a splitting of the tangent map. There are \(q^{K_i-c_i}\) possible higher-coefficient completions per column, independently, where \(c_i=\sum_{h\le s_i}n_h\), proving the kernel order and counting formula.

**3. The largest normal \(p\)-subgroup.** The unipotent radical of \(P\) has cardinality \(q^{\sum_{h<h'}n_hn_{h'}}\), and its Levi quotient is \(\prod_h\operatorname{GL}_{n_h}(k)\). The tangent kernel has a filtration by its action on the powers of \(\mathfrak m\); successive quotients embed in additive groups of characteristic \(p\), so it is a \(p\)-group. The preimage of the unipotent radical is therefore a normal \(p\)-group with order \(q^{\sum_iK_i-\sum_hn_h^2}\). Each \(\operatorname{GL}_{n_h}(k)\) has trivial normal \(p\)-subgroup: a normal \(p\)-subgroup acting on its defining characteristic-\(p\) module fixes a nonzero vector, and normality makes its full fixed subspace invariant under the transitive natural general linear group, hence the subgroup acts trivially. Thus the displayed preimage is the full \(O_p\).

**4. Exact socle scalar.** Let \(T=\sum_i(p^{s_i}-1)\) be the maximum possible total monomial degree. Since \(\mathfrak m^{T+1}=0\), replacing any linear image by that image plus terms of degree at least two cannot alter the coefficient of \(z\) in \(\phi(z)\). The action on the socle therefore depends only on the tangent matrix. A parabolic unipotent shear across distinct heights acts trivially on \(z\), because every cross term raises the exponent of a variable already at its maximal allowed degree. On each equal-height block, elementary shears likewise fix the product of top powers; a diagonal scaling changes it by \(\prod \lambda_i^{p^h-1}=\det(L_h)^{p^h-1}\). Transpositions also satisfy this identity: if \(p\) is odd, \(p^h-1\) is even, and if \(p=2\), the sign is trivial. General linear groups are generated by such matrices, so the character formula holds for all \(\phi\).

**5. Arithmetic image and equal fibers.** Each determinant map \(\operatorname{GL}_{n_h}(k)\to k^\times\) is surjective, so the socle image is the subgroup generated by \((k^\times)^{p^h-1}\) for the occurring heights. The group \(k^\times\) is cyclic of order \(q-1\). Its indicated subgroup therefore has index
\[
\gcd(q-1,p^{s_1}-1,\ldots,p^{s_d}-1)=p^{\gcd(e,s_1,\ldots,s_d)}-1.
\]
The fibers of a group homomorphism are cosets of its kernel and are equicardinal. The character is trivial if and only if its index equals \(q-1\), namely when \(e\) divides every \(s_i\). This also includes the prime-field case \(e=1\).

## Verification
The accompanying self-contained `verify.py` constructs polynomial quotient algebras, enumerates admissible generator images, checks invertibility by **actual substitution matrices**, and independently determines socle scalars. Its tests cover \(q\in\{2,3,4\}\), including both mixed- and equal-height cases, with exhaustive configurations: \((q;s_i)=(2;1),(2;2),(2;1,1),(2;1,2),(3;1),(4;1),(4;2),(4;1,1)\). The observed automorphism counts are respectively \(1,4,24,2048,6,3,48,2880\), all matching the theorem. The \(\mathbb F_4\) examples verify both a full socle-character image and a trivial one. The code ends with `VERIFY_OK`. These small exhaustive tests check calculations; the unrestricted formulas follow from the proof, not from extrapolation.

## Relationship to prior work
Benson's 2023 theorem gives a general socle determinant constraint for arbitrary finite \(p\)-group algebras, including the fact that the socle is fixed over the prime field. The present result **does not reassert that as new**. It specializes to abelian groups but adds a complete height-sensitive count of all algebra automorphisms, their parabolic quotient and largest normal \(p\)-subgroup, and the exact attainable socle-scalar subgroup and equal-size fibers over every finite extension field. The group-algebra isomorphism with a truncated polynomial ring is standard. Deo and Maitra classify **graded** automorphisms of truncated polynomial algebras over characteristic-zero fields; their monomial wreath-product restriction explicitly relies on characteristic zero and grading, whereas the present algebra automorphisms are ungraded and the characteristic-\(p\) Frobenius allows full same-height general linear blocks. Díaz, Liendo, Manzano-Flores, and Regeta describe automorphisms of zero-dimensional monomial algebras in characteristic zero; their characteristic-zero hypotheses do not supply these positive-characteristic Frobenius constraints or finite-field counts. Published results for truncated coordinate-cross algebras impose mixed-product-zero relations, rather than the pure-power relations of the present group algebras. The elementary formula for \(\operatorname{Aut}(G)\) concerns the much smaller subgroup of automorphisms induced by automorphisms of \(G\), so it cannot by itself count all \(k\)-algebra automorphisms.

## Limitations
The formulas apply only to finite **abelian** \(p\)-groups over finite coefficient fields of the same characteristic, with coefficient-field-linear automorphisms. They do not classify individual automorphisms up to conjugacy, nor do they address nonabelian group algebras. The literature comparison is not a proof of publication priority: an as-yet-unlocated general automorphism-group enumeration of modular group algebras might imply portions of the formulas. The computational verifier is exhaustive only for its stated small cases. Independent mathematical audit has not been performed.

## References
1. David J. Benson, *The socle of the group algebra of a finite \(p\)-group*, arXiv:2303.09940v1, publicly posted March 17, 2023. https://arxiv.org/html/2303.09940v1
2. R. Díaz, A. Liendo, A. Manzano-Flores, A. Regeta, *The Automorphism Groups of Zero-Dimensional Monomial Algebras*, arXiv:2408.02197v1, publicly posted August 5, 2024. https://arxiv.org/abs/2408.02197
3. R. Sharifi, *Iwasawa Theory, Chapter 2: Module Theory*, Lemma 2.3.6 on the modular group algebra as a local ring. https://math.ucla.edu/~sharifi/notes/iwasawa-ch02.html
4. S. Deo and J. K. Maitra, *Automorphism groups of truncated polynomial algebras*, National Academy Science Letters 20 (1997), 75–80. https://www.researchgate.net/profile/Satya-Deo-2/publication/266354814_Automorphism_groups_of_truncated_polynomial_algebras/links/576e255008ae0b3a3b7558c9/Automorphism-groups-of-truncated-polynomial-algebras.pdf
