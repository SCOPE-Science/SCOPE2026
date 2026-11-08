# Sharp sixth moments and spectral stability for quaternionic Stiefel linear statistics

## Finding

Let \(n\ge2\) and \(1\le r\le n\). Let \(W\in\mathbb H^{n\times r}\) be a Haar-uniform quaternionic orthonormal \(r\)-frame, so \(W^*W=I_r\). For every nonzero \(A\in\mathbb H^{n\times r}\), define its real linear statistic
\[
F_A(W)=\operatorname{Re}\operatorname{tr}_{\mathbb H}(A^*W),\qquad
p_j=\operatorname{tr}_{\mathbb H}((A^*A)^j),\qquad
\rho_j=p_j/p_1^j\quad(j=2,3).
\]
Here the trace of a quaternionic Hermitian matrix is the real sum of its eigenvalues, counted once per quaternionic dimension. Then \(\mathbb EF_A^2=p_1/(4n)\). The normalized sixth moment \(K_{n,r}(A)=\mathbb EF_A^6/(\mathbb EF_A^2)^3\) equals
\[
K_{2,r}(A)=20-12\rho_2\quad(n=2),
\]
and, for every \(n\ge3\),
\[
K_{n,r}(A)=C_n\bigl(2n^2-3n-1-3(n-1)\rho_2+2\rho_3\bigr),\qquad
C_n=\frac{15n^2}{(n-2)(n-1)(n+1)(2n+1)}.
\]
It has the complete sharp range
\[
\frac{30n^2}{(n+1)(2n+1)}\le K_{n,r}(A)\le
\begin{cases}
20-12/r,&n=2,\\
C_n\bigl(2n^2-3n-1-3(n-1)/r+2/r^2\bigr),&n\ge3.
\end{cases}
\]
The minimum is attained precisely by quaternionic rank-one matrices. The maximum is attained precisely when all \(r\) quaternionic singular values of \(A\) are equal and nonzero, equivalently \(A^*A=(p_1/r)I_r\). When \(r=1\) the two endpoints coincide; otherwise all intermediate ratios occur. In the full-frame case \(r=n\), the sharp maximum equals \(14\) for \(n=2\) and \(15\) for \(n\ge3\), displaying the small-dimension symplectic trace transition.

More precisely, let \(t_1,\dots,t_r\ge0\) be the normalized squared quaternionic singular values of \(A\), with \(\sum_i t_i=1\). For \(n\ge3\) there are two *exact*, nonnegative deficit identities:
\[
K_{n,r}(A)-K_{n,r}^{\min}
=C_n\sum_{i=1}^r t_i(1-t_i)\bigl(3(n-1)-2(1+t_i)\bigr),
\]
\[
K_{n,r}^{\max}-K_{n,r}(A)
=C_n\sum_{i=1}^r\bigl(t_i-1/r\bigr)^2
\bigl(3(n-1)-2(t_i+2/r)\bigr).
\]
For \(n=2\) their right sides are respectively \(12\sum_i t_i(1-t_i)\) and \(12\sum_i(t_i-1/r)^2\). In all admissible cases, the indicated factors are strictly positive wherever their accompanying energy terms can be nonzero.

Finally, the \(4nr\)-dimensional real space \(X_{n,r}=\{F_A:A\in\mathbb H^{n\times r}\}\), equipped with the \(L^6\) norm under Haar Stiefel measure, has exact Euclidean Banach–Mazur distance
\[
d_{\mathrm{BM}}\bigl(X_{n,r},\ell_2^{4nr}(\mathbb R)\bigr)^6
=K_{n,r}^{\max}/K_{n,r}^{\min}.
\]
Its optimal Euclidean comparator is the quaternionic Hilbert–Schmidt norm \(\sqrt{p_1}\), up to scaling. In particular, the distance is \(1\) for \(r=1\), is \((7/4)^{1/6}\) for \((n,r)=(2,2)\), and has sixth power \((n+1)(2n+1)/(2n^2)\) for \(n=r\ge3\).

## Assumptions and scope

