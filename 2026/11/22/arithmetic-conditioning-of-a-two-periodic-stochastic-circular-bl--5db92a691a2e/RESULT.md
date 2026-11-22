# Arithmetic conditioning of a two-periodic stochastic circular blur

## Finding

**Theorem (exact determinant, nullity, and sharp conditioning law).** For each integer \(q\ge2\), let \(P_{2q}(a,b)\) act on real cyclic arrays of length \(2q\) by
\[
(P_{2q}u)_j=(1-t_j)u_j+\frac{t_j}{2}(u_{j-1}+u_{j+1}),\quad
 t_j=\begin{cases}a,&j\text{ even},\\ b,&j\text{ odd},\end{cases}\qquad 0<a,b<1,
\]
with indices modulo \(2q\). Each row sums to one, every allowed stencil coefficient is strictly positive, and the transpose is a column-stochastic, two-periodic source-normalized blur. For \(a\ne b\), its minimal coefficient period is two.

1. If \(a+b<1\), the matrices are invertible with condition numbers uniformly bounded in \(q\). If \(a+b=1\), each matrix has nullity exactly one.
2. If \(a+b>1\), define the *resonant phase* \(\alpha\in(0,1/2)\) by
\[
 \cos^2(\pi\alpha)=\frac{(1-a)(1-b)}{ab},
\qquad \|x\|_{\mathbb Z}=\min_{m\in\mathbb Z}|x-m|.
\]
Then the exact real determinant is
\[
\boxed{\det P_{2q}=-4^{1-q}(ab)^q\sin^2(\pi q\alpha).}
\]
If \(\alpha=p/r\) is in lowest terms, the nullity is exactly two if \(r\mid q\) and zero otherwise. If \(\alpha\) is irrational, *every* finite matrix is invertible.
3. Let
\[
\begin{aligned}
 S_0&=(1-a)^2+(1-b)^2+a^2+b^2,\\
 M&=\left(\frac{S_0+\sqrt{S_0^2-4(1-a-b)^2}}2\right)^{1/2},\\
 S_*&=(1-a)^2+(1-b)^2+(a^2+b^2)\cos^2(\pi\alpha),\\
 C_{a,b}&=\frac{M\sqrt{S_*}}{\pi ab\sin(2\pi\alpha)}>0.
\end{aligned}
\]
Whenever \(q\to\infty\) through nonsingular grids in the regime \(a+b>1\), their Euclidean spectral condition numbers obey the sharp asymptotic
\[
\boxed{\kappa_2(P_{2q})=(C_{a,b}+o(1))\frac{q}{\|q\alpha\|_{\mathbb Z}}.}
\]
Consequently a rational phase produces exact singularities at every multiple of its denominator and linear conditioning along all other grid sizes. A badly approximable irrational phase produces \(O(q^2)\) conditioning on *all* grids and order \(q^2\) on infinitely many grids. A Liouville phase yields invertible matrices at every size but, for every \(H>0\), condition numbers greater than \(q^H\) for infinitely many sizes.

The condition numbers of the column-stochastic blur \(P_{2q}^{\mathsf T}\) are identical.

## Assumptions and scope

All parameters are fixed independently of \(q\). The norm is the induced Euclidean matrix norm; \(\kappa_2(P)=\|P\|_2\|P^{-1}\|_2\) if invertible, and infinite otherwise. The assertions concern exact arithmetic, not a particular floating-point FFT implementation. The approximation exponent is a property of the *resonant phase*, not of the spatial periodicity (which is fixed at two). A real irrational \(\alpha\) is badly approximable when \(\inf_{q\ge1}q\|q\alpha\|_{\mathbb Z}>0\); a Liouville number admits arbitrarily high rational approximation exponents.

Examples within the genuinely two-periodic family use \(a=3/4\) and \(b=[1+3\cos^2(\pi\alpha)]^{-1}\). The rational choice \(\alpha=1/3\) gives \(b=4/7\) and exact nullity two precisely when \(3\mid q\). The choice \(\alpha=\sqrt2-1\) gives the badly approximable regime. The classical Liouville constant \(\alpha=\sum_{j\ge1}10^{-j!}\) gives the superpolynomial subsequences. Each choice has \(0<b<1\), \(a+b>1\), and \(a\ne b\).

