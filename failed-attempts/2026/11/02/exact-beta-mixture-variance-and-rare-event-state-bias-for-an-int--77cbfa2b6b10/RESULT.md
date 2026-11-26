# Exact beta-mixture variance and rare-event state bias for an intermittently repulsive harmonic particle

## Finding

Consider the one-dimensional overdamped Langevin equation
\[
 dX_t=-A_{S_t}X_t\,dt+\sqrt{2D}\,dB_t,
 \qquad A_+=a>0,\quad A_-=-b<0,
\]
where \(D,a,b>0\); \(B\) is an independent standard Brownian motion; and an independent continuous-time two-state Markov chain switches \(+\to-\) at rate \(u>0\) and \(-\to+\) at rate \(w>0\). Assume the **mean confinement condition** \(aw>bu\). Put
\[
 \eta=\frac{u}{2a},\quad \xi=\frac{w}{2b},\quad
 \theta=\xi-\eta>0,\quad c=\frac Da,\quad d=\frac Db,
 \quad L=c+d.
\]
In the unique stationary regime, conditionally on the complete environment history, \(X\) is centered Gaussian with variance \(V\). The transformed variance
\[
 Y=\frac{V-c}{V+d}\in(0,1)
\]
has the following **exact conditional beta laws**:
\[
 Y\mid (S=+)\sim\operatorname{Beta}(\eta,\theta),\qquad
 Y\mid (S=-)\sim\operatorname{Beta}(\eta+1,\theta).
\]
The corresponding environmental weights are \(\pi_+=w/(u+w)\) and \(\pi_-=u/(u+w)\). In particular, \(V=(c+dY)/(1-Y)\) is an explicitly normalized two-component beta-transform mixture. This determines the full stationary position law via
\[
 p_X(x)=\sum_{s\in\{+,-\}}\pi_s\int_0^1
 \frac{\exp\!\left(-x^2/(2v(y))\right)}{\sqrt{2\pi v(y)}}
 \frac{y^{h_s-1}(1-y)^{\theta-1}}{\mathrm B(h_s,\theta)}\,dy,
 \quad v(y)=\frac{c+dy}{1-y},\quad h_+=\eta,\quad h_-=\eta+1.
\]
Define the explicit constant
\[
 K_V=\frac{L^\theta}{\theta}
 \left[\frac{\pi_+}{\mathrm B(\eta,\theta)}+
       \frac{\pi_-}{\mathrm B(\eta+1,\theta)}\right],\qquad
 K_X=K_V\frac{2^\theta\Gamma(\theta+1/2)}{\sqrt\pi}.
\]
Then the **two-sided rare-displacement tail has an exact coefficient**:
\[
 \mathbb P(|X|>x)\sim K_X x^{-2\theta}\quad(x\to\infty),
 \qquad \mathbb E|X|^p<\infty\iff 0\le p<2\theta.
\]
The one-sided positive and negative tails each have half this coefficient. Furthermore, the environment observed during an extreme displacement has a universal limiting composition,
\[
 \boxed{\lim_{x\to\infty}\mathbb P(S=-\mid |X|>x)=\frac{a}{a+b}.}
\]
Thus the fraction of extreme observations made in the repulsive state depends on the two stiffness magnitudes but **not** on \(u,w,D\), although the ordinary stationary occupation \(\pi_-=u/(u+w)\) generally differs from it.

For the example \(a=b=u=1\), \(w=2\), \(D=1/2\), the conditional mixing laws are \(\operatorname{Beta}(1/2,1/2)\) and \(\operatorname{Beta}(3/2,1/2)\), and the exact tail constant is
\[
 \mathbb P(|X|>x)\sim \frac{8\sqrt2}{3\pi^{3/2}}\frac1x.
\]
The repulsive state has stationary weight \(1/3\), but contributes asymptotically \(1/2\) of the extreme-position observations.

## Assumptions and scope

The process is defined for all finite real initial positions and either initial environment state, with \(u,w,D,a,b\) strictly positive and \(aw>bu\). The stationary law and all statements concern an unbounded spatial line, additive state-independent thermal noise, and environment switching independent of \(B\). The variance \(V\) is a **conditional variance given a complete two-sided environment history**, not the unconditional variance of \(X\). It can be random with an infinite mean. Beta laws are parameterized by the conventional positive shape parameters. The statement makes no claim about sample-estimation uncertainty or about models with correlated environmental switching and Brownian noise.

## Proof

