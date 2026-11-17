# A gamma spectral law for fixed-area hyperbolic annuli in analytic wavelet localization

## Finding

For every real \(\rho>0\) and \(h>0\), consider the probability-normalized weighted analytic Bergman space \(\mathcal A^2_{\rho-1}(\mathbb D)\) with norm
\[
\|f\|_\rho^2=\frac{\rho}{\pi}\int_{\mathbb D}|f(z)|^2(1-|z|^2)^{\rho-1}\,dx\,dy.
\]
For each \(u>1\), define the centered annulus
\[
\Omega_{u,h}=\left\{z\in\mathbb D:1-\frac1u<|z|^2<1-\frac1{u+h}\right\}.
\]
It has constant normalized hyperbolic area
\[
\frac1\pi\int_{\Omega_{u,h}}(1-|z|^2)^{-2}\,dx\,dy=h.
\]
Let \(T_{u,h}\) be the positive localization operator determined by
\[
\langle T_{u,h}f,g\rangle_\rho
=\frac\rho\pi\int_{\Omega_{u,h}} f(z)\overline{g(z)}(1-|z|^2)^{\rho-1}\,dx\,dy.
\]
The normalized monomials are a complete eigenbasis, with eigenvalues
\[
\lambda_n(u,h)=\frac1{B(n+1,\rho)}\int_{1-1/u}^{1-1/(u+h)}t^n(1-t)^{\rho-1}\,dt,
\qquad n=0,1,\ldots.
\]
This diagonal representation is a specialization of previously known radial-Bergman localization formulas; the claims below concern its complete maximizing-mode transitions and its sharp *moving-annulus* spectral scaling.

**Exact frequency staircase.** Define
\[
R_\rho(u,h)=\rho\,\frac{\log(1+h/u)}{\log\!\left(1+\dfrac{h}{(u+h)(u-1)}\right)}.
\]
For fixed \(\rho,h>0\), this is strictly increasing from \(0\) to \(\infty\) as \(u\) increases from \(1\) to \(\infty\). If \(R_\rho(u,h)\notin\mathbb Z\), the unique maximally concentrated monomial degree is \(\lfloor R_\rho(u,h)\rfloor\). If \(R_\rho(u,h)=k\in\{1,2,\ldots\}\), precisely degrees \(k-1\) and \(k\) tie for the norm. Each transition therefore occurs once and only once.

**Boundary spectral law.** For every fixed \(x>0\), uniformly for \(x\) in compact subintervals of \((0,\infty)\),
\[
\boxed{\lim_{u\to\infty}u\,\lambda_{\lfloor ux\rfloor}(u,h)
=F_{\rho,h}(x):=\frac{h}{\Gamma(\rho)}x^\rho e^{-x}.}
\]
Every maximizing degree \(n_*(u)\) obeys \(n_*(u)/u\to\rho\), and consequently
\[
\boxed{\lim_{u\to\infty}u\,\|T_{u,h}\|=
\frac{h\rho^\rho e^{-\rho}}{\Gamma(\rho)}.}
\]
The trace is exactly \(\operatorname{tr}(T_{u,h})=\rho h\) for *every* \(u>1\), whereas, for every fixed real \(q>0\),
\[
\boxed{\lim_{u\to\infty}u^{q-1}\operatorname{tr}(T_{u,h}^q)
=\frac{h^q\Gamma(\rho q+1)}{\Gamma(\rho)^q q^{\rho q+1}}.}
\]
In particular the effective spectral rank satisfies
\[
\boxed{\frac{(\operatorname{tr}T_{u,h})^2}{\operatorname{tr}(T_{u,h}^2)}
\sim u\,\frac{2^{2\rho+1}\rho^2\Gamma(\rho)^2}{\Gamma(2\rho+1)},}
\]
whose leading coefficient is independent of the fixed hyperbolic area \(h\).

## Assumptions and scope

All four parameters have the precise domains \(\rho>0\), \(h>0\), \(u>1\), and \(q>0\); in each limit \(u\to\infty\), the other parameters are held fixed. The operator is defined by orthogonal Bergman compression of the *indicator* of the displayed annulus, with probability-normalized Bergman area. The area invariant is specified above: for the customary curvature-\(-1\) Poincaré metric, the unnormalized hyperbolic area is \(4\pi h\). The corresponding normalized analytic-wavelet energy localization is unitarily equivalent through the Cayley/Bergman wavelet representation; the claim does not concern arbitrary mother wavelets. The eigenvalues include multiplicities, and \(T_{u,h}\) is positive trace class. The trace-power formula uses the usual positive functional calculus, including noninteger \(q\).

