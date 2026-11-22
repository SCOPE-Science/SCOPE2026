# A logarithmic slow-vertex crossover in complete-graph SI flooding

## Finding
Consider the irreversible continuous-time susceptible–infected process described below on the complete graph with \(N\ge3\) vertices. One vertex has reduced *susceptibility*, with incoming contacts slowed by a factor \(\rho_N\in(0,1]\). If \(T_N\) is the time when every vertex becomes infected and \(L_N\) is the event that the slow vertex becomes infected strictly last, then, at every finite size,
\[
\Pr(L_N)=\prod_{j=1}^{N-2}\frac{j}{j+\rho_N}
=\frac{\Gamma(N-1)\Gamma(1+\rho_N)}{\Gamma(N-1+\rho_N)}.
\]
When \(\rho_N\log N\to c\in(0,\infty)\), for a unit-mean exponential random variable \(E\),
\[
\frac{T_N}{\log N}\ \Longrightarrow\ \max\left\{2,1+\frac{E}{c}\right\},\qquad
\Pr(L_N)\longrightarrow e^{-c},\qquad
\frac{\mathbb E T_N}{\log N}\longrightarrow 2+\frac{e^{-c}}{c}.
\]
Equivalently, the limit distribution has cumulative distribution function \(F_c(x)=0\) for \(x<2\), and \(F_c(x)=1-e^{-c(x-1)}\) for \(x\ge2\). Its atom at \(2\) has mass \(1-e^{-c}\), and its remaining probability lies above \(2\) in an exponential tail. The boundary regimes have sharp contrasting behavior: if \(\rho_N\log N\to0\), then \(T_N/\log N\to+\infty\) in probability and \(\Pr(L_N)\to1\); if \(\rho_N\log N\to+\infty\), then \(T_N/\log N\to2\) in probability and \(\Pr(L_N)\to0\).

## Assumptions and scope
The initial infected vertex is one of the \(N-1\) ordinary vertices, and the slow vertex is initially susceptible. Each infected–susceptible ordinary pair transmits at rate \(1/N\), and each infected ordinary vertex transmits to the slow susceptible vertex at rate \(\rho_N/N\). After the slow vertex becomes infected, it transmits to each susceptible ordinary vertex at rate \(\rho_N/N\). All contact clocks are independent Poisson processes, and infection is permanent. There is no recovery, external field, or spontaneous infection. The bounds on \(\rho_N\) ensure rates are positive and at most the ordinary rate. All limiting statements quantify over any sequence \(\rho_N\in(0,1]\) satisfying the named hypothesis; \(N\to\infty\). Logarithms are natural.

The random variable \(T_N\) is full infection time, not the time to infect the slow vertex. The event \(L_N\) means the slow vertex is the unique last infection (simultaneous transitions have probability zero). The exact identity also holds for any fixed \(\rho_N>0\), even outside the restricted asymptotic range.

## Proof
**1. Ordinary baseline and slow-clock representation.** Set \(m=N-1\). Ignore all transmissions involving the slow vertex, and write \(K_N^0(t)\) for the number of ordinary infected vertices, starting at one. It is a pure-birth chain on \(\{1,\ldots,m\}\) with rate \(k(m-k)/N\) from \(k\) to \(k+1\). Conditional on this entire baseline trajectory, the time \(S_N\) of the first infection of the slow vertex has survival probability
\[
\Pr(S_N>t\mid K_N^0)=\exp\left(-\frac{\rho_N}{N}\int_0^t K_N^0(s)\,ds\right).
\]
This representation is exact because before infection of the distinguished vertex its slow incoming arrows do not change ordinary infections. It can be realized from an independent \(E\sim\mathrm{Exp}(1)\) by declaring the slow infection to occur when the integrated hazard first reaches \(E\).

**2. Exact last-vertex identity.** On \(L_N\), the entire ordinary population becomes infected before the slow vertex. At ordinary infected count \(k\in\{1,\ldots,m-1\}\), the race consists of ordinary infection at rate \(k(m-k)/N\) and slow infection at rate \(\rho_N k/N\). The probability that ordinary infection wins is \((m-k)/(m-k+\rho_N)\). Independence of successive exponential races yields
\[
\Pr(L_N)=\prod_{k=1}^{m-1}\frac{m-k}{m-k+\rho_N}=\prod_{j=1}^{m-1}\frac{j}{j+\rho_N}.
\]
The gamma identity follows from the gamma recurrence. For \(0<\rho_N\le1\), expanding \(\sum_{j=1}^{m-1}\log(1+\rho_N/j)\) gives
\[
\log\Pr(L_N)=-\rho_N\log N+O(\rho_N+\rho_N^2),
\]
where the bound is uniform in \(N\) and \(\rho_N\). Therefore the last-vertex probability converges to \(e^{-c}\) when \(\rho_N\log N\to c\in[0,\infty)\), and to zero when this product diverges.

