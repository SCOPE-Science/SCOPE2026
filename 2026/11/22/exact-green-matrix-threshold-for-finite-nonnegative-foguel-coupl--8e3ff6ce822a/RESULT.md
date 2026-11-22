# Exact Green-matrix threshold for finite nonnegative Foguel couplings

## Finding

Let \(S\) be the unilateral shift on \(\ell^2(\mathbb N_0)\), and let \(A\) be a nonzero \(N\)-by-\(N\) matrix with **real nonnegative entries**, extended by zero on all higher coordinates. For \(t\ge 0\), form the Foguel operator
\[
F_{tA}=\begin{pmatrix}S^*&tA\\0&S\end{pmatrix}.
\]
Define the real positive definite matrix \(G_0=[2(1+\min\{i,j\})]_{0\le i,j<N}\) and \(\sigma_0=\|G_0^{1/2} A G_0^{1/2}\|_2>0\). Then the **exact** lower-numerical-radius threshold is
\[
 w(F_{tA})=1\quad\Longleftrightarrow\quad 0\le t\le t_c(A):=\frac{2}{\sigma_0}.
\]
This is an if-and-only-if criterion for arbitrary finite, entrywise nonnegative, potentially nonsymmetric couplings, not merely diagonal or symmetric ones.

For \(t>t_c(A)\), the complete numerical radius is \(w(F_{tA})=\cosh s_t>1\), where \(s_t>0\) is the unique solution of
\[
 \frac t2\left\|G_s^{1/2} A G_s^{1/2}\right\|_2=1,
 \qquad (G_s)_{ij}=\frac{e^{-s|i-j|}-e^{-s(i+j+2)}}{\sinh s}.
\]
There is no positive \(s_t\) when \(t\le t_c(A)\). The numerical radius is not attained by a unit vector when \(t\le t_c(A)\), but is attained when \(t>t_c(A)\).

For the matrix unit \(A=E_{ij}\) with \(i,j\in\mathbb N_0\), the threshold reduces to \(t_c=((i+1)(j+1))^{-1/2}\). In the supercritical regime the unique positive \(s\) satisfies
\[
 t=\frac{2\sinh s}{\sqrt{(1-e^{-2(i+1)s})(1-e^{-2(j+1)s})}},
\]
and the sharp threshold onset is
\[
 w(F_{tE_{ij}})-1\sim \frac{2}{(i+j+2)^2}\left(\frac{t}{t_c}-1\right)^2
 \qquad (t\downarrow t_c\text{ from above}).
\]
As an explicitly coupled nonsymmetric example, if \(A=\left(\begin{smallmatrix}0&a\\b&0\end{smallmatrix}\right)\) with \(a,b\ge0\), then \(w(F_A)=1\) if and only if \(a\le1\), \(b\le1\) and
\[
 1-2a^2-2ab-2b^2+a^2b^2\ge0.
\]
In particular, equal two-way edges have the sharp threshold \(a=b\le\sqrt2-1\), whereas a single oriented edge has threshold \(1/\sqrt2\).

## Assumptions and scope

The Hilbert space is complex and separable, \(N\ge1\) is arbitrary but finite, all entries of \(A\) are real and nonnegative, and \(A\ne0\). The operator \(A\) is zero on the complement of \(\operatorname{span}\{e_0,\ldots,e_{N-1}\}\). The numerical radius is \(w(B)=\sup_{\|z\|=1}|\langle Bz,z\rangle|\). Every square root of a positive matrix is its unique positive definite square root. The symbol \(\|\cdot\|_2\) is the Euclidean operator/spectral norm (largest singular value), not the Frobenius norm. The rank-one illustration allows any two indices by increasing \(N\).

## Proof

