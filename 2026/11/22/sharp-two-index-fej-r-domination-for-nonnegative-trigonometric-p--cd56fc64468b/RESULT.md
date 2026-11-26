# Sharp two-index Fejér domination for nonnegative trigonometric polynomials

## Finding

Let \(m\ge 1\) and \(n\ge 0\) be integers, and write \(n=qm+r\), where \(q\ge 0\) and \(0\le r<m\). Set
\[
D=(q+2)m-r,\qquad C_{m,n}=\frac{(q+1)(q+2)m}{(q+2)m-r}.
\]
For every real-valued, nonnegative trigonometric polynomial \(T\) of degree at most \(n\), and every \(t\in\mathbb R\),
\[
\boxed{T(t)\le C_{m,n}(F_m*T)(t).}
\]
This constant is optimal. For nonzero \(T\), equality at \(t=t_0\) holds if and only if
\[
T(t)=c\left|P_{m,n}\big(e^{i(t-t_0)}\big)\right|^2,\qquad c>0,
\]
where the explicitly constructed polynomial is
\[
P_{m,n}(z)=\sum_{j=0}^{q}\left[(q+1-j)z^{jm}+(j+1)z^{jm+r}\right].
\]
Every zero of \(P_{m,n}\) lies on the unit circle (with the constant polynomial at \(n=0\) having no zeros). For matched degrees \(m=n\ge1\), the sharp constant is \(2\); outside that diagonal the exact constant depends on both orders. In particular, \(m>n\) gives \(C_{m,n}=2m/(2m-n)\), and \(m=1\) gives \(C_{1,n}=n+1\).

## Assumptions and scope

Here \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), normalized Haar integration is \(dt/(2\pi)\), and
\[
F_m(t)=\frac1m\left|\sum_{a=0}^{m-1}e^{iat}\right|^2
=\sum_{|k|<m}\left(1-\frac{|k|}{m}\right)e^{ikt}.
\]
Convolution is \((F_m*T)(t)=(2\pi)^{-1}\int_{0}^{2\pi}F_m(t-s)T(s)\,ds\). A trigonometric polynomial of degree at most \(n\) may have vanishing highest coefficients; no strict positivity or genericity is assumed. The coefficient \(C_{m,n}\) applies simultaneously at every point. Equality for the zero polynomial is trivial and is excluded from the uniqueness statement.

## Proof

**Step 1: a finite positive-definite Gram form.** By Fejér–Riesz factorization write \(T(t)=|p(e^{it})|^2\), with \(p(z)=\sum_{j=0}^{n}a_jz^j\). Fix \(t_0\), put \(w_j=a_je^{ijt_0}\), and set
\[
B_{ij}=\left(1-\frac{|i-j|}{m}\right)_+,\qquad 0\le i,j\le n.
\]
Then \(T(t_0)=|\sum_jw_j|^2\) and \((F_m*T)(t_0)=w^*Bw\). The matrix \(B\) is strictly positive definite. Indeed, \(B_{ij}\) is the Gram matrix of shifted length-\(m\) indicator vectors in \(\ell^2(\mathbb Z)\), scaled by \(1/m\). A finite linear combination of those shifts can vanish only if its Laurent-polynomial product with \(1+z+\cdots+z^{m-1}\) vanishes, forcing all coefficients to vanish.

**Step 2: an exact inverse vector.** Define a real vector \(u=(u_0,\ldots,u_n)\) by
\[
u_i=\frac mD\sum_{j=0}^q\left[(q+1-j)\mathbf1_{i=jm}+(j+1)\mathbf1_{i=jm+r}\right],\qquad 0\le i\le n.
\]
The summands combine when \(r=0\). Thus \(u\) is nonnegative and symmetric about index \(n/2\). It satisfies \(Bu=\mathbf1\). To verify this directly, extend \(u\) by zero off \(\{0,\dots,n\}\), and let \(b_k=(1-|k|/m)_+\) for integers \(k\). The exact difference relation
\[
b_{k+1}-2b_k+b_{k-1}=\frac1m\big(\mathbf1_{k=m}-2\mathbf1_{k=0}+\mathbf1_{k=-m}\big)
\]
shows that the second ordinary differences of \(v_i=\sum_jb_{i-j}u_j\) vanish at all \(1\le i\le n-1\), because \(u_{i-m}-2u_i+u_{i+m}=0\) there: each supported residue-class sequence of \(u\) is affine, with the indicated endpoint zero extension. Hence \(v_i\) is affine across \(0,\ldots,n\). Symmetry of \(u\) and of \(b\) makes \(v_i=v_{n-i}\), so \(v\) is constant. For \(r>0\),
\[
v_0=u_0+\left(1-\frac rm\right)u_r
=\frac{m(q+1)+(m-r)}D=1
\]
since \(u_0=m(q+1)/D\), \(u_r=m/D\), and \(D=(q+2)m-r\). For \(r=0\), \(u_0=1\) and no other nonzero coordinate lies at distance strictly less than \(m\), so \(v_0=1\). This proves \(Bu=\mathbf1\) in all cases.

Summing the coordinates gives
\[
\mathbf1^*u=\frac mD\left[\frac{(q+1)(q+2)}2+\frac{(q+1)(q+2)}2\right]
=C_{m,n}.
\]
Consequently \(\mathbf1^*B^{-1}\mathbf1=C_{m,n}\).

