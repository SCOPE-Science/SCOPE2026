# A matrix Cauchy law for singular Herglotz boundary spectra

## Finding
Let \(\Sigma\) be a finite positive semidefinite Hermitian matrix measure on the unit circle that is singular with respect to arc length, with strictly positive total matrix \(T=\Sigma(\mathbb T)\). For any Hermitian matrix \(B\), define the analytic matrix-valued function
\[
H(z)=B+i\int_{\mathbb T}\frac{\zeta+z}{\zeta-z}\,d\Sigma(\zeta),\qquad |z|<1.
\]
For almost every angle, its radial boundary value \(Y(\theta)=\lim_{r\uparrow1}H(re^{i\theta})\) exists and is Hermitian. Its **averaged matrix spectral measure** is independent of the location and decomposition of the singular measure:
\[
\frac1{2\pi}\int_0^{2\pi}g(Y(\theta))\,d\theta
=\int_{\mathbb R}g(x)\,K_{B,T}(x)\,dx,
\quad K_{B,T}(x)=\frac1\pi(B-xI-iT)^{-1}T(B-xI+iT)^{-1}
\]
for every bounded Borel function \(g:\mathbb R\to\mathbb C\). The integral on the right is an ordinary matrix-valued Lebesgue integral. In particular, \(K_{B,T}(x)\) is positive definite, \(\int K_{B,T}(x)dx=I\), and the entire averaged spectral-projection measure depends only on \(B\) and \(T\).

When \(B=0\), the density simplifies to \(K_{0,T}(x)=\pi^{-1}T(T^2+x^2I)^{-1}\). Consequently, for every real \(y\),
\[
\frac1{2\pi}\int_0^{2\pi}\mathbf1_{(y,\infty)}(Y(\theta))\,d\theta
=\tfrac12I-\pi^{-1}\arctan(yT^{-1}).
\]
The positive spectral projection therefore averages **exactly \(I/2\)**. For \(0<p<1\),
\[
\frac1{2\pi}\int_0^{2\pi}\operatorname{tr}|Y(\theta)|^p\,d\theta
=\frac{\operatorname{tr}(T^p)}{\cos(\pi p/2)},
\]
whereas the integral is infinite for every \(p\ge1\).

## Assumptions and scope
The dimension \(d\) is any finite positive integer. A matrix measure \(\Sigma\) is positive semidefinite if \(\Sigma(E)\) is Hermitian positive semidefinite for every Borel set \(E\), and singular if all its entries are supported on one arc-length-null Borel set. Assume \(T=\Sigma(\mathbb T)>0\) in the strictly positive definite sense. The matrix \(B=B^*\) is arbitrary; it need not commute with \(T\). Functional calculus \(g(Y)\) and spectral projectors use the usual Hermitian matrix spectral theorem. These assumptions allow atomic, singular-continuous and mixed singular measures.

For distinct angles \(\theta_j\) and matrices \(A_j\succeq0\) with \(\sum_jA_j=T>0\), the atomic choice \(\Sigma=\sum_jA_j\delta_{e^{i\theta_j}}\) has explicit boundary field
\[
Y(\theta)=B-\sum_j A_j\cot\frac{\theta-\theta_j}{2}.
\]
No commutativity among the residues is imposed; hence the displayed law is not obtained by simultaneous diagonalization of the individual summands.

## Proof
**1. Boundary Hermiticity.** For \(z\) in the disk, \(\operatorname{Im}H(z)=\int P_z(\zeta)\,d\Sigma(\zeta)\succeq0\), where \(P_z=(1-|z|^2)/|\zeta-z|^2\). For every vector \(v\), the scalar function \(v^*H(z)v\) is a Herglotz function whose representing positive measure is \(v^*\Sigma v\). Its finite radial boundary values exist almost everywhere, and their imaginary parts vanish almost everywhere because the representing measures are singular. Applying the scalar boundary theorem to a finite polarization family \(v=e_j,e_j+e_k,e_j+ie_k\) gives simultaneous entrywise radial boundary values and yields \(Y(\theta)=Y(\theta)^*\) almost everywhere.

**2. Exact resolvent average.** Fix any \(w\) with \(\operatorname{Im}w<0\). The matrix \(H(z)-wI\) has imaginary part at least \(|\operatorname{Im}w|I\), so it is invertible and its inverse has norm at most \(|\operatorname{Im}w|^{-1}\). The matrix function \(R_w(z)=(H(z)-wI)^{-1}\) is bounded analytic. The disk mean-value identity and dominated radial convergence give
\[
\frac1{2\pi}\int_0^{2\pi}(Y(\theta)-wI)^{-1}\,d\theta
=R_w(0)=(B+iT-wI)^{-1}. \tag{1}
\]
Define a positive matrix measure \(M(E)=(2\pi)^{-1}\int E_{Y(\theta)}(E)\,d\theta\). It has total mass \(I\), and equation (1) is exactly its matrix-valued Cauchy transform \(\int(x-w)^{-1}\,dM(x)\).

