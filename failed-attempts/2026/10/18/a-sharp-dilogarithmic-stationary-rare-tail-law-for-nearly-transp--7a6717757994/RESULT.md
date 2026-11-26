# A sharp dilogarithmic stationary rare-tail law for nearly transparent Brownian resetting

## Finding

Let standard Brownian motion on \(\mathbb R\), with generator \(\tfrac12\partial_{xx}\), undergo independent rate-one Poisson resets \(x\mapsto cx\), where \(0<c<1\). Write \(X_c\) for its stationary position and \(\delta=1-c^2\). For every **fixed** \(y>0\), define

\[
\Lambda(\theta)=\operatorname{Li}_2(\theta^2/2)
=\sum_{m=1}^\infty\frac{(\theta^2/2)^m}{m^2},
\qquad |\theta|<\sqrt2.
\]

There is a unique \(t_y\in(0,\sqrt2)\) satisfying

\[
y=\Lambda'(t_y)=-\frac2{t_y}\log(1-t_y^2/2).
\]

Set \(I(y)=yt_y-\Lambda(t_y)\). The **sharp stationary upper-tail asymptotic, including its relative-error-one prefactor**, is

\[
\boxed{\displaystyle
\mathbb P\!\left(X_c\ge\frac y\delta\right)
\sim\frac{\sqrt\delta}{t_y\sqrt{2\pi\Lambda''(t_y)}}
\left(\frac{e^{-\Lambda(t_y)}}{1-t_y^2/2}\right)^{1/2}
\exp\!\left(-\frac{I(y)}\delta\right),\qquad c\uparrow1.}
\]

Here \(\Lambda''(t_y)>0\). By symmetry, the same expression applies to \(\mathbb P(X_c\le-y/\delta)\). This is stronger than an ordinary large-deviation principle, which captures only the exponential factor. In particular, the multiplicative correction
\(\exp(B(t_y))=[e^{-\Lambda(t_y)}/(1-t_y^2/2)]^{1/2}\)
comes from the discrete geometrically weighted stationary perpetuity and is absent if its log moment generating function is replaced only by its first-order continuum limit.

## Assumptions and scope

The Poisson process has rate one and is independent of Brownian increments. At each Poisson jump, only the current position is multiplied by \(c\); there is no additive reset displacement. The invariant distribution is taken before the limit \(c\uparrow1\). The theorem holds for each fixed real threshold \(y>0\), with an asymptotic ratio tending to one. No assertion of uniformity as \(y\downarrow0\), \(y\to\infty\), or \(y=y(c)\) varies with \(c\) is made. The analogous assertion for a negative threshold uses symmetry. This is a statement about the stationary *one-time marginal*, not the distribution of time averages.

## Proof

**1. Known stationary perpetuity and exact transform.** Looking backward from a stationary time, the current Poisson age and successive preceding interarrival times are iid rate-one exponential random variables. The independent Brownian increment over such a time has symmetric Laplace density

\[
\ell(x)=\frac{e^{-\sqrt2|x|}}{\sqrt2},\qquad
\mathbb E e^{\theta L}=(1-\theta^2/2)^{-1}\quad (|\theta|<\sqrt2).
\]

Consequently the stationary marginal has the convergent representation

\[
X_c\overset d=\sum_{j=0}^\infty c^j L_j,
\quad L_j\text{ iid with density }\ell.
\]

Existence follows from \(\sum_j\operatorname{Var}(c^jL_j)=\delta^{-1}<\infty\); uniqueness follows by coupling two solutions using the same Brownian path and resets, since their difference is multiplied by \(c^{N_t}\to0\) almost surely. Its exact moment generating function is

\[
M_c(\theta)=\mathbb E e^{\theta X_c}
=\prod_{j=0}^\infty\left(1-\frac{\theta^2c^{2j}}2\right)^{-1}.
\]

The fixed-parameter perpetuity and transform are known, and are **not** asserted to be new.

**2. The order-one Euler–Maclaurin correction.** Put \(q=c^2=1-\delta\) and \(h=-\log q\). For \(\theta\) in any fixed compact subset of \((-\sqrt2,\sqrt2)\), let

\[
f_\theta(s)=-\log(1-\theta^2e^{-s}/2).
\]

This smooth function and every needed derivative decay exponentially as \(s\to\infty\), uniformly on compact \(\theta\)-sets. The first Euler–Maclaurin endpoint formula with a summable derivative remainder gives, also after differentiating finitely many times in \(\theta\),

\[
\sum_{j=0}^\infty f_\theta(jh)
=\frac1h\int_0^\infty f_\theta(s)\,ds+\frac12f_\theta(0)+O(h).
\]

