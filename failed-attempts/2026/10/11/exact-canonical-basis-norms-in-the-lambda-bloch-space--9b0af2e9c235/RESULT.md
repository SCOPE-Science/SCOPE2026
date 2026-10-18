# Exact canonical-basis norms in the \(\lambda\)-Bloch space

## Finding

Fix
\[
\lambda>0.
\]
For the canonical \(\lambda\)-analytic basis
\[
\phi_n^\lambda(z)
=
\epsilon_n
\sum_{j=0}^n
\frac{(\lambda)_j(\lambda+1)_{n-j}}
{j!(n-j)!}
\overline z^{\,j}z^{\,n-j},
\qquad
\epsilon_n
=
\sqrt{\frac{n!}{(2\lambda+1)_n}},
\]
the exact norm in the recently introduced \(\lambda\)-Bloch space is
\[
\|\phi_0^\lambda\|_{\mathfrak B_\lambda}
=
1+\lambda
\]
and, for every integer
\[
n\ge1,
\]
\[
\|\phi_n^\lambda\|_{\mathfrak B_\lambda}
=
(n+\lambda+1)\epsilon_n^{-1}
\frac{2}{n+2}
\left(\frac{n}{n+2}\right)^{n/2}.
\]

For
\[
n\ge1,
\]
this norm is attained at the positive real point
\[
r_n
=
\sqrt{\frac{n}{n+2}}.
\]
In particular,
\[
1-r_n\sim\frac1n.
\]

The exact formula gives the large-degree law
\[
\|\phi_n^\lambda\|_{\mathfrak B_\lambda}
\sim
\frac{2}{e\sqrt{\Gamma(2\lambda+1)}}\,
n^\lambda.
\]
Thus the canonical orthonormal basis of
\[
H_\lambda^2(\mathbb D)
\]
has precisely polynomial \(\lambda\)-Bloch norm growth, and the reflection parameter affects the amplitude through \(n^\lambda\) while the maximizing radial scale is universal.

## Assumptions and scope

The source assumes
\[
\lambda>0
\]
after introducing the general \(\lambda\)-analytic formalism. The \(\lambda\)-Bloch norm is
\[
\|f\|_{\mathfrak B_\lambda}
=
\sup_{z\in\mathbb D}
(1-|z|^2)
\left|
D_z\!\left(zf(z)\right)
\right|.
\]

The functions
\[
\phi_n^\lambda
\]
are the canonical basis appearing in the source's \(\lambda\)-analytic expansion. They form an orthonormal basis of
\[
H_\lambda^2(\mathbb D).
\]

The claim concerns exact norms of these individual basis vectors and their large-degree behavior. It does not assert unconditionality of the basis in \(\mathfrak B_\lambda\), characterize arbitrary coefficient sequences in \(\mathfrak B_\lambda\), or compute norms of general linear combinations.

## Proof

The source records the operator identity
\[
D_z\!\left(z\phi_{n-1}^\lambda(z)\right)
=
(n+\lambda)\phi_{n-1}^\lambda(z),
\qquad
n\ge1.
\]
After shifting the index,
\[
D_z\!\left(z\phi_n^\lambda(z)\right)
=
(n+\lambda+1)\phi_n^\lambda(z),
\qquad
n\ge0.
\]
Therefore
\[
\|\phi_n^\lambda\|_{\mathfrak B_\lambda}
=
(n+\lambda+1)
\sup_{z\in\mathbb D}
(1-|z|^2)|\phi_n^\lambda(z)|.
\]

The prior \(\lambda\)-analytic theory, reproduced in the source, gives
\[
|\phi_n^\lambda(z)|
\le
\epsilon_n^{-1}|z|^n.
\]
For positive real
\[
z=r\in(0,1),
\]
the defining series has no angular phases, so
\[
\phi_n^\lambda(r)
=
\epsilon_n r^n
\sum_{j=0}^n
\frac{(\lambda)_j(\lambda+1)_{n-j}}
{j!(n-j)!}.
\]
The coefficient convolution is exact. Indeed,
\[
(1-t)^{-\lambda}
(1-t)^{-(\lambda+1)}
=
(1-t)^{-(2\lambda+1)}.
\]
Comparing the coefficient of \(t^n\),
\[
\sum_{j=0}^n
\frac{(\lambda)_j(\lambda+1)_{n-j}}
{j!(n-j)!}
=
\frac{(2\lambda+1)_n}{n!}
=
\epsilon_n^{-2}.
\]
Hence
\[
\phi_n^\lambda(r)
=
\epsilon_n^{-1}r^n.
\]
The source pointwise upper bound is therefore sharp on every positive real radius.

