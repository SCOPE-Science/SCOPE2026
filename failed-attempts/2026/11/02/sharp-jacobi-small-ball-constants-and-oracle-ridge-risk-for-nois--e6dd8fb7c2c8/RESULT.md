# Sharp Jacobi small-ball constants and oracle-ridge risk for noisy affine fitting

## Finding
Let \(m\ge4\) be an integer, \(\alpha,\beta>0\), and let \(X_1,\ldots,X_m\) be independent \(\operatorname{Beta}(\alpha,\beta)\) variables on \([0,1]\). Define \(\bar X=m^{-1}\sum_iX_i\) and \(S=\sum_i(X_i-\bar X)^2\). Put
\[
q=\frac{m-1}{2},\qquad h=\frac m2\min\{\alpha,\beta\},\qquad \delta=\min\{q,h\},\qquad v_d=\frac{\pi^{d/2}}{\Gamma(1+d/2)}.
\]
Write \(B=B(\alpha,\beta)\) for the beta function and, for \(0<a<(m-1)/m\), define the finite strictly positive constant
\[
J_m(a)=\int_{\substack{z_i\ge0\\\sum_i(z_i-\bar z)^2\le1}}\prod_{i=1}^m z_i^{a-1}\,dz_1\cdots dz_m.
\]
As \(s\downarrow0\), the exact first-order lower-tail law is
\[
\Pr(S\le s)\sim
\begin{cases}
K_{\rm end}s^h,&h<q,\\
K_{\rm crit}s^q\log(1/s),&h=q,\\
K_{\rm int}s^q,&h>q,
\end{cases}
\]
with strictly positive constants
\[
\begin{aligned}
K_{\rm end}&=B^{-m}\sum_{a\in(\alpha,\beta):\,ma/2=h}J_m(a),\\
K_{\rm crit}&=\frac{\sqrt m\,v_{m-1}}{2B^m}\#\{a\in(\alpha,\beta):\,ma/2=q\},\\
K_{\rm int}&=\frac{\sqrt m\,v_{m-1}}{B^m} B(m\alpha-m+1,m\beta-m+1).
\end{aligned}
\]
The parenthesized pair \((\alpha,\beta)\) is counted *with multiplicity*, so equal endpoint parameters give two contributions. Only the constant applicable to the indicated regime is used. The exact inverse-moment boundary is \(\mathbb E[S^{-p}]<\infty\) if and only if \(0<p<\delta\); in particular equality diverges.

Now observe \(Y_i=a+bX_i+\varepsilon_i\), where \(a\in\mathbb R\), \(b\ne0\), and the independent errors have mean zero and common variance \(\sigma^2>0\), independently of the sites. Fit an unpenalized intercept and penalize only the slope by \(\lambda\ge0\):
\[
\widehat b_\lambda=\frac{\sum_i(X_i-\bar X)(Y_i-\bar Y)}{S+\lambda}.
\]
Its unconditional slope mean-squared error is uniquely minimized, over all deterministic \(\lambda\ge0\), by \(\lambda_*=\sigma^2/b^2\), and the minimum is exactly
\[
R_*(\sigma)=\sigma^2\mathbb E\left[\frac1{S+\sigma^2/b^2}\right].
\]
For fixed \(m,\alpha,\beta,b\) and \(\sigma\downarrow0\), set \(K=K_{\rm end}\) when \(h<q\). Then
\[
R_*(\sigma)\sim
\begin{cases}
K\Gamma(1+\delta)\Gamma(1-\delta)|b|^{2(1-\delta)}\sigma^{2\delta},&\delta<1,\\
K\sigma^2\log(b^2/\sigma^2),&\delta=1,\\
\sigma^2\mathbb E[S^{-1}],&\delta>1.
\end{cases}
\]
Since \(m\ge4\), all \(\delta\le1\) regimes are endpoint-dominated and do not carry an extra geometric logarithm. A concrete consequence is that four uniform samples yield a finite OLS slope MSE and a \(\sigma^2\)-order optimally regularized risk, whereas four arcsine samples \((\alpha=\beta=1/2)\) give infinite OLS slope MSE but finite optimally regularized risk with the sharp logarithmic equivalent
\[
R_*(\sigma)\sim\frac{2J_4(1/2)}{\pi^4}\sigma^2\log(b^2/\sigma^2).
\]
In contrast, five arcsine samples restore a finite OLS slope MSE.

