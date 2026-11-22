# Sharp Gaussian–Weibull dichotomy under diffusivity-only resetting

## Finding
Let \(r,\Lambda>0\). A Brownian tracer \(X\), started at zero, has stochastic diffusivity \(\omega_t^2\): between independent rate-\(r\) Poisson events,
\[
 d\omega_t=\sqrt2\Lambda\,dB_t,\qquad dX_t=\sqrt2\,\omega_t\,dW_t,
\]
where \(B,W\) are independent standard Brownian motions. At Poisson events, **only** \(\omega\) is set to zero; \(X\) remains continuous. The sign in the tracer noise amplitude is immaterial in law because the driving Brownian motion is independent of \(\omega\).

(a) The bath has unique invariant density
\[
\pi(w)=\frac{\sqrt r}{2\Lambda}\exp\!\left(-\frac{\sqrt r}{\Lambda}|w|\right).
\]
With \(\omega_0\sim\pi\), the tracer satisfies the ordinary central limit theorem
\[
\frac{X_t}{\sqrt t}\Longrightarrow N\!\left(0,\frac{4\Lambda^2}{r}\right)
\qquad(t\to\infty),
\]
yet its standardized excess kurtosis is strictly decreasing and **exactly**
\[
\frac{\mathbb E X_t^4}{(\mathbb E X_t^2)^2}-3
=30\frac{rt-1+e^{-rt}}{(rt)^2}.
\]

(b) For each fixed \(t>0\) under this invariant bath initialization, the exact logarithmic rare-displacement rate is
\[
\boxed{\lim_{x\to\infty}\frac{\log\Pr(|X_t|>x)}{x^{2/3}}
=-\frac3{2^{4/3}}\left(\frac r{\Lambda^2 t}\right)^{1/3}.}
\]
In particular, all nonzero exponential moments \(\mathbb E e^{kX_t}\) are infinite even though all fixed positive integer moments are finite.

(c) By contrast, if the bath begins at \(\omega_0=0\), then for every real \(k\ne0\) and finite \(t>0\),
\[
\mathbb E e^{kX_t}<\infty
\quad\Longleftrightarrow\quad
 2\Lambda|k|t<\frac\pi2.
\]
Thus the exact exponential-moment boundary is independent of the strictly positive bath reset rate.

## Assumptions and scope
The process lives on the whole real line; resetting is instantaneous and independent of both noises. The Brownian clocks have the normalization \(\mathbb E(B_t-B_s)^2=t-s\). The limits in (a) and (b) have different orders: (a) sends observation time to infinity at fixed \(r,\Lambda\), whereas (b) sends displacement threshold to infinity at fixed positive observation time. The explicit fourth-moment and rare-tail statements require the invariant initial bath, while (c) requires deterministic zero initial bath. The Gaussian limit also holds from \(\omega_0=0\).

## Proof
**1. Invariant bath and conditional Gaussianity.** The bath generator is \(\mathcal Lf(w)=\Lambda^2f''(w)+r[f(0)-f(w)]\). Since each completed reset erases its past, the stationary bath is the Gaussian mixture obtained by running \(\sqrt2\Lambda B\) for an independent exponential age \(S\sim\operatorname{Exp}(r)\). Its characteristic function equals \(\mathbb E e^{-\Lambda^2 q^2S}=r/(r+\Lambda^2q^2)\), giving the displayed Laplace density and uniqueness by regeneration. Define the integrated diffusivity \(A_t=\int_0^t\omega_s^2\,ds\). Conditional on the complete bath path and reset clock, the independent-noise stochastic integral satisfies \(X_t\mid A_t\sim N(0,2A_t)\).

