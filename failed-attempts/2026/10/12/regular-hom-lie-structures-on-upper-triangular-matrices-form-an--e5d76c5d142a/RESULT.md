# Regular Hom-Lie structures on upper triangular matrices form an explicit affine group

## Finding

Let \(K\) be a field, let \(n\ge3\), and let
\[
T_n(K)
\]
be the algebra of upper triangular \(n\times n\) matrices, viewed as a Lie algebra under the commutator bracket.

Write \(E=E_{1n}\). Every regular Hom-Lie structure on \(T_n(K)\) is uniquely of the form
\[
\boxed{
\Phi_{t,\alpha}(X)
=
(I+tE)X(I-tE)
+
\left(\sum_{i=1}^n\alpha_i x_{ii}\right)I,
}
\]
where
\[
t\in K,
\qquad
\alpha=(\alpha_1,\ldots,\alpha_n)\in K^n,
\]
and
\[
\boxed{r(\alpha)=1+\sum_{i=1}^n\alpha_i\ne0.}
\]

Composition is given by the closed formula
\[
\boxed{
\Phi_{t,\alpha}\circ\Phi_{s,\beta}
=
\Phi_{t+s,\,\alpha+r(\alpha)\beta}.
}
\]
Consequently
\[
\boxed{
\operatorname{RHL}(T_n(K))
\cong
(K,+)\times\bigl(K^{n-1}\rtimes K^\times\bigr),
}
\]
where \(K^\times\) acts on the additive group \(K^{n-1}\) by scalar multiplication.

Over a finite field \(\mathbf F_q\),
\[
\boxed{
|\operatorname{RHL}(T_n(\mathbf F_q))|
=q^n(q-1).
}
\]
For \(q=2\), this group is elementary abelian:
\[
\operatorname{RHL}(T_n(\mathbf F_2))\cong C_2^n.
\]
For \(q>2\),
\[
\boxed{|Z(\operatorname{RHL})|=q,\qquad
|[\operatorname{RHL},\operatorname{RHL}]|=q^{n-1}.}
\]
Thus the full group structure is independent of the triangular size except through the additive dimension \(n-1\).

## Assumptions and scope

The theorem treats \(n\ge3\). The two-dimensional chain has an exceptional freedom in the inner factor in the source classification and is excluded.

A regular Hom-Lie structure means an invertible linear self-map satisfying the Hom-Jacobi identity for the commutator Lie algebra.

No restriction on the characteristic or algebraic closure of \(K\) is needed.

## Proof

For the chain poset of size \(n\), the incidence algebra is \(T_n(K)\). Its Jacobson radical \(J\) is the strictly upper triangular algebra. The center of \(J\), for \(n\ge3\), is
\[
Z(J)=K E_{1n}.
\]

The cited classification of regular Hom-Lie structures on a finite-chain incidence algebra says that every such structure has a unique factorization
\[
\Phi=\xi_\beta+\nu,
\]
where \(\xi_\beta(X)=\beta X\beta^{-1}\), the diagonal of \(\beta\) is the identity, the radical part of \(\beta-I\) lies in \(Z(J)\), and \(\nu\) is central-valued and vanishes on \(J\).

Therefore
\[
\beta=I+tE_{1n}
\]
for a unique \(t\in K\). Since \(E_{1n}^2=0\),
\[
\beta^{-1}=I-tE_{1n}.
\]
Every central-valued linear map vanishing on \(J\) is uniquely
\[
\nu_\alpha(X)
=
\left(\sum_{i=1}^n\alpha_i x_{ii}\right)I
\]
for a unique \(\alpha\in K^n\). This yields the displayed formula for \(\Phi_{t,\alpha}\).

It remains to identify invertibility. The inner factor acts invertibly and leaves all diagonal entries unchanged. Modulo \(J\), the map induced by \(\Phi_{t,\alpha}\) on the diagonal vector \(x\in K^n\) is
\[
x\longmapsto x+(\alpha\cdot x)\mathbf 1,
\]
where \(\mathbf 1=(1,\ldots,1)^T\). By the matrix determinant lemma,
\[
\det(I+\mathbf 1\alpha^T)
=1+\alpha^T\mathbf 1
=1+\sum_i\alpha_i
=r(\alpha).
\]
Thus \(\Phi_{t,\alpha}\) is regular exactly when \(r(\alpha)\ne0\).

