# Stationary-moment identification of the cubic sign in reflected noisy pitchforks

## Finding
Let a scalar additive-noise pitchfork with linear drift coefficient \(\mu\), cubic coefficient \(s\), noise variance rate \(D>0\), and reflecting boundaries \(\pm L\) with \(L>0\) be in its stationary regime. The stationary second and fourth moments alone determine whether \(s<0\), \(s=0\), or \(s>0\), even when \(\mu\) and \(D\) are unknown. The second moment alone never determines that sign. Moreover, four even moments through degree eight give an **exact rational reconstruction** of both \(\mu/D\) and \(s/D\), without estimating the stationary density or its values at the reflecting boundaries.

For the second/fourth-moment test, define \(\alpha_0(u)\), for \(0<u<L^2\), as the unique real number satisfying
\[
 u=\frac{\int_{-L}^{L}x^2\exp(\alpha_0(u)x^2)\,dx}{\int_{-L}^{L}\exp(\alpha_0(u)x^2)\,dx},
\]
and set
\[
 H_L(u)=\frac{\int_{-L}^{L}x^4\exp(\alpha_0(u)x^2)\,dx}{\int_{-L}^{L}\exp(\alpha_0(u)x^2)\,dx}.
\]
Writing \(m_{2j}=\mathbb E[X^{2j}]\) in stationarity, the exact trichotomy is
\[
 \operatorname{sgn}(s)=\operatorname{sgn}\bigl(m_4-H_L(m_2)\bigr).
\]
Thus the cubic-sign boundary is a precisely specified curve in the stationary variance/fourth-moment plane, not a fixed universal kurtosis cutoff.

For an explicit formula requiring no numerical inversion, put
\[
 A=L^2m_2-m_4,\quad B=L^2m_4-m_6,\quad C=L^2m_6-m_8,
\]
\[
 Q=\frac{3m_2-L^2}{2},\qquad R=\frac{5m_4-3L^2m_2}{2},\qquad \Delta=AC-B^2.
\]
Then \(\Delta>0\) and
\[
 \boxed{\frac{\mu}{D}=\frac{CQ-BR}{\Delta},\qquad \frac{s}{D}=\frac{AR-BQ}{\Delta}.}
\]
In particular, \(\operatorname{sgn}(s)=\operatorname{sgn}(AR-BQ)\). All claims hold for every real \(\mu,s\), every \(D,L>0\), and exact stationary moments.

