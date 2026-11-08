# Block-shared diffusivity creates a sharp first-arrival moment phase diagram

## Finding

For every distance \(a>0\), heterogeneity exponent \(\alpha>0\), and positive integers \(m,k\), group \(N=mk\) independent Brownian search trajectories into \(m\) blocks of \(k\) particles. All particles begin at \(a\) on the positive half-line and are killed upon first reaching zero. Each block has one independent, time-frozen diffusion coefficient \(D_g\), shared by its \(k\) members, distributed with density \(\alpha d^{\alpha-1}\) on \((0,1)\). Brownian noises are mutually independent conditional on all coefficients. Each trajectory has generator \(D_g\partial_{xx}\). Let \(T_{m,k}\) be the first target-arrival time among all \(mk\) particles.

Set \(c=a/\sqrt\pi\), \(s(u)=\operatorname{erf}(a/(2\sqrt u))\) for \(u>0\), and let \(H_k\) be the minimum of \(k\) independent first-arrival times with generator \(\partial_{xx}\). The *exact finite-time survival law* is

\[
\Pr(T_{m,k}>t)=\left[\alpha t^{-\alpha}\int_0^t u^{\alpha-1}s(u)^k\,du\right]^m,\qquad t>0.
\]

The block factor in square brackets has the following *sharp, positive-constant asymptotics* as \(t\to\infty\):

\[
R_{\alpha,k}(t)\sim
\begin{cases}
\mathbb E[H_k^\alpha]t^{-\alpha},&0<\alpha<k/2,\\
\alpha c^k t^{-k/2}\log t,&\alpha=k/2,\\
\dfrac{\alpha c^k}{\alpha-k/2}t^{-k/2},&\alpha>k/2.
\end{cases}
\]

Here \(\mathbb E[H_k^\alpha]=\alpha\int_0^\infty u^{\alpha-1}s(u)^k\,du\) is finite and strictly positive in the first case. In particular, for *every* \(q>0\),

\[
\boxed{\mathbb E[T_{m,k}^q]<\infty\quad\Longleftrightarrow\quad q<m\min\{\alpha,k/2\}.}
\]

At equality the moment diverges; the marginal case \(\alpha=k/2\) additionally has an \((\log t)^m\) tail factor.

For an arbitrary positive nondegenerate coefficient distribution in place of the specified Beta law, and any fixed total \(N\), the fastest-arrival time is **strictly stochastically slower as the equal block size increases among divisors of \(N\)**: if \(k_1<k_2\) both divide \(N\), then

\[
\Pr(T_{N/k_1,k_1}>t)<\Pr(T_{N/k_2,k_2}>t)\quad\text{for every }t>0.
\]

For example, with \(N=6\) and \(\alpha=2/5\), block sizes \(k=1,2,3,6\) give respective survival power exponents \(12/5,6/5,4/5,2/5\). Consequently, the mean fastest-arrival time is finite for \(k=1,2\), yet infinite for \(k=3,6\), **despite the same six particles and identical single-particle marginal law**.

## Assumptions and scope

The spatial domain is \((0,\infty)\) with absorbing target \(0\); all trajectories start at the same strictly positive \(a\). Brownian motions and random diffusion coefficients are independent across distinct blocks, while the coefficient is perfectly shared within each block. Each coefficient is sampled once and never refreshed. There is no resetting, drift, finite domain, direct interaction, or common Brownian driving noise. All parameters \(a,\alpha,m,k\) are fixed in the long-time asymptotics. The stochastic ordering compares different block partitions using the same total population and the same one-particle diffusion coefficient law. The coefficient distribution has no atom at zero.

## Proof

**1. Exact single-particle formula.** For generator \(D\partial_{xx}\), reflection at the absorbing boundary or the Brownian hitting-time identity gives
\(\Pr(H_D>t)=\operatorname{erf}(a/(2\sqrt{Dt}))\). For \(D=1\), this is \(s(t)\), and the pathwise scaling representation is \(H_D\overset d=H_1/D\). In particular, since \(\operatorname{erf}(x)=2x/\sqrt\pi+O(x^3)\) as \(x\to0\),

\[
s(u)=c\,u^{-1/2}(1+O(u^{-1})),\qquad u\to\infty.
\]

**2. Shared-block survival.** Given block diffusivity \(D=d\), independent noises imply the probability that all \(k\) block members survive through \(t\) is \(s(dt)^k\). Average over the density \(\alpha d^{\alpha-1}\) and substitute \(u=dt\) to get the one-block survival
\[
R_{\alpha,k}(t)=\int_0^1 \alpha d^{\alpha-1}s(dt)^k\,dd=\alpha t^{-\alpha}\int_0^t u^{\alpha-1}s(u)^k\,du.
\]
Independence between blocks yields the stated \(m\)-th power. This is an exact equality, not an approximation based on mean diffusivity.

