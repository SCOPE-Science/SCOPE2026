# Exact multi-partner rescue factorization and a unique immigration-allocation law

## Finding

For every integer \(n\ge 2\), every strictly positive initial extinction hazard \(d_0\), every vector of strictly positive missing-partner hazards \((\delta_1,\ldots,\delta_n)\), and every total immigration-rate budget \(B>0\), consider the continuous-time colonization process defined below. Put \(D=\sum_{i=1}^{n}\delta_i\), and let \(\lambda_i\ge0\) be the allocated encounter rate for partner \(i\), subject to \(\sum_i\lambda_i=B\). The probability of acquiring every required partner before host extinction is exactly

\[
P(\boldsymbol\lambda)=\frac{B+D}{B+d_0}\prod_{i=1}^{n}\frac{\lambda_i}{\lambda_i+\delta_i}.
\]

Here a zero encounter rate gives establishment probability zero. The probability has exactly one maximizing allocation, which is strictly positive in every coordinate. It is characterized by a unique multiplier \(\eta>0\) such that

\[
\lambda_i^*=\frac{\sqrt{\delta_i^2+4\delta_i/\eta}-\delta_i}{2},
\qquad \sum_{i=1}^{n}\lambda_i^*=B.
\]

The optimal rates have the same strict ordering as the missing-partner hazards: \(\delta_i>\delta_j\) if and only if \(\lambda_i^*>\lambda_j^*\); equality of hazards gives equality of allocated rates. The initial extinction hazard \(d_0\) changes the maximal probability but **does not change the maximizing allocation** under a fixed total budget.

As \(B\) tends to zero the optimum approaches equal division, and as \(B\) tends to infinity it approaches square-root hazard weighting:

\[
\lim_{B\downarrow0}\frac{\lambda_i^*}{B}=\frac1n,
\qquad
\lim_{B\to\infty}\frac{\lambda_i^*}{B}
=\frac{\sqrt{\delta_i}}{\sum_j\sqrt{\delta_j}}.
\]

In the large-budget regime the optimal failure probability has the sharp first-order coefficient

\[
1-P(\boldsymbol\lambda^*)=
\frac{d_0+2\sum_{i<j}\sqrt{\delta_i\delta_j}}{B}
+O(B^{-2}).
\]


Writing \(P_{\mathrm{eq}}\) for the success probability at equal allocation \(\lambda_i=B/n\), the asymptotic **gain from risk-aware allocation** is

\[
P(\boldsymbol\lambda^*)-P_{\mathrm{eq}}=
\frac{\sum_{i<j}(\sqrt{\delta_i}-\sqrt{\delta_j})^2}{B}
+O(B^{-2}).
\]

The leading gain is strictly positive whenever not all missing-partner hazards are equal, and exactly zero for identical hazards (when equal allocation is already optimal for all budgets).

## Assumptions and scope

A host colony initially lacks all of \(n\) distinct, necessary microbial or other mutualist partners. The acquired-partner state is a subset \(S\subseteq\{1,\ldots,n\}\). Before acquisition of partner \(i\), successful encounter events occur at the constant rate \(\lambda_i\), independently across partner types. Acquiring a partner is irreversible, and encounters with already acquired partners have no effect. The colony is extinguished at rate \(d_0>0\) while \(S=\varnothing\), and at rate \(\sum_{i\notin S}\delta_i\) while \(S\) is nonempty but incomplete. Each \(\delta_i>0\) is the extinction-hazard contribution associated with a still-missing partner. Once all partners have arrived, the colonization event is scored as successful; subsequent host dynamics are outside this model. All clocks are exponential and memoryless conditional on the state. Rates and budgets share reciprocal-time units. The result covers any \(d_0>0\); the ecologically monotone-risk case \(d_0\ge D\) is included.

The objective is the eventual *first establishment of the complete partner set before extinction*, not long-run survival or coexistence. The budget constraint applies to the sum of encounter rates, not to monetary or nonlinear expenditure. It presumes no effect of additional partner arrivals on the arrival rates of other still-missing partners.

