# Poisson terminal infections and a weak-rim crossover on exponential first-passage wheels

## Finding
On a wheel with \(n\ge5\) rim vertices, start only the hub infected. In the irreversible model with spoke transmission rate \(\alpha>0\) and rim transmission rate \(\beta_n\ge0\), let \(N_n(t)\) count susceptible rim vertices at time \(t\) and let \(T_n\) be the time when the last becomes infected. Write \(G\) for the standard Gumbel law with cdf \(\exp(-e^{-x})\).

For fixed \(\alpha,\beta>0\) with \(\beta_n=\beta\), put \(a=\alpha+2\beta\) and \(t_n(x)=(\log n+2\beta/\alpha+x)/a\). For each real \(x\),
\[
N_n(t_n(x))\Rightarrow\operatorname{Pois}(e^{-x}),\qquad
aT_n-\log n-2\beta/\alpha\Rightarrow G.
\]
If instead \(\beta_n\log n\to c\in[0,\infty)\), then for each real \(x\),
\[
N_n((\log n+x)/\alpha)\Rightarrow\operatorname{Pois}(e^{-x-2c/\alpha}),\qquad
\alpha T_n-\log n+2c/\alpha\Rightarrow G.
\]
This identifies the rate scale \(1/\log n\) for an order-one shift from the star window, where \(\beta_n=0\) gives \(\Pr(T_n\le t)=(1-e^{-\alpha t})^n\) for \(t\ge0\). If \(\beta_n\to0\) but \(\beta_n\log n\to\infty\), then \(\alpha T_n-\log n\to-\infty\) in probability.

## Assumptions and scope
The rim is a simple undirected cycle. Each edge from an infected to a susceptible vertex transmits after an independent exponential wait of the given rate. Equivalently give each spoke an independent \(\operatorname{Exp}(\alpha)\) weight and each rim edge an independent \(\operatorname{Exp}(\beta_n)\) weight (infinite if \(\beta_n=0\)). Infection times are distances from the hub in this first-passage metric: an edge's wait is first needed when one endpoint becomes infected, so its independent exponential clock gives the stated Markov rates. Equivalently again, the rim counting process comes from the two-sided discrete Bass model on a circle with external rate \(p=\alpha\) and total neighbor influence \(q=2\beta_n\); each infected neighbor contributes \(q/2\). The claims concern terminal-window counts and completion times, not the mean adoption curve or a new exact finite-circle marginal formula.

## Proof

### One-point survival on the infinite line
Put independent exponential seed delays of rate \(\alpha\) at all sites on the infinite line, with independent nearest-neighbor edge weights of rate \(\beta\). Along one ray from the target, the distances to successive sites are the arrival times \(S_k\) of a rate-\(\beta\) Poisson process. Conditional on the edge weights, protection from that ray requires each seed delay to exceed \((t-S_k)_+\). Thus the one-ray protection probability is
\[
J_\beta(t)=\mathbb E\exp[-\alpha\textstyle\sum_{k\ge1}(t-S_k)_+]
=\exp[-\beta t+(\beta/\alpha)(1-e^{-\alpha t})],
\]
by the Poisson Laplace functional, integrating \(1-e^{-\alpha(t-s)}\) on \([0,t]\). For \(\beta=0\), take \(J_0=1\). The two independent rays and the seed at the target give
\[
p_\infty(t)=e^{-\alpha t}J_\beta(t)^2
=\exp[-(\alpha+2\beta)t+(2\beta/\alpha)(1-e^{-\alpha t})]. \tag{1}
\]
This is the infinite-line marginal. The calculation is included to make the tail argument self-contained; circle marginal laws are already treated in [1,2].

### Local truncation and pair protection
Let \(R=\lceil(\log n)^2\rceil\). Let \(X_i\) indicate that vertex \(i\) is still protected when only paths along either of its first \(R\) rim edges and the corresponding seed delays are used. For large \(n\), \(4R<n\), so the two radius-\(R\) rays use the same law as on the line. On the circle, any omitted successful path must use at least \(R\) rim edges along one ray into the target by time \(t\). The same holds for an omitted successful infection on the line. Thus the error probability of either one-point truncation is bounded by \(2\epsilon_n\), where \(\epsilon_n=\Pr(\operatorname{Pois}(\beta_n t)\ge R)\). In all windows used here \(\beta_n t=O(\log n)\), and the Poisson Chernoff bound gives \(n^K\epsilon_n\to0\) for every fixed \(K\). In particular, if \(p_n=\Pr(X_i=1)\), then \(p_n=p_\infty(t)+O(\epsilon_n)\) with \(\beta=\beta_n\) in (1), and the exact and truncated counts agree with probability at least \(1-2n\epsilon_n\).