**3. Cauchy inversion.** Let \(D_x=B-xI+iT\), which is invertible for every real \(x\) since \(T>0\). The resolvent identity shows
\[
-\operatorname{Im}(D_x^{-1})=D_x^{-*}TD_x^{-1},
\]
where \(\operatorname{Im}C=(C-C^*)/(2i)\). Hence the boundary negative imaginary part of the right side of (1) has density
\[
-\pi^{-1}\operatorname{Im}(B+iT-xI)^{-1}
=\pi^{-1}D_x^{-*}TD_x^{-1}=K_{B,T}(x).
\]
The entrywise Stieltjes inversion theorem recovers \(M\) from (1). Because \(T>0\) supplies a uniform lower imaginary part, the resolvent is analytic across the real \(w\)-axis from below; the inversion is uniform on compact real intervals, giving \(dM(x)=K_{B,T}(x)\,dx\), with no atoms or singular remainder. Applying bounded Borel functional calculus and integrating \(g\) against \(M\) proves the main identity. Moreover \(K_{B,T}(x)\succ0\), and normalization follows from \(M(\mathbb R)=I\).

**4. Scalarizable consequences for zero drift.** When \(B=0\), \(T\) commutes with \(T^2+x^2I\), so spectral calculus gives the displayed simplified density. For a scalar \(t>0\), elementary integration yields
\[
\frac1\pi\int_y^\infty \frac{t}{t^2+x^2}\,dx
=\frac12-\frac1\pi\arctan(y/t),
\]
and, for \(0<p<1\),
\[
\frac1\pi\int_{\mathbb R}|x|^p\frac{t}{t^2+x^2}\,dx
=\frac{t^p}{\cos(\pi p/2)}.
\]
Diagonalize \(T\), apply these identities to each eigenvalue, and sum the second identity for the trace. The density satisfies \(K_{0,T}(x)=\pi^{-1}Tx^{-2}+O(|x|^{-4})\) as \(|x|\to\infty\), giving divergence of all \(p\ge1\) trace moments.

## Verification
The mathematical proof is exact and applies to arbitrary finite matrix dimension and arbitrary finite positive singular matrix measures. `CHECK.py` independently tests the atomic two-dimensional noncommuting example by periodic midpoint quadrature for resolvents at several nonreal spectral parameters; it also checks the spectral Cauchy normalization and power-moment scalar integrals. These numerical checks are finite consistency tests, not proof of the general theorem. Run `python CHECK.py` from the extracted package with Python 3 and no third-party dependencies.

## Relationship to prior work
Efraimidis, Llinares, MacDonald, Uriarte-Tuero and Vukotić (2026, Theorem 1 and Corollary 1.1) establish the **scalar** positive-atomic cotangent distribution; the scalar phenomenon was previously proved by Poltoratski. Aizenman and Warzel (2013) study scalar Herglotz boundary Cauchy laws and diagonal matrix elements, but a scalar distribution for each quadratic form is not the operator-valued distribution of nonlinear spectral functions of noncommuting matrices. Gesztesy and Tsekanovskii (1997/2000) develop the general matrix-valued Herglotz representation and inversion, which are used here as background, and Liaw and Treil (2018) prove a matrix-valued spectral averaging theorem for a different **real perturbation parameter**. The statement here is an explicit average of entire spectral projections over the **unit-circle boundary parameter**, covering noncommuting residues and arbitrary singular matrix measures. The proof highlights the required matrix resolvent averaging and computes the positive density and special zero-drift invariants. It does not claim novelty for the scalar Boole law or for standard Herglotz inversion.

## Limitations
The strict positivity of \(T\) is used to avoid singular real-axis poles of the averaged resolvent; no classification with merely semidefinite \(T\) is asserted. The result concerns the *averaged matrix spectral measure*, not the joint law of ordered eigenvalues or individual eigenvectors. The order of the factors in the noncommuting density matters. The proof does not establish any claimed uniqueness or statistical independence among the matrix summands. The conclusion is a direct application of known analytic matrix tools; an equivalent operator-valued distribution identity could exist in older matrix spectral averaging literature. Independent literature-priority verification remains outstanding.

## References
1. I. Efraimidis, A. Llinares, S. MacDonald, I. Uriarte-Tuero and D. Vukotić, *A property of boundary extensions of atomic singular inner functions*, arXiv:2611.06877 (first public November 4, 2026), Theorem 1 and Corollary 1.1. https://arxiv.org/abs/2611.06877
2. M. Aizenman and S. Warzel, *On the ubiquity of the Cauchy distribution in spectral problems*, arXiv:1312.7769 (2013). https://arxiv.org/abs/1312.7769
3. F. Gesztesy and E. Tsekanovskii, *On Matrix-Valued Herglotz Functions*, arXiv:funct-an/9712004, Math. Nachr. 218 (2000), 61–138. https://arxiv.org/abs/funct-an/9712004
4. C. Liaw and S. Treil, *Matrix Measures and Finite Rank Perturbations of Self-Adjoint Operators*, arXiv:1806.08856 (2018), Theorem 4.1. https://arxiv.org/abs/1806.08856
5. A. Poltoratski, *On the distributions of boundary values of Cauchy integrals*, Proc. Amer. Math. Soc. 124 (1996), 2455–2463; bibliographic citation from reference 1, full text not inspected.