## Proof

**Step 1: Reference-process factorization.** Introduce a reference process identical to the stated process except that at the empty-partner state its extinction rate is \(D=\sum_i\delta_i\). In this reference process, the extinction hazard for **every** incomplete subset \(S\) is \(\sum_{i\notin S}\delta_i\). Couple it to independent clocks \(T_i\sim\operatorname{Exp}(\lambda_i)\) for partner arrival and \(K_i\sim\operatorname{Exp}(\delta_i)\) for the corresponding missing-partner hazard. Clocks \(K_i\) cease to be relevant when partner \(i\) arrives. Successful acquisition of all partners occurs exactly on the event \(T_i<K_i\) for every \(i\). These events are independent. Therefore the reference success probability is

\[
P_{\mathrm{ref}}=\prod_i \Pr(T_i<K_i)
=\prod_i\frac{\lambda_i}{\lambda_i+\delta_i}.
\]

For zero \(\lambda_i\), the corresponding event is impossible; the same product convention applies. This independent-clocks construction precisely reproduces each reference transition hazard, including the empty and partially associated states.

**Step 2: Arbitrary empty-state hazard.** Until the first partner arrives, the total encounter rate is \(B\), and extinction occurs at rate \(d_0\) in the stated process, or at rate \(D\) in the reference process. Given survival until the first encounter, its species has probability \(\lambda_i/B\) in either process. Its subsequent conditional success probability \(q_i\) is identical in both, because all nonempty-state transition rates coincide and exponential waiting times are memoryless. Thus

\[
P=\frac{\sum_i\lambda_i q_i}{B+d_0},
\qquad
P_{\mathrm{ref}}=\frac{\sum_i\lambda_i q_i}{B+D},
\]

proving \(P=(B+D)P_{\mathrm{ref}}/(B+d_0)\) without assuming that the initial hazard is additive. Notice that the prefactor is constant over the budget simplex \(\sum_i\lambda_i=B\).

**Step 3: Existence, uniqueness, and hazard ordering.** If any allocated rate vanishes, success probability is zero, whereas any strictly positive feasible allocation has positive success probability. Hence every maximizer is interior. The logarithm of the allocation-dependent factor is \(\sum_i f_i(\lambda_i)\), where \(f_i(t)=\log t-\log(t+\delta_i)\). Its second derivative is

\[
f_i''(t)=-\frac{\delta_i(2t+\delta_i)}{t^2(t+\delta_i)^2}<0
\qquad (t>0).
\]

Strict concavity on the positive simplex proves a unique optimum. The Lagrange equations are \(\delta_i/[\lambda_i(\lambda_i+\delta_i)]=\eta\). Solving each positive quadratic gives the displayed allocation formula. For fixed hazards, each coordinate is continuous and strictly decreasing in \(\eta\), with sum varying from infinity to zero as \(\eta\) varies from zero to infinity. Thus the multiplier exists and is unique. The derivative \(\delta/[t(t+\delta)]\) is strictly increasing in \(\delta\) at fixed positive \(t\); consequently the common multiplier assigns larger \(t\) to larger \(\delta\), proving the exact ordering.

**Step 4: Sharp budget limits.** At high multiplier \(\eta\), the explicit quadratic solution satisfies \(\lambda_i^*=\eta^{-1}+O(\eta^{-2})\). Thus when \(B\downarrow0\), each coordinate is asymptotic to \(B/n\). At low multiplier, \(\lambda_i^*=\sqrt{\delta_i/\eta}-\delta_i/2+O(\sqrt\eta)\). Summing gives the large-budget square-root shares, and also \(\sum_i\delta_i/\lambda_i^*=(\sum_i\sqrt{\delta_i})^2/B+O(B^{-2})\). Expanding the probability prefactor and product yields

\[
P(\boldsymbol\lambda^*)=1+
\frac{D-d_0-(\sum_i\sqrt{\delta_i})^2}{B}
+O(B^{-2}),
\]

