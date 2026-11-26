# A sharp extreme-opinion tail law for two-source media selection

## Finding
Consider the finite-population two-source opinion-update model of Zheng and Porter in its **media-only regime**: each ordinary agent has an opinion in \([-M,M]\), the two fixed media opinions are \(\pm M\), and every active update chooses the positive media opinion with probability
\[
 p_+(x)=\frac{1}{1+\exp(-\beta x)},\qquad p_-(x)=1-p_+(x),
\]
then replaces the selected opinion by \((x+M)/2\) or \((x-M)/2\), respectively. Let \(M\in(0,1]\), \(\beta\ge0\), and let the population contain any finite number \(N\ge2\) of ordinary agents, selected for updates independently of their states with strictly positive selection frequencies. There are no ordinary-agent pair updates (the paper's media probability is \(p_M=1\)).

The finite-population chain has stationary probabilities, and **every stationary marginal law** \(\nu\) of every ordinary agent satisfies:

1. If \(\beta>0\), \(\nu\) has full support \([-M,M]\), has no atoms, and is singular with respect to Lebesgue measure.
2. Set \(q=(1+e^{-\beta M})^{-1}\). There are finite positive constants \(A_+(\nu),A_-(\nu)\) such that, as integers \(m\to\infty\),
\[
\begin{aligned}
 \nu([M-2M2^{-m},M])&=A_+(\nu)q^m(1+O(2^{-m})),\\
 \nu([-M,-M+2M2^{-m}])&=A_-(\nu)q^m(1+O(2^{-m})).
\end{aligned}
\]
Consequently, the two endpoint local dimensions both exist and equal the **sharp extremism-tail exponent**
\[
 \gamma(\beta M)=\lim_{h\downarrow0}\frac{\log\nu([M-h,M])}{\log h}
 =\lim_{h\downarrow0}\frac{\log\nu([-M,-M+h])}{\log h}
 =\frac{\log(1+e^{-\beta M})}{\log2}\in(0,1).
\]
The exponent strictly decreases with \(\beta M\), so every positive amount of alignment bias changes the endpoint scaling from the linear, unbiased rate to a heavier power law. If \(\beta=0\), every stationary marginal is uniform on \([-M,M]\) and \(\gamma=1\).

The theorem concerns stationary *marginals*. It does not assert an explicit invariant joint law, an attraction rate, or persistence of the same singular law when ordinary-agent pair updates occur.

## Assumptions and scope
The two media sources are fixed at \(\pm M\). Media are accessible regardless of the ordinary-agent confidence bound, and interaction intensity is always one half, as in the cited model. The regime \(p_M=1\) excludes peer-to-peer compromise; an agent's active update is exactly the state-dependent two-branch kernel displayed above. The number of ordinary agents is any fixed integer \(N\ge2\); their selection rule does not depend on opinions, and each has nonzero selection probability. If one initially allows opinions outside \([-M,M]\), the theorem is only asserted for stationary probabilities supported inside the natural invariant interval, not for arbitrary nonstationary transients. Stationarity is with respect to the stochastic finite-population chain, not the deterministic mean-field approximation.

For an individual ordinary agent, define \(F_\pm(x)=(x\pm M)/2\) on \([-M,M]\). The active-update Markov operator on Borel probabilities is
\[
 P\nu=(F_+)_*(p_+\nu)+(F_-)_*(p_-\nu).
\]
Every stationary marginal obeys \(P\nu=\nu\), since the positive, state-independent probability of selecting that agent cancels its holding probability. Conversely, at least one stationary law exists, by compactness and continuity of the finite-population transition kernel.

## Proof
**Full support and atomlessness.** For finite \(\beta\), there is a uniform \(q_0>0\) such that both choice probabilities lie between \(q_0\) and \(1-q_0\) at every opinion. Any finite sequence of chosen signs maps the complete interval into a prescribed dyadic interval of length \(2M2^{-m}\). Every nonempty open interval contains such a dyadic cell; from every starting opinion its sign sequence occurs with probability at least \(q_0^m\). Stationarity therefore gives positive mass to every nonempty relative open interval. A point has at most two binary sign codings. Its mass is bounded by \(2(1-q_0)^m\) for all \(m\), hence is zero.

**Singularity for positive bias.** Apart from the endpoint-identification point (which has zero stationary mass), the piecewise expanding map
\[
 T(y)=\begin{cases}2y-M,&y>0,\\2y+M,&y<0\end{cases}
\]
satisfies \(T(F_+(x))=T(F_-(x))=x\), almost surely under a stationary law. Hence \(T_*\nu=\nu\). Rescaling \([-M,M]\) to the unit circle conjugates \(T\) to doubling modulo one. The only absolutely continuous doubling-invariant probability is normalized Lebesgue measure \(\lambda\): for every nonzero integer Fourier mode \(k\), invariance gives \(\widehat\mu(k)=\widehat\mu(2^jk)\), which tends to zero for an absolutely continuous measure by the Riemann–Lebesgue lemma.

Both \(T_*\) and \(P\) send absolutely continuous measures to absolutely continuous measures and singular measures to singular measures: their branches are nondegenerate affine maps, with bounded nonnegative weights for \(P\). Uniqueness of the Lebesgue decomposition then implies that the absolutely continuous component of \(\nu\), if it has mass \(a>0\), equals \(a\lambda\) and must itself be \(P\)-stationary. But on the positive half-interval, \(P\lambda\) has density \(p_+(2y-M)/M\), whereas \(\lambda\) has constant density \(1/(2M)\). They agree only when \(p_+\equiv1/2\), equivalent to \(\beta=0\). Thus \(a=0\) when \(\beta>0\). Along with non-atomicity and full support, this proves singular continuity with complete interval support.

**Exact endpoint asymptotics.** The rightmost dyadic interval \([M-2M2^{-m},M]\) records precisely \(m\) consecutive positive-media choices, up to the already-excluded dyadic endpoints. Its stationary probability is therefore
\[
 \int_{-M}^M\prod_{j=0}^{m-1}p_+(F_+^j(x))\,\nu(dx).
\]
Let \(q=p_+(M)\). Since \(F_+^j(x)=M-(M-x)2^{-j}\) and \(\log p_+(x)\) has derivative bounded in absolute value by \(\beta\),
\[
 \sum_{j=0}^\infty\left|\log\frac{p_+(F_+^j(x))}{q}\right|\le 4\beta M
\]
uniformly in \(x\in[-M,M]\). The infinite product
\[
 R_+(x)=\prod_{j=0}^\infty \frac{p_+(F_+^j(x))}{q}
\]
therefore converges uniformly to a strictly positive bounded continuous function, and its truncation has relative error \(1+O(2^{-m})\). Integration gives the stated formula with \(A_+(\nu)=\int R_+\,d\nu\in(0,\infty)\). Reflecting signs gives the left formula with \(A_-(\nu)=\int\prod_{j\ge0}(p_-(F_-^j(x))/q)\,d\nu\). The dyadic estimates sandwich arbitrary small endpoint intervals between two consecutive dyadic lengths, establishing the claimed logarithmic limits. Because \(q=(1+e^{-\beta M})^{-1}\), the common exponent is precisely \(-\log q/\log2\).

**Unbiased baseline.** At \(\beta=0\) every media sign is an independent fair sign at each active update. After \(m\) such updates, the first \(m\) binary digits of the scaled opinion are fair and its remaining dependence on the starting state is at most \(2^{-m}\). Thus the active-update law tends weakly to uniform measure; in particular every stationary marginal must be uniform. Its endpoint interval mass is \(h/(2M)\).

## Verification
The accompanying standalone `verify.py`, executable with `python verify.py`, checks all dyadic branch cell lengths exactly using rational arithmetic, the exact right-endpoint branch boundary, normalization at \(\beta=0\), and the uniform finite-product error bound at several positive parameter values. It prints `VERIFY_OK 2984 finite branch/product checks`. The infinite-product convergence, Lebesgue-decomposition argument, singularity and all-size conclusions are analytic proofs; the finite checker is not an infinite certificate.

## Relationship to prior work
Zheng and Porter (arXiv:2606.28318v1, Section 3) introduce this precise logistic two-media sampling mechanism and fixed half-compromise. Their Section 6 studies deterministic drift of a dominant cluster, notably a threshold in \(M\) when \(\beta=5\), rather than the stochastic stationary tail law in the all-media finite-population specialization considered here. The present law supplies a quantitative extreme-opinion observable even when the deterministic cluster analysis predicts no drift.

Cao and Cortez (arXiv:2408.01624v1, Sections 1 and 4) analyze interacting random-persuasion opinions and find the uniform Bernoulli-convolution law at a half-step when sign selection is independent of an agent's own opinion. Their stationary mean-field sign mechanism differs from the logistic own-opinion sampling here; the singular full-support outcome and exact logistic endpoint exponent are not consequences of their fair-sign half-step result.

The earlier published result *Full-support singular opinions at a critical random-action learning rate* (published-finding corpus, 2026) proves a singular full-support law for a distinct endogenous **affine** Bernoulli decision rule in a random-action opinion model. That result is a close structural precedent for the singular-continuity phenomenon, which is therefore not claimed as a new general IFS principle. It does not give the present logistic branch-selection law or the explicit exact endpoint scaling exponent and prefactors.

Jaroszewska and Rams (arXiv:0707.3532v2) prove a general Hausdorff-dimension upper bound for place-dependent iterated function systems, which does not identify the exact endpoint local dimensions or these logistic-tail constants. Classical Fourier rigidity for doubling and contracting-branch arguments are used as established mathematical ingredients, not claimed as new general theorems.

## Limitations
The all-media regime \(p_M=1\) is a boundary case of the finite-population model; interaction between ordinary agents is excluded. The result describes stationary marginals but does not prove uniqueness, mixing rates, finite-population metastable transitions, or empirical opinion distributions. Constants \(A_\pm(\nu)\) are positive integrals, not closed elementary numbers. The exponent is sharp at the two media endpoints only and is not the Hausdorff dimension of the whole measure. Standard probability and Fourier analysis are used in the proof. Whether an exact equivalent of the *specific logistic endpoint law* occurs in overlooked earlier publications remains a historical-priority risk. No independent validation is claimed.

## References
- O. Zheng and M. A. Porter, *Drift Behavior in a Bounded-Confidence Opinion Model with Media Influence*, arXiv:2606.28318v1, first public 2026-06-26. https://arxiv.org/html/2606.28318
- F. Cao and R. Cortez, *Fractal opinions among interacting agents*, arXiv:2408.01624v1, first public 2024-08-03. https://arxiv.org/html/2408.01624v1
- J. Jaroszewska and M. Rams, *On the Hausdorff dimension of invariant measures of weakly contracting on average measurable IFS*, arXiv:0707.3532v2 (first version 2007). https://arxiv.org/html/0707.3532v2
- *Full-support singular opinions at a critical random-action learning rate*, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-full-support-singular-opinions-at-a-critical-random-action-learn--cfba8772283c
