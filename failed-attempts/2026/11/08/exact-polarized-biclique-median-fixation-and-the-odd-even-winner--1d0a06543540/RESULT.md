# Exact polarized-biclique median fixation and the odd–even winner bias

## Finding

For every pair of integers \(m,n\geq1\) and rates \(\lambda_A,\lambda_B>0\), consider asynchronous binary weighted-median adoption on the complete bipartite graph \(K_{m,n}\). All \(m\) vertices in camp \(A\) initially have opinion \(0\), and all \(n\) vertices in camp \(B\) initially have opinion \(1\). Every vertex in a camp has an independent Poisson update clock of its camp's rate, adopts the **strict** majority opinion among its neighbors, and retains its current opinion in an exact tie. Write \(P_1\) for the probability of eventual unanimous opinion \(1\).

Let \(a=\lceil m/2\rceil\) and \(b=\lceil n/2\rceil\). If \(T_A\) is the \(a\)-th order statistic among \(m\) independent rate-\(\lambda_A\) exponential variables and \(T_B\) is the \(b\)-th order statistic among \(n\) independent rate-\(\lambda_B\) exponential variables, with the two families independent, then the process reaches consensus almost surely and

\[
\boxed{P_1=\Pr(T_A<T_B).}
\]

In particular, for every such \(m,n,\lambda_A,\lambda_B\), its **exact finite rational expression in the two rates** is

\[
P_1=a\binom ma\sum_{j=0}^{b-1}\binom nj
\sum_{k=0}^{a-1}\sum_{h=0}^{j}
\frac{(-1)^{k+h}\binom{a-1}{k}\binom jh\,\lambda_A}
{(m-a+1+k)\lambda_A+(n-j+h)\lambda_B}.
\]

At equal individual rates, the cancellation-free count is

\[
\boxed{P_1=\frac{1}{\binom{m+n}{m}}\sum_{j=0}^{b-1}
\binom{a+j-1}{j}\binom{m+n-a-j}{m-a}.}
\]

A strict **parity law** holds at equal rates: if both camp sizes are odd, \(P_1=1/2\) for any sizes; if \(m\) is even and \(n\) odd then \(P_1>1/2\); if \(m\) odd and \(n\) even then \(P_1<1/2\). For both-even camp sizes the finite count above applies; if \(m=n\), symmetry gives \(P_1=1/2\) regardless of parity. Thus an even-sized camp has a strict advantage over an odd-sized opposing camp under equal per-vertex activation rates, irrespective of the camp sizes.

Writing \(r=\lambda_A/\lambda_B\), for each fixed pair \((m,n)\) the function \(P_1(r)\) is continuous and strictly increasing from \(0\) to \(1\); there is exactly one activity ratio \(r_*\) giving \(P_1(r_*)=1/2\). For example, at \((m,n)=(2,3)\),

\[
P_1(r)=1-\frac{6}{(3+2r)(2+2r)},\qquad
P_1(1)=\frac{7}{10},\qquad r_*=\frac12.
\]

At \((m,n)=(2,4)\) with equal rates, \(P_1=3/5\).

## Assumptions and scope

The graph has neither self-neighbor weights nor edges within either camp; each edge from a vertex to the opposite camp has equal influence weight. Opinions are binary; all of \(A\) starts at \(0\), all of \(B\) at \(1\). A vertex updates when its own independent rate-\(\lambda_A\) or rate-\(\lambda_B\) clock rings, implementing the median of the opposite camp's current binary opinions and choosing its **own** current opinion when the median is nonunique. All sizes are finite and positive; rates are strictly positive, not normalized to a common total group activation rate. The labels \(A\) and \(B\) specify the initial camps; \(P_1\) concerns the final opinion, not an arbitrary binary voter model.

## Proof