## Assumptions and scope
The statements concern any fixed integer \(m\ge4\), all real \(\alpha,\beta>0\), and independent beta-distributed sites, with \(S\) the *uncorrected* centered sum of squares, not the sample variance divided by \(m-1\). The regression has one slope and one freely fitted intercept. Noise requires only independent centered finite-variance errors independent of the sites; Gaussianity is not used. The optimum \(\lambda_*\) is an oracle choice depending on the unknown nonzero slope, and is not claimed to be implementable without estimating it. Asymptotics are at fixed \(m,\alpha,\beta,b\), not in growing dimension or simultaneous sample-size limits.

## Proof
**1. Shrinking tube around coincident sites.** Let \({\bf1}=(1,\dots,1)\), write \(x=t{\bf1}+y\), with \(t=\bar x\) and \(y\cdot{\bf1}=0\). In the Euclidean volume on the \((m-1)\)-dimensional orthogonal complement, the Jacobian is \(\sqrt m\), while \(S(x)=\|y\|^2\). Thus
\[
\Pr(S\le s)=\frac{\sqrt m}{B^m}\int_{\|y\|\le\sqrt s}\int_{\substack{0<t+y_i<1\\\text{for every }i}}\prod_i(t+y_i)^{\alpha-1}(1-t-y_i)^{\beta-1}\,dt\,dy.
\]
For \(t\) bounded away from both endpoints, put \(y=\sqrt s\,u\). The transverse volume is \(v_{m-1}s^q\) and the limiting integrand is \(t^{m(\alpha-1)}(1-t)^{m(\beta-1)}\). If \(h>q\), both exponents are greater than \(-1\); splitting at \(t=2\sqrt s\) and \(1-t=2\sqrt s\), and bounding the endpoint layers by \(O(s^{m\alpha/2})\) and \(O(s^{m\beta/2})\), gives dominated convergence. Integrating over \(t\) gives \(K_{\rm int}\).

**2. Endpoint-dominated phase.** Suppose \(h<q\), and consider the left endpoint when \(m\alpha/2=h\). In the fixed endpoint neighborhood \(x_i\le\eta<1\), substitute \(x_i=\sqrt s\,z_i\). The event becomes \(S(z)\le1\), the density and Jacobian contribute \(s^{m\alpha/2}B^{-m}\prod z_i^{\alpha-1}\), and the remaining factors tend to one. The integral \(J_m(\alpha)\) converges: in mean/transverse coordinates \(z=t{\bf1}+y\), \(\|y\|\le1\), its large-\(t\) integrand is comparable to \(t^{m(\alpha-1)}\), integrable exactly when \(m\alpha<m-1\); in bounded regions, coordinate singularities are integrable because \(\alpha>0\). Dominated convergence is valid on the expanding rescaled endpoint region. The right endpoint is identical with \(\beta\) in place of \(\alpha\). Regions away from both endpoint diagonals contribute \(O(s^q)=o(s^h)\), and endpoints with larger exponent are lower order. The sum gives \(K_{\rm end}\).

**3. Critical phase.** At \(m\alpha/2=q\), the tube's interior section near the left endpoint is \(\sqrt m\,v_{m-1}s^q B^{-m}t^{-1}(1+o(1))\,dt\) uniformly on \(M\sqrt s<t<\eta\) after first choosing large fixed \(M\), then small fixed \(\eta\). This interval contributes \(\tfrac12\sqrt m\,v_{m-1}B^{-m}s^q\log(1/s)\) to leading order. The portion \(t=O(\sqrt s)\) is \(O(s^q)\) by endpoint scaling over bounded rescaled domains, and the part \(t\ge\eta\) is also \(O(s^q)\). Taking \(M\to\infty\) and \(\eta\downarrow0\) after the leading limit determines the coefficient. Add one identical contribution if the right endpoint is critical. A noncritical endpoint is lower order. This proves \(K_{\rm crit}\).

**4. Moment frontier.** For every \(p>0\), integration by parts gives \(\mathbb E[S^{-p}]=p\int_0^\infty s^{-p-1}\Pr(S\le s)\,ds\) (with the integral effectively restricted to the bounded support, plus its harmless positive upper tail). Inserting the three positive tail equivalents shows finiteness exactly for \(p<\delta\). At \(p=\delta\) the integral diverges, with an extra logarithm in the critical case.

