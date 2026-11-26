# Universal high-dropout spacing law for Brownian-bridge quadrature

## Finding

Fix an integer \(n\ge3\). Let \(B\) be a standard Brownian bridge from zero to zero on \([0,1]\), and put \(J=\int_0^1B(t)\,dt\). Place \(n\) noiseless sensors at deterministic ordered locations \(0\le x_1\le\cdots\le x_n\le1\). Each readout is returned with probability \(r=1-q\in(0,1)\), independently of the other readouts and the bridge. The returned values and the availability indicators are observed, and the estimator of \(J\) is its conditional mean.

The expected squared error has a **unique minimizer among ordered placements** for each \(0<r<1\), and the minimizing design is reflection-symmetric. At fixed \(n\) the minimizing locations satisfy, as \(r\downarrow0\),
\[
x_i^*(1-r)=\frac12+\frac{r}{8}(2i-n-1)+o_n(r),\qquad 1\le i\le n.
\]
Adjacent optimal locations thus separate by \(r/4+o_n(r)\); the design does not collapse to exact midpoint replication at high dropout.

## Assumptions and scope

The covariance of the bridge is \(K(s,t)=\min(s,t)-st\); the two endpoint values are known exactly. Coincident candidate locations are allowed and successful readouts there give the same bridge value. The objective is the variance of the error in estimating the single integral, not the integral of the pointwise reconstruction variances. Sensors are selected before seeing the bridge or any availability indicators.

## Proof

**Conditional risk.** In a realized survivor set \(S=\{i_1<\cdots<i_k\}\), put \(t_0=0\), \(t_j=x_{i_j}\) for \(1\le j\le k\), and \(t_{k+1}=1\). Conditionally on the exact returned values, the centered residuals on nonzero gaps are independent Brownian bridges. On a gap of length \(h\), the integral has variance \(h^3/12\), by rescaling the unit-interval covariance and integrating it twice. A repeated site adds only a gap of length zero and no information. Thus the expected risk is
\[
 R_q(x)=\frac1{12}\sum_{S\subseteq\{1,\ldots,n\}}r^{|S|}q^{n-|S|}\sum_{j=0}^{|S|}(t_{j+1}-t_j)^3.
\]

**Uniqueness and symmetry.** The convexity of the cube on the nonnegative half-line makes each survivor-set contribution convex on the ordered simplex. When all sensors survive, the vector of affine gap lengths determines \(x\) uniquely, and at least one gap changes between any two distinct placements. The cube is strictly convex even when one argument is zero. This event has weight \(r^n>0\), so the full continuous objective is strictly convex on the compact simplex and has a unique minimizer. Reflection \(x_i\mapsto1-x_{n+1-i}\) preserves the risk and hence preserves this minimizer.

**Localization on the scale \(r\).** Write \(m=(1/2,\ldots,1/2)\), \(\delta=x-m\). With a single survivor at \(t=1/2+d\), the conditional variance is \(1/48+d^2/4\). For any survivor set, the change in risk along the segment from \(m\) to \(x\) has absolute value at most \(\tfrac14\sum_{i\in S}|\delta_i|\): the derivative at an active site is the difference of the squares of its adjacent gaps divided by four. The probability of retaining a specified site and at least one other site is \(r(1-q^{n-1})\le(n-1)r^2\). Therefore
\[
R_q(x)-R_q(m)\ge\frac{r q^{n-1}}4\|\delta\|_2^2-\frac{(n-1)r^2}4\|\delta\|_1.
\]
At a minimizer the left side is nonpositive, giving \(\|x^*-m\|_2\le(n-1)\sqrt n\,r/q^{n-1}\). This includes the case \(x^*=m\), and proves the required fixed-size scale bound.

**Limiting design.** Put \(x=m+ry\) with bounded ordered \(y\). For a surviving pair \(i<j\), the two exterior gaps are \(1/2+ry_i\) and \(1/2-ry_j\), and the middle gap is \(r(y_j-y_i)\). The sum of their cubes divided by twelve differs from its midpoint value by \(-r(y_j-y_i)/16+O(r^2)\). A singleton contributes \(r^2y_i^2/4\) before weighting by its survival-pattern probability; events with at least three survivors have total probability \(O_n(r^3)\) and change their conditional variance by \(O_n(r)\) for bounded \(y\). It follows that uniformly on bounded ordered sets,
\[
r^{-3}(R_{1-r}(m+ry)-R_{1-r}(m))
=G(y)+O_{n,\|y\|_\infty}(r),\qquad
G(y)=\frac14\sum_i y_i^2-\frac1{16}\sum_{i<j}(y_j-y_i).
\]
The last sum is \(\sum_i(2i-n-1)y_i\). Completing the square gives the unique optimizer \(y_i^0=(2i-n-1)/8\), already strictly ordered and feasible after rescaling for small enough \(r\). The rescaled true optimizers are bounded by the scale estimate. Comparison with the trial vector \(y^0\) and uniform convergence on bounded sets imply that every subsequential limit minimizes \(G\). Hence the rescaled optimizers converge to \(y^0\), proving the law.

## Verification and limits

The analytic argument covers every fixed \(n\ge3\); there is no joint large-\(n\), small-\(r\) claim or exact intermediate-dropout formula. The accompanying `verify_dropout.py` uses NumPy and SciPy for finite comparisons of conditional variances and small-network designs. It also checks the overlapping two-site formula as a separate reference case. A comparison of finite cases is not the proof of uniqueness or of the limiting expansion. The result does not cover noisy returned values, process-dependent losses, other kernels or adaptive sampling.

## Relationship to prior work

The independent-delivery two-site solution is a specialization of [*Exact two-sensor Brownian-bridge quadrature under correlated observation erasures*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-exact-two-sensor-brownian-bridge-quadrature-under-correlated-obs--47f6c01bcecf/RESULT.md), with marginal delivery \(p=r\) and joint delivery \(q=r^2\) in that result's notation. It is not part of the contribution here. [*Exact optimal sampling for Brownian-bridge path reconstruction with independent observation erasures*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-exact-optimal-sampling-for-brownian-bridge-path-reconstruction-w--849744f935dc/RESULT.md) instead minimizes an expected sum of **squared** gaps, from the integral of pointwise posterior variances. Its optimal first-order spacing is \(r/2\), not the \(r/4\) obtained here from cubed gaps.

The same cubic-gap risk can be expressed as the expected integral of squared distance to the nearest delivered site or known endpoint. The criterion in Frasca, Garin, Gerencsér and Hendrickx, [*Optimal one-dimensional coverage by unreliable sensors*](https://arxiv.org/abs/1404.7711), is instead an expected maximum distance and yields exact midpoint co-location at high failure. Santin, [*Equally spaced points are optimal for Brownian Bridge kernel interpolation*](https://arxiv.org/abs/2210.15959), studies a deterministic interpolation error criterion, not erasure-averaged integral variance. These comparisons do not establish historical priority.
