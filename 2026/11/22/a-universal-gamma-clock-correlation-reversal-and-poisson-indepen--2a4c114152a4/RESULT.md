# A universal Gamma-clock correlation reversal and Poisson independence in comb diffusion

## Finding

For an ideal two-dimensional diffusive comb with complete renewal resetting, the stationary longitudinal and transverse **squared displacements** have the exact normalized covariance

\[
\boxed{\frac{\operatorname{Cov}(X^2,Y^2)}{\mathbb E[X^2]\,\mathbb E[Y^2]}=\frac{1-k}{5(k+1)}.}
\]

Here \(k>0\) is the shape of the Gamma renewal-reset clock; all diffusion coefficients and the Gamma rate cancel. The covariance is strictly positive for \(0<k<1\), is zero for \(k=1\), and is strictly negative for \(k>1\). Its sharp limiting values are \(1/5\) and \(-1/5\), neither attained at finite positive \(k\).

More strongly, within this Gamma-clock family the two stationary **positions** are independent exactly at \(k=1\), the exponential (Poisson) inter-reset law. At this unique value their full stationary joint density is a product of two Laplace densities. This factorization is a known consequence of the Poisson-reset comb resolvent, not the claimed novel component; the new classification is the entire Gamma-clock dependence and its sign/independence boundary.

## Assumptions and scope

Fix \(D_x>0\), \(D_y>0\), \(\lambda>0\) and \(k>0\). On each excursion, let \(B,W\) be independent standard one-dimensional Brownian motions and set

\[
Y_t=\sqrt{2D_y}\,B_t,\qquad
L_t=\int_0^t\delta_0(Y_s)\,ds,\qquad
X_t=\sqrt{2D_x}\,W_{L_t}.
\]

The occupation-normalized local time is the almost-sure limit of \((2\epsilon)^{-1}\int_0^t\mathbf 1_{|Y_s|<\epsilon}\,ds\) as \(\epsilon\downarrow0\). This fixes the local-time convention and gives the distributional forward generator \(D_y\partial_{yy}+D_x\delta_0(y)\partial_{xx}\). Excursions start at \((0,0)\). Their Brownian noises are independently refreshed after each **complete** reset; neither partial coordinate resetting nor resetting only the finger coordinate is covered.

Inter-reset durations are independent and identically distributed \(S\sim\operatorname{Gamma}(k,\lambda)\) with **shape** \(k\) and **rate** \(\lambda\); the density is \(\lambda^k s^{k-1}e^{-\lambda s}/\Gamma(k)\) for \(s>0\). The stationary law is obtained using the equilibrium-renewal age \(A\), whose density is \(\mathbb P(S>a)/\mathbb E S\). This must not be confused with observing a single excursion just after a reset. All moments used below are finite.

## Proof

**1. Exact free-excursion moments.** Conditional on the transverse Brownian path, \(X_t\) is centered Gaussian with variance \(2D_xL_t\). The heat-kernel normalization gives

\[
\mathbb E[\delta_0(Y_s)]=(4\pi D_y s)^{-1/2},\qquad
\mathbb E X_t^2=\frac{2D_x}{\sqrt{\pi D_y}}\sqrt t,
\qquad \mathbb E Y_t^2=2D_y t.
\]

For \(0<s<t\), Brownian Markov independence yields

\[
\mathbb E[\delta_0(Y_s)Y_t^2]
=2D_y(t-s)(4\pi D_y s)^{-1/2}.
\]

Consequently

\[
\begin{aligned}
\mathbb E[X_t^2Y_t^2]
&=4D_xD_y\int_0^t\frac{t-s}{\sqrt{4\pi D_y s}}\,ds\\
&=\frac{8D_x\sqrt{D_y}}{3\sqrt\pi}\,t^{3/2}.
\end{aligned}
\]

At every deterministic \(t>0\), the free-excursion squared-coordinate covariance is thus strictly negative:

\[
\operatorname{Cov}(X_t^2,Y_t^2)
=-\frac{4D_x\sqrt{D_y}}{3\sqrt\pi}\,t^{3/2}.
\]

This is a genuine comb constraint: large excursions into a finger suppress longitudinal local time.

**2. Equilibrium renewal averaging.** With \(\bar F(a)=\mathbb P(S>a)\) and \(m=\mathbb E S=k/\lambda\), the equilibrium reset age has density \(\bar F(a)/m\). Hence for every \(p\ge0\), Tonelli's theorem and the Gamma moment formula give

\[
\mathbb E[A^p]
=\frac{\mathbb E S^{p+1}}{(p+1)\mathbb ES}
=\frac{\Gamma(k+p+1)}{(p+1)\Gamma(k+1)\lambda^p}.
\]

Writing \(a_p=\mathbb E[A^p]\), the free-excursion moments imply

\[
\begin{aligned}
\mathbb E X^2&=\frac{2D_x}{\sqrt{\pi D_y}}a_{1/2},\\
\mathbb E Y^2&=2D_y a_1,\\
\mathbb E[X^2Y^2]&=\frac{8D_x\sqrt{D_y}}{3\sqrt\pi}a_{3/2}.
\end{aligned}
\]

