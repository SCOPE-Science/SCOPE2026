# Exact free-boundary monitoring design for a one-dimensional exponential-covariance geostatistical field

## Finding
Consider a continuous environmental transect of length \(L>0\), sampled without noise at \(n\ge2\) freely chosen sites. Under a known stationary Gaussian field with covariance \(\sigma^2 e^{-\theta |s-t|}\), \(\sigma,\theta>0\), and known mean, there is exactly one ordered design minimizing *integrated pointwise simple-kriging prediction variance* over the whole transect. It has a symmetric pair of nonzero terminal margins and identical interior gaps. Its terminal margins are **strictly shorter** than its interior gaps for every positive transect length and every \(n\ge2\).

More precisely, with \(X=\theta L\), the unique positive pair \((a,d)\) satisfies
\[
2a+(n-1)d=X,\qquad 1-e^{-2a}=\coth d-d\operatorname{csch}^2d.
\]
The optimal sites are \(x_i=(a+(i-1)d)/\theta\), for \(1\le i\le n\), with \(0<a<d\). For \(X\downarrow0\),
\[
a=\frac{X}{3n-1}+O(X^2),\qquad d=\frac{3X}{3n-1}+O(X^2).\]
For fixed \(n\) and \(X\to\infty\),
\[
d=\frac{X}{n+1}+\frac{\log(4X/(n+1))}{n+1}+o(1),\]
\[
a=\frac{X}{n+1}-\frac{n-1}{2(n+1)}\log\left(\frac{4X}{n+1}\right)+o(1).\]
Thus the short-range or weakly correlated limit has an exact \(1:3\) terminal-to-interior gap ratio, while the terminal *absolute* deficit relative to each interior gap grows logarithmically in the long-transect regime.

## Assumptions and scope
Let \(Z(t)\), \(t\in[0,L]\), be a real-valued stationary Gaussian process with **known** deterministic mean and known covariance \(\operatorname{Cov}(Z(s),Z(t))=\sigma^2\exp(-\theta|s-t|)\), \(\sigma,\theta>0\). The process is observed exactly, without instrument error, at exactly \(n\ge2\) distinct points \(0\le x_1<\cdots<x_n\le L\), chosen continuously. Define
\[
\mathcal J(x_1,\ldots,x_n)=\int_0^L\operatorname{Var}\left(Z(t)\mid Z(x_1),\ldots,Z(x_n)\right)\,dt.
\]
The integral is over **pointwise conditional variances**, not the posterior variance of the integral of \(Z\). The result does not cover ordinary kriging with unknown mean, noisy measurements, covariance estimation, irregular spatial weighting, or multidimensional fields. It addresses one-dimensional environmental or river-transect geostatistical network design; no empirical river calibration is implied.

## Proof
**1. An exact additive objective.** By the Markov property of the exponential-covariance Gaussian process, conditional variance on a terminal interval at dimensionless distance \(z\) from the nearest site is \(\sigma^2(1-e^{-2z})\). Integrating over a terminal gap of dimensionless length \(u\) gives \(\sigma^2 G(u)/\theta\), where
\[G(u)=u-\frac{1-e^{-2u}}{2}.\]
For \(0<z<d\) between adjacent observations separated by dimensionless gap \(d\), the exact conditional bridge variance, divided by \(\sigma^2\), is
\[
\frac{(1-e^{-2z})(1-e^{-2(d-z)})}{1-e^{-2d}}.
\]
Its integral over \(z\in[0,d]\) is \(H(d)=d\coth d-1\), with continuous extension \(H(0)=0\). Introduce \(u=\theta x_1\), \(v=\theta(L-x_n)\) and \(d_i=\theta(x_{i+1}-x_i)\); then
\[
\frac{\theta}{\sigma^2}\mathcal J=G(u)+G(v)+\sum_{i=1}^{n-1}H(d_i),\qquad u+v+\sum_{i=1}^{n-1}d_i=X.
\]
This identity also holds by continuity when some gaps are zero, allowing the simplex boundary to be checked.

