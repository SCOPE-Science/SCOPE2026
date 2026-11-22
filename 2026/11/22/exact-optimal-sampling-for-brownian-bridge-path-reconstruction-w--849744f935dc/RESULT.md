# Exact optimal sampling for Brownian-bridge path reconstruction with independent observation erasures

## Finding
Let \(B\) be a standard Brownian bridge on \([0,1]\). Fix an integer \(n\ge1\) and a delivery probability \(p\in(0,1]\). Choose \(n\) deterministic sample times before learning which observations are delivered; the observations at distinct times are independently delivered with probability \(p\), and delivery indicators are observed. Given the delivered exact bridge values and the known zero endpoint values, use the conditional-mean reconstruction \(\widehat B\).

Among all ordered sampling times \(0\le t_1\le\cdots\le t_n\le1\), the **unique** minimizer of the integrated, averaged path-reconstruction risk
\[
\mathcal R(t_1,\ldots,t_n)
=\mathbb E\!\left[\int_0^1(B(s)-\widehat B(s))^2\,ds\right]
\]
is
\[
\boxed{\displaystyle t_i^*=\frac{1+(i-1)p}{2+(n-1)p},\qquad i=1,\ldots,n.}
\]
The sharp minimum is
\[
\boxed{\displaystyle \mathcal R_{\min}(n,p)=\frac{2-p}{6[2+(n-1)p]}.}
\]
The boundary margins are both \(1/[2+(n-1)p]\), and every interior gap equals \(p/[2+(n-1)p]\). For any fixed \(n\ge2\), the samples converge to the midpoint as \(p\downarrow0\) and become equally spaced with endpoint margins at \(p=1\). For fixed \(p>0\), \(n\mathcal R_{\min}(n,p)\to(2-p)/(6p)\) as \(n\to\infty\).

## Assumptions and scope
The Gaussian process is centered with covariance \(K(s,t)=\min(s,t)-st\), pinned at \(B(0)=B(1)=0\). Samples are **exact conditional on delivery**; failed transmissions provide no sample value. Each candidate site has the same independent success probability \(p\), regardless of process values and all other delivery indicators. Times are nonadaptive, and the estimator is the posterior mean under the stipulated Brownian-bridge model; its conditional uncertainty does not depend on the received values. The loss integrates mean-square reconstruction error over the full unit interval. Relabeling unordered sites has no effect; uniqueness means uniqueness after sorting. The possibility of coincident or endpoint sample times is included in the feasible set.

## Proof
**1. Conditional error on observed gaps.** For an observed set of distinct times \(0=u_0<u_1<\cdots<u_k<u_{k+1}=1\), the conditional mean is linear on each gap. On a gap of length \(\ell\), the conditional error is a centered bridge with variance \(v(\ell-v)/\ell\) at displacement \(v\in[0,\ell]\). Its integrated variance is \(\ell^2/6\). The formula extends continuously to repeated times, which add no information. Therefore, defining
\[
Q(t)=6\mathcal R(t)=\mathbb E\sum_{j=0}^k(u_{j+1}-u_j)^2,
\]
where the expectation is over independently retained indices, is exact (including the no-delivery event, whose squared-gap sum is \(1\)).

**2. Exact quadratic and strict convexity.** Write \(q=1-p\). For any retained indices, expanding the sum of gap squares and averaging yields
\[
Q(t)=1+2p\sum_{i=1}^n t_i^2
-2p^2\sum_{1\le i<j\le n}q^{j-i-1}t_it_j
-2p\sum_{i=1}^nq^{n-i}t_i.
\tag{1}
\]
Indeed, the probability that indices \(i,j\) are consecutive among retained sites is \(p^2q^{j-i-1}\); the probability that \(i\) is the last retained index is \(pq^{n-i}\). For \(p=1\), interpret the term with exponent zero as \(1\).

Every fixed-retention-pattern squared-gap sum is convex in the ordered times. The all-sites-retained event, of probability \(p^n>0\), contributes the positive-definite quadratic form \(\sum_{i=0}^n(t_{i+1}-t_i)^2\), with \(t_0=0,t_{n+1}=1\): its Hessian in the free times is twice the positive-definite Dirichlet path tridiagonal matrix. Thus \(Q\) is **strictly convex** on the entire ordered feasible simplex for every \(p>0\).

