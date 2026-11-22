# A Gaussian-width quorum reversal between shared-risk response and independent randomization

## Finding
Fix an integer group size \(N\ge2\). Agents independently have an adaptive type with probability \(x\in(0,1)\), and otherwise defect unconditionally. A realized collective-loss probability \(R\in[0,1]\) is observed perfectly by the adaptive agents in the **shared-risk protocol**, which makes them contribute precisely when \(R\ge\tau\). Set \(s=\Pr(R\ge\tau)\in(0,1)\), \(\mu=\mathbb E R>0\), and \(h=\mathbb E[R\mathbf{1}_{\{R\ge\tau\}}]/\mu\). Assume \(s<h<1\). In the **independent-randomization protocol**, each adaptive agent instead draws an independent Bernoulli decision with probability \(s\), independently of the true \(R\); thus the protocols have the same expected number of contributions and the same stipulated per-agent monitoring and contribution charges. The independent protocol is an explicitly *uninformative benchmark*, not an equally accurate observation method.

For any integer quorum \(1\le m\le N\), define the binomial tail
\[
B_{N,m}(p)=\sum_{j=m}^{N}\binom Nj p^j(1-p)^{N-j},\qquad q=sx.
\]
The two group-achievement probabilities are \(A_{\mathrm{shared}}(m)=sB_{N,m}(x)\) and \(A_{\mathrm{ind}}(m)=B_{N,m}(q)\). Their positive ratio
\[
L_m=\frac{sB_{N,m}(x)}{B_{N,m}(q)}
\]
is **strictly increasing** in \(m\), with \(L_1<1<L_N\). Consequently, the achievement ordering changes at most once as the quorum rises.

If missing the quorum causes loss of the endowment with probability \(R\), and the endowment is \(b>0\), the difference in expected net payoff per agent (shared minus independent) is exactly
\[
\Delta W_m=b\mu\big[hB_{N,m}(x)-B_{N,m}(q)\big].
\]
Both protocols incur the same average contribution charge \(c q\) and the same average observation charge \(d x\), for any prescribed \(c,d\ge0\). The welfare ordering therefore changes at most once and no later than achievement does.

Writing \(\Phi\) for the standard normal distribution function and \(\sigma=\sqrt{q(1-q)}\), define \(m_A(N)\) as the first quorum with \(L_m\ge1\), and \(m_W(N)\) as the first quorum with \((h/s)L_m\ge1\). For fixed \(x,s,h\) with \(0<s<h<1\),
\[
\begin{aligned}
m_A(N)&=Nq+\sigma\Phi^{-1}(1-s)\sqrt N+o(\sqrt N),\\
m_W(N)&=Nq+\sigma\Phi^{-1}(1-h)\sqrt N+o(\sqrt N).
\end{aligned}
\]
Hence the number of integer quorums for which **shared sensing lowers achievement yet raises expected net welfare** is
\[
\sigma\big[\Phi^{-1}(1-s)-\Phi^{-1}(1-h)\big]\sqrt N+o(\sqrt N),
\]
with a strictly positive coefficient. This discordance band lies strictly below the full quorum for all sufficiently large \(N\).

For the uniform-risk case \(R\sim U[0,1]\), \(s=1-\tau\), \(\mu=1/2\), and \(h=1-\tau^2\). At \(N=6\), \(m=2\), \(x=\tau=1/2\), shared sensing lowers achievement by exactly \(85/4096\) but increases expected net payoff by exactly \(827b/8192\).

## Assumptions and scope
The group is independently sampled at the level of strategic types; type labels are Bernoulli with parameter \(x\). Within one group, the loss probability \(R\) is shared across players, and conditional on failure the expected remaining endowment of each agent is \(b(1-R)\). Contributions cost \(c\) irrespective of whether failure occurs. Observation costs \(d\) apply to adaptive types irrespective of the realized signal. The independent protocol deliberately discards information about realized risk while preserving each adaptive agent's ex-ante contribution frequency; it is not claimed to isolate correlation from informativeness. No equilibrium, endogenous imitation, or finite fixed-composition population is assumed. Full quorum \(m=N\) is included as a natural mathematical boundary; the asymptotic discordance band is entirely within \(m<N\), the original paper's admissible quorum range.

## Proof
**1. Count laws and equal resource costs.** In the shared protocol the common threshold event \(H=\mathbf{1}_{\{R\ge\tau\}}\) has probability \(s\). Conditional on \(H=1\), the number of contributors is \(\operatorname{Bin}(N,x)\); conditional on \(H=0\), it is zero. The independent protocol gives \(\operatorname{Bin}(N,q)\) with \(q=sx\). Both expected counts are \(Nq\), and each has average adaptive-type frequency \(x\). The claimed achievement and cost identities follow.

**2. Strict single-crossing of the achievement ratio.** For each positive count \(j\in\{1,\dots,N\}\), the ratio of the shared to independent point masses is
\[
r_j=\frac{s\binom Nj x^j(1-x)^{N-j}}{\binom Nj (sx)^j(1-sx)^{N-j}}
=s^{1-j}\left(\frac{1-x}{1-sx}\right)^{N-j},
\qquad
\frac{r_{j+1}}{r_j}=\frac{1-sx}{s(1-x)}>1.
\]
The tail ratio \(L_m\) is a weighted average of \(r_j\) for \(j\ge m\), with strictly positive weights equal to the independent point masses. Removing the lowest, strictly smaller ratio increases this average, so \(L_m<L_{m+1}\). At the upper endpoint \(L_N=s^{1-N}>1\). For the lower endpoint, the probability of no contribution under the shared scheme is \((1-s)+s(1-x)^N\), whereas under independent randomization it is \((1-sx)^N\). Strict Jensen convexity of \(z\mapsto (1-xz)^N\) for \(N\ge2\) gives the former as strictly larger; thus \(L_1<1\).

