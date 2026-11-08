# Sharp logarithmic rare-error rate for Gaussian-refresh least-squares SGD

## Finding

For the stationary scalar least-squares stochastic-gradient recursion defined below, with any fixed learning rate \(0<a<2/3\), Gaussian regression noise of variance \(\sigma^2>0\), and Gaussian covariates refreshed with probability \(1-\rho\) per update for \(0<\rho<1\), its stationary error \(E\) obeys

\[
\boxed{\lim_{x\to\infty}\frac{\log\log x}{\log x}\,\big[-\log\mathbb P(|E|>x)\big]=-\log\rho.}
\]

Thus the failure probability at an extreme error threshold has the exact logarithmic scale \(\exp\{-(|\log\rho|+o(1))\log x/\log\log x\}\). Its leading constant is independent of the fixed stable stepsize and noise variance. This concerns the stationary last iterate of unmodified SGD, rather than a finite training horizon or a simultaneous vanishing-stepsize limit.

## Assumptions and scope

Take independent Gaussian marks \(G_j\sim N(0,1)\), independent Bernoulli refresh indicators with refresh probability \(1-\rho\), and independent errors \(Z_j\sim N(0,\sigma^2)\), independent of all marks and refreshes. In its two-sided stationary version, the covariate \(X_j\) retains its previous value with probability \(\rho\), otherwise replacing it by a fresh mark. The objective is the population scalar quadratic \(\tfrac12\mathbb E[(Y-\beta X)^2]\) with observations \(Y_j=\beta_* X_j+Z_j\), and the SGD error is updated by

\[
e_j=(1-aX_j^2)e_{j-1}+aX_j Z_j.
\]

Fix \(0<a<2/3\), \(0<\rho<1\), and \(\sigma>0\). All limits let only the error threshold \(x\to\infty\); the parameters are fixed. The two-sided stationary solution exists almost surely, as follows from negative average logarithmic multiplier and integrable logarithmic innovations. Its distribution is denoted by \(E\).

## Proof

**1. Contraction and the stationary series.** Set \(B_j=1-aX_j^2\) and \(\gamma=-\mathbb E\log|1-aG^2|\) for \(G\sim N(0,1)\). The logarithm is integrable, including its isolated zeros. Jensen's inequality and Gaussian moments give

\[
\mathbb E\log|1-aG^2|\le\tfrac12\log\mathbb E(1-aG^2)^2
=\tfrac12\log(1-2a+3a^2)<0.
\]

Thus \(\gamma>0\). The stationary ergodic covariate sequence has negative logarithmic product drift and finite \(\mathbb E\log^+(a|XZ|)\). Hence the stationary series converges almost surely:

\[
E=\sum_{j=0}^\infty aX_{-j}Z_{-j}\prod_{i=0}^{j-1}B_{-i}.
\]

**2. A geometric-Gaussian block tail.** In backward time, the covariates are constant on independent blocks. Each complete backward block has a mark \(G\sim N(0,1)\) and an independent length \(L\) with \(\mathbb P(L=\ell)=(1-\rho)\rho^{\ell-1}\) for \(\ell\ge1\). The first block has the same law because the stationary refresh chain is reversible. Fix any \(0<\delta<\gamma\) and let

\[
Y=L\big(\log|1-aG^2|+\delta\big),\qquad c=-\log\rho>0.
\]

Then \(Y\) has finite absolute mean and \(\mathbb EY=(\delta-\gamma)/(1-\rho)<0\). Its upper tail satisfies

\[
\lim_{y\to\infty}\frac{\log y}{y}\big[-\log\mathbb P(Y>y)\big]=c. \tag{1}
\]

Here is a direct proof. For \(\varepsilon>0\), split according to \(L\ge y/((1+\varepsilon)\log y)\). The first event has probability at most \(\exp[-c y/((1+\varepsilon)\log y)+O(1)]\). On the complementary event, \(Y>y\) demands \(\log|1-aG^2|+\delta>(1+\varepsilon)\log y\); the Gaussian tail of this event is bounded by \(\exp[-C y^{1+\varepsilon}]\) for a fixed \(C>0\) and all sufficiently large \(y\). This gives the lower bound on the limiting exponent. Conversely, choose \(L=\lceil(1+\varepsilon)y/\log y\rceil\) and require \(G^2\in[y/(\log y)^2,2y/(\log y)^2]\). For large \(y\), the latter event makes \(Y>y\), while its Gaussian cost is \(\exp[-o(y/\log y)]\). The prescribed geometric length costs \(\exp[-c(1+\varepsilon)y/\log y+O(1)]\). Let \(\varepsilon\downarrow0\) to obtain (1).