**3. Exact stationary configuration.** Conditional on site \(i\) being retained, let \(L_i\) and \(R_i\) be the distances from it to the nearest retained site or fixed endpoint on the left and right. Differentiating each squared-gap sum, then averaging, gives
\[
\frac{\partial Q}{\partial t_i}=2p\,\mathbb E[L_i-R_i\mid i\text{ retained}].
\tag{2}
\]
Put \(D=2+(n-1)p\), \(b=1/D\), and \(d=p/D=pb\). The candidate sites are \(t_i=b+(i-1)d\); their terminal margins are \(b\), and their inner gaps are \(d\). The probability that each of the first \(k\) preceding sites has failed is \(q^k\). Summing the expected left-hand gap gives
\[
\mathbb E[L_i\mid i\text{ retained}]
=d\sum_{k=0}^{i-2}q^k+bq^{i-1}
=\frac{d}{p}(1-q^{i-1})+bq^{i-1}=b.
\]
The analogous right-hand calculation also equals \(b\). Equation (2) therefore vanishes in every coordinate at the candidate, which lies in the strict interior of the feasible simplex. By strict convexity, it is the unique global optimum, including against coincident-node and endpoint alternatives.

**4. Value of the minimum.** Separate the quadratic and linear terms in (1) and use Euler's identity at the stationary point: its quadratic part equals \(p\sum_{i=1}^nq^{n-i}t_i^*\), so
\[
Q(t^*)=1-p\sum_{i=1}^n q^{n-i}t_i^*.
\]
The identity
\[
\sum_{k=0}^{n-1}q^k[1+(n-1-k)p]
=\sum_{k=0}^{n-1}[(n-k)q^k-(n-k-1)q^{k+1}]=n
\]
yields \(Q(t^*)=1-np/D=(2-p)/D\), which gives the stated risk after division by \(6\).

The limit statements follow by direct substitution. There is no assertion of a unique minimizer at \(p=0\): without delivered samples, every placement has risk \(1/6\).

## Verification
The standalone `check.py` uses exact rational arithmetic and enumerates every delivered subset for \(1\le n\le7\) at five rational probabilities, including \(p=1\). It independently matches the subset formula against the quadratic identity (1), verifies the claimed exact minimum and all coordinate derivatives, and tests small feasible perturbations. Running `python3 check.py` produced `check_output.txt`: 405 exact-rational assertions passed. The finite checks are supplementary; the proof of global uniqueness for arbitrary \(n\) and \(p\) is analytic.

## Relationship to prior work
Friedrich, Gallon, Pumir and Grauer (2020) give the Gaussian multipoint bridge reconstruction mechanism, also for nonuniform sites and fractional Brownian models, but their model selection concerns a Hurst exponent, not the design of sites surviving independent erasures. Peng, Chen and Gong (first public 2021) optimize causal Wiener-process sampling under random delivery **delay**, a distinct online setting rather than a fixed-grid Brownian-bridge erasure risk. Santin (2022, Theorem 5) proves the unique equal-spacing optimum for the **supremum** power-function error without missing observations; its noiseless subcase agrees with the endpoint \(p=1\) of the present integrated-error result but does not imply the erasure-dependent design at \(0<p<1\). Frasca, Garin, Gerencsér and Hendrickx (2015) optimize failure-robust **worst-distance coverage**, not integrated posterior path variance. Related Brownian-bridge *integral* estimation under dropout minimizes the posterior variance of one linear functional, with a cubic-gap objective; the present trace-of-covariance loss has a squared-gap objective, and neither optimality statement implies the other. This distinction matters quantitatively: the present small-delivery adjacent-gap coefficient is \(p/2+O_n(p^2)\), rather than the \(p/4\) coefficient of the nearby integral-functional design.

## Limitations
The analysis excludes additive measurement noise, location-dependent or correlated failures, unobserved delivery indicators, adaptive sampling, and covariance misspecification. Exact interpolation of the observed path is not exact recovery of an unobserved Brownian trajectory. The mathematical result is self-contained but its historical priority has not been independently established; a related unavailable 2012 spatial-estimation paper remains a literature risk. No general Gaussian-process kernel claim follows from the squared-gap calculation.

## References
- J. Friedrich, S. Gallon, A. Pumir and R. Grauer, *Stochastic interpolation of sparsely sampled time series via multi-point fractional Brownian bridges*, arXiv:2005.07591 (first posted 2020-05-15); Phys. Rev. Lett. 125, 170602 (2020). https://arxiv.org/abs/2005.07591
- F. Peng, X. Chen and J. Gong, *Optimal sampling policy of multi-dimensional Wiener processes with random delivery time*, first published 2021-10-11, DOI:10.1049/cth2.12205. https://doi.org/10.1049/cth2.12205
- G. Santin, *Equally spaced points are optimal for Brownian Bridge kernel interpolation*, arXiv:2210.15959 (first posted 2022-10-28); Appl. Math. Lett. 2023. https://arxiv.org/abs/2210.15959
- P. Frasca, F. Garin, B. Gerencsér and J. M. Hendrickx, *Optimal One-Dimensional Coverage by Unreliable Sensors*, SIAM J. Control Optim. 53 (2015), 3120–3140, arXiv:1404.7711. https://arxiv.org/abs/1404.7711
- J. Cortés, *Deployment of an unreliable robotic sensor network for spatial estimation*, Systems & Control Letters 61 (2012), 41–49, DOI:10.1016/j.sysconle.2011.10.007.
