# Algebraic first-passage tails and geometric–Rayleigh survivor selection under Pareto resetting

## Finding

Consider a Brownian particle on the positive half-line, absorbed at the origin and returned instantaneously to its starting position after independent Type-I Pareto clock intervals. For **every finite positive Pareto index**, including indices for which the mean reset interval is finite, the exact long-time probability of not yet hitting the target has a *power-law*, never an exponential, tail. Moreover, conditioning on an unusually long search selects a single exceptionally long ongoing excursion: the completed-reset count converges to a geometric law, independently of a Rayleigh-scaled current position.

Precisely, with the notation below, let \(T\) be absorption time, \(N(t)\) the number of completed resets by time \(t\) on the event \(T>t\), \(\sigma(t)\) the last reset epoch (zero if none), and \(X(t)\) the particle position. Put \(\alpha=\beta+1/2\) and \(z=a^2/(4D\tau_0)\). Then

\[
\mathbb P(T>t)\sim \frac{a\tau_0^\beta}{p\sqrt{\pi D}}\,t^{-(\beta+1/2)}, \qquad t\longrightarrow\infty,
\]

where the explicit single-attempt hit probability is

\[
p=\frac{\Gamma(1/2,z)+z^{-\beta}\gamma(\beta+1/2,z)}{\sqrt\pi}\in(0,1).
\]

Here \(\Gamma(s,z)\) and \(\gamma(s,z)\) are respectively the upper and lower incomplete gamma functions. With \(q=1-p\), for each integer \(n\ge0\),

\[
\mathbb P(N(t)=n\mid T>t)\longrightarrow p q^n,
\]

and jointly, conditional on \(T>t\),

\[
\left(N(t),\frac{X(t)}{\sqrt{Dt}},\frac{\sigma(t)}{t}\right)
\ \Longrightarrow\ (G,Z,0),
\]

where \(\mathbb P(G=n)=pq^n\), \(G\) is independent of \(Z\), and \(Z\) has the Rayleigh-type density \(f_Z(y)=\frac y2 e^{-y^2/4}\) for \(y>0\). Consequently, for every real \(s>0\),

\[
\mathbb E[T^s]<\infty\quad\Longleftrightarrow\quad s<\beta+\frac12.
\]

In particular the mean is finite exactly for \(\beta>1/2\), and the variance is finite exactly for \(\beta>3/2\). These moment boundaries follow from the proved tail equivalence and are included for clarity; the general mean-moment criterion for restart processes was already available in earlier renewal literature.

## Assumptions and scope

Fix \(a,D,\tau_0,\beta>0\). Between clock events, independently on each attempt, the particle follows \(X_s=a+\sqrt{2D}B_s\), where \(B\) is standard Brownian motion. It is absorbed at the first time it reaches \(0\). If the independent reset clock \(R\) rings first, the particle returns instantly to \(a\), a fresh independent Brownian path and clock are drawn, and the experiment continues. The reset law is exactly

\[
\mathbb P(R>u)=
\begin{cases}
1,&0\le u<\tau_0,\\
(\tau_0/u)^\beta,&u\ge\tau_0.
\end{cases}
\]

No reflecting boundary, confinement, drift, reset latency, state-dependent rate, or second target is assumed. Equality of independent continuous times has probability zero. The claims are for fixed positive model parameters and \(t\to\infty\), and do not assert uniformity as \(\beta\to\infty\) or \(\tau_0\to0\).

## Proof

**1. One-attempt survival, success probability, and defective reset kernel.** Let \(H\) be the unreset Brownian hitting time of \(0\). The reflection principle gives

\[
S_0(u)=\mathbb P(H>u)=\operatorname{erf}\!\left(\frac{a}{\sqrt{4Du}}\right),\qquad
f_H(u)=\frac{a\,e^{-a^2/(4Du)}}{\sqrt{4\pi D}\,u^{3/2}},
\]

and \(S_0(u)\sim a/(\sqrt{\pi D}\sqrt u)\) as \(u\to\infty\). The probability of target capture within a single attempt is \(p=\mathbb P(H<R)\), and the probability that the attempt ends instead in a reset is \(q=\mathbb P(R<H)=1-p\). In particular \(0<p,q<1\). Integrating \(f_H\) over \(u<\tau_0\) and over \(u\ge\tau_0\), weighted by \((\tau_0/u)^\beta\) on the latter range, and substituting \(v=a^2/(4Du)\), gives the displayed incomplete-gamma formula for \(p\).

The probability that the first attempt survives *both* hitting and resetting to time \(t\) is

\[
h(t)=S_0(t)\mathbb P(R>t)
\sim c t^{-\alpha},\qquad c=\frac{a\tau_0^\beta}{\sqrt{\pi D}},\quad\alpha=\beta+\frac12>0.
\]

The density of an unsuccessful, reset-terminated attempt is

