# A unique abundance-threshold covariance reversal for every Dirichlet power concentration

## Finding
Let \(m\ge2\) be an integer, \(a>0\), and \(P=(P_1,\ldots,P_m)\sim\operatorname{Dirichlet}(a,\ldots,a)\). For every real \(q>1\) and \(0<t<1\), define the abundance-exceedance count \(N_t=\sum_{i=1}^m\mathbf 1\{P_i>t\}\) and the concentration power sum \(H_q=\sum_{i=1}^m P_i^q\). Put \(b=(m-1)a\), \(s=ma\), \((u)_q=\Gamma(u+q)/\Gamma(u)\), and \(T_{u,v}(t)=\Pr\{\operatorname{Beta}(u,v)>t\}\).

Then the **exact** dependence law, valid for all the indicated parameters, is
\[
\frac{\operatorname{Cov}(N_t,H_q)}{\mathbb E H_q}
=T_{a+q,b}(t)+(m-1)T_{a,b+q}(t)-mT_{a,b}(t),\qquad
\mathbb E H_q=\frac{m(a)_q}{(s)_q}.
\]
For each fixed \(m,a,q\), the covariance has **exactly one zero** \(t_q\in(0,1)\); it is strictly negative for \(0<t<t_q\) and strictly positive for \(t_q<t<1\). For the Simpson concentration order \(q=2\), the zero and the full covariance are explicit:
\[
t_2=\frac{a+1}{ma+2},\qquad
\operatorname{Cov}(N_t,H_2)
=\frac{m(s+2)t^a(1-t)^b}{(b+1)(s+1)B(a,b)}
\left(t-\frac{a+1}{s+2}\right).
\]
Moreover, as \(q\to\infty\) with \(m,a\) fixed, \(t_q\to t_\infty\), the unique solution of
\[
 m\Pr\{\operatorname{Beta}(a,(m-1)a)>t_\infty\}=1.
\]
Equivalently, this limiting threshold is where the **expected number of above-threshold components is one**. For example, for \(m=3,a=1\), \(t_2=2/5\) whereas \(t_\infty=1-1/\sqrt3\).

## Assumptions and scope
All \(m\) coordinates are exchangeable and have strictly positive Dirichlet parameter \(a\); the result does not assert the same unique crossing for heterogeneous Dirichlet parameters. The power order may be any real \(q>1\), not merely an integer. The threshold lies strictly between zero and one. No sampling observations, posterior update, finite-population correction, or asymptotic in \(m\) is assumed. The generalized Tsallis diversity \((1-H_q)/(q-1)\) has the opposite covariance sign.

## Proof
**Beta-tail identity.** By Dirichlet aggregation, \(P_1\sim\operatorname{Beta}(a,b)\). The Dirichlet monomial identity implies, for \(j\ne1\),
\[
\begin{aligned}
\mathbb E[P_1^q\mathbf 1\{P_1>t\}]&=\frac{(a)_q}{(s)_q}T_{a+q,b}(t),\\
\mathbb E[P_j^q\mathbf 1\{P_1>t\}]&=\frac{(a)_q}{(s)_q}T_{a,b+q}(t).
\end{aligned}
\]
Summing over \(i,j\), and using \(\mathbb E N_t=mT_{a,b}(t)\) and \(\mathbb E H_q=m(a)_q/(s)_q\), proves the first displayed identity.

