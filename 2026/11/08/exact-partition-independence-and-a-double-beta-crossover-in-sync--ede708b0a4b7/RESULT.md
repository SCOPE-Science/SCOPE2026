# Exact partition independence and a double-Beta crossover in synchronous noisy voting

## Finding

For synchronous two-opinion noisy voting on the complete bipartite graph \(K_{a,b}\), the two entire vertex-part configurations are independent under the unique stationary law, for every \(a,b\ge2\) and every reset probability \(0<\varepsilon\le1\). More generally, this exact stationary partition independence holds on **every finite bipartite graph without isolated vertices** with independent parallel updates and fair resetting.

For the partwise fractions \(U_{a,b}\) and \(V_{a,b}\) of opinion 1 on \(K_{a,b}\), let \(a,b\to\infty\) at arbitrary relative rates, put \(h_{a,b}=a^{-1}+b^{-1}\), and allow the reset parameter to vary with \(a,b\). If \(\varepsilon_{a,b}/h_{a,b}\to\lambda\in[0,\infty]\), the joint stationary fractions converge in distribution to *independent* copies of the same random variable \(Z_\lambda\), where

\[
Z_\lambda\sim
\begin{cases}
\tfrac12\delta_0+\tfrac12\delta_1,&\lambda=0,\\
\operatorname{Beta}(2\lambda,2\lambda),&0<\lambda<\infty,\\
\delta_{1/2},&\lambda=\infty.
\end{cases}
\]

In particular, if \(\varepsilon_{a,b}\ll a^{-1}+b^{-1}\), the two parts each become nearly unanimous while disagreeing with asymptotic probability \(1/2\). At the critical noise scale they instead have independent non-Gaussian Beta opinion shares.

## Assumptions and scope

Let \(G=(A\sqcup B,E)\) be a finite bipartite graph without isolated vertices. Every vertex has a spin \(\xi_t(v)\in\{0,1\}\). All vertices update **simultaneously** using the time-\(t\) configuration: independently for each vertex, with probability \(\varepsilon\in(0,1]\) it adopts a fresh fair Bernoulli spin, and with probability \(1-\varepsilon\) it copies the time-\(t\) spin of one uniformly selected neighbor. All reset coins, fresh spins, and neighbor choices are independent across vertices and times. The update is not the asynchronous process in which one vertex changes per tick.

For the limit theorem take \(G=K_{a,b}\) with positive integers \(a,b\ge2\), write \(U_t=a^{-1}\sum_{v\in A}\xi_t(v)\), \(V_t=b^{-1}\sum_{w\in B}\xi_t(w)\), and interpret \(U_{a,b},V_{a,b}\) as their stationary laws. The limit requires both \(a\to\infty\) and \(b\to\infty\), not any restriction on their ratio. All limits refer to the unique stationary law at strictly positive noise, even in the regime where that noise vanishes as the graph grows.

## Proof

**1. Existence, uniqueness, and exact independence.** With \(\varepsilon>0\), every prescribed next spin configuration can occur with positive probability by resetting every vertex. Consequently the finite-state transition matrix is strictly positive, so there is a unique invariant law and convergence to it from any initial law.

Suppose the current state has an independent product law across its bipartition, \(P_A\otimes P_B\), although dependence *within* either part is permitted. All new spins in \(A\) are measurable functions only of the old state in \(B\) and fresh randomness for \(A\); analogously new spins in \(B\) are functions only of the old state in \(A\) and independent fresh randomness for \(B\). The two collections of inputs are independent. Hence the next state again has an independent law across \(A\) and \(B\). Starting with independent partwise states, every finite-time law factorizes, and convergence to the unique invariant law preserves this factorization. This proves independence of the *whole part configurations*, not merely independence of their densities. On \(K_{a,b}\), permutation symmetry also makes each part exchangeable.

**2. Exact two-step marginal kernel.** Set \(q=1-\varepsilon\) and \(r(u)=\varepsilon/2+qu\). Conditional on \(U_t=u\),

