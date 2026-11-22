# A uniform front and a random exponential bulk in collective ballistic threshold resetting

## Finding

Consider \(N\) independent left-moving ballistic particles that start each excursion at \(L>0\), independently draw speeds from \(\operatorname{Exp}(\lambda)\), and all return instantaneously to \(L\) when the first reaches the origin. Every return redraws all speeds independently. The following constitutes one joint stationary-and-large-population theorem.

For every \(N\ge2\) the process has a unique stationary probability law. At a stationary observation, write \(M_N=\max_{1\le i\le N}V_i\) and \(X_i\) for the positions. The speed vector has the original product-exponential law tilted by \(1/M_N\), and independently a phase \(U\) is uniform on \((0,1)\):

\[
X_i=L\left(1-U\frac{V_i}{M_N}\right),\qquad 1\le i\le N.
\]

In particular, the leftmost position \(\min_i X_i=L(1-U)\) is **exactly uniform on \((0,L)\) for every \(N\ge2\)**, although the tagged-particle position is not uniform. By contrast \(N=1\) has no stationary probability law. The exact time \(\tau_N\) between successive collective returns has survival function

\[
\Pr(\tau_N>t)=\left(1-e^{-\lambda L/t}\right)^N,\qquad t>0,
\]

so its positive moment of order \(p\) is finite precisely when \(p<N\).

As \(N\to\infty\), define the scaled displacements toward the target

\[
Z_{i,N}=(\log N)\left(1-\frac{X_i}{L}\right),\qquad
\mu_N=\frac1N\sum_{i=1}^N\delta_{Z_{i,N}}.
\]

For any fixed number \(k\) of tagged particles,

\[
(Z_{1,N},\ldots,Z_{k,N})\ \Rightarrow\ (UE_1,\ldots,UE_k),
\]

where \(E_1,\ldots,E_k\) are independent unit-rate exponential variables, independent of the *same* \(U\sim\operatorname{Uniform}(0,1)\). Moreover the random empirical measures converge weakly in distribution to \(\mu_U\), with conditional density

\[
\mu_U(dz)=\frac1U e^{-z/U}\mathbf1_{\{z\ge0\}}\,dz.
\]

Consequently, for each \(z>0\), the fraction of particles displaced by more than \(Lz/\log N\) converges in distribution to the **nondegenerate** random fraction

\[
\frac1N\#\left\{i:X_i<L\left(1-\frac{z}{\log N}\right)\right\}
\ \Rightarrow\ Q_z=e^{-z/U}.
\]

Its exact distribution is \(\Pr(Q_z\le q)=z/(-\log q)\) for \(0<q<e^{-z}\), and equals one for \(q\ge e^{-z}\). In the same stationary snapshot, \((\log N)(1-N^{-1}\sum_i X_i/L)\Rightarrow U\), while \(\min_i X_i/L\) remains uniform for every finite population. Thus the unscaled bulk concentrates at the reset point but the extreme front spans the entire interval, and the scaled bulk does not self-average.

## Assumptions and scope

At the start of every excursion, each particle draws a fresh independent speed with density \(\lambda e^{-\lambda v}\) on \(v>0\), moves deterministically to the left at that speed, and stops the whole excursion at the first arrival to zero. All particles instantly reappear at \(L\), and all speeds are independently redrawn. The index \(N\) is a positive integer. The full state includes positions and their current speeds, so the described process is regenerative and Markovian on its natural state space. The stationary claims concern observation at an ordinary time, not at a return epoch; these sampling rules differ. The large-population results first take the stationary regime at each \(N\ge2\), then send \(N\) to infinity. Convergence of random probability measures is for the weak topology on measures on \([0,\infty)\). There is no thermal Brownian noise, speed persistence between returns, target other than zero, or interaction other than the shared return event.

## Proof

**1. Excursion clock and existence.** Conditional on freshly sampled speeds, the first absorption occurs at \(\tau_N=L/M_N\). Independence gives \(\Pr(\tau_N>t)=\Pr(V_1<L/t)^N=(1-e^{-\lambda L/t})^N\). Its tail is asymptotic to \((\lambda L)^Nt^{-N}\). The tail-integral characterization of moments shows \(\mathbb E\tau_N^p<\infty\) exactly when \(0<p<N\). Thus the mean excursion duration is finite exactly for \(N\ge2\). The positive continuous excursion-duration law is nonarithmetic. Standard regenerative occupation and renewal results give a unique stationary law when this mean is finite. A finite invariant probability for \(N=1\) would require normalizing the excursion occupation measure by the infinite mean duration, which is impossible; thus the \(N=1\) process is not positive recurrent and has no stationary probability.