The underlying field is the real quaternion division algebra \(\mathbb H\), with conjugate transpose \(\cdot^*\). Quaternionic Haar Stiefel measure is the pushforward of Haar probability on compact \(\operatorname{Sp}(n)\) to its first \(r\) columns. It is invariant under left \(\operatorname{Sp}(n)\) and right \(\operatorname{Sp}(r)\), and the real trace \(\operatorname{Re}\operatorname{tr}_{\mathbb H}\) is cyclic. The variables \(A,W\) have the same \(n\times r\) dimensions; all norms are taken in real \(L^p\), and all moment ratios concern nonzero coefficients. We include the boundary \(n=2\) explicitly instead of using a formula with denominator \(n-2\).

## Proof

**1. Quaternionic singular-value reduction.** By quaternionic singular-value decomposition and left/right Haar invariance, \(F_A\) has the same distribution as \(\sum_{i=1}^r s_iX_i\), where \(s_i\ge0\) are the singular values and \(X_i=\operatorname{Re}U_{ii}\) for a Haar-uniform \(U\in\operatorname{Sp}(n)\). Independent multiplication of any row by \(-1\) forces vanishing of mixed moments with an odd exponent in any individual \(X_i\). The first column of \(U\) is uniform on the real sphere of dimension \(d=4n\), giving \(\mathbb EX_1^2=1/d\) and
\[
a=\mathbb EX_1^6=\frac{15}{d(d+2)(d+4)}.
\]

**2. The mixed fourth–second moment.** Conditional on the first quaternionic column \(u\), the second column is uniform on the quaternionic orthogonal complement \(u^\perp\), of real dimension \(4(n-1)\). Its real inner product with the second standard quaternionic basis vector therefore has conditional second moment \((1-|u_2|^2)/(4(n-1))\). Uniform-sphere monomials give
\[
\mathbb EX_1^4=\frac3{d(d+2)},\qquad
\mathbb E\bigl[X_1^4|u_2|^2\bigr]=\frac{12}{d(d+2)(d+4)}.
\]
Consequently,
\[
b=\mathbb EX_1^4X_2^2=\frac3{4(n-1)(d+2)(d+4)}.
\]

**3. Three-index mixed moment and the exceptional dimension.** Set \(c=\mathbb EX_1^2X_2^2X_3^2\) when \(n\ge3\). Rains's symplectic trace-moment theorem counts fixed-point-free involutions of six symbols subject to a longest-decreasing-subsequence constraint. All \(15\) involutions are admissible for \(n\ge3\) (complex symplectic dimension \(2n\ge6\)); exactly \(14\) are admissible for \(n=2\) (dimension four). Since \(\chi(U)=\operatorname{Tr}_{\mathbb C}U=2\sum_iX_i\), we have for \(n\ge3\)
\[
\frac{15}{64}=\mathbb E\bigl(\sum_{i=1}^nX_i\bigr)^6
=na+15n(n-1)b+15n(n-1)(n-2)c.
\]
Solving gives
\[
c=\frac{2n^2-3n-1}{64n(n-2)(n-1)(n+1)(2n+1)}.
\]
The \(n=2\) calculation uses only \(a,b\), with the \(14/64\) trace check. A polynomial expansion, using \(p_j=\sum_i s_i^{2j}\), now yields
\[
\mathbb EF_A^6
=a p_3+15b(p_1p_2-p_3)+15c(p_1^3-3p_1p_2+2p_3),\qquad n\ge3,
\]
and \(\mathbb EF_A^6=a p_3+15b(p_1p_2-p_3)\) for \(n=2\). This is the displayed normalized formula after dividing by \((p_1/(4n))^3\).

**4. Both spectral inequalities and complete equality cases.** Write \(t_i=s_i^2/p_1\). Direct expansion of \(\rho_2=\sum_it_i^2\) and \(\rho_3=\sum_it_i^3\), using \(\sum_it_i=1\), gives the two deficit identities in the finding. For \(n\ge3\), the minimum-deficit bracket is at least \(3(n-1)-4=3n-7>0\). For the maximum-deficit bracket and \(r\ge2\), it is at least \(3(n-1)-2(1+2/r)\ge3n-7>0\). Thus equality at the lower endpoint requires exactly one \(t_i=1\); equality at the upper requires \(t_i=1/r\) for every \(i\). The \(n=2\) formulas have the same equality implications. The unit sphere in the real coefficient space of dimension \(4nr\ge8\) is path connected, and the continuous moment quotient therefore fills the interval between the attained endpoints.

