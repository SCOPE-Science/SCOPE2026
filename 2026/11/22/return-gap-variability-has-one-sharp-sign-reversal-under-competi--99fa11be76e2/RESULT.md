# Return-gap variability has one sharp sign reversal under competing heat-stress memories, while matched moments can give opposite responses

## Finding

Consider a second-event response with a residual harmful memory and a residual protective memory that relax at different rates. For fixed and bounded mean-zero inter-event fluctuations, changing their variability in convex order can reverse its effect on the *expected response* at most once as the mean time between events increases. The possible reversal is exactly computable from two exponential moments of the gap fluctuations. Separately, two distinct nonnegative return-gap distributions with precisely the same mean and variance can alter this response in **opposite directions** relative to a fixed interval at that mean. These statements concern a mathematical response index, not a measured coral bleaching probability.

The novel joint object is the coupling of a two-mode protective–harmful recovery surrogate with event-return-time *distributions*. The motivating question is whether representing recurrent environmental shocks by only their mean spacing and spacing variance can misclassify whether variable recurrence is beneficial or harmful.

## Assumptions and scope

Let \(0<a<d\), \(A,D>0\), and \(v_0\ge A\). For every elapsed time \(t\ge0\) after a first heat-stress episode, define
\[
V(t)=v_0+D e^{-dt}-A e^{-at}.
\]
The term \(D e^{-dt}\) represents residual harmful sensitization and the term \(A e^{-at}\) retained protection from acclimatization. The faster rate \(d\) describes harmful memory relaxing more rapidly than beneficial memory. The inequality \(v_0\ge A\) ensures \(V(t)\ge0\), but does not give this index a calibrated probability interpretation.

Let \(X,Y\) be bounded real random variables with \(\mathbb E X=\mathbb E Y=0\), distinct laws, and \(X\preceq_{\mathrm{cx}}Y\): \(\mathbb E\varphi(X)\le\mathbb E\varphi(Y)\) for every convex test function \(\varphi\). Equivalently, their laws admit a martingale coupling; the usual strict Jensen inequality is valid for a strictly convex test function when the laws differ. Choose \(\mu\ge\mu_0\) where
\[
\mu_0=\max\{0,-\operatorname{ess\,inf}X,-\operatorname{ess\,inf}Y\},
\]
so that both physical return gaps \(\mu+X\) and \(\mu+Y\) are nonnegative. Define the strictly positive numbers
\[
\Delta_s=\mathbb E(e^{-sY})-\mathbb E(e^{-sX}),\qquad s>0.
\]
The index comparison is \(C(\mu)=\mathbb E V(\mu+Y)-\mathbb E V(\mu+X)\). Here positive \(C\) means the more variable gap law gives a larger expected vulnerability index, and negative \(C\) means a smaller one. Boundedness can be weakened to existence of the two relevant exponential moments and a common lower support bound.

## Proof

**Exact one-switch theorem.** Every function \(t\mapsto e^{-st}\), \(s>0\), is strictly convex. Since the two laws are different and in convex order, the martingale-coupling form of strict Jensen gives \(\Delta_a>0\) and \(\Delta_d>0\). By linearity and exponential factorization,
\[
C(\mu)=D\Delta_d e^{-d\mu}-A\Delta_a e^{-a\mu}
=e^{-a\mu}\bigl(D\Delta_d e^{-(d-a)\mu}-A\Delta_a\bigr).
\]
The bracket is strictly decreasing in \(\mu\) and has exactly one real zero, at
\[
\mu_* =\frac{\log(D\Delta_d/(A\Delta_a))}{d-a}.
\]
Consequently, on the admissible half-line \(\mu\ge\mu_0\), there is one interior positive-to-negative sign reversal if and only if \(\mu_*>\mu_0\). If \(\mu_*=\mu_0\), there is equality only at the admissible endpoint and a negative difference afterward; if \(\mu_*<\mu_0\), the difference is negative everywhere. No second reversal is possible, independent of the full shapes of the two bounded gap laws. This establishes all boundaries and quantifiers of the first claim.