**5. Exact ridge risk and its unique optimum.** Conditional on the sites,
\[
\widehat b_\lambda-b=-\frac{b\lambda}{S+\lambda}+\frac{\sum_i(X_i-\bar X)\varepsilon_i}{S+\lambda},
\]
so \(R(\lambda)=\mathbb E[(b^2\lambda^2+\sigma^2S)/(S+\lambda)^2]\). For every \(\lambda>0\), differentiation under the bounded expectation yields
\[
R'(\lambda)=2(b^2\lambda-\sigma^2)\mathbb E\!\left[\frac{S}{(S+\lambda)^3}\right].
\]
The expectation is strictly positive, so the sole global minimum is \(\lambda_*\). Substitution reduces the integrand to \(\sigma^2/(S+\lambda_*)\).

**6. Sharp small-noise phases.** Write \(F(s)=\Pr(S\le s)\). Integration by parts gives \(\mathbb E[(S+\lambda)^{-1}]=\int_0^\infty F(s)(s+\lambda)^{-2}\,ds\). For \(0<\delta<1\), the endpoint tail has \(F(s)\sim Ks^\delta\); set \(s=\lambda u\), dominate the tail using the two-sided asymptotic bounds, and evaluate \(\int_0^\infty u^\delta/(1+u)^2\,du=\Gamma(1+\delta)\Gamma(1-\delta)\). At \(\delta=1\) the same integral truncated at order \(1/\lambda\) grows like \(\log(1/\lambda)\). At \(\delta>1\), the moment frontier makes \(S^{-1}\) integrable, so monotone convergence applies. Substitute \(\lambda=\sigma^2/b^2\) throughout.

## Verification
A standalone Python verifier is provided as `verify.py`. It checks exact rational identities for the ridge risk and derivative, exact homogeneity of the endpoint scaling, a known two-sample uniform calibration of the tube constant, the explicit four-sample uniform coefficient \(8\pi/3\), and independently coded finite-sample random-design diagnostics. These checks corroborate, but do not replace, the analytic limits above. The value \(J_4(1/2)\) is specified by a convergent integral; numerical quadrature is not treated as proof of its value.

## Relationship to prior work
Xu and Zhang (arXiv:2407.10221, first public July 14, 2024) analyze random Jacobi sampling stability for polynomial least squares at increasing degrees and high-probability sample-rate scales, not the fixed-degree lower-tail constants above. Migliorati, Nobile and Tempone (2015) analyze noisy discrete least squares including beta sampling and convergence bounds, without the all-sample-count small-ball coefficient and small-noise oracle-ridge equivalents here. Mourtada (arXiv:1912.10754) studies broad nonasymptotic lower-tail and excess-risk results, but its stated results do not specialize to this exact beta endpoint/interior coefficient phase diagram. Previously established beta-design slope moment frontiers, universal continuous-density affine design tube constants and a three-sample beta-variance tail classification supply relevant ingredients and partial special cases: the present result adds the explicit constants for *every* \(m\ge4\), including singular endpoint densities and critical logarithms, linked to the exact regularized noise risk. These comparisons do not establish absolute publication priority against all literature.

## Limitations
The theorem does not claim the first discovery of the slope moment threshold, least-squares normal equations, the elementary oracle tuning identity, or the three-sample beta case. It does not concern arbitrary multivariate polynomial degrees, normalized sample variance without rescaling, data-driven ridge parameter estimation, heteroskedastic errors, or other endpoint densities. A full specialist priority audit may reveal an equivalent small-ball coefficient theorem under a different terminology.

## References
1. Z. Xu and X. Zhang, *Stability of Least Square Approximation under Random Sampling*, arXiv:2407.10221 (first posted 2024-07-14), https://arxiv.org/abs/2407.10221.
2. G. Migliorati, F. Nobile, and R. Tempone, *Convergence estimates in probability and in expectation for discrete least squares with noisy evaluations at random points*, Journal of Multivariate Analysis 142 (2015), 167–182, https://doi.org/10.1016/j.jmva.2015.08.009.
3. J. Mourtada, *Exact minimax risk for linear least squares, and the lower tail of sample covariance matrices*, arXiv:1912.10754 (first posted 2019-12-23), https://arxiv.org/abs/1912.10754.