**Step 3: sharp inequality and full equality statement.** Cauchy–Schwarz in the \(B\)-inner product yields
\[
|\mathbf1^*w|^2\le (\mathbf1^*B^{-1}\mathbf1)(w^*Bw)=C_{m,n}(w^*Bw).
\]
More precisely, the exact nonnegative defect is
\[
C_{m,n}w^*Bw-|\mathbf1^*w|^2
=C_{m,n}\left(w-\frac{\mathbf1^*w}{C_{m,n}}u\right)^*
B\left(w-\frac{\mathbf1^*w}{C_{m,n}}u\right).
\]
Strict definiteness forces equality precisely when \(w\) is a scalar multiple of \(u\). Up to a common positive scale, the coefficient vector \(u\) equals that of \(P_{m,n}\). Undoing the rotation \(w_j=a_je^{ijt_0}\) gives the stated equality class, and this class attains the bound.

**Step 4: location of all extremizer zeros.** Suppose first \(q\ge1\). Set
\[
A(w)=\sum_{j=0}^{q}(q+1-j)w^j,\qquad
R(w)=w^qA(1/w)=\sum_{j=0}^{q}(j+1)w^j.
\]
Then \(P_{m,n}(z)=A(z^m)+z^rR(z^m)\). The coefficients of \(A\) are strictly decreasing from \(q+1\) to \(1\). The Eneström–Kakeya root bound locates every root \(\alpha\) of \(A\) strictly outside the closed unit disk. Because the roots of the monic real polynomial \(A\) occur in conjugate pairs (with multiplicity), its reversed polynomial is \(R(w)=\prod_\alpha(1-\overline\alpha w)\). Comparing each factor with the corresponding factor of \(A\), we have
\[
 |1-\overline\alpha w|^2-|w-\alpha|^2=(1-|\alpha|^2)(1-|w|^2)<0
\]
whenever \(|w|<1\). Hence \(|R(w)|<|A(w)|\) there and \(P_{m,n}(z)\ne0\) for \(|z|<1\). Directly from its coefficients, \(z^nP_{m,n}(1/z)=P_{m,n}(z)\) and its constant and leading coefficients are nonzero. Inversion symmetry rules out roots outside the unit circle, proving every root lies exactly on it. For \(q=0\), \(P_{m,n}(z)=1+z^r\) (constant \(2\) if \(r=0\)), so the conclusion is immediate.

## Verification

Running `python3 verification_check.py` with Python's standard library produced `PASS 44893 exact rational identities and inequalities`. The standalone script checks \(Bu=\mathbf1\), symmetry, \(\mathbf1^*u=C_{m,n}\), the exact quadratic normalization, and randomly sampled exact rational inequality tests for dozens of independent index pairs. This finite test guards algebraic slips; **the argument above, not the finite enumeration, establishes the result for all indices**.

For concrete checks: \(C_{4,5}=24/11\), \(P_{4,5}(z)=2+z+z^4+2z^5\); \(C_{4,9}=16/5\); \(C_{n,n}=2\) for \(n\ge1\). Normalized Haar measure, the matrix coefficients, and the zero-degree exception are explicit above.

## Relationship to prior work

MacDonald's November 2026 paper [1, Theorem 3, equivalent convolution formulation] proves the matched-index inequality \(T\le2(F_n*T)\) for degree-at-most-\(n\) nonnegative polynomials and identifies its two-frequency equality case. This is precisely the \(m=n\) restriction of the present finding; [1] does not state or determine the general unequal-order constants \(C_{m,n}\) or the quotient–remainder coefficient formula for the corresponding equality polynomials. Its proof also uses Fejér–Riesz factorization and completes squares, but it addresses the matching regime. A simple pointwise monotonicity comparison between distinct Fejér orders cannot substitute for the sharp two-index computation. General Fejér-kernel and summability-kernel properties [2] do not determine these pointwise extremal constants. Mentz [3] treats Toeplitz covariance inversion; only its abstract was accessible, so the relationship of its general inverse procedure to the specific closed formula above remains a bibliographic risk.

The extremizing factor, up to scale, is the degree-\(n\) reproducing kernel at \(1\) for the measure \(F_m(t)\,dt/(2\pi)\), and \(C_{m,n}\) is its diagonal value. The unit-circle zero property also follows from the classical unit-circle Christoffel–Darboux formula [4, Eq. (3.23)]: multiplying the kernel at \(1\) by \(1-z\) gives a constant multiple of a paraorthogonal polynomial. The specific contribution is the exact kernel value and coefficient formula for independently varying \(m,n\), not a general root-location principle.

## Limitations

This is a one-dimensional circle theorem for *nonnegative trigonometric polynomials*, not an arbitrary signed polynomial or a higher-dimensional analogue. It does not establish a pointwise inequality for non-polynomial positive functions with an infinite spectrum, or a multivariate formula. The novelty assessment is relative to the examined primary paper and accessible comparisons, not a proof that no unindexed earlier formula exists. Numerical checks do not constitute an independent proof or audit.

## References

[1] Sullivan Francis MacDonald, *A convolution inequality and the Krzyż conjecture*, arXiv:2611.05363, first submitted November 3, 2026, revised November 5, 2026, especially Theorem 3 and its proof. https://arxiv.org/html/2611.05363v2

[2] Fejér summability kernel and Fejér–Riesz factorization, classical standard results; the normalization and factorization are stated in [1, §2] and in the displayed definitions above.

[3] Raúl Pedro Mentz, *On the Inverse of Some Covariance Matrices of Toeplitz Type*, SIAM Journal on Applied Mathematics 31 (1976), 426–437, DOI 10.1137/0131036 (abstract consulted; full text not inspected).

[4] Barry Simon, *The Christoffel–Darboux Kernel*, arXiv:0806.1528, Section 3, https://arxiv.org/abs/0806.1528.
