# Plücker degree dominates Euler characteristic for even orthogonal two-plane Grassmannians
## Finding
For every integer
\[
n\ge4,
\]
let
\[
X_n=\operatorname{OG}(2,2n)
\]
be the complex Grassmannian of isotropic two-planes in a \(2n\)-dimensional vector space with a nondegenerate symmetric bilinear form. Equip \(X_n\) with its Plücker embedding.

Then
\[
\boxed{
\deg X_n=
\frac{2(4n-7)!}
{(n-1)(n-2)(2n-3)!(2n-5)!}
}
\]
and
\[
\boxed{
\chi_{\mathrm{top}}(X_n)=2n(n-1).
}
\]

The projective degree is always strictly larger:
\[
\boxed{
\deg X_n>\chi_{\mathrm{top}}(X_n)
\qquad(n\ge4).
}
\]

More strongly, the normalized ratio
\[
\frac{\deg X_n}{\chi_{\mathrm{top}}(X_n)}
\]
is strictly increasing. Its first value is
\[
\frac{\deg X_4}{\chi_{\mathrm{top}}(X_4)}
=
\frac{168}{24}
=
7.
\]

The consecutive degree ratio is
\[
\boxed{
\frac{\deg X_{n+1}}{\deg X_n}
=
\frac{2(4n-5)(4n-3)}{n(2n-1)}.
}
\]
Hence
\[
\frac{\deg X_{n+1}/\chi_{\mathrm{top}}(X_{n+1})}
{\deg X_n/\chi_{\mathrm{top}}(X_n)}
=
\frac{2(4n-5)(4n-3)(n-1)}
{n(2n-1)(n+1)}
>1.
\]

## Assumptions and scope
All varieties are over \(\mathbb C\). The notation
\[
\operatorname{OG}(2,2n)
\]
means the connected homogeneous variety of two-dimensional isotropic subspaces for a nondegenerate quadratic form on \(\mathbb C^{2n}\).

The embedding is the ordinary Plücker embedding. This is not the half-spin embedding used for maximal even orthogonal Grassmannians.

The restriction \(n\ge4\) keeps the family in the stable type-\(D_n\) range and away from the low-rank accidental isomorphism \(D_3\simeq A_3\).

## Proof
Write the positive roots of type \(D_n\) as
\[
e_i-e_j,\quad e_i+e_j
\qquad(1\le i<j\le n).
\]
For \(X_n=\operatorname{SO}(2n)/P_2\), the Plücker line bundle corresponds to the fundamental weight
\[
\omega_2=e_1+e_2.
\]
The half-sum of positive roots is
\[
\rho=(n-1,n-2,\ldots,1,0).
\]

The positive roots outside the Levi subsystem are
\[
e_1-e_j,\ e_2-e_j,\ e_1+e_j,\ e_2+e_j
\qquad(3\le j\le n),
\]
together with
\[
e_1+e_2.
\]
Their number is
\[
4(n-2)+1=4n-7,
\]
which is the dimension of \(X_n\).

For a homogeneous embedding \(G/P\hookrightarrow\mathbb P(V_\lambda)\), the Weyl dimension formula applied to
\[
H^0(G/P,\mathcal O(m))
\]
shows that the projective degree is
\[
(\dim X_n)!
\prod_{\alpha\in\Phi^+\setminus\Phi_P^+}
\frac{\langle\omega_2,\alpha\rangle}
{\langle\rho,\alpha\rangle}.
\]
All numerator factors equal \(1\), except for \(e_1+e_2\), which contributes \(2\).

The denominator is
\[
(2n-3)
\prod_{j=3}^{n}
(j-1)(j-2)(2n-j-1)(2n-j-2).
\]
Rearranging the four factorial products gives
\[
(2n-3)
\frac{(n-1)!(n-2)!(2n-4)!(2n-5)!}
{(n-2)!(n-3)!}
=
(n-1)(n-2)(2n-3)!(2n-5)!.
\]
Therefore
\[
\deg X_n=
\frac{2(4n-7)!}
{(n-1)(n-2)(2n-3)!(2n-5)!}.
\]

