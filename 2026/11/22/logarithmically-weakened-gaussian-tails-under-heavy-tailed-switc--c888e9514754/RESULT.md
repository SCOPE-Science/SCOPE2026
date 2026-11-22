# Logarithmically weakened Gaussian tails under heavy-tailed switching between two confining traps

## Finding

A Brownian particle alternating between two *strictly positive* harmonic stiffnesses has a Gaussian far tail, but heavy-tailed residence in the softer trap leaves an exact logarithmic attenuation. This is different from the algebraic spatial tails that arise when the softer stiffness is zero.

Precisely, suppose the soft-trap sojourn has survival probability \(\Pr(W>t)\sim c t^{-\beta}\), where \(c>0\) and \(\beta>1\); the stiff-trap sojourn lasts a deterministic time \(\tau>0\). With soft stiffness \(a>0\), stiff stiffness \(b>a\), and diffusion coefficient \(D>0\), write \(L=D/a\), \(\mu=\mathbb EW\), and let \(p\) be the normalized stationary position density. Then

\[
\boxed{\displaystyle
p(x)\sim\frac{\exp[-x^2/(2L)]}{\sqrt{2\pi L}}\,
\frac{c}{(\mu+\tau)(\beta-1)}
\left[\frac{\log(|x|/\sqrt L)}a\right]^{1-\beta}}
\qquad(|x|\to\infty).
\]

The equivalence includes the full multiplicative constant. In particular, the Gaussian envelope alone is **not** an asymptotic equivalent: its true stationary density ratio tends to zero with a power of the logarithm. Measuring that ratio determines the residence survival exponent \(\beta\) from its logarithmic slope, in principle.

## Assumptions and scope

Let \(J_t\in\{\ell,h\}\) alternate between a soft state \(\ell\) and a stiff state \(h\), independently of a standard Brownian motion \(B_t\). Successive soft durations \(W_1,W_2,\ldots\) are independent copies of a strictly positive random variable satisfying \(\Pr(W>t)\sim c t^{-\beta}\) as \(t\to\infty\), for \(c>0\), \(\beta>1\). Every stiff duration equals \(\tau>0\); all durations are independent of \(B\). At soft and stiff times respectively the diffusion follows

\[
dX_t=-a X_t\,dt+\sqrt{2D}\,dB_t,\qquad
 dX_t=-b X_t\,dt+\sqrt{2D}\,dB_t,
\]

where \(0<a<b\) and \(D>0\). The process is understood in its stationary two-sided alternating-renewal regime; this exists since \(\mu=\mathbb EW<\infty\) and \(a>0\). We make no smoothness assumption on the soft-duration law, beyond the specified survival asymptotic. The claim concerns the full unconditional one-time stationary spatial **density**, not a finite-time transient or a phase-conditioned density.

## Proof

**1. Conditional Gaussian variance.** For a stationary switching environment \(J\), the solution obtained from the remote past is a centered Gaussian conditional on \(J\), with variance

\[
V_t=2D\int_{-\infty}^{t}\exp\!\left(-2\int_s^t k_{J_u}\,du\right)ds,
\quad k_\ell=a,\quad k_h=b.
\]

Write \(H=D/b\) and \(L=D/a\). Comparison with the constant-stiffness solutions gives \(H\le V_t\le L\). Between switches the conditional variance obeys \(dV/dt=2D-2k_{J_t}V\). Let \(Z=L-V\) at the beginning of a soft interval. Every immediately preceding stiff interval lasted \(\tau\), so the stiff variance evolution gives the *deterministic* bounds

\[
0<z_0=(L-H)(1-e^{-2b\tau})\le Z\le z_1=L-H.
\tag{1}
\]

At soft age \(A\), the variance gap is exactly \(L-V=Ze^{-2aA}\). The new soft duration is independent of \(Z\).

**2. Rare events near the maximal variance.** Stationary renewal sampling assigns probability \(\mu/(\mu+\tau)\) to the soft phase, and conditional soft age has equilibrium-excess survival

\[
\Pr(A>t\mid J=\ell)=\frac1\mu\int_t^\infty \Pr(W>u)\,du
\sim\frac{c}{\mu(\beta-1)}t^{1-\beta}.
\tag{2}
\]

The asymptotic follows by integrating the two-sided \((1\pm\varepsilon)c u^{-\beta}\) bounds; it does not presume a density for \(W\). Independence of current soft age and entrance variance, together with (1), uniformly squeezes the event \(Ze^{-2aA}/L<y\) between the two thresholds obtained by replacing \(Z\) by \(z_0\) and \(z_1\). Since their ages differ by bounded constants, (2) implies

\[
\Pr((L-V)/L<y,\ J=\ell)\sim
\frac{c}{(\mu+\tau)(\beta-1)}
\left[\frac{\log(1/y)}{2a}\right]^{1-\beta}.
\tag{3}
\]

