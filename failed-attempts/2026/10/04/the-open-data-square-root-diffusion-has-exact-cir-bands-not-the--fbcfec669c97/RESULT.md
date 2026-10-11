# The open-data square-root diffusion has exact CIR bands, not the published normal-variance bands

## Finding

Under each equilibrium regime in the stochastic government-enterprise data-sharing model, the optimal effort controls are constant. Consequently the published state equation reduces to
\[
dK_t=(A-\delta K_t)\,dt+\sigma\sqrt{K_t}\,dW_t,
\]
where \(A>0\), \(\delta>0\), and \(\sigma>0\) are constant within the chosen game regime.

This is a square-root, or Cox–Ingersoll–Ross, diffusion. Conditional on
\[
K_0=k_0,
\]
its exact one-time law is
\[
K_t\overset{d}=c_tY_t,
\qquad
c_t=\frac{\sigma^2(1-e^{-\delta t})}{4\delta},
\]
where \(Y_t\) is noncentral chi-square with degrees of freedom
\[
\nu=\frac{4A}{\sigma^2}
\]
and noncentrality
\[
\lambda_t=
\frac{4\delta e^{-\delta t}k_0}
{\sigma^2(1-e^{-\delta t})}.
\]
Thus exact equal-tail state bands at any finite time are obtained directly from noncentral-chi-square quantiles.

As \(t\to\infty\),
\[
K_t
\Longrightarrow
\Gamma\!\left(
\frac{2A}{\sigma^2},
\frac{\sigma^2}{2\delta}
\right),
\]
where the two arguments are shape and scale. In particular, the stationary law is Gamma, not Normal.

The source nevertheless repeatedly assumes that the open-data stock is normally distributed and prints the 95% band
\[
E[K_t]\pm1.96D[K_t].
\]
Earlier in the same derivation it explicitly defines
\[
D[K_t]=E[K_t^2]-E[K_t]^2,
\]
so \(D[K_t]\) is the variance. Therefore there are two distinct problems with the printed band:

1. the square-root diffusion does not have a Normal law; and
2. even under a Normal approximation, a 95% band uses the standard deviation
\[
\sqrt{D[K_t]},
\]
not the variance \(D[K_t]\).

For the paper's Nash numerical benchmark, its own equilibrium formulas give
\[
X_N^*=2.4,\qquad
Y_N^*=1.6,
\]
so
\[
A_N=\alpha_GX_N^*+\alpha_EY_N^*=2.4.
\]
With
\[
\delta=0.1,\qquad \sigma=0.4,
\]
the stationary law is exactly
\[
K_\infty\sim\Gamma(30,0.8).
\]
Its mean, variance, and standard deviation are
\[
E[K_\infty]=24,
\qquad
D[K_\infty]=19.2,
\qquad
\sqrt{D[K_\infty]}\approx4.38178046.
\]

The source's limiting band is therefore
\[
[24-1.96(19.2),\,24+1.96(19.2)]
=
[-13.632,61.632].
\]
This interval extends below the nonnegative state space. Under the exact stationary Gamma law its coverage is approximately
\[
0.999999999676,
\]
not \(0.95\).

The exact equal-tail 95% stationary interval is
\[
[16.19269922,33.31906995].
\]
For comparison, a moment-matched Gaussian interval using the standard deviation is
\[
[15.41171030,32.58828970],
\]
whose coverage under the exact Gamma law is approximately
\[
0.9519472240.
\]

The correction applies to the uncertainty bands in the Nash, Stackelberg, and cooperative regimes because all three equilibrium state equations have the same square-root-diffusion form with a regime-specific constant \(A\).

## Assumptions and scope

The result uses the equilibrium state equation printed in the source,
\[
dK_t=
[\alpha_GX+\alpha_EY-\delta K_t]\,dt
+\sigma\sqrt{K_t}\,dW_t,
\]
after substituting the source's constant equilibrium controls. Define
\[
A=\alpha_GX^*+\alpha_EY^*.
\]

The exact distribution formulas require
\[
A>0,\qquad
\delta>0,\qquad
\sigma>0.
\]
These conditions hold in the paper's numerical benchmark.

The finding concerns probability bands for the state \(K_t\). It does not alter the paper's constant equilibrium controls, its formulas for the first moment, or its variance formula. It also does not assert that a Normal approximation can never be numerically adequate when the Gamma shape is large; it establishes that Normality is not exact and that the printed variance-width band is invalid even as a Gaussian band.

The source calls its intervals confidence intervals. Mathematically, when model parameters are treated as fixed and the random state itself is being enclosed, these are state-distribution or prediction bands. The substantive correction does not depend on terminology.

## Proof

Write the equilibrium state equation as
\[
dK_t=\delta(\theta-K_t)\,dt+\sigma\sqrt{K_t}\,dW_t,
\qquad
\theta=\frac{A}{\delta}.
\]
This is the standard square-root diffusion. Its conditional transition law is noncentral chi-square. With the present parameters,
\[
c_t=\frac{\sigma^2(1-e^{-\delta t})}{4\delta},
\qquad
\nu=\frac{4\delta\theta}{\sigma^2}
=\frac{4A}{\sigma^2},
\]
and
\[
\lambda_t=
\frac{4\delta e^{-\delta t}k_0}
{\sigma^2(1-e^{-\delta t})}.
\]
Hence
\[
K_t/c_t
\]
has the stated noncentral-chi-square law.