**3. Macroscopic ordinary infection curve.** For every fixed \(x\ge0\),
\[
\frac{K_N^0(x\log N)}{N}\ \xrightarrow{\Pr}\ \mathbf1_{\{x>1\}}
\]
when \(x\ne1\). For \(x<1\), the pure-birth rate is bounded above by \(k\); thus \(\mathbb E K_N^0(t)\le e^t\), and Markov's inequality applies. For \(x>1\), let \(H_{N,\delta}\) be the hitting time of at least \((1-\delta)m\) infected ordinary vertices, for fixed \(\delta\in(0,1)\). Its waiting times are independent exponentials with parameters \(k(m-k)/N\) for the corresponding \(k\), and their sums satisfy
\[
\mathbb E H_{N,\delta}=\log N+O_{\delta}(1),\qquad
\operatorname{Var}(H_{N,\delta})=O_{\delta}(1).
\]
Chebyshev's inequality implies \(K_N^0(x\log N)/N\to1\) in probability. Monotonicity, boundedness, and upper/lower Riemann sums consequently show, for each \(x\ge0\),
\[
\frac{1}{N\log N}\int_0^{x\log N}K_N^0(s)\,ds\ \xrightarrow{\Pr}\ (x-1)_+.
\]

**4. Slow-vertex limit and weak/strong boundaries.** Conditional survival from step 1, the preceding integrated-hazard limit, and bounded convergence yield, whenever \(\rho_N\log N\to c\in(0,\infty)\),
\[
\Pr\left(\frac{S_N}{\log N}>x\right)\longrightarrow
\exp\{-c(x-1)_+\}.
\]
The limit is the law of \(1+E/c\). For \(\rho_N\log N\to0\), its conditional cumulative hazard vanishes uniformly on every fixed logarithmic time interval, so \(S_N/\log N\to+\infty\) in probability. When \(\rho_N\log N\to+\infty\), the same integrated-hazard estimate implies \(S_N/\log N\to1\) in probability (for the upper bound, use the positive limiting integrated mass at every \(x>1\)); the lower bound uses the first-moment estimate before \(x=1\).

**5. Ordinary completion is on the universal \(2\log N\) scale.** Let \(U_N\) be the time when all ordinary vertices are infected in the true process. Coupling by the graphical infection arrows sandwiches it between the ordinary-only completion time \(U_N^0\) and the completion time \(U_N^+\) when the slow vertex is forced infected at time zero:
\[
U_N^+\le U_N\le U_N^0.
\]
The bounding pure-birth chains have respective rates \((k+\rho_N)(m-k)/N\) and \(k(m-k)/N\). The latter obeys
\[
\mathbb E U_N^0=\frac{2N}{m}H_{m-1}=2\log N+O(1),\qquad
\operatorname{Var}(U_N^0)=O(1).
\]
Because \(0<\rho_N\le1\), \(U_N^+\) is stochastically at least the same process with \(\rho_N=1\), whose expectation is \(2\log N+O(1)\) and variance \(O(1)\). Hence \(U_N/\log N\to2\) in probability, without requiring independence from \(S_N\). Now \(T_N=\max\{U_N,S_N\}\), proving the distributional statements including the two boundary regimes by the continuous mapping theorem and convergence in probability.

