# Singular resource selection and a quadratic noise clock in a Bayesian harvesting game

## Finding

In the continuous-resource, four-phenotype Gaussian-perception evolutionary game of Patra, Das Bairagya and Chakraborty [1], fix the perception threshold \(c\in(0,1)\) and the harvesting-feedback balance \(\theta=(1-c)/c\). For every finite sensory-noise strength \(0<\sigma<\infty\), every strictly interior phenotype–resource trajectory converges to one equilibrium. The phenotype distribution selects the contingent action \(HL\), and the environmental abundance tends to the unique \(n_\sigma\in(0,1)\) satisfying \(\omega_\sigma(n_\sigma)=c\).

As noise becomes large, this equilibrium has the universal selected limit and relaxation exponent
\[
 n_\sigma=\frac{1+c}{3}+O(\sigma^{-2}),\qquad
 \lambda_\sigma=-\frac{\epsilon(1-c)(1+c)(2-c)}{18\sigma^2}+O(\sigma^{-4}).
\]
The equilibrium limit is independent of the four-strategy initial composition and of the strictly ordered payoff values. In contrast, at exactly infinite noise the environmental equilibria form a continuum, and the dynamics can preserve explicit information about the initial state. For the fully interior example \(R=S=0\), \(T=P=1\), with all four phenotypes initially of frequency \(1/4\) and any \(n(0)=n_0\in(0,1)\),
\[
\lim_{\sigma\to\infty}\lim_{t\to\infty}n_\sigma(t)=\frac{1+c}{3},\qquad
\lim_{t\to\infty}\lim_{\sigma\to\infty}n_\sigma(t)=n_0.
\]
On the stretched time \(t=\sigma^2\tau\), the finite-noise resource converges at each \(\tau>0\), uniformly on compact subintervals of \((0,\infty)\), to the solution \(u(\tau)\) of
\[
\frac{du}{d\tau}=\frac{\epsilon(1-c)}2u(1-u)\left(\frac{1+c}{3}-u\right),\qquad u(0)=n_0.
\]
Thus the infinite-noise degeneracy hides a precise order-\(\sigma^2\) restoration clock. For \(c=1/5\), \(n_0=4/5\), the two iterated limits are respectively \(2/5\) and \(4/5\).

## Assumptions and scope

The underlying population is deterministic, infinitely large, and well mixed. Resource abundance \(n\) lies in \((0,1)\). Four heritable contingent strategies \(LL,LH,HL,HH\) are indexed by their action under perceived *replete* and perceived *depleted* conditions, respectively; the first component denotes the replete action. Write their positive frequencies \(z_{LL},z_{LH},z_{HL},z_{HH}\), with sum one. The low-harvester marginals are \(x=z_{LL}+z_{LH}\) and \(y=z_{LL}+z_{HL}\); linkage deviation is \(D=z_{LL}-xy\). These definitions fix the phenotype convention independently of shorthand labels.

The perceived depleted-state probability is the normalized truncated-Gaussian probability, for \(0<\sigma<\infty\),
\[
 \omega_\sigma(n)=
 \frac{\int_0^c\exp[-(v-n)^2/(2\sigma^2)]\,dv}
 {\int_0^1\exp[-(v-n)^2/(2\sigma^2)]\,dv},
 \qquad p_\sigma(n)=1-\omega_\sigma(n).
\]
For two-action payoff entries \(R,S,T,P\), assume the strict reversed-dominance ordering \(T>R\) and \(P>S\). Define
\[
 h=p_\sigma(n)x+\omega_\sigma(n)y,\quad
 k=(R-T)h+(S-P)(1-h)<0.
\]
The full equations, in the source's normalization [1, Eqs. (7)–(8)], are
\[
\begin{aligned}
 \dot x&=[p_\sigma x(1-x)-\omega_\sigma D]k,\\
 \dot y&=[-\omega_\sigma y(1-y)+p_\sigma D]k,\\
 \dot D&=[p_\sigma(1-2x)-\omega_\sigma(1-2y)]kD,\\
 \dot n&=\epsilon n(1-n)[-1+(1+\theta)h].
\end{aligned}
\]
Here \(\epsilon>0\), \(\theta=(1-c)/c\), and all unlabelled perception probabilities are evaluated at \(n\). At \(\sigma=\infty\), \(\omega_\infty(n)\equiv c\) is defined by the continuous high-noise limit; it is not finite positive noise. In the explicit memory and time-rescaling parts alone, impose \(R=S=0\), \(T=P=1\), and initially independent strategy coordinates \(D(0)=0\). For the displayed noncommuting-limit and stretched-time conclusions, further set \(x(0)=y(0)=1/2\), which is equivalent to \(z_{ij}(0)=1/4\).

