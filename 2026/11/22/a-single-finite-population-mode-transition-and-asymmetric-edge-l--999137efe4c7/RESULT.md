# A single finite-population mode transition and asymmetric edge laws for a Poisson-reset Bose gas

## Finding

The stationary **sample mean**, rather than a single-particle density, of a simultaneously reset ideal harmonic Bose gas exhibits one sharp Gaussian-smoothing mode transition. For every fixed positive reset-to-oscillation ratio \(\lambda\), the center-of-mass density has exactly two modes below a unique smoothing-variance threshold \(t_c(\lambda)\in(0,1)\) and exactly one above it. In the large-particle limit the two peaks move into the deterministic support endpoints from inside, on the \(N^{-1/2}\) scale; their heights increase as \(N^{1/4}\). Both Gaussian-leakage probabilities decay as \(N^{-1/4}\), and the right-to-left ratios of peak heights and leakage probabilities converge to the same quantity, \(\cosh(\pi r/\omega)\). The underlying stationary joint distribution and its edge-divergent mixing law were established previously [1].

## Assumptions and scope

Fix \(a,m,\omega,r,\hbar>0\) and an integer \(N\ge1\). Initially all noninteracting bosons occupy the harmonic ground state centered at \(+a\). Between instantaneous *simultaneous* Poisson resets of rate \(r\), the system evolves in the harmonic trap centered at \(-a\). Resetting restores the original state. Write \(\sigma=\sqrt{\hbar/(m\omega)}\), \(\lambda=r/\omega>0\), \(\bar X_N=N^{-1}\sum_{j=1}^N X_j\), and \(Y_N=(\bar X_N+a)/(2a)\). Here \(X_j\) denote the positions measured jointly in the stationary reset ensemble. Let \(\phi_t(v)=(2\pi t)^{-1/2}\exp(-v^2/(2t))\), and

\[
h_\lambda(z)=\frac{\lambda\cosh[\lambda(\pi-\arccos z)]}{\sinh(\pi\lambda)\sqrt{1-z^2}}\,\mathbf1_{(-1,1)}(z),\quad t_N=\frac{\sigma^2}{8a^2N}.
\]

The following conclusions concern the *density of the sample mean* \(f_{t_N,\lambda}=h_\lambda*\phi_{t_N}\), not the density of a single boson and not a quantum-state purity or entanglement measure. The analytic results also apply to continuous \(t>0\), although population is integer.

## Proof

**1. Exact probabilistic reduction (known stationary structure).** The conditional stationary position law at a common reset age \(S\sim\operatorname{Exp}(r)\) is a product of Gaussian distributions of means \(a(2\cos(\omega S)-1)\) and variances \(\sigma^2/2\) [1, Eq. 26]. Hence the dimensionless mean satisfies exactly

\[
Y_N\ \overset{d}{=}\ Z+\sqrt{t_N}\,G,\qquad Z=\cos(\omega S),\qquad G\sim N(0,1),\quad G\perp Z.
\]

Summing over all cosine preimages and using the exponential reset-age density gives the stated \(h_\lambda\) (also [1, Eq. 40]). It integrates to one after substituting \(z=\cos\theta\). At the edges, with \(s\downarrow0\),

\[
h_\lambda(-1+s)=A_-s^{-1/2}(1+o(1)),\quad h_\lambda(1-s)=A_+s^{-1/2}(1+o(1)),
\]

where \(A_-=\lambda/[\sqrt2\sinh(\pi\lambda)]\) and \(A_+=A_-\cosh(\pi\lambda)\). These leading edges are likewise derivable from [1, Eq. 41].

**2. Exactly one modal transition.** In the angle \(z=\cos\theta\),

\[
\frac{d}{d\theta}\log h_\lambda(\cos\theta)=-\lambda\tanh[\lambda(\pi-\theta)]-\cot\theta.
\]

The derivative of the right side is \(\lambda^2\operatorname{sech}^2[\lambda(\pi-\theta)]+\csc^2\theta>0\), and the right side runs from \(-\infty\) to \(+\infty\). Thus \(h_\lambda\) has precisely one interior minimum, decreases toward it from its left infinite endpoint, and increases afterward to its right infinite endpoint. To bound the Gaussian-smoothed mode count, retain \(h_\lambda\) on \([-1+\epsilon,1-\epsilon]\), ramp linearly to zero at \(-1\) and \(1\), and extend by zero. For small \(\epsilon\) the derivative signs of this continuous approximant are \(+,-,+,-\). The removed and added masses both tend to zero by the endpoint estimates in Step 1. Gaussian convolution is variation diminishing, so each approximant's smoothed derivative has at most three sign changes. Since the approximants converge in \(L^1\) and \(\phi_t'\) is bounded, the smoothed derivatives converge uniformly to \(f'_{t,\lambda}\). Any four sign changes of that limit would persist at five test points for a sufficiently good approximant. Thus \(f'_{t,\lambda}\) has at most three sign changes, and at most two strict local maxima are possible.

