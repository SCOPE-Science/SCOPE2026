# Extreme-position velocity and reset-age boundary layers in a harmonically trapped particle driven by resetting Brownian noise

## Finding
Consider a stationary one-dimensional process driven by Brownian noise that resets but whose position does **not** reset. At an exceptionally large observed position, most particles move with an outward-biased Gaussian velocity, despite **exactly zero conditional mean velocity at every position**. A vanishing fraction of newly reset trajectories carries a compensating inward current.

For all \(\mu,r,D>0\), let \(Y\) evolve as Brownian motion with infinitesimal variance \(2D\) and independently reset to zero at Poisson rate \(r\). Let \(X\) solve \(dX/dt=-\mu X+rY\), without resets of \(X\). Write \(S\) for time elapsed since the last reset of \(Y\), \(W=-\mu X+rY\) for instantaneous velocity, and \(\sigma=\operatorname{sgn}(x)\) when conditioning on \(X=x\neq0\). Set
\[
 k=\frac{\mu}{\sqrt{Dr}},\qquad c=\frac{\mu}{2r\sqrt{Dr}},\qquad m=\frac{r\sqrt{Dr}}{\mu},\qquad v=\frac{Dr^2}{\mu}.
\]
Then the following claims hold as \(|x|\to\infty\):

**(i) Typical extreme-position trajectories.** Under the regular conditional law given \(X=x\),
\[
 \left(\frac{S-c|x|}{\sqrt{c|x|/(2r)}},\;\sigma W\right)
 \Longrightarrow (Z,V),
\]
where \(Z\sim N(0,1)\), \(V\sim N(m,v)\), and the two limiting variables are independent. In particular,
\[
 \lim_{|x|\to\infty}\Pr(\sigma W<0\mid X=x)
 =\Phi\!\left(-\sqrt{r/\mu}\right).
\]

**(ii) Thin young-reset population.** For each fixed \(H>0\),
\[
 \lim_{|x|\to\infty}|x|\Pr\!\left(S\le\frac{H}{|x|}\,\middle|\,X=x\right)
 =\frac{r}{k\mu}\left(1-e^{-k\mu H}\right).
\]
Equivalently, on every fixed compact interval of nonnegative \(h\), the locally finite measures \(|x|\Pr(|x|S\in dh\mid X=x)\) converge to \(r e^{-k\mu h}\,dh\). Conditioned on that young-reset event, \(W/|x|\to-\sigma\mu\) in probability. Thus its contribution to \(\mathbb E[\sigma W\mid X=x]\), first taking \(|x|\to\infty\) and then \(H\to\infty\), is \(-r/k=-m\).

**(iii) Exact stationary flux cancellation.** For every real \(x\), the canonical smooth conditional density version satisfies
\[
 \mathbb E[W\mid X=x]=0.
\]
The Gaussian limit in (i) is therefore not uniformly integrable in its first moment: the thin class (ii) explains the missing mean. The statement is not about velocity moments converging to those of the weak Gaussian limit.

## Assumptions and scope
Only the stationary **Poissonian noise-reset** process above is considered. The position is continuous through reset events; its derivative has a jump at those events, which are null at an independent stationary observation time. The reset-age \(S\) is backward recurrence time at a stationary observation, so it is exponential with rate \(r\). All limits take \(|x|\to\infty\) with \(\mu,r,D\) fixed; the two signs follow by reflection symmetry. The source result below provides the sharp stationary position-density tail
\[
 p_X(x)\sim\frac{k}{2}e^{-3r/(2\mu)}e^{-k|x|},\qquad |x|\to\infty.
\]
This published position marginal is used as a premise, **not claimed as new**.

## Proof
**1. Regenerative Gaussian representation.** At the last noise-reset event, let \(U\) denote the inherited position. The Poisson memoryless property (and stationarity) makes \(U\), the new Brownian increments, and \(S\sim\operatorname{Exp}(r)\) mutually independent; \(U\) has the stationary density \(p_X\), by PASTA. Conditional on \(S=s\),
\[
 X=e^{-\mu s}U+G_s,\quad W=-\mu e^{-\mu s}U+H_s,
\]
where \((G_s,H_s)\) is centered Gaussian, with
\[
\begin{aligned}
 V_s:=\operatorname{Var}G_s&=\frac{2Dr^2}{\mu^2}\left[s-\frac{2(1-e^{-\mu s})}{\mu}+\frac{1-e^{-2\mu s}}{2\mu}\right],\\
 C_s:=\operatorname{Cov}(G_s,H_s)&=\frac{Dr^2}{\mu^2}(1-e^{-\mu s})^2,\\
 Q_s:=\operatorname{Var}H_s&=\frac{Dr^2}{\mu}(1-e^{-2\mu s}).
\end{aligned}
\]
These follow directly from stochastic integrals
\(G_s=(r\sqrt{2D}/\mu)\int_0^s(1-e^{-\mu(s-t)})\,dB_t\) and
\(H_s=r\sqrt{2D}\int_0^s e^{-\mu(s-t)}\,dB_t\).
For large \(s\), \(V_s=A(s-3/(2\mu))+O(e^{-\mu s})\), \(C_s=A/2+O(e^{-\mu s})\), \(Q_s=v+O(e^{-2\mu s})\), with \(A=2Dr^2/\mu^2\). For short \(s\), \(V_s=\frac23Dr^2s^3+O(s^4)\).

