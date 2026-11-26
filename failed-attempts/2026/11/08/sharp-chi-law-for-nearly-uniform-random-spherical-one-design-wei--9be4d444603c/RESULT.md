# Sharp chi-law for nearly uniform random spherical one-design weights

## Finding

Fix an ambient dimension \(d\ge 2\). Let \(X_1,\dots,X_m\) be independent uniform points on the unit sphere \(S^{d-1}\subset\mathbb R^d\), with \(m\ge d+1\). Define the **minimum relative box radius**
\[
T_m=\min\left\{\max_{1\le i\le m}|mw_i-1|:\ \sum_{i=1}^mw_i=1,\quad\sum_{i=1}^mw_iX_i=0,\quad w_i\in\mathbb R\right\}.
\]
Thus the weights integrate every affine function on the sphere against normalized surface measure exactly. The unconstrained minimum is used to measure the precise radius; whenever \(T_m<1\), the realizing weights are strictly positive. Set \(S_m=\sum_{i=1}^mX_i\) and
\[
D_m(u)=\min_{a\in\mathbb R}\sum_{i=1}^m|a+u\cdot X_i|,\qquad
c_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)}.
\]
Then, almost surely for every \(m\ge d+1\), the finite-sample identity is
\[
\boxed{T_m=\max_{\|u\|_2=1}\frac{|u\cdot S_m|}{D_m(u)}.}
\]
For each fixed \(d\), as \(m\to\infty\),
\[
\boxed{\sqrt m\,T_m\ \xrightarrow{\mathrm{law}}\ \frac{\chi_d}{\sqrt d\,c_d},}
\]
where \(\chi_d\) denotes the Euclidean norm of \(d\) independent standard Gaussian variables. In particular, on the circle \(d=2\), for every fixed \(t\ge0\),
\[
\boxed{\lim_{m\to\infty}\Pr\left(T_m\le \frac{t}{\sqrt m}\right)=1-\exp\left(-\frac{4t^2}{\pi^2}\right).}
\]
For fixed \(t>0\) and all sufficiently large \(m\), the event on the left is *exactly* the existence of a **positive** affine-exact quadrature rule on those nodes with every weight in
\[
\left[\frac{1-t/\sqrt m}{m},\ \frac{1+t/\sqrt m}{m}\right].
\]
Consequently, for any fixed failure target \(\delta\in(0,1)\), the asymptotically sharp circle threshold is \(t_\delta=(\pi/2)\sqrt{\log(1/\delta)}\): the probability limit at box radius \(t_\delta/\sqrt m\) is exactly \(1-\delta\). This is a limiting critical calibration law, not a uniform finite-sample tail bound.

## Assumptions and scope

The dimension \(d\ge2\) is fixed while the sample count \(m\) grows. Nodes are independent and exactly uniform on \(S^{d-1}\). All linear-programming statements use exact real arithmetic. The box radius \(T_m\) is defined by a minimax **relative** weight deviation, not by least-squares reweighting or an arbitrary positive representation of the origin. For \(m\ge d+1\), the augmented data vectors \((1,X_i)\) span \(\mathbb R^{d+1}\) almost surely; therefore the affine constraints admit real solutions and the optimum is finite and attained. When \(m=d+1\), this full rank holds because a proper affine hyperplane intersects the sphere in a set of surface measure zero. All probability limits concern the complete, unconditioned random sample.

## Proof

**1. Exact finite-sample duality.** Write \(mw_i=1+e_i\). The exactness constraints are
\[
\sum_{i=1}^me_i=0,\qquad\sum_{i=1}^me_iX_i=-S_m.
\]
Let \(B\) denote the \((d+1)\)-by-\(m\) matrix with columns \((1,X_i)\). In finite dimensions, the quotient norm induced by \(\|e\|_\infty\) satisfies
\[
\min_{Be=(0,-S_m)}\|e\|_\infty=
\max_{(a,u)\ne(0,0)}\frac{|u\cdot S_m|}{\sum_i|a+u\cdot X_i|}.
\]
This follows directly from linear-programming duality between \(\ell_\infty\) and \(\ell_1\); full row rank of \(B\) ensures that every denominator is positive for a nonzero dual vector. The case \(u=0\) contributes zero. For \(u\ne0\), homogeneity permits \(\|u\|_2=1\); for each such \(u\), choosing \(a\) to minimize the denominator gives \(D_m(u)\). The maximum exists by compactness and the absence of a nonzero null vector for \(B^\mathsf T\). This proves the boxed finite-sample identity.

**2. Uniform convergence of all projected absolute deviations.** For \(\|u\|_2=1\), each projection \(u\cdot X_i\) belongs to \([-1,1]\); a minimizer of \(a\mapsto\sum_i|a+u\cdot X_i|\) is a negative sample median and thus lies in \([-1,1]\). For every \((u,a)\) in the compact set \(S^{d-1}\times[-1,1]\), the integrand \(f_{u,a}(x)=|a+u\cdot x|\) is bounded by \(2\) and obeys the deterministic Lipschitz bound
\[
|f_{u,a}(x)-f_{v,b}(x)|\le |a-b|+\|u-v\|_2.
\]
Take finite arbitrarily fine nets in this compact parameter set; the strong law on every finite net, then the Lipschitz bound, imply
\[
\sup_{\|u\|_2=1,\ |a|\le1}\left|\frac1m\sum_i|a+u\cdot X_i|-\mathbb E|a+u\cdot X_1|\right|\xrightarrow{\mathrm{a.s.}}0.
\]
Rotational symmetry makes the expectation independent of \(u\), and symmetry plus convexity in \(a\) shows its minimum occurs at \(a=0\). Therefore its minimum is \(c_d=\mathbb E|X_{1,1}|\), independent of \(u\). Integrating the standard spherical-coordinate density gives
\[
\mathbb E|X_{1,1}|=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)}>0.
\]
Taking minima over \(a\) preserves the uniform error bound, yielding
\[
\boxed{\sup_{\|u\|_2=1}\left|\frac{D_m(u)}m-c_d\right|\xrightarrow{\mathrm{a.s.}}0.}
\]
In particular every \(D_m(u)\) is uniformly bounded below by \(mc_d/2\) for all sufficiently large \(m\), almost surely.