For \(t_2>t_1\), the Gaussian semigroup identity \(f_{t_2,\lambda}=f_{t_1,\lambda}*\phi_{t_2-t_1}\) forbids creation of new extrema [3]. For \(t\ge1\), the conditional Gaussian posterior identity gives

\[
\frac{d^2}{dy^2}\log f_{t,\lambda}(y)=-\frac1t+\frac{\operatorname{Var}(Z\mid Z+\sqrt tG=y)}{t^2}<0,
\]

because \(Z\in(-1,1)\) has posterior variance strictly less than \(1\). Therefore \(f_{t,\lambda}\) is strictly unimodal for all \(t\ge1\). In fact, all critical points at any \(t>0\) lie in \((-1,1)\): the Gaussian derivative inside the mixture is strictly positive for \(y\le-1\) and strictly negative for \(y\ge1\). At \(t=1\) there is one critical point, with strictly negative second derivative. Continuity of the derivatives on \([-1,1]\) preserves the second-derivative sign near that point and the first-derivative signs on the complement for \(t\) sufficiently close to 1. Hence unimodality already holds on an interval below \(1\).

Step 3 shows two strict maxima for every sufficiently small \(t\). Bimodality is open in \(t\): two strict maxima of the analytic density supply four ordered points where the derivative has signs \(+,-,+,-\), which persist for nearby \(t\). By the semigroup no-new-extrema principle the bimodal parameters therefore form an initial interval \((0,t_c(\lambda))\), with \(0<t_c(\lambda)<1\). Above it there is just one maximum, since the density must attain a maximum and its mode count is at most two. At \(t_c\) at least one critical point satisfies \(f'_{t_c,\lambda}(y)=f''_{t_c,\lambda}(y)=0\): otherwise the finitely many simple critical points in \((-1,1)\) would persist and no others could arise, by continuity of the derivatives and compactness of \([-1,1]\). No exact order of vanishing or universal normal form is asserted. For integer \(N\), two modes occur when \(N>\sigma^2/(8a^2t_c)\) and one when \(N<\sigma^2/(8a^2t_c)\).

**3. Universal two-edge profile, mode locations, and heights.** Define

\[
F(\xi)=\int_0^\infty s^{-1/2}\phi_1(\xi+s)\,ds.
\]

At the right edge write \(z=1-\sqrt t\,s\) in the convolution. For any fixed, sufficiently small \(\delta>0\), on \(1-z<\delta\) the rescaled factor \(t^{1/4}h_\lambda(1-\sqrt t\,s)\) is bounded by a constant times \(s^{-1/2}\). The Gaussian and its first two derivatives yield an integrable bound after multiplication by \(s^{-1/2}\), uniformly on compact sets of \(\xi\). The part with \(1-z\ge\delta\) tends to zero exponentially after rescaling, since the distance from the evaluation point to that part is at least \(\delta/2\) for small \(t\), and \(h_\lambda\) is integrable. At the left edge reflect the argument. Dominated convergence then gives, locally uniformly in \(\xi\) and with convergence of the first two scaled profile derivatives,

\[
f_{t,\lambda}(1+\sqrt t\xi)=A_+t^{-1/4}[F(\xi)+o(1)],\quad f_{t,\lambda}(-1+\sqrt t\xi)=A_-t^{-1/4}[F(-\xi)+o(1)].
\]

Integration by parts shows \(F''(\xi)+\xi F'(\xi)+F(\xi)/2=0\). Also \(F>0\), \(F(\xi)\to0\) at both infinities, \(F'(0)<0\), and at **every** root of \(F'\), \(F''=-F/2<0\). Consequently \(F\) has one and only one strict maximum at \(\xi_*=-q<0\), with \(q=0.764950867\ldots\), independently of physical parameters. The derivative convergence and the bound from step 2 identify exactly one mode in each edge neighborhood for small \(t\). Since their heights diverge like \(t^{-1/4}\) whereas \(h_\lambda\) remains bounded on interior compact subsets, there are no other global candidate maxima. Returning to physical units,

\[
x_{N,-}=-3a+q\frac{\sigma}{\sqrt{2N}}+o(N^{-1/2}),\qquad x_{N,+}=a-q\frac{\sigma}{\sqrt{2N}}+o(N^{-1/2}).
\]

The corresponding physical density peak heights are asymptotic to \(A_-F(-q)t_N^{-1/4}/(2a)\) and \(A_+F(-q)t_N^{-1/4}/(2a)\). Their ratio tends to \(A_+/A_-=\cosh(\pi\lambda)\). The common \(N^{1/4}\) height law and asymmetric ratio follow.

**4. Sharp finite-population leakage.** Conditioning on \(Z\), and writing \(\bar\Phi=1-\Phi\), yields

\[
\Pr(Y_N>1)=\int_{-1}^1h_\lambda(z)\,\bar\Phi((1-z)/\sqrt{t_N})\,dz.
\]

Rescale \(1-z=\sqrt{t_N}\,s\) and use the right-edge expansion plus Gaussian domination. This gives \(\Pr(Y_N>1)\sim A_+C t_N^{1/4}\). At the left endpoint the same reasoning gives \(\Pr(Y_N<-1)\sim A_-C t_N^{1/4}\), where

\[
C=\int_0^\infty s^{-1/2}\bar\Phi(s)\,ds=\frac{2^{1/4}\Gamma(3/4)}{\sqrt\pi}.
\]

The **right-to-left** leakage ratio \(\Pr(Y_N>1)/\Pr(Y_N<-1)\) therefore tends to the same \(\cosh(\pi\lambda)\) as the right-to-left modal-height ratio. The left-to-right leakage ratio tends to \(1/\cosh(\pi\lambda)\). All limits keep physical \(a,\sigma,\lambda\) fixed.

## Verification

The accompanying `check.py` is a standalone deterministic numerical cross-check using only NumPy and SciPy. It tests phase-density normalization, numerical solutions of \(f'=f''=0\) at finite smoothing (\(\lambda=1/2\) and \(1\)), modal counts on both sides, and small-noise peak/leakage asymptotic ratios for three rates. These finite evaluations do not establish the continuous-parameter mode theorem or the asymptotics: those depend on the arguments above. Run with `python check.py` and installed `numpy`, `scipy`.

## Relationship to prior work

Kulkarni, Majumdar and Sabhapandit [1] derive the stationary conditionally independent Gaussian joint law, latent cosine density \(h_\lambda\), its endpoint exponents and relative endpoint amplitudes. In Section 3.1 they give the exact one-particle Gaussian convolution and discuss a critical width. At fixed \(\lambda\), the sample mean follows exactly that same one-particle width family with \(\sigma\) replaced by \(\sigma/\sqrt N\); population scans the width and does not create a separate modal mechanism. Biroli, Larralde, Majumdar and Schehr [2] give a general conditionally independent sample-mean framework. Noncreation of modes under Gaussian smoothing is standard [3]. The contribution is a proof of the whole-width mode count and uniqueness of the smoothing transition for each fixed \(\lambda>0\), together with the explicit inward \(N^{-1/2}\) peak shifts, \(N^{1/4}\) peak amplitudes, and \(N^{-1/4}\) outer leakage laws. The two right-to-left ratios are consequences of the known latent endpoint amplitude ratio; the assertions here concern how that ratio is inherited by the smoothed observables.

## Limitations

This is a stationary position-measurement result, not a statement about entanglement, quantum coherence, or a finite-time reset transient. It assumes ideal noninteracting bosons, a fixed ground-state width, a sudden harmonic trap quench, and instantaneous common Poisson resets. The transition value \(t_c(\lambda)\) is characterized structurally, not by a closed-form elementary expression; no strict mode-count assertion is made at equality beyond the proved upper bound and critical-point degeneracy. Other mixtures or reset-age laws may have different edge exponents. Unindexed equivalent special-function/scale-space arguments remain a literature-priority risk.

## References

[1] M. Kulkarni, S. N. Majumdar and S. Sabhapandit, *Dynamically emergent correlations in bosons via quantum resetting*, arXiv:2407.20342, first submitted 2024-07-29, https://arxiv.org/html/2407.20342v2 (stationary joint law, Eqs. 23–26; cosine density Eq. 40; edge Eq. 41; one-particle profile Eq. 43).

[2] M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Exact extreme, order and sum statistics in a class of strongly correlated system*, arXiv:2307.15351, first submitted 2023-07-28, https://arxiv.org/html/2307.15351v2 (sample mean, Sec. VI.1).

[3] T. Lindeberg, *Non-creation of local extrema and semi-group structure*, 1997, https://www.csc.kth.se/~tony/cern-review/cern-html/node6.html (Gaussian scale-space mode noncreation).