## Proof

**1. Diagonalization, trace, and compactness.** With \(d\mu_\rho=(\rho/\pi)(1-|z|^2)^{\rho-1}dx\,dy\), one has
\[
\|z^n\|_\rho^2=\rho B(n+1,\rho),\qquad
K_\rho(z,w)=(1-z\overline w)^{-\rho-1}.
\]
The normalized monomials \(e_n(z)=z^n/\sqrt{\rho B(n+1,\rho)}\) give a complete orthonormal basis. Radiality makes the compression diagonal and polar integration yields the stated \(\lambda_n\). For fixed \(u\), its eigenvalues are positive and decay exponentially in \(n\), hence the operator belongs to every Schatten class \(S_q\), \(q>0\). The diagonal kernel identity yields
\[
\sum_{n\ge0}\frac{t^n}{B(n+1,\rho)}=\rho(1-t)^{-\rho-1},\quad 0\le t<1.
\]
Tonelli's theorem and direct integration consequently show
\[
\sum_{n\ge0}\lambda_n
=\rho\int_{1-1/u}^{1-1/(u+h)}(1-t)^{-2}\,dt=\rho h.
\]

**2. Exact comparison of consecutive modes.** Differentiating \(t^{n+1}(1-t)^\rho\) and using
\(B(n+2,\rho)=(n+1)B(n+1,\rho)/(n+\rho+1)\) gives, with \(a=1-1/u\) and \(b=1-1/(u+h)\),
\[
\lambda_{n+1}-\lambda_n
=\frac{a^{n+1}(1-a)^\rho-b^{n+1}(1-b)^\rho}{(n+1)B(n+1,\rho)}.
\]
The sign is positive, zero, or negative according as \(n+1\) is smaller than, equal to, or greater than \(R_\rho(u,h)\). This establishes unimodality and the exact one-mode/two-mode alternatives.

To prove uniqueness of every transition in \(u\), let
\[
w_u(t)=\frac1{(u+t)(u+t-1)},\qquad0\le t\le h.
\]
Integration gives
\[
\frac{R_\rho(u,h)}\rho=
\frac{\int_0^h(u+t-1)w_u(t)\,dt}{\int_0^h w_u(t)\,dt}.
\]
Differentiating a normalized weighted mean, with \(\mathbb E_u\) denoting expectation under normalized \(w_u\,dt\), yields
\[
\frac1\rho\frac{dR_\rho}{du}
=1+\operatorname{Cov}_u\left(t,-\frac1{u+t}-\frac1{u+t-1}\right)>1.
\]
The second covariance argument is strictly increasing in \(t\), so its covariance with \(t\) is strictly positive on an interval of nonzero length. The explicit logarithmic expression gives \(R_\rho\to0\) as \(u\downarrow1\), while the weighted-mean formula bounds \(R_\rho/\rho\) strictly between \(u-1\) and \(u+h-1\). Thus \(R_\rho/u\to\rho\), proving all assertions about transitions and maximizing-degree scaling.

**3. Pointwise gamma spectral profile.** In the beta integral substitute \(y=u(1-t)\), obtaining the exact expression
\[
\lambda_n(u,h)=\frac{u^{-\rho}}{B(n+1,\rho)}
\int_{u/(u+h)}^1 (1-y/u)^n y^{\rho-1}\,dy.
\]
If \(n/u\to x\in(0,\infty)\), the beta coefficient obeys
\(B(n+1,\rho)^{-1}\sim n^\rho/\Gamma(\rho)\), the integration interval has length \(h/(u+h)\sim h/u\), and the integrand converges uniformly there to \(e^{-x}\). All statements remain uniform for \(x\) in compact subsets of \((0,\infty)\), giving \(u\lambda_n\to F_{\rho,h}(x)\). Since \(F_{\rho,h}\) has its unique maximum at \(x=\rho\), and Step 2 puts every maximizer at a degree with ratio tending to \(\rho\), the operator-norm constant follows.

