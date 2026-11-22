# Universal refresh-phase cusp and heavy-tail fingerprint in absorbed random walks

## Finding

Let a continuous-time symmetric nearest-neighbor walk on the nonnegative integers start at a fixed integer site \(m\ge1\) and be absorbed on its first visit to zero. Its total jump rate is an independent, nonnegative random variable, redrawn at physical times \(0,\tau,2\tau,\ldots\) with fixed \(\tau>0\). Assume the rate is finite almost surely and its Laplace transform satisfies
\[
\varphi(s):=\mathbb E e^{-s\lambda}=1-cs^\alpha+o(s^\alpha)\quad(s\downarrow0),
\qquad c>0,\quad 0<\alpha\le1.
\]
Write \(S_m(t)=\Pr_m(T>t)\), and \(\nu=1/(2\alpha)\). The survival at completed redraw periods obeys the established leading power law
\[
S_m(n\tau)\sim \frac{m\sqrt2\,\Gamma(\nu)}{\pi\alpha\sqrt\tau}\,c^{-\nu}n^{-\nu}.
\]
The additional result is a **uniform within-period, first-relative-order phase fingerprint**. For every fixed starting site and rate law as above,
\[
\boxed{\quad\lim_{n\to\infty}\sup_{0\le\theta\le1}
\left|n\left[\left(1+\frac\theta n\right)^\nu
\frac{S_m((n+\theta)\tau)}{S_m(n\tau)}-1\right]
-\nu(\theta-\theta^\alpha)\right|=0.\quad}
\]
Thus this phase profile is independent of the starting site, refresh duration, rate scale and all other features of the jump-rate law. For \(0<\alpha<1\) it is strictly negative at every interior phase and has its unique minimum at \(\theta_*=\alpha^{1/(1-\alpha)}\). At the finite-mean boundary \(\alpha=1\) it vanishes identically at this order. For any fixed \(0<\theta<1\), the profile value is strictly increasing in \(\alpha\in(0,1]\), so the heavy-tail index is uniquely encoded by one asymptotic phase contrast.

For \(0<\alpha<1\) there is also a **fractional cusp at every redraw instant**. With
\[
\ell(p)=1-\cos(\pi p),\qquad
A_m(p)=\frac{\sin(m\pi p)\sin(\pi p)}{1-\cos(\pi p)},
\]
define the strictly positive finite coefficient
\[
B_{n,m}=c\int_0^1 A_m(p)\varphi(\tau\ell(p))^n\ell(p)^\alpha\,dp.
\]
For each integer \(n\ge1\),
\[
\boxed{\quad S_m(n\tau+u)=S_m(n\tau)-B_{n,m}u^\alpha+o(u^\alpha)
\quad(u\downarrow0),\qquad
\lim_{n\to\infty}\frac{n\tau^\alpha B_{n,m}}{S_m(n\tau)}=\nu.\quad}
\]
The left time derivative of survival at every positive redraw instant is finite, while its right derivative is \(-\infty\). These two conclusions are aspects of the same rate-law-independent refresh-boundary phenomenon.

## Assumptions and scope

Jumps in either direction have conditional rate \(\lambda_j/2\) on the interval \([j\tau,(j+1)\tau)\). The nonnegative rates \(\lambda_j\) are independent and identically distributed, are finite almost surely, and are independent of all step directions and of the unit-rate spatial walk. The first draw is at time zero. The underlying walk is absorbed immediately upon reaching zero, with no positional resetting, no bias and no reflecting boundary. The stated regular variation is an assumption on the rate law's **small-argument Laplace transform**, not on its density. Rates may have atoms, including one at zero. It implies \(\Pr(\lambda>0)>0\). If \(\alpha=1\), monotone convergence yields \(c=\mathbb E\lambda<\infty\); if \(0<\alpha<1\), the mean is infinite.

The initial distance \(m\), rate distribution, tail exponent and period \(\tau\) remain fixed as the number \(n\) of completed redraw periods tends to infinity. Uniformity holds in the within-period phase \(\theta\) only. The cusp statement requires \(0<\alpha<1\) and each fixed positive integer \(n\); its large-\(n\) amplitude law is a subsequent limit, not a joint \(n,u\) error estimate. All probabilities are averaged over both the rate history and spatial walk.

