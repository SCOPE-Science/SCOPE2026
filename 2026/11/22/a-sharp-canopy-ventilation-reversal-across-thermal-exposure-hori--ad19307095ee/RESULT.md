# A sharp canopy–ventilation reversal across thermal exposure horizons

## Finding

**Theorem (strict exposure log-concavity and one horizon reversal).** Let an idealized street canyon begin with zero excess heat, receive a constant positive heat source, and lose heat through first-order ventilation. Suppose the control \(x\in[0,L]\) reduces both the heat source and ventilation exponentially as specified below. For every integer \(k\ge0\) and every horizon \(T>0\), the iterated cumulative exposure \(E_k(T,x)\) is **strictly log-concave in canopy intensity**. Therefore every globally exposure-minimizing intensity is an endpoint: no intermediate intensity minimizes exposure.

More precisely, if the fractional shade attenuation \(\alpha\) is at least the fractional ventilation attenuation \(\beta\), full intensity \(x=L\) uniquely minimizes \(E_k\) for all \(T\). If \(0<\alpha<\beta\), there is one and only one horizon \(T_{*,k}\) at which the two endpoint risks tie. Full intensity is uniquely optimal below this horizon, and zero intensity is uniquely optimal above it. At the transition, precisely the two endpoints minimize exposure; every intermediate intensity has strictly higher exposure.

The geometry of the **worst**, rather than the best, intermediate choice also has a complete classification. There exists a unique \(y_k>0\) solving \(g_k(y_k)=\alpha/\beta\), with \(g_k\) defined below. If \(T\le y_k/\lambda_0\), exposure decreases strictly from \(x=0\) to \(x=L\). If \(T\ge e^{\beta L}y_k/\lambda_0\), exposure increases strictly from \(x=0\) to \(x=L\). In between these horizons it has exactly one interior critical point, a strict global **maximum**, situated at
\[
 x_{\max}(T)=\frac{1}{\beta}\log\!\left(\frac{\lambda_0T}{y_k}\right).
\]
The minimizer switch is contained strictly between these two monotonicity thresholds. The result covers terminal excess heat (\(k=0\)), integrated heat burden (\(k=1\)), and all higher integer time integrals.

## Assumptions and scope

Fix constants \(H_0,\lambda_0,\alpha,\beta,L>0\). Control \(x\) is held fixed throughout an observation interval. Source and ventilation are modeled by
\[
 H(x)=H_0e^{-\alpha x},\qquad \lambda(x)=\lambda_0e^{-\beta x}.
\]
The idealized one-zone excess heat \(U(t;x)\) solves \(\dot U=H(x)-\lambda(x)U\) with \(U(0;x)=0\). The dimensionless attenuation parameters are model assumptions, not empirically inferred canopy coefficients. For every integer \(k\ge0\), let
\[
 E_k(T,x)=H(x)\int_0^T(T-s)^k e^{-\lambda(x)s}\,ds,
 \qquad \phi_k(y)=\int_0^1(1-v)^k e^{-yv}\,dv.
\]
Then \(E_k(T,x)=H_0e^{-\alpha x}T^{k+1}\phi_k(\lambda_0Te^{-\beta x})\). In particular \(E_0=U(T;x)\), and \(E_1=\int_0^T U(t;x)\,dt\). For \(k\ge2\) this is a positive constant multiple of an iterated time integral, not a new physical measurement without additional interpretation.

Put
\[
 g_k(y)=-\frac{d\log\phi_k(y)}{d\log y}
 =\frac{y\int_0^1v(1-v)^ke^{-yv}\,dv}
 {\int_0^1(1-v)^ke^{-yv}\,dv},\qquad y>0.
\]
For \(0<\alpha<\beta\), define \(y_k\) as the unique solution of \(g_k(y)=\alpha/\beta\), and \(T_{*,k}\) as the unique positive solution of
\[
 \frac{\phi_k(e^{-\beta L}\lambda_0T)}{\phi_k(\lambda_0T)}=e^{\alpha L}.
\]
All uniqueness claims refer to positive real values; no spatially varying flow, heat-wave timing, dynamic canopy control, temperature-dependent ventilation, background heat storage, radiation, evapotranspiration or biological dose model is assumed.

## Proof

