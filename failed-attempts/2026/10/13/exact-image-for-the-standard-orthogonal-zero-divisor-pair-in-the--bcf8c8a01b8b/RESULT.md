# Exact image for the standard orthogonal zero-divisor pair in the split octonion algebra
## Finding
Let \(F\) be a field with \(\operatorname{char}F\ne2\). Use the standard split-octonion model
\[
\mathcal O=M_2(F)\oplus M_2(F)\omega,\qquad \omega^2=1,
\]
with
\[
(a+x\omega)(b+y\omega)=(ab+\overline yx)+(ya+x\overline b)\omega,
\]
where \(\overline X=\operatorname{tr}(X)I-X\). Put \(p_0=E_{11}\) and \(n_0=E_{12}\), and define
\[
\Phi(x,y)=p_0(xy)-n_0(yx).
\]
Then
\[
\operatorname{Im}\Phi=(Fp_0+Fn_0)\oplus M_2(F)\omega.
\]
Thus the image is a six-dimensional vector subspace. Moreover, one fixed slice already fills it: if \(x_0=E_{11}+E_{21}\), then
\[
\{\Phi(x_0,y):y\in\mathcal O\}=(Fp_0+Fn_0)\oplus M_2(F)\omega.
\]

## Assumptions and scope
The field satisfies \(\operatorname{char}F\ne2\), matching the standing hypothesis of the motivating octonion result. The claim concerns the standard pair \(p_0,n_0\) fixed in the usual split model; it does not assert that every linearly independent pair of orthogonal zero divisors has a linear image.

The matrices \(p_0\) and \(n_0\) are linearly independent nonzero zero divisors and satisfy \(N(p_0,n_0)=0\), because \(\det p_0=\det n_0=\det(p_0+n_0)=0\). Hence this pair lies in case (iii) of the recent generalized-commutator theorem, the case for which that theorem determines only the dimension of the linear span of the image.

## Proof
Write \(U=Fp_0+Fn_0\) and \(W=U\oplus M_2(F)\omega\). For \(z=a+b\omega\), direct use of the Cayley--Dickson multiplication gives
\[
p_0z=p_0a+(bp_0)\omega,\qquad n_0z=n_0a+(bn_0)\omega.
\]
Both \(p_0a\) and \(n_0a\) have zero second row, so their quaternion parts lie in \(U\). Also \(M_2(F)p_0+M_2(F)n_0=M_2(F)\). Therefore
\[
p_0\mathcal O+n_0\mathcal O=U\oplus M_2(F)\omega=W.
\]
Since every value \(p_0(xy)-n_0(yx)\) lies in \(p_0\mathcal O+n_0\mathcal O\), this proves \(\operatorname{Im}\Phi\subseteq W\).

For the reverse inclusion, fix \(x_0=E_{11}+E_{21}\). Write
\[
y=A+B\omega,
\]
where
\[
A=\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix},\qquad
B=\begin{pmatrix}b_{11}&b_{12}\\b_{21}&b_{22}\end{pmatrix}.
\]
A direct multiplication gives
\[
\Phi(x_0,y)=
(a_{11}-a_{21}-a_{22})E_{11}+a_{12}E_{12}
+
\begin{pmatrix}
b_{11}+b_{12}&b_{12}\\
b_{21}+b_{22}&b_{22}
\end{pmatrix}\omega.
\]
The first two displayed coefficients are arbitrary, and the linear transformation
\[
(b_{11},b_{12},b_{21},b_{22})\longmapsto
(b_{11}+b_{12},b_{12},b_{21}+b_{22},b_{22})
\]
has determinant \(1\). Hence \(y\mapsto\Phi(x_0,y)\) is onto \(W\), so \(W\subseteq\operatorname{Im}\Phi\). The two inclusions prove the claim.

## Verification
The accompanying `verify.py` reconstructs the Cayley--Dickson product symbolically. It verifies that the quaternion part of a general value of \(\Phi\) has zero second row, and that the matrix of the fixed slice \(y\mapsto\Phi(E_{11}+E_{21},y)\) in the ordered basis
\[
(E_{11},E_{12},E_{21},E_{22},E_{11}\omega,E_{12}\omega,E_{21}\omega,E_{22}\omega)
\]
has rank \(6\). A six-by-six minor has determinant \(1\), so the rank assertion is field-independent. The script also verifies \(N(p_0,n_0)=0\) in the matrix model and terminates with `VERIFY_OK`.

## Relationship to prior work
De Mello and Saini study \(A(xy)-B(yx)\) on octonion algebras. Their Theorem 1.1 states that for linearly independent nonzero zero divisors with \(N(A,B)=0\), the linear span of the image has dimension \(6\), and explicitly leaves open whether the image itself is a vector subspace in that case. The same paper fixes \(p_0=E_{11}\) and \(n_0=E_{12}\) as standard elements in its split-octonion model. The result above identifies the exact image for this canonical pair and shows that a single linear slice already attains the full six-dimensional span.

Panja, Saini, and Singh prove that \(Axy-Byx\) has vector-space image on \(M_2(K)\) over an algebraically closed field. That associative matrix result does not imply the present octonion statement, because octonion multiplication is nonassociative and the unresolved case in the recent octonion theorem occurs only in the split octonion setting.

## Limitations
No claim is made for arbitrary pairs in case (iii), nor is an orbit classification of such pairs asserted. The characteristic-two case is outside the standing hypotheses of the motivating theorem. The proof is exact and symbolic; finite-field enumeration is not used to infer the result.

## References
1. T. Castilho de Mello and P. Saini, *Generalized commutator on octonion algebra*, arXiv:2610.04466v1, 2026.
2. S. Panja, P. Saini, and A. Singh, *Images of polynomial maps with constants*, arXiv:2312.13865v1; Mathematika 71 (2025), Paper e70031.