which is the stated failure-probability expansion because \((\sum_i\sqrt{\delta_i})^2-D=2\sum_{i<j}\sqrt{\delta_i\delta_j}\). For equal allocation, expanding the same expression gives \(P_{\mathrm{eq}}=1-[d_0+(n-1)D]/B+O(B^{-2})\). Subtracting yields the displayed gain because \(nD-(\sum_i\sqrt{\delta_i})^2=\sum_{i<j}(\sqrt{\delta_i}-\sqrt{\delta_j})^2\). All limits hold for fixed positive hazards and fixed \(n\).

## Verification

The standalone `checker.py` solves the independent subset-state first-step recursion using exact rational arithmetic for 270 heterogeneous parameter cases with \(2\le n\le7\), and checks the closed formula exactly. In 200 separate floating-point optimization cases for \(2\le n\le9\), it checks the budget, equal marginal log-success derivatives, strict hazard ordering, and domination of randomized feasible allocations. It also checks both budget-limit formulas numerically. All tests passed when run from the packaged file. The exact-state tests are finite diagnostics, not a substitute for the coupling and concavity proofs above.

For a concrete three-partner example, take \((\delta_1,\delta_2,\delta_3)=(1,4,9)\), \(d_0=20\), and \(B=12\). The unique optimum is approximately \((2.4654,4.1785,5.3561)\). The corresponding success probability is approximately \(0.1102\), versus approximately \(0.1000\) for equal allocation \((4,4,4)\). These illustrative rates have not been fitted to a biological system.

## Relationship to prior work

Amarasekare (2004) develops a spatial plant–pollinator mutualism model and shows that dispersal can rescue vulnerable local communities or deplete sources. Its full-text occupancy and dispersal dynamics are not the present finite, independent-encounter, multi-partner rate-allocation process. Antunes, Deaville and Goss (first public online 2005) examine an empirical soybean–mycorrhiza–rhizobium tripartite association, furnishing motivation for multiple beneficial partners but not a fixed-budget stochastic arrival law. Yamauchi, Nishida and Ohgushi (first public online 2009) model stochastic tunneling before and after association with a **single** symbiont using a diffusion approximation with one association rate; their analyzed growth and variance trade-offs do not entail the multi-partner factorization or allocation theorem. Older system-reliability and exponential-repair scheduling research addresses related stochastic optimization but could provide an unrecognized equivalent abstraction. These are comparisons of models and implications, not a claim that a database search proves historical uniqueness.

## Limitations

The conclusion depends on independent constant-rate arrival clocks and additive missing-partner hazards after the first arrival; it is not established for time-varying immigration, facilitation between partner arrivals, irreversible partner loss, density-dependent extinction, nonadditive intermediate hazards, or finite-time objectives. The empty-state multiplier is allocation-independent only because the total first-encounter rate is held fixed. The ecological interpretation is an idealized mechanistic benchmark, not a measured conservation policy. A broad, formally equivalent theorem in generic competing-risks or reliability literature cannot be excluded without further domain-specific historical review. No independent audit or empirical validation is asserted.

## References

- Amarasekare, P. (2004). *Spatial dynamics of mutualistic interactions*. Journal of Animal Ecology 73, 128–142. First online 2004-01-06. https://doi.org/10.1046/j.0021-8790.2004.00788.x
- Antunes, P. M., Deaville, D., and Goss, M. J. (2006). *Effect of two AMF life strategies on the tripartite symbiosis with Bradyrhizobium japonicum and soybean*. Mycorrhiza 16, 167–173. First online 2005-12-16. https://doi.org/10.1007/s00572-005-0028-3
- Yamauchi, A., Nishida, T., and Ohgushi, T. (2009). *Stochastic tunneling in the colonization of mutualistic organisms: Primary succession by mycorrhizal plants*. Journal of Theoretical Biology 261, 74–82. First online 2009-07-28. https://doi.org/10.1016/j.jtbi.2009.07.021
- Shaked, M., and Shanthikumar, J. G. (1988). *On the first failure time of dependent multicomponent reliability systems*. Mathematics of Operations Research 13, 50–64. https://doi.org/10.1287/moor.13.1.50
