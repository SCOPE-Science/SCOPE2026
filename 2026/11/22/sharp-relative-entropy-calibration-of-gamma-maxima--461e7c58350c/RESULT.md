# Sharp relative-entropy calibration of gamma maxima

## Finding

Let \(\alpha>0\) be fixed, \(\alpha\ne1\). For every integer \(n\ge2\), let \(X_1,\ldots,X_n\) be independent rate-one Gamma variables with shape \(\alpha\), and let \(M_n=\max_iX_i\). Write
\[
 S_\alpha(x)=\frac{\Gamma(\alpha,x)}{\Gamma(\alpha)},\qquad
 f_\alpha(x)=\frac{x^{\alpha-1}e^{-x}}{\Gamma(\alpha)},\qquad x>0,
\]
where \(\Gamma(\alpha,x)\) is the upper incomplete gamma integral. Define the *exact* upper-tail quantile \(b_n>0\) and reciprocal-hazard scale \(a_n>0\) by
\[
 S_\alpha(b_n)=n^{-1},\qquad a_n=\frac{S_\alpha(b_n)}{f_\alpha(b_n)},\qquad
 Y_n=\frac{M_n-b_n}{a_n}.
\]
For \(\mu\in\mathbb R\), \(\sigma>0\), let \(G_{\mu,\sigma}\) be the Gumbel distribution with CDF \(\exp\{-\exp[-(y-\mu)/\sigma]\}\); write \(D(P\Vert Q)\) for **forward** Kullback–Leibler divergence, using natural logarithms. Then, with \(\zeta\) denoting the Riemann zeta function,
\[
 \boxed{\lim_{n\to\infty}\frac{b_n^4}{(\alpha-1)^2}
 \inf_{\mu\in\mathbb R,\,\sigma>0}
 D(\mathcal L(Y_n)\Vert G_{\mu,\sigma})
 =C_*=\frac{11\pi^4}{720}-\frac{3\zeta(3)^2}{\pi^2}
 =1.048985110381614\ldots>0.}
\]
The optimal Gumbel parameters exist and are unique for each \(n\), and have the explicit asymptotics
\[
 \mu_n=\frac{\alpha-1}{b_n^2}\,d_\mu+o_\alpha(b_n^{-2}),\qquad
 \sigma_n=1+\frac{\alpha-1}{b_n^2}\,d_\sigma+o_\alpha(b_n^{-2}),
\]
where \(\gamma\) is Euler's constant and
\[
 d_\sigma=1-\gamma-\frac{\zeta(3)}{\zeta(2)}=-0.307978634302971\ldots,
\]
\[
 d_\mu=\frac{\gamma^2-2\gamma+2-\zeta(2)}2
   +(\gamma-1)\frac{\zeta(3)}{\zeta(2)}
   =-0.542048872554755\ldots.
\]
Even **without** the additional Gumbel fitting, the reciprocal-hazard normalization is second-order accurate in density and obeys
\[
 D(\mathcal L(Y_n)\Vert G_{0,1})\sim
 \frac{(\alpha-1)^2}{2b_n^4}\,\mathbb E[s(Z)^2]
 =\frac{(\alpha-1)^2}{b_n^4}(1.211803027588514\ldots),
\]
where \(Z\sim G_{0,1}\) and
\[
 s(y)=y+\frac{e^{-y}-1}{2}y^2.
\]
Because \(b_n\sim\log n\), the optimal information loss has the sharp logarithmic order \((\log n)^{-4}\) for *every* fixed nonexponential Gamma shape. The exponential endpoint \(\alpha=1\) is explicitly excluded: its different, faster finite-sample rate is prior work, not part of this result.

## Assumptions and scope

The sample is iid; the Gamma shape \(\alpha\) is a **fixed** arbitrary positive real number different from one; rate one entails no loss because affine Gumbel minimization is invariant under a positive scaling of all observations. The sample size tends through integers \(n\to\infty\). Forward KL is taken from the continuous normalized maximum to a positive-density Gumbel reference. The claimed parameter uniqueness is for this forward KL objective; no reverse KL claim is made. The relative error \(o_\alpha(1)\) is not asserted to be uniform when \(\alpha\) varies with \(n\), particularly near one.