**3. Maximum of the logarithmic product.** Write \(S_j=\sum_{i=0}^{j-1}\log|B_{-i}|\), with \(S_0=0\), and \(M=\sup_{j\ge0}(S_j+\delta j)\). Within each backward constant-covariate block the quantity \(S_j+\delta j\) changes linearly, so its supremum occurs at block boundaries. Therefore \(M\) is exactly the supremum of a random walk whose independent increments have the distribution \(Y\). We claim

\[
\lim_{y\to\infty}\frac{\log y}{y}\big[-\log\mathbb P(M>y)\big]=c. \tag{2}
\]

The lower bound on probability is \(\mathbb P(M>y)\ge\mathbb P(Y>y)\). For the converse, fix \(c'<c\). By (1), for all sufficiently large \(y_0\) and all \(t\ge y_0\), \(\mathbb P(Y>t)\le\exp[-c't/\log t]\). Define an upper-stochastically-dominating law that agrees with \(Y\) below \(y_0\), and whose survival function for \(t\ge y_0\) is

\[
\overline F_+(t)=\min\{\mathbb P(Y>y_0),\exp[-c't/\log t]\}.
\]

This survival function is nonincreasing for sufficiently large \(y_0\), matches the original survival at the join, and dominates its tail. The surplus contribution to the mean tends to zero as \(y_0\to\infty\): the plateau ends at \(O(y_0)\), and its height is \(\exp[-(c+o(1))y_0/\log y_0]\); the remaining integrated tail is smaller still. Thus \(y_0\) can be chosen so its dominating increment has negative mean. Beyond the plateau, its tail is exactly \(\exp[-c't/\log t]\). This law's integrated-tail distribution is subexponential. To verify the required nonstandard tail condition, put \(\phi(t)=c't/\log t\). Then \(\phi'\) decreases to zero and \(\phi\) is eventually increasing and concave. For the survival function \(e^{-\phi(t)}\), split the two-fold convolution at \(h(t)=\sqrt{\log t}\) and at \(t^\alpha\), with any fixed \(0<\alpha<1\). On \(0\le u\le h(t)\), the tail ratio at \(t-u\) tends uniformly to one. On \(h(t)\le u\le t^\alpha\), the density-times-tail-ratio is bounded by a constant multiple of \(e^{-C u/\log u}/\log u\) for some \(C>0\), whose integral over \(u\ge h(t)\) vanishes. On \(t^\alpha\le u\le t/2\), concavity makes \(\phi(u)+\phi(t-u)-\phi(t)\) at least \(C t^\alpha/\log t\), so the corresponding integral is negligible. The overlap event where both summands exceed \(t/2\) is also negligible. Hence the two-fold convolution tail is asymptotically twice the original tail. Furthermore, integration by parts or l'Hopital's rule gives \(\int_t^\infty e^{-\phi(v)}\,dv\sim(\log t/c')e^{-\phi(t)}\); the same split verifies the two-fold criterion for the integrated tail. The negative-drift random-walk maximum theorem of Veraverbeke, in the form proved by Zachary (2004), then bounds \(\mathbb P(M>y)\) by a constant multiple of this integrated tail. By elementary integration, its logarithm is \(-c'y/\log y+o(y/\log y)\). Letting \(c'\uparrow c\) establishes (2). This explicitly uses a comparison law, not the unsupported inference that a logarithmic tail equivalent alone implies subexponentiality.

**4. The upper error tail.** For the \(\delta\) fixed in Step 2, put \(W=a\sum_{j\ge0}e^{-\delta j}|X_{-j}Z_{-j}|\). Minkowski's inequality gives \(\|W\|_2\le a\sigma\sum_{j\ge0}e^{-\delta j}<\infty\), notwithstanding dependence between the covariates. The stationary expansion yields \(|E|\le e^M W\). For every fixed \(0<\eta<1\),

\[
\mathbb P(|E|>e^y)\le\mathbb P(M>(1-\eta)y)+\mathbb P(W>e^{\eta y}).
\]

The second probability is at most \(\mathbb EW^2e^{-2\eta y}\), negligible on the scale \(e^{-c y/\log y}\). Inserting (2), and then letting \(\eta\downarrow0\), gives

\[
\liminf_{x\to\infty}\frac{\log\log x}{\log x}[-\log\mathbb P(|E|>x)]\ge c.
\]

**5. The matching lower error tail.** Put \(y=\log x\), \(v=y/(\log y)^2\), and \(m=\lceil(1+\eta)y/\log y\rceil\), for any fixed \(\eta>0\). Require the most recent \(m+1\) covariates to share one Gaussian mark with \(G^2\in[v,2v]\). The event has probability \(\rho^m\mathbb P(G^2\in[v,2v])\). Conditional on the whole design path, \(E\) is a centered Gaussian variable: its defining innovations are independent centered Gaussians. Its standard deviation is at least the absolute coefficient of the innovation \(Z_{-m}/\sigma\), namely \(\sigma a|G|\,|1-aG^2|^m\). The logarithm of this quantity is \((1+\eta)y(1-o(1))>y\), uniformly on the prescribed mark interval, so a universal positive conditional Gaussian exceedance probability applies for all large \(y\). Moreover \(-\log\mathbb P(G^2\in[v,2v])=O(v)=o(y/\log y)\). Consequently

\[
\limsup_{x\to\infty}\frac{\log\log x}{\log x}[-\log\mathbb P(|E|>x)]\le c(1+\eta).
\]

Let \(\eta\downarrow0\). Combining this with Step 4 proves the theorem.

## Verification

The standalone `verify.py` checks the stationary-product recursion against direct unrolling, block-boundary maximality, the exact quadratic Gaussian moment identity, a finite-value tail sum for the block increment and the Markov second-moment bound. It is a supplementary finite diagnostic, not a proof of the asymptotic theorem. Run it with `python3 verify.py` without external dependencies. Steps 1–5 above establish the infinite-threshold conclusion independently of the numerical checks.

## Relationship to prior work

Li and Wu, *Gaussian Limits for SGD Without Stationary Moments* (2026), introduce the Gaussian-refresh least-squares design, prove existence and failure of every positive stationary moment, and in Appendix G obtain a non-sharp lower tail bound on the \(\log x/\log\log x\) scale. Those facts are not claimed as new here. The present theorem identifies the matching two-sided logarithmic asymptotic and its exact refresh-dependent coefficient. Zachary's account of Veraverbeke's random-walk maximum theorem is used as an existing probability tool; it does not itself identify the stationary SGD error or the geometric-Gaussian increment cost. Li, Lei, Wei and Wu (2026) derive a different tail regime for regularly varying innovations in nonlinear SGD, rather than this persistent Gaussian-design mechanism.

## Limitations

The result is for one-dimensional least-squares SGD, a stationary Gaussian-refresh design with \(0<\rho<1\), independent Gaussian regression errors, fixed \(0<a<2/3\), and a stationary last iterate. It is not a finite-horizon bound, a high-dimensional theorem, a full multiplicative tail equivalent, or a claim about the stepsize-dependent prefactor. The boundary \(\rho=0\) has a different mechanism and is excluded. The upper-tail proof uses an established subexponential random-walk theorem and does not claim a new general theorem for arbitrary dependent recursions. Historical-priority risk remains for unindexed applications of regenerative perpetuity theory to this exact model.

## References

- X. Li and W. B. Wu, *Gaussian Limits for SGD Without Stationary Moments*, arXiv:2610.05599v1 (first public October 4, 2026), especially Section 3 and Appendix G. https://arxiv.org/abs/2610.05599
- S. Zachary, *A Note on Veraverbeke's Theorem*, Queueing Systems 46 (2004), 9–14; arXiv:1410.8551. https://arxiv.org/abs/1410.8551
- X. Li, Q. Lei, Z. Wei and W. B. Wu, *Exact Tail Laws for Nonlinear SGD with Infinite-Variance Gradients*, arXiv:2610.23750v1 (October 16, 2026), a distinct regularly varying innovation regime. https://arxiv.org/abs/2610.23750
