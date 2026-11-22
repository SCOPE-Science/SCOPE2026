# A drift-controlled hierarchy of collective extremes under shared geometric-Brownian resetting

## Finding

**Theorem (sharp many-particle common-reset extremes).** Fix an integer \(n\geq1\), a reset intensity \(r>0\), noise amplitude \(\sigma>0\), and logarithmic growth drift \(a\in\mathbb R\). Let \(n\) geometric Brownian coordinates be returned **simultaneously** to value \(1\) at the times of one rate-\(r\) Poisson process, while their Wiener noises are mutually independent. In the unique stationary law, put \(Y_j=\log X_j\), and define
\[
 s_n=\sqrt{a^2+2r\sigma^2/n},\qquad
 k_n=\frac{n(s_n-a)}{\sigma^2},\qquad
 C_n=\frac{r\sigma^{n+1}s_n^{(n-3)/2}}{(2\pi)^{(n-1)/2}\sqrt n\,(s_n-a)^n}.
\]
Then for every fixed \(n\geq1\), as \(y\to\infty\),
\[
 \boxed{\mathbb P\{Y_1>y,\ldots,Y_n>y\}
 \sim C_n y^{-(n-1)/2}e^{-k_n y}.}
\]
In particular the exact one-particle upper tail, at every \(y>0\), is
\[
 \mathbb P\{Y_j>y\}=c_1e^{-k_1y},\qquad
 c_1=\frac{\Delta+a}{2\Delta},\quad
 \Delta=\sqrt{a^2+2r\sigma^2}.
\]
At identical marginal upper-tail probabilities \(\varepsilon\downarrow0\), the \(n\)-fold coincidence probability is asymptotic to
\[
 \boxed{C_n\left(\frac{k_1}{\log(c_1/\varepsilon)}\right)^{(n-1)/2}
 \left(\frac{\varepsilon}{c_1}\right)^{\alpha_n},\qquad
 \alpha_n=\frac{k_n}{k_1}=\frac{\Delta+a}{s_n+a}.}
\]
For each fixed integer \(n\geq2\), \(1<\alpha_n<n\); it is strictly decreasing in \(a\) for fixed \(r,\sigma\), and strictly increasing with \(n\). Its upper-tail dependence coefficient is zero, but its residual tail-dependence coefficient is \(\eta_n=1/\alpha_n\), strictly larger than the independent-reset value \(1/n\). All claims hold without assuming the existence of the ordinary moments of the geometric Brownian coordinates.

**Sharp drift trichotomy (iterated limit).** The size of the collective tail exponent as \(n\to\infty\), *after* the fixed-\(n\) high-threshold limit, exhibits three regimes:
\[
 \boxed{
 \alpha_n\longrightarrow\frac{\Delta+a}{2a}\quad(a>0),\qquad
 \alpha_n=\sqrt n\quad(a=0),\qquad
 \frac{\alpha_n}{n}\longrightarrow\frac{2|a|}{\Delta+|a|}\quad(a<0).
 }
\]
Thus common catastrophes cause an arbitrarily high number of positive-log-growth particles to share a bounded rare-event exponent, whereas neutral and negative log drift have square-root and linear exponent hierarchies respectively. These are exponents of tail probabilities, **not** an interchange of the particle-count and threshold limits.

## Assumptions and scope

For each integer \(n\), take independent standard real Wiener processes \(W_j\), independent of a homogeneous Poisson process of intensity \(r\). Between common resetting events let
\[
 dX_j(t)=\mu X_j(t)\,dt+\sigma X_j(t)\,dW_j(t),\qquad X_j(t)>0,
 \qquad \mu=a+\frac{\sigma^2}{2}.
\]
Every reset maps the entire vector to \((1,\ldots,1)\). Events are independent of all coordinates and increments. The vector is observed in its unique stationary distribution; its logarithms can be negative. A synchronized event resets **all** coordinates, rather than selecting a random subset or using separate clocks. The probability theorem has fixed finite \(n\) and common positive logarithmic threshold \(y\to\infty\). The drift trichotomy concerns the resulting sequence of rate exponents. There is no assumption on the sign of \(a\) or \(\mu\), and no finite-moment assumption. Standard Brownian motion has variance \(t\), so \(\sigma\) is the stochastic volatility rather than a diffusivity generator coefficient.

## Proof

### 1. Stationarity and marginal tail

Extend the common rate-\(r\) Poisson process to the negative time axis. Its backward recurrence time \(T\) at a stationary observation is exponential with rate \(r\), independent of the Wiener increments after the last reset. The logarithmic dynamics give the exact representation
\[
 (Y_1,\ldots,Y_n)\;\stackrel d=\;
 (aT+\sigma\sqrt T Z_1,\ldots,aT+\sigma\sqrt T Z_n),
 \quad T\sim\operatorname{Exp}(r),\quad Z_j\stackrel{\mathrm{iid}}\sim N(0,1),
\]
with all displayed variables independent except through their common \(T\). A synchronous reset in any future interval couples any two versions driven by the same noise and clock, yielding a unique stationary distribution.