**4. The complete positive Schatten-moment law.** For all \(u\ge\max\{2,h\}\) and all \(n\ge0\), the gamma ratio and the annulus width furnish a bound, with \(C\) depending only on \(\rho,h\),
\[
0\le u\lambda_n(u,h)\le C\left(\frac{n+1}{u}\right)^\rho e^{-n/(2u)}.
\]
Indeed, \(B(n+1,\rho)^{-1}\le C_\rho(n+1)^\rho\); on the integration interval \((1-t)^{\rho-1}\le C_{\rho,h}u^{1-\rho}\), \(b-a\le h/u^2\), and \(t^n\le b^n\le e^{-n/(2u)}\). Therefore the \(q\)-powers of the scaled eigenvalues are dominated by an integrable polynomial-times-exponential envelope on the rescaled index lattice for every fixed \(q>0\), including \(q<1\). Splitting at fixed small and large \(n/u\), using the estimate on the tails, and applying the compact-uniform profile from Step 3 gives the Riemann-sum limit
\[
\frac1u\sum_{n\ge0}[u\lambda_n(u,h)]^q
\longrightarrow\int_0^\infty F_{\rho,h}(x)^q\,dx
=\frac{h^q}{\Gamma(\rho)^q}\frac{\Gamma(\rho q+1)}{q^{\rho q+1}}.
\]
Rearrangement proves the displayed Schatten formula. Setting \(q=2\), dividing the exact squared trace by the asymptotic second trace, and simplifying gives the effective-rank limit. This completes the proof.

## Verification

The included `check_annular_wavelet.py` uses independent 48-point Gaussian quadrature, incomplete beta functions, comparisons of forward differences and tied modes, and large-\(u\) spot checks. It passed 3,960 numerical assertions upon replay. These observations are finite checks only; the proof of all unbounded quantifiers is the beta-integral argument, the positive covariance, and the dominated Riemann-sum theorem above. The script requires Python, NumPy, and SciPy; run with `python check_annular_wavelet.py`.

## Relationship to prior work

Abreu, Mouayn, and Voigtlaender derived the radial beta-prime eigenvalue representation for wavelet/Bergman localization on hyperbolically equidistributed Cantor unions of annuli (their Proposition 4.1). Thus **radial diagonalization and the existence of beta-prime eigenvalues are prior work**, not asserted as new here. Their estimates address fractal unions with growing hyperbolic area and do not state the present exact fixed-area single-annulus frequency staircase, sharp boundary gamma profile, full positive Schatten-moment limits, or area-independent effective-rank coefficient.

Ramos and Tilli proved that pseudohyperbolic disks maximize analytic-wavelet energy concentration among sets of prescribed hyperbolic area. Their global optimizer is a disk, whereas the present theorem addresses the spectral behavior of a constrained non-optimal annular family as it escapes to the boundary. Abreu and Dörfler's inverse localization results characterize geometric domains from eigenfunctions rather than these joint thin-annulus spectral limits.

Maximenko and Pacheco studied general radial-measure Bergman Toeplitz diagonalization. The centered-circle harmonic Bergman trace staircase is a diagonal **boundary trace** problem, while the present operator is the positive area-compression by a moving annulus; the spectral-filling result for unbounded hyperbolic-distance costs is likewise not an annular concentration asymptotic. General formulas from these papers are compatible with, and can serve as ingredients for, the present argument; the claimed contribution is the additional sharp classification and scaling law, not the underlying diagonalization.

## Limitations

The theorem fixes the Bergman exponent and annulus invariant area before letting its center approach the unit circle; no joint scaling of \(h\) with \(u\), nonconcentric annuli, or nonanalytic wavelet family is covered. Its Schatten limits have asymptotic errors, not finite-\(u\) universal error bars. The precise eigenvalue integral is already supplied by radial Toeplitz theory; an earlier unindexed derivation of the present exact staircase or thin-annulus gamma/Schatten limits remains a genuine historical-priority risk. No independent mathematical audit is claimed.

## References

1. L. D. Abreu, Z. Mouayn and F. Voigtlaender, *A fractal uncertainty principle for Bergman spaces and analytic wavelets*, arXiv:2201.11705 (first posted January 27, 2022), especially Sections 2–4, Proposition 4.1, and the ensuing norm estimates. https://arxiv.org/abs/2201.11705
2. J. P. G. Ramos and P. Tilli, *A Faber–Krahn inequality for wavelet transforms*, arXiv:2205.07998 (first posted May 16, 2022), especially Sections 1–4. https://arxiv.org/abs/2205.07998
3. L. D. Abreu and M. Dörfler, *An Inverse Problem for Localization Operators*, arXiv:1202.5841 (2012). https://arxiv.org/abs/1202.5841
4. E. A. Maximenko and C. Pacheco, *Toeplitz operators in Bergman space induced by radial measures*, arXiv:2503.23649 (2025). https://arxiv.org/abs/2503.23649
5. *Exact frequency staircase for weighted harmonic Bergman circle traces*, public mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-frequency-staircase-for-weighted-harmonic-bergman-circle-t--e5356e299a36
6. *The positive second-order gap in hyperbolic Bergman spectral filling*, public mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-positive-second-order-gap-in-hyperbolic-bergman-spectral-fil--c6321f2aae5a