**1. Stationarity and conditional Gaussianity.** For a two-sided stationary version of the switching chain, its invariant probabilities are \(\pi_+=w/(u+w)\) and \(\pi_-=u/(u+w)\). Its mean confining stiffness is
\[
 \overline A=\pi_+a-\pi_-b=\frac{aw-bu}{u+w}>0.
\]
The ergodic theorem gives \(t^{-1}\int_{-t}^0 A_{S_r}\,dr\to\overline A\) almost surely. Consequently the stochastic integral
\[
 X_0=\sqrt{2D}\int_{-\infty}^0
 \exp\!\left(-\int_s^0 A_{S_r}\,dr\right)\,dB_s
\]
converges conditionally in \(L^2\), yielding a stationary solution. Differences of solutions with the same driving noises contract almost surely like \(\exp(-\int_0^t A_{S_r}\,dr)\); the stationary joint law is therefore unique. Conditional on the environment path, \(X_0\) is centered Gaussian with
\[
 V_0=2D\int_{-\infty}^0
 \exp\!\left(-2\int_s^0 A_{S_r}\,dr\right)\,ds.
\]
Since \(A_s\le a\), one has \(V_0\ge c=D/a\), with strict inequality almost surely. Along each fixed switching trajectory the conditional variance evolves as the piecewise-deterministic Markov process
\[
 \dot V=2(D-aV)=-2a(V-c)\quad(S=+),\qquad
 \dot V=2(D+bV)=2b(V+d)\quad(S=-).
\]