Let \(i\ne j\) have cyclic distance at most \(2R\). In the longer complementary arc take the outward radius-\(R\) ray from each target. These two rays are disjoint because the arc length exceeds \(2R\); their non-root seed delays, edge weights and the two root seeds are all independent. If both vertices survive under truncation, their own seeds exceed \(t\) and their respective outward rays are protected. Writing \(J_{\beta,R}(t)\) for the one-ray protection probability keeping only the first \(R\) sites,
\[
\Pr(X_i=X_j=1)\le e^{-2\alpha t}J_{\beta_n,R}(t)^2
\le e^{-2\alpha t}(J_{\beta_n}(t)+\epsilon_n)^2. \tag{2}
\]
The indicators have a dependency graph obtained by joining vertices at cyclic distance at most \(2R\): each indicator is independent of the collection outside its own graph neighborhood, by disjoint underlying weights.

### Terminal counts and completion
For fixed \(\beta>0\), at \(t_n(x)\) the mean in (1) obeys \(np_\infty(t_n(x))=\exp[-x-(2\beta/\alpha)e^{-\alpha t_n(x)}]\to e^{-x}\), and the bound (2) is \(O(n^{-(2\alpha+2\beta)/(\alpha+2\beta)})\). In the weak-rim window \(t=(\log n+x)/\alpha\) with \(\beta_n\log n\to c\), the exponent of \(np_\infty(t)\) is \(-x-2\beta_n t+(2\beta_n/\alpha)(1-e^{-\alpha t})\to-x-2c/\alpha\), and (2) is \(O(n^{-2})\).

Apply the dependency-graph Chen–Stein bound [3] to \(\sum_iX_i\) with mean \(np_n\). Its two terms are \(n(4R+1)p_n^2=O(R/n)\) and the sum of \(\Pr(X_i=X_j=1)\) over ordered neighboring distinct pairs. The latter is \(O(R n^{-\alpha/(\alpha+2\beta)})\) for fixed positive \(\beta\), and \(O(R/n)\) for the weak-rim window. Both tend to zero; so does the full-count truncation error. This proves the two Poisson limits. Taking the mass at zero, using \(\{T_n\le t\}=\{N_n(t)=0\}\), gives the displayed Gumbel laws. At \(\beta_n=0\) the independent spoke delays give the exact star distribution. Finally if \(\beta_n\to0\) and \(\beta_n\log n\to\infty\), take \(t=(\log n-K)/\alpha\) for any fixed \(K>0\). Then \(np_\infty(t)\to0\) by (1), and the same one-point truncation bound gives \(\Pr(T_n>t)\le np_\infty(t)+O(n\epsilon_n)\to0\). This proves escape from the star window.

## Verification
The accompanying `verify_wheel.py` constructs finite-wheel Markov generators and compares one-point survival computed by uniformization with (1) for selected sizes and rates. These comparisons concern the one-point approximation, not the count or extreme-value limits, which follow from the proof.

## Relationship to prior work and limitations
The two-sided homogeneous discrete Bass circle [1,2] has exactly the rim transition rates here under \(p=\alpha, q=2\beta\). In particular, [2, §4.1, eqs. (4.3)–(4.6)] gives exact finite-circle one-point survival via a recursion, valid for two-sided as well as one-sided diffusion, and §§3.3–3.4 give useful survival-event identities. Taking the infinite-size limit in the marginal recursion yields the ODE \(S'(t)=[-(p+q)+qe^{-pt}]S(t)\), which gives (1). The distinction here is control of the **joint rare-survivor count in a logarithmic time window**, with a Poisson limit and a crossover for the last adoption time. One-point survival alone does not exclude clusters. The locality argument and dependent-pair bound are needed for these conclusions. The comparison is bounded and does not settle absolute priority.

There is no claim of uniformity over unrestricted rate sequences, Gumbel moment convergence, a finite-wheel distribution of \(T_n\), or extension to nonexponential weights. In particular the proof uses fixed positive rim rate, or the specified weak-rim regimes, with the hub as the single initial source.

## References
1. G. Fibich and R. Gibori, *Aggregate diffusion dynamics in agent-based models with a spatial structure*, Operations Research **58** (2010), 1450–1468. [DOI](https://doi.org/10.1287/opre.1100.0818).
2. G. Fibich, T. Levin and O. Yakir, *Boundary Effects in the Discrete Bass Model*, SIAM Journal on Applied Mathematics **79** (2019), no. 3. [Author-hosted article](https://www.math.tau.ac.il/~fibich/Manuscripts/Bass_boundary_SIAP19.pdf).
3. R. Arratia, L. Goldstein and L. Gordon, *Two moments suffice for Poisson approximations: the Chen–Stein method*, Ann. Probab. **17** (1989), 9–25. [DOI](https://doi.org/10.1214/aop/1176991491).
