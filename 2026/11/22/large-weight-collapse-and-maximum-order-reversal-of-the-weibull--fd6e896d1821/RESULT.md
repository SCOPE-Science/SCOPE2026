# Large-weight collapse and maximum-order reversal of the Weibull min-characteristic goodness-of-fit statistic

## Finding

For a fixed nonconstant sample of positive observations fitted by the two-parameter Weibull maximum-likelihood estimator, consider the exponentially weighted squared empirical min-characteristic-function statistic defined below. As the weight parameter \(\gamma\to\infty\), the statistic has a leading term independent of every observation, but its first sample-dependent correction is determined by the largest fitted-and-standardized observation. Specifically, for sample size \(n\ge2\), write \(M=\max_j Y_j\) and \(r=\#\{j:Y_j=M\}\). Then

\[
T_{n,\gamma}=nI(\gamma)-\frac{2r e^{-M}}{\gamma^2}e^{-\gamma/M}(1+O_Y(\gamma^{-1})),\qquad
I(\gamma)=2\left(\frac2\gamma\right)^{3/2}K_3(2\sqrt{2\gamma}).
\]

The deterministic term satisfies

\[
I(\gamma)\sim 2^{5/4}\sqrt\pi\,\gamma^{-7/4}e^{-2\sqrt{2\gamma}}.
\]

Thus for two fixed samples of the same size with unequal standardized maxima, the larger-max sample eventually has the **smaller** goodness-of-fit statistic as \(\gamma\to\infty\). Moreover, the following bound holds for **every** strictly positive vector of standardized values with mean one, not just genuine fitted samples:

\[
\left|T_{n,\gamma}-nI(\gamma)\right|
\le n e^{-\gamma/n}\left(\frac{1+n^{-2}}{\gamma}+\frac{2}{n\gamma^2}+\frac{2}{\gamma^3}\right).
\]

Consequently, for any integer sequence \(n=n(\gamma)\ge2\) with \(\gamma/n(\gamma)^2\to\infty\), the ratio \(T_{n,\gamma}/(nI(\gamma))\to1\) uniformly over such mean-one vectors.

## Assumptions and scope

Let \(n\ge2\) and let \(x_1,\ldots,x_n>0\) not all be equal. The fitted null family is the two-parameter Weibull family

\[
F_{c,\phi}(x)=1-\exp(-(x/c)^\phi),\qquad c>0,\ \phi>0,\ x>0.
\]

Let \((\widehat c,\widehat\phi)\) denote a finite positive joint maximum-likelihood estimate. Set \(Y_j=(x_j/\widehat c)^{\widehat\phi}\). Let

\[
\psi_n(t)=\frac1n\sum_{j=1}^n\min\{1,tY_j\},\quad
\psi_0(t)=t(1-e^{-1/t}),\quad
T_{n,\gamma}=n\int_0^\infty(\psi_n(t)-\psi_0(t))^2 e^{-\gamma t}\,dt
\]

for every \(\gamma>0\). Here \(K_3\) is the modified Bessel function of the second kind. These are the Weibull member and exponential weighting convention of the min-characteristic-function test of Meintanis, Milošević and Jiménez-Gamero, arXiv:2310.12348, equations (3.1), (3.3), (4.1)–(4.3). The second-order limit fixes both the sample and its fitted values while \(\gamma\to\infty\); the uniform leading-term statement also allows \(n\) to increase with \(\gamma\).

## Proof

**Step 1: an exact profile-likelihood constraint.** For fixed Weibull shape \(\phi>0\), differentiating the log likelihood with respect to the scale gives the maximizer

\[
\widehat c(\phi)^\phi=\frac1n\sum_{j=1}^n x_j^\phi.
\]

Hence at the joint MLE, \(\sum_{j=1}^nY_j=n\). In particular, \(0<Y_j\le n\) and \(M\le n\). For every \(0<t\le1/n\), no term of the empirical minCF is truncated, so \(\psi_n(t)=t\). Since a unit exponential law has \(\psi_0(t)=t(1-e^{-1/t})\), on that whole interval the difference is exactly \(t e^{-1/t}\), independently of the sample.

**Step 2: a uniform nonasymptotic estimate.** Let \(a=1/n\) and \(I(\gamma)=\int_0^\infty t^2 e^{-2/t-\gamma t}\,dt\). The integrands defining \(T_{n,\gamma}/n\) and \(I(\gamma)\) coincide on \((0,a]\). On \([a,\infty)\), the squared minCF difference is at most one, while \(t^2e^{-2/t}\le t^2\). Therefore

\[
\left|\frac{T_{n,\gamma}}n-I(\gamma)\right|
\le\int_a^\infty(1+t^2)e^{-\gamma t}\,dt
=e^{-\gamma a}\left(\frac{1+a^2}{\gamma}+\frac{2a}{\gamma^2}+\frac2{\gamma^3}\right).
\]

This proves the stated bound without any probabilistic approximation. The classical Bessel integral identity yields \(I(\gamma)=2(2/\gamma)^{3/2}K_3(2\sqrt{2\gamma})\). Alternatively set \(t=\sqrt{2/\gamma}\,s\). Laplace's method for the strictly minimized phase \(s+s^{-1}\), whose unique minimum at \(s=1\) is two and whose second derivative there is two, gives

\[
I(\gamma)\sim2^{5/4}\sqrt\pi\,\gamma^{-7/4}e^{-2\sqrt{2\gamma}}.
\]

If \(\gamma/n^2\to\infty\), the ratio between the explicit error bound and \(I(\gamma)\) vanishes: its exponential part is \(\exp\{-\gamma/n+2\sqrt{2\gamma}\}\), which beats every polynomial factor. This is uniform in the observations.

**Step 3: the first sample-dependent term.** For every \(t>0\) define

\[
A_Y(t)=\frac1n\sum_{j=1}^n(tY_j-1)_+,\qquad d(t)=t e^{-1/t}.
\]

The exact identity \(\psi_n(t)=t-A_Y(t)\) gives

\[
nI(\gamma)-T_{n,\gamma}
=n\int_0^\infty\{2d(t)A_Y(t)-A_Y(t)^2\}e^{-\gamma t}\,dt.
\]

Put \(t_0=1/M\). Then \(A_Y(t)=0\) for \(t\le t_0\). On a fixed right neighborhood of \(t_0\), only the \(r\) largest fitted values are active, so \(A_Y(t_0+s)=rMs/n\) for small positive \(s\). In addition, \(d(t_0+s)=e^{-M}/M+O_Y(s)\). Thus the bracket after multiplication by \(n\) equals \(2r e^{-M}s+O_Y(s^2)\). Integration against \(e^{-\gamma(t_0+s)}\) gives the leading correction \(2r e^{-M}e^{-\gamma/M}/\gamma^2\) with relative error \(O_Y(\gamma^{-1})\). Contributions beyond that right neighborhood have a strictly larger exponential decay rate and are negligible. This proves the second-order formula, including its positive sign for sufficiently large \(\gamma\).

**Step 4: reverse-maximum ordering.** For two samples of common size \(n\), the term \(nI(\gamma)\) is identical. If their standardized maxima satisfy \(M_A>M_B\), their positive second-order corrections obey

\[
\frac{nI(\gamma)-T_{A,\gamma}}{nI(\gamma)-T_{B,\gamma}}
\sim\frac{r_A e^{-M_A}}{r_B e^{-M_B}}\exp\{\gamma(M_B^{-1}-M_A^{-1})\}\longrightarrow\infty.
\]

Therefore \(T_{A,\gamma}<T_{B,\gamma}\) for every sufficiently large \(\gamma\), with threshold permitted to depend on the two fixed samples.

## Verification

A standalone script, `verify_min_cf.py`, independently evaluates the Bessel integral and its direct quadrature; constructs the test statistic from piecewise integrals; checks the exact correction identity and deterministic error bound for four distinct mean-one samples; verifies the first nonconstant endpoint correction at multiple weights; profiles Weibull MLEs for two positive samples; and checks the eventual reverse-maximum ordering numerically. It reports 66 passed numerical assertions using 65-digit arithmetic. The infinite-dimensional and asymptotic claims are proved above, not inferred from these finite checks. Run `python verify_min_cf.py` with `mpmath>=1.2`.

## Relationship to prior work

The 2023 min-characteristic-function test paper, arXiv:2310.12348 (first publicly posted 2023-10-18), defines exactly this fitted Weibull test and analyzes its null limit and fixed-alternative consistency at **fixed** positive weight, including experiments at \(\gamma=0.5,1,5\). Its full accessible text, including definitions, asymptotics, simulations and appendix, does not give the large-\(\gamma\) deterministic saddle-point term, the sample-dependent endpoint correction, or reverse-maximum ordering. Matsui and Meintanis, arXiv:2307.03429, establish the MLE-equivariance and distribution-free standardization of Weibull tests but not a varying-weight result. Falk and Stupfler establish general uniqueness and empirical-process theory for minCFs, not these weighted test asymptotics. A published version of the first paper appeared in 2024; the first public date is the 2023 arXiv submission. These comparisons do not claim priority over all classical Laplace-asymptotic methods.

## Limitations

The second-order asymptotic and rank reversal fix the sample as \(\gamma\to\infty\); they are **not** a simultaneous limit theorem for the null distribution of the fitted maximum. The joint regime \(\gamma/n^2\to\infty\) proves only leading-term collapse, not a second-order limit uniform in growing \(n\). Fixed-weight consistency from the original work remains intact. In particular, convergence of the normalized statistic to a deterministic term does **not** alone imply zero calibrated power, because extremely small sample-dependent differences retain an ordering. Finite-precision cancellation may become severe, but no computational accuracy or significance-level threshold is asserted. The exact asymptotic for fixed data presupposes a finite joint MLE; equal observations are excluded. The published literature comparison is not a proof of global novelty.

## References

1. S. G. Meintanis, B. Milošević and M. D. Jiménez-Gamero, *Goodness-of-Fit Tests Based on the Min-Characteristic Function*, arXiv:2310.12348 (first submission 2023-10-18), https://arxiv.org/abs/2310.12348 ; journal version, *Computational Statistics & Data Analysis* 197 (2024), 107988, https://doi.org/10.1016/j.csda.2024.107988.
2. M. Matsui and S. G. Meintanis, *MLE-Equivariance, Data Transformations and Invariant Tests of Fit*, arXiv:2307.03429 (first submission 2023-07-07), https://arxiv.org/abs/2307.03429.
3. M. Falk and G. Stupfler, *The Min-characteristic Function: Characterizing Distributions by Their Min-linear Projections*, *Sankhya A* 83 (2021), 254–282, https://doi.org/10.1007/s13171-019-00184-1.