For composition, inner shears commute and add because \(E^2=0\):
\[
\xi_{I+tE}\xi_{I+sE}=\xi_{I+(t+s)E}.
\]
They preserve diagonal entries, while any scalar matrix is fixed by every inner automorphism. Therefore
\[
\Phi_{t,\alpha}\Phi_{s,\beta}
=
\Phi_{t+s,\,\alpha+r(\alpha)\beta}.
\]
In particular,
\[
r(\alpha+r(\alpha)\beta)
=r(\alpha)r(\beta).
\]

Let
\[
G=\{\alpha\in K^n:r(\alpha)\ne0\}
\]
with product
\[
\alpha*\beta=\alpha+r(\alpha)\beta.
\]
Then
\[
r:G\to K^\times
\]
is a surjective homomorphism. Its kernel is the additive hyperplane
\[
H=\left\{\alpha:\sum_i\alpha_i=0\right\}\cong K^{n-1}.
\]
A section is given by
\[
c\longmapsto(c-1)e_n.
\]
Conjugation by this section multiplies \(H\) by \(c\). Hence
\[
G\cong K^{n-1}\rtimes K^\times,
\]
and the independent parameter \(t\) contributes the direct factor \((K,+)\).

Over \(\mathbf F_q\), the order is immediately
\[
q\cdot q^{n-1}(q-1)=q^n(q-1).
\]
If \(q=2\), the multiplicative factor is trivial, so the group is \(C_2^n\). If \(q>2\), the center of the affine factor is trivial and its commutator subgroup is its translation subgroup \(\mathbf F_q^{n-1}\). The outer direct additive factor therefore gives center order \(q\), and the derived subgroup has order \(q^{n-1}\).

## Verification

The included checker verifies the parameter group law over \(\mathbf F_2\), \(\mathbf F_3\), and \(\mathbf F_5\), including associativity, inverses, the stated orders, centers, and derived subgroup sizes.

It separately constructs the corresponding linear maps on \(T_3(\mathbf F_q)\) for \(q=2,3\), checks invertibility, and verifies the Hom-Jacobi identity on every ordered triple of matrix-unit basis elements.

The checker returns `VERIFY_OK`.

These finite computations are consistency checks; the theorem itself is proved symbolically.

## Relationship to prior work

Fornaroli, Khrypchenko, and Santulo classify regular Hom-Lie structures on incidence algebras. For a finite chain of size greater than two, their chain specialization says that every regular Hom-Lie structure is uniquely an inner automorphism whose radical part lies in the one-dimensional center of the radical, plus a unique central map annihilating the radical.

Their paper also proves that regular Hom-Lie structures form a normal subgroup of the Lie automorphism group. The inspected full text does not state the explicit abstract group isomorphism above, does not specialize to finite fields, and contains no finite-field enumeration.

Chen and Yu classify regular Hom-Lie structures on strictly upper triangular matrix Lie algebras. That is a different Lie algebra: it omits the diagonal subalgebra whose rank-one update is responsible for the \(K^{n-1}\rtimes K^\times\) factor here.

Targeted semantic and literature searches under regular Hom-Lie, upper triangular, chain incidence, affine semidirect-product, and finite-field counting formulations did not locate the displayed group decomposition or its finite-field center and derived-subgroup formulas.

## Limitations

The theorem begins at \(n=3\); the source classification has an exceptional \(n=2\) chain case.

The result concerns regular, hence invertible, Hom-Lie structures. It does not classify singular Hom-Lie maps.

The group decomposition is a structural extraction from the published classification, not a new classification theorem for arbitrary incidence algebras.

Failed searches do not prove novelty.

## References

1. E. Z. Fornaroli, M. Khrypchenko, and E. A. Santulo Jr., “Regular Hom-Lie structures on incidence algebras,” arXiv:2212.12591v1, first public version 23 December 2022; *Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas* 117 (2023), Article 122, DOI 10.1007/s13398-023-01454-2. Primary MSC 2020 includes 16S50.
2. H. Chen and X. Yu, “Regular Hom-Lie structures on strictly upper triangular matrix Lie algebras,” *Journal of Algebra and Its Applications* 21 (2022), 2250081, DOI 10.1142/S0219498822500815.
