# Bandwidth-driven separation in two-request Green-kernel quadrature with erased observations

## Finding

Let \(\kappa>0\), \(0<p<1\), and let \(X_\kappa\) be the centered Gaussian process on \([0,1]\) with Dirichlet Green covariance
\[
K_\kappa(s,t)=\frac{\sinh(\kappa\min\{s,t\})\sinh(\kappa(1-\max\{s,t\}))}{\kappa\sinh\kappa}.
\]
The scalar target is \(J=\int_0^1X_\kappa(t)\,dt\). Two predetermined exact observation requests, at \(0\le x\le y\le1\), are independently delivered with the same probability \(p\). Erasures are known; the estimate of \(J\) is its Gaussian conditional mean given the delivered observations. The objective is its expected posterior variance, averaging only over delivery patterns.

Define, for \(h\ge0\),
\[
g_\kappa(h)=\frac{h}{\kappa^2}-\frac{2}{\kappa^3}\tanh\left(\frac{\kappa h}{2}\right),
\qquad H_\kappa(h)=\tanh^2\left(\frac{\kappa h}{2}\right).
\]
The expected posterior variance is exactly
\[
\begin{aligned}
R_{\kappa,p}(x,y)={}&(1-p)^2g_\kappa(1)\\
&+p(1-p)\bigl[g_\kappa(x)+g_\kappa(1-x)+g_\kappa(y)+g_\kappa(1-y)\bigr]\\
&+p^2\bigl[g_\kappa(x)+g_\kappa(y-x)+g_\kappa(1-y)\bigr].
\end{aligned}
\]
For **every** \(\kappa>0\) and \(0<p<1\), the unique global minimizer (with points ordered) is
\[
(x_*,y_*)=\left(\frac{1-u_{\kappa,p}}2,\frac{1+u_{\kappa,p}}2\right),
\]
where \(u_{\kappa,p}\) is the **unique** number in \((0,1/3)\) satisfying, with \(a=(1-u)/2\), \(b=(1+u)/2\),
\[
(1-p)[H_\kappa(b)-H_\kappa(a)]=p[H_\kappa(a)-H_\kappa(u)]. \tag{1}
\]
The optimal separation \(u_{\kappa,p}\) is strictly increasing in **both** \(\kappa\) (for fixed \(p\)) and \(p\) (for fixed \(\kappa\)). Its limits are
\[
\begin{aligned}
\lim_{\kappa\downarrow0}u_{\kappa,p}
&=\frac{p}{2-p+\sqrt{(2-p)^2+3p^2}},\\
u_{\kappa,p}&=\frac13-\frac{2\log(1/p)}{3\kappa}+o(\kappa^{-1})
\qquad(\kappa\to\infty).
\end{aligned}
\]
For each fixed \(\kappa>0\), \(u_{\kappa,p}\downarrow0\) as \(p\downarrow0\) and \(u_{\kappa,p}\uparrow1/3\) as \(p\uparrow1\). When \(p=1\) the unique optimum is the trisection pair \((1/3,2/3)\) for all \(\kappa\). The zero-tension formula is a known Brownian-bridge limiting case and is not asserted as new.

## Assumptions and scope

The covariance is normalized as the inverse of \(-\partial_t^2+\kappa^2\) with both endpoint values pinned to zero. The two requests are nonadaptive, may initially be placed anywhere in the closed interval, and produce noiseless process values when delivered. The Bernoulli delivery indicators are independent of one another and of the process. Their common success probability \(p\) and the kernel parameter \(\kappa\) are known. The estimator conditions on the observed delivery pattern. The loss is unconditional mean-square error of the posterior mean for the **integral**, not integrated pointwise path-reconstruction error. The theorem concerns two requests, not a general number of sensors.

## Proof

**1. Gaussian Green bridge decomposition.** If exact values are conditioned on at an ordered set of points and the fixed Dirichlet endpoints are included, the conditional covariance vanishes across the resulting disjoint open gaps. Within each gap of length \(h\), it is exactly the Dirichlet Green kernel of \(-\partial_t^2+\kappa^2\) on that gap, by the one-dimensional Gaussian Markov property (or directly by taking the Schur complement of the stated Green kernel). To calculate the integral variance of one gap, solve \((-\partial_t^2+\kappa^2)v=1\) with \(v(0)=v(h)=0\). The solution is
\[
v(t)=\kappa^{-2}\left[1-\frac{\cosh(\kappa(t-h/2))}{\cosh(\kappa h/2)}\right].
\]
Its integral is \(g_\kappa(h)\). Because conditional gap integrals are independent, the posterior integral variance is the sum of \(g_\kappa\) over all surviving gaps. Enumerating the four erasure patterns gives the displayed formula for \(R_{\kappa,p}\). The formula extends continuously to zero-length gaps and coincident requests.