**2. Stationary transport equation.** Let \(f_+(v)=-2a(v-c)\) and \(f_-(v)=2b(v+d)\) for \(v>c\). The conditional joint invariant densities \(p_+(v),p_-(v)\) (mass including environmental occupation) solve
\[
 (f_+p_+)'=-up_++wp_-,\qquad
 (f_-p_-)'=up_+-wp_-.
\]
The total stationary flux is zero: the sum \(f_+p_++f_-p_-\) is constant, while the invariant probability has no flux entering from \(v=c\) or from infinity. Hence \(f_+p_+=-f_-p_-=:q(v)\). Substitution gives
\[
 \frac{q'(v)}{q(v)}=\frac{u}{2a(v-c)}-\frac{w}{2b(v+d)}.
\]
Thus, for a negative normalization constant \(C\),
\[
 q(v)=C(v-c)^\eta(v+d)^{-\xi},\quad
 p_+(v)=-\frac C{2a}(v-c)^{\eta-1}(v+d)^{-\xi},\quad
 p_-(v)=-\frac C{2b}(v-c)^\eta(v+d)^{-\xi-1}.
\]
Both are integrable at \(c\) and infinity because \(\eta,\theta>0\). This furnishes an invariant probability density, whose uniqueness follows from the contraction argument in Step 1.

**3. Beta transformation and normalization.** Substitute \(y=(v-c)/(v+d)\); then \(v=(c+dy)/(1-y)\), \(v-c=Ly/(1-y)\), \(v+d=L/(1-y)\), and \(dv=L(1-y)^{-2}dy\). The preceding conditional densities become proportional to
\[
 p_+(y)\propto y^{\eta-1}(1-y)^{\theta-1},\qquad
 p_-(y)\propto y^\eta(1-y)^{\theta-1}.
\]
Their normalized conditional laws are exactly \(\operatorname{Beta}(\eta,\theta)\) and \(\operatorname{Beta}(\eta+1,\theta)\). Integrating the stationary environment equations yields the required weights \(\pi_+,\pi_-\). Alternatively, the ratio \(p_-(v)/p_+(v)=a(v-c)/(b(v+d))=(a/b)y\), whose beta-mean relation forces \(\pi_-/\pi_+=u/w\). Gaussian conditioning gives the displayed stationary density of \(X\).

**4. Exact tails and all moment cutoffs.** If \(Y\sim\operatorname{Beta}(h,\theta)\), then elementary integration near the right endpoint shows
\[
 \mathbb P(Y>1-\varepsilon)\sim
 \frac{\varepsilon^\theta}{\theta\mathrm B(h,\theta)}.
\]
As \(1-Y=L/(V+d)\), summing the two components gives \(\mathbb P(V>v)\sim K_Vv^{-\theta}\). Let \(Z\) be standard normal independent of \(V,S\). Since \(X\overset d=\sqrt V Z\), integrating these regularly varying tails over \(Z\) (split the integral at moderate Gaussian values and dominate the complement using Gaussian moments) gives
\[
 \mathbb P(|X|>x)\sim K_V\mathbb E|Z|^{2\theta}x^{-2\theta}
 =K_Xx^{-2\theta}.
\]
The same comparison proves exactly the moment condition \(\mathbb E|X|^p<\infty\iff p<2\theta\) for \(p\ge0\): the equality boundary diverges logarithmically by the positive power-law coefficient. Symmetry of centered Gaussian mixtures splits the two-sided tail equally.

**5. Universal extreme-state composition.** Conditional on \(S=s\), the tail of \(V\) has coefficient \(L^\theta/[\theta\mathrm B(h_s,\theta)]\). The Gaussian-factor contribution is identical in both states. Therefore
\[
 \lim_{x\to\infty}\mathbb P(S=-\mid |X|>x)
 =\frac{\pi_-/\mathrm B(\eta+1,\theta)}
 {\pi_+/\mathrm B(\eta,\theta)+\pi_-/\mathrm B(\eta+1,\theta)}.
\]
Using \(\mathrm B(\eta+1,\theta)=\eta/(\eta+\theta)\mathrm B(\eta,\theta)=\eta/\xi\,\mathrm B(\eta,\theta)\), \(\pi_-/\pi_+=u/w\), and \(\xi/\eta=aw/(bu)\) reduces this ratio to \(a/(a+b)\), proving the claim.

## Verification

The standalone script `check.py` reproduces the two conditional beta densities and tests the resulting moments against independently solved stationary Markov-generator moment recurrences. It checks the zero-flux identity pointwise in the variance coordinate. It was executed successfully on 36 parameter combinations, including 72 independent finite second/fourth-moment checks, 144 tail-amplitude and extreme-state-bias comparisons, and 1044 flux comparisons. These tests are finite diagnostic checks; the proof for all positive parameters is analytical in Steps 1–5. The checker uses Python, NumPy, and SciPy; it does not sample an infinite stationary trajectory to infer an exact tail law.

## Relationship to prior work

Guyon, Iovleff, and Yao (2004) establish ergodicity and moment conditions for Markov-switched linear diffusions, explicitly including an attractive/repulsive two-state example. De Saporta and Yao (2005; preprint March 24, 2005, following a 2004 note) establish the heavy-tail dichotomy and characterize its power exponent; in their two-state calculation the exponent is the same \(2\theta\) obtained above. These general results **are not claimed as discoveries** here. The present specific contribution is the fully normalized conditional beta-mixture law of the random conditional variance, its explicit heavy-tail prefactor, and the rate-independent extreme-environment composition. Zhang and Wang (author version public January 20, 2016) derive special stationary transforms assuming nonpositive drift coefficients in each regime and specifically exclude the explosive regime treated here. Ratanov (2021) concerns a different Kac/telegraph-noise model. Historical priority for the explicit beta-mixture and extreme-state-bias statements remains provisional.

## Limitations

The theorem requires state-independent positive Brownian diffusivity, linear stiffness with exactly one attractive and one repulsive regime, positive switching intensities, and mean confinement \(aw>bu\). The tail **exponent** and the existence of power-law tails are previously established in broader theories, so only the normalized mixture, prefactor, and rare-state composition are assessed as a contribution. No claim is made for nonlinear traps, correlated noise, higher dimensions, or finite-sample estimation. The originality comparison cannot exclude an as-yet-unidentified equivalent formula in older specialized telegraph-noise literature. Independent scientific review has not been performed.

## References

1. X. Guyon, S. Iovleff, and J.-F. Yao, "Linear diffusion with stationary switching regime," ESAIM: Probability and Statistics 8 (2004), 25–35. DOI: 10.1051/ps:2003017. Full text: https://www.numdam.org/item/10.1051/ps:2003017.pdf .
2. B. de Saporta and J.-F. Yao, "Tail of a linear diffusion with Markov switching," Annals of Applied Probability 15 (2005), 992–1018, arXiv:math/0503527 (first arXiv posting March 24, 2005). Earlier short note, Comptes Rendus Mathématique 339 (2004), 643–646; DOI: 10.1016/j.crma.2004.09.022.
3. Z. Zhang and W. Wang, "The stationary distribution of Ornstein–Uhlenbeck process with a two-state Markov switching," Communications in Statistics—Simulation and Computation 46 (2017), 4783–4794. Accepted author version posted January 20, 2016; DOI: 10.1080/03610918.2015.1132321.
4. N. Ratanov, "First-passage probabilities and invariant distributions of Kac–Ornstein–Uhlenbeck processes," arXiv:2102.13308 (2021); a different telegraph-noise system.
