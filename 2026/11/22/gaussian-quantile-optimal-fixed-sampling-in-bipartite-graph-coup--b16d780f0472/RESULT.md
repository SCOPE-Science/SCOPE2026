# Gaussian-quantile optimal fixed sampling in bipartite graph coupon coverage

## Finding

Let \(K_{a,b}\) be the complete bipartite graph with nonempty vertex classes \(A,B\) of respective sizes \(a,b\). At each independent sampling round, choose a vertex in \(A\) with total probability \(q\in(0,1)\), and one in \(B\) otherwise; within the selected class the vertex may be chosen arbitrarily. If that vertex has an uncovered neighbor, cover one such neighbor (with any choice rule). Initially every vertex is uncovered. Let \(T_{a,b}(q)\) be the number of rounds to cover the graph, and put \(N=a+b\).

For every integer \(t\ge N\), the **full exact completion-time distribution** is
\[
 \Pr\{T_{a,b}(q)\le t\}=\sum_{j=b}^{t-a}\binom tj q^j(1-q)^{t-j},
\]
with probability zero for \(t<N\). If \(X\sim\operatorname{Bin}(N,q)\), then
\[
 \mathbb E T_{a,b}(q)=N+\frac{\mathbb E(X-b)_+}{1-q}+\frac{\mathbb E(b-X)_+}{q}.
\]

Consider any integer sequences \(a_N,b_N\ge1\) with \(a_N+b_N=N\to\infty\) and \(a_N/N\to\alpha\in(0,1)\). Write \(\beta=1-\alpha\), \(\beta_N=b_N/N\), \(\sigma=\sqrt{\alpha\beta}\), and let \(\Phi,\phi\) denote the standard normal distribution function and density. For each fixed real \(u\), choose \(q_N=\beta_N+u/\sqrt N\) (for sufficiently large \(N\)). With \(Z\sim N(0,1)\), put \(Y_u=u+\sigma Z\). Then
\[
 \frac{T_{a_N,b_N}(q_N)-N}{\sqrt N}\ \Rightarrow\ W_u:=\frac{(Y_u)_+}{\alpha}+\frac{(-Y_u)_+}{\beta},
\qquad
 \frac{\mathbb E T_{a_N,b_N}(q_N)-N}{\sqrt N}\longrightarrow F(u):=\mathbb E W_u.
\]
The law is explicit: for \(r\ge0\),
\[
 \Pr(W_u\le r)=\Phi\left(\frac{\alpha r-u}{\sigma}\right)-\Phi\left(\frac{-\beta r-u}{\sigma}\right).
\]

Every exact minimizer \(q_N^*\in(0,1)\) of the expected completion time over **fixed, independent class-sampling probabilities** has the same sharp expansion
\[
 q_N^*=\beta_N+\frac{\sigma\Phi^{-1}(\alpha)}{\sqrt N}+o(N^{-1/2}),
\qquad
 \min_{q\in(0,1)}\mathbb E T_{a_N,b_N}(q)
 =N+\frac{\phi(\Phi^{-1}(\alpha))}{\sigma}\sqrt N+o(\sqrt N).
\]
If instead a vertex is sampled uniformly from all \(N\) vertices, then \(q_N=a_N/N\), and for \(\alpha\ne1/2\),
\[
 \frac{\mathbb E T_{a_N,b_N}(a_N/N)}N\longrightarrow
 \max\left\{\frac\alpha\beta,\frac\beta\alpha\right\}>1.
\]
Thus a fixed, size-aware choice of source-class probabilities changes the waste from linear to square-root order for asymptotically unequal classes. Even within the optimal square-root scale, the uniquely optimal shift is generally **not** zero: it is governed by a Gaussian quantile.

## Assumptions and scope

All sampling rounds are independent, with the same class probability \(q\) throughout a run. The selected vertex and selected uncovered neighbor can be chosen by any rule within the chosen class because, on a complete bipartite graph, each successful selection of class \(A\) covers exactly one previously uncovered vertex of \(B\), and conversely. The optimum is restricted to the family of fixed, i.i.d. source-class probabilities; history-dependent policies are a different problem. The asymptotic assertions require both classes to occupy positive limiting fractions.

## Proof

**Exact law.** Let \(S_t\) be the number of rounds through time \(t\) that select a source in \(A\). Then \(S_t\sim\operatorname{Bin}(t,q)\) and the number of covered vertices in \(B\) is exactly \(\min(S_t,b)\); in \(A\) it is exactly \(\min(t-S_t,a)\). Hence covering is complete by \(t\) exactly if \(b\le S_t\le t-a\). This gives the binomial CDF displayed above.

After the first \(N\) rounds let \(X=S_N\). If \(X\ge b\), all \(B\) vertices are covered and exactly \(X-b\) vertices of \(A\) remain uncovered. These need \(X-b\) future source selections in \(B\), each independently occurring with probability \(1-q\); their conditional expected additional time is \((X-b)/(1-q)\). If \(X<b\), the additional time has conditional expectation \((b-X)/q\). The exact expectation follows, including the case \(X=b\).

**Local limiting law.** Put \(q_N=\beta_N+u/\sqrt N\) and \(t_N=N+\lfloor r\sqrt N\rfloor\). For any \(r\ge0\), the exact CDF gives
\[
 \Pr\{T_{a_N,b_N}(q_N)\le t_N\}=\Pr\{b_N\le S_{t_N}\le b_N+\lfloor r\sqrt N\rfloor\}.
\]
The triangular-array binomial central limit theorem yields
\[
 \frac{S_{t_N}-b_N}{\sqrt N}\Rightarrow N(u+r\beta,\sigma^2).
\]
The displayed probability therefore tends to \(\Phi((\alpha r-u)/\sigma)-\Phi((-\beta r-u)/\sigma)\), precisely the CDF of \(W_u\); the limit has no atoms. At \(r<0\) both variables have zero probability. The expectation formula and the binomial central limit theorem give the mean limit: the standardized binomial variables have uniformly bounded second moments, so their positive and negative parts are uniformly integrable, and \(q_N\to\beta\in(0,1)\).

