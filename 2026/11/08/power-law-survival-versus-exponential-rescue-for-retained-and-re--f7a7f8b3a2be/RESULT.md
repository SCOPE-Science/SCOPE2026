# Power-law survival versus exponential rescue for retained and refreshed surface-reaction thresholds

## Finding

A reflecting diffusion with Poisson position resets retains an algebraic reaction-time tail whenever its single, conserved surface-contact threshold has a regularly varying tail. Refreshing **both** contact progress and an independently drawn threshold at each reset instead yields an exponential tail, even when the conserved-threshold mean reaction time is infinite. Specifically, for the normalization and assumptions below,

\[
\Pr(T_{\mathrm{keep}}>t)\sim\Psi(Jt),\qquad
J=\sqrt{Dr}\exp(-R\sqrt{r/D}).
\]

For the Lomax survival \(\Psi(\ell)=(1+\ell/\ell_0)^{-\alpha}\), with \(\ell_0>0\) and \(\alpha>0\),

\[
\Pr(T_{\mathrm{keep}}>t)\sim\left(\frac{\ell_0}{Jt}\right)^\alpha,
\qquad
\mathbb E T_{\mathrm{keep}}<\infty\ \Longleftrightarrow\ \alpha>1.
\]

This is a joint statement contrasting two precisely specified contact-state reset protocols; it is **not** a new inverse-local-time transform or a new derivation of the known contact-production-rate optimizer.

## Assumptions and scope

Let \(D,r,R>0\). Between reset times of a rate-\(r\) Poisson process, \(X_t\) is reflected Brownian motion on \([0,\infty)\) with generator \(D\partial_{xx}\). Its initial and every post-reset position are \(R\). Reflection is instantaneous, and the boundary-contact local time has the occupation normalization

\[
L_t=\lim_{\varepsilon\downarrow0}\frac D\varepsilon
\int_0^t\mathbf 1_{[0,\varepsilon]}(X_s)\,ds.
\]

At a position reset the accumulated \(L_t\) is retained, and only the position is replaced. Let \(\Lambda>0\) a.s. be independent of the motion and reset clock, with a continuous distribution and survival function \(\Psi(\ell)=\Pr(\Lambda>\ell)\). Assume \(\Psi\) is ultimately positive and regularly varying with index \(-\alpha\), \(\alpha>0\); that is, \(\Psi(cy)/\Psi(y)\to c^{-\alpha}\) for every \(c>0\). Put \(T_{\mathrm{keep}}=\inf\{t>0:L_t>\Lambda\}\).

For comparison, \(T_{\mathrm{fresh}}\) starts from the same initial position and a fresh copy of \(\Lambda\), but **at each reset** discards both accumulated local time and the previous threshold, and samples a *new independent* \(\Lambda\). This fresh-redraw rule is essential: resetting progress without redrawing a quenched heavy-tailed threshold is a different process and is not covered by the exponential-tail assertion.

## Proof

**Step 1: a light-tailed reward for one complete position-reset cycle.** Put \(k=\sqrt{r/D}\), \(a=e^{-Rk}\), and let \(E\) be an independent \(\mathrm{Exp}(r)\) cycle duration. Starting each cycle at \(R\), write \(Y\) for the local-time increase during the entire cycle. Without resetting, the inverse first-contact time at boundary local time \(\ell>0\) has the Brownian hitting-time Laplace transform

\[
\mathbb E_R e^{-s\tau_\ell^{(0)}}
=\exp[-(R+\ell)\sqrt{s/D}],\qquad s>0.
\]

This follows by the strong Markov property at the first boundary hit and the reflection-principle transform for the inverse regulator. Consequently,

\[
\Pr(Y>\ell)=\Pr(\tau_\ell^{(0)}<E)
=e^{-k(R+\ell)}=a e^{-k\ell},\quad \ell>0.
\]

