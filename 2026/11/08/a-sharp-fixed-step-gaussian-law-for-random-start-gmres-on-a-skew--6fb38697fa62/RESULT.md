# A sharp fixed-step Gaussian law for random-start GMRES on a skew Toeplitz stencil

## Finding
Let \(q\ge1\) be fixed, let even \(N\to\infty\), and let \(S_N\in\mathbb R^{N\times N}\) have entries \((S_N)_{j+1,j}=1\), \((S_N)_{j,j+1}=-1\), and all other entries zero. Draw \(b_N\) uniformly on the real Euclidean unit sphere and solve \(S_Nx=b_N\) by exact-arithmetic, unrestarted GMRES from zero. Write \(R_{N,k}=\|r_k\|_2/\|b_N\|_2\).

Set \(L=2q+1\). For every such \(N\ge2q+2\), \(R_{N,2q+1}=R_{N,2q}\) identically, for every starting vector. Moreover,
\[
R_{N,2q}\xrightarrow{\mathbb P}\frac1{\sqrt L},\qquad
\sqrt N\left(R_{N,2q}-\frac1{\sqrt L}\right)
\xrightarrow{\mathrm d}\mathcal N\!\left(0,\frac{(2L-1)(L-1)}{6L^2}\right).
\]
Equivalently the squared relative residual satisfies
\[
\sqrt N\left(R_{N,2q}^2-\frac1L\right)
\xrightarrow{\mathrm d}\mathcal N\!\left(0,\frac{2(2L-1)(L-1)}{3L^3}\right).
\]
In particular the first nontrivial even step has limiting residual \(1/\sqrt3\) and norm-fluctuation variance \(5/27\), whereas the fourth step has limiting residual \(1/\sqrt5\) and variance \(6/25\). The same result holds when every \(S_N\) is multiplied by any nonzero real scalar, because its Krylov spaces are unchanged.

## Assumptions and scope
The dimension \(N\) tends to infinity through even integers; \(q\) remains fixed independently of \(N\). GMRES is Euclidean, exact, and unrestarted; the initial vector is zero; the right-hand side is Haar-uniform on the **real** sphere, independent of the deterministic coefficient matrix. The matrix \(S_N\) is nonsingular for even \(N\), since its eigenvalues are \(2i\cos(j\pi/(N+1))\) for \(1\le j\le N\). No statement is made for growing iteration index, nonzero reaction diagonal, finite precision, or complex Haar starts.

## Proof
**1. Parity of the Krylov minimization.** Because \(S_N^\mathsf T=-S_N\), for every real vector \(b\), every \(j,l\ge0\) and every odd total exponent,
\[
\langle S_N^{2j}b,S_N^{2l+1}b\rangle
=b^\mathsf T S_N^{2j+2l+1}b=0.
\]
The space spanned by odd powers is orthogonal to the space spanned by even powers. Writing each residual polynomial as an even polynomial plus an odd polynomial, with constant term one, shows that the odd part can only increase the norm. Therefore minimizing over degrees at most \(2q+1\) gives exactly the same residual norm as minimizing over degrees at most \(2q\), including possible early termination.

**2. Deterministic limiting extremal polynomial.** The imaginary eigenvalues of \(S_N\) are \(i x_j\), where \(x_j=2\cos(j\pi/(N+1))\). Their empirical law converges, with \(O(N^{-1})\) quadrature error for every fixed polynomial, to the arcsine probability measure
\[
\nu(dx)=\frac{\mathbf1_{(-2,2)}(x)}{\pi\sqrt{4-x^2}}\,dx.
\]
Write an even residual polynomial in the form \(p(i x)=Q(x)\), with \(Q\) real, even, degree at most \(2q\), and \(Q(0)=1\). The unique minimizer of \(\int Q(x)^2\nu(dx)\) is the normalized reproducing kernel at zero. With \(T_j\) the Chebyshev polynomials of the first kind, orthonormality of \(1,\sqrt2\,T_j(x/2)\) gives
\[
Q_q(x)=\frac{1+2\sum_{j=1}^{q}(-1)^jT_{2j}(x/2)}{L},
\qquad L=2q+1.
\]
Indeed \(Q_q(0)=1\), and \(\int x^{2j}Q_q(x)\nu(dx)=0\) for \(1\le j\le q\); the Gram matrix on the latter monomials is strictly positive definite. Hence \(\int Q_q^2d\nu=1/L\).

**3. Exact fourth moment.** Put \(x=2\cos\theta\). Then
\[
LQ_q(2\cos\theta)=1+2\sum_{j=1}^q(-1)^j\cos(2j\theta)
=\sum_{j=-q}^q e^{ij(2\theta+\pi)}.
\]
For a Dirichlet kernel with \(L\) consecutive frequencies, its squared modulus has Fourier coefficients \(L-|m|\) for \(|m|<L\). Parseval therefore yields
\[
\int Q_q^4d\nu=\frac1{L^4}\left(L^2+2\sum_{m=1}^{L-1}(L-m)^2\right)
=\frac{2L^2+1}{3L^3}.
\]
Thus the limiting second-moment fluctuation variance is precisely
\[
2\left(\int Q_q^4d\nu-\big(\int Q_q^2d\nu\big)^2\right)
=\frac{2(2L-1)(L-1)}{3L^3}>0.
\]

