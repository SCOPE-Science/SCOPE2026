# The sharp Beta sampling density for integrated Brownian-bridge energy

## Finding
Let \(B\) be a standard Brownian bridge pinned at zero at times \(0\) and \(1\), and define its integrated quadratic energy
\[
Q=\int_0^1 B_t^2\,dt.
\]
Choose \(n\) deterministic times before observing the path. From the exact values \(B_{t_1},\ldots,B_{t_n}\), estimate \(Q\) by its conditional expectation \(\widehat Q\). Write \(R_n^*\) for the infimum of the unconditional mean squared error over all such designs. Then
\[
\boxed{\lim_{n\to\infty}(n+1)^2 R_n^*
=\frac13\operatorname{B}\!\left(\frac43,\frac43\right)^3
=0.049623314190395\ldots.}
\]
This constant is attained by placing the observation times at successive quantiles of the \(\operatorname{Beta}(4/3,4/3)\) law. For comparison, the equally spaced scheme has limit \(1/18=0.055555555555556\ldots\), so the asymptotically optimal design reduces squared-error risk by \(10.678034457289\ldots\%\).

More strongly, for **every finite ordered design**, an exact, elementary gap formula gives its risk. With endpoints \(t_0=0,t_{n+1}=1\) and gaps \(\ell_i=t_{i+1}-t_i\),
\[
\boxed{R(t_1,\ldots,t_n)=\sum_{i=0}^{n}
\left[\frac{t_i(1-t_{i+1})\ell_i^3}{3}
+\frac{\ell_i^4}{9}-\frac{4\ell_i^5}{45}\right].}
\]
The asymptotic result is not an assertion that Beta quantiles optimize each fixed finite \(n\).

## Assumptions and scope
The process is centered Gaussian with covariance
\(K(s,t)=\min(s,t)-st\), \(0\le s,t\le1\). Observations are exact, are made at predetermined nonadaptive times, and have zero cost other than their count. The squared loss is for the **single nonlinear path functional** \(Q\), not integrated pointwise path-reconstruction error and not Gaussian-process quadrature of \(\int B_t\,dt\). Since conditioning on duplicated readings adds no information, allow weakly ordered \(0\le t_1\le\dots\le t_n\le1\) when taking the infimum. All times and risks are dimensionless with interval length one and unit Brownian variance.

## Proof
**1. Posterior covariance and exact gap identity.** Fix distinct interior sample times and put \(a=t_i\), \(b=t_{i+1}\), \(\ell=b-a\). Write \(B=m+Z\), where \(m=\mathbb E[B\mid\text{observations}]\) and the zero-mean Gaussian residual \(Z\) is independent of those observations. Its covariance \(C\) vanishes between different gaps, and within a gap, for \(0\le u\le v\le\ell\), is
\[
C(a+u,a+v)=\frac{u(\ell-v)}{\ell}.
\]
The covariance of \(m\) is \(K-C\). Isserlis' identity, followed by total expectation, gives
\[
R=2\iint C(s,t)^2\,ds\,dt
+4\iint C(s,t)(K-C)(s,t)\,ds\,dt.
\]
These double integrals are sums over gaps. Direct integration on the triangle \(0\le u\le v\le\ell\) gives, on one gap,
\[
\iint C^2=\frac{\ell^4}{90},\qquad
\iint C(K-C)=\frac{a(1-b)\ell^3}{12}
+\frac{(1-\ell)\ell^4}{45}.
\]
Substitution yields the stated exact risk expression. Its individual summands are nonnegative: \(a(1-b)\ge0\) and \(\ell^4(5-4\ell)/45\ge\ell^4/45\), since \(0\le\ell\le1\). The expression is continuous at merged or endpoint observation times, so it also covers repeated readings without assuming an invertible observation covariance.

**2. Lower bound for any asymptotically optimal sequence.** Set \(m=n+1\) and \(g(s)=[s(1-s)]^{1/3}\). A uniform grid has risk \((5m^2-5m+2)/(90m^4)=O(m^{-2})\). Thus a minimizing or asymptotically minimizing family can be taken to have \(m^2R\le C\). The nonnegative remainder in the exact gap formula shows \(\sum_i\ell_i^4\le45R\); therefore \(\max_i\ell_i\le(45C)^{1/4}m^{-1/2}\to0\). By Hölder's inequality for the \(m\) gap terms,
\[
3m^2R\ge m^2\sum_i[t_i(1-t_{i+1})]\ell_i^3
\ge\left(\sum_i[t_i(1-t_{i+1})]^{1/3}\ell_i\right)^3.
\]
Because the maximum gap tends to zero and \(g\) is uniformly continuous, the bracket is a convergent Riemann sum for
\[
I=\int_0^1 g(s)\,ds=\operatorname B\!\left(\frac43,\frac43\right).
\]
Consequently \(\liminf_{m\to\infty}m^2R_n^*\ge I^3/3\). The compactified ordered-design simplex ensures a minimizer exists for each \(n\); alternatively, take near-minimizers.