**Optimization.** For \(z=u/\sigma\), direct normal integration gives
\[
 F(u)=\frac{\sigma\phi(z)+u\Phi(z)}{\alpha}
      +\frac{\sigma\phi(z)-u\Phi(-z)}{\beta},
\qquad
 F'(u)=\frac{\Phi(z)}\alpha-\frac{\Phi(-z)}\beta,
\qquad
 F''(u)=\frac{\phi(z)}{\sigma\alpha\beta}>0.
\]
Thus \(F\) has exactly one minimizer \(u_*=\sigma\Phi^{-1}(\alpha)\). At this point the two terms involving \(u\) cancel and \(F(u_*)=\phi(\Phi^{-1}(\alpha))/\sigma\).

For each finite \(N\), \(q\mapsto\mathbb E T_{a_N,b_N}(q)\) is continuous on \((0,1)\), and it diverges at both endpoints because \(T\) must include at least \(b_N\) source-\(A\) and at least \(a_N\) source-\(B\) selections. Thus an exact minimizer exists. Choosing \(q=\beta_N\) in the expectation identity and applying Cauchy–Schwarz proves \(\min_q\mathbb E T\le N+O(\sqrt N)\). On the other hand, the necessary quotas give
\[
 \mathbb E T_{a_N,b_N}(q)\ge\max\left\{\frac{b_N}{q},\frac{a_N}{1-q}\right\}.
\]
Consequently every exact minimizer satisfies \(q_N^*=\beta_N+O(N^{-1/2})\). Along any subsequence where \(\sqrt N(q_N^*-\beta_N)\to u\), the already-proved mean limit applies, and comparison to every fixed alternative \(\beta_N+v/\sqrt N\) shows \(F(u)\le F(v)\) for all \(v\in\mathbb R\). Strict convexity forces \(u=u_*\). This proves the minimizer expansion and the optimal expected-time expansion for the entire sequence.

**Uniform vertex sampling.** With \(q_N=a_N/N\), the law of large numbers gives \((S_N-b_N)/N\to\alpha-\beta\) in \(L^1\). Substituting into the exact mean formula and using denominators bounded away from zero yields the stated ratio.

## Verification

Run `python3 checker.py` from this package. It computes exact rational expected hitting times by an independent two-dimensional absorbing-state recursion and compares them to the binomial positive-part expression for all class sizes from one to seven and five rational sampling probabilities. It also computes exact deadline CDFs from a finite-state Markov recursion and compares them against the binomial formula. The recorded execution returned `PASS exact mean and all deadline CDF checks: 1470`. These finite checks corroborate the algebra but are not substitutes for the all-size proof or the asymptotic argument.

Independent numerical minimizations (not required to run the standalone checker) at proportions \(\alpha=0.2,0.5,0.75\) and sizes \(N=100,500,2000,8000\) showed convergence of the scaled optimal offset and expected cost to the stated Gaussian-quantile expressions. The proof, not the numerical evidence, establishes the limits.

## Relationship to prior work

Deng and Wang, *Extremal graphs for Alon's graph coupon-collector conjecture* (arXiv:2611.11345v1, 8 November 2026), study the uniform-source graph covering process and prove fixed-degree graph extremality. Their Corollary 4.2 obtains the fixed-\(d\) completion-time tail of \(K_{d,d}\); their Proposition 5.1 reduces unions of such components to repeated coupon collection; their Proposition 5.2 obtains a square-root **lower bound** from balanced quotas for a union of two cliques. Those statements do not treat optimization over fixed asymmetric source-class weights, the growing-\(a,b\) Gaussian-quantile bias correction, or the full optimized completion-time profile. These known reductions and bounds are credited rather than claimed anew.

Dimitrov and Plaxton, *Optimal Cover Time for a Graph-Based Coupon Collector Process* (Journal of Discrete Algorithms 19, 2013, pp. 39–51), consider uniform source vertices and different neighbor-choice algorithms and bounds on general graphs; no fixed-source-class probability optimization or its growing-size quantile law was located in the inspected relevant sections. Related published work on biased random **walk** coverage of complete bipartite graphs addresses a different mechanism: a walk's next source is constrained by its current position rather than independently selectable at every round.

## Limitations

The optimizer is over static i.i.d. class weights only; adaptive, periodic or other dependent vertex-selection mechanisms may cover sooner. The result applies to complete bipartite graphs with both class proportions bounded away from zero; neither sparsely sized parts nor arbitrary irregular graphs are classified. The asymptotic rate is shown without an explicit uniform error bound. Broader unidentified two-quota scheduling or biased-sampling theorems might imply this result; literature searches do not prove novelty. The mathematical assessment here is not an independent validation.

## References

- X. Deng and G. Wang, *Extremal graphs for Alon's graph coupon-collector conjecture*, arXiv:2611.11345v1, first submitted 8 November 2026. https://arxiv.org/abs/2611.11345
- N. B. Dimitrov and C. G. Plaxton, *Optimal Cover Time for a Graph-Based Coupon Collector Process*, Journal of Discrete Algorithms **19** (2013), 39–51. https://www.cs.utexas.edu/~plaxton/pubs/2013/jda.pdf
- D. J. Newman and L. Shepp, *The Double Dixie Cup Problem*, American Mathematical Monthly **67** (1960), 58–61. Cited for the related repeated coupon-collector setting, not for the new optimizing theorem.