## Proof

**1. Uniform selection of the contingent phenotype.** Put \(d=\min\{T-R,P-S\}>0\). The payoff difference between a low and a high action under replete perception is \(k\), whereas the corresponding difference under depleted perception is \(-k\). Hence the pure strategy \(HL\) strictly dominates each of the other three contingent phenotypes, with exact replicator log-ratio differences
\[
\begin{aligned}
\frac{d}{dt}\log\frac{z_{HL}}{z_{LL}}&=-p_\sigma(n)k,\\
\frac{d}{dt}\log\frac{z_{HL}}{z_{HH}}&=-\omega_\sigma(n)k,\\
\frac{d}{dt}\log\frac{z_{HL}}{z_{LH}}&=-k.
\end{aligned}
\]
Because \(-k\ge d\) and, for fixed finite \(\sigma\), the two perception probabilities have a strictly positive minimum on the compact resource interval, every other phenotype decays exponentially relative to \(HL\). Therefore
\[
 z_{HL}(t)=1-O(e^{-\gamma t}),\quad
 x(t)=O(e^{-\gamma t}),\quad 1-y(t)=O(e^{-\gamma t})
\]
for some \(\gamma>0\) determined by the parameters and initial population, without any assumption on the resource's trajectory. For \(\sigma\ge1\), the Gaussian kernel on the unit interval lies between \(e^{-1/2}\) and \(1\), giving a rate \(\gamma\) uniformly bounded away from zero as \(\sigma\to\infty\).

**2. Global selection of an interior resource equilibrium.** Differentiating the normalized Gaussian integral with respect to \(n\) yields
\[
 \omega_\sigma'(n)=\sigma^{-2}\operatorname{Cov}_{\sigma,n}
 (V,\mathbf1_{\{V<c\}})<0,
\]
where \(V\) has the density proportional to \(\exp[-(v-n)^2/(2\sigma^2)]\) on \([0,1]\). The inequality is strict because lower values of \(V\) have strictly larger indicator values. At \(n=0\) the density decreases strictly with \(v\), so \(\omega_\sigma(0)>c\); at \(n=1\) it increases strictly, so \(\omega_\sigma(1)<c\). Consequently the equation \(\omega_\sigma(n)=c\) has a unique root \(n_\sigma\in(0,1)\).

The harvesting balance turns the environmental equation into
\[
\dot n=\frac{\epsilon}{c}n(1-n)
 \left[\omega_\sigma(n)-c+
 p_\sigma(n)x-\omega_\sigma(n)(1-y)\right].
\]
The last two terms vanish exponentially by Step 1. For every small \(\delta>0\), eventually \(\dot n>0\) below \(n_\sigma-\delta\), and \(\dot n<0\) above \(n_\sigma+\delta\); the signs hold uniformly in those closed subintervals. Invariance of \(0<n<1\), and the inward-pointing barriers, imply \(n(t)\to n_\sigma\). This is a global statement for strictly positive genotype frequencies and interior resource; no inference from a local Jacobian alone is used.