## Proof

**1. Exact finite-sample distribution and unique Gumbel fit.** Let \(F_\alpha=1-S_\alpha\). On \(y>-b_n/a_n\), the density of \(Y_n\) is
\[
 p_n(y)=na_nf_\alpha(b_n+a_ny)F_\alpha(b_n+a_ny)^{n-1},
\]
and it is zero below that endpoint. Its entropy \(H(Y_n)\) is finite for every positive shape, including shapes below one: at the endpoint the density has an integrable power singularity, and at infinity it has an exponential tail.

Fix \(n\), put \(m_n=\mathbb EY_n\), and \(L_n(r)=\mathbb Ee^{-rY_n}\) for \(r>0\). The support has a finite lower endpoint, so \(L_n(r)<\infty\). From the Gumbel density, with \(r=1/\sigma\),
\[
 D(\mathcal L(Y_n)\Vert G_{\mu,1/r})
 =-H(Y_n)-\log r+r(m_n-\mu)+e^{r\mu}L_n(r).
\]
For a fixed \(r\), the unique minimizing location is \(\mu=-r^{-1}\log L_n(r)\). The resulting one-dimensional objective is
\[
 J_n(r)=-H(Y_n)-\log r+rm_n+\log L_n(r)+1.
\]
Its second derivative is \(J_n''(r)=r^{-2}+\operatorname{Var}_{n,r}(Y_n)>0\), where \(\operatorname{Var}_{n,r}\) is computed under the exponentially tilted probability with density proportional to \(p_n(y)e^{-ry}\). As \(r\downarrow0\), \(J_n(r)\to\infty\) because of \(-\log r\). As \(r\to\infty\), the Laplace principle at the finite lower endpoint \(\ell_n=-b_n/a_n\) gives \(\log L_n(r)=-r\ell_n+O(\log r)\), and therefore \(J_n(r)\to\infty\), since \(m_n>\ell_n\). Thus there is exactly one global optimal \(r_n>0\), and exactly one \((\mu_n,\sigma_n)\), with \(\sigma_n=r_n^{-1}\).