\[
bV_{t+1}\sim\operatorname{Bin}(b,r(u)),\qquad
aU_{t+2}\mid V_{t+1}=v\sim\operatorname{Bin}(a,r(v)).
\]

Thus the even-time \(A\)-fraction is an autonomous two-step chain. Put \(\mu(u)=r(r(u))=(1-q^2)/2+q^2u\). Conditional binomial variance followed by total variance gives the **exact** identities

\[
\mathbb E[U_{t+2}-u\mid U_t=u]=-(1-q^2)(u-1/2),
\]
\[
\operatorname{Var}(U_{t+2}\mid U_t=u)=
\frac{\mu(u)(1-\mu(u))}{a}
+q^2\left(1-\frac1a\right)\frac{r(u)(1-r(u))}{b}.
\]

The corresponding relations for \(V\) exchange \(a,b\). In particular both stationary means are exactly \(1/2\).

**3. Critical regime.** Write \(h=a^{-1}+b^{-1}\) and suppose \(\varepsilon/h\to\lambda\in(0,\infty)\). Uniformly for \(0\le u\le1\), the exact formulas yield

\[
\frac{\mathbb E[\Delta\mid u]}h\longrightarrow\lambda(1-2u),\qquad
\frac{\mathbb E[\Delta^2\mid u]}h\longrightarrow u(1-u),
\quad\Delta=U_{t+2}-u.
\]

Moreover \(\sup_u\mathbb E[|\Delta|^3\mid u]=O(h^{3/2})=o(h)\): condition on the first binomial stage; its centered fourth moment is \(O(b^{-2})\), the second binomial has centered fourth moment \(O(a^{-2})\), and the two-step deterministic shift is \(O(h)\). Minkowski's inequality and Hölder's inequality then give the claimed uniform bound.

Take any weakly convergent subsequence of stationary \(U\)-laws (compactness of \([0,1]\)). Invariance of the two-step chain and Taylor's theorem show, for every polynomial \(f\), that the limiting law \(\nu\) satisfies

