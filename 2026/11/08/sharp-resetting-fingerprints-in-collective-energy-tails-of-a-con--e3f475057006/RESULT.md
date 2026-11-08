# Sharp resetting fingerprints in collective energy tails of a confined Brownian gas

## Finding

The stationary collective mean-square displacement of a simultaneously reset, harmonically confined Brownian gas has a non-Gaussian finite-size edge even though its conditional dynamics are Gaussian. More precisely, fix a reset rate \(r>0\), damping \(\mu>0\), diffusivity \(D>0\), and set \(b=r/(2\mu)\), \(\theta=D/\mu\). For \(N\) particles let
\[
Q_N=\frac1N\sum_{i=1}^N X_i^2.
\]
The exact finite-particle representation is
\[
\frac{Q_N}{\theta}\ \stackrel{d}{=}\ V H_N,\qquad
V\sim\operatorname{Beta}(1,b),\quad H_N\sim\chi_N^2/N,\quad V\perp H_N.
\]
This representation follows from the *previously known* common-reset stationary joint distribution and is used here as the starting point, not claimed as new. The claim is the following sharp **collective-energy tail theorem**, with its complete prefactors:

For every fixed \(x\in\mathbb R\),
\[
\lim_{N\to\infty}N^{b/2}\Pr\!\left\{Q_N>\theta\left(1+\frac{x}{\sqrt N}\right)\right\}
=\mathcal F_b(x),\qquad
\mathcal F_b(x)=b\int_0^\infty s^{b-1}\overline\Phi\!\left(\frac{x+s}{\sqrt2}\right)\,ds,
\]
where \(\overline\Phi(z)=\Pr\{Z>z\}\) for \(Z\sim N(0,1)\). In particular, at the equilibrium energy threshold,
\[
\Pr\{Q_N>\theta\}\sim
\frac{2^{b-1}\Gamma((b+1)/2)}{\sqrt\pi}\,N^{-b/2}.
\]
For every fixed \(t>1\),
\[
\Pr\{Q_N>\theta t\}\sim
\frac{2^b\Gamma(b+1)}{\sqrt\pi\,(t-1)^{b+1}}
N^{-b-1/2}
\exp\!\left[-\frac N2(t-1-\log t)\right].
\]
Thus the supercritical exponential rate is independent of the resetting rate, whereas its sharp polynomial factor \(N^{-b-1/2}\) and the entire critical crossover depend on \(b=r/(2\mu)\). The critical window is of width \(N^{-1/2}\), and its probability is of order \(N^{-b/2}\). The already-covered macroscopic law \(Q_N/\theta\Rightarrow\operatorname{Beta}(1,b)\) provides physical context but is not part of the originality claim.

## Assumptions and scope

Particles move on \(\mathbb R\). Between resets, for every \(i=1,\ldots,N\),
\[
dX_i(t)=-\mu X_i(t)\,dt+\sqrt{2D}\,dW_i(t),
\]
where the \(W_i\) are mutually independent standard Brownian motions. One independent Poisson process of rate \(r\) instantaneously resets all positions to zero simultaneously. The process is observed in its unique stationary law; all positive model parameters are fixed as \(N\to\infty\). The theorems concern one-dimensional harmonic confinement with common resets and the natural nonnegative aggregate \(Q_N\), not the distribution of the spatial maximum or arbitrary confining potentials. The fixed-threshold supercritical limit is not asserted uniformly when \(t\downarrow1\); the separate crossover formula treats \(t=1+O(N^{-1/2})\).

## Proof

**1. Exact stationary reduction.** In stationarity the backward age \(T\) of the last common Poisson reset is independent of all subsequent Brownian noise and obeys \(T\sim\operatorname{Exp}(r)\). Conditional on \(T=\tau\), the positions are independent centered Gaussians of variance
\[
\sigma^2(\tau)=\frac D\mu(1-e^{-2\mu\tau})=\theta(1-e^{-2\mu\tau}).
\]
For \(U=e^{-2\mu T}\), direct change of variables gives \(\Pr\{U\le u\}=u^b\) for \(0<u<1\), so \(V=1-U\) has density \(b(1-v)^{b-1}\). Scaling the independent conditional squares yields the displayed independent-product representation with \(H_N=\chi_N^2/N\).