## Proof

**1. Exact killed-walk spectral identity.** For the total-rate-one nearest-neighbor walk absorbed at zero, the standard sine spectral representation of survival is
\[
h_m(v)=\Pr_m(H>v)=\int_0^1 A_m(p)e^{-v\ell(p)}\,dp.
\]
The elementary identities \(\ell(p)=2\sin^2(\pi p/2)\) and \(A_m(p)=\sin(m\pi p)\cot(\pi p/2)\) show that \(A_m\) is bounded on \([0,1]\) and \(A_m(0)=2m\). (For \(m>1\) the spectral weight need not have one sign.) Independent random time change gives \(X_t\) the law of the unit-rate killed walk observed at \(\Lambda_t=\int_0^t\lambda_{\lfloor v/\tau\rfloor}\,dv\). Since rates are independently resampled, for every integer \(n\ge0\) and \(0\le\theta\le1\),
\[
S_m((n+\theta)\tau)=\int_0^1 A_m(p)
\varphi(\tau\ell(p))^n\varphi(\theta\tau\ell(p))\,dp.\tag{1}
\]
At \(\theta=1\) the last factor simply completes the next full period. This exact formula includes absorption within a refresh interval.

**2. Long-time scale and leading mass.** As \(p\downarrow0\),
\[
\ell(p)=\frac{\pi^2p^2}{2}(1+O(p^2)),\quad
A_m(p)=2m+O_m(p^2),\quad
1-\varphi(\tau\ell(p))\sim a p^{2\alpha},
\quad a=c\tau^\alpha(\pi^2/2)^\alpha.
\]
For each fixed \(\delta>0\), the portion \(p\in[\delta,1]\) of (1) is exponentially small in \(n\), since \(\varphi(\tau\ell(p))\le\rho_\delta<1\). For small \(p\) there are constants \(b_1,b_2>0\) such that \(b_1p^{2\alpha}\le1-\varphi(\tau\ell(p))\le b_2p^{2\alpha}\). Put \(p=(an)^{-\nu}y\). Dominated convergence using the integrable majorant \(C e^{-b y^{2\alpha}}\) gives
\[
S_m(n\tau)\sim 2m(an)^{-\nu}
\int_0^\infty e^{-y^{2\alpha}}dy
=\frac{m\Gamma(\nu)}\alpha a^{-\nu}n^{-\nu},
\]
which is the displayed leading constant.

**3. The first within-period contrast.** Subtract equation (1) at phase \(\theta\) from the same equation at phase zero:
\[
S_m(n\tau)-S_m((n+\theta)\tau)=\int_0^1 A_m(p)
\varphi(\tau\ell(p))^n
[1-\varphi(\theta\tau\ell(p))]dp.\tag{2}
\]
For fixed \(\theta\in(0,1]\), the scale in step 2 yields, pointwise in \(y>0\),
\[
\lim_{n\to\infty}n[1-\varphi(\theta\tau\ell((an)^{-\nu}y))]
=\theta^\alpha y^{2\alpha}.
\]
The same small-\(p\) bounds dominate the rescaled numerator by a multiple of \(y^{2\alpha}e^{-b y^{2\alpha}}\). Dividing (2) by the positive asymptotic survival in step 2, using dominated convergence and the Gamma identity, proves
\[
\lim_{n\to\infty}n\left[1-\frac{S_m((n+\theta)\tau)}{S_m(n\tau)}\right]
=\theta^\alpha\frac{\Gamma(\nu+1)}{\Gamma(\nu)}
=\nu\theta^\alpha.\tag{3}
\]
At \(\theta=0\) it is exact. Each left-hand expression in (3) is nondecreasing in \(\theta\) because survival is nonincreasing in physical time. Pointwise convergence of monotone functions on a compact interval to the continuous function \(\nu\theta^\alpha\) is uniform: subdivide the interval into finitely many pieces on which the limiting function varies by arbitrarily little and squeeze every function between its endpoint values. Consequently (3) is uniform for \(\theta\in[0,1]\). Also uniformly, \((1+\theta/n)^\nu=1+\nu\theta/n+O(n^{-2})\). Multiplying these two expansions proves the boxed phase fingerprint without any second-order regular-variation assumption.