Thus \(Y\) has a point mass \(1-a\) at zero and, conditional on being positive, is exponential with rate \(k\). In particular, \(\mathbb EY=a/k\), and \(\mathbb Ee^{\theta Y}=1-a+ak/(k-\theta)<\infty\) whenever \(\theta<k\). Distinct complete cycles have i.i.d. rewards (although within each cycle the duration and its reward need not be independent). Their expected rate of local-time production is

\[
J=r\mathbb EY=\frac{ra}{k}=\sqrt{Dr}\,e^{-R\sqrt{r/D}}.
\]

**Step 2: exponential concentration in physical time.** Let \(N_t\) count the Poisson resets before time \(t\), and let \(Y_i\) be the full rewards of cycles sampled indefinitely. Then \(N_t\sim\mathrm{Poisson}(rt)\). On \(N_t\ge m_-:=\lfloor(r-\varepsilon)t\rfloor\), positivity gives \(L_t\ge\sum_{i=1}^{m_-}Y_i\). On \(N_t\le m_+:=\lceil(r+\varepsilon)t\rceil\), the partial final cycle is bounded by the full reward of that cycle, so

\[
L_t\le\sum_{i=1}^{m_+}Y_i
+\max_{1\le i\le m_++1}Y_i.
\]

For each \(\delta\in(0,J)\), choose \(\varepsilon\in(0,r)\) small enough that \((r\pm\varepsilon)\mathbb EY\) lie strictly inside \((J-\delta/2,J+\delta/2)\). Poisson Chernoff bounds, i.i.d. Cramér bounds (the displayed moment generating function), and \(\Pr(\max_{i\le m_++1}Y_i>\delta t/2)\le(m_++1)a e^{-k\delta t/2}\) imply constants \(C_\delta,c_\delta>0\) such that

\[
\Pr(|L_t/t-J|>\delta)\le C_\delta e^{-c_\delta t}
\]

for all sufficiently large \(t\). This argument does not assume independence between cycle rewards and cycle durations.

**Step 3: survival tail.** Conditioning on \(L_t\) and the independent continuous threshold gives \(\Pr(T_{\mathrm{keep}}>t)=\mathbb E\Psi(L_t)\). Since \(\Psi\) is decreasing, the concentration bound implies, for \(0<\delta<J\),

\[
(1-Ce^{-ct})\Psi((J+\delta)t)
\le\Pr(T_{\mathrm{keep}}>t)
\le\Psi((J-\delta)t)+Ce^{-ct}.
\]

Regular variation makes the exponential error negligible compared with \(\Psi(Jt)\), and the ratios of the outer terms converge to \(((J\pm\delta)/J)^{-\alpha}\). Sending \(\delta\downarrow0\) proves \(\Pr(T_{\mathrm{keep}}>t)\sim\Psi(Jt)\). For Lomax thresholds, this yields the stated prefactor and the sharp finite-mean criterion by integrating the survival function. More generally, when \(\alpha=1\) the mean criterion can depend on the slowly varying factor; no universal assertion is made for that borderline beyond the Lomax family.

**Step 4: the fresh-redraw protocol.** For one attempt without resetting, let \(T_0\) denote the time until the boundary local time exceeds an independently drawn threshold. The inverse-local-time hitting transform implies

\[
f(s):=\mathbb E e^{-sT_0}
=e^{-R\sqrt{s/D}}\,\mathbb E e^{-\Lambda\sqrt{s/D}}
\quad(s>0).
\]

With independent Poisson restart at rate \(r\), each attempt succeeds before its reset with probability \(p=f(r)>0\) because \(\Lambda\) is finite a.s. The renewal identity gives

\[
\mathbb ET_{\mathrm{fresh}}
=\frac{1-p}{rp}
=\frac1r\left[\frac{e^{R\sqrt{r/D}}}
{\mathbb E(e^{-\Lambda\sqrt{r/D}})}-1\right]<\infty.
\]

For \(s\ge0\), its Laplace transform is