**2. Bulk limit.** The regenerative bath is positive recurrent with finite mean return times and finite invariant moments; its ergodic theorem gives \(A_t/t\to\mathbb E_\pi\omega_0^2=2\Lambda^2/r\) almost surely. Consequently
\[
\mathbb E e^{iuX_t/\sqrt t}=\mathbb E e^{-u^2A_t/t}
\longrightarrow e^{-2\Lambda^2u^2/r},
\]
which is the characteristic function of the claimed centered Gaussian distribution. Since \(\mathbb E X_t^2=4\Lambda^2t/r\), there is no stationary tracer position law with finite second moment.

**3. Exact non-Gaussian correction.** The stationary bath moments, obtained from \(\mathcal Lw^2=2\Lambda^2-rw^2\) and \(\mathcal Lw^4=12\Lambda^2w^2-rw^4\), are
\[
\mathbb E_\pi\omega^2=\frac{2\Lambda^2}r,\quad
\mathbb E_\pi\omega^4=\frac{24\Lambda^4}{r^2},\quad
\operatorname{Var}_\pi(\omega^2)=\frac{20\Lambda^4}{r^2}.
\]
The quadratic conditional semigroup gives \(\mathbb E[\omega_s^2\mid\omega_0=w]=2\Lambda^2/r+e^{-rs}(w^2-2\Lambda^2/r)\); hence
\[
\operatorname{Cov}_\pi(\omega_0^2,\omega_s^2)
=\frac{20\Lambda^4}{r^2}e^{-rs}.
\]
Integrating this covariance yields
\[
\operatorname{Var}(A_t)=\frac{40\Lambda^4}{r^2}
\left(\frac tr-\frac{1-e^{-rt}}{r^2}\right).
\]
The conditional Gaussian identity \(\kappa_4(X_t)=12\operatorname{Var}(A_t)\), together with \(\operatorname{Var}(X_t)=2\mathbb E A_t\), gives (a). The identity
\[
\frac{z-1+e^{-z}}{z^2}=\int_0^1(1-s)e^{-zs}\,ds
\]
proves that the excess kurtosis is strictly positive and strictly decreasing for all \(z=rt>0\), with limits \(15\) as \(z\downarrow0\) and asymptotic \(30/z\) as \(z\to\infty\).

**4. Sharp fixed-time tail.** Put \(a=\sqrt r/\Lambda\). At equilibrium \(|\omega_0|\sim\operatorname{Exp}(a)\), independently of future Brownian increments and resets. The conditional normal tail is \(2\overline\Phi(x/\sqrt{2A_t})\). Choose \(\delta>0\), and set \(H_x=\{\sup_{s\le t}|B_s|\le\delta x^{2/3}\}\). The reflection principle gives \(\Pr(H_x^c)\le4e^{-\delta^2x^{4/3}/(2t)}\). On \(H_x\), for any number and arrangement of bath resets,
\[
A_t\le t\bigl(|\omega_0|+2\sqrt2\Lambda\delta x^{2/3}\bigr)^2.
\]
Using \(2\overline\Phi(y)\le2e^{-y^2/2}\), integrating the exponential density of \(|\omega_0|\), and rescaling \(|\omega_0|=y x^{2/3}\) shows that the \(\limsup\) of \(x^{-2/3}\log\Pr(|X_t|>x)\) is bounded above by
\[
-\inf_{y\ge0}\left\{ay+\frac1{4t(y+2\sqrt2\Lambda\delta)^2}\right\}.
\]
Now send \(\delta\downarrow0\). Conversely, require no bath reset on \([0,t]\) (probability \(e^{-rt}\)), \(H_x\), and \(\omega_0\in[yx^{2/3},(y+\varepsilon)x^{2/3}]\). For any fixed \(y>\sqrt2\Lambda\delta\), these events imply
\[
A_t\ge t(y-\sqrt2\Lambda\delta)^2x^{4/3}.
\]
The standard Gaussian-tail logarithmic asymptotic and then \(\varepsilon,\delta\downarrow0\) give the reverse bound for every \(y>0\). Hence the limit is
\[
-\inf_{y>0}\left\{ay+\frac1{4ty^2}\right\}
=-\frac3{2^{4/3}}\left(\frac{a^2}t\right)^{1/3},
\]
with unique minimizer \(y=(2at)^{-1/3}\). The resulting \(\exp[-\Theta(x^{2/3})]\) tail implies divergence of all nontrivial exponential moments. Finite algebraic moments follow from the finite bath moments and bounded observation horizon.