**2. Dominant age and conditional velocity.** The exact stationary position-age density is
\[
 f_{X,S}(x,s)=re^{-rs}\,\mathbb E\left[\frac{\exp\{-\frac{(x-e^{-\mu s}U)^2}{2V_s}\}}{\sqrt{2\pi V_s}}\right].
\]
For \(s\) of order \(|x|\), the inherited-position term is exponentially suppressed. The leading exponent of the Gaussian mixture is \(F_x(s)=rs+x^2/(2As)\), with unique minimum at \(s_*=c|x|\), \(F_x''(s_*)=2r/s_*\). Standard one-dimensional Laplace localization yields a centered Gaussian age fluctuation of variance \(s_*/(2r)\). To control competing ages, split the exact mixture into \(s\le H/|x|\), \(H/|x|<s<\varepsilon|x|\), \(\varepsilon|x|\le s\le M|x|\), and \(s>M|x|\); the published exponential bound on \(p_X\), the small-\(s\) Gaussian variance, and the strict Laplace rate away from \(s_*\) bound the off-saddle mass. For fixed \(H\), the first class is only of order \(|x|^{-1}\) of the position density (proved below); the remaining off-saddle classes vanish after \(H\uparrow\infty\), \(\varepsilon\downarrow0\) and \(M\uparrow\infty\). In the saddle neighborhood, the conditional law of \(H_s\), given \(G_s=x-e^{-\mu s}U\), is
\[
 N\left(\frac{C_s}{V_s}(x-e^{-\mu s}U),\;Q_s-\frac{C_s^2}{V_s}\right).
\]
Its mean tends to \(\sigma (A/2)/(Ac)=\sigma m\), variance tends to \(v\), uniformly on a saddle-scaled bounded age window. The limiting Gaussian characteristic function factors from that of the centered age, proving (i). Since \(m/\sqrt v=\sqrt{r/\mu}\), the wrong-direction limit follows.

**3. The thin age layer.** Set \(s=h/|x|\), where \(h\in[0,H]\). Here \(\sqrt{V_s}=O(|x|^{-3/2})\) and \(e^{-\mu s}=1-\mu h/|x|+O(|x|^{-2})\). Smooth convolution and the exact exponential positional tail imply, uniformly for bounded \(h\),
\[
 \frac{f_{X\mid S=h/|x|}(x)}{p_X(x)}\longrightarrow e^{-k\mu h}.
\]
Indeed \(x e^{\mu h/|x|}=x+\sigma\mu h+o(1)\), and the Jacobian of the inherited-position change approaches one. Multiply by \(re^{-rs}\,ds=(r/|x|)(1+o(1))\,dh\) to get the density convergence and (ii). Since \(W=-\mu e^{-\mu s}U+H_s\), while \(X=e^{-\mu s}U+G_s\), \(W=-\mu X+\mu G_s+H_s\); the last two terms have variance tending to zero within the layer. Therefore \(W/|x|\to-\sigma\mu\), also after conditional weighting. The bounded-\(h\) layer's signed flux converges to \(-\mu r\int_0^H e^{-k\mu h}dh\); taking \(H\to\infty\) gives \(-r/k=-m\).

**4. Zero current at every position.** Since \(X\) has continuous paths and derivative \(W\) except at a discrete set of noise-reset instants, stationarity yields \(\mathbb E[W f'(X)]=0\) for each smooth compactly supported test \(f\). Hence the distributional current \(j(x)=p_X(x)\mathbb E[W\mid X=x]\) is constant. Integrability of \(W\), together with \(\int|j(x)|dx\le\mathbb E|W|<\infty\), forces that constant to be zero. Gaussian smoothing gives the canonical continuous conditional version, proving (iii). The typical Gaussian drift \(+m\) and the thin-layer drift \(-m\) are equal and opposite as claimed.

## Verification
The included standalone `check_science.py` independently integrates Gaussian stochastic-kernel covariances and numerically evaluates the no-inherited-position saddle integrals for three nontrivial parameter triples. The density-tail, age-scale, mean-velocity, wrong-direction probability and flux-coefficient comparisons all pass. Numerical saddle tests validate only the **dominant-age component**; the full stationary-process assertions rely on the proofs above, the published positional tail, and the young-age density-ratio argument, not on a simulation that could miss rare events. Run `python check_science.py` with Python, NumPy and SciPy available.

## Relationship to prior work
Guéneau, Majumdar and Schehr (2023), arXiv:2306.09453, introduce exactly this resetting-noise harmonic model, determine the stationary position law and its exponential tail (their §4.4, Eq. 81 and Appendix F), and compute two-time position correlations (§4.5, Appendix G). Their analyses provide the essential input but do not report the conditional far-tail velocity Gaussian law, exponentially distributed age saddle, the \(|x|^{-1}\) newly-reset population, or its finite hidden contribution to zero current. General large-deviation and stationary-flux frameworks are background tools rather than statements of this three-part specialized conclusion. These comparisons concern implications, not absence of matching keywords.

## Limitations
This is a fixed-parameter, one-dimensional, stationary Poisson-noise-reset result, not a result for direct position resetting, finite-time observations, periodic resetting, or arbitrary resetting noise. The source's positional tail is an explicit prior premise. The age-layer convergence is local on bounded scaled-age intervals; it is **not** a total-variation approximation for the entire conditional age distribution. Weak velocity convergence does **not** extend to first moments, and this nonuniformity is essential. The analysis does not determine higher weighted contributions of intermediate-age classes or give finite-distance error constants. Literature noncoverage cannot prove global novelty, and no independent audit has been performed.

## References
1. M. Guéneau, S. N. Majumdar, and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453, initial preprint 2023-06-15, https://arxiv.org/abs/2306.09453; full text https://arxiv.org/html/2306.09453v2, §4.4, Appendix F and §4.5.
2. H. Touchette, *The large deviation approach to statistical mechanics*, Physics Reports 478 (2009), arXiv:0804.0327. Background on Laplace principles; not a source for the specialized claim.