**3. Distributional limit and positivity.** Write \(Z_m=S_m/\sqrt m\). Because the uniform spherical law has mean zero and covariance \(I_d/d\), the multivariate central limit theorem gives \(Z_m\Rightarrow Z\sim N(0,I_d/d)\). By Step 2 and the dual identity,
\[
\frac{\|Z_m\|_2}{c_d+o(1)}\le\sqrt m\,T_m\le\frac{\|Z_m\|_2}{c_d-o(1)}
\]
almost surely along the sample sequence, where the uniform \(o(1)\) need not be deterministic. Slutsky's theorem gives \(\sqrt m T_m\Rightarrow\|Z\|_2/c_d=\chi_d/(\sqrt d\,c_d)\). The limiting distribution is continuous. For \(d=2\), \(c_2=2/\pi\), and the Rayleigh survival function is \(\Pr(\chi_2>x)=e^{-x^2/2}\); substitution yields the claimed \(e^{-4t^2/\pi^2}\) survival law. Finally, for fixed \(t\), the radius \(t/\sqrt m\) is smaller than \(1\) for sufficiently large \(m\), and all weights in its box are positive. Conversely, any weights in the box furnish a feasible point for the minimization defining \(T_m\). Hence the event equivalence and limiting success probability hold exactly as stated.

## Verification

The accompanying `verify.py` builds the primal linear program directly from the affine moment equations, solves it with a linear-programming solver, checks the achieved exactness and primal feasibility, and independently reconstructs the dual optimum from the solver's dual variables. It tests dimensions \(d=2,3,5\), several sample sizes, and deterministic random inputs. These finite numerical tests are supplementary; the probabilistic limit and universal finite-sample identity follow from the proof above.

## Relationship to prior work

Neumayer, Schäfer and Ullrich (2026, arXiv:2610.32699v1, Theorem 1.1, Remark 2.6, and Corollary 2.13) prove high-probability existence of exact positive random quadrature with approximately equal weights in general function spaces, including spherical polynomial spaces. Their stated box radius yields a sufficient sample bound but not the distribution of the *smallest feasible radius*, the precise chi limit, or the sharp circle success probability at the critical \(m^{-1/2}\) scale. The present result addresses precisely that first-degree boundary case rather than replacing their general theorem.

Zhou and Chen (2015/2018) study spherical designs with near-equal positive weights, primarily for nodes in prescribed enclosures, not the stochastic minimal-radius law. Bělík, Narayan and Turnage (2026) construct randomized least-squares quadrature with concentrated weights; that particular least-squares solution differs from this globally minimized \(\ell_\infty\) deviation. Fu, Wang and Yan (2022/2023) study optimal spherical projection sums and explicitly record the known constant \(c_d\), but their minimax configuration problem does not optimize exact quadrature weights on a random sample. Wendel's classical theorem gives the probability that arbitrary nonnegative weights can center a random spherical sample; it does not control the relative deviation of *every* weight from \(1/m\). No historical uniqueness claim follows solely from these comparisons.

## Limitations

The law is for fixed \(d\), affine functions (spherical design degree one), and iid uniform points; it is not a high-dimensional simultaneous limit or a result for higher-degree spherical designs. The finite-sample minimization initially allows signed weights, becoming a positive-weight statement only on subunit-radius events. The circle success formula is a limit for fixed rescaled box radius, not an exact formula at arbitrary finite \(m\), nor a uniform estimate as the requested failure probability itself tends to zero. Floating-point verification does not certify the infinite-population theorem, and unindexed general statistical calibration results could affect historical attribution.

## References

1. S. Neumayer, M. Schäfer, T. Ullrich, *Random nodes with positive weights: Richter–Tchakaloff rules and optimal positive quadrature*, arXiv:2610.32699v1 (23 October 2026), https://arxiv.org/html/2610.32699v1.
2. F. Bělík, A. Narayan, J. Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares*, arXiv:2609.09506 (8 September 2026), https://arxiv.org/abs/2609.09506.
3. Y. Zhou, X. Chen, *Spherical \(t_\epsilon\)-Designs for Approximations on the Sphere*, arXiv:1502.03562 (12 February 2015); Mathematics of Computation 87 (2018), 2831–2855, https://arxiv.org/abs/1502.03562.
4. W. Fu, G. Wang, J. Yan, *On the minimax spherical designs*, first published 19 April 2022, Random Structures & Algorithms 62 (2023), 131–154, https://doi.org/10.1002/rsa.21087.
5. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica 11 (1962), 109–111, https://doi.org/10.7146/math.scand.a-10655.
