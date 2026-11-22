# An essential-singularity explosion clock at the resetting Zeno threshold

## Finding
For a geometrically accelerating continuous-time random walk whose internal state sometimes renews to zero, the presence or absence of a finite jump-accumulation time has a sharp power-law reset-hazard threshold. On the explosive side, the *mean* accumulation time grows by an essential singularity on approaching the threshold, and the appropriately normalized *random* accumulation time becomes exponentially distributed.

Precisely, for the model below, \(\zeta=\infty\) almost surely when \(0<\beta\le1\), while \(\zeta<\infty\) almost surely when \(\beta>1\). In the latter range,
\[
\mathbb E\zeta=\frac{\tau\sum_{k=0}^{\infty}r^k s_k(\beta)}{q_\beta},\qquad
s_k(\beta)=\prod_{j=1}^{k}(1-cj^{-\beta}),\quad
q_\beta=\prod_{j=1}^{\infty}(1-cj^{-\beta}),\quad s_0=1.
\]
For fixed \(0<c<1\) and \(0<r<1\), as \(\beta\downarrow1\) through values above one,
\[
\boxed{\mathbb E\zeta\sim \tau\Gamma(1-c)(1-r)^{c-1}\exp\!\left(\frac{c}{\beta-1}\right)}
\]
and, on the same approach to the threshold,
\[
\boxed{\frac{\zeta}{\mathbb E\zeta}\Longrightarrow \operatorname{Exp}(1).}
\]
These assertions form a single theorem on the critical accumulation clock.

## Assumptions and scope
Fix \(\tau>0\), \(0<r<1\), \(0<c<1\), and \(\beta>0\). The internal state begins at \(k=0\). Upon entering state \(k\ge0\), the walker waits an exponential time of mean \(\tau r^k\), independently of every earlier holding time and state-transition decision. At the end of that wait it makes one instantaneous jump; independently it resets its internal state to zero with probability \(p_k=c/(k+1)^\beta\), otherwise moving to \(k+1\). A reset from state zero is also counted as a departure and starts a fresh independent state-zero wait. The spatial displacement of the instantaneous jump may be sampled separately and is not used in the theorem. The accumulation time \(\zeta\) is the limit of the increasing sequence of departure times, allowing \(+\infty\); no state-space completion of the post-accumulation walk is assumed. An *excursion* is the sequence of waits from one fresh state-zero entry to the next reset, or to infinite state growth with no reset.

## Proof
**1. Renewal decomposition and the exact expectation.** The probability that a fresh excursion reaches state \(k\) is \(s_k(\beta)\). The probability it never resets is
\[
q_\beta=\prod_{j=1}^{\infty}(1-cj^{-\beta}).
\]
The number of reset-ending excursions before the first never-resetting excursion is geometric with success probability \(q_\beta\), whenever \(q_\beta>0\). Let \(L\) be the duration of one excursion, including the infinite but summable sequence of holding times if there is no reset. Since the expected wait at state \(k\) is \(\tau r^k\), Tonelli's theorem gives
\[
B_\beta:=\mathbb E L=\tau\sum_{k=0}^{\infty}r^k s_k(\beta),\qquad 0<B_\beta\le\frac{\tau}{1-r}.
\]
The regenerative identity \(\mathbb E\zeta=B_\beta+(1-q_\beta)\mathbb E\zeta\), justified first by summing the independent episode costs for a geometric number of episodes, gives \(\mathbb E\zeta=B_\beta/q_\beta\) when \(q_\beta>0\).

**2. Almost-sure explosion dichotomy.** The infinite product \(q_\beta\) is positive exactly when \(\sum_{j\ge1} cj^{-\beta}<\infty\), namely \(\beta>1\); the factors lie strictly between zero and one, so the standard infinite-product criterion applies. If \(\beta>1\), eventually a never-resetting excursion occurs almost surely. Its total waiting time is finite almost surely because it is a sum of independent positive random variables with expectation \(\tau/(1-r)<\infty\). The finitely many preceding reset excursions also have finite durations, so \(\zeta<\infty\) almost surely. If \(\beta\le1\), every excursion eventually resets almost surely and there are infinitely many such excursions. Each begins with a fresh independent state-zero exponential holding time of mean \(\tau\). Their sum diverges almost surely by the strong law, forcing \(\zeta=\infty\) almost surely. This also rules out uncounted accumulation through repeated resets.