During a stiff interval, the variance decreases; to have \(L-V<Ly\), the variance at the *end of the preceding soft interval* must already have gap below \(Ly\). By the lower bound \(z_0\), this requires that preceding *whole* soft duration be at least \(\log(z_0/(Ly))/(2a)\). Thus

\[
\Pr((L-V)/L<y,\ J=h)
\le\frac\tau{\mu+\tau}\Pr\!\left(W>\frac{\log(z_0/(Ly))}{2a}\right)
=O([\log(1/y)]^{-\beta}).
\tag{4}
\]

This is smaller than (3) by one logarithmic power. Therefore the complete variance gap \(Y=(L-V)/L\) has cumulative small-gap law

\[
\Pr(Y<y)\sim K\left[\frac{\log(1/y)}{2a}\right]^{1-\beta},
\qquad K=\frac{c}{(\mu+\tau)(\beta-1)}.
\tag{5}
\]

**3. From the variance edge to the spatial far tail.** The exact Gaussian-mixture identity is

\[
p(x)=\mathbb E\left[\frac{e^{-x^2/(2V)}}{\sqrt{2\pi V}}\right].
\]

Let \(\phi_L(x)=e^{-x^2/(2L)}/\sqrt{2\pi L}\) and \(q=x^2/(2L)\). Then

\[
\frac{p(x)}{\phi_L(x)}
=\mathbb E\left[(1-Y)^{-1/2}\exp\left(-\frac{qY}{1-Y}\right)\right].
\tag{6}
\]

Because \(Y\le1-H/L<1\), splitting at \(Y=\delta\), bounding the small-gap factor between Laplace kernels at \(q\) and \(q/(1-\delta)\), and then sending \(\delta\downarrow0\), shows that (6) is asymptotic to \(\mathbb E e^{-qY}\). Indeed the contribution from \(Y\ge\delta\) is exponentially small, and the prefactor tends uniformly to one on \(Y\le\delta\).

The distribution function in (5) varies slowly at zero: for each fixed \(u>0\), \(\Pr(Y<u/q)/\Pr(Y<1/q)\to1\). Integration by parts yields \(\mathbb Ee^{-qY}=\int_0^\infty e^{-u}\Pr(Y<u/q)\,du\); splitting the integral into compact \(u\) and exponentially small tails (or applying the elementary Laplace form of the slow-variation theorem) gives

\[
\mathbb Ee^{-qY}\sim\Pr(Y<1/q)
\sim K\left[\frac{\log q}{2a}\right]^{1-\beta}.
\]

Finally \(\log q=2\log(|x|/\sqrt L)-\log2\), completing the asserted density equivalent.

## Verification

The standalone \(\texttt{CHECK.py}\) checks the exact variance-gap sandwich and the resulting Gaussian-mixture integral for two independent positive-stiffness parameter sets and Pareto-type soft clocks with \(\Pr(W>t)=(1+t/s)^{-\beta}\). Its numerical soft-tail upper and lower ratios converge toward the proved coefficient; the test also checks that the stiff-phase near-edge bound is subleading. Run \(\texttt{python CHECK.py}\) with Python 3 and SciPy. These calculations independently test constants and inequalities, while steps (1)–(6), not finite numerical tests, establish the infinite-displacement theorem.

## Relationship to prior work

Frydel (2026), *Semi-Markovian switching in a fluctuating harmonic trap*, supplies the general two-stiffness age-structured formulation and Gaussian-mixture viewpoint. Its detailed variance-space spatial-tail analysis specializes to a *released* phase with zero stiffness and obtains algebraic spatial tails for algebraic residence laws. The present result instead retains **two strictly positive stiffnesses** and determines a logarithmic factor in an ultimately Gaussian tail, including its normalization, by a stationary-age/variance-edge argument. It does not claim originality for renewal conditioning, Gaussian mixtures, or the general switching model.

Frydel (2024), *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, studies exponentially switched on/off trapping and hence does not establish the positive/positive heavy-tail logarithmic equivalent. Related trapped run-and-tumble edge results concern compactly supported active particle positions, not the Brownian Gaussian-mixture spatial far tail. Both the close 2026 formulation and the general regular-variation methods remain essential prior ingredients.

## Limitations

The assertion requires a strictly positive soft stiffness, finite mean soft residence, and a deterministic positive stiff residence. Neither a zero-soft-stiffness limit nor infinite-mean renewal clocks are included. The asymptotic can converge very slowly as a function of physical displacement because its small parameter is the inverse logarithm. The result does not infer the time-dependent switching process uniquely from finite data, prove an optimal protocol, or claim a new general regular-variation theorem. Publication priority relative to unindexed equivalent statements requires independent literature verification.

## References

1. D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation*, Physical Review E **114**, 024105 (2026), initially public July 6, 2026; https://arxiv.org/abs/2607.05173; https://doi.org/10.1103/7pxv-tg3b.
2. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap* (2024); https://arxiv.org/abs/2407.12213.
3. Standard renewal excess-age and regular-variation integration facts are used directly and proved in the required form in the text above.