The stationary distribution of a square-root diffusion is Gamma. In shape-scale notation,
\[
a=\frac{2\delta\theta}{\sigma^2}
=\frac{2A}{\sigma^2},
\qquad
b=\frac{\sigma^2}{2\delta}.
\]
Its mean and variance are
\[
ab=\frac{A}{\delta},
\qquad
ab^2=\frac{A\sigma^2}{2\delta^2}.
\]
These match the limiting first and second central moments derived in the source, so the distributional correction is consistent with the source's moment calculation.

For the Nash benchmark, the source's equilibrium controls are
\[
X_N^*
=
\frac{\omega\lambda[\mu_G(r+\delta)+\tau\alpha_G]}
{\beta_G(r+\delta)},
\]
\[
Y_N^*
=
\frac{(1-\omega)\lambda[\mu_E(r+\delta)+\tau\alpha_E]}
{\beta_E(r+\delta)}.
\]
Substitution of the paper's numerical values gives
\[
X_N^*=2.4,\qquad Y_N^*=1.6,
\]
and therefore
\[
A_N=0.6(2.4)+0.6(1.6)=2.4.
\]
Thus
\[
a=\frac{2(2.4)}{0.4^2}=30,
\qquad
b=\frac{0.4^2}{2(0.1)}=0.8.
\]
The displayed stationary moments and bands then follow directly.

Finally, the source itself defines
\[
D[K_t]=E[K_t^2]-E[K_t]^2.
\]
Therefore \(D[K_t]\) is a variance. A moment-matched Gaussian 95% band would use
\[
E[K_t]\pm1.96\sqrt{D[K_t]},
\]
not
\[
E[K_t]\pm1.96D[K_t].
\]
This variance-versus-standard-deviation correction is independent of the stronger fact that the exact law is non-Gaussian.

## Verification

The bundled `verify.py` independently recomputes the Nash equilibrium controls and obtains
\[
X_N^*=2.4,\qquad
Y_N^*=1.6,\qquad
A_N=2.4.
\]
It then checks the exact stationary parameters
\[
a=30,\qquad b=0.8,
\]
the mean \(24\), variance \(19.2\), and standard deviation approximately \(4.38178046\).

Using a standalone implementation of the regularized incomplete Gamma function and bisection, the checker reproduces the exact stationary equal-tail quantiles
\[
16.19269922
\quad\text{and}\quad
33.31906995.
\]
It also verifies that the source's interval is
\[
[-13.632,61.632]
\]
with exact stationary coverage approximately \(0.999999999676\), while the standard-deviation Gaussian approximation has exact Gamma coverage approximately \(0.9519472240\).

The distributional identification itself is analytic and is supported by primary square-root-diffusion literature. The numerical checker is not used as a substitute for that theorem.

## Relationship to prior work

Fan, Tao, Zhang, Fan, and Cheng (2022/2023), DOI 10.3934/math.2023234, is the motivating source. Its open full text was inspected through the state equation, Nash equilibrium formulas, moment derivation, all three printed Normal-band statements, and the numerical parameter table. The paper correctly derives the first two moments of the square-root diffusion, but after defining \(D[K_t]\) as the variance it assumes a Normal state law and uses \(1.96D[K_t]\) as the half-width.

Gordy's square-root-diffusion work, DOI 10.17016/FEDS.2012.12 and its journal version DOI 10.1239/jap/1421763319, gives the relevant distribution theory. The full Federal Reserve version explicitly states that the CIR transition distribution is noncentral chi-square and that the stationary univariate law is Gamma. Applying that established law to the source's equilibrium state equation yields the exact finite-time and stationary bands above.

Searches by the source's exact title and DOI, together with aliases involving CIR, Gamma laws, Normal bands, variance, and confidence intervals, located no published correction of the source's uncertainty bands.

## Limitations

The finding corrects uncertainty quantification for the model state. It does not claim that the source's equilibrium effort ordering, cost-sharing comparisons, or first two moments are wrong.

The exact numerical interval
\[
[16.19269922,33.31906995]
\]
is the stationary equal-tail interval for the paper's Nash benchmark only. Stackelberg and cooperative regimes have different values of \(A\) and therefore different Gamma shapes and quantiles, although the same exact law applies after substitution.

A Gaussian approximation can be accurate for sufficiently large Gamma shape. The claim is not that Gaussian approximation is intrinsically forbidden; it is that the published Normality assumption is not the exact law and that the printed half-width uses variance where a Gaussian approximation requires standard deviation.

## References

1. Z. Fan, Y. Tao, W. Zhang, K. Fan, J. Cheng, “Research on open and shared data from government-enterprise cooperation based on a stochastic differential game,” AIMS Mathematics 8 (2023), 4726–4752. DOI: 10.3934/math.2023234. Published 7 December 2022.
2. M. B. Gordy, “On the Distribution of a Discrete Sample Path of a Square-Root Diffusion,” Finance and Economics Discussion Series 2012-12, Federal Reserve Board, 2012. DOI: 10.17016/FEDS.2012.12.
3. M. B. Gordy, “Finite-Dimensional Distributions of a Square-Root Diffusion,” Journal of Applied Probability 51 (2014), 930–942. DOI: 10.1239/jap/1421763319.