For \(0<\alpha<1\), \(\theta-\theta^\alpha<0\) on \((0,1)\). Its derivative \(1-\alpha\theta^{\alpha-1}\) changes from negative to positive exactly at \(\theta_*\). For each fixed interior \(\theta\), differentiation of the phase profile in \(\alpha\) gives
\[
\frac{\partial}{\partial\alpha}\frac{\theta-\theta^\alpha}{2\alpha}
=\frac{\theta^\alpha(1-\alpha\log\theta)-\theta}{2\alpha^2}>0.
\]
Strict positivity uses \(\theta^\alpha\ge\theta\) and \(1-\alpha\log\theta>1\). This proves unique tail-index identification from an ideal limiting contrast; it is not a noise-stability theorem.

**4. Genuine fractional cusp and positive amplitude.** Fix \(0<\alpha<1\) and any positive integer \(n\). Since \(1-\varphi(u\ell)=cu^\alpha\ell^\alpha+o(u^\alpha)\) as \(u\downarrow0\), uniformly for \(0\le\ell\le2\) after a bounded domination, equation (2) with \(u\) instead of \(\theta\tau\) gives
\[
S_m(n\tau)-S_m(n\tau+u)=B_{n,m}u^\alpha+o(u^\alpha).
\]
The sign of \(A_m\) alone cannot prove \(B_{n,m}>0\). Instead use the fractional Bernstein identity for \(0<\alpha<1\),
\[
\ell^\alpha=\frac\alpha{\Gamma(1-\alpha)}
\int_0^\infty(1-e^{-v\ell})v^{-1-\alpha}dv.
\]
Independence and the time-change identity convert it into
\[
\frac{B_{n,m}}c=\frac\alpha{\Gamma(1-\alpha)}
\int_0^\infty \mathbb E\left[h_m(\Lambda_{n\tau})-h_m(\Lambda_{n\tau}+v)\right]
 v^{-1-\alpha}dv.
\]
The integrand is strictly positive for every \(v>0\), since the killed unit-rate walk has a strictly positive first-hit density at every positive operational time, and is integrable at both ends. Thus \(0<B_{n,m}<\infty\), even though \(A_m\) may change sign. The cusp exponent \(0<\alpha<1\) and positivity imply a negative infinite right derivative.

On the preceding refresh interval, differentiation of (1) is legitimate for every \(v>0\): the elementary bound \(s|\varphi'(s)|\le1-\varphi(s)\le1\) for \(s>0\) gives an integrable domination for \(\ell\varphi'(v\ell)\). Hence the left derivative at \(n\tau\) is finite. Finally, the same rescaling as step 3, now with \(B_{n,m}=c\int A_m\varphi(\tau\ell)^n\ell^\alpha dp\), shows
\[
\lim_{n\to\infty}\frac{n\tau^\alpha B_{n,m}}{S_m(n\tau)}
=\frac{\Gamma(\nu+1)}{\Gamma(\nu)}=\nu.
\]
This establishes the normalized cusp amplitude and completes the theorem.

## Verification

Run `python3 check.py` beside this document; it requires NumPy and SciPy. The standalone checker evaluates the exact finite-time sine integral independently of the asymptotic expression, cross-checks its deterministic-rate specialization against an independent modified-Bessel survival formula, and tests the within-period phase limits across three distinct infinite-mean rate-law transforms, several starting sites and phases, and the finite-mean exponential boundary. It also checks strict physical-time monotonicity and the predicted unique minimum at \(\theta=1/4\) for \(\alpha=1/2\). The recorded execution passed 193 finite assertions, including direct fractional-cusp coefficient checks. The proof above, not the finite assertions, establishes all quantifiers, limits and cusp statements.