The integral is \(\Lambda(\theta)\), by the absolutely convergent power series. As \(h=\delta+\delta^2/2+O(\delta^3)\),

\[
\boxed{\log M_c(\theta)=\frac{\Lambda(\theta)}\delta+B(\theta)+O(\delta),
\quad B(\theta)=\frac12\big[-\log(1-\theta^2/2)-\Lambda(\theta)\big].}
\]

The remainder is locally uniform together with the first three \(\theta\)-derivatives. Differentiating the integral yields

\[
\Lambda'(\theta)=-\frac2\theta\log(1-\theta^2/2),\qquad
\Lambda''(\theta)=\int_0^\infty\frac{e^{-s}(1+\theta^2e^{-s}/2)}{(1-\theta^2e^{-s}/2)^2}\,ds>0.
\]

The derivative \(\Lambda'\) increases continuously from zero to infinity on \((0,\sqrt2)\); hence \(t_y\) is well defined and unique for every \(y>0\).

**3. Gaussian local limit under the exact exponential tilt.** For fixed \(t=t_y\), define the tilted probability \(Q_{c,t}\) by

\[
\frac{dQ_{c,t}}{dP}=\exp\big(tX_c-\log M_c(t)\big).
\]

Under \(Q_{c,t}\), the Laplace summands remain independent, with their individual tilted distributions. Set \(Y_c=\delta X_c\), and \(U_c=(Y_c-y)/\sqrt\delta\). The cumulant expansion gives

\[
\mathbb E_{Q_{c,t}}Y_c=y+O(\delta),\qquad
\operatorname{Var}_{Q_{c,t}}Y_c=\delta\Lambda''(t)+O(\delta^2).
\]

For every fixed real \(u\), expansion of the complex cumulant in a disk about \(t\) (possible since \(t<\sqrt2\)) gives

\[
\mathbb E_{Q_{c,t}}e^{iuU_c}\longrightarrow
\exp[-u^2\Lambda''(t)/2].
\]

We verify the stronger **uniform density local limit** rather than assuming it. Let \(\varphi_c(u)\) denote this characteristic function. For the \(j\)-th tilted summand, its modulus at Fourier argument \(u\sqrt\delta\) obeys the exact bound

\[
\left|\frac{1-t^2q^j/2}{1-(t+iu\sqrt\delta)^2q^j/2}\right|^2
=\frac{(1-a_j)^2}{(1-a_j)^2+(1+a_j)\delta u^2q^j+\delta^2u^4q^{2j}/4}
\le\frac1{1+\delta u^2q^j},\qquad a_j=t^2q^j/2.
\]

Choose \(N=\lfloor(2\delta)^{-1}\rfloor\). For all sufficiently small \(\delta\), \(q^j\ge e^{-1}\) for \(0\le j<N\). Multiplication of the first \(N\) factors gives

\[
|\varphi_c(u)|\le(1+e^{-1}\delta u^2)^{-N/2}.
\]

On \(|u|\le\delta^{-1/2}\), \(\log(1+v)\ge v/(1+v)\) gives a uniform Gaussian majorant \(\exp(-A u^2)\) for a fixed \(A>0\). On \(|u|>\delta^{-1/2}\), the remaining integral is bounded by

\[
2\delta^{-1/2}\int_1^\infty(1+e^{-1}v^2)^{-N/2}\,dv\longrightarrow0,
\]

since the integral decays exponentially in \(N\) (use the integrable majorant \((1+e^{-1}v^2)^{-2}\) times the factor \((1+e^{-1})^{-(N-4)/2}\) for \(N\ge4\)). Thus \(\varphi_c\to\exp[-u^2\Lambda''(t)/2]\) in \(L^1(\mathbb R)\). Fourier inversion gives continuous densities \(g_c\) of \(U_c\) with

\[
\sup_{z\in\mathbb R}\left|g_c(z)-\frac1{\sqrt{2\pi\Lambda''(t)}}e^{-z^2/(2\Lambda''(t))}\right|\to0.
\]

**4. Tail integration at the exact threshold.** The change of measure implies, for \(y>0\),

\[
\mathbb P(Y_c\ge y)=e^{-ty/\delta}M_c(t)\,
\mathbb E_{Q_{c,t}}[e^{-t(Y_c-y)/\delta}\mathbf1_{\{Y_c\ge y\}}].
\]

The density of \(Y_c\) under the tilt is \(\delta^{-1/2}g_c((z-y)/\sqrt\delta)\). Writing \(z=y+\delta v\) yields

\[
\mathbb E_{Q_{c,t}}[e^{-t(Y_c-y)/\delta}\mathbf1_{\{Y_c\ge y\}}]
=\sqrt\delta\int_0^\infty e^{-tv}g_c(v\sqrt\delta)\,dv
\sim\frac{\sqrt\delta}{t\sqrt{2\pi\Lambda''(t)}}.
\]

Uniform convergence of the densities and integrability of \(e^{-tv}\) justify the last limit by dominated convergence. Finally \(e^{-ty/\delta}M_c(t)=e^{-I(y)/\delta+B(t)+O(\delta)}\) by Step 2. Multiplication gives the boxed asymptotic, with a **relative** error tending to zero. Symmetry supplies the left tail. This establishes every stated quantifier; no finite numerical experiment is used to prove the limit.

## Verification

Run \(\texttt{python3 checker.py}\) with Python 3 standard library from the accompanying standalone package. The checker verifies exact stationary-generator moment identities, numerical dilogarithm and saddlepoint equations, and the order-one Euler–Maclaurin endpoint correction against geometric-product partial sums. These are finite verification checks; the uniform Fourier inversion in Step 3 and the asymptotic ratio in Step 4 are justified by the analytical bounds above, not by simulations or the checker.

## Relationship to prior work

Assefa, Keller-Ressel and Palmowski (2026) treat polynomial-process moments under affine resetting and include proportional Brownian resets; this supplies the recent model-level motivation but does not state the sharp stationary tail formula. The known invariant perpetuity and exact generating product are described in Di Bello and collaborators (2023), Grzywny and collaborators (2024), and Kolb–Wübker (2026). They are cited as prior results, not repackaged as new.

The logarithmic large-deviation rate itself is **not** a stand-alone originality claim: Vysotsky (2021, Theorem 6.1) and Najim (2002) treat much more general kernel-weighted-sum large-deviation principles, and the dilogarithmic rate follows from the geometric Laplace kernel. Classical exponential tilting and saddlepoint theory also motivate the proof. The full-text asymptotic expansion of van Leeuwaarden and Temme (2011) treats **finite power-weighted sums of positive exponential variables**, not this infinite geometric sum of symmetric Laplace variables. What is assessed here is the explicit **sharp relative-error asymptotic** with its precise \(\sqrt\delta\) scale and the nontrivial, exactly evaluated \(\exp(B(t_y))\) factor for this near-transparent-reset stationary law. The inspected cited works do not state or evaluate that model-specific correction. Broader exact saddlepoint expansions might encompass the statement after additional work, which remains a priority risk.

## Limitations

The formula is pointwise for \(y>0\); no uniform two-scale crossover at \(y\downarrow0\), large-threshold joint limit, or pathwise large-deviation statement is proved. Only one-dimensional Brownian motion with rate-one Poisson resets and a deterministic contraction is covered. Independence of Poisson intervals is essential to the exhibited transform. The mathematical review is not independent external validation.

## References

1. J. Assefa, M. Keller-Ressel, Z. Palmowski, *Moments of polynomial processes under affine resetting* (2026), arXiv:2610.01363v1, first submitted 2026-10-01.
2. C. Di Bello et al., *Time-dependent probability density function for partial resetting dynamics* (2023), arXiv:2305.13722, especially the stationary Fourier product.
3. T. Grzywny et al., *Stationary states for stable processes with partial resetting* (2024), arXiv:2412.15626, stationary and asymptotic distribution results.
4. M. Kolb and A. Wübker, *Brownian Motion With Partial Resetting Conditioned to Stay Positive*, Bulletin of the London Mathematical Society (2026), doi:10.1112/blms.70314.
5. V. Vysotsky, *Contraction principle for trajectories of random walks and Cramér's theorem for kernel-weighted sums*, ALEA 18 (2021), 1103–1125, doi:10.30757/ALEA.v18-42, Theorem 6.1.
6. J. Najim, *A Cramér type theorem for weighted random variables*, Electronic Journal of Probability 7 (2002), paper 4, pp. 1–32.
7. R. Kiesel and U. Stadtmüller, *A large deviation principle for weighted sums of independent identically distributed random variables*, Journal of Mathematical Analysis and Applications 251 (2000), 929–939.
8. J. S. H. van Leeuwaarden and N. M. Temme, *A uniform asymptotic expansion for weighted sums of exponentials*, Statistics & Probability Letters 81 (2011), 1571–1579, author manuscript at https://ir.cwi.nl/pub/18559/18559B.pdf.
9. H. E. Daniels, *Saddlepoint Approximations in Statistics*, Annals of Mathematical Statistics (1954), general saddlepoint methodology.
