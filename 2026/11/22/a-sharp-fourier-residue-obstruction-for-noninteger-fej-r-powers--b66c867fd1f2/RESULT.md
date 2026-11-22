# A sharp Fourier-residue obstruction for noninteger Fejér powers

## Finding

For every integer \(N\ge2\) and every real exponent \(\gamma\ge0\), put
\[
F_N(\theta)=\frac{1}{N}\left|\sum_{k=0}^{N-1}e^{ik\theta}\right|^2
=\frac{1}{N}\left(\frac{\sin(N\theta/2)}{\sin(\theta/2)}\right)^2,
\qquad K_{N,\gamma}(\theta)=F_N(\theta)^\gamma.
\]
At zeros, positive real powers are defined by continuity; the zero-th power is the constant one. Then the stationary circle kernel \(K_{N,\gamma}(x-y)\) is positive semidefinite on every finite point set **if and only if** \(\gamma\) is a nonnegative integer.

More precisely, for each \(\gamma>0\) that is not an integer define the real numbers
\[
S_{N,\gamma}(r)=\sum_{j=1}^{N-1}
\left[\frac{N}{4\sin^2(\pi j/N)}\right]^\gamma
\cos\left(\frac{2\pi rj}{N}\right),\qquad r=0,\ldots,N-1.
\]
For the normalized Fourier coefficients \(\widehat K_{N,\gamma}(m)=(2\pi)^{-1}\int_0^{2\pi}K_{N,\gamma}(\theta)e^{-im\theta}\,d\theta\), the sharp residue-class law is
\[
\boxed{\widehat K_{N,\gamma}(m)=-\frac{\Gamma(2\gamma+1)\sin(\pi\gamma)}{\pi\,m^{2\gamma+1}}\,
S_{N,\gamma}(m\bmod N)+O_{N,\gamma}(m^{-2\gamma-2})}\qquad(m\longrightarrow+\infty).
\]
Here \(S_{N,\gamma}(0)>0\), \(\sum_{r=0}^{N-1}S_{N,\gamma}(r)=0\), and at least one \(S_{N,\gamma}(r)\) is negative. Thus each noninteger exponent generates *infinitely many strictly negative Fourier coefficients* along at least one explicit arithmetic progression. The asymptotic only asserts an eventual sign where its leading residue constant is nonzero; no sign is asserted from the leading term on a residue class where it vanishes.

## Assumptions and scope

The group is \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with normalized Haar measure and the convention \(\widehat f(m)=(2\pi)^{-1}\int_0^{2\pi} f(\theta)e^{-im\theta}\,d\theta\). Positive semidefinite means that \((K(x_j-x_k))_{j,k=1}^M\) is Hermitian positive semidefinite for **every** positive integer \(M\) and every \(x_1,\ldots,x_M\in\mathbb T\). Repeated points are permitted. The theorem holds for fixed \(N\) and fixed \(\gamma\); no uniformity in either parameter is claimed for the error term or the onset of signs. Values at removable singularities of \(F_N\) are taken by continuity, so \(F_N(0)=N\).

## Proof

**1. Integer powers preserve positive type.** The elementary identity
\[
F_N(\theta)=\sum_{|k|<N}\left(1-\frac{|k|}{N}\right)e^{ik\theta}
\]
shows that every Fourier coefficient is nonnegative. For any nonnegative integer \(q\), the Fourier coefficient sequence of \(F_N^q\) is the \(q\)-fold discrete convolution of a nonnegative finite sequence, with the case \(q=0\) giving the constant kernel. Every coefficient is therefore nonnegative. The circle Bochner–Herglotz criterion gives positive semidefiniteness.