**5. Exact Euclidean distance.** The compact left/right quaternionic unitary action preserves the \(L^6\) norm and acts irreducibly on the real Hilbert–Schmidt coefficient space in the sense that every invariant real positive quadratic form is a scalar multiple of \(p_1\). One direct way to see this is to average over independent quaternionic unit phases in individual rows and columns, which removes distinct-coordinate cross terms, and then over row and column permutations, which makes all coordinate coefficients equal. For any proposed Euclidean comparator \(H\) with \(aH\le\|F_A\|_6\le bH\), average \(H^2\) over this compact action: the resulting invariant quadratic form \(\overline{H^2}\) satisfies \(\|F_A\|_6^2/b^2\le\overline{H^2}(A)\le\|F_A\|_6^2/a^2\). The ratio \(b/a\) therefore cannot improve on the Hilbert–Schmidt comparator. Its distortion is exactly the sixth root of the normalized moment endpoint ratio. The displayed specializations follow by substitution.

## Verification

The included standalone `quaternionic_moment_checker.py` uses exact rational arithmetic to verify the fixed-point-free involution counts \(14,15\), the sixth-moment expansion, the two spectral deficit identities, equality witnesses, and the full-rank trace specializations across a range of dimensions and ranks. It separately samples genuinely quaternionic Haar frames by Gaussian quaternionic Gram–Schmidt to corroborate the moment values. Run with `python quaternionic_moment_checker.py`; its only dependency is the Python standard library. The finite numerical tests are diagnostic: the all-dimensional theorem depends on the argument above and the cited representation-theoretic trace identity.

## Relationship to prior work

Rains's 1998 Theorem 3.4 proves a combinatorial formula for symplectic **trace** moments, from which the exceptional \(14\) versus \(15\) sixth trace moments are obtained. It does not classify arbitrary rectangular quaternionic matrix coefficient functionals, their rank-dependent six-moment extrema, or their Euclidean norm distortion. Collins and Śniady's 2004 symplectic Weingarten integration gives a general method to evaluate compact symplectic matrix-entry moments, but does not present these specialized sharp optimization and two-sided stability results. Tropp's 2011 Stiefel comparison principle treats real frames through Gaussian bounds, not exact quaternionic sixth-moment extrema. The present argument combines conditional quaternionic-sphere moments with the symplectic trace result to give a complete sharp classification. General Weingarten calculus can implicitly recover the moment coefficients; the distinction claimed is the explicit spectral inequality and its equality geometry, not a new integration formalism.

## Limitations

The statement is restricted to real-valued quaternionic trace-linear statistics on Haar-uniform quaternionic Stiefel frames, their sixth moments and real Banach–Mazur distance. It does not address general distributions, higher even moments, complex-valued quaternionic trace conventions, nonuniform Stiefel weights or arbitrary representations. The algebraic identities and finite exact checks are not independent validation; the external independent audit has not been performed. An unindexed equivalent spectral inequality or direct corollary of a specialized symplectic moment inequality cannot be excluded completely by the literature searches.

## References

1. E. M. Rains, *Increasing Subsequences and the Classical Groups*, Electronic Journal of Combinatorics **5** (1998), #R12, Theorem 3.4. Published 1998-01-30. DOI: `10.37236/1350`.
2. B. Collins and P. Śniady, *Integration with respect to the Haar measure on unitary, orthogonal and symplectic group*, arXiv:`math-ph/0402073` (first version 2004-02-26), especially Section 4.
3. J. A. Tropp, *A Comparison Principle for Functions of a Uniformly Random Subspace*, arXiv:`1102.0534` (2011), theorem and real Stiefel setup.
