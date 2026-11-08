# Exact three-level singular spectrum of Fourier sampling on invertible Hermitian binary forms

## Finding

Let \(q\ge2\) be any prime power. Write \(V=\operatorname{Herm}_2(\mathbb F_{q^2})\), and \(S=\{X\in V:\det X\ne0\}\). For every nontrivial additive character \(\psi\colon\mathbb F_q\to\mathbb C\), let
\[
H_{X,Y}=\psi(\operatorname{tr}(XY)),\qquad X,Y\in S.
\]
The trace is the usual matrix trace; it belongs to \(\mathbb F_q\), because both factors are Hermitian. Put \(s=|S|=q(q-1)(q^2+1)\). Then the **complete singular spectrum** is
\[
\begin{array}{c|c}
\text{singular value}&\text{multiplicity}\\\hline
q^2&s-q^3+q^2-q+1\\
q^{3/2}&(q^2+1)(q-2)\\
q&q^2+1
\end{array}
\]
with zero multiplicities omitted (the middle level is absent at \(q=2\)). All occurring levels are positive, so \(H\) is invertible; its exact Euclidean condition number is \(\kappa_2(H)=q\).

## Assumptions and scope

The base field is an arbitrary finite field \(\mathbb F_q\), including characteristic two. Conjugation on \(\mathbb F_{q^2}\) is \(z\mapsto z^q\). Any \(X\in V\) is uniquely
\[
X=\begin{pmatrix}a&z\\z^q&b\end{pmatrix},\quad a,b\in\mathbb F_q,\ z\in\mathbb F_{q^2}.
\]
The determinant form is \(Q(X)=ab-z^{q+1}\). Its polar form is
\[
B(X,Y)=Q(X+Y)-Q(X)-Q(Y)=\operatorname{tr}(\operatorname{adj}(X)Y).
\]
The linear adjugate involution \(X\mapsto\operatorname{adj}(X)\) preserves determinant and permutes \(S\), so \((\psi(B(X,Y)))_{S,S}\) is obtained from \(H\) by permuting rows. It therefore has the same singular values.

## Proof

**1. The elliptic determinant cone.** Let \(C=\{X\in V:Q(X)=0\}\). If \(a\ne0\), for each \(a\) and \(z\) there is a unique \(b=z^{q+1}/a\); if \(a=0\), the zero determinant condition forces \(z=0\), leaving \(q\) choices for \(b\). Thus
\[
|C|=q^2(q-1)+q=q^3-q^2+q=:c.
\]
Every nonzero element of \(C\) lies on exactly one of \(r=(c-1)/(q-1)=q^2+1\) one-dimensional \(\mathbb F_q\)-subspaces (isotropic lines). Distinct isotropic lines are not perpendicular under \(B\). Indeed, for \(X\ne0\) with \(Q(X)=0\), a change of Hermitian coordinates or the decomposition \(Q=ab-N(z)\) shows that any \(B\)-orthogonal isotropic vector is proportional to \(X\): its class modulo \(\langle X\rangle\) lies in the anisotropic norm plane. Equivalently, the quadratic space is the orthogonal sum of one hyperbolic plane and an anisotropic norm plane, of Witt index one. This remains true in characteristic two.

**2. Fourier transform of the cone.** For \(t\ne0\), multiplication of two independent sums gives
\[
\sum_{a,b\in\mathbb F_q}\psi(tab)=q,\qquad
\sum_{z\in\mathbb F_{q^2}}\psi(-t z^{q+1})=1+(q+1)\sum_{u\in\mathbb F_q^\times}\psi(-tu)=-q.
\]
Consequently \(\sum_{X\in V}\psi(tQ(X))=-q^2\). Since \(B\) is the polar form of \(Q\), translation by \(t^{-1}Y\) gives, for every \(Y\in V\),
\[
\sum_{X\in V}\psi(tQ(X)+B(X,Y))=-q^2\psi(-Q(Y)/t).
\]
The indicator identity \(1_C(X)=q^{-1}\sum_{t\in\mathbb F_q}\psi(tQ(X))\) now yields
\[
\widehat{1_C}(Y)=\sum_{X\in C}\psi(B(X,Y))=
\begin{cases}
c,&Y=0,\\
-q(q-1),&Y\in C\setminus\{0\},\\
q,&Y\notin C.
\end{cases}
\]
No assumption about the parity of \(q\) enters these computations.

**3. Exact Gram spectrum on the cone.** Define \(F_C=(\psi(B(X,Y)))_{X,Y\in C}\). Character orthogonality gives
\[
(F_CF_C^*)_{X,Y}=\widehat{1_C}(X-Y)
=q^3\delta_{X,Y}+q-q^2 1_{\{B(X,Y)=0\}},\qquad X,Y\in C.
\]
Here we used \(Q(X-Y)=-B(X,Y)\) for \(X,Y\in C\), valid also in characteristic two. Let \(A=(1_{\{B(X,Y)=0\}})_{C,C}\) and \(J\) be the all-ones matrix. Then
\[
F_CF_C^*=q^3I+qJ-q^2A.
\]
Write \(h=q-1\). On the \(r\) disjoint nonzero isotropic lines, \(A\) has an all-ones block of size \(h\) on each line, zero blocks between different lines, and a first row and column of ones corresponding to \(0\). Thus:

* Functions summing to zero on each nonzero line and vanishing at \(0\) form a subspace of dimension \(r(h-1)=r(q-2)\); both \(J\) and \(A\) annihilate this subspace, giving squared singular value \(q^3\).
* Functions constant on each nonzero line, zero at \(0\), and with line constants summing to zero form a subspace of dimension \(r-1\). Here \(A\) acts by \(h\) and \(J\) by zero, giving \(q^3-q^2h=q^2\).
* The remaining two-dimensional space consists of functions constant at \(0\) and on all nonzero cone points. The vector \(1_C-q\delta_0\) is an eigenvector of \(F_C\) with eigenvalue \(-q^2\), by the three values in the preceding display; hence the Gram has an eigenvalue \(q^4\). The trace of the residual two-dimensional Gram block is \(q^4+q^2\) (equivalently, compute its displayed incidence block directly), so its other eigenvalue is \(q^2\).

Altogether
\[
\operatorname{spec}(F_CF_C^*)=
\{(q^4)^1,(q^3)^{r(q-2)},(q^2)^r\}.
\]
The multiplicities add to \(1+r(q-1)=c\).

**4. Complementary-block transfer.** The full Fourier matrix \(F=(\psi(B(X,Y)))_{X,Y\in V}\) satisfies \(FF^*=q^4I\), so \(U=q^{-2}F\) is unitary. Partition rows and columns into \(C\) and \(S=V\setminus C\). For every partitioned unitary matrix, the squared singular values of the diagonal blocks \(U_{CC}\) and \(U_{SS}\) that lie strictly between \(0\) and \(1\) agree, with multiplicities; zero singular values also agree up to the ambient dimension difference. This follows from \(U_{CC}^*U_{CC}+U_{SC}^*U_{SC}=I_C\) and \(U_{SS}U_{SS}^*+U_{SC}U_{SC}^*=I_S\): the positive spectra of the cross-block Gram matrices coincide. In our case \(U_{CC}\) has singular values \(1\) once, \(q^{-1/2}\) with multiplicity \(r(q-2)\), and \(q^{-1}\) with multiplicity \(r\), and no zero singular values. Thus \(U_{SS}\) has the same two levels below one, plus \(s-c+1\) copies of one. Multiplication by \(q^2\) and the adjugate row permutation give exactly the claimed three singular levels for \(H\). The largest is \(q^2\) and the smallest is \(q\), giving \(\kappa_2(H)=q\).

## Verification

The independent coordinate implementation `check_hermitian.py` builds an isometric elliptic quadratic model of the determinant form over fields of orders \(2,3,4,5\), forms the unnormalized complex Fourier matrix on the anisotropic complement, and numerically checks the entire singular multiset. It checks matrix sizes \(10,60,204,520\) and produces `HERMITIAN_FOURIER_SPECTRUM_PASS` on each case. Maximum observed numerical singular-value discrepancies were less than \(3\cdot 10^{-14}\). Run using Python 3 and NumPy as specified in `requirements.txt`. These are finite corroborations; the preceding character-sum and incidence arguments prove the statement for all prime powers.

## Relationship to prior work

Iosevich and Koh investigate Fourier extension bounds for finite-field nondegenerate quadratic surfaces; their main estimates concern normalized \(L^p\)-\(L^r\) inequalities, not the two-sided square restriction to the nonzero-determinant Hermitian locus. Stanton and Schmidt describe the Hermitian rank-metric translation association-scheme character sums, which include relevant cone Fourier coefficients. Their character formulas concern the full additive space and do not directly provide the exact spectrum of the principal Fourier submatrix indexed by invertible matrices. The additional projective line-incidence diagonalization and unitary complementary-block transfer determine that spectrum. A broader earlier scheme-theoretic consequence has not been ruled out exhaustively.

## Limitations

The classification is for Hermitian \(2\times2\) matrices only, but covers all finite fields, including characteristic two. It concerns complex linear reconstruction from a square Fourier sampling operator, not recovery from magnitudes, robustness under sample deletion, or larger Hermitian matrix ranks. The computer checks are finite and numerical; they are not the source of the universal proof. Historical priority remains subject to more exhaustive literature comparison.

## References

1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, first public version 2008-04-28, arXiv:0804.4505, https://arxiv.org/abs/0804.4505.
2. K.-U. Schmidt, *Hermitian rank distance codes*, first public version 2017-02-09, arXiv:1702.02793, https://arxiv.org/abs/1702.02793, especially Section 2 and its character eigenvalues.
3. D. Stanton, *A partially ordered set and \(q\)-Krawtchouk polynomials*, *J. Combin. Theory Ser. A* 30 (1981), 276–284, doi:10.1016/0097-3165(81)90023-6. The full text was not available for direct comparison.