**2. Exact stationary law.** Let \(\mathbb P_N\) denote the original product-exponential speed measure. The stationary renewal-reward identity, valid for bounded measurable functions \(F\) of positions and (if desired) speeds, is

\[
\mathbb E_{\mathrm{st}}F
=\frac{\mathbb E_{\mathbb P_N}\big[\int_0^{L/M_N}
 F(L-aV_1,\ldots,L-aV_N;V_1,\ldots,V_N)\,da\big]}
 {L\,\mathbb E_{\mathbb P_N}(1/M_N)}.
\]

Changing variable \(a=uL/M_N\) produces the claimed speed tilt and an independent uniform \(u\). Since the maximal speed advances the largest distance, \(\min_iX_i=L(1-U)\). This proves the exact uniform extreme without assuming spatial independence.

**3. Vanishing tilt in the large-population limit.** Set \(E_i=\lambda V_i\), \(Y_N=\max_iE_i\), \(a_N=Y_N/\log N\). Under the original product law, \(Y_N/\log N\to1\) in probability. For every \(\delta\in(0,1)\),

\[
\Pr(Y_N<(1-\delta)\log N)\le e^{-N^{\delta}},\qquad
\Pr(Y_N>(1+\delta)\log N)\le N^{-\delta}.
\]

For \(N\ge3\), \(\mathbb E(Y_N^{-2})\le\mathbb E(Y_3^{-2})<\infty\). Cauchy--Schwarz controls the small-maximum event:

\[
\mathbb E\left[\frac{\log N}{Y_N}\mathbf1_{\{Y_N<(1-\delta)\log N\}}\right]
\le (\log N)\sqrt{\mathbb E(Y_3^{-2})}\,e^{-N^{\delta}/2}.
\]

On the complement the reciprocal is bounded by \(1/(1-\delta)\), and the maximum-concentration inequalities apply. Letting first \(N\to\infty\), then \(\delta\downarrow0\), gives \((\log N)/Y_N\to1\) in \(L^1\). Consequently the product-law density of the tilted speed distribution, proportional to \(1/Y_N\), tends to one in \(L^1\); equivalently, the tilted and original \(N\)-speed measures have total-variation distance tending to zero. In particular \(\mathbb E(1/M_N)\sim\lambda/\log N\). The tilt does not alter any bounded-probability large-population limit.

**4. Tagged particles and random empirical limit.** Under the original speed law, \(a_N\to1\) in probability and the empirical law of \((E_1,\ldots,E_N)\) converges to the unit-rate exponential law by the law of large numbers. The independent uniform phase remains independent under the tilted law for every \(N\). Since \(Z_{i,N}=UE_i/a_N\), Slutsky's theorem proves the fixed-tag joint limit. For every bounded Lipschitz \(f\),

\[
\frac1N\sum_{i=1}^N f(UE_i/a_N)
-\frac1N\sum_{i=1}^N f(UE_i)\ \longrightarrow\ 0
\]

in probability: its magnitude is bounded by the Lipschitz constant times \(U|a_N^{-1}-1|N^{-1}\sum_iE_i\). Conditional on \(U\), the second average converges to \(\mathbb E[f(UE_1)\mid U]\). A countable bounded-Lipschitz determining class yields random-measure convergence, and the preceding total-variation argument transfers it to stationary samples. The exponential density follows by scaling a unit-rate exponential variable by \(U\).

**5. Measurable consequences and sharp limits.** The limiting measure has no atom at any positive threshold, so its upper-tail fraction at \(z>0\) is \(Q_z=e^{-z/U}\). The displayed distribution function follows by solving \(e^{-z/U}\le q\) for \(U\). It is nondegenerate because it is strictly increasing in \(U\). The scaled empirical first moment satisfies \(N^{-1}\sum_i Z_{i,N}=U(N^{-1}\sum_iE_i)/a_N\Rightarrow U\). Since \(N^{-1}\sum_iX_i/L=1-(N^{-1}\sum_iZ_{i,N})/\log N\), the unscaled empirical measure collapses to the point mass at \(L\). This does not affect the exactly uniform leftmost particle, which is a single extreme observation and has vanishing empirical weight. The statements hold only for the stipulated order of limits and the exponential-speed ensemble.