**3. The three regimes.** As \(u\to\infty\), the integrand in the last integral is asymptotic to \(\alpha c^k u^{\alpha-1-k/2}\). It is integrable at zero because \(s(u)\le1\) and \(\alpha>0\). If \(\alpha<k/2\), it is integrable at infinity; monotone convergence shows the integral tends to \(\mathbb E H_k^\alpha\), by the layer-cake moment identity and \(\Pr(H_k>u)=s(u)^k\). If \(\alpha=k/2\), the integral is \(\alpha c^k\log t+O(1)\), since the asymptotic correction has integrable order \(u^{-2}\). If \(\alpha>k/2\), elementary asymptotic integration yields \(\alpha c^k t^{\alpha-k/2}/(\alpha-k/2)\,(1+o(1))\). This proves every displayed constant, including critical logarithms and the endpoint \(\alpha=k/2\).

**4. Moment boundary.** For \(q>0\), \(\mathbb E[T_{m,k}^q]=q\int_0^\infty t^{q-1}\Pr(T_{m,k}>t)\,dt\). The integral over \((0,1]\) is bounded. The previously proved positive-constant tail and the integral test show finiteness exactly for \(q<m\min\{\alpha,k/2\}\); at equality the integral diverges, with a logarithmic enhancement at the critical single-block exponent.

**5. Stochastic ordering at fixed population.** For any nonconstant positive random diffusivity \(D\), let \(Z_t=s(Dt)\), so \(0<Z_t<1\), and \(Z_t\) is nonconstant for each \(t>0\) because \(s\) is strictly decreasing. With \(N=mk\),
\[
\Pr(T_{N/k,k}>t)=(\mathbb E[Z_t^k])^{N/k}=\|Z_t\|_{L^k}^{N}.
\]
Strict monotonicity of \(L^p\)-norms in \(p\) for a positive nonconstant random variable proves the ordering. This only claims ordering across equal-size partitions with integer block sizes dividing \(N\); it does not assert ordering for every arbitrary repartition.

**6. Six-particle threshold.** For \(\alpha=2/5\), each permissible \(k\in\{1,2,3,6\}\) satisfies \(\alpha<k/2\). The survival exponent is therefore \(m\alpha=(6/k)(2/5)\), giving \(12/5,6/5,4/5,2/5\). The exact moment criterion proves the stated finite/infinite mean transition.

## Verification

Run `python checks.py` using Python 3 and `mpmath` (version 1.3 or later). The checker evaluates the exact diffusion-mixture integral, tests strict grouped-survival ordering at fixed population, verifies the constants and critical logarithms numerically, and confirms the six-particle exponent table. It reports 54 passed numerical/symbolic assertions. Those tests corroborate finite evaluations only: the proof above is what establishes all-time ordering and infinite-time tails and moment criteria.

## Relationship to prior work

Sposini and collaborators (Phys. Rev. Lett. 132, 117101, 2024; arXiv:2403.10143) analyze independent searchers with heterogeneous diffusivities and extreme first-arrival enhancement; their displayed product formulas rely on independence and do not establish exact block-shared slow-diffusivity tails or finite-moment transitions. Their companion Phys. Rev. E 109, 034120 (arXiv:2403.10138) gives one-particle subordination and target-survival comparisons, and directly supplies the classical conditional error-function survival formula. Lawley (Phys. Rev. E 101, 012413, 2020; arXiv:1909.09883) proves broad fastest-first-passage asymptotics for iid search times primarily as the number of searchers grows, not finite-population clustered dependence with time-frozen shared diffusivities. Hass and collaborators (arXiv:2406.17733) consider correlated search through shared, short-range-in-time random walks in random environments, not frozen independent Beta-distributed diffusivity blocks.

The conditional-survival identity, Jensen/\(L^p\)-norm ordering, and regular-variation integral method are classical tools and are not claimed to be novel individually. The proposed specific contribution is their combined **all-block-size sharp moment and logarithmic critical classification** for Brownian diffusion in frozen heavy-slow environments, including a fixed-population transition between finite and infinite mean first arrival. A general dependent-lifetime or shared-frailty theorem could subsume some or all of the conclusions; a literature search cannot rule out unindexed coverage.

## Limitations

The result is an exact special-model theorem rather than a universal statement about arbitrary disorder tails, time-dependent correlated environments, or bounded chambers. Independence of Brownian motions conditional on block diffusivities is essential. The Beta power law approaches zero diffusivity; different small-diffusivity behavior can change exponents and logarithmic corrections. The sharp constants use fixed positive parameters as \(t\to\infty\), and no uniformity in a joint particle-number/time limit is asserted. The finding has undergone a self-review, not an independent audit.

## References

1. V. Sposini, S. Nampoothiri, A. Chechkin, E. Orlandini, F. Seno, F. Baldovin, *Being Heterogeneous Is Advantageous: Extreme Brownian Non-Gaussian Searches*, Phys. Rev. Lett. **132**, 117101 (2024). DOI: https://doi.org/10.1103/PhysRevLett.132.117101 ; preprint https://arxiv.org/abs/2403.10143.
2. Same authors, *Being heterogeneous is disadvantageous: Brownian non-Gaussian searches*, Phys. Rev. E **109**, 034120 (2024). https://arxiv.org/abs/2403.10138.
3. S. D. Lawley, *Universal Formula for Extreme First Passage Statistics of Diffusion*, Phys. Rev. E **101**, 012413 (2020). https://arxiv.org/abs/1909.09883.
4. J. B. Hass, H. Drillick, I. Corwin, E. I. Corwin, *Extreme Diffusion Measures Statistical Fluctuations of the Environment* (2024). https://arxiv.org/abs/2406.17733.