**3. Sharp essential singularity.** For \(\beta>1\), the absolutely convergent expansion of the logarithmic product is
\[
\log q_\beta=-\sum_{m=1}^{\infty}\frac{c^m}{m}\,\zeta_{\mathrm R}(m\beta),
\]
where \(\zeta_{\mathrm R}\) is the Riemann zeta function. As \(\beta\downarrow1\), \(\zeta_{\mathrm R}(\beta)=(\beta-1)^{-1}+\gamma+o(1)\); the subseries with \(m\ge2\) converges uniformly by \(0<c<1\). Hence
\[
\lim_{\beta\downarrow1}\bigl(\log q_\beta+c/(\beta-1)\bigr)
=-c\gamma-\sum_{m=2}^{\infty}\frac{c^m\zeta_{\mathrm R}(m)}m
=-\log\Gamma(1-c).
\]
The last equality is the convergent Weierstrass series for \(\log\Gamma(1-c)\). Independently, dominated convergence gives
\[
\lim_{\beta\downarrow1}B_\beta
=\tau\sum_{k=0}^{\infty}r^k\prod_{j=1}^k(1-c/j)
=\tau\sum_{k=0}^{\infty}\frac{(1-c)_k}{k!}r^k
=\tau(1-r)^{c-1},
\]
by the generalized binomial theorem. Combining the numerator and product limits proves the exact amplitude and exponential factor claimed.

**4. Exponential limiting clock.** Every excursion duration \(L\) can be coupled below \(S=\sum_{k\ge0}E_k\), where the independent \(E_k\) are exponential with means \(\tau r^k\); thus \(\sup_{\beta>1}\mathbb E L^2\le\mathbb E S^2<\infty\). More particularly, on the successful never-resetting event, \(L=S\), and the holding times are independent of transition choices, so \(\mathbb E[L\mid\text{success}]=\tau/(1-r)\). Set \(q=q_\beta\), \(B=B_\beta\), and \(s=tq/B\), with fixed \(t\ge0\). The renewal equation for the Laplace transform is
\[
\mathbb E e^{-s\zeta}
=\frac{\mathbb E[e^{-sL};\text{success}]}{1-\mathbb E[e^{-sL};\text{reset}]}.
\]
As \(\beta\downarrow1\), \(q\to0\) and \(B\to\tau(1-r)^{c-1}>0\). The numerator equals \(q(1+O(s))\) by the uniform conditional mean on success. By the second-moment bound, the denominator equals
\[
q+s\,\mathbb E[L;\text{reset}]+O(s^2),\qquad
\mathbb E[L;\text{reset}]=B-q\frac{\tau}{1-r}.
\]
It follows that the transform tends to \((1+t)^{-1}\). This is the Laplace transform of \(\operatorname{Exp}(1)\), establishing the distributional limit for \(q\zeta/B=\zeta/\mathbb E\zeta\).

## Verification
The accompanying `verification/check.py` uses the Python standard library only. It checks 208 exact rational identities between (i) the finite-depth first-step equations and (ii) the independent survival-product expression for the expected time to reach a forced terminal depth; it also verifies the critical generalized-binomial series and numerical convergence toward the derived asymptotic amplitude. With \(c=0.4\), \(r=0.55\), \(\tau=1\), the predicted limiting amplitude is approximately \(2.404491569992\). At \(\beta=1.02\), the numerically calculated expectation divided by the asserted leading asymptotic is approximately \(0.998567482\). The checker is a consistency test, not a computational proof of an infinite product, limit, or weak convergence; these follow from the analytic argument above.

## Relationship to prior work
Huang's 2026 internal-renewal CTRW manuscript introduces state-dependent renewal probabilities and geometrically decreasing exponential holding times. Its Zeno section describes the finite-time supertask when resets are suppressed, and its feedback section studies other holding-time and reset choices. The present theorem instead locates the exact almost-sure accumulation threshold for slowly decaying internal reset hazards and computes the sharp activated mean clock and its exponential rare-success law. Montero and Villarroel's Sisyphus walk allows state-dependent restarts in discrete time but does not use geometrically shrinking holding times or give this accumulation-time asymptotic. General external resetting CTRW treatments assume independent renewal reset clocks, not the state-dependent hazard considered here. Classical catastrophe-process analyses address extinction with a different reset kernel, not the present explosion clock. These are implication comparisons rather than evidence of an exhaustive novelty guarantee.

## Limitations
The theorem fixes the geometrically decaying mean holding times and the exact hazard \(p_k=c/(k+1)^\beta\) with \(0<c<1\). It does not claim a spatial position limit at the explosion time, a continuation of the process after accumulation, or uniformity when \(r\) or \(c\) varies with \(\beta\). Generic regenerative rare-success theory explains why an exponential clock limit is plausible; the stated explicit singular amplitude and model-specific threshold require the proof above. Independent external assessment of literature priority has not been performed.

## References
1. B. Z. Huang, *Continuous-Time Random Walks with Internal Stochastic Renewal Process*, arXiv:2611.16383v1 (November 12, 2026). https://arxiv.org/html/2611.16383v1
2. M. Montero and J. Villarroel, *Sisyphus random walk*, arXiv:1603.09239v2 (2016). https://arxiv.org/pdf/1603.09239
3. F. Colantoni and G. Pagnini, *Master equations for continuous-time random walks with stochastic resetting*, arXiv:2507.07590v1 (2025). https://arxiv.org/html/2507.07590
4. B. Cairns and P. K. Pollett, *Extinction times for a general birth, death and catastrophe process*, J. Appl. Prob. 41 (2004), 1211–1218. https://people.smp.uq.edu.au/PhilipPollett/papers/bdc/bdc.pdf