1. **First-threshold race, including ties.** Let \(x\) count vertices of \(A\) that have switched to \(1\), and \(y\) count vertices of \(B\) that have switched to \(0\), starting from \((0,0)\). As long as \(x<a\) and \(y<b\), we have \(x<m/2\) and \(y<n/2\). Thus each unrevised vertex in \(A\) switches from \(0\) to \(1\) at rate \(\lambda_A\), and each unrevised vertex of \(B\) switches from \(1\) to \(0\) at rate \(\lambda_B\). No already switched vertex changes back in this region. Consequently the pre-threshold change rates are \((m-x)\lambda_A\) and \((n-y)\lambda_B\).

   Suppose \(x\) first reaches \(a\) before \(y\) reaches \(b\). Since \(y<b\) still implies \(y<n/2\), the current \(A\)-vertices with opinion \(0\) continue to adopt \(1\). Since \(x\geq m/2\), the remaining \(B\)-vertices holding \(1\) never switch to \(0\): if \(m\) is even and \(x=m/2\), they retain opinion \(1\) by the tie rule; if \(x>m/2\), all updated \(B\)-vertices adopt \(1\). Thus \(y\) cannot increase to \(b\), and all \(A\)-vertices become \(1\) after finitely many clock rings almost surely. Once \(A\) is unanimous \(1\), any \(B\)-vertices with opinion \(0\) switch to \(1\) at positive rate, giving eventual unanimous \(1\). The symmetric argument when \(y\) hits \(b\) first gives unanimous \(0\). Continuous independent clocks make simultaneous threshold attainment probability zero. In particular, using the **strict-majority** threshold \(\lfloor m/2\rfloor+1\) would be wrong for even-sized camps: reaching exactly half already prevents the other camp's remaining unfavorable conversions.

2. **Independent exponential order statistics.** Until the first of the thresholds, each individual can contribute at most one opinion conversion, at the first ring of that individual's own clock. Replace the post-threshold evolution by the virtual first-clock times for all individuals; this replacement does not change which camp first reaches its threshold. In \(A\), the \(a\)-th such time is \(T_A\); in \(B\), the \(b\)-th is \(T_B\). Independence proves \(P_1=\Pr(T_A<T_B)\), including almost-sure absorption.

3. **Closed form.** The density of \(T_A\) is

   \[
   f_A(t)=a\binom ma\lambda_A
   (1-e^{-\lambda_A t})^{a-1}e^{-(m-a+1)\lambda_A t},
   \]

   and

   \[
   \Pr(T_B>t)=\sum_{j=0}^{b-1}\binom nj
   (1-e^{-\lambda_B t})^{j}e^{-(n-j)\lambda_B t}.
   \]

   Integrate \(f_A(t)\Pr(T_B>t)\) over \(t\in(0,\infty)\), expand the two binomial powers, and integrate each exponential. Every denominator is strictly positive, yielding the displayed finite-sum formula.

4. **Equal-rate discrete count.** At \(\lambda_A=\lambda_B\), the order of all \(m+n\) distinct first-clock times is a uniformly random arrangement of \(m\) labels \(A\) and \(n\) labels \(B\). If the \(a\)-th \(A\) occurs in position \(a+j\), with \(0\leq j<b\), it is the first camp to attain its threshold. The preceding positions admit \(\binom{a+j-1}{j}\) arrangements, and the remaining positions admit \(\binom{m+n-a-j}{m-a}\) arrangements. Divide their sum by \(\binom{m+n}{m}\).

5. **Odd–even sign.** Under equal rates, apply the increasing transformation \(u=1-e^{-\lambda t}\) to both order statistics. The two transformed variables are independent with distributions \(U_A\sim\mathrm{Beta}(a,m-a+1)\) and \(U_B\sim\mathrm{Beta}(b,n-b+1)\). For an odd camp, the beta density is symmetric about \(1/2\); for an even camp of size \(2k\), its threshold density is proportional to \(u^{k-1}(1-u)^k\), whose value at \(u\in(0,1/2)\) strictly exceeds the value at \(1-u\). If \(U_B\) is symmetric, let \(g(u)=\Pr(U_B>u)\). Then \(g(1-u)=1-g(u)\) and \(g(u)>1/2\) below \(1/2\). Pairing each \(u\) with \(1-u\) in the integral \(\Pr(U_A<U_B)=\int f_A(u)g(u)\,du\) proves it strictly exceeds \(1/2\) when \(A\) is even and \(B\) odd. Exchanging the camps gives the reversed sign. If both camps are odd, the joint reflection \((U_A,U_B)\mapsto(1-U_A,1-U_B)\) exchanges the two strict order events, giving exactly \(1/2\). If the two camp sizes agree, exchangeability also gives \(1/2\).