**1. Reduction to one real selfadjoint problem.** Let \(J=(S+S^*)/2\). Since every matrix entry of \(F_{tA}\) is nonnegative, the absolute-value inequality for any unit vector \(z\) gives
\[
 |\langle F_{tA}z,z\rangle|\le \langle F_{tA}|z|,|z|\rangle
 =\langle H_t|z|,|z|\rangle,
 \qquad H_t=\begin{pmatrix}J&tA/2\\tA^*/2&J\end{pmatrix}.
\]
Conversely, nonnegative real test vectors show \(w(F_{tA})=\sup\sigma(H_t)\). The essential spectrum of \(H_t\) is \([-1,1]\) because it is a finite-rank perturbation of \(J\oplus J\). Hence \(w(F_{tA})\ge1\).

**2. Exact finite threshold.** For \(\lambda>1\), \(R_\lambda=(\lambda-J)^{-1}\) is positive. By the Schur complement, the operator \(\lambda I-H_t\) is positive definite precisely when
\[
 \frac t2\big\|R_\lambda^{1/2} A R_\lambda^{1/2}\big\|_2<1.
\]
This inequality uses the block positivity test \(\left(\begin{smallmatrix}I&-B\\-B^*&I\end{smallmatrix}\right)>0\iff\|B\|<1\), applied after conjugation by \((\lambda-J)^{-1/2}\). Because \(A\) is supported in the first \(N\) coordinates, the nonzero singular values of the product are those of \(G_\lambda^{1/2} A G_\lambda^{1/2}\), where \(G_\lambda=P_N R_\lambda P_N^*\); this follows by polar factorization of \(R_\lambda^{1/2}P_N^*\). 

Set \(\lambda=\cosh s\). The resolvent kernel follows by solving the discrete Dirichlet Green equation (or reflecting the full-line Green kernel):
\[
 (R_{\cosh s})_{ij}=\frac{e^{-s|i-j|}-e^{-s(i+j+2)}}{\sinh s}.
\]
Taking the limit \(s\downarrow0\) gives \(G_0\), with entries \(2(1+\min\{i,j\})\). These entries form the Gram matrix of discrete initial-segment indicators, hence \(G_0\) is positive definite. The limiting matrix norm is \(\sigma_0\). The largest spectrum point of \(H_t\) stays at one if and only if \(t\sigma_0\le2\). Equality is included because a spectral point \(>1\) would violate the Schur inequality at some \(\lambda>1\), while strict inequality \(t\sigma_0>2\) guarantees a spectral point beyond one by continuity.

**3. Unique supercritical root.** For \(\lambda_2>\lambda_1>1\), the finite compressions satisfy \(0<G_{\lambda_2}<G_{\lambda_1}\) in the strict Loewner order. The variational identity
\[
 \big\|G^{1/2}AG^{1/2}\big\|_2=
 \sup_{x,y\ne0}\frac{|x^*Ay|}{\sqrt{(x^*G^{-1}x)(y^*G^{-1}y)}}
\]
shows strict decrease for nonzero \(A\), since the two denominator quadratic forms strictly increase as \(G\) decreases. The norm tends to zero as \(\lambda\to\infty\). It decreases continuously from \(\sigma_0\) to zero, so for \(t>t_c\) there is exactly one root, and positivity of \(H_t\)'s resolvent below its largest spectral point identifies that root with \(w(F_{tA})\). Because \(H_t\) is finite rank away from the essential band, the supercritical top point is an eigenvalue. A nonnegative eigenvector gives equality in the numerical-radius variational formula. At or below threshold, a putative norm-attaining nonnegative vector would be an eigenvector of \(H_t\) at eigenvalue one; beyond the finite support it satisfies \(x_{n+1}-2x_n+x_{n-1}=0\), whose only square-summable tail is zero. Backward recurrence gives the entire vector zero, a contradiction. This proves the attainment statements.

