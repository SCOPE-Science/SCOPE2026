# Exact two-sensor Brownian-bridge quadrature under correlated observation erasures

## Finding
Consider the integral \(J=\int_0^1B(t)\,dt\) of a standard Brownian bridge. Two noiseless observations are requested at predetermined sites \(0\le a\le b\le1\). Each request succeeds with marginal probability \(p\in(0,1]\), independently of the bridge; the joint success probability is \(q\in[\max(0,2p-1),p]\), without requiring independence between the two successes. Whenever a reading is unavailable, its absence is known. The estimator is the conditional expectation of \(J\) given the received readings and availability indicators. The squared-error Bayes risk is averaged over those indicators.

For every admissible \((p,q)\), the unique optimal **ordered** pair of request sites, including possible coincidence when \(q=0\), is
\[
\boxed{a_*=\frac12-d_*,\quad b_*=\frac12+d_*,\quad
 d_*=\frac{q}{2\left(2p-q+\sqrt{(2p-q)^2+3q^2}\right)}.}
\]
The half-separation satisfies \(0\le d_*\le1/6\); it is zero precisely when \(q=0\), and reaches \(1/6\) precisely when \(q=p\). In particular, the design depends only on the relative co-delivery rate \(q/p\), increases strictly in that ratio, and lies between midpoint-repeated queries and the trisection pair \((1/3,2/3)\).

A second sharp statement distinguishes observation availability from deterministic sampling geometry: for fixed \(0<p<1\), the **optimized** Bayes risk is strictly increasing as the two delivery indicators become more positively associated, parametrized by their joint success probability \(q\) across its full feasible interval. More precisely, if \(R_*(p,q)\) denotes the minimum expected conditional variance, then
\[
\boxed{\frac{\partial R_*}{\partial q}=
\frac{a_*(1-b_*)(1+b_*-a_*)}{4}>0,}
\]
with one-sided derivatives at feasible endpoints. Thus greater simultaneous delivery at fixed individual delivery probabilities worsens this integral estimation risk by increasing the chance that both measurements are simultaneously absent; the spatially optimal separation nevertheless increases.

At independent delivery with \(p=1/2\) and \(q=1/4\), one obtains
\[
(a_*,b_*)=\left(1-\frac{1}{\sqrt3},\frac{1}{\sqrt3}\right),\qquad
R_* =\frac1{12}-\frac{\sqrt3}{36}=0.0352208109008645\ldots.
\]
Using both requests at the midpoint instead gives risk \(7/192\), which is strictly larger.

## Assumptions and scope
The bridge is centered Gaussian with covariance \(K(s,t)=\min(s,t)-st\), conditioned to vanish at both endpoints. The two observation statuses form a joint Bernoulli vector independent of the Gaussian path, with equal success probability \(p\) and joint success probability \(q\); no assumption of status independence is made. Both query locations are chosen *before* observing statuses or path values. The posterior mean uses the available observations exactly (no additional measurement noise). The criterion is \(R(a,b;p,q)=\mathbb E[(J-\mathbb E[J\mid\text{available observations and statuses}])^2]\). Coincident requests are allowed, with the same path value seen twice if both succeed. The symmetry in the formula refers to the set of locations; exchanging request labels is immaterial because their marginals agree.

## Proof
**1. Conditional integral variances.** The Brownian bridge decomposes conditionally into independent smaller Brownian bridges on the gaps between observed sites and the known endpoints. The variance of an integral over a bridge interval of length \(\ell\) is \(\ell^3/12\). Thus, with \(f(t)=t^3+(1-t)^3\) and \(g(a,b)=a^3+(b-a)^3+(1-b)^3\), the posterior variances after zero, one at \(t\), or two readings at \(a\le b\) are respectively \(1/12\), \(f(t)/12\), and \(g(a,b)/12\). These identities extend continuously to coincident sites.

**2. Exact risk and global uniqueness.** The four possible observation-status probabilities are \(1-2p+q\), \(p-q\), \(p-q\), and \(q\), so
\[
12R(a,b;p,q)=1-2p+q+(p-q)[f(a)+f(b)]+qg(a,b).\tag{1}
\]
The function \(f\) is strictly convex on \([0,1]\). The function \(g\) is also strictly convex on the ordered triangle \(0\le a\le b\le1\): it is the sum of cubes of the three nonnegative gaps \((a,b-a,1-b)\), and the gap vector is an injective affine function of \((a,b)\); the cube is strictly convex on nonnegative arguments. Since \(p>0\), at least one of \(p-q\) and \(q\) is strictly positive, and the right-hand side of (1) is strictly convex. Consequently there is exactly one minimizing ordered pair. Reflection \((a,b)\mapsto(1-b,1-a)\) preserves (1), so the unique minimizer satisfies \(a+b=1\).