**2. Strict convexity and interiority.** For \(u\ge0\), \(G'(u)=1-e^{-2u}\) and \(G''(u)=2e^{-2u}>0\). For \(d>0\),
\[
H'(d)=\coth d-d\operatorname{csch}^{2}d,\quad H''(d)=2\operatorname{csch}^{2}d(d\coth d-1)>0.
\]
The last inequality follows from \(d\cosh d>\sinh d\) for \(d>0\), and \(H''(0)=2/3\). Furthermore \(G'(0)=H'(0)=0\), and both derivatives are strictly positive at positive arguments. Consequently no minimizer on the nonnegative gap simplex with \(X>0\) can have a zero component: shifting a small amount from any positive gap to any zero gap strictly lowers the objective to first order. The objective is strictly convex on the compact simplex, so it has exactly one minimizer, necessarily interior.

**3. Unique symmetric allocation.** Equality of Lagrange multipliers gives \(G'(u)=G'(v)=H'(d_i)\) for all \(i\). Strictly increasing derivatives force \(u=v=a\), and all \(d_i=d\). Since \(2a+(n-1)d=X\), this yields the stated unique pair and all optimal stations. For all \(d>0\), writing \(q=e^{-2d}\),
\[
G'(d)-H'(d)=\frac{q\,[4d-3+4q-q^2]}{(1-q)^2}>0.
\]
Indeed \(F(d)=4d-3+4e^{-2d}-e^{-4d}\) has \(F(0)=0\) and \(F'(d)=4(1-e^{-2d})^2>0\). Since \(G'\) is increasing and \(G'(a)=H'(d)<G'(d)\), necessarily \(0<a<d\). This also proves that designs constrained to both endpoints cannot be globally optimal for the unrestricted objective.

**4. Short-transect and long-transect laws.** Near zero, \(G'(a)=2a+O(a^2)\) and \(H'(d)=2d/3+O(d^3)\). Thus \(a=d/3+O(X^2)\); inserting into the sum constraint gives the first asymptotic pair. As \(X\to\infty\), both \(a\) and \(d\) diverge (otherwise the common positive derivative could not approach the limiting constraint), and the exact equality yields
\[
e^{-2a}=1-H'(d)=(4d-2)e^{-2d}+O(de^{-4d}).\]
Taking logarithms gives \(a=d-\tfrac12\log(4d)+o(1)\). Substitution into \(2a+(n-1)d=X\), using \(d\sim X/(n+1)\), establishes both displayed large-\(X\) expansions.

## Verification
The standalone `checker.py` numerically rederives minimizers from the scalar marginal-equation, independently integrates the Gaussian conditional covariance-matrix formula on grids, compares randomized nonnegative gap allocations against the proposed optimum, checks the short- and long-transect asymptotics, and compares numerical unconstrained optimization. It passed **1,192 individual diagnostic assertions** in a fresh run with NumPy and SciPy. These finite computations cross-check arithmetic and implementation; global uniqueness and inequalities are proved above, not inferred from numerical sampling.

For \(n=2\) and \(\theta L=1\), the optimal dimensionless positions are \(0.220985994768\) and \(0.779014005232\). The normalized integrated loss is \(0.186445202322\), compared with \(0.313035285499\) for compulsory endpoint sites. This is a **40.44%** relative reduction in the model's integrated prediction variance. The example is dimensionless and not an observed environmental effect.

## Relationship to prior work
Zimmerman (2006) motivates kriging-variance optimal network design and compares prediction-oriented versus covariance-estimation-oriented spatial monitoring, principally via finite two-dimensional grid examples; the examined full article does not establish the present one-dimensional unrestricted free-terminal theorem. Dasgupta, Mukhopadhyay and Keith (arXiv 2020; journal 2022) establish I-optimal **equispaced** designs for reduced cokriging models with an exponential-covariance primary process. Crucially their Section 5 restricts the observation domain to \([x_1,x_n]\), imposing \(x_1=0\) and \(x_n=1\) before its integrated-variance optimization (Theorem 5.2). Their interior-bridge formula is consistent with \(H\), but their fixed-endpoint theorem does not imply the new *nonzero shorter terminal margin* optimality condition. Conversely the present proof contains their known-mean fixed-endpoint special case by setting \(u=v=0\).

Sikolya and Baran (2019) similarly impose fixed endpoints for complex Ornstein–Uhlenbeck integrated-variance designs. Existing research on OU **Bayesian quadrature** optimizes posterior variance of an *integral*, a distinct quantity with different endpoint behavior; likewise results on condition numbers of exponential kernel matrices are not integrated pointwise prediction-variance extrema. The inaccessible full text of Antognini and Zagoraiou (2010) is a residual historical-priority risk, and general convex design principles can imply portions of the argument. No absolute historical-priority claim or independent verification is made.

## Limitations
This is a theorem for a known-mean, known-covariance, noiseless Gaussian Markov model. River chemistry often exhibits drift, discontinuities, nonstationarity, measurement error and non-Gaussian dynamics; the result does not prescribe field deployments without validating those assumptions. Full inspection of every potentially relevant historical monograph and the 2010 source was unavailable. The new theorem is analytically self-contained, but its originality assessment is necessarily provisional. Numerical diagnostics do not constitute infinite mathematical proof or independent audit.

## References
- Zimmerman, D. L. (first publicly available 2006-08-22). *Optimal network design for spatial prediction, covariance parameter estimation, and empirical prediction*. Environmetrics 17, 635–652. https://doi.org/10.1002/env.769 . Full openly accessible text: https://www.asc.ohio-state.edu/statistics/comp_exp/jour.club/Zimmerman-2006-Environmetrics.pdf
- Dasgupta, S., Mukhopadhyay, S., Keith, J. (initial preprint 2020-04-29; published 2022). *Optimal designs for some bivariate cokriging models*. https://arxiv.org/abs/2004.13967 ; https://doi.org/10.1016/j.jspi.2022.02.004 . Inspected arXiv PDF especially Section 5 and Theorem 5.2.
- Sikolya, K. and Baran, S. (2019). *On the optimal designs for the prediction of complex Ornstein-Uhlenbeck processes*. https://doi.org/10.1080/03610926.2019.1645855 . Inspected published full-text Section 3 and its endpoint restriction.
- Antognini, A. and Zagoraiou, M. (2010). *Exact optimal designs for computer experiments via Kriging metamodelling*. https://doi.org/10.1016/j.jspi.2010.03.027 . Full text was not obtained; its contents beyond accessible abstracts and citations were not assumed.
- Müller, W. G., Pronzato, L., Rendas, J., Waldl, H. (first publicly available 2014-11-26). *Efficient prediction designs for random fields*. https://doi.org/10.1002/asmb.2084 .