**4. Explicit examples and onset.** For \(A=E_{ij}\), the compressed product has norm \(\sqrt{(G_s)_{ii}(G_s)_{jj}}\), which yields the displayed hyperbolic formula and threshold. If \(h=i+1\), \(k=j+1\), the expansion \((G_s)_{ii}=2h-2h^2s+O(s^2)\), and likewise for \(j\), gives \(t/t_c=1+(h+k)s/2+O(s^2)\). Since \(\cosh s-1=s^2/2+O(s^4)\), the stated quadratic constant follows.

For the two-way-edge example, \(G_0=\left(\begin{smallmatrix}2&2\\2&4\end{smallmatrix}\right)\) and the norm threshold is equivalent by congruence to
\[
 G_0^{-1}-\frac14 A^*G_0A=
 \begin{pmatrix}1-b^2&-(1+ab)/2\\-(1+ab)/2&(1-a^2)/2\end{pmatrix}\succeq0.
\]
Its principal-minor test gives the inequalities stated above. At \(a=b\), the quartic factors as \((a^2-(\sqrt2-1)^2)(a^2-(\sqrt2+1)^2)\); the small admissible branch is exactly \(a\le\sqrt2-1\).

## Verification

The standalone reproducibility checker `checks/check_foguel.py` evaluates exact rational Green-matrix and two-way-edge identities, matrix-unit secular equations, and large finite Jacobi compressions for deterministic nonnegative test matrices. It does not substitute finite sampling for the infinite-dimensional Schur-complement or no-attainment arguments. Run with `python checks/check_foguel.py` (Python 3, NumPy and SciPy). The exact analytic steps are given above.

## Relationship to prior work

Gau–Wang–Wu (2021) develop numerical ranges of Foguel operators, including nonnegative diagonal coupling. Gau–Li–Wang–Wu (2023) establish upper/lower extremality criteria and supply a **sufficient** finite-matrix test for symmetric nonnegative couplings (Proposition 3.1), including the one-site and first-two-site diagonal examples. Those instances are recovered by the present criterion, and are not claimed as discoveries. Jiang–Spitkovsky (2022/2023) use a Schur complement to calculate the numerical range in the scalar infinite-support case. The present classification makes the finite-support **arbitrary nonsymmetric nonnegative** condition necessary and sufficient, gives the supercritical singular-value root for every support size, and identifies a two-way-coupling quartic and exact off-diagonal rank-one onset. The methods (positive-matrix comparison and the Dirichlet Green kernel) are standard; the assessed content is their complete sharp coupling classification, not a new general Schur theorem.

## Limitations

Entrywise nonnegativity is essential for reducing all numerical-radius directions to the positive real direction; no such formula is asserted for signed or complex matrix entries. The support dimension is finite; no theorem is claimed about general compact or noncompact couplings or about the unresolved universal compactness question. The supercritical value is characterized by a unique scalar root, not generally an elementary closed form. Historical novelty is based on inspected sources and searches, not exhaustive priority certification; an unindexed finite-support formula may exist. No independent external validation is asserted.

## References

1. H.-L. Gau, K.-Z. Wang, P. Y. Wu, *Numerical ranges of Foguel operators*, Linear Algebra Appl. 610 (2021), 766–784. DOI: 10.1016/j.laa.2020.10.017. Available full-text representation: https://www.researchgate.net/publication/346357215_Numerical_ranges_of_Foguel_operators
2. H.-L. Gau, C.-K. Li, K.-Z. Wang, P. Y. Wu, *Extremality of bounds for numerical radii of Foguel operators*, J. Math. Anal. Appl. 528 (2023), 127484. Author preprint https://cklixx.people.wm.edu/Foguel_Extremality_revision.pdf ; DOI: 10.1016/j.jmaa.2023.127484.
3. M. Jiang, I. M. Spitkovsky, *Numerical ranges of some Foguel operators*, Operators and Matrices 17 (2023), 179–185; first preprint arXiv:2204.04631 (10 April 2022); https://files.ele-math.com/articles/oam-17-14.pdf.
