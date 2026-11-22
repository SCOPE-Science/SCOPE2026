# Unique erasure-robust two-node quadrature for exponential Gaussian processes

## Finding

Let \(X\) be a centered unit-variance stationary Gaussian process on \([0,1]\) with covariance \(K(s,t)=e^{-\lambda|s-t|}\), where \(\lambda>0\) is known. Exactly two nonadaptive, noiseless point queries are scheduled. Each independently returns its value with probability \(p\in(0,1]\), and the success indicators are reported. The estimator of \(I=\int_0^1 X(t)\,dt\) is its conditional mean using the successful queries. The design minimizes unconditional mean-square error, equivalently expected posterior integral variance, over **all** unordered choices of two points in \([0,1]\), including repeated points.

There is a **unique** optimal unordered design \(\{1/2-u_{\lambda,p}/\lambda,\ 1/2+u_{\lambda,p}/\lambda\}\), with \(0<u_{\lambda,p}<\lambda/2\), where \(u_{\lambda,p}\) is the unique solution of
\[
 p=\frac{4e^{-\lambda/2}\sinh u\cosh^2 u}
 {1-e^{-\lambda/2-2u}\cosh u}.
\]
The optimal half-gap \(u_{\lambda,p}\) strictly increases with successful-delivery probability \(p\). It is **strictly positive at every \(p>0\)**, although it tends to zero as \(p\downarrow0\). With \(z=e^{-\lambda/2}\),
\[
 u_{\lambda,p}=\frac{1-z}{4z}p+O_{\lambda}(p^2),\quad p\downarrow0.
\]
The dependence on covariance length has two further exact limits for each fixed \(p>0\):
\[
 \frac{u_{\lambda,p}}{\lambda}\longrightarrow \frac{p}{4(2-p)}\quad(\lambda\downarrow0),
 \qquad
 u_{\lambda,p}=\frac{\lambda}{6}+\frac{\log(2p)}3+o(1)\quad(\lambda\to\infty).
\]
Thus the sites approach \(1/2\pm p/[4(2-p)]\) in the long-correlation limit and approach \(1/3,2/3\) in the short-correlation limit regardless of fixed positive delivery probability. The \(p=1\) boundary recovers the previously known two-point noiseless design; the claim of new content is the **whole independent-erasure family**, including global uniqueness, monotone movement and these asymptotic laws.

## Assumptions and scope

The process is zero-mean stationary Gaussian with known unit marginal variance and covariance \(e^{-\lambda|s-t|}\). Observations, if delivered, have no additive noise; each delivery is an independent Bernoulli event of common known probability \(p\) and independent of the process. The two locations are committed before any value or delivery is seen. The estimator conditions on the observed values **and** on which queries succeeded. A duplicated location yields only one distinct function value when either or both copies succeed; it is allowed as a competing design. The loss is the scalar integral's squared error, not the spatially integrated error of reconstructing the entire path. All optimization statements quantify over every \(\lambda>0\) and \(0<p\le1\).

## Proof

**1. Risk as a two-site Schur complement.** Put
\[
 W_\lambda(t)=\operatorname{Cov}(I,X(t))
 =\frac{2-e^{-\lambda t}-e^{-\lambda(1-t)}}\lambda,\quad
 V_0=\operatorname{Var}(I)=\frac{2(\lambda-1+e^{-\lambda})}{\lambda^2}.
\]
For distinct locations \(s<t\), set \(r=e^{-\lambda(t-s)}\), \(w_s=W_\lambda(s)\), \(w_t=W_\lambda(t)\). If exactly one query succeeds, the variance reduction is \(w_s^2\) or \(w_t^2\); if both succeed, inversion of \(\begin{psmallmatrix}1&r\\r&1\end{psmallmatrix}\) gives reduction \((w_s^2+w_t^2-2r w_sw_t)/(1-r^2)\). The unconditional gain, to be maximized, is therefore exactly
\[
 G_{\lambda,p}(s,t)=p(1-p)(w_s^2+w_t^2)
 +p^2\frac{w_s^2+w_t^2-2r w_sw_t}{1-r^2}.
\]
The mean-square risk is \(V_0-G_{\lambda,p}(s,t)\). The continuous coincident-site extension is \(G_{\lambda,p}(s,s)=p(2-p)W_\lambda(s)^2\).

