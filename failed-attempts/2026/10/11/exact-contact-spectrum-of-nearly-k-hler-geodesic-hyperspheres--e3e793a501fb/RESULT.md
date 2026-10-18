# Exact contact spectrum of nearly Kähler geodesic hyperspheres

## Finding

Let
\[
M_r\subset S^6,\qquad 0<r<\pi,
\]
be the geodesic hypersphere of radius \(r\) in the standard unit nearly Kähler six-sphere. Let
\[
\xi=-JN,\qquad \eta=g(\,\cdot\,,\xi),\qquad \mathcal D=\ker\eta,
\]
and let \(\phi\) be the canonical induced almost-contact tensor. Write
\[
G_NX=G(X,N).
\]

Define an endomorphism \(\Psi_r\) by
\[
\Psi_r\xi=0
\]
and, on \(\mathcal D\),
\[
\boxed{
\Psi_r=\cos r\,\phi-\sin r\,G_N.
}
\]
Then \(\Psi_r\) is an orthogonal complex structure on \(\mathcal D\), and
\[
\boxed{
d\eta(X,Y)=2\csc r\,g(\Psi_rX,Y)
}
\]
for all tangent vectors \(X,Y\).

Consequently, for every \(0<r<\pi\),

\[
\boxed{\eta\ \text{is a contact form},}
\]
its Reeb vector field in the contact sense is exactly \(\xi\), the two horizontal singular values of \(d\eta\) are both
\[
\boxed{2\csc r,}
\]
and
\[
\boxed{
\left\|\eta\wedge(d\eta)^2\right\|=8\csc^2r.
}
\]

Thus the explicit geodesic-hypersphere family has maximal horizontal rank everywhere. The recent quantitative estimate determines its horizontal norm
\[
\|d\eta|_{\Lambda^2\mathcal D}\|^2=8\csc^2r;
\]
the result here upgrades that scalar norm to the full singular-value and contact-volume description.

## Assumptions and scope

The ambient sphere is the unit round \(S^6\) with its standard octonionic nearly Kähler structure, of constant type \(1\).

The normal orientation is the one for which the geodesic hypersphere has shape operator
\[
A=(\cot r)I.
\]
Changing the normal changes \(\xi\) and \(\eta\) by sign but does not affect contactness or the displayed absolute density.

The norm
\[
\|\eta\wedge(d\eta)^2\|
\]
is the pointwise norm with respect to the induced metric. No choice of orientation is needed for this absolute statement.

The theorem concerns the explicit totally umbilical family. It does not assert that the canonical Reeb form is contact on every real hypersurface of every strict nearly Kähler six-manifold.

## Proof

For a geodesic hypersphere, the shape operator is
\[
A=(\cot r)I.
\]
The general hypersurface identity is
\[
d\eta(X,Y)
=
g((\phi A+A\phi)X,Y)
-
2g(G_NX,Y).
\]
Hence
\[
d\eta(X,Y)
=
2g((\cot r\,\phi-G_N)X,Y).
\]

The same identity holds without restricting \(X,Y\) to \(\mathcal D\). We first check its vertical part. Since
\[
\phi\xi=0,
\]
the shape contribution vanishes on \(\xi\). Also
\[
\xi=-JN.
\]
Using skew-symmetry of \(G\) and
\[
G(X,JY)=-JG(X,Y),
\]
we get
\[
G_N\xi
=
G(\xi,N)
=
-G(N,\xi)
=
G(N,JN)
=
0.
\]
Thus
\[
d\eta(\xi,\cdot)=0.
\]

On \(\mathcal D\), the strict nearly Kähler identities give
\[
\phi^2=-I,
\qquad
G_N^2=-I,
\qquad
G_N\phi=-\phi G_N.
\]
Therefore
\[
\begin{aligned}
\Psi_r^2
&=
\cos^2r\,\phi^2
+\sin^2r\,G_N^2
-\sin r\cos r\,(\phi G_N+G_N\phi)\\
&=-I.
\end{aligned}
\]
Both \(\phi\) and \(G_N\) are skew-adjoint on \(\mathcal D\), so \(\Psi_r\) is skew-adjoint. Together with
\[
\Psi_r^2=-I,
\]
this implies that \(\Psi_r\) is orthogonal.