## Verification

The companion `checker.py` uses only Python's standard library and a fixed random seed. It compares the exact two-particle reciprocal-maximum normalization \(2\lambda\log2\) with numerical quadrature; compares the inter-return survival against independently simulated cycles; checks duration-weighted stationary expectations for several particle counts; and tests the scaled mean displacement, positive limiting variance of the exceedance fraction, and the explicit limiting distribution function. Finite checks establish arithmetic consistency but do not prove the infinite-population theorem. The proof of total-variation convergence and the random-measure limit is analytic and independent of those diagnostics.

## Relationship to prior work

Das, Majumdar and Pal (arXiv:2611.16733, publicly submitted 12 November 2026) derive a uniform stationary **single-particle** position law, transient freezing and shock effects for randomized-speed threshold resetting; their conclusion specifically identifies the many-ballistic-particle extension as a further direction. Biroli, Majumdar and Schehr (arXiv:2512.00440) solve the collective **Brownian** first-passage-resetting gas and its large-population **Gaussian** mixture and correlations. This paper supplies an important methodological precedent and the phenomenon of reset-induced common-factor correlations is not new. Biswas, Majumdar and Pal (arXiv:2504.13501, supplementary section S8.2, equations S96–S98) **already derive the identical survival function** \((1-e^{-L/t})^N\) and the associated finite-mean threshold \(N\ge2\) for exponential-speed ballistic first passage at their optimal search boundary. Their protocol ends on target arrival and otherwise resets at a separate boundary; it does not supply an ordinary-time stationary position law in the repeated-cycle model considered here. The excursion survival function and the population recurrence cutoff are therefore credited precedents, **not priority claims**. The new part is the full stationary position/velocity law and its logarithmically scaled, non-self-averaging exponential empirical measure. The general renewal-reward/mean-local-time principle from Das, Majumdar and Pal (arXiv:2609.24438) is also pre-existing and is used explicitly. What is asserted here as potentially original is the distinct exact exponential-speed stationary population law, the *uniform extreme with exponentially mixed logarithmic bulk*, and its non-self-averaging exceedance statistic. The recurrence cutoff, inter-return survival and classical occupation method are mathematical premises and are not asserted to be new. These conclusions are not merely the Brownian formulas with relabeled parameters.

## Limitations

Only one specified law of the speeds is classified in the large-population theorem; universality over arbitrary speed distributions is **not** claimed. The full joint stationary law follows from regenerative occupation; renewal and concentration techniques are classical, so novelty is confined to the concrete combined first-passage ballistic population consequences. Large-population convergence says nothing quantitative about the convergence rate at moderate \(N\). Numerical diagnostics do not constitute an exhaustive proof. The identical first-passage duration and mean threshold in arXiv:2504.13501 are expressly credited; other unindexed work may contain equivalent stationary-profile results; independent source verification and publication-priority assessment remain outstanding.

## References

1. R. Das, S. N. Majumdar, A. Pal, *Freezing transition and shock-like transients in ballistic random walks under threshold resetting*, arXiv:2611.16733v1 (12 November 2026), https://arxiv.org/html/2611.16733.
2. M. Biroli, S. N. Majumdar, G. Schehr, *First Passage Resetting Gas*, arXiv:2512.00440v2; EPL 153, 31002 (2026), https://arxiv.org/html/2512.00440v2.
3. A. Biswas, S. N. Majumdar, A. Pal, *Target Search Optimization by Threshold Resetting*, arXiv:2504.13501 (first submitted 18 April 2025); Physical Review Letters 135, 227101 (2025), https://arxiv.org/abs/2504.13501.
4. R. Das, S. N. Majumdar, A. Pal, *Non-equilibrium dynamics of drift-diffusion process under threshold resetting*, arXiv:2609.24438 (first submitted 21 September 2026), https://arxiv.org/abs/2609.24438.
