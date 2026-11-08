# An exact full-clustering atom for hard-saturated infinite-mean random graphs

## Finding

Fix \(0<\alpha<1\) and \(\lambda>0\). A critical rank-one random graph with Pareto vertex weights and capped edge probabilities has a random limit for its vertex-averaged local clustering, with a computable atom at perfect clustering. Let \(C_n\) denote the average over vertices of the usual proportion of adjacent neighbor pairs, interpreted as zero for degrees zero and one. Then

\[
C_n\ \xRightarrow[n\to\infty]{}\ Q(\Pi),\qquad
\Pr\{Q(\Pi)=1\}=1-e^{-\lambda}(1+\lambda),
\qquad \mathbb E Q(\Pi)=1-e^{-\lambda/(1-\alpha)}.
\]

More precisely, the proportion of vertices whose entire neighbor set is a clique tends to one in probability. This statement includes isolated and degree-one vertices as having a vacuously complete neighborhood; it does not assert that the graph itself is complete. The positive atom at the upper endpoint distinguishes hard saturation from the closely related exponential connection kernel.

## Assumptions and scope

For each integer \(n\ge2\), take independent random weights \(W_1,\ldots,W_n\) with
\[
\Pr(W_i>w)=w^{-\alpha}\quad(w\ge1),\qquad
\varepsilon_n=(\lambda/n)^{1/\alpha}.
\]
Conditional on all weights, distinct edges are independent with probabilities
\[
p_{ij}=\min\{\varepsilon_nW_iW_j,1\},\qquad i\ne j.
\]
This is the **capped**, not exponential, rank-one graph. Let \(D_i\) be the degree. For \(D_i\ge2\), define \(L_i\) as the number of edges joining two neighbors of vertex \(i\), divided by \(\binom{D_i}{2}\); put \(L_i=0\) otherwise, and \(C_n=n^{-1}\sum_iL_i\).

Let \(\Pi\) be a Poisson point process on \((0,\infty)\) with intensity \(\nu(dt)=\lambda\alpha t^{-1-\alpha}\,dt\). For each \(w\ge1\) define, conditionally on \(\Pi\), independent Bernoulli indicators \((B_t(w):t\in\Pi)\) with parameters \(\min\{wt,1\}\). The finite sum \(H_w=\sum_{t\in\Pi}B_t(w)\) is well defined almost surely, since \(\int\min\{wt,1\}\nu(dt)=\lambda w^\alpha/(1-\alpha)<\infty\). Define the measurable random variable
\[
Q(\Pi)=\int_1^\infty\alpha w^{-1-\alpha}
\Pr(H_w\ge2\mid\Pi)\,dw.
\]
The probability inside the integral is over Bernoulli indicators with \(\Pi\) fixed; those indicators need not be coupled across different \(w\).

## Proof

**1. Extreme-weight process and clique neighborhoods.** Put \(T_{n,j}=\varepsilon_nW_j\) and \(\Pi_n=\sum_j\delta_{T_{n,j}}\). The Pareto tail identity \(n\Pr(T_{n,j}>t)=\lambda t^{-\alpha}\) for fixed positive \(t\) and sufficiently large \(n\) proves convergence of \(\Pi_n\) to \(\Pi\) away from zero by multinomial-to-Poisson convergence, with independent disjoint-set counts. For fixed \(\delta>0\), let \(H_{n,\delta}=\{j:T_{n,j}\ge\delta\}\). Its cardinality is tight, and when \(\varepsilon_n<\delta^2\), any pair of vertices in \(H_{n,\delta}\) is connected with probability one, because
\[
\varepsilon_nW_iW_j=T_{n,i}T_{n,j}/\varepsilon_n\ge\delta^2/\varepsilon_n>1.
\]