\[
k(u)=S_0(u)\frac{\beta\tau_0^\beta}{u^{\beta+1}}\mathbf 1_{\{u\ge\tau_0\}}.
\]

It is nonnegative, bounded, supported in \([\tau_0,\infty)\), has mass \(\int_0^\infty k(u)du=q\), and satisfies \(k(u)=O(u^{-\alpha-1})\).

**2. Exact regenerative expansion and a proved convolution estimate.** Writing convolution on \([0,\infty)\) as \(*\), the strong Markov and renewal properties give, exactly,

\[
S(t):=\mathbb P(T>t)=h(t)+(k*S)(t)
=\sum_{n=0}^\infty(k^{*n}*h)(t),
\]

where \(k^{*0}\) is unit mass at zero. The \(n\)-th summand is exactly \(\mathbb P(T>t,N(t)=n)\). Let \(u=\sum_{n\ge1}k^{*n}\) denote the density of the renewal measure excluding its zero atom. By Tonelli, \(u\ge0\), \(\int_0^\infty u=q/(1-q)=q/p\), and \(u=k+k*u\).

We justify the long-time estimate rather than assuming it from a simulation. Choose \(\delta\) strictly between \(\max(0,1-\alpha)\) and \(1\), and put \(b(t)=(1+t)^{-(\alpha+\delta)}\). Thus \(b\) is integrable and \(k(t)/b(t)\to0\). Split \((k*b)(t)\) at \(t/2\): dominated convergence on the first half gives \((k*b)(t)/b(t)\to q\), while on the second half \(k(s)=O(t^{-\alpha-1})\) and \(\int b<\infty\), giving a relative bound \(O(t^{\delta-1})\to0\). Hence \((k*b)(t)/b(t)\to q<1\).

Take \(\varepsilon>0\) with \(q+\varepsilon<1\). For large enough \(t_0\), \((k*b)(t)\le(q+\varepsilon)b(t)\) for \(t\ge t_0\). Since \(k/b\) is bounded and \(u\) is bounded on finite intervals (the support of \(k\) is separated from zero), choose \(C<\infty\) so that \(u\le Cb\) up to \(t_0\) and \(k\le C(1-q-\varepsilon)b\) thereafter. The identity \(u=k+k*u\) and induction in intervals of width \(\tau_0\) imply \(u(t)\le Cb(t)\) for every \(t\ge0\). This is a direct integrable power-envelope proof of the bound needed below.

Now split \((u*h)(t)\) at \(t/2\). On \(0\le s\le t/2\), regular variation of \(h\) and dominated convergence yield

\[
\int_0^{t/2}u(s)h(t-s)\,ds\sim\frac{q}{p}h(t).
\]

On \(t/2<s<t\), the envelope above gives

\[
\int_{t/2}^t u(s)h(t-s)ds
\le C' t^{-\alpha-\delta}\int_0^{t/2}h(v)dv=o(t^{-\alpha})=o(h(t)),
\]

because the last integral is \(O(1)\), \(O(\log t)\), or \(O(t^{1-\alpha})\) according as \(\alpha>1\), \(\alpha=1\), or \(0<\alpha<1\), and our choice of \(\delta\) covers each case. Therefore \(S=h+u*h\sim(1+q/p)h=h/p\), proving the exact tail constant for every \(\beta>0\). Integrating the survival tail by the layer-cake identity \(\mathbb E T^s=s\int_0^\infty t^{s-1}S(t)dt\) proves the strict moment cutoffs, including divergence at equality.

**3. Conditional completed-reset count and last-reset epoch.** For each fixed \(n\ge1\), \(k^{*n}\le u\), and its mass is \(q^n\). The same split argument gives \((k^{*n}*h)(t)\sim q^n h(t)\), with the \(n=0\) statement immediate. Dividing by \(S(t)\sim h(t)/p\) gives the geometric limit \(p q^n\). The limiting probabilities sum to one, so the reset-count laws are tight, and no mass is lost at unbounded \(n\).

For each fixed \(n\), the convolution integral defining \((k^{*n}*h)(t)\), restricted to prior reset duration \(s\ge\epsilon t\), is \(o(h(t))\) for every \(\epsilon>0\): use the finite mass and tail decay of \(k^{*n}\le u\) for \(\epsilon t\le s\le t/2\), and the integrable power-envelope bound for \(s>t/2\). Thus, conditional on \(T>t,N(t)=n\), the total duration of the first \(n\) unsuccessful attempts is \(o(t)\) in probability. Combined with tightness of \(N(t)\), this proves \(\sigma(t)/t\to0\) conditionally.

**4. The surviving endpoint law.** The absorbing Brownian heat kernel is

\[
G_v(a,y)=\frac{1}{\sqrt{4\pi Dv}}
\left[\exp\!\left(-\frac{(y-a)^2}{4Dv}\right)-
\exp\!\left(-\frac{(y+a)^2}{4Dv}\right)\right],\quad y>0.
\]