## Proof

**Periodic Fourier blocks.** Write the even and odd components as pairs of length \(q\) and apply the unitary Fourier transform to the cell index. At frequency \(k\in\{0,\dots,q-1\}\), set \(\theta_k=2\pi k/q\). The transformed matrix is the direct sum of
\[
 B_k=\begin{pmatrix}
 1-a &\frac a2(1+e^{-i\theta_k})\\
 \frac b2(1+e^{i\theta_k})&1-b
 \end{pmatrix}.
\]
Consequently its determinant is
\[
 \Delta_k=(1-a)(1-b)-ab\cos^2(\pi k/q).
\]
In the supercritical regime this is \(\Delta_k=\frac{ab}{2}[\cos(2\pi\alpha)-\cos(2\pi k/q)]\).

**Chebyshev determinant identity.** The polynomial identity
\[
 \prod_{k=0}^{q-1}\left(z-\cos\frac{2\pi k}{q}\right)
 =2^{1-q}[T_q(z)-1]
\]
follows from the zeros, multiplicities and leading coefficient of the first-kind Chebyshev polynomial. Multiplying \(\Delta_k\) and substituting \(T_q(\cos(2\pi\alpha))=\cos(2\pi q\alpha)\) yields
\[
 \det P_{2q}=2^{1-2q}(ab)^q[\cos(2\pi q\alpha)-1]
 =-4^{1-q}(ab)^q\sin^2(\pi q\alpha).
\]
For \(0<\alpha<1/2\), distinct zeros of the block determinants occur precisely at \(k/q\equiv\pm\alpha\pmod1\). Each corresponding \(2\times2\) block has rank one, since both diagonal entries are positive. Thus the nullity is exactly two for resonant rational grids and zero for irrational phases.

**Subcritical and critical regimes.** When \(a+b<1\), every \(\Delta_k\ge1-a-b>0\). All block norms are uniformly bounded, so the least singular values are uniformly positive. When \(a+b=1\), only \(k=0\) has \(\Delta_k=0\); that block has rank one and every other block is invertible.

**Exact singular values and norm.** Put \(c_k=|\cos(\pi k/q)|\). Direct calculation gives
\[
 S_k=\operatorname{tr}(B_k^*B_k)=(1-a)^2+(1-b)^2+(a^2+b^2)c_k^2,
 \qquad s_{\pm}(k)^2=\frac{S_k\pm\sqrt{S_k^2-4\Delta_k^2}}2.
\]
Diagonal unitary changes turn \(B_k\) into the nonnegative real matrix with diagonals \(1-a,1-b\) and off-diagonals \(ac_k,bc_k\). Its operator norm is nondecreasing in \(c_k\), by applying the absolute-value inequality to test vectors. Because \(c_0=1\), the largest singular value of the entire matrix is exactly \(M\), independently of \(q\).

**Uniform near-zero asymptotics.** Near either simple zero \(x=\alpha\) or \(x=1-\alpha\),
\[
 |\Delta(x)|=ab\pi\sin(2\pi\alpha)\,|x-\alpha|\,(1+O(|x-\alpha|)),
\]
with the analogous distance to \(1-\alpha\). At a zero, the nonzero singular value is \(\sqrt{S_*}\). Using \(s_-(x)s_+(x)=|\Delta(x)|\), uniformly for sampled points within \(O(1/q)\) of the zeros,
\[
 s_-(x)=\frac{ab\pi\sin(2\pi\alpha)}{\sqrt{S_*}}
 \operatorname{dist}(x,\{\alpha,1-\alpha\})\,(1+O(1/q)).
\]
The least distance of a grid point \(k/q\) to either zero modulo one is exactly \(\|q\alpha\|_{\mathbb Z}/q\). Since the symbol is bounded away from singularity outside neighborhoods of the two zeros, these nearest points control the minimum singular value for all sufficiently large nonsingular grids. Dividing the constant maximum singular value \(M\) by this minimum proves the displayed asymptotic even for unusually good rational approximations (the relative Taylor error remains uniform).

