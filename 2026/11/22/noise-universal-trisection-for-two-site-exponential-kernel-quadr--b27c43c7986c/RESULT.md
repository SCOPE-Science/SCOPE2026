# Noise-universal trisection for two-site exponential-kernel quadrature

## Finding
Let \(X\) be a centered Gaussian process on \([0,1]\) with stationary exponential covariance \(K_\lambda(u,v)=\exp(-\lambda|u-v|)\), where \(\lambda>0\). Two independently corrupted observations are \(Y_j=X(t_j)+\varepsilon_j\), with \(\varepsilon_j\sim N(0,\eta)\) independent of each other and of \(X\), where \(\eta>0\). The target is \(J=\int_0^1X(t)\,dt\). Both sites \(t_1,t_2\in[0,1]\) are freely chosen and may coincide.

The **unique unordered pair minimizing the posterior variance of \(J\)** is
\[
\{t_1,t_2\}=\left\{\frac12-\frac{s_{\lambda,\eta}}{\lambda},\ \frac12+\frac{s_{\lambda,\eta}}{\lambda}\right\},
\]
where \(s_{\lambda,\eta}\) is the unique solution in \((0,\lambda/2)\) to
\[
\exp(\lambda/2)=\exp(s)+(1+\eta)\exp(2s)\sinh(s).
\]
The two optimal sites are distinct for every finite \(\eta>0\). The optimal Bayesian linear quadrature weights are equal, both being
\[
w_{\lambda,\eta}=\frac{2[1-e^{-\lambda/2}\cosh(s_{\lambda,\eta})]}{\lambda[1+\eta+e^{-2s_{\lambda,\eta}}]}.
\]
The minimum posterior variance is exactly
\[
V^*_{\lambda,\eta}=
\frac{2(\lambda-1+e^{-\lambda})}{\lambda^2}
-\frac{8[1-e^{-\lambda/2}\cosh(s_{\lambda,\eta})]^2}{\lambda^2[1+\eta+e^{-2s_{\lambda,\eta}}]}.
\]

**Noise-universal trisection:** when the observation-noise variance equals the marginal process variance, \(\eta=1\), the unique optimal sites are \(1/3\) and \(2/3\) for **every \(\lambda>0\)**. In this case each optimal weight is \((1-e^{-\lambda/3})/\lambda\), and
\[
V^*_{\lambda,1}=\frac{2[\lambda-3+3e^{-\lambda/3}]}{\lambda^2}.
\]
More generally the left site is less than, equal to, or greater than \(1/3\) exactly as \(\eta<1\), \(\eta=1\), or \(\eta>1\), respectively. At fixed \(\lambda>0\), increasing \(\eta\) strictly moves both sites toward the midpoint; they do not coincide at any finite noise level.

## Assumptions and scope
The kernel is normalized to unit pointwise variance. Observation errors are independent Gaussian noises with the same known *positive* variance, and a zero process mean is known. The criterion is the exact Gaussian posterior variance of the integral, optimized over every ordered pair of sampling sites, including endpoints and repetitions; equivalently one minimizes Bayes mean-square loss of the posterior-mean estimator. This does not assert an unrestricted minimax deterministic integration rule or optimality for three or more observations. All statements hold for every real \(\lambda>0\), \(\eta>0\), without an asymptotic hypothesis.

## Proof
**1. Exact information objective.** Write \(a=1+\eta\), \(r=\exp(-\lambda|t_2-t_1|)\), and
\[
m(t)=\operatorname{Cov}(J,X(t))=\frac{2-e^{-\lambda t}-e^{-\lambda(1-t)}}{\lambda},\qquad
Q=\operatorname{Var}(J)=\frac{2(\lambda-1+e^{-\lambda})}{\lambda^2}.
\]
The observation covariance matrix is \(\begin{pmatrix}a&r\\r&a\end{pmatrix}\), which is strictly positive definite even if the sites coincide, since \(a>1\). Gaussian conditioning yields \(V=Q-H\) with captured variance
\[
H(t_1,t_2)=\frac{[m(t_1)+m(t_2)]^2}{2(a+r)}+\frac{[m(t_1)-m(t_2)]^2}{2(a-r)}.
\]

**2. Global reflection centering for a fixed site separation.** Order the sites as \(c-d\le c+d\), with \(0\le d\le 1/2\) and \(d\le c\le1-d\). Put \(s=\lambda d\), \(L=\lambda/2\), \(q=e^{-L}\), \(R=e^{-2s}\), and \(C=\cosh(\lambda(c-1/2))\). Then \(1\le C\le\cosh(L-s)\) and a direct substitution gives
\[
H=\frac8{\lambda^2}\left\{\frac{(1-q\cosh(s)C)^2}{a+R}+\frac{q^2\sinh^2(s)(C^2-1)}{a-R}\right\}.
\]
For \(0<s<L\), subtracting the midpoint-centered value \(H(C=1)\), the sign of the difference for \(C>1\) is the sign of
\[
-2\cosh(s)+q(C+1)\left[\cosh^2(s)+\frac{a+R}{a-R}\sinh^2(s)\right].
\]
Because \(a>1\), one has \((a+R)/(a-R)<(1+R)/(1-R)=\coth(s)\), so the bracket in square brackets is strictly below \(\cosh(s)e^s\). Also, since \(C\le\cosh(L-s)\),
\[
q e^s(C+1)\le e^{-(L-s)}[1+\cosh(L-s)]=\tfrac12(1+e^{-(L-s)})^2<2.
\]
Consequently \(H(C)<H(1)\) for every noncentral placement at the same separation. For \(s=0\), the coincident-site objective \(2m(c)^2/(2+\eta)\) is maximized uniquely at \(c=1/2\), since \(m\) increases to the midpoint and then decreases. For \(s=L\), the only permissible center is \(c=1/2\). Hence every global optimum is midpoint-reflected, and the centering is unique at each separation.