**3. Exact minimizer.** Write \(a=1/2-d\), \(b=1/2+d\), where \(0\le d\le1/2\). Equation (1) reduces to
\[
12R(d;p,q)=1-2p+q+(p-q)\left(\frac12+6d^2\right)
+q\left(\frac14-\frac32d+3d^2+6d^3\right).\tag{2}
\]
Differentiation yields
\[
\frac{d}{dd}(12R)=\frac32\left[12qd^2+(8p-4q)d-q\right].\tag{3}
\]
For \(q=0\), equation (3) is strictly positive at positive \(d\), so the minimum is at \(d=0\). For \(q>0\), it is negative at zero and positive at \(d=1/2\), while the derivative is strictly increasing because \(p>0\). Its unique nonnegative zero is the displayed radical. Equivalently the optimizer satisfies
\[
\frac qp=\frac{8d_*}{1+4d_*-12d_*^2}.\tag{4}
\]
The right-hand side increases strictly for \(0\le d\le1/6\), as its derivative is \(8(1+12d^2)/(1+4d-12d^2)^2>0\), and ranges from zero to one. This proves the separation bounds, endpoints and strict dependence on \(q/p\).

**4. Correlation penalty after optimization.** For a fixed design, differentiate (1) in \(q\) to obtain the exact factorization
\[
12\,\partial_qR=1-f(a)-f(b)+g(a,b)=3a(1-b)(1+b-a).\tag{5}
\]
The unique optimal sites satisfy \(1/3\le a_*\le1/2\le b_*\le2/3\), so the right side of (5) is strictly positive. The unique optimizer varies continuously with \(q\), and the envelope theorem (also valid one-sided at the endpoints) yields the displayed positive derivative of \(R_*\). This proves strict worsening of optimal risk as \(q\) increases at fixed \(p\).

**5. Independent-delivery benchmark.** Substitution \(p=1/2,q=1/4\) into (3) gives \(d_*=1/\sqrt3-1/2\). Substitution into (2) gives \(R_*=1/12-\sqrt3/36\). At \(d=0\), (2) gives \(R=7/192\), verifying a strict gain from distinct sites.

## Verification
Run `python verify.py` using Python 3.10+ and SymPy from this package. The verifier checks the algebraic identities (2), (3), (5), the derivative in (4), exact Gram-matrix Gaussian-conditioning formulas for rational locations including repeated sites, the exact independent-delivery benchmark, and thousands of supplementary finite-grid comparisons across feasible \((p,q)\). These computational checks are independent tests of the manipulations; the strict convexity, factorization and envelope arguments above prove the all-parameter claims.

## Relationship to prior work
The Brownian-bridge fixed-node residual-variance formula is prior knowledge: the published *Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature* identifies \(\sum\text{gap}^3/12\) and optimizes an **i.i.d. random distribution of node positions without erasures**, rather than two predetermined locations subject to possibly correlated missing readings. *Exact optimal nodes and stratification penalty for Ornstein–Uhlenbeck Bayesian quadrature* treats a different covariance kernel and fully observed sites. Karvonen, Kanagawa and Särkkä (2018 preprint) give general Gaussian-process quadrature-conditioning and weight results, not the closed-form optimum for jointly unavailable Brownian-bridge readings. Santin (2022) studies Brownian-bridge interpolation/power-function optimal nodes, not this missing-data scalar-integral objective. Briol et al. (2017) study choosing a sampling law for kernel quadrature rather than delivery-status correlation. The novelty asserted here is the **complete joint-Bernoulli two-site optimum and strict correlation penalty**, not the classical Gaussian conditioning formula or the fixed-node cubic-gap identity.

## Limitations
The result is for exactly two nonadaptive, equally reliable noiseless readings of a standard pinned bridge, and for estimating its linear integral. It does not imply results for arbitrary Gaussian kernels, observation noise, heterogeneous marginal success rates, more than two sites, adaptive scheduling, or quadratic path functionals. Literature searches cannot prove exhaustive historical priority; possible older unlocated correlated-erasure sensor-design work is a residual originality risk. Scientific conclusions have not undergone independent validation.

## References
1. T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509v1, first public 2018-12-20, https://arxiv.org/abs/1812.08509.
2. G. Santin, *Equally spaced points are optimal for Brownian Bridge kernel interpolation*, arXiv:2210.15959v1, first public 2022-10-28, https://arxiv.org/abs/2210.15959.
3. F.-X. Briol, C. J. Oates, J. Cockayne, W. Y. Chen and M. Girolami, *On the Sampling Problem for Kernel Quadrature*, arXiv:1706.03369v1, first public 2017-06-11, https://arxiv.org/abs/1706.03369.
4. *Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-unique-optimal-i-i-d-two-node-design-for-brownian-bridge-kernel--1c7b05ec88c4.
5. *Exact optimal nodes and stratification penalty for Ornstein–Uhlenbeck Bayesian quadrature*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-optimal-nodes-and-stratification-penalty-for-ornstein-uhle--971795799fba.
6. S. Decorte et al., *Missing Value Imputation of Wireless Sensor Data for Environmental Monitoring*, 2024, https://pmc.ncbi.nlm.nih.gov/articles/PMC11053546/ (missing-reading motivation, not a priority claim).