**Arithmetic consequences.** If \(\alpha=p/r\), then \(\|q\alpha\|_{\mathbb Z}=0\) exactly for \(r\mid q\); on other residues it is between \(1/r\) and \(1/2\), so the condition numbers are of linear order. If \(\alpha\) is badly approximable, \(\|q\alpha\|_{\mathbb Z}\ge c/q\) for all \(q\), while continued-fraction convergents give infinitely many \(q\) with \(\|q\alpha\|_{\mathbb Z}<1/q\). The two bounds give respectively \(O(q^2)\) and \(\Omega(q^2)\). If \(\alpha\) is Liouville, infinitely many approximations achieve \(\|q\alpha\|_{\mathbb Z}<q^{-H}\) for arbitrarily large chosen \(H\), forcing superpolynomial condition numbers. The example parameters implement each regime exactly.

## Verification

Run `python verify.py` with Python 3, NumPy and SymPy. The program assembles the full matrices independently of the Fourier-block formula; checks their singular values against the block and closed-form formulas; verifies the determinant numerically; verifies finite rational cases by exact SymPy matrix determinants and ranks; and checks the sharp asymptotic constant for two irrational phases. It completed with `VERIFY_OK 242`. These finite checks are reproducibility tests, not substitutes for the preceding all-dimension and number-theoretic proof.

## Relationship to prior work

González del Cueto and Guevara Vasquez, *Fast circular convolution with periodic kernels*, arXiv:2611.16144v1, establish the unitary Fourier-block representation of general spatially periodic convolution and apply it to matrix inversion and regularization. The present claim concerns a specific minimal two-phase positive blur, its all-size **Chebyshev sine-square determinant**, exact rank-loss arithmetic, and **sharp Diophantine condition-number constant**. The general block decomposition alone does not state this classification. Periodic Jacobi spectral theory and the classical theory of rational approximation supply background tools, rather than the explicit blur law. Earlier transform-based circular deconvolution stability studies concern backward/forward stability of FFT algorithms rather than this exact family-wide conditioning arithmetic. A thorough historical-priority guarantee is not asserted.

## Limitations

The blur is a specially chosen three-tap, two-periodic family, not a classification of arbitrary point-spread functions. Superpolynomial instability requires finely tuned parameters; the universal supercritical phenomenon is at least linear deterioration on increasingly fine cycles. Bounds refer to worst-case Euclidean measurement perturbations, not average-case image error, noisy coefficient identification, roundoff errors, or a claim that Tikhonov-regularized reconstruction fails. The irrational parameter relation is prescribed exactly, so finite-precision coefficient rounding can alter the extremely long-range Liouville regime. Full historical priority of the exact construction remains an unresolved research risk.

## References

1. F. González del Cueto and F. Guevara Vasquez, *Fast circular convolution with periodic kernels*, arXiv:2611.16144v1 (2026-11-12), https://arxiv.org/abs/2611.16144 . Sections 1, 4, 7 and 8; especially Theorem 4.2, Remark 4.6 and the condition-number discussion.
2. P. Y. Yalamov, *On the Almost Strong Stability of the Circular Deconvolution Algorithm*, SIAM Journal on Matrix Analysis and Applications 22 (2000), 358–363, https://doi.org/10.1137/S0895479899351052 . Available abstract only for this comparison.
3. E. Linzer, *On the Stability of Transform-Based Circular Deconvolution*, SIAM Journal on Numerical Analysis 29 (1992), 1482–1492, https://doi.org/10.1137/0729085 . Available abstract only for this comparison.
4. A. Dyachenko and M. Tyaglov, *On the spectrum of the tridiagonal matrices with two-periodic main diagonal*, arXiv:2109.10771 (2021), https://arxiv.org/abs/2109.10771 . Available abstract; related finite tridiagonal rather than the periodic blur conditioning problem.