**3. Universal high-noise selection and the slow eigenvalue.** Taylor expansion of the numerator and denominator integrands, uniformly for \(v,n\in[0,1]\), gives
\[
\omega_\sigma(n)=c+
 \frac{c(1-c)}{2\sigma^2}\left(\frac{1+c}{3}-n\right)
 +O(\sigma^{-4}),\qquad
 \omega_\sigma'(n)=-\frac{c(1-c)}{2\sigma^2}+O(\sigma^{-4}).
\]
For clarity, the coefficient follows from the exact moments
\[
 \int_0^c(v-n)^2\,dv=\frac{c^3}{3}-c^2n+cn^2,\qquad
 \int_0^1(v-n)^2\,dv=\frac13-n+n^2.
\]
Substituting the unique root and using the uniform strict leading derivative gives \(n_\sigma=(1+c)/3+O(\sigma^{-2})\). At the all-\(HL\) equilibrium, the resource-direction Jacobian eigenvalue equals
\[
 \lambda_\sigma=\frac{\epsilon}{c}n_\sigma(1-n_\sigma)
 \omega_\sigma'(n_\sigma)
 =-\frac{\epsilon(1-c)(1+c)(2-c)}{18\sigma^2}+O(\sigma^{-4}).
\]
The other phenotype-direction rates remain bounded strictly negative as \(\sigma\to\infty\). Thus the resource relaxation clock diverges proportionally to \(\sigma^2\).

**4. Exact infinite-noise memory.** In the payoff slice \(R=S=0,T=P=1\), we have \(k\equiv-1\). Since \(D(0)=0\), the equation for \(D\) preserves \(D\equiv0\), and, at \(\sigma=\infty\),
\[
 \dot x=-(1-c)x(1-x),\quad
 \dot y=cy(1-y),\quad
 \frac{d}{dt}\log\frac{n}{1-n}
 =\frac{\epsilon}{c}[(1-c)x+c(y-1)].
\]
For arbitrary \(x_0,y_0\in(0,1)\), the logistic solutions obey
\[
 \int_0^\infty(1-c)x(t)\,dt=-\log(1-x_0),\qquad
 \int_0^\infty c(y(t)-1)\,dt=\log y_0.
\]
Hence the exact infinite-noise terminal abundance satisfies
\[
 \operatorname{logit}n_\infty(\infty)=
 \operatorname{logit}n_0+
 \frac{\epsilon}{c}\log\frac{y_0}{1-x_0}.
\]
For \(x_0=y_0=1/2\), this shift vanishes and \(n_\infty(\infty)=n_0\), proving the claimed noncommutation of finite-noise and infinite-noise long-time limits. Continuous dependence of the smooth vector field on \(\sigma^{-2}\) proves the inner \(\sigma\to\infty\) limit at every finite physical time.

**5. The stretched-time crossover.** Retain \(x_0=y_0=1/2\), \(D_0=0\), the payoff slice in Step 4, and let \(\ell_\sigma=\operatorname{logit}n_\sigma\). Decompose
\[
 \frac{d\ell_\sigma}{dt}
 =\frac{\epsilon}{c}[\omega_\sigma(n_\sigma)-c]+r_\sigma(t),\quad
 r_\sigma(t)=\frac{\epsilon}{c}
 [p_\sigma(n_\sigma)x_\sigma-\omega_\sigma(n_\sigma)(1-y_\sigma)].
\]
Step 1 bounds \(|r_\sigma(t)|\le Ce^{-\gamma t}\), with \(C,\gamma>0\) independent of \(\sigma\ge1\). Continuous dependence at fixed times and the common exponential envelope show
\[
\lim_{\sigma\to\infty}\int_0^\infty r_\sigma(t)\,dt
 =\int_0^\infty r_\infty(t)\,dt=0
\]
by Step 4. For each \(\delta>0\), the same convergence is uniform when the upper limit is \(\sigma^2\tau\) with \(\tau\ge\delta\), since the missing exponential tail is uniformly negligible. Now integrate the high-noise expansion in Step 3 on \(t=\sigma^2\tau\). The accumulated nontransient term converges to
\[
 \frac{\epsilon(1-c)}2
 \int_0^\tau\left[\frac{1+c}{3}-
 \operatorname{logistic}(\ell_\sigma(\sigma^2s))\right]ds.
\]
Its expansion error is \(O(\tau\sigma^{-2})\). The transient contribution is negligible for positive stretched times; the interval \([0,\delta]\) contributes at most a constant times \(\delta\) to the slow integral. Standard Gronwall comparison, followed by \(\delta\downarrow0\), yields local uniform convergence on every \([\delta,T]\subset(0,\infty)\) to the unique limiting logit solution with initial value \(\operatorname{logit}n_0\). Converting back to abundance gives the cubic flow in the Finding. The qualifier \(\tau>0\) is essential: a nontrivial fast transient can survive inside a boundary layer near \(\tau=0\), even when its net logit shift is zero.