For one coordinate the moment-generating function of \(Y\) is \(r/(r-at-\sigma^2t^2/2)\) near zero. Its inverse transform has density \((r/\Delta)e^{-k_1y}\) for \(y>0\). Integration gives the exact upper tail \(c_1e^{-k_1y}\), with \(c_1=r/(\Delta k_1)=(\Delta+a)/(2\Delta)\). This identifies the marginal Pareto exponent \(k_1\) of \(X=e^Y\).

### 2. Exact integral and its unique saddle

Conditional independence gives for all \(y>0\)
\[
 Q_n(y):=\mathbb P(Y_1>y,\ldots,Y_n>y)
 =r\int_0^\infty e^{-rt}\left[\overline\Phi\!\left(\frac{y-at}{\sigma\sqrt t}\right)\right]^n\,dt,
\]
where \(\overline\Phi\) is the survival function of a standard normal. Scale \(t=yz\). In the region \(1-az>0\), the Gaussian Mills expansion, locally uniformly over positive compact intervals of \(z\), gives
\[
 Q_n(y)\sim r\sigma^n(2\pi)^{-n/2}y^{1-n/2}
 \int_0^\infty\!\frac{z^{n/2}}{(1-az)^n}e^{-yf_n(z)}\,dz
\]
for the contribution of any compact subinterval contained in that region, with
\[
 f_n(z)=rz+\frac{n(1-az)^2}{2\sigma^2 z}.
\]
The phase is strictly convex: \(f_n''(z)=n/(\sigma^2z^3)>0\). Its unique unconstrained minimizer is \(z_n=1/s_n\), and since \(s_n>|a|\), one has \(1-az_n>0\). Moreover
\[
 f_n(z_n)=\frac{n(s_n-a)}{\sigma^2}=k_n,
 \qquad f_n''(z_n)=\frac{ns_n^3}{\sigma^2}.
\]
The small-\(z\) region is exponentially negligible because the Gaussian tail requires an increasingly costly fluctuation; large \(z\) is negligible because of the factor \(e^{-ryz}\). When \(a>0\), the complementary region \(z\ge1/a\), where a Gaussian tail need not be small, has total probability at most \(e^{-ry/a}\). It is negligible relative to \(e^{-k_ny}\) because \(k_n=2r/(s_n+a)<r/a\). For negative \(a\), the Mills region includes every positive \(z\). Consequently the minimizer is the sole leading contribution, and uniform Mills estimates on a neighborhood of it followed by Laplace's method are justified.

### 3. The prefactor

The amplitude at the saddle is
\[
 \frac{z_n^{n/2}}{(1-az_n)^n}
 =\frac{s_n^{n/2}}{(s_n-a)^n}.
\]
The Gaussian quadratic integral contributes
\[
 \left(\frac{2\pi}{y f_n''(z_n)}\right)^{1/2}
 =\frac{\sigma\sqrt{2\pi}}{\sqrt{ny}\,s_n^{3/2}}.
\]
Multiplying by the renewal and Mills prefactors yields \(C_ny^{-(n-1)/2}e^{-k_ny}\) with precisely the stated \(C_n\). The \(n=1\) coefficient simplifies to \(c_1\), consistent with the independently derived exact marginal law. All factors are positive and finite for every stated parameter. This concludes the sharp joint-tail equivalent.

### 4. Marginally standardized extremes and size hierarchy

The common upper \(1-\varepsilon\) marginal quantile has log-level \(y_\varepsilon=\log(c_1/\varepsilon)/k_1\) for sufficiently small \(\varepsilon>0\). Substitute this into the fixed-\(n\) equivalent to obtain the second boxed formula. The identity
\[
 k_n=\frac{2r}{s_n+a},\qquad k_1=\frac{2r}{\Delta+a}
\]
proves the expression for \(\alpha_n\). Since \(s_n<\Delta\) for \(n>1\) and \(s_n+a>0\), \(\alpha_n>1\). Since \(s_n>a\) and \(s_n<\Delta\), the alternative form \(\alpha_n=n(s_n-a)/(\Delta-a)\) gives \(\alpha_n<n\). As \(n\) increases, \(s_n\) strictly decreases, so \(\alpha_n\) increases. Moreover
\[
 \frac{d}{da}\log\alpha_n=\frac1\Delta-\frac1{s_n}<0,
\]
proving the strict drift monotonicity at fixed volatility and reset rate.

For any fixed \(n\ge2\), \(\alpha_n>1\) implies \(Q_n(y_\varepsilon)/\varepsilon\to0\), the vanishing asymptotic upper-tail dependence coefficient. The power-law exponent in \(\varepsilon\) is \(\alpha_n\), hence the residual coefficient is \(1/\alpha_n\). If the same processes instead have *independent* rate-\(r\) reset clocks, their marginal laws remain unchanged but the joint probability is exactly \(\varepsilon^n\). Since \(\alpha_n<n\), synchronized resetting makes simultaneous sufficiently rare exceedances exponentially more likely in logarithmic threshold, despite the ultimate vanishing conditional exceedance probability.