Since
\[
\cot r\,\phi-G_N
=
\csc r\,(\cos r\,\phi-\sin r\,G_N)
=
\csc r\,\Psi_r,
\]
we obtain
\[
d\eta(X,Y)
=
2\csc r\,g(\Psi_rX,Y)
\]
on \(\mathcal D\), and the preceding vertical calculation extends the formula to all tangent vectors.

Choose an orthonormal basis
\[
e_1,\Psi_re_1,e_2,\Psi_re_2
\]
of \(\mathcal D\). In this basis, the horizontal two-form has two equal skew singular values
\[
2\csc r.
\]
In particular it is nondegenerate on the four-dimensional distribution, so
\[
\eta\wedge(d\eta)^2\ne0.
\]
Moreover, if
\[
\Omega_r(X,Y)=g(\Psi_rX,Y),
\]
then
\[
\|\Omega_r\wedge\Omega_r\|=2.
\]
Since
\[
d\eta=2\csc r\,\Omega_r,
\]
we obtain
\[
\left\|\eta\wedge(d\eta)^2\right\|
=
4\csc^2r\,\|\Omega_r\wedge\Omega_r\|
=
8\csc^2r.
\]

Finally, \(\eta(\xi)=1\) and
\[
d\eta(\xi,\cdot)=0,
\]
so \(\xi\) is the Reeb vector field in the contact-geometric sense.

## Verification

The bundled checker uses an explicit four-dimensional model of two anti-commuting orthogonal complex structures representing
\[
\phi|_{\mathcal D}
\quad\text{and}\quad
G_N|_{\mathcal D}.
\]
It verifies symbolically that
\[
K=2(k\phi-G_N)
\]
satisfies
\[
K^2=-4(k^2+1)I,
\]
so both skew singular values are
\[
2\sqrt{k^2+1}.
\]
After
\[
k=\cot r,
\]
this is
\[
2\csc r.
\]

The same matrix calculation gives Pfaffian magnitude
\[
4(k^2+1),
\]
hence the four-form coefficient
\[
8(k^2+1)=8\csc^2r.
\]
These exact identities agree with the published squared horizontal norm
\[
8\csc^2r.
\]

The checker verifies algebra only. The global contact conclusion follows from the analytic hypersurface identities proved above.

## Relationship to prior work

Lee and Lee prove the exact pointwise identity
\[
\|d\eta|_{\Lambda^2\mathcal D}\|^2
=
\frac12\|\phi B+B\phi\|_{\mathrm{HS}}^2+8\alpha
\]
for real hypersurfaces of strict nearly Kähler six-manifolds. For geodesic hyperspheres in the standard \(S^6\), they specialize it to
\[
\|d\eta|_{\Lambda^2\mathcal D}\|^2=8\csc^2r.
\]
They explicitly emphasize that a positive norm does not determine the rank of \(d\eta\) and therefore does not imply contactness.

Anarella and D'haene describe the full two-sphere of compatible almost-contact tensors with the same Reeb field on such hypersurfaces and classify several stronger structure classes. Their full preprint does not formulate the exterior derivative of the canonical Reeb form in the scaled fundamental-form identity above.

Earlier work records special almost-contact geometry on the equatorial \(S^5\), including a Sasakian distinguished structure. The theorem here is different in scope: it gives the canonical Reeb form's exact contact spectrum and contact volume for every radius, including all non-equatorial totally umbilical hyperspheres.

Targeted searches using the source identifier, geodesic-hypersphere terminology, contact-rank language, and the exact singular-value formula did not locate a prior all-radius statement.

## Limitations

The theorem is restricted to the standard nearly Kähler \(S^6\) and its geodesic hyperspheres.

It does not classify which arbitrary real hypersurfaces have contact canonical Reeb form.

The contact form \(\eta\) is canonical, while the tensor \(\Psi_r\) used to express \(d\eta\) is radius-dependent. For \(r\ne\pi/2\), this identity is not a claim that the original induced tensor \(\phi\) itself defines a contact metric structure with the same normalization.

## References

1. Jae Won Lee and Chul Woo Lee, *A Quantitative Reeb-Form Obstruction for Real Hypersurfaces of Strict Nearly Kähler Six-Manifolds*, arXiv:2610.00078v1, first submitted 5 September 2026.
2. Mateo Anarella and Marie D'haene, *Hypersurfaces of six-dimensional nearly Kähler manifolds*, arXiv:2507.22526v1, first submitted 30 July 2025.