**3. Unique optimal separation.** For midpoint-reflected sites, the objective reduces to
\[
H_\mathrm{sym}(s)=\frac8{\lambda^2}\frac{(1-e^{-L}\cosh s)^2}{a+e^{-2s}},\qquad 0\le s\le L.
\]
The numerator factor is positive on this interval. The logarithmic derivative has the sign of
\[
G(s)=e^L-e^s-ae^{2s}\sinh(s).
\]
The function \(G\) is strictly decreasing, \(G(0)=e^L-1>0\), and \(G(L)<0\). It has a unique zero \(s_{\lambda,\eta}\in(0,L)\), and \(H_\mathrm{sym}\) increases strictly before and decreases strictly after this zero. The formulas for the unique global optimizer, equal conditional-mean weights and minimum variance follow.

**4. Universality and strict threshold.** Setting \(a=2\) makes \(s=L/3\) an exact zero, since \(e^{L/3}+2e^{2L/3}\sinh(L/3)=e^L\). Strict monotonicity of \(G\) shows \(s>L/3\) when \(a<2\) and \(s<L/3\) when \(a>2\). Substitution into the weight and posterior-variance formulas at \(s=L/3\) gives the stated cancellations. Implicit differentiation of the scalar equation gives \(\partial s/\partial a<0\), proving the strict noise-dependent movement.

## Verification
The accompanying standalone \(\texttt{verify.py}\) numerically checks the full Gaussian conditional-covariance formula against the reduced formula, optimizers against 4,200 random unrestricted pairs, reflection centering against 3,000 translated pairs, 6,012 symmetric-grid comparisons, exact trisection at \(\eta=1\) across several decay rates, and two asymptotic limits. It passed on execution. These computations are independent diagnostics, not a substitute for the analytic proof.

Two useful limiting laws, obtained by expanding the unique scalar root, are
\[
s_{\lambda,\eta}\sim\frac{e^{\lambda/2}-1}{\eta+2}\quad(\eta\to\infty\text{ at fixed }\lambda),\qquad
\lim_{\lambda\downarrow0}t_1^*=\frac{1+\eta}{2(2+\eta)}.
\]
At fixed \(\eta>0\), \(t_1^*\to1/3\) as \(\lambda\to\infty\). At finite \(\eta\) the two sites remain distinct. The exact formulas should be evaluated with numerically stable exponential-difference functions for extremely small \(\lambda\).

## Relationship to prior work
The posterior-variance and kernel-quadrature representation and general conditions for positive weights are established in Karvonen, Kanagawa and Särkkä (2018, subsequently published 2019). General noisy Matérn kernel-quadrature error rates were analyzed by Cai, Lam and Scarlett (2022), but those rates do not select the exact best pair of sites. Earlier work by Mukherjee (2003) considered exactly optimal integral-observation designs for product covariance processes, including Ornstein–Uhlenbeck processes, principally in the exact-observation context; the full text was not obtainable here, so an equivalent error-in-observations result remains a priority risk. A separately published result characterizes noiseless exponential-kernel optimal designs for arbitrary site count; its zero-nugget statement does not imply the positive-nugget trisection identity. The new claim is explicitly the fully optimized *two-site, positive-noise* law and its decay-independent threshold, not the Gaussian conditioning identity or the noiseless case.

## Limitations
The theorem applies to stationary exponential covariance, uniform integration on one interval, two equal-quality independent noisy point observations and a known mean; it does not generalize here to unequal noise variances, other kernels, arbitrary numbers of nodes, non-Gaussian data or adaptive sampling. No algorithmic speed claim is made. The primary mathematical argument was checked within this work only; an independent mathematical audit and broader publication-priority review have not been performed. The inaccessible 2003 original creates a residual historical overlap risk.

## References
- T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, first public arXiv version 2018-12-20, https://arxiv.org/abs/1812.08509 ; open-access full article https://doi.org/10.1007/s11222-019-09901-0 .
- X. Cai, C. T. Lam and J. Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, first public arXiv version 2022-02-22, https://arxiv.org/abs/2202.10615 .
- B. Mukherjee, *On Sampling Designs for Integral Estimation of a Random Process*, *Communications in Statistics: Theory and Methods* 32 (2003), DOI https://doi.org/10.1081/STA-120022249 ; original full text not accessible in this review.
- *Exact optimal nodes and stratification penalty for Ornstein–Uhlenbeck Bayesian quadrature*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-optimal-nodes-and-stratification-penalty-for-ornstein-uhle--971795799fba ; record summary was accessible, but full text could not be inspected.