## Verification

The included standalone `checker.py` uses only the Python standard library. Running `python3 checker.py` checks: reconstruction of the full four-phenotype replicator equations from explicit phenotype payoffs; exact rational moment identities for the Gaussian expansion; monotone roots for several thresholds and noise strengths; an independent numerical integration of the infinite-noise initial-memory identity; and direct integrations of the full finite-noise equations against the scaled cubic prediction. Numerical runs are finite consistency checks; the all-parameter and infinite-time conclusions rely on the proofs above. For \(c=1/5\), computed finite-noise equilibria at \(\sigma=1,3,10,30\) are respectively approximately \(0.397592754,0.399733236,0.399975999,0.399997333\), tending to the exact value \(2/5\).

## Relationship to prior work

Patra, Das Bairagya and Chakraborty [1] formulate this continuous-resource noisy Bayesian harvesting system, characterize equilibria and show numerical noise–feedback phase regions. Their Fig. 4 singles out the critical harvesting balance and notes the collapse of the partially depleted region at infinite noise. The finding here analyzes that critical balance quantitatively: strict-global phenotype selection and environmental convergence for finite noise, the universal finite-noise selected limit, the exact infinite-noise memory law, and the quadratic slow-time crossover. It does **not** claim novelty for the underlying game, its stationary fixed points, or general asymptotically autonomous comparison techniques.

Mondal and Chakraborty [2] investigate noisy perception in a two-state stochastic repeated-game resource, not this continuous Gaussian-perception four-phenotype deterministic flow. Weitz and coauthors [3] analyze feedback-evolving replicator games without this truncated-Gaussian high-noise critical limit. These are conceptual antecedents, not evidence of historical uniqueness; a mathematically equivalent asymptotic calculation in other literature remains possible.

## Limitations

This is a deterministic infinite-population model with normalized truncated Gaussian perception. Global convergence assumes **all four initial phenotype frequencies are strictly positive** and \(n_0\in(0,1)\); it does not cover missing competing strategies on invariant simplex faces, fixed resource boundaries, or fluctuating finite populations. Strict payoff inequalities \(T>R\) and \(P>S\) are required for universal phenotype selection. The explicit initial-memory formula and quadratic crossover use the specified constant-gap payoff slice and initially independent phenotype coordinates; the general-payoff statement is the finite-noise equilibrium selection and leading eigenvalue only. The clock is a local relaxation exponent and a slow-time convergence limit, not an empirically calibrated recovery time. Uniform convergence of the stretched trajectory is asserted only away from \(\tau=0\). Independent validation has not been performed.

## References

[1] Arunava Patra, Joy Das Bairagya and Sagar Chakraborty, *Bayesian eco-evolutionary game dynamics*, Physical Review E **111**, 044401 (first online 2025-04-01), DOI: https://doi.org/10.1103/PhysRevE.111.044401; open preprint https://arxiv.org/abs/2504.02399 (first arXiv posting 2025-04-03), especially Eqs. (4), (7)–(9), Fig. 4 and Section III.C.

[2] Samrat Sohel Mondal and Sagar Chakraborty, *Noisy information channel mediated prevention of the tragedy of the commons*, https://arxiv.org/abs/2408.08744 (initial posting 2024-08-16).

[3] Joshua S. Weitz, Ceyhun Eksin, Keith Paarporn, Sam P. Brown and William C. Ratcliff, *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*, Proceedings of the National Academy of Sciences **113** (2016), E7518–E7525, DOI: https://doi.org/10.1073/pnas.1604096113.