**Exact equal-moment counterexample.** Put \(v_0=D=A=a=1\), \(d=2\), \(\mu=\log5\), and \(J=\log2\). Compare the deterministic gap \(T_0=\mu\) with two stochastic gaps \(T_P,T_Q\) having distributions
\[
\Pr(T_P=\mu-J)=\Pr(T_P=\mu+J)=\tfrac12,
\]
\[
\Pr(T_Q=\mu)=\tfrac34,\quad
\Pr(T_Q=\mu-2J)=\Pr(T_Q=\mu+2J)=\tfrac18.
\]
Because \(\mu-2J=\log(5/4)>0\), all gaps are positive. Both distributions have mean \(\mu\) and variance \(J^2\), since \(\tfrac18(2J)^2+\tfrac18(2J)^2=J^2\). Their Laplace excesses over the deterministic gap, before multiplication by \(e^{-s\mu}\), are
\[
\begin{aligned}
E_{P,1}&=\tfrac14,& E_{P,2}&=\tfrac98,\\
E_{Q,1}&=\tfrac9{32},& E_{Q,2}&=\tfrac{225}{128}.
\end{aligned}
\]
Indeed, \(e^{J}=2\) and \(e^{2J}=4\), so these are exact rational evaluations of the two distributions' exponential moments. As \(V(t)=1+e^{-2t}-e^{-t}\),
\[
\mathbb E V(T_P)-V(\mu)=\frac{9/8}{25}-\frac{1/4}{5}=-\frac1{200},
\]
\[
\mathbb E V(T_Q)-V(\mu)=\frac{225/128}{25}-\frac{9/32}{5}=\frac9{640}.
\]
This proves a strict opposite-sign outcome despite equal first and second moments. More precisely, the two protocols have different one-switch mean-gap thresholds relative to a fixed gap at the same mean: \(\mu_{*,P}=\log(9/2)\) and \(\mu_{*,Q}=\log(25/4)\); the witness mean \(\log5\) lies strictly between them. Both random laws are convex-order larger than a fixed interval, but the two random laws need not be convex-ordered with each other. The proof of the one-switch theorem does not depend on this counterexample, and the counterexample does not assert a convex ordering between \(P\) and \(Q\).

## Verification

The accompanying standalone `checker.py` performs exact rational evaluations of all four Laplace excesses, the equality of both variances, the strict positivity of all return times, the opposing vulnerability changes, and the exact ordering of the two crossover thresholds. It also checks a few signs on either side of the analytic boundary. It uses the Python standard library only and has no external data dependencies. The all-distributions, all-means result is proved analytically above; the finite test program is not used as a surrogate for the infinite-quantifier proof.

For the displayed example, recompute \(E_{P,s}\) and \(E_{Q,s}\) by averaging \(2^{\pm s}\) and \(4^{\pm s}\) for \(s=1,2\). Then multiply each by \(5^{-s}\), take the harmful minus protective components, and compare the resulting rational fractions.

## Relationship to prior work

Schoepf, Sanderson and Larcombe (first published 23 December 2021) empirically compared coral thermal-variability regimes and found that similar total exposure can yield different physiological outcomes. Brown and colleagues (2023) documented beneficial acclimatization in some species and prolonged/incomplete recovery in others after repeated heatwaves. Pfab and colleagues (2024) developed a nonlinear bioenergetic coral-symbiosis model with temperature-driven metabolic acceleration and photosynthetic damage. These are biological motivations, not premises that establish the particular surrogate or its stochastic-gap result. None of the inspected statements, methods, results or model equations gives the exact convex-order return-gap threshold and the equal-first-two-moments opposite-sign pair above.

The convex-order/Jensen statement itself and elementary Laplace-transform algebra are standard tools; no general priority claim is made for those tools. The narrowly assessed distinction is the combined recovery-gap response classification and explicit moment-indistinguishability boundary for this stylized stress-memory index. A stronger existing result on signed exponential mixtures, if found, could reduce historical priority; published-database searches and the inspected primary texts are evidence against directly matching coverage, not proof of uniqueness.

## Limitations

No empirical coral observations are fitted, and there is no claim that response \(V\) equals probability of mortality or bleaching. Instantaneous episodes, independent fixed amplitudes, constant rates, two memory modes and exogenous return-gap laws are simplifying assumptions. Real reef responses can be nonlinear, species-specific, severity-dependent and shaped by selection, adaptation, cumulative damage and many more latent variables. The result does not compare full event sequences with feedback, identify optimal interventions or predict a reef's fate. The strict convex-order assumption is essential for the universal one-switch comparison; variance alone is not a convex order. The counterexample is exact but parameter-specific and is intended to identify a limitation of mean–variance summaries, not establish an experimentally observed sign flip. General mathematical antecedents for signed exponential mixtures remain a residual priority risk. Independent validation has not been performed.

## References

1. Schoepf, V., Sanderson, H. & Larcombe, E. (2022). *Coral heat tolerance under variable temperatures: Effects of different variability regimes and past environmental history vs. current exposure*. Limnology and Oceanography 67, 404–418. First publicly published 2021-12-23. https://doi.org/10.1002/lno.12000
2. Brown, K. T. et al. (2023). *Divergent bleaching and recovery trajectories in reef-building corals following a decade of successive marine heatwaves*. PNAS 120, e2312104120. Published 2023-12-19. https://doi.org/10.1073/pnas.2312104120
3. Pfab, F. et al. (2024). *Heat stress and bleaching in corals: a bioenergetic model*. Coral Reefs 43, 1627–1645. Published 2024-10-30. https://doi.org/10.1007/s00338-024-02561-1
4. Rothschild, M. & Stiglitz, J. E. (1970). *Increasing risk: I. A definition*. Journal of Economic Theory 2, 225–243. Classical convex-order/mean-preserving-spread antecedent; not an application-specific result.