6. **Unique activity calibration.** Write \(T_A=S_A/\lambda_A\) and \(T_B=S_B/\lambda_B\) for independent, strictly positive unit-rate order statistics. Therefore \(P_1(r)=\Pr(S_A/S_B<r)\). The ratio has a continuous density that is positive throughout \((0,\infty)\), proving strict increase, continuity and the limiting values. For \((m,n)=(2,3)\), \(S_A\) is exponential of rate \(2\) and \(S_B\) is the sum of independent rate-\(3\) and rate-\(2\) exponentials. Its Laplace transform yields the stated rational expression and unique root \(r_*=1/2\).

## Verification

Execute the accompanying standalone Python standard-library script with `python verify.py`. It checks 196 exact-rational instances (all \(1\leq m,n\leq7\) at four rate pairs) against the integral sum, 49 same-rate uniform-permutation formulas, all checked parity instances, and 72 independent labeled-state Markov recursions (all \(1\leq m,n\leq4\) at three rate pairs) implementing each node's actual median and tie behavior. All checks passed. These finite checks do not prove the infinite parameter statement; the six proof steps above do.

## Relationship to prior work

The discrete weighted-median influence rule and nearest-current-opinion tie resolution are those of Mei et al. (2019); the general equilibrium and convergence analysis of Mei et al. (2022) addresses the qualitative dynamics but does not give this polarized biclique's exact rate-dependent fixation law in its inspected main text and appendices. The 2024 continuous-time median-with-inertia model is dynamically different from instantaneous stochastic updates. Classical voter results on heterogeneous graphs allow random-neighbor copying rather than strict-majority adoption; on a polarized biclique their neutral copying fixation mechanism differs from the parity-sensitive law above. The 2023 asynchronous majority work studies initial private signals, initially unannounced opinions, and random rather than complete bipartite networks. Exact binomial/negative-hypergeometric order-statistic identities are standard mathematical tools; the contribution claimed here is their sharp coupling to the tie-retaining median dynamics and the resulting complete outcome/parity/rate law, not invention of those identities.

## Limitations

The claim does not treat mixed initial opinions within a camp, self-weights, nonuniform neighbor weights, different per-node rates within a camp, arbitrary bipartite graphs, or time-varying weights. It gives winner probabilities and almost-sure consensus, not full consensus-time distributions. The conclusion for an even camp uses **retention of the current opinion on ties**; other tie conventions can change the result. Literature novelty is based on the inspected accessible material and searches; an unindexed equivalent remains a priority risk. Independent external validation has not been performed.

## References

- Wenjun Mei, Francesco Bullo, Ge Chen, Julien Hendrickx, Florian Dörfler, *Rethinking the Micro-Foundation of Opinion Dynamics: Rich Consequences of the Weighted-Median Mechanism*, arXiv:1909.06474, first publicly posted 2019-09-13. https://arxiv.org/html/1909.06474v9
- Wenjun Mei, Julien M. Hendrickx, Ge Chen, Francesco Bullo, Florian Dörfler, *Convergence, Consensus and Dissensus in the Weighted-Median Opinion Dynamics*, arXiv:2212.08808, first publicly posted 2022-12-17. https://arxiv.org/html/2212.08808v1
- Yi Han, Julien M. Hendrickx, Ge Chen, Wenjun Mei, *Modeling, Analysis, and Control of Continuous-Time Weighted-Median Opinion Dynamics*, arXiv:2404.16318, first publicly posted 2024-04-25. https://arxiv.org/html/2404.16318v3
- V. Sood, T. Antal, S. Redner, *Voter Models on Heterogeneous Networks*, Physical Review E **77** (2008), 041121. https://pmc.ncbi.nlm.nih.gov/articles/PMC2471880/
- D. Mohan, P. Prałat, *Asynchronous Majority Dynamics on Binomial Random Graphs*, arXiv:2309.04691, first publicly posted 2023-09-09. https://arxiv.org/html/2309.04691v2