For a uniformly selected root whose weight is bounded by \(M\), and for \(\delta M<1\), the conditional expected number of its adjacent vertices outside \(H_{n,\delta}\) is at most
\[
(n-1)\varepsilon_nM\,\mathbb E[W\mathbf1\{W<\delta/\varepsilon_n\}]
\le \frac{\lambda\alpha M}{1-\alpha}\delta^{1-\alpha}.
\]
Here the exact truncated Pareto first moment gives the inequality. Therefore the probability that a uniform root has any neighbor below cutoff is bounded, in the limit superior, by
\[
M^{-\alpha}+\frac{\lambda\alpha M}{1-\alpha}\delta^{1-\alpha}.
\]
First take \(\delta\downarrow0\) for fixed \(M\), then \(M\to\infty\). Exchangeability and Markov's inequality imply that the fraction of roots with any neighbor below cutoff vanishes in this iterated limit. Every remaining root has all its neighbors in the fully connected hub set; hence its neighborhood is a clique. The same estimate shows that using the degree truncated to neighbors in \(H_{n,\delta}\) instead of the full degree affects the indicator of degree at least two for only a vanishing fraction of vertices.

**2. Empirical degree-two indicator.** For fixed \(\delta>0\), discard the \(O_{\Pr}(1)\) vertices in \(H_{n,\delta}\). Conditional on the weights, the truncated degrees of all remaining vertices depend on disjoint edge sets and are independent. If \(g_\delta(w,\pi)\) denotes the probability that the sum of independent Bernoulli indicators with parameters \(\min\{wt,1\}\), over points \(t\ge\delta\) of \(\pi\), is at least two, conditional variance of their empirical average is at most \(1/n\). The ordinary weights conditional on the extremes are independent Pareto samples truncated below \(\delta/\varepsilon_n\). Their empirical averages against the bounded family \(g_\delta(\cdot,\Pi_n)\) approach the population average: condition on the finite extreme-weight list and use the bounded conditional variance, while the change from truncated to untruncated Pareto integration is bounded by \(O(1/n)\). Consequently,
\[
\frac1n\sum_{i=1}^n\mathbf1\{D_{i,\delta}\ge2\}
-\int_1^\infty\alpha w^{-1-\alpha}g_\delta(w,\Pi_n)\,dw
\xrightarrow{\Pr}0.
\]
On the space of finite point measures restricted to \([\delta,\infty)\), the integral functional is bounded and continuous at configurations with no point at \(\delta\); the limiting Poisson process satisfies this condition almost surely. Hence the integral converges in distribution to \(Q_\delta(\Pi)\), the corresponding functional using only points \(t\ge\delta\). The bound from step 1 controls the difference between full local clustering and truncated degree-two counts. Since \(Q_\delta(\Pi)\uparrow Q(\Pi)\) almost surely by monotone coupling as \(\delta\downarrow0\), the converging-together theorem yields \(C_n\Rightarrow Q(\Pi)\), as well as convergence to zero in probability of the fraction of non-clique neighborhoods.

**3. Exact mean.** Thinning the Poisson process at a fixed root weight \(w\) makes \(H_w\) Poisson with mean
\[
\mu(w)=\lambda\alpha\int_0^\infty\min\{wt,1\}t^{-1-\alpha}\,dt
=\frac{\lambda w^\alpha}{1-\alpha}.
\]
Writing \(c=\lambda/(1-\alpha)\), Tonelli's theorem and the substitution \(u=w^\alpha\), which gives the Pareto density \(u^{-2}\,du\), yield
\[
1-\mathbb E Q
=\int_1^\infty e^{-cu}(1+cu)u^{-2}\,du
=\left[-\frac{e^{-cu}}u\right]_{u=1}^{\infty}=e^{-c}.
\]