**2. The globally optimal pair is centered, without imposing symmetry.** Set \(u=\lambda(t-s)/2\in[0,\lambda/2]\), \(v=\lambda(s+t-1)/2\), \(z=e^{-\lambda/2}\), and \(C=\cosh v\). The feasible range is \(|v|\le\lambda/2-u\), with \(C\ge1\). The two individual covariances are \(w_s=2[1-z\cosh(v-u)]/\lambda\) and \(w_t=2[1-z\cosh(v+u)]/\lambda\). Differentiating the one-success sum with respect to \(C\) gives
\[
 \frac{d(w_s^2+w_t^2)}{dC}
 =\frac{16z}{\lambda^2}\bigl[-\cosh u+z C\cosh(2u)\bigr]<0.
\]
Indeed \(zC\le e^{-u}\) and \(e^{-u}\cosh(2u)<\cosh u\) for \(u>0\). For \(u=0\), \(zC<1\) follows from \(\lambda>0\). Similarly the two-success gain \(G_2=(w_s^2+w_t^2-2r w_sw_t)/(1-r^2)\), where \(r=e^{-2u}\), satisfies
\[
 \frac{dG_2}{dC}=
 \frac{16z\cosh u}{\lambda^2(1+e^{-2u})}
 \bigl(ze^u C-1\bigr)<0
\]
whenever \(0<u<\lambda/2\), because \(ze^uC\le e^{-(\lambda/2-u)}\cosh(\lambda/2-u)<1\). At the maximal gap \(u=\lambda/2\), the center is forced to be zero. For coincident sites the gain is uniquely largest at the midpoint, because \(W_\lambda(t)\) uniquely peaks there. Hence, for each fixed separation, the best pair is uniquely reflection-symmetric around \(1/2\), and no asymmetric global minimizer is possible.

**3. Strictly unique optimal separation.** On a centered pair, \(w_s=w_t=2(1-z\cosh u)/\lambda\). Substitution reduces the gain to
\[
 G_{\lambda,p}(u)=\frac{8p}{\lambda^2}
 [1-z\cosh u]^2\left[1-\frac p2+\frac p2\tanh u\right],
 \qquad 0\le u\le\lambda/2.
\]
Write \(A(u)=1-z\cosh u>0\) and \(B(u)=1-p/2+(p/2)\tanh u>0\). Both are concave on this interval, and \(A''=-z\cosh u<0\). Consequently \(2\log A+\log B\) is **strictly concave**. At the left endpoint its derivative is \(p/(2-p)>0\). At the right endpoint, \(A'/A=-1\), while \(B'/B\le1-\tanh u<1\), so the log derivative is less than \(-1\). There is exactly one interior maximum. Solving its first-order condition yields the scalar equation in the finding, whose root is thereby proved unique in the asserted interval.

**4. Dependence on success and covariance length.** The partial derivative of \(\partial_u\log B\) with respect to \(p\) is \(\operatorname{sech}^2u/[2B(u)^2]>0\), while the total second derivative of \(\log G\) in \(u\) is strictly negative. The implicit-function theorem gives \(\partial_pu_{\lambda,p}>0\), including the one-sided statement at \(p=1\). Expanding the unique-root equation at \(p=u=0\) gives \(u=(1-z)p/(4z)+O_\lambda(p^2)\). For fixed \(p>0\) and \(\lambda\downarrow0\), write \(u=\lambda d\); the root equation tends to \(p=8d/(1+4d)\), hence \(d\to p/[4(2-p)]\) by uniqueness and endpoint bracketing. For \(\lambda\to\infty\), evaluate the root equation at \(u=\lambda/6+c\): its right side tends to \(e^{3c}/2\), uniformly for \(c\) in each fixed compact interval. Strict log-unimodality brackets the unique root, implying \(u=\lambda/6+\log(2p)/3+o(1)\). These are limits with the other parameter held fixed, not joint \(p,\lambda\) uniform claims.

