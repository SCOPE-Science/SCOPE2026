# Universal optimal sensing meshes under a Brownian-bridge precision budget

## Finding

**Theorem (all finite measurement budgets).** Let \(B\) be the centered standard Brownian bridge on \([0,1]\), with covariance \(K(s,t)=\min(s,t)-st\), and let \(J=\int_0^1 B(t)\,dt\). Fix any integer \(n\ge1\) and any total measurement precision \(P>0\). A design specifies \(n\) deterministic sites \(t_i\in[0,1]\) and nonnegative precisions \(p_i\) with \(\sum_{i=1}^n p_i=P\); for positive precision, \(Y_i=B(t_i)+\varepsilon_i\), with independent centered Gaussian noises having variance \(1/p_i\), independent of \(B\). Zero precision means the observation is not used. Minimize the unconditional mean-square error of the exact conditional-mean estimator \(\mathbb E[J\mid Y_1,\ldots,Y_n]\) across all such designs, including coincident nodes and inactive sensors.

There is exactly one optimum up to relabeling. Define \(W=W_{n,P}\in(0,n/(n+1))\) as the unique solution of
\[
(1-W)^2-\frac{W^2}{n^2}=\frac{8W}{P}.
\]
The optimal design, weights in its posterior-mean quadrature rule, and its minimum risk are
\[
\boxed{\ p_i=\frac{P}{n},\quad t_i=\frac{1-W}{2}+\frac{i-\tfrac12}{n}W,\quad w_i=\frac{W}{n}\quad(1\le i\le n),\ }
\]
\[
\boxed{\ R_{n,P}=\frac{(1-W)^3+W^3/n^2}{12}+\frac{W^2}{P}.\ }
\]
The full fixed-budget optimization is therefore uniquely symmetric, uses all available sensors, distributes precision equally, and puts the sensors at equal separations within a centered interval of width \(W\). An equivalent explicit root is
\[
W=\frac{2}{2+8/P+\sqrt{(2+8/P)^2-4(1-n^{-2})}}.
\]
The formula applies at \(n=1\) without any limiting interpretation. For each fixed \(P>0\), \(R_{n,P}\) decreases strictly with \(n\). At fixed \(n\), \(W\uparrow n/(n+1)\) as \(P\to\infty\), recovering sites \(i/(n+1)\) and risk \(1/[12(n+1)^2]\); as \(P\downarrow0\), \(W=P/8+O(P^2)\) and the sites cluster around \(1/2\).

## Assumptions and scope

The covariance is normalized exactly as stated, integration is against Lebesgue measure on \([0,1]\), noise terms are mutually independent and independent of the bridge, and measurement quality is charged by the *sum of inverse noise variances*. No spatial constraints, minimum distinct-site separation, fixed individual precisions, adaptivity, non-Gaussian observation noise, or prior uncertainty are included. A zero-precision channel is omitted from conditioning. The theorem optimizes the Bayesian posterior variance of the scalar integral, not the integrated pointwise prediction error of the entire bridge.

## Proof

**1. Gaussian regression and a deterministic dual.** One may realize \(B(t)=\int_0^1(\mathbf 1_{\{s\le t\}}-t)\,dW_s\) for a standard Wiener process \(W\). Consequently, \(J=\int_0^1 a(s)\,dW_s\) where \(a(s)=1/2-s\). For any real coefficients \(w_i\), define the mean-zero step function
\[
g(s)=\sum_{i=1}^n w_i(\mathbf1_{\{s\le t_i\}}-t_i).
\]
The risk of the linear estimate \(\sum_i w_iY_i\) is exactly
\[
\|a-g\|_{L^2(0,1)}^2+\sum_{i:p_i>0}\frac{w_i^2}{p_i},
\]
where an inactive channel must have coefficient zero. Gaussian conditioning makes the minimizing coefficients the conditional-mean coefficients. For fixed coefficients, Cauchy–Schwarz gives the exact optimum over the precision budget,
\[
\min_{p_i\ge0,\ \sum p_i=P}\sum_i\frac{w_i^2}{p_i}
=\frac{(\sum_i|w_i|)^2}{P},
\]
attained by \(p_i=P|w_i|/\sum_j|w_j|\) for nonzero coefficients (with the usual zero-coefficient convention). Thus the joint problem is a best step approximation of \(a\) penalized by squared total variation.

**2. Positive weights and a bounded total jump.** A mean-zero step function with at most \(n\) jumps has a decreasing rearrangement with the same integral and \(L^2\) norm, at most \(n\) jumps, and total variation no larger than the original jump-total \(\sum|w_i|\). Since \(a\) is strictly decreasing, swapping any two out-of-order step values on intervals of equal positive length strictly increases \(\int ag\); iteration or the elementary rearrangement inequality proves the rearranged function has no larger risk, strictly improving a nonmonotone one. Every mean-zero decreasing step function is representable in the above form with \(w_i\ge0\). Write \(W=\sum_i w_i\), the total downward jump. If \(W>1\), clip the step values to the range \([-1/2,1/2]\) of \(a\), then subtract the clipped function's mean. Clipping strictly decreases the squared distance to \(a\) on a positive-length cell, centering cannot increase that distance (because \(a\) has mean zero), and the new total jump is at most one. Its precision penalty is not larger. Thus no optimum has \(W>1\), and it suffices to optimize \(w_i\ge0\) with \(0\le W\le1\).