**6. Convergence of the mean in the critical window.** Let \(H_N\) be the baseline time to infect at least half the ordinary vertices. As in step 3, \(\mathbb E H_N=\log N+O(1)\) and \(\operatorname{Var}(H_N)=O(1)\). After \(H_N\), the slow-vertex hazard is at least \(\rho_N/3\) for all sufficiently large \(N\). Consequently \(S_N\) is stochastically dominated by \(H_N+Z_N\), where \(Z_N\) is an exponential waiting time of rate \(\rho_N/3\) (the stochastic domination is sufficient, independence need not be assumed for the actual process). When \(\rho_N\log N\to c>0\), \(\sup_N\mathbb E[(S_N/\log N)^2]<\infty\) apart from finitely many irrelevant initial \(N\). The same holds for \(U_N^0/\log N\) and thus \(T_N/\log N\). Uniform integrability now gives
\[
\lim_{N\to\infty}\frac{\mathbb E T_N}{\log N}
=\mathbb E\max\{2,1+E/c\}
=2+\int_1^\infty e^{-cu}\,du
=2+\frac{e^{-c}}c.
\]

## Verification
The companion `weak_vertex_verifier.py` implements the exact finite-state mean-completion equations in two different recursion organizations and checks their equality using `fractions.Fraction` for all \(3\le N\le13\) and \(\rho\in\{1/7,1,3/2,7/3\}\): 44 exact-rational comparisons. It also checks the last-vertex product against sequential exponential-race equations and tests the uniform-rate identity \(\Pr(L_N)=1/(N-1)\). Running `python3 weak_vertex_verifier.py` prints `PASS` after all assertions succeed. Illustrative large-size product evaluations accompany these assertions; they are not proofs of the asymptotic limit.

The proof's critical analytical steps are the ordinary birth-chain concentration, integrated-hazard limit and uniform-integrability bound; finite computations verify small cases but cannot replace those arguments.

## Relationship to prior work
Janson establishes the universal two-logarithm complete-graph flooding scale with independent identically distributed edge passage times. That baseline corresponds to no distinguished low-susceptibility vertex and does not furnish the critical \(1/\log N\) marked-receiver crossover. Aalto and Leskelä study populations with heterogeneous transmitter contact rates and passive receivers; their contact dynamics select recipients uniformly, whereas the present slow vertex has reduced incoming rates on *all incident edges*. Peterson studies a rank-one vertex-weighted complete-graph contact process with precisely the same potential edge-rate factorization, but with recovery at rate one and extinction/quasi-stationary observables; those results do not give the irreversible all-infected completion time. Leskelä and Ngo treat sparse random graph first-passage paths with additive boundary delays, not the dense graph's rate-weakened recipient. A related study of an asynchronous double-star rumor process produces a qualitatively analogous mixed last-vertex limit on a different graph, but its structural conclusion does not imply the present complete-graph law.

These comparisons support a specific difference in assumptions and conclusions, not a claim of exhaustive historical priority. The birth-process method itself is classical, and the homogeneous baseline and general hazard construction are not claimed as new.

## Limitations
Only irreversible exponential-contact SI dynamics with a single distinguished slow vertex, a single ordinary initial seed, and complete-graph connectivity are covered. No constant-order fluctuation law, quantitative convergence rate, non-exponential passage-time universality, several-slow-vertex law or sparse-network extension is proved. The present literary comparison is substantial but not exhaustive; an earlier equivalent or stronger heterogeneity theorem may exist. Scientific review of this result has not been independently audited.

## References
1. S. Janson, *One, Two and Three Times \(\log n/n\) for Paths in a Complete Graph with Random Weights*, Combinatorics, Probability and Computing **8** (1999), 347–361. https://doi.org/10.1017/S0963548399003892 ; accessible manuscript: https://www.stat.berkeley.edu/~aldous/260-FMIE/Papers/janson_123.pdf . Published online 1999-07-01.
2. P. Aalto and L. Leskelä, *Information Spreading in a Large Population of Active Transmitters and Passive Receivers*, SIAM J. Appl. Math. **75** (2015), 1965–1982. https://doi.org/10.1137/141001469 ; open repository manuscript https://acris.aalto.fi/ws/portalfiles/portal/32111297/141001469.pdf ; first arXiv posting https://arxiv.org/abs/1412.7563 (2014-12-23).
3. J. Peterson, *The Contact Process on the Complete Graph with Random Vertex-Dependent Infection Rates*, Stochastic Processes and their Applications **121** (2011), 609–629. https://arxiv.org/abs/1005.0810 ; posted 2010-05-05.
4. L. Leskelä and H. Ngo, *First Passage Percolation in Sparse Random Graphs with Boundary Weights*, Journal of Applied Probability **56** (2019), 458–471. https://arxiv.org/abs/1806.09568 ; posted 2018-06-25. Supporting comparison only; published after the focal-source window.
