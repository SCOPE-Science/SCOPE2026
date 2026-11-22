# Sharp noise-driven choice between value and derivative sensing in integrated-Wiener quadrature

## Finding

For a once-integrated standard Wiener process, consider estimating its path integral from **one** freely timed Gaussian observation. The observer must choose either the process value or its first derivative, with the same calibrated noise variance \(\eta\geq0\) for either instrument. There is exactly one modality transition, at

\[
\eta_* = 0.126085210302255\ldots.
\]

For \(0\leq\eta<\eta_*\), the unique optimal instrument measures the process **value**; for \(\eta>\eta_*\), the unique optimal instrument measures its **derivative**; at equality, exactly one optimal location exists for each modality. In the switching regime the value sensor is placed at the terminal point \(1\), whereas the derivative sensor is placed at \(y_*=0.521234065743882\ldots\).

Precisely, put

\[
 x_0=\frac{6-\sqrt6}{5},\quad
 y_0=\frac{9-\sqrt{21}}{10},\quad
 L(y)=\frac{y(-5y^2+9y-3)}{6(1-y)^2}.
\]

The optimal derivative location is the unique \(y_\eta\in[y_0,1)\) satisfying \(L(y_\eta)=\eta\). The optimal value location is the unique \(x_\eta\in[x_0,1)\) satisfying

\[
 \eta=\frac{-x_\eta^3(5x_\eta^2-12x_\eta+6)}{24(x_\eta^2-3x_\eta+3)}
\]

when \(0\leq\eta<1/24\), and equals \(1\) otherwise. The switching value is \(\eta_*=L(y_*)\), where \(y_*\) is the unique root in \((y_0,1)\) of

\[
80y^6-416y^5+880y^4-896y^3+432y^2-96y+9=0.
\]

As \(\eta\to\infty\), optimal derivative sensing yields \(16/9\) times the posterior-variance **reduction** of optimal value sensing. This does not mean the total posterior risk has the same ratio.

## Assumptions and scope

Let \(B\) be standard Brownian motion on \([0,1]\), with \(B(0)=0\). Define the zero-start once-integrated process

\[
X(t)=\int_0^t B(s)\,ds=\int_0^t(t-s)\,dB(s),\qquad X'(t)=B(t)
\]

