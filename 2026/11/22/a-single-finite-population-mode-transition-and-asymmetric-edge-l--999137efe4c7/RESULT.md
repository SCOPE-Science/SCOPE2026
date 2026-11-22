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

The derivative of the right side is \(\lambda^2\operatorname{sech}^2[\lambda(\pi-\theta)]+\csc^2\theta>0\), and the right side runs from \(-\infty\) to \(+\infty\). Thus \(h_\lambda\) has precisely one interior minimum, decreases toward it from its left infinite endpoint, and increases afterward to its right infinite endpoint. To bound the Gaussian-smoothed mode count, truncate and cap the two endpoint singularities by positive compactly supported piecewise-smooth approximants whose derivative signs occur in the order positive/negative/positive/negative. Each derivative has at most three sign changes. Gaussian convolution is strictly variation diminishing, so each approximant's smoothed derivative has at most three sign changes. The approximants converge in \(L^1\); uniform convergence of their smoothed derivatives on compact sets transfers the no-more-than-three-alternating-signs conclusion to \(f'_{t,\lambda}\). Since \(f'_{t,\lambda}>0\) far to the left and \(f'_{t,\lambda}<0\) far to the right, at most two strict local maxima are possible.

For \(t_2>t_1\), the Gaussian semigroup identity \(f_{t_2,\lambda}=f_{t_1,\lambda}*\phi_{t_2-t_1}\) forbids creation of new extrema [3]. For \(t\ge1\), the conditional Gaussian posterior identity gives

\[
\frac{d^2}{dy^2}\log f_{t,\lambda}(y)=-\frac1t+\frac{\operatorname{Var}(Z\mid Z+\sqrt tG=y)}{t^2}<0,
\]

because \(Z\in(-1,1)\) has posterior variance strictly less than \(1\). Therefore \(f_{t,\lambda}\) is strictly unimodal for all \(t\ge1\). Strict negative curvature at its unique mode, continuity in \(t\), and the uniform outer-tail derivative signs (the latent variable stays in \([-1,1]\)) ensure unimodality also on some interval immediately below \(t=1\). Step 3 shows two distinct strict maxima for every sufficiently small \(t\). Real analyticity in \(y\) and the semigroup no-new-extrema principle imply that the bimodal smoothing parameters form an initial interval \((0,t_c(\lambda))\) with \(0<t_c(\lambda)<1\), the unimodal regime contains every \(t>t_c\), and at the boundary a double critical point is necessary. Exactly at equality we assert only degeneracy and at most two maxima; we do not claim a universal normal form there. For integer \(N\), two modes occur when \(N>\sigma^2/(8a^2t_c)\) and one when \(N<\sigma^2/(8a^2t_c)\).

**3. Universal two-edge profile, mode locations, and heights.** Define

\[
F(\xi)=\int_0^\infty s^{-1/2}\phi_1(\xi+s)\,ds.
\]

A boundary change of variables and dominated convergence, including differentiated Gaussian integrands, give locally uniformly in \(\xi\),

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

The left/right leakage ratio therefore recovers the same parameter \(\cosh(\pi\lambda)\) as the modal-height ratio, providing two distinct large-population diagnostics of the reset-to-trap frequency ratio. All limits keep physical \(a,\sigma,\lambda\) fixed.

## Verification

The accompanying `check.py` is a standalone deterministic numerical cross-check using only NumPy and SciPy. It verifies phase-density normalization, two independent finite-smoothing double-root parameter estimates (\(\lambda=1/2\) and \(1\)), modal counts on both sides, and small-noise peak/leakage asymptotic ratios for three rates. It passes all specified assertions. These finite evaluations do not establish the continuous-parameter mode theorem or the asymptotics: those depend on the arguments above. Run with `python check.py` and installed `numpy`, `scipy`.

## Relationship to prior work

Kulkarni, Majumdar and Sabhapandit [1] derive the exact stationary conditionally independent Gaussian joint law, the latent cosine density \(h\), its endpoint exponents and relative endpoint amplitudes, and numerical/special-function discussion of one-particle mode transitions. The present sample-mean density is a direct finite-\(N\) consequence of their joint law; it is **not** presented as an independently new mixture formula. Biroli, Larralde, Majumdar and Schehr [2] give a general conditionally independent sample-mean framework (including Gaussian mixture expansion), so the mere large-\(N\) recovery of the latent law is also not new. Noncreation of modes under Gaussian smoothing is standard [3]. The assessed addition is the specific *whole finite-population mode count*, uniqueness in smoothing, and the explicit, asymmetric \(N^{-1/2}\) peak positions, \(N^{1/4}\) peak amplitudes and \(N^{-1/4}\) outer leakage laws for this nonequilibrium quantum gas. These statements were not found in the inspected sections and appendices of [1] and [2].

## Limitations

This is a stationary position-measurement result, not a statement about entanglement, quantum coherence, or a finite-time reset transient. It assumes ideal noninteracting bosons, a fixed ground-state width, a sudden harmonic trap quench, and instantaneous common Poisson resets. The transition value \(t_c(\lambda)\) is characterized structurally, not by a closed-form elementary expression; no strict mode-count assertion is made at equality beyond the proved upper bound and critical-point degeneracy. Other mixtures or reset-age laws may have different edge exponents. Unindexed equivalent special-function/scale-space arguments remain a literature-priority risk.

## References

[1] M. Kulkarni, S. N. Majumdar and S. Sabhapandit, *Dynamically emergent correlations in bosons via quantum resetting*, arXiv:2407.20342, first submitted 2024-07-29, https://arxiv.org/html/2407.20342v2 (stationary joint law, Eqs. 23–26; cosine density Eq. 40; edge Eq. 41; one-particle profile Eq. 43).

[2] M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Exact extreme, order and sum statistics in a class of strongly correlated system*, arXiv:2307.15351, first submitted 2023-07-28, https://arxiv.org/html/2307.15351v2 (sample mean, Sec. VI.1).

[3] T. Lindeberg, *Non-creation of local extrema and semi-group structure*, 1997, https://www.csc.kth.se/~tony/cern-review/cern-html/node6.html (Gaussian scale-space mode noncreation).
