# A universal delayed covariance pulse in nested resetting chains

## Finding

Let \(N\ge 2\) and \(r>0\). Each coordinate \(X_i\), \(1\le i\le N\), evolves between independent rate-\(r\) Poisson reset events by adding increments of its own independent, centered, square-integrable Lévy process. The variance accumulated per unit time by the noise at site \(i\) is \(q_i\ge0\), with \(q_1>0\). A reset of site \(i\) instantaneously replaces \(X_i\) by \(X_{i-1}\), with the fixed root \(X_0=0\). Set \(V=q_1/r\). All quantities below refer to the unique stationary process.

For every \(j\in\{2,\ldots,N\}\), write \(m=j-1\) and define the forward and reverse stationary, centered, time-lagged covariances for \(t\ge0\) by

\[
C_m^\rightarrow(t)=\operatorname{Cov}(X_1(0),X_{m+1}(t)),\qquad
C_m^\leftarrow(t)=\operatorname{Cov}(X_{m+1}(0),X_1(t)).
\]

Then **exactly**, for every \(t\ge0\),

\[
\boxed{C_m^\rightarrow(t)=V2^{-m}e^{-rt}\sum_{k=0}^{m}\frac{(2rt)^k}{k!},\qquad C_m^\leftarrow(t)=V2^{-m}e^{-rt}.}
\]

For each \(m\ge1\), the forward covariance is initially increasing and has **exactly one** global maximum, at \(t_m=\lambda_m/(2r)\), where \(\lambda_m\) is the unique positive solution of

\[
\sum_{k=0}^{m-1}\frac{\lambda_m^k}{k!}=\frac{\lambda_m^m}{m!}.
\]

The pulse propagates ballistically through the chain but decays only algebraically at its peak:

\[
\boxed{rt_m=m-1+O(m^{-1}),\quad C_m^\rightarrow(t_m)=V\sqrt{\frac{2}{\pi m}}\bigl(1+O(m^{-1})\bigr),\quad C_m^\rightarrow(0)=V2^{-m}.}
\]

At the same time, the integrated directed response survives arbitrary chain depth:

\[
\boxed{\int_0^\infty C_m^\rightarrow(t)\,dt=\frac Vr(2-2^{-m}),\qquad \int_0^\infty C_m^\leftarrow(t)\,dt=\frac Vr2^{-m}.}
\]

Thus the time-integrated forward-minus-reverse covariance tends to \(2V/r\), not zero, as \(m\to\infty\). All these conclusions are **independent of every downstream noise variance \(q_2,\ldots,q_N\)** and of the detailed noise distributions, even when the increments are non-Gaussian. Ordinary Brownian nested resetting is the special case \(q_i=2D\).

## Assumptions and scope

The chain is finite; the reset clocks at different sites are independent, each with rate \(r>0\), and are independent of every driving Lévy process. The noises are independent across sites, have stationary independent increments, zero mean, and finite second moment at unit time. They can have jumps. A site's reset does not reset the remaining sites or their noises. At simultaneous events, which occur with probability zero, a consistent order may be chosen. The root is pinned at zero. There is no feedback upstream.

A unique stationary law exists with finite second moments: tracing any coordinate backwards through the most recent reset at its site, then at the predecessor, and so on, reaches the pinned root after at most \(N\) exponential waiting stages. The accumulated independent finite-variance increments have finite second moment. This backward construction is shift-invariant in time and couples any finite-time initial condition to the stationary construction after a finite almost-sure backward ancestry time. Every stationary mean equals zero. The covariance formulas hold for each fixed finite \(N\), and their \(m\to\infty\) interpretation uses chains with \(N\ge m+1\).

## Proof

**1. Stationary first-row covariance.** Let \(c_{ij}=\mathbb E[X_iX_j]\) in stationarity, with \(c_{0j}=0\). The infinitesimal generator applied to \(X_1^2\) gives \(0=q_1-r c_{11}\), hence \(c_{11}=V\). For \(j>1\), independent noises contribute no cross-variation and only resets at sites \(1\) and \(j\) change \(X_1X_j\). Applying the generator therefore gives

\[
0=-r c_{1j}+r(c_{1,j-1}-c_{1j}),\qquad
c_{1j}=\tfrac12c_{1,j-1}=V2^{-(j-1)}.
\]

The independent noise at any downstream site contributes nothing to these balances. The same generator calculation gives \(\mathbb E[X_j^2]=\sum_{i=1}^jq_i/r\), confirming finite stationary variances for arbitrary heterogeneous noise strengths.

**2. Exact lagged covariance.** On coordinate functions, the generator is \(\mathcal L X_1=-rX_1\) and \(\mathcal L X_j=r(X_{j-1}-X_j)\) for \(j>1\). Thus conditional means given the complete state at time zero solve a lower-triangular linear system, whose explicit solution is

\[
\mathbb E[X_j(t)\mid X(0)]=e^{-rt}\sum_{k=0}^{j-1}\frac{(rt)^k}{k!}X_{j-k}(0).
\]

Multiplying by \(X_1(0)\) and taking stationary expectations, using the first-row identity in Step 1, gives the stated forward covariance. The reverse direction follows from \(\mathbb E[X_1(t)\mid X(0)]=e^{-rt}X_1(0)\). For \(t>0\), the forward covariance is strictly greater than its reverse: every extra term of the finite sum is positive.