**2. A local singularity transform.** For fixed real \(\beta>0\) not in \(2\mathbb Z_{\ge0}\), let \(\chi\) be smooth, compactly supported, and identically one near the origin. With Fourier phase \(e^{-imu}\), one has, as \(m\to+\infty\),
\[
\int_{\mathbb R}\chi(u)|u|^\beta e^{-imu}\,du
=-2\Gamma(\beta+1)\sin(\pi\beta/2)m^{-\beta-1}
+O_{\chi,\beta,L}(m^{-L})
\]
for every fixed \(L>\beta+1\). To reconstruct this formula, first insert \(e^{-\varepsilon|u|}\) in the full-power distribution. Its even transform is
\[
2\Gamma(\beta+1)\operatorname{Re}(\varepsilon+im)^{-\beta-1},
\]
which tends off frequency zero to \(-2\Gamma(\beta+1)\sin(\pi\beta/2)m^{-\beta-1}\). For \(-1<\beta<0\) this follows directly from the absolutely integrable Laplace-regularized integral, and all other non-even exponents follow by the distributional differentiation identity and analytic continuation in the exponent. Replacing the full-power distribution by its localized version changes its Fourier transform, away from frequency zero, by \(O(m^{-L})\) for arbitrary fixed \(L>\beta+1\): the difference is smooth near zero and its derivatives of such orders are integrable at infinity, so repeated distributional integration by parts applies. Furthermore, if \(a\) is smooth near zero, Taylor expansion of \(a(u)\) and the same transform identity applied to \(u^k|u|^\beta\) yield
\[
\frac{1}{2\pi}\int\chi(u)|u|^\beta a(u)e^{-imu}\,du
=-\frac{\Gamma(\beta+1)\sin(\pi\beta/2)}{\pi}\,a(0)m^{-\beta-1}
+O(m^{-\beta-2}).
\]
For the Taylor remainder, choose its order larger than \(\beta+3\) and integrate by parts sufficiently many times; a fixed smooth cutoff isolates the singular point. These arguments also justify the stated remainder, not merely a formal distributional leading term.

**3. Contributions from all kernel zeros.** The distinct circle zeros of \(F_N\) are exactly \(\theta_j=2\pi j/N\), \(1\le j\le N-1\). Around each, with local signed coordinate \(u\), direct expansion of the ratio of sines gives
\[
F_N(\theta_j+u)=\frac{N}{4\sin^2(\pi j/N)}u^2\bigl(1+O(u)\bigr).
\]
In fact, the factor after \(u^2\) is smooth and strictly positive near the zero, so raising it to any fixed positive real \(\gamma\) preserves smoothness. Apply the local lemma with \(\beta=2\gamma\) and \(a(0)=[N/(4\sin^2(\pi j/N))]^\gamma\), then restore the Fourier phase \(e^{-im\theta_j}\). A smooth partition of unity around the \(N-1\) zeros has a complementary \(C^\infty\) periodic remainder, whose Fourier coefficients decay faster than every power. Summing produces the boxed residue-class asymptotic. Conjugate zero pairs prove that \(S_{N,\gamma}(r)\) is real.

**4. An unavoidable negative residue class.** For \(\gamma>0\), every summand in \(S_{N,\gamma}(0)\) is positive, hence this sum is strictly positive. The roots-of-unity identity \(\sum_{r=0}^{N-1}e^{-2\pi irj/N}=0\) for \(1\le j<N\) gives \(\sum_r S_{N,\gamma}(r)=0\). Thus some residue has strictly negative \(S\). If \(\sin(\pi\gamma)>0\), take residue \(r=0\); if \(\sin(\pi\gamma)<0\), take any residue with \(S_{N,\gamma}(r)<0\). In either case the leading Fourier coefficient in that residue class is strictly negative and dominates its smaller remainder for all sufficiently large positive frequencies. Therefore every noninteger positive power has infinitely many negative Fourier coefficients, contradicting circle positive semidefiniteness by Bochner–Herglotz. Together with Step 1 this proves both directions.