**5. Exact transform-domain boundary for zero-start bath.** For one Brownian excursion of deterministic length \(u\) beginning at zero, Feynman–Kac applied to \(\mathbb E\exp(k^2\int_0^u\omega_s^2ds)\) with quadratic-exponential ansatz yields the Riccati equations
\[
A'=4\Lambda^2A^2+k^2,\qquad B'=2\Lambda^2 A,
\qquad A(0)=B(0)=0,
\]
and therefore
\[
\mathbb E_0\exp\!\left(k^2\int_0^u\omega_s^2ds\right)
=\frac1{\sqrt{\cos(2\Lambda|k|u)}}
\]
for \(u<\pi/(4\Lambda|k|)\), diverging at and beyond that time. For total time \(t\) strictly below the threshold, condition on the finite Poisson count \(N_t\): all excursion lengths are at most \(t\), and their independent transform product is bounded by \(M^{N_t+1}\), where \(M=[\cos(2\Lambda|k|t)]^{-1/2}\). Since \(N_t\) is Poisson, this has finite expectation. At or above the boundary, the positive-probability event \(N_t=0\) alone has infinite transform. This proves (c), including the boundary case.

## Verification
The standalone `check.py` independently integrates the Feynman–Kac Riccati equations, checks stationary generator identities, verifies the exact fourth-cumulant coefficient and its strict monotonicity, reproduces the variational tail constant numerically over multiple physical parameters, and compares the integrated diffusivity with independent finite-step Monte Carlo. The analytical arguments, not the finite numerical checks, establish the all-parameter and rare-tail assertions.

## Relationship to prior work
Santra, Basu and Sabhapandit (arXiv:2205.00549, first posted 1 May 2022) analyze the same Brownian-squared diffusivity with simultaneous resetting of both tracer and bath. Their conclusion specifically lists resetting **only** the diffusion coefficient as a remaining question. That published model attains a stationary tracer density, unlike the present continuously moving tracer. Bodrova, Chechkin and Sokolov (arXiv:1812.05664) study the opposite protocol—position resetting with a prescribed, nonrandom power-law diffusivity unaffected by resets. Zhan and Wang (Phys. Rev. E 109, 044115, 2024) give general random-diffusivity ergodicity criteria; this may subsume generic bulk-ergodic observations, which are not claimed as the novel contribution. The specific reset-only stochastic bath, sharp fixed-time \(2/3\)-Weibull logarithmic constant, exact fourth-cumulant decay, and deterministic-start transform boundary form the assessed contribution.

## Limitations
The logarithmic tail limit does not determine a full algebraic prefactor. It applies at fixed positive time under stationary bath initialization, not uniformly in time or in the reset rate. No first-passage theorem or empirical validation is claimed. Full text of Zhan and Wang (2024) was unavailable at review time, leaving a residual publication-priority risk. Standard Gaussian convergence does not imply finite moment-generating functions; the theorem highlights exactly this distinction. Independent scientific validation has not been performed.

## References
- I. Santra, U. Basu and S. Sabhapandit, *Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient*, arXiv:2205.00549 (1 May 2022), https://arxiv.org/abs/2205.00549.
- A. S. Bodrova, A. V. Chechkin and I. M. Sokolov, *Non-renewal resetting of scaled Brownian motion*, arXiv:1812.05664 (13 December 2018), https://arxiv.org/abs/1812.05664.
- Z. Zhan and X. Wang, *Ergodic criterion of a random diffusivity model*, Phys. Rev. E **109**, 044115 (2024), https://doi.org/10.1103/PhysRevE.109.044115.