For example, at \(\alpha=1/2\), \(\theta=1/4\), the universal normalized phase contrast is exactly \(-1/4\); at the exponential-rate boundary \(\alpha=1\) it is zero. These are mathematical predictions, not fitted coefficients. All numerical integrations in `check.py` use a rescaled spectral variable to control concentration near zero.

## Relationship to prior work

Levit and Reuveni, *First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean* (arXiv:2609.26925v1, first public 2026-09-22), establish the absorbed symmetric walk's exact sine-transform survival formula, the universal leading power-law tail and the mean-time transition at \(\alpha=1/2\). Those are inputs, not novelties here. The present assertion determines the **next-order normalized phase difference without requiring any second-order tail expansion**, a universal interior-phase extremum, and a strict fractional singularity with sharp amplitude at each redraw instant. The complete formula for survival at all times in the cited paper does not itself state these asymptotic limit and cusp comparisons.

Arutkin and Reuveni, *Doubly stochastic continuous time random walk* (arXiv:2302.07041, first public 2023-02-14), introduce the random-rate time-change framework. Their 2024 supplemental section on first-exit density discontinuities treats an exponential-rate, finite-interval model and shows finite density jumps at redraw times; it does not give an infinite-mean fractional cusp or the dimensionless phase limit above. Those finite-mean discontinuities are acknowledged, not claimed as new.

Published work titled *Universal distance-scaled first-passage law for fluctuating jump rates* studies the large-start distributional limit and all low-order moments, rather than the large-time within-period ratio at fixed start. *Finite-size rounding of a fluctuating-rate first-passage transition* studies the reflecting-boundary mean and critical length scale. *Arithmetic tail resonance and hidden phase laws in periodically refreshed Cox walks* concerns extreme displacement for a uniformly phase-randomized environment, not the absorbed half-line survivor with synchronized refreshes. *A one-step obstruction and a sharp late-time penalty for fluctuating lattice jump rates* assumes bounded rates and compares heterogeneous to constant-rate survival. None implies this heavy-tail fingerprint or its fractional cusp at the stated level of generality. Classical Laplace regular variation, Fourier-sine kernels, and fractional Bernstein identities remain acknowledged mathematical tools, not original discoveries.

## Limitations

Only the symmetric nearest-neighbor half-line search, deterministic refresh periods, and regularly varying rate Laplace exponent \(0<\alpha\le1\) are covered. The large-time conclusion is a *relative* order-\(1/n\) phase law; it is not a universal complete second-order expansion of survival. When \(\alpha=1\), vanishing of the normalized phase fingerprint does not imply continuity of the unnormalized hitting-time density. No claim is made for a renewal-random refresh grid, a drifted walk, a finite absorbing interval, or simultaneous variation of \(m\), \(\tau\), \(\alpha\) and \(n\). The asymptotic one-phase identification is an exact-law statement and may be poorly conditioned in finite noisy data. Although targeted literature and published mathematical claims were compared, no search establishes exhaustive publication priority; a more general subordination or regular-variation theorem might imply this specialization.

## References

1. B. Levit and S. Reuveni, *First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean*, arXiv:2609.26925v1 (2026), https://arxiv.org/html/2609.26925 .
2. M. Arutkin and S. Reuveni, *Doubly stochastic continuous time random walk*, arXiv:2302.07041 (2023), https://arxiv.org/abs/2302.07041 ; supplemental section SV at https://journals.aps.org/prresearch/supplemental/10.1103/PhysRevResearch.6.L012033/SM.pdf .
3. *Universal distance-scaled first-passage law for fluctuating jump rates*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-universal-distance-scaled-first-passage-law-for-fluctuating-jump--50200fbcdf63 .
4. *Finite-size rounding of a fluctuating-rate first-passage transition*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-finite-size-rounding-of-a-fluctuating-rate-first-passage-transit--4aa761bb0923 .
5. *Arithmetic tail resonance and hidden phase laws in periodically refreshed Cox walks*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-arithmetic-tail-resonance-and-hidden-phase-laws-in-periodically--9ae66f40315e .
6. *A one-step obstruction and a sharp late-time penalty for fluctuating lattice jump rates*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-one-step-obstruction-and-a-sharp-late-time-penalty-for-fluctua--82177d9e189c .