Subtracting the product of the two means and substituting the Gamma age moments gives

\[
\boxed{
\operatorname{Cov}(X^2,Y^2)
=\frac{4D_x\sqrt{D_y}}{15\sqrt\pi\,\lambda^{3/2}}
\frac{\Gamma(k+3/2)}{\Gamma(k+1)}(1-k).
}
\]

The denominator \(\mathbb E X^2\,\mathbb E Y^2\) equals

\[
\frac{4D_x\sqrt{D_y}}{3\sqrt\pi\,\lambda^{3/2}}
\frac{\Gamma(k+3/2)}{\Gamma(k+1)}(k+1).
\]

Division proves the claimed universal normalized identity. Its numerator changes sign only at \(k=1\); the function \((1-k)/(5(k+1))\) decreases strictly on \((0,\infty)\), with limiting values \(\pm1/5\). This also explicitly separates the negative within-excursion effect from positive random-age mixing.

**3. Full independence at and only at the exponential clock.** If \(k\ne1\), the proven nonzero squared-coordinate covariance rules out independence of \(X\) and \(Y\). For \(k=1\), let \(r=\lambda\), \(\beta=\sqrt{r/D_y}\) and \(\alpha=\sqrt{2\sqrt{rD_y}/D_x}\). The stationary reset Fokker–Planck equation is

\[
0=D_y\partial_{yy}p+D_x\delta_0(y)\partial_{xx}p-rp+r\delta_0(x)\delta_0(y).
\]

After Fourier transformation in \(x\), its unique exponentially decaying solution away from \(y=0\) has the form \(\widehat p(\xi,y)=c_\xi e^{-\beta|y|}\). Integrating across the backbone and using the unit point source gives

\[
c_\xi=\frac{r}{D_x\xi^2+2\sqrt{rD_y}}.
\]

Fourier inversion therefore yields the normalized stationary density

\[
p(x,y)=\frac{\alpha\beta}{4}e^{-\alpha|x|-\beta|y|}.
\]

Both marginals are normalized Laplace distributions, hence independent. The regenerative construction makes this law the unique invariant positional marginal. Combining with the previous paragraph proves the claimed **if and only if** within the Gamma family. The exponential-case resolvent/factorization is not asserted to be new.

## Verification

The standalone script `checks/check_gamma_clock.py` checks the Gamma equilibrium-age formula by independent survival-integral quadrature; checks mixed moments against the closed covariance and universal normalized ratio over multiple diffusion coefficients, reset rates and shapes on both sides of the threshold; checks the Poisson product density normalization and its first mixed moments; and independently integrates the Brownian return kernel producing the mixed \(t^{3/2}\) moment. Executing it with Python, SciPy and a standard math library returned 342 passing numerical/analytical checks. The infinite-dimensional and all-parameter claims are proved above, not inferred from these finite tests.

## Relationship to prior work

Domazetoski et al. (2020), DOI `10.1103/PhysRevResearch.2.033027`, derive the Poisson globally reset three-dimensional comb transform (their Eq. (4)) and explicitly explain its two-dimensional specialization (Sec. V). That published transform can already establish the \(k=1\) factorized distribution; it is background, not priority claimed here.

Masó-Puigdellosas, Sandev and Méndez (2023), DOI `10.3390/e25111529`, treat a general comb Langevin model with global and local resetting, including an exponential reset clock and power-law alternatives. Their relevant global-reset results in Sec. 3.3, Eqs. (31)–(37), concern the longitudinal mean squared displacement, not the **mixed fourth moment**, Gamma-shape crossover or the Gamma-family independence criterion. The renewal-moment identity itself is standard and not presented as new. The added statement is the exact shape-only two-coordinate dependence law.

Published research records and searches covering shared-clock Brownian covariance and renewal resetting were also compared; these involve different geometries or observables, and the close 2020 and 2023 comb papers remain the primary comparison. Absence of a matching indexed record cannot prove worldwide priority.

## Limitations

The theorem is for the unconfined, two-dimensional *continuum* comb with independent excursion noises, complete resets, Gamma renewal intervals, and equilibrium-renewal observation. It is not a result about discrete graph combs, finger-only resets, heavy-tailed intervals with infinite mean, finite-time initialization just after a reset, or higher-dimensional comb geometry. Zero covariance at the exponential clock is supplemented by a full density proof; zero covariance alone would not establish independence. The normalized ratio captures one fourth-order statistic and does not classify the entire joint density for \(k\ne1\). An unindexed stronger statement may affect publication priority.

## References

1. V. Domazetoski et al., *Stochastic resetting on comblike structures*, Physical Review Research **2**, 033027 (2020). DOI: https://doi.org/10.1103/PhysRevResearch.2.033027. Full legal OA text: https://webs.uab.cat/vmendez/wp-content/uploads/sites/97/2009/05/115.pdf.
2. A. Masó-Puigdellosas, T. Sandev and V. Méndez, *Random Walks on Comb-like Structures under Stochastic Resetting*, Entropy **25**, 1529 (9 November 2023). DOI: https://doi.org/10.3390/e25111529. Full text: https://www.mdpi.com/1099-4300/25/11/1529.