Its integral over \(y>0\) is \(S_0(v)\). Under conditioning on \(H>v\), substitution \(y=\sqrt{Dv}\,z\), a first-order expansion in \(a/\sqrt{Dv}\), and dominated convergence show

\[
\frac{X_v}{\sqrt{Dv}}\ \Longrightarrow\ Z,\qquad
f_Z(z)=\frac z2e^{-z^2/4}\mathbf1_{\{z>0\}}.
\]

Given \(N(t)=n\) and its total prior-reset duration \(s\), the currently surviving segment is just such an absorbing Brownian excursion, conditioned to survive duration \(t-s\); conditioning on \(R>t-s\) does not further modify its spatial distribution because the clock is independent. For each fixed \(n\), Step 3 gives \(s/t\to0\). Therefore the conditional spatial limit is \(Z\) for every \(n\), with the same limit independent of \(n\); tightness of the count permits mixing over \(n\). This proves the full joint convergence, including asymptotic independence.

## Verification

The accompanying standalone `VERIFY.py` computes the one-attempt probability both from the incomplete-gamma identity and direct quadrature of the Brownian first-hit density; independently integrates the unsuccessful-reset kernel; tests the defective-renewal survival equation through an FFT discretization at large times; and checks the absorbing-kernel conditional spatial distribution against the Rayleigh limit. These finite calculations check constants, signs, normalization, and limiting trends. The infinite-time equivalences and universal quantifiers follow from Steps 1–4, not the finite numerical tests.

## Relationship to prior work

Liu, Li, Ghosh, Nayak and Marchesoni (2024, Section 3 and Figure 2(a)) investigate a Pareto-reset free-Brownian first-passage benchmark as part of their analysis of autonomous ratcheting. The numerically observed exponential-looking regime at large Pareto indices is a finite-time feature: the present exact asymptotic establishes an eventual algebraic tail for every fixed finite index. No assertion is made about the separate ratchet-potential first-passage problem.

Nagar and Gupta (arXiv:1512.02092, Section on first-passage time) derive a renewal treatment and mean-first-passage formulas for the same power-law-clock family. Godrèche and Luck (arXiv:2309.06997, Section 7, Equations (7.1) and (7.2)) establish the general first-passage restart transform, the unconditional geometric number of failed attempts, and the general mean-moment criterion. **These previously established facts are not claimed as new here.** The distinguishing results are the sharp, all-index asymptotic survival equivalent with evaluated coefficient and the *long-time-survivor* joint geometric–Rayleigh limit and vanishing relative last-reset epoch. These do not follow as stated merely from an unconditional geometric count or the general renewal transform without further heavy-tail and conditional spatial analysis.

Masó-Puigdellosas, Campos and Méndez (arXiv:2205.01613) condition the backward and forward clock ages on the particle's current position in a non-absorbing reset process, rather than on survival against a target. Linn and Lawley (arXiv:2302.05409) treat a distinct limit in which the resetting becomes frequent, not a fixed Pareto clock followed to arbitrarily long observation times.

## Limitations

The result is limited to one-dimensional free Brownian motion, an absorbing point, independent fresh-clock resetting to a fixed positive start, and strictly positive Type-I Pareto parameters. It gives no uniform error estimate in \(\beta\) or an explicit crossover time; for large \(\beta\), preasymptotic behavior may resemble exponential decay over long accessible windows. The full conditional path, not just its time-\(t\) endpoint, is not classified. A general renewal identity and the mean threshold already exist, so the exact boundary between this asymptotic refinement and possible implicit coverage by earlier renewal theory merits independent publication-priority review. The result has not undergone independent verification.

## References

1. J. Liu, Y. Li, P. K. Ghosh, S. Nayak and F. Marchesoni, “Ratcheting by Stochastic Resetting With Fat-Tailed Time Distributions,” *ChemPhysChem* 25 (2024), e202400313. First online 2024-08-12. DOI: https://doi.org/10.1002/cphc.202400313 .
2. A. Nagar and S. Gupta, “Diffusion with stochastic resetting at power-law times,” *Physical Review E* 93 (2016), 060102. https://arxiv.org/abs/1512.02092 .
3. C. Godrèche and J.-M. Luck, “Replicating a renewal process at random times,” https://arxiv.org/abs/2309.06997 (especially §7).
4. A. Masó-Puigdellosas, D. Campos and V. Méndez, “Conditioned backward and forward times of diffusion with stochastic resetting: a renewal theory approach,” https://arxiv.org/abs/2205.01613 .
5. S. Linn and S. D. Lawley, “First passage times under frequent stochastic resetting,” *Physical Review E* 108 (2023), 024114, https://arxiv.org/abs/2302.05409 .