Finally, the exact identities \(s_n=\sqrt{a^2+2r\sigma^2/n}\) and \(\alpha_n=(\Delta+a)/(s_n+a)\) yield: for \(a>0\), \(s_n\to a\); for \(a=0\), \(\alpha_n=\sqrt n\); for \(a<0\), setting \(A=|a|\) gives \(s_n-A\sim r\sigma^2/(An)\), so \(\alpha_n/n\to2A/(\Delta+A)\). The three asymptotic regimes hold as an *iterated* high-threshold/particle-count analysis. This completes the theorem.

## Verification

The standalone `verify.py` numerically integrates the original exact exponential-age/Gaussian-survival formula using an independent adaptive quadrature, checks its normalized marginal tails against the analytic inverse-Laplace expression, and checks convergence to the full sharp joint-tail equivalent for several positive and negative drifts, reset rates, volatilities, and \(n\in\{2,3,4,6\}\). It also checks the closed rate identity, increasing \(n\)-hierarchy, strict drift ordering and neutral-drift benchmark. With SciPy available, `python3 verify.py` passed **128 assertions**. It does not constitute a proof for untested parameters or the infinite limits. The proof is the renewal representation, unique-saddle analysis and exact algebra in the preceding sections.

## Relationship to prior work

Stojkoski, Sandev, Kocarev and Pal, *Geometric Brownian Motion under Stochastic Resetting* (arXiv:2104.01571, first public version 2021-04-04), derive the **one-coordinate** stationary power-law tail and moment regimes; those facts are used rather than presented as new. Their independent-replica sample-size analysis does not use a single shared catastrophe clock or determine joint upper extremes. Vinod and collaborators (Phys. Rev. E 105 L012106, 2022) analyze time averaging and nonergodicity of a single resetting GBM.

Opitz, *Modeling asymptotically independent spatial extremes based on Laplace random fields* (arXiv:1507.02537), establishes residual asymptotic independence for **centered elliptical** exponential-variance Gaussian scale mixtures. That covers the zero-log-drift Gaussian mixture benchmark (the \(a=0\) case at the exponential-rate level), not the off-center variance-mean mixture \(aT+\sigma\sqrt T Z\) whose drift term scales differently with the common age. Engelke, Opitz and Wadsworth, *Extremal dependence of random scale constructions* (arXiv:1803.04221), give broader random-*scale* theories, but the present variance-mean mixing is not their single independent radial multiplier.

Published shared/partial-batch Brownian-resetting results, including *Anisotropic joint-excursion rates under asymmetric shared and individual Brownian resetting* and *Multivariate excursion cones and optimal age pooling under batch resetting*, contain **zero-drift** joint exponential rates for Brownian positions and are important direct comparisons. The no-drift \(\sqrt n\) benchmark is covered or implied there and is not claimed as new. Neither of their modeled Brownian dynamics contains the shared reset age multiplied by nonzero logarithmic drift. The present asserted addition is the complete nonzero-drift, all-size **sharp prefactor** and drift-sign crossover of the exponent hierarchy. A general published result on multivariate asymmetric Laplace/variance-mean mixtures might derive an equivalent statement implicitly; the assessed novelty is therefore bounded to the inspected literature, not a claim of absolute publication priority.

## Limitations

The theorem applies to equal growth parameters, independent Brownian noises, identical simultaneous reset levels, one common Poisson clock, and fixed finite \(n\) before the high-threshold limit. It does not establish a joint simultaneous limit with \(n\) growing alongside \(y\), a classification of partial-batch resetting or correlated Wiener increments, nor finite-threshold risk bounds. The elementary asymptotic form becomes accurate slowly when positive logarithmic drift is large relative to volatility; the numerical checker deliberately distinguishes a finite-threshold approximation from a limit. Zero drift is a covered benchmark; the structural nonzero-drift crossover and full prefactor are the assessed focus.

## References

1. V. Stojkoski, T. Sandev, L. Kocarev, A. Pal, *Geometric Brownian Motion under Stochastic Resetting: A Stationary yet Non-ergodic Process*, arXiv:2104.01571 (first public 2021-04-04), https://arxiv.org/abs/2104.01571 .
2. D. Vinod et al., *Nonergodicity of reset geometric Brownian motion*, Phys. Rev. E 105, L012106 (2022), https://doi.org/10.1103/PhysRevE.105.L012106 .
3. T. Opitz, *Modeling asymptotically independent spatial extremes based on Laplace random fields*, arXiv:1507.02537 (2015), https://arxiv.org/html/1507.02537v2 .
4. S. Engelke, T. Opitz, J. Wadsworth, *Extremal dependence of random scale constructions*, arXiv:1803.04221 (2018), https://arxiv.org/abs/1803.04221 .
5. *Anisotropic joint-excursion rates under asymmetric shared and individual Brownian resetting*, published published-finding corpus scientific record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-anisotropic-joint-excursion-rates-under-asymmetric-shared-and-in--707257f9e1f5 .
6. *Multivariate excursion cones and optimal age pooling under batch resetting*, published published-finding corpus scientific record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-multivariate-excursion-cones-and-optimal-age-pooling-under-batch--83d8c983aa19 .