\[
\int_0^1\left[\lambda(1-2u)f'(u)+\frac{u(1-u)}2f''(u)\right]\,\nu(du)=0.
\]

Taking \(f(u)=u^k\) for \(k\ge1\) gives the recursion for its moments \(m_k\):

\[
(4\lambda+k-1)m_k=(2\lambda+k-1)m_{k-1},\qquad m_0=1.
\]

The Beta distribution \(\operatorname{Beta}(2\lambda,2\lambda)\) has precisely these moments. The Hausdorff moment problem on \([0,1]\) is determinate, so every subsequential limit agrees with this Beta distribution. The same proof holds for the \(B\) part without a ratio restriction. Their finite-size independence from Step 1 then implies convergence to the **product** Beta law.

**4. Zero- and high-noise boundaries.** Let \(R_A\) (respectively \(R_B\)) be the stationary covariance of any two *distinct* spins \(2\xi(v)-1\) in the same part, equivalently their correlation because each has variance 1. Two copied spins are equal only if they select the same neighbor or distinct neighbors whose old spins correlate. Resets erase correlations. Thus

\[
R_A=q^2\left[\frac1b+\left(1-\frac1b\right)R_B\right],\qquad
R_B=q^2\left[\frac1a+\left(1-\frac1a\right)R_A\right].
\]

Solving yields

\[
R_A=\frac{q^2/b+q^4(1-1/b)/a}{1-q^4(1-1/a)(1-1/b)},\qquad
R_B=\frac{q^2/a+q^4(1-1/a)/b}{1-q^4(1-1/a)(1-1/b)}.
\]

Here the denominators are positive because \(q<1\). Exchangeability gives

\[
\operatorname{Var}(U)=\frac14\left[\frac1a+\left(1-\frac1a\right)R_A\right],\qquad
\operatorname{Var}(V)=\frac14\left[\frac1b+\left(1-\frac1b\right)R_B\right].
\]

When \(\varepsilon/h\to0\), both correlations converge to 1, so each fraction has limiting mean \(1/2\) and variance \(1/4\). For a random variable in \([0,1]\), these jointly force equal mass at 0 and 1: use \(\mathbb E[U(1-U)]=1/4-\operatorname{Var}(U)\to0\). When \(\varepsilon/h\to\infty\), both correlations converge to zero; both fractions tend in \(L^2\) to \(1/2\). Taking products of independent marginal limits completes all three regimes. The argument remains valid when the two part sizes have an arbitrarily varying ratio. \(\square\)

## Verification

A standalone standard-library Python checker, `verify.py`, evaluates the exact two-stage transition kernels over 21 combinations of part sizes and positive rational noise levels. It solves stationary count distributions using exact fractions, verifies joint count independence, both mean and covariance identities, and the conditional two-step drift and variance. In addition, it constructs complete opinion-configuration transitions for four small bipartite sizes and independently verifies stationarity of the product-form configuration law. The checker produces `VERIFY_OK 1112 exact rational assertions`.

These finite calculations check identities and implementation but do not certify the asymptotic limits. The latter follow from the generator/moment argument and explicit correlation bounds above.

## Relationship to prior work

Benjamini, Helman Tov and Zhukovskii [1], especially Section 6, study **the same simultaneous-update noisy voter process on complete bipartite graphs**, but their results concern temporal observations of one vertex and a two-time coalescence/repetition probability. They do not state the full stationary bipartition factorization or the three-regime joint empirical-density law established here. Their two-time repetition statistic must not be confused with the same-time two-part distribution.

Pymar and Rivera [2] study the stationary density of a **one-vertex-per-step** noisy voter chain. Ben-Ari, Panzo, Speegle and VandenBerg [3] study quasi-stationary laws for an **asynchronous, noiseless** voter chain on complete bipartite graphs. Mori, Hisakado and Nakayama [4] derive a multivariate Beta-type stationary law for a different network voter model with interacting within-node populations; their model and joint density are not the independent-Beta law of this simultaneous alternating update. Kononovicius et al. [5] analyze asynchronous updates with periodically polled delays, a distinct mechanism. The present result treats the full configuration independence and both finite-population noise-scaling boundaries under the explicitly fixed update convention.

## Limitations

The full-product identity concerns **opposite bipartition classes at the same time** and need not imply independence across time or among vertices within a class. The Beta limit uses only weak convergence of fractions; no total-variation claim is made for a continuous limit of discrete variables. The positive-noise stationary distribution is taken before the size limit, and no statement is made about uniqueness at exactly zero noise. General bipartite graphs inherit the exact independence statement, not the complete-bipartite Beta limit. No quantitative convergence rate is claimed. The literature comparison does not constitute a proof of historical priority.

## References

1. I. Benjamini, H. Helman Tov, and M. Zhukovskii, *Global information from local observations of the noisy voter model on a graph*, arXiv:2207.01224 (first public version 2022-07-04), Section 6. https://arxiv.org/abs/2207.01224
2. R. Pymar and N. Rivera, *Asymptotic behaviour of the noisy voter model density process*, arXiv:2112.01478 (2021). https://arxiv.org/abs/2112.01478
3. I. Ben-Ari, H. Panzo, R. Speegle, and R. VandenBerg, *Quasi-Stationary Distributions for the Voter Model on Complete Bipartite Graphs*, arXiv:2004.10187 (2020). https://arxiv.org/abs/2004.10187
4. S. Mori, M. Hisakado, and K. Nakayama, *A voter model on networks and multivariate beta distribution*, arXiv:1810.05643 (2018). https://arxiv.org/abs/1810.05643
5. A. Kononovicius, R. Astrauskas, M. Radavičius, and F. Ivanauskas, *Delayed interactions in the noisy voter model through the periodic polling mechanism*, arXiv:2403.10277 (2024). https://arxiv.org/abs/2403.10277