It follows that, for
\[
n\ge1,
\]
\[
\|\phi_n^\lambda\|_{\mathfrak B_\lambda}
=
(n+\lambda+1)\epsilon_n^{-1}
\max_{0\le r<1}
(1-r^2)r^n.
\]
Set
\[
g_n(r)=(1-r^2)r^n.
\]
Then
\[
g_n'(r)
=
r^{n-1}
\left(
n-(n+2)r^2
\right).
\]
The unique interior radial maximizer is
\[
r_n^2=\frac{n}{n+2},
\]
and
\[
g_n(r_n)
=
\frac{2}{n+2}
\left(
\frac{n}{n+2}
\right)^{n/2}.
\]
This proves the exact norm formula and its attainment at
\[
z=r_n.
\]

For
\[
n=0,
\]
one has
\[
\phi_0^\lambda\equiv1
\]
and
\[
D_z(z\phi_0^\lambda)
=
(1+\lambda)\phi_0^\lambda,
\]
so
\[
\|\phi_0^\lambda\|_{\mathfrak B_\lambda}
=
1+\lambda.
\]

Finally,
\[
\epsilon_n^{-1}
=
\sqrt{
\frac{\Gamma(n+2\lambda+1)}
{\Gamma(2\lambda+1)\Gamma(n+1)}
}
\sim
\frac{n^\lambda}{\sqrt{\Gamma(2\lambda+1)}}.
\]
Moreover,
\[
\frac{n+\lambda+1}{n+2}\to1
\]
and
\[
\left(
\frac{n}{n+2}
\right)^{n/2}
\to e^{-1}.
\]
Therefore
\[
\|\phi_n^\lambda\|_{\mathfrak B_\lambda}
\sim
\frac{2}{e\sqrt{\Gamma(2\lambda+1)}}
n^\lambda.
\]

## Verification

The proof was replayed from the source's actual basis formula, pointwise bound, \(\lambda\)-Bloch norm definition, and Dunkl operator identity.

The only additional identity needed for sharpness is the Pochhammer convolution
\[
\sum_{j=0}^n
\frac{(\lambda)_j(\lambda+1)_{n-j}}
{j!(n-j)!}
=
\frac{(2\lambda+1)_n}{n!},
\]
which follows directly by coefficient extraction from
\[
(1-t)^{-\lambda}
(1-t)^{-(\lambda+1)}.
\]

The one-variable optimization is exact:
\[
\frac{d}{dr}
\left[
(1-r^2)r^n
\right]
=
r^{n-1}
\left[
n-(n+2)r^2
\right].
\]
Thus no angular sampling or numerical maximization is used to establish the norm.

As an independent consistency check, direct evaluation of the finite defining sums for several positive \(\lambda\) and small degrees agrees with the closed formula, and angular samples stay below the real-axis value. Those finite checks are not used as proof.

## Relationship to prior work

The 2026 source introduces the \(\lambda\)-Bloch space and defines its norm through
\[
(1-|z|^2)
D_z(zf(z)).
\]
It also reproduces the canonical basis, the pointwise bound
\[
|\phi_n^\lambda(z)|
\le
\epsilon_n^{-1}|z|^n,
\]
and the exact Dunkl identity for
\[
D_z(z\phi_n^\lambda).
\]
In the inspected sections, it uses these ingredients for completeness, growth, higher-operator characterizations, and an explicit unbounded Bloch function, but it does not state the exact individual basis norms above.

The 2022 preprint later published in the Journal of Approximation Theory develops the associated Hardy and Bergman spaces. It records the same canonical basis bound and Dunkl identity but predates the definition of the \(\lambda\)-Bloch space and therefore does not provide the present norm formula.

The exact norm is not merely the source's upper estimate: its sharpness requires identifying equality of the angular bound on the real axis and then solving the radial extremal problem. Targeted searches for the exact basis norm, its equivalent extremal formula, and the \(n^\lambda\) leading constant did not locate an implication-equivalent published result.

## Limitations

The formula is for a single canonical basis vector. Norms of sums can involve angular cancellation and are not determined by the individual values.

The claim is stated for
\[
\lambda>0,
\]
matching the nonclassical regime used throughout the source after its introductory definitions. At
\[
\lambda=0,
\]
the construction reduces to the classical analytic Bloch setting, but that endpoint is not needed for the result.

The originality comparison covered the recent source around its norm definition and basis machinery, the principal earlier Hardy/Bergman source, targeted source-specific searches, and semantic published-finding searches. An older equivalent calculation expressed without \(\lambda\)-Bloch terminology remains a residual literature risk.

## References

1. H. Wei, K. Qian, Z. Li, and Y. Niu, *A Bloch type space associated with \(\lambda\)-analytic functions*, arXiv:2603.25012v1, first posted 26 March 2026.
2. Z. Li and H. Wei, *Some aspects of the Bergman and Hardy spaces associated with a class of generalized analytic functions*, Journal of Approximation Theory 301 (2024), 106044, DOI: 10.1016/j.jat.2024.106044.