\[
\mathbb E e^{-sT_{\mathrm{fresh}}}
=\frac{f(r+s)}{1-\frac r{r+s}[1-f(r+s)]}.
\]

The denominator equals \(p>0\) at \(s=0\) and is continuous near zero for \(s>-r\). Choosing a sufficiently small \(\eta>0\) permits the same renewal expression at \(s=-\eta\), via the positive geometric series of failed attempts. Hence \(\mathbb E e^{\eta T_{\mathrm{fresh}}}<\infty\) and \(\Pr(T_{\mathrm{fresh}}>t)\le C e^{-\eta t}\).

**Step 5: an optimal tail prefactor (known production-rate consequence).** For Lomax \(\Psi(Jt)\sim(\ell_0/Jt)^\alpha\). The derivative of \(\log J(r)=\frac12\log(Dr)-R\sqrt{r/D}\) vanishes uniquely at \(r=D/R^2\), with positive derivative below and negative derivative above. This observation is included as a corollary, not claimed as a new optimization theorem.

## Verification

The standalone `CHECK.py` uses independent Gaussian/reflection-principle integrals to verify \(\Pr(Y>\ell)=e^{-k(R+\ell)}\) for several positive local-time levels, the exponential-mixture moment-generating function, the reward rate \(J\), fresh-cycle geometric mean identities for several Lomax shapes, the strict production-rate optimum, and the regularly varying Lomax ratios. Execute `python CHECK.py` with Python 3 and SciPy. These are finite checks of key algebra and constants; the infinite-time survival and exponential-tail claims rely on the complete proof above, not on numerical extrapolation.

## Relationship to prior work

Bressloff (2022a, arXiv:2202.01119v1) develops contact-local-time propagators under position-only resetting and examines Pareto-II surface thresholds in the **complete state-renewal** setting; its nonrenewal position-only analysis does not state the regular-variation survival equivalence above. Bressloff (2022b, arXiv:2203.04868v1, section 3) obtains the **deterministic-threshold** mean reaction time for retained local time, which is not claimed as new here. Bressloff (2023, arXiv:2303.10483v1) derives heavy-tail reaction asymptotics for **fractional subdiffusion in a bounded interval without Poisson position resetting**, a different mechanism. The novelty assessed here is the sharp random-threshold survival constant for *retained* contact history and its contrast with *fresh independently redrawn* thresholds. Known inverse-local-time and renewal formulas are used as background, not attributed as new discoveries.

## Limitations

The result concerns one-dimensional normal diffusion on a reflecting half-line, fixed positive reset rate and location, and a single independent threshold with regular variation. The fresh protocol explicitly redraws the threshold: retaining a quenched threshold while resetting only its progress is not addressed. The argument does not establish sharp exponential decay exponents in the fresh case, nor finite-size spatial geometries, imperfect reflecting dynamics, correlations among thresholds, or the \(r\downarrow0\) joint scaling limit. The \(\alpha=1\) finite-mean statement applies to the Lomax family, not every slowly varying correction. General renewal-reward and regular-variation theory may make portions of the argument implicit in prior work; a publication-level priority review remains advisable.

## References

1. P. C. Bressloff, *Diffusion-mediated surface reactions and stochastic resetting*, arXiv:2202.01119v1 (first public 2022-02-02). https://arxiv.org/abs/2202.01119
2. P. C. Bressloff, *Threshold surface reactions and local time resetting*, arXiv:2203.04868v1 (first public 2022-03-09). https://arxiv.org/abs/2203.04868
3. P. C. Bressloff, *Encounter-based reaction-subdiffusion model I: surface adsorption and the local time propagator*, arXiv:2303.10483v1 (first public 2023-03-18). https://arxiv.org/abs/2303.10483
4. A. S. Bodrova and I. M. Sokolov, *Continuous-time random walks under power-law resetting*, Phys. Rev. E 101, 062117 (2020). https://doi.org/10.1103/PhysRevE.101.062117