The Schubert cell decomposition gives the Euler characteristic as the number of Weyl-group cosets. Since
\[
|W(D_n)|=2^{n-1}n!,
\]
while the Levi Weyl group is
\[
W(A_1)\times W(D_{n-2}),
\]
we obtain
\[
\chi_{\mathrm{top}}(X_n)
=
\frac{2^{n-1}n!}
{2\cdot2^{n-3}(n-2)!}
=
2n(n-1).
\]

Taking the quotient of the degree formula at \(n+1\) and \(n\) yields
\[
\frac{\deg X_{n+1}}{\deg X_n}
=
\frac{2(4n-5)(4n-3)}{n(2n-1)}.
\]
Also
\[
\frac{\chi_{\mathrm{top}}(X_{n+1})}
{\chi_{\mathrm{top}}(X_n)}
=
\frac{n+1}{n-1}.
\]
Thus the normalized degree-to-Euler ratio grows exactly when
\[
2(4n-5)(4n-3)(n-1)
>
n(2n-1)(n+1).
\]
The difference between the left and right sides is
\[
30n^3-97n^2+95n-30.
\]
For \(n\ge4\),
\[
30n^3-97n^2+95n-30
=
n^2(30n-97)+95n-30
>0.
\]
Since
\[
\deg X_4=168,\qquad
\chi_{\mathrm{top}}(X_4)=24,
\]
the strict inequality follows for every \(n\ge4\).

## Verification
The bundled checker evaluates the factorial degree formula and Weyl-order Euler formula for
\[
4\le n\le200.
\]
It verifies integrality, the exact consecutive degree recurrence, strict growth of the normalized ratio, and the base value
\[
(\deg X_4,\chi_{\mathrm{top}}(X_4))=(168,24).
\]

It separately reconstructs the Weyl product denominator from the individual complementary type-\(D_n\) roots and checks equality with the closed factorial denominator.

These finite checks are regression evidence only. The all-\(n\) proof is the Weyl-product calculation and polynomial inequality above.

## Relationship to prior work
Buch, Kresch, and Tamvakis develop the classical and quantum Schubert calculus of even orthogonal Grassmannians, including the Schubert-cell indexing and the role of the special Chern classes. Their archival preprint is classified primarily under MSC \(14N15\). Its full text contains no topological Euler-characteristic comparison and no projective-degree-versus-Euler phase statement.

Pragacz and Ratajski give a Pieri-type formula for even orthogonal Grassmannians and classify the subject under MSC \(14M15\). This supplies an earlier Schubert-calculus framework for the same family.

The degree formula used here is reconstructed directly from the type-\(D_n\) Weyl dimension product rather than imported as a numerical table. Targeted searches for \(\operatorname{OG}(2,2n)\), Plücker degree, Euler characteristic, and the consecutive ratio did not locate the displayed comparison theorem.

Related degree–Euler results for symplectic Grassmannians and maximal spinor varieties concern different homogeneous spaces and do not imply the even-orthogonal two-plane formula.

## Limitations
The theorem treats only the two-plane family \(\operatorname{OG}(2,2n)\), not arbitrary \(\operatorname{OG}(k,2n)\).

It compares only projective degree and ordinary topological Euler characteristic. No claim is made about Betti-number domination, motives, Hodge structures, or analogous inequalities in positive characteristic.

The Weyl-product calculation is elementary once the correct homogeneous data are fixed, so an equivalent unindexed observation remains a residual originality risk.

## References
Anders S. Buch, Andrew Kresch, and Harry Tamvakis, *A Giambelli formula for even orthogonal Grassmannians*, arXiv:1109.6669, first submitted 29 September 2011; *Journal für die reine und angewandte Mathematik* 708 (2015), 17--48, DOI 10.1515/crelle-2013-0071.

Piotr Pragacz and Jan Ratajski, *A Pieri-type formula for even orthogonal Grassmannians*, *Fundamenta Mathematicae* 178 (2003), 49--96, DOI 10.4064/fm178-1-2.
