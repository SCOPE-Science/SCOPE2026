# A sharp correlation boundary layer for minimax two-query numerical differentiation

## Finding

Let \(M,\sigma,\ell>0\) and \(0\leq\rho\leq1\). An unknown real function \(f\in C^3(\mathbb R)\) satisfies \(\sup_{x\in\mathbb R}|f'''(x)|\leq M\). At two distinct, nonadaptively selected arguments \(a,b\), observe \(Y(a)=f(a)+\varepsilon_a\) and \(Y(b)=f(b)+\varepsilon_b\), where the errors are centered jointly Gaussian and
\[
\operatorname{Var}(\varepsilon_a)=\operatorname{Var}(\varepsilon_b)=\sigma^2,\qquad
\operatorname{Cov}(\varepsilon_a,\varepsilon_b)=\rho\sigma^2e^{-|a-b|/\ell}.
\]
Among **all predetermined two-query linear estimators** of \(f'(0)\), with freely selected query locations and coefficients, the unique finite-risk minimax design, up to query interchange, is the symmetric central difference at \(\pm h_*\). Writing
\[
\kappa=\frac{9\sigma^2}{M^2\ell^6},\qquad x_*=h_*/\ell,
\]
its spacing is the unique positive solution of
\[
\boxed{\;x_*^6=\kappa\bigl[1-\rho(1+x_*)e^{-2x_*}\bigr].\;}
\]
For every fixed \(\kappa>0\), both \(h_*\) and the optimal mean-square risk decrease strictly as \(\rho\) increases. The minimum risk is
\[
\boxed{\;R_*=\frac{M^2h_*^4}{36}+\frac{\sigma^2(1-\rho e^{-2h_*/\ell})}{2h_*^2}.\;}
\]

There is a singular transition when the independent-error nugget vanishes. As \(\kappa\downarrow0\), for each *fixed* \(\rho<1\),
\[
\frac{h_*}{\ell}\sim[\kappa(1-\rho)]^{1/6},\qquad
R_*\sim\frac{M^2\ell^4}{12}[\kappa(1-\rho)]^{2/3},
\]
whereas at \(\rho=1\),
\[
\frac{h_*}{\ell}\sim\kappa^{1/5},\qquad
R_*\sim\frac{5M^2\ell^4}{36}\kappa^{4/5}.
\]
More sharply, if \(\kappa\downarrow0\) and \((1-\rho)/\kappa^{1/5}\to\alpha\in[0,\infty)\), then
\[
\frac{h_*}{\ell\kappa^{1/5}}\longrightarrow z_\alpha,
\quad z_\alpha^6=z_\alpha+\alpha,\quad z_\alpha\ge1,
\]
with a unique solution \(z_\alpha\) in \([1,\infty)\), and
\[
\frac{R_*}{M^2\ell^4\kappa^{4/5}}
\longrightarrow\frac{z_\alpha^4}{36}+\frac{\alpha+2z_\alpha}{18z_\alpha^2}.
\]
The crossover scale is therefore exactly \(1-\rho\asymp\kappa^{1/5}\), not a fixed correlation threshold.

## Assumptions and scope

The estimators have the form \(T=w_1Y(a)+w_2Y(b)\) with deterministic real \(a,b,w_1,w_2\), \(a\ne b\). The locations, coefficients and noise parameters are chosen without seeing the observations; the risk is \(\sup_{\|f'''\|_\infty\le M}\mathbb E_f[(T-f'(0))^2]\). No bound is imposed on the lower-order polynomial coefficients of \(f\). The error covariance describes, for example, an Ornstein–Uhlenbeck correlated component of fraction \(\rho\), plus independent per-query error of fraction \(1-\rho\). Only the covariance is needed for the mean-square theorem; Gaussianity specifies a concrete valid observation model. The query domain is all of \(\mathbb R\). Both \(M>0\) and \(\sigma>0\) are essential for a strictly positive finite optimal separation.

This is minimax optimality *within fixed two-query linear estimators*, not among nonlinear or adaptive estimators, not for additional queries, and not under unknown covariance parameters.

## Proof

**1. Quadratic exactness forces symmetry.** Constants, affine functions and quadratic functions all belong to the function class with arbitrarily large coefficients. Finite worst-case error therefore requires
\[
w_1+w_2=0,\quad w_1a+w_2b=1,\quad w_1a^2+w_2b^2=0.
\]
If \(a=b\), the first two equations are inconsistent. For distinct sites, the first two yield \(w_1=1/(a-b)\), \(w_2=-1/(a-b)\), and the last gives \(a+b=0\). Hence, after swapping sites, \(a=h>0,b=-h,w_1=1/(2h),w_2=-1/(2h)\). No other predetermined two-query linear design has finite worst-case risk.

**2. Exact worst-case risk.** The central-difference identity \((f(h)-f(-h))/(2h)=\frac{1}{2h}\int_{-h}^{h}f'(u)\,du\) and Taylor's theorem give a deterministic bias bounded in absolute value by \(Mh^2/6\). Equality is attained at every \(h\) by \(f(u)=Mu^3/6\) and by its negative. The noise difference has variance \(2\sigma^2(1-\rho e^{-2h/\ell})\). Therefore the exact, not merely upper-bounded, worst-case mean-square risk is
\[
R(h)=\frac{M^2h^4}{36}+\frac{\sigma^2(1-\rho e^{-2h/\ell})}{2h^2}.
\]
It diverges at \(h\downarrow0\) for every \(\rho\in[0,1]\) (like \(h^{-2}\) for \(\rho<1\), and like \(h^{-1}\) for \(\rho=1\)), and at \(h\to\infty\) (like \(h^4\)).

**3. Unique global minimizer.** Differentiation yields
\[
R'(h)=\frac{M^2h^3}{9}-\frac{\sigma^2}{h^3}
\Bigl[1-\rho(1+h/\ell)e^{-2h/\ell}\Bigr].
\]
Put \(q_\rho(x)=1-\rho(1+x)e^{-2x}\). Then \(q_\rho>0\) and \(q'_\rho=\rho(1+2x)e^{-2x}\ge0\). For \(\rho=1\),
\[
6q_1(x)-xq'_1(x)=6-e^{-2x}(6+7x+2x^2)>0\quad(x>0)
\]
because \(6e^{2x}>6+7x+2x^2\). For \(0\le\rho<1\), \(q_\rho\ge q_1\) and \(q'_\rho\le q'_1\), so the same strict inequality holds. Thus \(q_\rho(x)/x^6\) strictly decreases from \(+\infty\) to \(0\) as \(x\) runs from \(0\) to \(+\infty\). The stationarity equation \(q_\rho(x)/x^6=1/\kappa\) consequently has exactly one solution, and \(R'\) changes from negative to positive there. As \(q_\rho(x)\) strictly decreases with \(\rho\) at each fixed \(x>0\), the unique root \(x_*\) strictly decreases with \(\rho\); the optimal risk also strictly decreases since the risk of any fixed finite \(h\) decreases strictly with \(\rho\).

**4. Singular correlation boundary layer.** Uniformly for \(0\le\rho\le1\) and \(x\downarrow0\),
\[
q_\rho(x)=(1-\rho)+\rho x+O(x^3).
\]
For fixed \(\rho<1\), the defining equation and \(x_*\to0\) imply \(x_*^6\sim\kappa(1-\rho)\). At \(\rho=1\), it gives \(x_*^5\sim\kappa\). Substitution into \(R(h)\) produces the displayed risk constants.

For the joint limit, write \(\delta=1-\rho\), \(\delta/\kappa^{1/5}\to\alpha\). Monotonicity in \(\rho\) gives \(x_*\ge x_*(\kappa,1)\sim\kappa^{1/5}\); the bound \(q_\rho(x)\le\delta+x\) for small \(x\) and the defining equation bound \(x_*=O(\kappa^{1/5})\). Thus every subsequential limit \(z=\lim x_*/\kappa^{1/5}\) satisfies \(z\ge1\) and \(z^6=z+\alpha\). The function \(z\mapsto z^6-z\) is strictly increasing on \([1,\infty)\), so the limit is uniquely \(z_\alpha\). Finally, \(1-\rho e^{-2x_*}=\delta+2x_*+o(\kappa^{1/5})\), giving the crossover risk expression.

## Verification

Run `python3 verify.py` with the Python standard library. It checks the stationary equation and a logarithmic grid of 361 competitors for 42 parameter pairs; verifies strict monotonicity in correlation, the cubic exact-bias witness, the analytic positivity condition on 5,000 seeded random inputs and three approaches to each of four boundary-layer limits. These supplementary finite checks do not prove uniqueness or asymptotics; those follow from the inequalities above. The script reports 20,174 checks.

For illustration with \(\kappa=10^{-5}\), the unique dimensionless spacings are approximately \(0.146779926762\) at \(\rho=0\), \(0.112272913733\) at \(\rho=0.9\), and \(0.099879220204\) at \(\rho=1\).

## Relationship to prior work

Lam, Li and Zhang (2020, arXiv:2007.04443), Section 2.1, prove a broader linear-minimax result for **independently sampled** noisy function evaluations with variance constraints. Its two-query independent case corresponds to \(\rho=0\) here and is not claimed as a new independent-noise result. The new question is what a specified *distance-dependent joint noise covariance* does to the exact optimum and especially to the singular nearly-perfect-correlation limit.

Shi, Xie, Xuan and Nocedal (2021, arXiv:2110.06380), Sections 1–3, develop an adaptive interval-selection procedure balancing truncation and bounded evaluation error; those guarantees do not supply the two-query correlated-Gaussian minimax equation or the correlation boundary layer. Liang, Liu and Zhang (2024, arXiv:2405.05638), Sections 2–4, construct correlated finite-difference *estimators from reused pilot samples* and study their statistical asymptotics; this is distinct from the stationary spatial correlation model imposed here on the two measurements. Berahas, Cao, Choromanski and Scheinberg (2019, arXiv:1905.01332), Sections 1–3, study multi-method gradient approximations under bounded function error and likewise do not establish the specific covariance-dependent sharp law.

Semantic searches for central finite differences, exponential/Ornstein–Uhlenbeck correlated oracle noise, two-query minimaxity, nugget variance, and fifth-versus-sixth-root scaling did not identify a covering exact result in the inspected sources. Absence of a match is not proof of historical uniqueness.

## Limitations

The minimax statement concerns predetermined **linear** two-query estimators, not arbitrary nonlinear algorithms or randomized/adaptive designs. It assumes \(M,\sigma,\ell>0\), known covariance, unrestricted locations on the real line, and unbounded lower polynomial coefficients of \(f\). It is a squared-error statement, not a tail-probability or almost-sure guarantee. The perfect-correlation endpoint is still spatially varying Ornstein–Uhlenbeck noise; it is not a perfectly common constant offset. The proof does not establish global publication priority; additional historical material on common random numbers and correlated-noise numerical differentiation could contain overlapping specializations.

## References

1. H. Lam, H. Li and X. Zhang, *Minimax Efficient Finite-Difference Stochastic Gradient Estimators Using Black-Box Function Evaluations*, arXiv:2007.04443, first submitted 8 July 2020, https://arxiv.org/abs/2007.04443.
2. H.-J. M. Shi, Y. Xie, M. Q. Xuan and J. Nocedal, *Adaptive Finite-Difference Interval Estimation for Noisy Derivative-Free Optimization*, arXiv:2110.06380, first submitted 12 October 2021, https://arxiv.org/abs/2110.06380.
3. G. Liang, G. Liu and K. Zhang, *A Correlation-induced Finite Difference Estimator*, arXiv:2405.05638, first submitted 9 May 2024, https://arxiv.org/abs/2405.05638.
4. A. S. Berahas, L. Cao, K. Choromanski and K. Scheinberg, *A Theoretical and Empirical Comparison of Gradient Approximations in Derivative-Free Optimization*, arXiv:1905.01332, first submitted 3 May 2019, https://arxiv.org/abs/1905.01332.