**4. The unit atom.** The number \(N=\Pi([1,\infty))\) is Poisson with mean \(\lambda\). If \(N\ge2\), at least two Bernoulli indicators in \(H_w\) are identically one for every \(w\ge1\). Thus \(Q=1\). Conversely, if \(N\le1\), then almost surely the second-largest Poisson point is strictly below one. Hence there exists \(\eta>0\) such that for every \(w\in[1,1+\eta]\), at most one Bernoulli parameter equals one. Moreover \(\sum_{t\in\Pi:t<1}t<\infty\) almost surely: its expectation is \(\lambda\alpha/(1-\alpha)\). On a possibly smaller interval, the infinite product of probabilities of failure for all remaining Bernoulli trials is strictly positive. Thus \(\Pr(H_w\le1\mid\Pi)>0\) on an interval of positive Pareto measure, implying \(Q<1\). Consequently
\[
\{Q=1\}=\{N\ge2\}\quad\text{almost surely},\qquad
\Pr(Q=1)=1-e^{-\lambda}(1+\lambda).
\]

**5. Comparison with a soft kernel.** For edges with probabilities \(1-e^{-\varepsilon_nW_iW_j}\), the same extreme-point and fixed-cutoff argument gives a limiting local clustering functional using Bernoulli parameters \(1-e^{-wt}\). For every finite \(w\), these parameters are strictly below one and their sum over \(\Pi\) is finite almost surely; consequently the probability of zero successes is strictly positive. The soft-kernel functional is therefore strictly below one almost surely. The positive unit atom is an exact, model-distinguishing consequence of **hard** saturation, not a general claim that heavy-tail clustering is new.

## Verification

The accompanying `verify_local_clustering.py` independently checks the truncated Pareto edge-probability identity, its asymptotic mean, the Poisson thinning integral, the exact Pareto mixture integral, the unit-atom Poisson calculation, and finite model-specific saturation identities using deterministic numerical calculations. Run with `python verify_local_clustering.py`; it uses the Python standard library only. These are finite diagnostics; the proofs of convergence and the atom characterization are the analytic arguments above.

## Relationship to prior work

Andreis, Avena, Hazra, and Matteini (2026) introduce the same capped Pareto graph at the critical scale and prove Poisson-environment limits for global component structure and degrees. Their abstract does not state a local-clustering theorem; the full manuscript was not available for complete comparison, which remains a priority risk. Avena, Garlaschelli, Hazra, and Lalli (2022/2025) study the related exponential connection kernel, emphasizing that global triangle behavior does not determine local clustering, but explicitly do not study local clustering. Catanzaro, van der Hofstad, and Garlaschelli (2026) **do** rigorously establish local clustering and lack of self-averaging for the exponential kernel; these qualitative effects and the basic low-degree clique mechanism are not claimed to be new here. The present exact probability of *perfect empirical clustering in the random limit* depends on deterministic saturation: the soft-kernel analogue has no such atom. Numerical similarity between the two models does not imply equality of their endpoint laws.

## Limitations

The theorem concerns the specific unbounded Pareto law, fixed \(0<\alpha<1\), fixed \(\lambda>0\), the critical scale and the vertex-averaged coefficient assigning zero below degree two. It does not determine the full density of \(Q\) on \([0,1)\), a convergence rate, or the global ratio of triangles to wedges. Averages taken only over degree-at-least-two vertices follow different normalization conventions. The 2026 capped-model primary paper was available at the abstract level but not for complete text comparison; an undiscovered broader theorem could cover the endpoint atom. The result has not undergone independent mathematical audit.

## References

1. L. Andreis, L. Avena, R. S. Hazra, and E. Matteini, *Inhomogeneous random graphs: how heavy tails reshape connectivity*, arXiv:2610.29564 (first public 2026-10-21), https://arxiv.org/abs/2610.29564.
2. A. Catanzaro, R. van der Hofstad, and D. Garlaschelli, *Clustering without geometry in sparse networks with independent edges*, arXiv:2603.13159 (first public 2026-03-13), https://arxiv.org/html/2603.13159v1.
3. L. Avena, D. Garlaschelli, R. S. Hazra, and M. Lalli, *Inhomogeneous random graphs with infinite-mean fitness variables*, arXiv:2212.08462 (2022), *Journal of Applied Probability* (online 2025), https://doi.org/10.1017/jpr.2025.10037.