## Assumptions and scope
Consider the one-dimensional reflected diffusion on the *known* closed interval \([-L,L]\):
\[
 dX_t=(\mu X_t+sX_t^3)\,dt+\sqrt D\,dW_t+dK_t^--dK_t^+,
\]
where \(K^-\) and \(K^+\) are continuous nondecreasing regulators carried respectively by \(X=-L\) and \(X=L\). The diffusion has normal instantaneous reflection, constant noise variance rate \(D>0\), and no other drift terms. The parameters are fixed in time. Its uniformly elliptic generator in the interior is \(\mathcal Lf=(\mu x+sx^3)f'+(D/2)f''\) with Neumann boundary conditions.

On a compact interval, smooth drift and nondegenerate additive noise give a unique positive stationary density and ergodicity. The sign of the cubic drift coefficient is the supercritical/subcritical normal-form discriminator for the underlying *interior deterministic* pitchfork, when this coefficient is nonzero. The reflected diffusion need not share the global escaping behavior of the unconstrained system. The theorem concerns exact stationary laws; it does not require access to time derivatives, the regulator processes, or the magnitude of \(D\).

## Proof
**Stationary density.** The stationary Fokker–Planck current is \(J(x)=(\mu x+sx^3)p(x)-(D/2)p'(x)\). Reflection makes the current zero at each endpoint, hence throughout the interval. Therefore
\[
 p_{\mu,s,D,L}(x)=Z^{-1}\exp\!\left(\frac{\mu x^2+(s/2)x^4}{D}\right),\qquad -L\le x\le L.
\]
This density is strictly positive and continuous on the whole interval, including its interior. It also directly satisfies the no-flux boundary conditions.

**Sharp two-moment sign test.** Write \(\alpha=\mu/D\), \(\beta=s/(2D)\), and \(Y=X^2\). For the two-parameter exponential family proportional to \(\exp(\alpha x^2+\beta x^4)\), let \(M_1(\alpha,\beta)=\mathbb E[Y]\) and \(M_2(\alpha,\beta)=\mathbb E[Y^2]\). All derivatives are legitimate because the domain is compact. For fixed finite \(\beta\),
\[
 \frac{\partial M_1}{\partial\alpha}=\operatorname{Var}(Y)>0.
\]
As \(\alpha\to-\infty\), mass concentrates near zero and \(M_1\to0\); as \(\alpha\to+\infty\), it concentrates near the two endpoints and \(M_1\to L^2\). Consequently, for any \(u\in(0,L^2)\) and any real \(\beta\), there is a unique \(\alpha=\alpha(\beta;u)\) making \(M_1=u\). Differentiating this equality yields
\[
 \alpha'(\beta;u)=-\frac{\operatorname{Cov}(Y,Y^2)}{\operatorname{Var}(Y)}.
\]
Along that fixed-variance curve,
\[
 \frac{d}{d\beta}M_2(\alpha(\beta;u),\beta)
 =\operatorname{Var}(Y^2)-\frac{\operatorname{Cov}(Y,Y^2)^2}{\operatorname{Var}(Y)}>0.
\]
Strictness follows because \(Y^2\) is not an affine function of \(Y\) on any interval and the law of \(Y\) has a positive density on \((0,L^2)\). At \(\beta=0\) the second raw moment of \(Y\) is exactly \(H_L(u)\). Thus \(M_2-H_L(M_1)\) has exactly the sign of \(\beta\), hence of \(s\). Since \(\alpha(\beta;u)\) exists for all \(\beta\), models with \(s<0\), \(s=0\), and \(s>0\) can have *exactly the same* \(m_2=u\). This proves both the sign trichotomy and the inadequacy of variance alone.

**Algebraic reconstruction without boundary data.** From the stationary density,
\[
 p'(x)=\frac2D(\mu x+sx^3)p(x).
\]
For integers \(k=0,1\), integrate the derivative of \(x^{2k+1}(L^2-x^2)p(x)\) on \([-L,L]\). Its boundary term vanishes at both ends by construction. Expanding gives
\[
 2\frac{\mu}{D}(L^2m_{2k+2}-m_{2k+4})
 +2\frac{s}{D}(L^2m_{2k+4}-m_{2k+6})
 =(2k+3)m_{2k+2}-(2k+1)L^2m_{2k},
\]
with \(m_0=1\). The two instances are precisely
\[
 A(\mu/D)+B(s/D)=Q,\qquad B(\mu/D)+C(s/D)=R.
\]
Let \(w(x)=x^2(L^2-x^2)\). Then
\[
 A=\mathbb E[w(X)],\quad B=\mathbb E[w(X)X^2],\quad
 C=\mathbb E[w(X)X^4].
\]
Because \(w>0\) in the interior except at \(x=0\) and the stationary density is positive there, strict Cauchy–Schwarz under the positive measure \(w(x)p(x)\,dx\) yields \(AC>B^2\). The displayed rational reconstruction follows by solving this invertible two-by-two system. No unknown boundary density, reflection local time, or diffusion-scale estimate enters.

## Verification
Run `python verify.py` after installing the dependency in `requirements.txt`. The checker evaluates the stationary density by high-precision quadrature in eight parameter regimes (positive, negative, and zero cubic coefficient; multiple noise scales and interval widths), tests the two exact rational formulas, and tests the sign comparison against the uniquely fitted zero-cubic reference. It also constructs three distinct parameter pairs with equal stationary variance and cubic coefficients of opposite or zero sign. The checker returned `PASS 26 numerical checks; 8 parameter cases and same-variance sign separation`. These finite numerical cases are reproducibility diagnostics, not substitutes for the universal proof above.

## Relationship to prior work
Sanders, Kuehn, Hilder and Bastiaansen (2026) propose temporal-derivative regression to identify the cubic normal-form sign from noisy pre-transition trajectories. The present result concerns a *different observation regime*: an equilibrated diffusion with known hard reflecting boundaries, where the **stationary state distribution**, rather than temporal increments, determines that sign exactly. It does not assert the present method applies to the unconfined and potentially escaping subcritical process in their paper.

Miyazawa (first available 2024) establishes stationary densities for general one- and two-sided reflected diffusions. The density used here is a standard specialization of the known zero-current formula; that density itself is **not claimed as new**. Pavliotis and Zanoni (first available 2022) establish moment-based parameter inference for polynomial interacting diffusions on an unbounded state space; their method and the general principle of exponential-family identifiability are likewise prior art. The asserted addition is the *reflected pitchfork-specific* sharp two-moment sign boundary, the impossibility result for variance alone, and the explicit **boundary-annihilating** eighth-moment formula for both coefficients when the reflection local times and the noise magnitude are unobserved. Hu and coauthors (2015) and Hu–Xi (2021) previously developed moment inference for reflected linear Ornstein–Uhlenbeck dynamics, a different drift family. These are mathematical distinctions, not a claim of exhaustive historical priority.

## Limitations
The statements require the full stationary law of the prescribed reflected additive-noise cubic model, known endpoints, and positive constant noise variance. A killed diffusion, absorbing boundary, conditional quasi-stationary law, unknown boundary location, nonpolynomial drift, or time-dependent forcing is not covered. Only the ratios \(\mu/D\) and \(s/D\) can be recovered from the stationary distribution if the noise time scale is unknown; multiplying all three coefficients by the same positive constant preserves that distribution. Near \(s=0\), sign classification from noisy empirical moments can be ill-conditioned; \(\Delta\) can become small when the stationary mass concentrates, and no finite-sample error guarantees are asserted. General exponential-family theory already implies the basic two-sufficient-statistics identifiability principle. Independent literature priority review remains appropriate for the specific sign and rational-formula statements.

## References
1. P. A. Sanders, C. Kuehn, B. Hilder, R. Bastiaansen, *Early warning of critical transitions: Distinguishing supercritical and subcritical bifurcations from noisy observations*, arXiv:2610.38866v1 (first submitted October 28, 2026), https://arxiv.org/html/2610.38866v1 .
2. M. Miyazawa, *The stationary distributions of state-dependent diffusions reflected at one and two sides*, arXiv:2410.11496 (first submitted October 15, 2024), https://arxiv.org/abs/2410.11496 .
3. G. A. Pavliotis and A. Zanoni, *A method of moments estimator for interacting particle systems and their mean field limit*, arXiv:2212.00403 (first submitted December 1, 2022), https://arxiv.org/html/2212.00403v2 .
4. Y. Hu, C. Lee, M. Lee, J. Song, *Parameter estimation for reflected Ornstein–Uhlenbeck processes with discrete observations*, Statistical Inference for Stochastic Processes 18 (2015), 279–291, https://doi.org/10.1007/s11203-014-9112-7 (bibliographic comparison only; full text not verified).
5. Y. Hu and Y. Xi, *Estimation of all parameters in the reflected Ornstein–Uhlenbeck process from discrete observations*, Statistics & Probability Letters 174 (2021), 109099, https://doi.org/10.1016/j.spl.2021.109099 (bibliographic comparison only; full text not verified).