**3. Exact welfare comparison.** The saved expected loss per person, relative to an otherwise failed group, is \(b\mathbb E[R\mathbf{1}_{\{C\ge m\}}]\). For shared sensing this is \(b\mu h B_{N,m}(x)\). For independent randomization, the contribution count is independent of \(R\), and the saving is \(b\mu B_{N,m}(q)\). Costs cancel by step 1, proving the welfare formula. Its sign is that of \((h/s)L_m-1\). Since \(h/s>1\), the welfare crossing cannot occur later than the achievement crossing.

**4. Gaussian limits and the width.** Put \(q=sx\in(0,x)\). For a fixed real \(z\), take integer \(m_N=Nq+z\sqrt N+O(1)\). The law of large numbers with a standard exponential binomial tail bound gives \(B_{N,m_N}(x)\to1\), while the binomial central limit theorem gives
\[
B_{N,m_N}(q)\longrightarrow1-\Phi(z/\sigma).
\]
Thus \(L_{m_N}\to s/[1-\Phi(z/\sigma)]\). The two strict crossing conditions become \(\Phi(z/\sigma)>1-s\) and \(\Phi(z/\sigma)>1-h\), respectively. Sandwiching the discrete first-crossing indices between any two constants on opposite sides of each quantile proves both displayed \(o(\sqrt N)\) expansions. Since \(h>s\), the quantiles are distinct, and the integer count of the intervening strict-reversal quorums has the claimed positive asymptotic width; possible exact equality at one endpoint changes the count by at most two.

**5. Rational witness.** At \(N=6\), \(m=2\), \(x=\tau=1/2\), let \(q=1/4\). Then \(B_{6,2}(1/2)=57/64\) and \(B_{6,2}(1/4)=1909/4096\). Shared and independent achievement probabilities are \(57/128=1824/4096\) and \(1909/4096\), respectively. The difference in saved risk-weighted mass is \((3/4)(57/64)-1909/4096=827/4096\), and multiplication by \(b\mu=b/2\) yields \(827b/8192\).

## Verification
Run `python checker.py` with Python 3. The stand-alone checker uses exact rational arithmetic and independent configuration enumeration. It passed 560 quota comparisons across 112 parameter combinations for the uniform model; those check mass, first and second moments, strict tail-ratio ordering, and both achievement and welfare identities. Another 243 exact finite-support nonuniform-risk cases passed independent enumeration. The six-agent example is checked as an exact fraction. Finite tests are not the proof of strict monotonicity for all sizes or of the Gaussian asymptotics; those follow from the arguments above.

## Relationship to prior work
Zhou, Han, Chen and Szolnoki (2026) introduce risk-threshold adaptive contributors under a shared uniformly distributed collective-risk variable and calculate finite-population payoffs and group achievement. Fernández Domingos, Ichinose, Tateishi and Lenaerts (2026) study purchasing and relaying information about an uncertain *quorum*, rather than risk-conditioned common versus uninformed independent decisions. De Jaegher (2020) analyzes evolutionary incentives and pivotal binomial probabilities for threshold public goods. The Bernoulli-mixture literature, including the 2014 study cited below, supplies general tools for exchangeable dependent success counts but does not, in the inspected material, give this pair of outcome-ordering cutoffs and their distinct Gaussian-quorum windows. Likelihood-ratio tail averaging and binomial central limits are standard mathematical ingredients and are not claimed as inventions.

## Limitations
No claim concerns equilibria, evolutionary stability, optimal signal acquisition, measured behavioral response, or superiority over *equally informative* independent signals. The benchmark is expressly uninformative. Costs are stipulated equal and group composition is Bernoulli, not finite fixed counts. The result is a mathematical comparison of protocols, not evidence of a real-world benefit. A stronger priority claim than the literature-bounded comparison is not established; some dependent-Bernoulli and public-information literature may contain equivalent special cases. The binomial central limit result concerns fixed \(x,s,h\) as \(N\to\infty\), not regimes in which those quantities approach boundary values with \(N\).

## References
1. Chuanzhi Zhou, Ju Han, Xiaojie Chen, Attila Szolnoki (2026). *Evolutionary dynamics of collective-risk social dilemma game with risk uncertainty and adaptive strategy*, arXiv:2611.07627v1. https://arxiv.org/abs/2611.07627
2. Elias Fernández Domingos, Genki Ichinose, Wakaba Tateishi, Tom Lenaerts (2026). *The Conditional Value of Costly Information in Collective-Risk Dilemmas*, arXiv:2610.33895v1. https://arxiv.org/abs/2610.33895
3. Kris De Jaegher (2020). *High thresholds encouraging the evolution of cooperation in threshold public-good games*. Scientific Reports 10, 5863. https://doi.org/10.1038/s41598-020-62626-3
4. *Sum of Bernoulli Mixtures: Beyond Conditional Independence* (2014). https://doi.org/10.1155/2014/838625