Set \(W=1-V\), so \(W\) has density \(bw^{b-1}\) on \((0,1)\), and define \(G_N(z)=\Pr\{H_N>z\}\). The exact survival probability for any \(t>0\) becomes
\[
P_N(t)=\Pr\{Q_N>\theta t\}=b\int_0^1 w^{b-1}
G_N\!\left(\frac{t}{1-w}\right)\,dw.\tag{1}
\]

**2. Central edge and crossover.** Fix \(x\in\mathbb R\), put \(t_N=1+x/\sqrt N\) and substitute \(w=s/\sqrt N\) in (1). This gives
\[
N^{b/2}P_N(t_N)=b\int_0^{\sqrt N}s^{b-1}
G_N\!\left(\frac{1+x/\sqrt N}{1-s/\sqrt N}\right)\,ds.\tag{2}
\]
By the classical central limit theorem for sums of squared standard Gaussians,
\[
\frac{\chi_N^2-N}{\sqrt{2N}}\Rightarrow N(0,1).
\]
For fixed \(s\ge0\), the argument of \(G_N\) in (2) is \(1+(x+s)/\sqrt N+O(N^{-1})\), and consequently the integrand tends to \(b s^{b-1}\overline\Phi((x+s)/\sqrt2)\).

To justify convergence of the unbounded integral, use the standard chi-square Chernoff inequality
\[
G_N(z)\le\exp[-NI(z)],\qquad
I(z)=\frac12(z-1-\log z),\quad z>1.
\]
Choose \(S>2|x|+2\). For \(s\in[S,\sqrt N/2]\), the argument in (2) exceeds one by at least a constant times \(s/\sqrt N\); the inequality \(I(1+u)\ge c u^2\) for bounded positive \(u\) gives the integrable bound \(C s^{b-1}e^{-cs^2}\). For \(s\in[\sqrt N/2,\sqrt N)\), the argument is bounded below by a number strictly larger than one for all sufficiently large \(N\), so the contribution is at most \(O(N^{b/2}e^{-c'N})\). On bounded \(s\)-intervals, the factor \(s^{b-1}\) is integrable for every \(b>0\). Dominated convergence proves the crossover formula.

At \(x=0\), Tonelli's theorem and a Gaussian tail moment give
\[
\begin{aligned}
\mathcal F_b(0)
&=b\int_0^\infty s^{b-1}\overline\Phi(s/\sqrt2)\,ds\\
&=\int_0^\infty\frac{e^{-z^2/2}}{\sqrt{2\pi}}(\sqrt2z)^b\,dz
=\frac{2^{b-1}\Gamma((b+1)/2)}{\sqrt\pi}.
\end{aligned}
\]

**3. Supercritical boundary Laplace asymptotics.** Fix \(t>1\). Stirling's formula applied to the gamma density of \(\chi_N^2\), followed by one-sided endpoint Laplace integration, gives the uniform tail equivalent
\[
G_N(z)=\frac{e^{-NI(z)}}{(z-1)\sqrt{\pi N}}(1+o(1))
\]
for \(z\) in any fixed compact subset of \((1,\infty)\). In (1) the rate function \(I(t/(1-w))\) is strictly increasing in \(w\in[0,1)\), and at the minimizing endpoint \(w=0\),
\[
I\!\left(\frac{t}{1-w}\right)=I(t)+\frac{t-1}{2}w+O(w^2).
\]
For \(w\ge\varepsilon\), the Chernoff bound makes the contribution exponentially smaller than \(e^{-NI(t)}\). For \(N^{-2/3}\le w\le\varepsilon\), positivity of the endpoint derivative gives an additional \(e^{-cN^{1/3}}\) factor, while \(w\le N^{-2/3}\) lies in the uniform gamma-tail regime. Substitute \(w=y/N\) in the latter interval and apply dominated convergence:
\[
\begin{aligned}
P_N(t)&\sim \frac{b\,e^{-NI(t)}}{(t-1)\sqrt{\pi N}}
N^{-b}\int_0^\infty y^{b-1}e^{-(t-1)y/2}\,dy\\
&=\frac{2^b\Gamma(b+1)}{\sqrt\pi(t-1)^{b+1}}
N^{-b-1/2}e^{-NI(t)}.
\end{aligned}
\]
This proves all new sharp asymptotics and their constants. The large-deviation rate \(I(t)\) is the ordinary chi-square rate at the largest admissible conditional variance; the reset-age distribution controls the additional endpoint mass and hence the power-law prefactor.

**4. Bulk context, not a new claim.** Since \(H_N\to1\) in probability, the previously known conditional-iid law of large numbers immediately yields \(Q_N/\theta\Rightarrow V\), with \(\Pr\{V>t\}=(1-t)^b\) for \(0<t<1\). This is included to connect the two tail regimes and is explicitly excluded from the asserted contribution.

## Verification

The standalone `verify.py` uses only the Python standard library. Run `python3 verify.py`. Its 105 finite comparisons check independent moment formulas, evaluate the exact beta–chi-square mixture using a numerical incomplete-gamma survival function, compare several finite-size critical/crossover and supercritical probabilities with the displayed constants, and check the \(\chi_2^2\) survival function. All 105 comparisons passed on the packaged version. Numerical evidence tests finite instances only; the statements for every \(b>0\), every fixed \(x\in\mathbb R\) and every fixed \(t>1\) are proved analytically above.

## Relationship to prior work

De Mauro, Majumdar and Schehr (2026), arXiv:2606.31634v1, give the common-reset Brownian gas in harmonic confinement and its exact stationary joint law, with density, pair correlations, extrema and gaps. The renewal/conditionally-independent construction used in Step 1 is therefore established prior work. Biroli, Larralde, Majumdar and Schehr (2023), arXiv:2307.15351, develop general conditionally independent sum statistics: their broad sum theorem implies the large-\(N\) bulk Beta energy law in this specialization. Neither the bulk law nor the exact stationary Gaussian mixture is presented here as novel. The present contribution is the explicit equilibrium-threshold \(N^{-1/2}\) crossover with its full Gaussian-tail integral and constant, together with the sharp supercritical energy tail including its reset-dependent \(N^{-b-1/2}\) prefactor and rate-independent exponential rate.

Published results on extreme positions in the same harmonic gas do not imply these energy-tail prefactors: a maximum is governed by different finite-\(N\) fluctuations than a normalized sum of squared positions. The 2025 non-Poissonian common-reset Brownian-gas extension treats a different renewal clock and focuses on extreme/order/counting observables. A complete priority assertion would require broader literature coverage, including inaccessible or not fully inspected supplements.

## Limitations

The calculation fixes \(r,\mu,D\) as \(N\to\infty\), assumes independent Gaussian Brownian increments conditional on a common Poisson reset age, and addresses only the harmonic trap and one-time stationary collective energy. It does not establish uniform matching between fixed \(t>1\) and the \(N^{-1/2}\) transition, nor an exact finite-\(N\) closed-form special function for the tail. It does not apply unchanged to nonharmonic traps, partially reset populations, general renewal clocks or time-dependent energy statistics. The result is supported by a reconstructed analytical proof and finite numerical checks; no independent mathematical or publication-priority validation is claimed. The full appendices of all potentially relevant sources were not exhaustively inspected, leaving residual possibility of earlier implicit coverage.

## References

1. G. de Mauro, S. N. Majumdar and G. Schehr, *Effects of confinement in a Brownian gas with simultaneous stochastic resetting and dynamically emergent correlations*, arXiv:2606.31634v1, posted 2026-06-30, https://arxiv.org/abs/2606.31634.
2. M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Exact extreme, order and sum statistics in a class of strongly correlated system*, arXiv:2307.15351, 2023, https://arxiv.org/abs/2307.15351.
3. G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658, 2025, https://arxiv.org/abs/2509.06658.
4. M. Biroli, M. Kulkarni, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570, 2023, https://arxiv.org/abs/2312.02570.