**4. Gaussian linear-statistic fluctuation.** Express \(b_N=g_N/\|g_N\|_2\), with independent standard real Gaussian coordinates. Let \(p_q\) be the even real polynomial with \(p_q(i x)=Q_q(x)\), and put \(B_N=p_q(S_N)^\mathsf Tp_q(S_N)=p_q(S_N)^2\). The matrices \(B_N\) are uniformly bounded real symmetric matrices, with \(N^{-1}\operatorname{tr}B_N=1/L+O(N^{-1})\) and \(N^{-1}\operatorname{tr}B_N^2\to\int Q_q^4d\nu\). Orthogonally diagonalizing each \(B_N\) and applying the Lindeberg central limit theorem to its bounded weighted sums of centered independent Gaussian squares, jointly with \(N^{-1}\|g_N\|_2^2\), gives
\[
\sqrt N\left(b_N^\mathsf T B_N b_N-\frac1L\right)
\xrightarrow{\mathrm d}\mathcal N\!\left(0,2\left[\int Q_q^4d\nu-\frac1{L^2}\right]\right).
\]
The normalization by \(\|g_N\|_2\) is essential for the subtraction of the squared mean.

**5. Adaptation of the optimizing residual polynomial.** Define the random spectral moment functional \(\mu_N(f)=b_N^\mathsf T f(-iS_N)b_N\) for even real polynomials \(f\); this has the real spectral interpretation from Step 2. Its fixed finitely many moments converge to those of \(\nu\) with error \(O_{\mathbb P}(N^{-1/2})\). Let \(c_N\in\mathbb R^q\) denote the minimizer coefficients in \(Q_N(x)=1+\sum_{j=1}^q c_{N,j}x^{2j}\), and let \(c_*\) be the coefficients of \(Q_q\). Since the limiting Gram matrix \((\int x^{2i+2j}d\nu)_{1\le i,j\le q}\) is strictly positive definite, standard finite-dimensional inverse-matrix perturbation gives \(c_N-c_*=O_{\mathbb P}(N^{-1/2})\). Completing the square in the quadratic objective gives exactly
\[
\mu_N(Q_N^2)-\mu_N(Q_q^2)
=-(c_N-c_*)^\mathsf T G_N(c_N-c_*)=O_{\mathbb P}(N^{-1}),
\]
where \(G_N\) is the random monomial Gram matrix, bounded in probability. Therefore the true minimum squared residual has the same \(\sqrt N\)-limit as the fixed polynomial in Step 4. Finally the delta method at the positive value \(1/L\), with derivative \(\sqrt L/2\), gives the asserted norm variance \((2L-1)(L-1)/(6L^2)\). This completes the proof.

## Verification
The standalone `verify.py` uses only the Python standard library and prints `VERIFY_OK 5540` on successful execution. It checks exact rational Chebyshev and Dirichlet moments, each normal equation, the two variance formulas for \(1\le q\le8\), finite-matrix odd-step stagnation, spectral quadrature convergence, and seeded Gaussian sanity checks. Those finite calculations do not certify the CLT; the argument above supplies the infinite-dimensional proof. Reproduce with `python3 verify.py`.

## Relationship to prior work
Chen and Soodhalter (2026) study which GMRES residual curves can occur for tridiagonal Toeplitz matrices and illustrate their theory with finitely many random starting seeds; their statement is about attainable curves, not the distribution of fixed-step random-start residuals or its asymptotic Gaussian variance. Liesen and Strakoš (2004), and Li and Zhang (2007 preprint), analyze deterministic Toeplitz GMRES residuals and bounds, including selected right-hand sides. Titley-Peloquin, Pestana and Wathen (2013/2014) provide the spectral weighted least-squares formulation for fixed right-hand sides. These are foundational for the reduction but do not state the particular real-Haar sharp fixed-step fluctuation law. Standard Haar quadratic-form central limit theory and Chebyshev reproducing kernels are used openly in the proof; the contribution claimed here is their fully quantified GMRES specialization, including the parity effect and exact variance. The 2022 CG/MINRES sample-covariance CLT studies a random-matrix ensemble and different algorithms rather than this deterministic skew stencil with a random right-hand side. No claim of broad uniqueness or priority over unindexed equivalent special cases is made.

## Limitations
The normal approximation is asymptotic in the dimension for each **fixed** \(q\), with no uniform iteration-length error bound. The result is for real Haar starts, a zero-diagonal skew stencil, and exact arithmetic; finite-dimensional simulations do not determine an infinite-dimensional distribution. It does not imply iteration-complexity statements for fixed tolerances or perturbations of the Toeplitz stencil. Historical-priority risk remains from possible unstated specializations of general weighted spectral GMRES analyses and Gaussian quadratic-form fluctuation results. No independent mathematical validation has been performed.

## References
- F. Chen and K. M. Soodhalter, *Constraints on admissible behavior of GMRES applied to tridiagonal Toeplitz systems*, arXiv:2609.24751, initially public 2026-09-21, https://arxiv.org/abs/2609.24751.
- J. Liesen and Z. Strakoš, *Convergence of GMRES for tridiagonal Toeplitz matrices*, 2004, https://www.karlin.mff.cuni.cz/~strakos/download/2004_LiSt.pdf.
- R.-C. Li and W. Zhang, *The Rate of Convergence of GMRES on a Tridiagonal Toeplitz Linear System*, Technical Report 2007-12, https://cdn.prod.web.uta.edu/-/media/project/website/science/mathematics/documents/preprint/2007/rep2007_12.pdf.
- D. Titley-Peloquin, J. Pestana and A. J. Wathen, *GMRES convergence bounds that depend on the right-hand-side vector*, IMA Journal of Numerical Analysis 34 (2014), 462–479, https://doi.org/10.1093/imanum/drt025 (2013 accepted manuscript: https://ora.ox.ac.uk/objects/uuid%3A682cdddf-e26c-4540-bb82-37ab23d09648).
- *Central Limit Theorem for the Residuals and Error of CG and MINRES on Sample Covariance Matrices*, Communications on Pure and Applied Mathematics (2022), https://doi.org/10.1002/cpa.22081.