## Verification

The standalone `verify_erasure_ou.py` reconstructs the posterior reduction by both Gaussian Schur complements and the hyperbolic formula, checks five symbolic identities (including the stationarity and centering derivatives), compares 600 random/direct-optimization candidate results across 30 parameter pairs, and checks the three limiting formulae numerically. Reproduce using `python verify_erasure_ou.py` with Python 3, NumPy, SciPy and SymPy. The proof of global uniqueness is analytic; finite sampled designs and symbolic software are supplementary and are not used as an exhaustive search over a continuum.

At \(\lambda=1\), \(p=1/2\), the optimal locations are approximately \(0.3975454362615\) and \(0.6024545637385\); the optimal expected posterior integral variance is \(0.2632443574757\), versus \(0.2713045171044\) for two repeated midpoint queries. The exact risk is computed from \(V_0-G_{\lambda,p}\).

## Relationship to prior work

Pronzato and Zhigljavsky (2018) provide the kernel-energy/Bayesian quadrature framework and an exponential-kernel example but not an independent query-erasure optimizer. Kanagawa and Hennig (2019) analyze adaptive Bayesian-quadrature consistency and rates, not this two-query robust-design problem. Cai, Lam and Scarlett (2022) analyze average-case rates under additive observation noise; they do not replace exact observation delivery failures by the present mixture of zero-, one-, and two-query posterior risks. A previously reported exact optimal-node theorem for stationary exponential covariance (2026) determines the **noiseless always-delivered** case for arbitrary sample count, including the \(p=1\) boundary here. Separate reported Gaussian-noise-precision results cover additive-noise queries rather than independent erasures. The novelty claimed here is not the Gaussian conditioning formula or that previous boundary; it is the globally optimal independent-erasure design for every \(0<p<1\) and its monotonic and asymptotic structure.

## Limitations

Only two fixed, noiseless queries with identical independent delivery probabilities are considered. No result is asserted for heterogeneous delivery probabilities, unknown covariance parameters, additive measurement noise on successful deliveries, adaptive query locations, more than two queries, or nonexponential covariance kernels. The proof uses the stationary exponential kernel. Independent mathematical audit and comprehensive historical publication-priority verification remain outstanding. An older dissertation on optimal stochastic-process sampling mentions integral estimation, but the complete dissertation could not be inspected for indirect priority comparisons; no assertion of its noncoverage is made.

## References

1. L. Pronzato and A. Zhigljavsky, *Bayesian quadrature and energy minimization for space-filling design*, arXiv:1808.10722v1 (first public 2018-08-31), https://arxiv.org/abs/1808.10722.
2. M. Kanagawa and P. Hennig, *Convergence Guarantees for Adaptive Bayesian Quadrature Methods*, arXiv:1905.10271v1 (2019-05-24), https://arxiv.org/abs/1905.10271.
3. X. Cai, C. T. Lam and J. Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, arXiv:2202.10615v1 (2022-02-22), https://arxiv.org/abs/2202.10615.
4. *Exact optimal nodes and stratification penalty for Ornstein–Uhlenbeck Bayesian quadrature* (2026), public full-text scientific result at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-optimal-nodes-and-stratification-penalty-for-ornstein-uhle--971795799fba.
5. B. Mukherjee, *Optimal designs for estimating the path of a stochastic process*, Purdue University dissertation (2001), abstract at https://docs.lib.purdue.edu/dissertations/AAI3043760/.