and the numerical-integration target \(J=\int_0^1X(t)\,dt\). Exactly one scalar measurement is available: either \(Y_V=X(x)+\epsilon\) or \(Y_D=X'(y)+\epsilon\), with \(x,y\in[0,1]\) freely selectable and \(\epsilon\sim N(0,\eta)\) independent of \(B\). The same *dimensionless, calibrated* variance \(\eta\) applies across instrument types. For \(\eta=0\), a zero-variance measurement at time zero conveys no information and is assigned zero variance reduction. The estimator is the Gaussian conditional mean; the objective is minimum posterior mean-square error for \(J\), not pathwise reconstruction, arbitrary calibration, or multiple readings.

The result belongs primarily to numerical integration (MSC2020 65D30). All optima are global over the closed timing interval and both instrument choices.

## Proof

**1. Exact posterior variance.** Stochastic Fubini and Itô isometry give

\[
J=\int_0^1\frac{(1-u)^2}{2}\,dB(u),\qquad \operatorname{Var}(J)=\frac1{20}.
\]

For \(t\in[0,1]\), define

\[
 C(t)=\operatorname{Cov}(J,X(t))=\frac{t^2(t^2-4t+6)}{24},\quad
 D(t)=\operatorname{Cov}(J,X'(t))=\frac{t(t^2-3t+3)}6.
\]

As \(\operatorname{Var}X(t)=t^3/3\) and \(\operatorname{Var}X'(t)=t\), the respective decreases in posterior variance are

\[
 F_\eta(t)=\frac{C(t)^2}{t^3/3+\eta},\qquad
 G_\eta(t)=\frac{D(t)^2}{t+\eta}.
\]

Maximizing either decrease is equivalent to minimizing the posterior mean-square risk \(1/20-\max(F_\eta,G_\eta)\).

**2. Value branch.** Direct differentiation (away from the removable zero-time case) yields

\[
 F_\eta'(t)=\frac{t^3(t^2-4t+6)}{192(3\eta+t^3)^2}
 \left[24\eta(t^2-3t+3)+t^3(5t^2-12t+6)\right].
\]

The polynomial \(5t^2-12t+6\) is nonnegative for \(0\leq t\leq x_0\) and negative on \((x_0,1]\). For \(t\geq x_0\), the vanishing derivative defines

\[
 H(t)=\frac{-t^3(5t^2-12t+6)}{24(t^2-3t+3)}.
\]

We claim \(H\) is strictly increasing on \([x_0,1]\). Differentiating,

\[
H'(t)=\frac{-t^2(5t^4-28t^3+63t^2-60t+18)}{8(t^2-3t+3)^2}.
\]

Since \(x_0>7/10\), write \(u=1-t\in[0,3/10]\); the quartic in parentheses becomes \(5u^4+8u^3+9u^2-2u-2<0\). Indeed the first three terms together are bounded by their value \(1.0665\) at \(u=3/10\), whereas \(-2u-2\leq-2\). Hence \(H'(t)>0\); with \(H(x_0)=0\), \(H(1)=1/24\), the value optimum is exactly as stated, including uniqueness at \(\eta=0\) and \(\eta=1/24\).

**3. Derivative branch.** Because \(D(t)>0\) for \(t>0\), the sign of \(G_\eta'(t)\) is the sign of \(2D'(t)(t+\eta)-D(t)\). Its zero is equivalent to \(\eta=L(t)\). For \(t\leq y_0\), the derivative is strictly positive, except at the isolated maximum for \(\eta=0\). For \(t\in(y_0,1)\),

\[
L'(t)=\frac1{3(1-t)^3}-\frac56>0.
\]

Thus \(L\) increases continuously from \(0\) to \(+\infty\) on \([y_0,1)\), giving a unique global derivative optimum \(y_\eta\) for each \(\eta\geq0\). Note \(y_0>1/3\).

**4. Comparison across modalities.** The value design at the endpoint has reduction

\[
F_\eta(1)=\frac{1}{64(\eta+1/3)}.
\]

Define the ratio of the optimal derivative reduction to this endpoint-value reduction,

\[
R(\eta)=\max_{0\leq y\leq1}\frac{64(\eta+1/3)D(y)^2}{\eta+y}.
\]

It is **strictly increasing**: the unique maximizing \(y_\eta\) always exceeds \(1/3\), and for every fixed \(y>1/3\) the ratio's derivative with respect to \(\eta\) equals \(64D(y)^2(y-1/3)/(\eta+y)^2>0\). Comparison at the former maximizer proves strict increase of the maximized ratio.

At \(\eta=1/24\), the root condition places the derivative maximizer strictly between \(47/100\) and \(12/25\): specifically \(L(47/100)=11797/337080<1/24<L(12/25)=42/845\). Since \(D\) is increasing,

\[
G_{1/24}(y_{1/24})
<\frac{D(12/25)^2}{47/100+1/24}
=\frac{120207456}{2998046875}<\frac1{24}=F_{1/24}(1).
\]

Finally, \(R(\eta)\to16/9>1\) as \(\eta\to\infty\), because \(D(1)=1/6\). Continuity and strict increase prove the existence and uniqueness of \(\eta_*>1/24\) with \(R(\eta_*)=1\). For every \(\eta\leq1/24\), the globally optimized value decrease is at least the endpoint decrease, which is strictly better than derivative sensing; for \(\eta\geq1/24\), the endpoint is already globally best among value sites. Consequently the single crossing controls the **entire** two-instrument optimization.

**5. Algebraic description.** At a derivative stationary site \(y\), the optimal derivative reduction simplifies to

\[
G_{L(y)}(y)=\frac{y(y^2-3y+3)(1-y)^2}{6}.
\]

Equating it to \(F_{L(y)}(1)\), cancelling the strictly positive \((1-y)^2\), and expanding gives the displayed sextic. Since \(L\) and \(R\) are strictly increasing in the relevant domains, exactly one of its roots lies in \((y_0,1)\). Numerical root isolation gives \(y_*=0.521234065743882\ldots\) and \(\eta_*=0.126085210302255\ldots\). The tie therefore has precisely two ordered choices: the value measurement at \(x=1\) and the derivative measurement at \(y=y_*\), with no other global optima.

## Verification

The standalone script `verify.py` (dependency specified in `requirements.txt`) checks the three stochastic-integral covariance identities, symbolic derivative and crossing-polynomial identities, an exact rational endpoint-separation certificate, and 32,014 additional finite objective comparisons across eight noise levels. Run `python verify.py` after installing the listed dependency. It is a supplementary computation: the global uniqueness and threshold statements are proved above and do not rely on finite grids.

## Relationship to prior work

Xi, Briol and Girolami (arXiv:1801.04153, 2018) provide general Gaussian-process quadrature posterior-covariance formulas and multi-output integration methodology. Those formulas apply after specifying a kernel, but their stated theorems do not optimize a one-measurement value-versus-derivative choice for the zero-start integrated-Wiener integral. Zhang, Stringer, Brown and Stafford (arXiv:2302.02053, 2023) establish integrated-Wiener process and derivative inference and convergence of overlapping-spline approximations, but not an exact experiment-location/modality switch. The covariance-conditioning identity itself is standard and not claimed as new; the result here is the single sharp mixed-information threshold, all optimal sites and their uniqueness.

## Limitations

The claim assumes the exact zero-start \(\mathrm{IWP}_2\) prior with no additional random polynomial trend and equal calibrated measurement-noise variance in the two modalities. Differing instrument units, costs or noise floors can shift or eliminate the crossing. It does not cover two or more observations, uncertain smoothness, alternative risk criteria, or noisy derivative estimates formed from finite differences. The supporting searches do not establish absolute publication priority; equivalent older optimal-recovery results may remain unindexed.

## References

1. X. Xi, F.-X. Briol and M. Girolami, *Bayesian Quadrature for Multiple Related Integrals*, arXiv:1801.04153, first public 2018-01-12. https://arxiv.org/html/1801.04153v7
2. Z. Zhang, A. Stringer, P. Brown and J. Stafford, *Model-based Smoothing with Integrated Wiener Processes and Overlapping Splines*, arXiv:2302.02053, first public 2023-02-04. https://arxiv.org/abs/2302.02053