**Single crossing.** Conditional on \(P_1=x\), the remaining normalized vector is independent and symmetric Dirichlet on \(m-1\) coordinates. Consequently
\[
f_q(x):=\mathbb E[H_q\mid P_1=x]=x^q+c_q(1-x)^q,
\qquad c_q=\frac{(m-1)(a)_q}{(b)_q}.
\]
Write \(\mu_q=\mathbb E H_q\) and \(g_q=f_q-\mu_q\). Since \(q>1\), \(g_q\) is strictly convex. Moreover \(g_q(1)=1-\mu_q>0\), and
\[
\frac{c_q}{\mu_q}=\frac{m-1}{m}\frac{(s)_q}{(b)_q}>1.
\]
The ratio equals one at \(q=1\) and increases strictly for \(q>1\), because its logarithmic derivative is \(\psi(s+q)-\psi(b+q)>0\). Thus \(g_q(0)>0\). Its beta-weighted mean is zero by the tower property, so strict convexity forces exactly two interior zeros with \(g_q<0\) between them. Let \(h(x)=x^{a-1}(1-x)^{b-1}/B(a,b)\) and \(J(t)=\int_t^1g_q(x)h(x)\,dx\). We have \(J(0)=J(1)=0\) and \(J'(t)=-g_q(t)h(t)\). Hence \(J\) starts negative, ends positive, and increases strictly between the two zeros of \(g_q\). This implies exactly one interior zero of \(J\), negative before and positive after it. Since \(\operatorname{Cov}(N_t,H_q)=mJ(t)\), the assertion follows.

**Quadratic order.** At \(q=2\), \(c_2=(a+1)/(b+1)\). For a beta density \(h\), integration by parts gives
\[
\begin{aligned}
\int_t^1(x-\mathbb E X)h(x)\,dx&=\frac{t(1-t)h(t)}s,\\
\int_t^1(x^2-\mathbb E X^2)h(x)\,dx
&=\frac{t(1-t)h(t)}{s+1}\left(t+\frac{a+1}s\right).
\end{aligned}
\]
Apply these to \(x^2+c_2(1-x)^2\). The result simplifies to the stated exact covariance, with unique zero \((a+1)/(s+2)\).

**Large power orders.** For each fixed \(0<t<1\), \(T_{a+q,b}(t)\to1\) and \(T_{a,b+q}(t)\to0\) as \(q\to\infty\), by concentration of the shifted beta laws at their respective endpoints. The exact identity therefore yields
\[
\lim_{q\to\infty}\frac{\operatorname{Cov}(N_t,H_q)}{\mathbb E H_q}
=1-mT_{a,b}(t)=1-\mathbb E N_t.
\]
The right-hand side is continuous and strictly increasing from \(1-m<0\) to \(1>0\). Its unique zero is \(t_\infty\); applying the one-crossing sign rule at points on either side proves \(t_q\to t_\infty\).

## Verification
The accompanying `verify.py` uses exact rational beta-binomial tails for 690 exact quadratic covariance identities and exact zero tests, then independently compares noninteger-power beta-tail formulas against direct conditional-moment quadrature. It also checks numerical large-order limits and root convergence. It completed 860 assertions successfully. These finite and numerical checks supplement, but do not replace, the analytic proof above. Run: `python verify.py` (Python 3, SciPy).

## Relationship to prior work
Cerquetti (2012) develops Simpson evenness moments under Gibbs-type species priors and explicitly identifies finite symmetric Dirichlet frequencies in Fisher's model. Cerquetti (2014) treats generalized Tsallis power-sum diversity and prior/posterior moments. Those frameworks supply the natural objects and standard Dirichlet moment tools. The claim here concerns instead a **mixed non-polynomial abundance-threshold count**, a complete all-real-power covariance sign classification, and the high-power threshold tied to expected exceedances. Inspected statements and formulas in those works do not state this mixed law or its one-crossing and limiting-threshold conclusions. Earlier general moment machinery may permit independent derivations; the historical originality assessment is limited accordingly.

## Limitations
The formula assumes a finite symmetric Dirichlet vector; heterogeneity, random number of categories, and observed-sample exceedances are not covered. No monotonicity in \(q\) of \(t_q\) is proved. Direct integration can derive the identities from familiar beta/Dirichlet facts; no priority claim is made for those classical facts. Unexamined full literature may contain an equivalent special-purpose threshold formula. Independent expert review has not been performed.

## References
- A. Cerquetti, *Bayesian nonparametric estimation of Simpson's evenness index under alpha-Gibbs priors*, arXiv:1203.1666 (first posted 2012-03-08), https://arxiv.org/abs/1203.1666.
- A. Cerquetti, *Bayesian nonparametric estimation of Tsallis diversity indices under Gnedin-Pitman priors*, arXiv:1404.3441 (first posted 2014-04-14), https://arxiv.org/abs/1404.3441.
- H. W. Block, T. H. Savits, and M. Shaked, *A concept of negative dependence using stochastic ordering*, *Statistics & Probability Letters* 3 (1985), 81–86, https://doi.org/10.1016/0167-7152(85)90029-X (general dependence background; does not by itself determine a mixed power-index covariance).