**3. Constructing asymptotically attaining sites.** Define \(F(t)=I^{-1}\int_0^t g(s)\,ds\) and choose the sites \(t_i=F^{-1}(i/m)\), \(1\le i<m\). Every gap has \(\int_{t_i}^{t_{i+1}}g(s)\,ds=I/m\). On any fixed interior subinterval \([\varepsilon,1-\varepsilon]\), the mean-value theorem and uniform continuity give \(\ell_i=I/(mg(\xi_i))\) for some \(\xi_i\) in the gap. Hence each interior leading-risk term is asymptotic to \(I^3/(3m^3)\), uniformly there.

For the boundary tails, since \(g(s)\asymp s^{1/3}\) near zero and symmetrically near one, the quantiles obey \(t_i\asymp(i/m)^{3/4}\) and \(\ell_i\le C m^{-3/4}i^{-1/4}\) for \(1\le i\le m/2\), with symmetric bounds at the other endpoint. The leading terms on each \(\varepsilon\)-boundary fraction sum to at most \(C\varepsilon m^{-2}\), while \(\sum_i\ell_i^4=O(m^{-3}\log m)=o(m^{-2})\). The corresponding fifth-power sum is smaller. Thus after letting \(m\to\infty\) and then \(\varepsilon\downarrow0\), this explicit quantile design has \(\limsup m^2R\le I^3/3\), matching the lower bound.

**4. Uniform-grid comparison.** Substituting \(t_i=i/m\) into the exact gap formula gives
\[
R_{\rm uniform}=\frac{5m^2-5m+2}{90m^4};\qquad
\lim_{m\to\infty}m^2R_{\rm uniform}=\frac1{18}.
\]
Dividing the sharp and uniform constants proves the stated relative decrease \(1-6I^3\).

## Verification
The included standalone \(\texttt{verify.py}\) reproduces the conditional covariance integrals symbolically, proves the uniform-grid identity for symbolic \(m\), checks five cases by independent two-dimensional Gaussian covariance quadrature, tests 986 rational gap designs, and evaluates Beta-quantile grids of 10, 30, 100, and 300 intervals. Its recorded output is included as \(\texttt{verification\_output.txt}\). The complete asymptotic claim depends on the analytic Hölder and boundary-tail proof, not on the finite tests.

## Relationship to prior work
Foster, Lyons and Oberhauser (2019 preprint; 2020 journal) study Brownian-path polynomial approximation, including quadratic path integrals conditional on different, non-point observations; their results motivate the target but do not supply the point-design quantile law. Santin (2022 preprint) proves equally spaced nodes optimal for a Brownian-bridge kernel **interpolation power function**, a linear reconstruction criterion not equivalent to Bayes risk for the quadratic functional here. Cui and Chronopoulou (2023) study path-estimation distortion for fractional Brownian motion, rather than the error of its integrated square. A previously identified exact two-reading analysis covers a fixed finite budget, not the sharp all-budget asymptotic constant or the attaining continuum density. The distinction between quadratic energy estimation and standard linear quadrature is essential.

## Limitations
The result is limited to a pinned Gaussian Brownian bridge with exact deterministic point readings and a conditional-mean estimator; it does not address unknown drift, noisy or erased readings, adaptively selected times, non-Gaussian bridges, or exact finite-budget uniqueness. The proof characterizes the sharp limiting risk and provides an attaining design, but does not determine finite-\(n\) optimal nodes. A priority search cannot rule out an equivalent theorem under another terminology; historical priority is provisional until independent review.

## References
- J. Foster, T. Lyons and H. Oberhauser, *An optimal polynomial approximation of Brownian motion*, arXiv:1904.06998, first submitted April 15, 2019. https://arxiv.org/abs/1904.06998
- G. Santin, *Equally spaced points are optimal for Brownian Bridge kernel interpolation*, arXiv:2210.15959, first submitted October 28, 2022. https://arxiv.org/abs/2210.15959
- X. Cui and A. Chronopoulou, *Optimal Sampling for Estimation of Fractional Brownian Motion*, arXiv:2304.07661, first submitted April 16, 2023. https://arxiv.org/abs/2304.07661