**1. Exact reduction.** Solving the scalar initial-value problem gives \(U(t;x)=H(x)\int_0^t e^{-\lambda(x)s}\,ds\). Fubini's theorem yields \(\int_0^TU(t;x)\,dt=H(x)\int_0^T(T-s)e^{-\lambda(x)s}\,ds\). The same positive-kernel argument extends the mathematical definition to all \(k\ge0\); substituting \(v=s/T\) yields the displayed expression for \(E_k\).

**2. Strict logarithmic concavity.** Set \(f_k(z)=\log\phi_k(e^z)\) for real \(z\). With \(v=e^w\), \(w<0\),
\[
 \phi_k(e^z)=\int_{-\infty}^{0}
 \exp\bigl(w+k\log(1-e^w)-e^{z+w}\bigr)\,dw.
\]
On the convex domain \(\{(z,w):z\in\mathbb R,w<0\}\), the logarithm of the integrand is jointly concave: \(w\) is affine, \(w\mapsto\log(1-e^w)\) is concave, and \(-(z,w)\mapsto e^{z+w}\) is concave after inserting the minus sign. The classical Prékopa marginal log-concavity theorem therefore proves that \(f_k\) is concave on \(\mathbb R\). (For \(k=0\) the middle term vanishes.) Moreover \(\phi_k(y)>0\) is real analytic in \(y>0\), so \(f_k\) is real analytic in real \(z\). As \(y\downarrow0\), \(\phi_k(y)\to1/(k+1)\) and \(y\phi_k'(y)/\phi_k(y)\to0\); as \(y\to\infty\), \(\phi_k(y)\sim 1/y\) and \(y\phi_k'(y)/\phi_k(y)\to-1\), by the substitution \(u=yv\) and dominated convergence. Thus \(f_k'\) takes distinct limiting values \(0\) and \(-1\). A concave analytic function that is affine on any nontrivial interval is affine everywhere; therefore \(f_k\) is strictly concave, and \(f'_k\) is strictly decreasing (any equality between derivative values of a differentiable concave function would make an interval affine). Hence \(g_k(y)=-f'_k(\log y)\) is continuous, strictly increasing from \(0\) to \(1\). Finally,
\[
 \log E_k(T,x)=\log(H_0T^{k+1})-\alpha x
 +f_k(\log(\lambda_0T)-\beta x),
\]
which is strictly concave for \(0\le x\le L\) since \(\beta>0\). A strictly concave function on a compact interval lies strictly above the chord between distinct endpoints: the minimum of \(E_k\) can occur only at the endpoints, with no interior ties.

**3. Single-crossing endpoints.** The endpoint risk ratio is
\[
 R_k(T)=\frac{E_k(T,L)}{E_k(T,0)}
 =e^{-\alpha L}\frac{\phi_k(e^{-\beta L}\lambda_0T)}{\phi_k(\lambda_0T)}.
\]
Writing \(y=\lambda_0T\), logarithmic differentiation gives
\[
 \frac{d\log R_k}{d\log T}
 =g_k(y)-g_k(e^{-\beta L}y)>0,
\]
because \(0<e^{-\beta L}<1\). Thus \(R_k\) is strictly increasing. Its small-horizon and long-horizon limits are respectively
\[
 \lim_{T\downarrow0}R_k(T)=e^{-\alpha L}<1,
 \qquad\lim_{T\to\infty}R_k(T)=e^{(\beta-\alpha)L}.
\]
When \(\alpha\ge\beta\), the endpoint ratio is strictly below \(1\) at every finite horizon (also directly from the derivative in step 4). When \(\alpha<\beta\), the limits straddle one, proving existence and uniqueness of the crossing \(T_{*,k}\). Strict log-concavity excludes intermediate minimizers, including at the endpoint tie.

**4. Where the interior maximum exists.** Differentiation gives
\[
 \frac{\partial}{\partial x}\log E_k(T,x)
 =-\alpha+\beta g_k(\lambda_0Te^{-\beta x}).
\]
The right-hand side is strictly decreasing with \(x\). If \(\alpha\ge\beta\), it is negative for every finite positive \(T\), using \(g_k(y)<1\). If \(0<\alpha<\beta\), the derivative changes sign at the unique \(x_{\max}\) displayed in the Finding, and that critical point lies in \((0,L)\) precisely for \(y_k/\lambda_0<T<e^{\beta L}y_k/\lambda_0\). At smaller horizons it is negative throughout \((0,L)\); at greater horizons it is positive throughout \((0,L)\). At either boundary it only vanishes at a boundary, so the function remains strictly monotone on the interval. Because its endpoints cannot tie in the monotone regimes and do tie at \(T_{*,k}\), the unique switch horizon lies strictly between the two thresholds.

## Verification

The standalone `verify.py` uses only Python's standard library and evaluates exact \(k=0\) and \(k=1\) formulas, integral quadrature for higher \(k\), root bracketing, boundary behavior, derivative signs, and finite numerical instances of the strict log-concavity and single-crossing statements. In its recorded run it passed **3,642 assertions**. These numerical checks are *regression tests* and do not replace the analytical proof for unbounded \(k\), continuous intensities, or unbounded horizons.

As one scale-free illustration take \(L=\lambda_0=H_0=1\), \(\alpha=\log2\) and \(\beta=\log4\). For terminal heat, \(y_0\approx1.256431208626\) and \(T_{*,0}\approx2.437511453744\); for integrated heat, \(y_1\approx2.149125799907\) and \(T_{*,1}\approx4.248570184265\). These are illustrative dimensionless parameters, not fitted urban measurements. For \(k=0\) and this parameter choice, the strictly positive critical elasticity root satisfies \(e^{y_0}=1+2y_0\). The endpoint tie can alternatively be verified by setting \(q=e^{-T_{*,0}/4}\), so the unique \(q\in(0,1)\) solves \(q^3+q^2+q-1=0\).

## Relationship to prior work

The wind-tunnel observations of Zhao et al. (2023) establish that the foliage-mediated exchange of street-canyon air and heat can change with tree size and thermal regime. Sharmin et al. (2023) provide field evidence that tree traits and observation times modulate cooling and warming. Liang et al. (2018) model street-canyon temperature with a multizone heat and airflow balance. Those sources motivate a transparent competing attenuation benchmark, but none of the inspected material asserts this exact one-zone, all-horizons endpoint reversal or strict log-concavity classification. The proof's decisive marginal log-concavity step is an application of the *established* Prékopa theorem, not a newly discovered general inequality. Schmidt and Schwabe use related log-concavity tools in a different statistical-design integral, not this heat-balance objective. These comparisons do not establish exhaustive priority over all uninspected prior literature.

## Limitations

The exponential source and ventilation laws are stipulated. A real tree crown may cool through evapotranspiration, reduce incoming radiation, alter longwave exchange, change turbulent transfer, and vary throughout a heatwave. Real observations can contain positive initial thermal storage, heterogeneous temperature fields, wind dependence, time-varying forcing, and nonconvex feasible canopy decisions. The theorem does **not** say that cities should eliminate or maximize actual tree cover: doing so would ignore ecological benefits and physical mechanisms outside this scalar model. It also does not estimate mortality, exposure distributions, or empirical temperature changes. If \(\alpha=0\), \(\beta=0\), or a positive initial condition is included, the stated strict classification need not apply; these are excluded by hypothesis. The cited literature supports motivation and comparison, not field validation. Historical priority remains a risk because not every plausible recent applied optimization paper was available in full text; this work is not independently audited.

## References

1. Y. Zhao, H. Li, R. Bardhan, A. Kubilay, Q. Li, J. Carmeliet, *The time-evolving impact of tree size on nighttime street canyon microclimate: Wind tunnel modeling of aerodynamic effects and heat removal*, arXiv:2301.05766 (first public posting 2023-01-13), https://arxiv.org/abs/2301.05766 ; journal DOI: https://doi.org/10.1016/j.uclim.2023.101528 .
2. M. Sharmin et al., *Tree Traits and Microclimatic Conditions Determine Cooling Benefits of Urban Trees*, Atmosphere 14 (2023), 606, https://doi.org/10.3390/atmos14030606 .
3. W. Liang et al., *A zonal model for assessing street canyon air temperature of high-density cities*, Building and Environment 132 (2018), 160–169, https://doi.org/10.1016/j.buildenv.2018.01.035 ; author manuscript https://orca.cardiff.ac.uk/id/eprint/109839/1/accepted%20manuscript.pdf .
4. A. Prékopa, *Logarithmic concave measures with application to stochastic programming*, Acta Sci. Math. (Szeged) 32 (1971), 301–316 (classical marginal log-concavity principle).
5. D. Schmidt and R. Schwabe, *Optimal Design for Multiple Regression with Information Driven by the Linear Predictor*, Statistica Sinica, DOI https://doi.org/10.5705/ss.202015.0385 ; accessible preprint https://www3.stat.sinica.edu.tw/preprint/SS-2015-0385_Preprint.pdf .