**2. Strict global convexity and symmetry.** Direct differentiation gives
\[
g_\kappa'(h)=\kappa^{-2}H_\kappa(h),\qquad
g_\kappa''(h)=\kappa^{-1}\tanh(\kappa h/2)\operatorname{sech}^2(\kappa h/2)>0
\quad(h>0).
\]
Hence \(g_\kappa\) is strictly convex on \([0,\infty)\). For \(0<p<1\), the term multiplied by \(p(1-p)\) is strictly convex in the pair \((x,y)\), and the final term is convex; consequently \(R_{\kappa,p}\) is strictly convex on the closed triangle \(0\le x\le y\le1\). Reflection \((x,y)\mapsto(1-y,1-x)\) preserves this triangle and the objective, so the unique minimizer must satisfy \(x+y=1\).

Write \(x=a=(1-u)/2\), \(y=b=(1+u)/2\), \(0\le u\le1\). The derivative of the restricted objective divided by \(p\) is
\[
F_{\kappa,p}(u)=(1-p)[g_\kappa'(b)-g_\kappa'(a)]
+p[g_\kappa'(u)-g_\kappa'(a)].
\]
It is strictly increasing because the restricted objective is strictly convex. At \(u=0\), \(F_{\kappa,p}(0)=p[g_\kappa'(0)-g_\kappa'(1/2)]<0\); at \(u=1/3\), \(F_{\kappa,p}(1/3)=(1-p)[g_\kappa'(2/3)-g_\kappa'(1/3)]>0\). Thus there is precisely one root in \((0,1/3)\), it is an interior stationary point of the full symmetric objective, and strict convexity makes it the unique global optimum. Substituting \(g_\kappa'=H_\kappa/\kappa^2\) yields (1).

**3. Monotonicity in delivery probability.** For fixed \(\kappa\) and \(0<u<1/3\), define
\[
T_\kappa(u)=\frac{H_\kappa(b)-H_\kappa(a)}{H_\kappa(a)-H_\kappa(u)}.
\]
It increases strictly from zero to infinity as \(u\) runs from zero to \(1/3\): the numerator increases as \(a\) decreases and \(b\) increases, while the positive denominator decreases as \(u\) increases and \(a\) decreases. Equation (1) is \(T_\kappa(u)=p/(1-p)\). Thus the unique optimizer separation increases strictly with \(p\), and the stated \(p\)-endpoint limits follow.

**4. Strict monotonicity in inverse lengthscale.** Set
\[
w_\kappa(t)=H_\kappa'(t)=\kappa\tanh(\kappa t/2)\operatorname{sech}^2(\kappa t/2)>0\quad(t>0).
\]
For each fixed \(t>0\), with \(z=\kappa t\), direct differentiation gives
\[
\partial_\kappa\partial_t\log w_\kappa(t)
=\frac{\sinh z-z\cosh z}{\sinh^2 z}
-\tanh(z/2)-\frac z2\operatorname{sech}^2(z/2)<0.
\]
The first term is strictly negative since \(z\cosh z-\sinh z>0\) for \(z>0\), and so are the remaining two terms. Therefore for \(\kappa_2>\kappa_1\), the ratio \(w_{\kappa_2}(t)/w_{\kappa_1}(t)\) decreases strictly with \(t\). Integrating this strict likelihood-ratio ordering over the disjoint adjacent intervals \((a,b)\) and \((u,a)\) proves
\[
T_{\kappa_2}(u)=\frac{\int_a^bw_{\kappa_2}(t)\,dt}{\int_u^aw_{\kappa_2}(t)\,dt}
<T_{\kappa_1}(u).
\]
Since \(T_\kappa(u)\) increases strictly with \(u\), the equality \(T_\kappa(u_{\kappa,p})=p/(1-p)\) forces \(u_{\kappa,p}\) to increase strictly with \(\kappa\).

**5. Exact limits.** Uniformly on compact \(t\)-intervals, \(H_\kappa(t)/\kappa^2\to t^2/4\) as \(\kappa\downarrow0\). Equation (1) becomes \(3pu^2+(4-2p)u-p=0\); its unique positive root is the displayed radical. For fixed \(p>0\), strict monotonicity ensures a limit \(u_\infty\le1/3\). If this limit were below \(1/3\), then the upper-to-lower ratio \(T_\kappa(u_{\kappa,p})\) would tend to zero exponentially, contradicting its fixed positive value \(p/(1-p)\). Hence \(u_\infty=1/3\). Rewriting (1) as
\[
\operatorname{sech}^2(\kappa a/2)=(1-p)\operatorname{sech}^2(\kappa b/2)+p\operatorname{sech}^2(\kappa u/2)
\]
and using \(\operatorname{sech}^2(\kappa t/2)=4e^{-\kappa t}(1+o(1))\) for \(t\to1/3\) or \(2/3\), we obtain \(e^{-\kappa a}=p e^{-\kappa u}(1+o(1))\). Therefore \(\kappa(a-u)=\log(1/p)+o(1)\). Since \(a-u=(1-3u)/2\), this gives the stated sharp first-order high-tension separation law. For \(p=1\), ordinary Jensen strict convexity for the three gap lengths makes the trisection design unique.

## Verification

The standalone standard-library program `verify_bridge_dropout.py` computes the conditional integral variance a second way, from the direct one- and two-point Gaussian Schur complements using the closed Green kernel and the integral-kernel representer. It checks the equality against all erasure-pattern gap formulas at randomized parameters, tests the analytic root against its zero-tension radical, compares it against a two-dimensional grid of alternative placements, and checks parameter monotonicity and the high-tension coefficient. The program completed 6,443 assertions. Representative values for \(p=1/2\) are \(u_{0,p}=0.15470053837925152\), \(u_{2,p}=0.17226319454732714\), and \(u_{10,p}=0.2854007926144019\). Finite numerical checks support identities only; the proof of uniqueness, monotonicity, and all continuum claims is analytic above.

## Relationship to prior work

Karvonen, Kanagawa and Särkkä (2018) establish the Gaussian-process Bayesian-quadrature variance framework and investigate positive weights and locally optimal designs. Santin (2022) derives this same Dirichlet Green-kernel family and proves equally spaced nodes minimize the maximum pointwise interpolation power function with no erased observations; that is a different loss and delivery model. The public result *Exact optimal nodes and stratification penalty for Ornstein–Uhlenbeck Bayesian quadrature* (2026) provides an all-node integral-variance design theorem for a stationary, **unpinned** exponential covariance without erasures; its terminal gap cost differs from the Dirichlet one. The zero-tension Brownian-bridge two-request optimizer is already available and is only recovered as a check, not claimed as new. None of these inspected statements implies the strict \(\kappa\)-dependent two-request erasure design, its two-parameter monotonicity, or the logarithmic high-tension spacing correction. An undiscovered equivalent result remains possible.

## Limitations

Two requests only, independent equal-probability erasures, known kernel shape and known zero mean, exact delivered observations, and zero endpoint values are essential. No assertion is made for noisy values, unequal or dependent delivery, more sites, unknown covariance, adaptive placement, unpinned stationary kernels, or a different integral measure. Historical priority is provisional; the numerical tests alone do not establish infinite-parameter assertions. The related earlier Brownian-limit formula must not be counted as a new theorem.

## References

1. T. Karvonen, M. Kanagawa and S. Särkkä, *On the Positivity and Magnitudes of Bayesian Quadrature Weights*, arXiv:1812.08509v1, first public 2018-12-20, https://arxiv.org/abs/1812.08509; full-text revision https://arxiv.org/html/1812.08509v2.
2. G. Santin, *Equally Spaced Points Are Optimal for Brownian Bridge Kernel Interpolation*, arXiv:2210.15959v1, first public 2022-10-28, https://arxiv.org/abs/2210.15959.
3. *Exact optimal nodes and stratification penalty for Ornstein–Uhlenbeck Bayesian quadrature*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-optimal-nodes-and-stratification-penalty-for-ornstein-uhle--971795799fba.