**3. One and only one maximum.** Put \(x=rt\) and \(\lambda=2x\). Differentiating the forward covariance with respect to \(x\) gives a strictly positive factor times

\[
Q_m(\lambda)=\sum_{k=0}^{m-1}\frac{\lambda^k}{k!}-\frac{\lambda^m}{m!}.
\]

For \(\lambda>0\), division by \(\lambda^m/m!\) shows that the derivative sign equals the sign of

\[
S_m(\lambda)-1,\qquad S_m(\lambda)=\sum_{\ell=1}^{m}\frac{m(m-1)\cdots(m-\ell+1)}{\lambda^\ell}.
\]

Every summand is strictly decreasing in \(\lambda>0\), and \(S_m\) decreases continuously from infinity to zero. Therefore there is exactly one positive root; the derivative changes from positive to negative there. The forward covariance tends to zero as \(t\to\infty\), so this root is its unique global maximum.

**4. Sharp delay and height.** For bounded real \(c\), put \(\lambda=2m+c\). Expanding the falling factorial for each fixed \(\ell\), and controlling the summable tails uniformly by a geometric bound, yields

\[
S_m(2m+c)=1-\frac{c+2}{m}+O(m^{-2}),\qquad \frac{\partial S_m}{\partial\lambda}(2m+c)=-\frac1m+O(m^{-2}).
\]

Consequently the unique root is \(\lambda_m=2m-2+O(m^{-1})\), giving the stated lag. At the root, the defining equation makes the finite exponential sum twice its final term, so

\[
C_m^\rightarrow(t_m)=2V\,e^{-\lambda_m/2}\frac{(\lambda_m/2)^m}{m!}.
\]

As \(\lambda_m/2=m-1+O(m^{-1})\), Stirling's formula shows that this equals \(V\sqrt{2/(\pi m)}(1+O(m^{-1}))\). The simultaneous covariance was already determined in Step 1. The ratio of peak to simultaneous covariance therefore grows as \(2^m\sqrt{2/(\pi m)}\).

**5. Integrated directional transport.** Termwise integration is justified by the nonnegative finite sum. The gamma integral gives \(\int_0^\infty e^{-rt}(rt)^k\,dt=k!/r\), hence

\[
\int_0^\infty C_m^\rightarrow(t)\,dt=\frac Vr2^{-m}\sum_{k=0}^m2^k=\frac Vr(2-2^{-m}).
\]

Integrating the reverse exponential gives \((V/r)2^{-m}\), proving the directed difference and its limit.

## Verification

The supplied `verify_signal.py` runs with the Python 3 standard library. It independently reconstructs finite-chain quadratic generator balances with exact rational arithmetic, checks heterogeneity of the downstream Lévy variance rates, integrates the conditional-moment ODE numerically without using the closed-form propagator, checks finite-root derivative signs and peak identities, and independently quadratures the integrated covariances. The extracted and executed program reported **1,499 passed deterministic checks**. These computations support the finite-dimensional identities but are not substitutes for the all-index and asymptotic arguments above.

## Relationship to prior work

Alston, Britton and Bertrand (2025) established the stationary single-time distributions and exact **equal-time** two-point correlations of the Brownian nested-resetting model. In particular, their static framework covers the \(t=0\) specialization of the present covariance formula. Britton and collaborators (2026) established **one-time** relaxation and accumulation times along the nested chain, including a propagating relaxation front, as well as heterogeneous resetting rates. Neither inspected study states the stationary two-time root-to-descendant covariance pulse, its unique optimal lag with ballistic and inverse-square-root laws, the nonvanishing integrated causal transfer, or its independence from arbitrary downstream finite-variance Lévy disturbances. The conditional-mean formula by itself is a straightforward linear-generator identity; the claim of extension specifically concerns its complete directed pulse geometry, asymptotic and integrated laws, and noise universality.

## Limitations

The result treats a fixed pinned root, equal independent reset rates, independent centered finite-variance Lévy increments, and root-to-descendant two-time covariances. It does not classify general pairs, unequal rates, dependence between noises, nonlinear interactions, higher cumulants or entropy production. Raw covariances scale as described; normalized Pearson correlations additionally divide by the downstream stationary standard deviation, which can depend on all noise strengths. Large-depth statements are limiting results for a sequence of finite chains, not a construction of an infinite-chain invariant law. Although the two most directly relevant works were materially inspected, unidentified broader results could affect publication priority; no independent external scientific validation is claimed.

## References

1. H. Alston, C. Britton and T. Bertrand, *Nested Stochastic Resetting: Nonequilibrium Steady-states and Exact Correlations*, arXiv:2502.03225, first posted 5 February 2025, https://arxiv.org/abs/2502.03225 ; published in *Physical Review Letters* 135, 167101 (2025), https://doi.org/10.1103/ccjj-6ksn .
2. C. Britton, B. Le Jeune, H. Alston, P. C. Bressloff and T. Bertrand, *Approach to Steady-State in Nested Resetting Processes*, arXiv:2609.25252, first posted 21 September 2026, https://arxiv.org/abs/2609.25252 .
3. G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658, first posted 8 September 2025, https://arxiv.org/abs/2509.06658 ; different global-resetting protocol.