**3. Best nodes for given weights.** For ordered sites and nonnegative weights, use the covariance and kernel mean identities
\[
K(t_i,t_j)=t_i(1-t_j)\ (i\le j),\qquad \operatorname{Cov}(J,B(t))=t(1-t)/2.
\]
The quantity \(\operatorname{Var}(J)-\operatorname{Var}(J-\sum_iw_iB(t_i))\) is the quadratic expression
\[
F(t)=\sum_iw_i(1-w_i)t_i(1-t_i)-2\sum_{i<j}w_iw_jt_i(1-t_j).
\]
Its Hessian is \(-2[\operatorname{diag}(w)-ww^\mathsf T]\), negative semidefinite for \(W\le1\) by weighted Cauchy–Schwarz and negative definite when \(W<1\) and every weight is positive. Direct differentiation gives stationary positions
\[
t_i^*=\frac{1-W}{2}+\sum_{j<i}w_j+\frac{w_i}{2}.
\]
These are ordered and in \([0,1]\) for \(W\le1\); concavity proves global maximality (uniqueness for positive weights and \(W<1\)). Substituting and collecting cubic terms yields the exact fixed-weight identity
\[
\min_{0\le t_1\le\cdots\le t_n\le1}
\operatorname{Var}\left(J-\sum_iw_iB(t_i)\right)
=\frac{(1-W)^3+\sum_i w_i^3}{12}.
\]
The same identity extends by continuity to zero weights and \(W=1\).

**4. Equal allocation and the sharp scalar minimizer.** Strict convexity of \(z\mapsto z^3\) for nonnegative \(z\) gives \(\sum_iw_i^3\ge W^3/n^2\), with equality (when \(W>0\)) only if \(w_i=W/n\). The minimum precision penalty is \(W^2/P\), uniquely attained by equal precision for equal positive weights. Therefore every admissible design has risk at least
\[
\Phi(W)=\frac{(1-W)^3+W^3/n^2}{12}+\frac{W^2}{P},\quad0\le W\le1.
\]
Here \(\Phi'(0)=-1/4<0\), \(\Phi'(1)=1/(4n^2)+2/P>0\), and
\[
\Phi''(W)=\frac{1-W}{2}+\frac{W}{2n^2}+\frac{2}{P}>0.
\]
Thus there is exactly one minimizing \(W\in(0,1)\), determined by the displayed quadratic equation. Substitution gives the design and posterior weights in the theorem. Every equality condition is strict away from permutations of that design. Since the derivative of \(\Phi\) at \(W=n/(n+1)\) equals \(2W/P>0\), the minimizer is smaller than that noiseless value. Strict reduction in the cubic term when \(n\) increases gives strict improvement in the optimal risk. The limit and small-budget expansion follow from the scalar equation.

## Verification

Run `python verify.py` with NumPy installed. This independently evaluates rational covariance identities for several dimension and weight patterns, checks Gaussian-conditioning coefficient equations and posterior variances for multiple budgets, and compares 4,500 nonoptimal randomly drawn designs to the theorem. These finite tests supplement the preceding all-parameter proof and do not substitute for it. In an exact three-sensor example, \(n=3\), \(P=18\) gives \(W=1/2\), sites \(1/3,1/2,2/3\), each precision \(6\), each regression weight \(1/6\), and risk \(11/432\).

## Relationship to prior work

Karvonen, Kanagawa and Särkkä (2018 preprint) establish properties of Bayesian quadrature weights and locally variance-optimal nodes, not a jointly optimized allocation of site locations and an inverse-noise-variance budget. Santin, Karvonen and Haasdonk (2020 preprint) treat nodal approximation of linear functionals by kernel methods, especially greedy and quasi-uniform convergence, but do not state this exact all-budget global optimizer. Santin (2022 preprint) proves equally spaced nodes minimize a Brownian-bridge interpolation power-function criterion, distinct from the *scalar integrated* posterior variance optimized here. The noiseless equally spaced integral-quadrature design and the equal-noise two-observation case are special cases already covered by earlier mathematical work and are **not** separately claimed as novel. The additional result is the all-\(n\) global allocation rigidity, the common precision budget's exact scalar law, and its proof against every asymmetric or partially inactive design.

## Limitations

This is an exact idealized result for the centered unit Brownian-bridge Gaussian prior and the stated precision-cost model. No guarantee is made for unknown covariance parameters, kernels with different shape, heteroscedastic per-unit costs, noisy derivative observations, adaptive sampling, interpolation maximum-error criteria, or general finite-cost physical sensors. An older unpublished or inaccessible exact design theorem could affect publication priority; the available comparisons do not establish absolute novelty. The supporting numerical tests are finite, while the proof is analytic.

## References

- T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509v1, first publicly posted 20 December 2018. https://arxiv.org/abs/1812.08509
- G. Santin, T. Karvonen and B. Haasdonk, *Sampling based approximation of linear functionals in Reproducing Kernel Hilbert Spaces*, arXiv:2004.00556v1, first publicly posted 1 April 2020. https://arxiv.org/abs/2004.00556
- G. Santin, *Equally spaced points are optimal for Brownian Bridge kernel interpolation*, arXiv:2210.15959v1, first publicly posted 28 October 2022. https://arxiv.org/abs/2210.15959
- B. Mukherjee, *Optimal designs for estimating the path of a stochastic process*, doctoral dissertation (bibliographic abstract; full text not accessed). https://docs.lib.purdue.edu/dissertations/AAI3043760/