**5. Finite Gram witnesses.** The coefficient negativity has a direct finite-dimensional meaning. For a fixed negative coefficient at frequency \(m\), let \(M\to\infty\) through integers exceeding \(2m\) and consider equally spaced points \(2\pi j/M\). The circulant Gram matrix has Fourier eigenvalue \(\sum_{j=0}^{M-1}K_{N,\gamma}(2\pi j/M)e^{-2\pi imj/M}\). Dividing by \(M\), the eigenvalue converges by Riemann sums to the negative coefficient. Hence some finite Gram matrix has a negative eigenvalue. This is an existence statement; no uniform finite witness size across \(N,\gamma\) is asserted.

## Verification

The exact one-zero cross-check for \(N=2\) is
\[
\widehat K_{2,\gamma}(m)=\frac{2^{-\gamma}\Gamma(2\gamma+1)}{\Gamma(\gamma-m+1)\Gamma(\gamma+m+1)},
\]
with reciprocal gamma poles understood as zero at integer powers. The included standard-library program `verify_fejer_powers.py` checks nonnegative finite convolution coefficients for integer exponents, exact roots-of-unity residue identities, this gamma quotient in its reflection-stable form for noninteger powers, and sign/magnitude comparisons against direct high-resolution Fourier quadrature for several larger degrees. Its execution completed **313 finite diagnostics**. Analytic steps 2–5, rather than the finite diagnostics, establish the infinite-exponent classification and asymptotic. Running `python verify_fejer_powers.py` prints the PASS count if all finite assertions hold.

## Relationship to prior work

The Fejér-kernel normalization, positive Fourier coefficients, and Cesàro-summation role are classical and given explicitly in the NIST DLMF. Kravitz and Steinerberger (first public preprint 27 July 2020) investigate sharp smoothing under a nonnegative Fourier condition and identify the Fejér triangle multiplier as an extremizer; their stated theorems neither classify real pointwise powers of a fixed Fejér kernel nor give the present nodal-residue Fourier tails. Published work on **integer** powered Fejér–Jackson kernels establishes sharp derivative norms and a Gaussian high-power limit, but those quantities do not imply noninteger positive-type behavior. The new target is the complete real-exponent positivity classification together with its sharp cyclic residue-class obstruction, not classical integer-power positivity itself.

## Limitations

The assertion concerns the **pointwise real power** of a fixed standard Fejér kernel; it does not concern fractional Cesàro means or the fractional Fourier transform, and it does not characterize real powers of arbitrary positive trigonometric polynomials. The sign-forcing arithmetic progression can depend on the exponent and may start at a very high frequency. Leading coefficients can vanish for selected residue classes; their next-order behavior is not classified. Numerical checks cannot verify arbitrary degrees, exponents, or infinitely many modes. Historical priority is provisional pending a wider specialist review of classical results on powers of positive-type functions and singularity-driven Fourier asymptotics. No independent mathematical audit has been carried out.

## References

1. N. Kravitz and S. Steinerberger, *The smoothest average: Dirichlet, Fejér and Chebyshev*, arXiv:2007.13700, first submitted 2020-07-27, https://arxiv.org/abs/2007.13700 . Theorems 1–2, §§1.2–1.5, and their proofs.
2. NIST Digital Library of Mathematical Functions, *§1.15 Summability Methods*, especially (1.15.15)–(1.15.16), https://dlmf.nist.gov/1.15 .
3. *Sharp rough-input Lipschitz norms of powered Fejér–Jackson kernels*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-rough-input-lipschitz-norms-of-powered-fej-r-jackson-kerne--cf9850093a62 ; comparison specifically with the full `RESULT.md` theorem on integer powers.
4. *Fractional Fourier Series on the Torus and Applications*, *Fractal and Fractional* **8** (2024), article 494, https://www.mdpi.com/2504-3110/8/8/494 . The fractional Fejér kernels there involve a rescaled angular variable, not a real power of the ordinary Fejér kernel; the accessible text was reviewed for this distinction.