**2. Tail expansion at exact hazard normalization.** Put \(c=\alpha-1\), \(b=b_n\), \(a=a_n\), and \(\ell(x)=\log S_\alpha(x)\). Standard repeated integration by parts in the upper incomplete-gamma integral, with differentiable remainders for a fixed shape, gives as \(x\to\infty\)
\[
 \ell(x)=-x+c\log x-\log\Gamma(\alpha)+c/x+O_\alpha(x^{-2}),
\]
\[
 \ell''(x)=-c/x^2+O_\alpha(x^{-3}),\qquad
 \ell'''(x)=O_\alpha(x^{-3}).
\]
By definition, \(a\ell'(b)=-1\). On every central range \(|y|=O(\log b)\), Taylor's theorem therefore gives
\[
 \log\{nS_\alpha(b+ay)\}
 =-y-\frac{c}{2b^2}y^2
 +O_\alpha\!\left(\frac{1+|y|^3}{b^3}\right),
\]
with the differentiated expansion holding on the same range. As \(b\sim\log n\), \(n^{-1}\) is smaller than every fixed inverse power of \(b\).

Set \(G(y)=e^{-e^{-y}}\), \(g(y)=e^{-y-e^{-y}}\), and \(A_b=[-2\log\log b,\,10\log b]\) for sufficiently large \(b\). Since
\[
 \Pr(Y_n\le y)=\big\{1-n^{-1}[nS_\alpha(b+ay)]\big\}^n,
\]
the expansion of the preceding display and its derivative yield, **uniformly for \(y\in A_b\)**,
\[
 \frac{p_n(y)}{g(y)}
 =1+\frac{c}{b^2}s(y)
 +O_\alpha\!\left(\frac{(\log b)^K}{b^3}\right),
 \qquad s(y)=y+\frac{e^{-y}-1}{2}y^2,
\]
for some absolute finite exponent \(K\). The sign in \(s\) follows by differentiating \(G(y)e^{-y}y^2/2\); the density expansion integrates to zero at first order.

**3. Tail control and passage to forward KL.** Here the moving window is important because a local density expansion alone does not prove an entropy asymptotic. Both laws assign \(o(b^{-m})\) mass to \(A_b^c\), for every fixed \(m>0\) on the left, and at least \(O(b^{-9})\) on the right. More precisely, for \(z\ge2\log\log b\) with \(b-az\ge b/2\), the ratio \(nS_\alpha(b-az)\ge\exp[(1-O_\alpha(b^{-1}))z]\). Hence
\[
 \Pr(Y_n\le-z)\le
 \exp\{-\exp[(1-O_\alpha(b^{-1}))z]\}.
\]
For the deeper range \(0<b+ay<b/2\), \(\Pr(Y_n\le y)\le\exp[-c_\alpha e^{b/3}]\) for all sufficiently large \(b\) and some \(c_\alpha>0\). At the right endpoint, the formula for \(p_n\), together with the Gamma upper-tail estimate, gives \(p_n(y)\le C_\alpha e^{-0.85y}\) for \(y\ge10\log b\) and large \(b\). On this right range \(|\log(p_n/g)|\le C_\alpha(1+y+|\log(1+y)|)\). On the left the same expectation bound follows from integration by parts applied to the displayed double-exponential CDF bound; near the lower support endpoint the \(|\log(b+ay)|\) singularity is integrable against the Gamma density. Consequently
\[
 \int_{A_b^c}p_n(y)\left|\log\frac{p_n(y)}{g(y)}\right|dy=o_\alpha(b^{-4}),
\]
and likewise the complementary first-order mass discrepancy and relevant polynomial score moments are negligible at order \(b^{-4}\). These estimates justify Taylor expansion of \((1+z)\log(1+z)\) under the density integral, not only pointwise. Since \(\int g s=0\),
\[
 D(\mathcal L(Y_n)\Vert G_{0,1})
 =\frac{c^2}{2b^4}\int_{\mathbb R}g(y)s(y)^2dy+o_\alpha(b^{-4}).
\]

**4. Globally optimal location and scale, and the constant.** The two Gumbel location/scale score functions at \((\mu,\sigma)=(0,1)\) are
\[
 t_\mu(y)=1-e^{-y},\qquad
 t_\sigma(y)=-1+y(1-e^{-y}).
\]
The KL convergence above forces every globally minimizing Gumbel law to converge to \(G_{0,1}\). By the exact strict-convex objective in Step 1 and the smooth score equations, its deviations are of order \(b^{-2}\). Expanding the Gumbel density in those two coordinates shows that the sharp local KL coefficient is the squared \(L^2(g)\) distance from \(s\) to the span of \(t_\mu,t_\sigma\), divided by two:
\[
 \frac12\min_{u,v\in\mathbb R}
 \mathbb E\{s(Z)-u t_\mu(Z)-v t_\sigma(Z)\}^2.
\]
This is not merely an upper bound: the strictly convex exact objective ensures that the global optimizer is the local projection and excludes a better distant parameter choice.

For independent notation, put \(U=e^{-Z}\sim\operatorname{Exp}(1)\). Every needed moment follows from
\[
 \mathbb E[U^j(-\log U)^m]=(-1)^m\Gamma^{(m)}(j+1),\qquad j=0,1,2,\;m\le4.
\]
The Gram matrix of the scores and the cross-product vector are
\[
 \mathcal I=
 \begin{pmatrix}
 1&\gamma-1\\
 \gamma-1&(\gamma-1)^2+\zeta(2)
 \end{pmatrix},\qquad
 v=\begin{pmatrix}\mathbb E[s(Z)t_\mu(Z)]\\\mathbb E[s(Z)t_\sigma(Z)]\end{pmatrix}.
\]
In particular \(\det\mathcal I=\zeta(2)>0\), and explicit evaluation of \(\mathcal I^{-1}v\) gives \((d_\mu,d_\sigma)^\top\) displayed in the Finding. Evaluation of the residual yields
\[
 \frac12\{\mathbb E[s(Z)^2]-v^\top\mathcal I^{-1}v\}
 =\frac{\zeta(2)^3+3\zeta(2)\zeta(4)-2\zeta(3)^2}{4\zeta(2)}
 =\frac{11\pi^4}{720}-\frac{3\zeta(3)^2}{\pi^2}.
\]
It is strictly positive because the quadratic-polynomial component of \(s(y)\) cannot be expressed as a linear combination of the two score functions for all \(y\). The stated limit and optimizer expansions follow. \(\square\)

## Verification

The included `verify.py` independently evaluates the Gaussian-score Gram integrals via \(U\sim\operatorname{Exp}(1)\), confirms the zeta-value expression and the two optimizing coefficients to more than 25 decimal places, and evaluates the **exact** finite-sample KL objective by quadrature using the inverse regularized incomplete-gamma function. The extra test cases with Gamma shapes two and three and sample size one million check the scale and strict improvement numerically. They are diagnostics only: the infinite limit, global optimality, and tail estimates are provided analytically above. Run with `python verify.py` using Python 3, SciPy, NumPy, and mpmath. The accompanying `CHECKS.txt` contains the actual output.

## Relationship to prior work

Johnson, *Information-theoretic convergence of extreme values to the Gumbel distribution*, arXiv:2007.03569, first posted 7 July 2020, introduces max-score methods and proves relative-entropy convergence for Gamma maxima among other families. Its concluding discussion explicitly identifies optimal relative-entropy rates as a further question; it does not supply this shape-uniform logarithmic-fourth-power constant or an optimal Gumbel projection. Gasull, López-Salcedo, and Utzet, *Maxima of Gamma random variables and other Weibull-like distributions and the Lambert W function*, *TEST* 24 (2015), analyze Gamma extreme-value norming constants, CDF convergence, and detection applications; that comparison is important since the present normalization is not new. The leading Gamma tail expansion and classical extreme-value limit are standard tools, not novelty claims. Related earlier work on optimizing the KL fit for **exponential** maxima covers \(\alpha=1\), whose order is different and does not imply the nonexponential result. The new claim is the exact global **forward-KL** optimum and universal zeta-value coefficient for fixed \(\alpha\ne1\), not merely the usual Gumbel convergence or CDF correction.

## Limitations

This is a first-order asymptotic as \(n\to\infty\) for each fixed nonexponential shape, not a nonasymptotic error bound, not a uniform-in-shape result, and not a statement of independence or outside mathematical certification. Numerical tests are finite diagnostics. The optimizer belongs to the Gumbel location-scale family only. In reverse KL, the Gumbel law assigns positive mass below the finite lower support endpoint of \(Y_n\); hence reverse KL is infinite, so the direction is essential. A specialized historical work not identified in the searches could already contain an equivalent constant; the literature comparison is qualified accordingly.

## References

1. O. T. Johnson, *Information-theoretic convergence of extreme values to the Gumbel distribution*, arXiv:2007.03569 (first public version, 2020-07-07; subsequent *Journal of Applied Probability* 61 (2024), 244–254), https://arxiv.org/abs/2007.03569, https://doi.org/10.1017/jpr.2023.37.
2. A. Gasull, J. A. López-Salcedo and F. Utzet, *Maxima of Gamma random variables and other Weibull-like distributions and the Lambert W function*, *TEST* 24 (2015), 714–733, https://doi.org/10.1007/s11749-015-0431-9; lawful preprint https://files01.core.ac.uk/download/pdf/78533779.pdf.
3. Y. Ma and B. Tian, *Revisit on the convergence rate of normal extremes*, arXiv:2507.09496 (2025). This is a separate Gaussian-parent case; no Gamma KL optimum is inferred from its abstract.
