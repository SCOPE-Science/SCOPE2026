# A smooth blind manifold for a uniformity U-statistic with subnominal limiting power

## Finding
For every \(a\in[-1,1]\setminus\{0\}\), let the shifted Legendre polynomials be
\[
L_2(x)=6x^2-6x+1,\qquad L_4(x)=70x^4-140x^3+90x^2-20x+1,
\]
and put
\[
b(a)=\frac{462+11a-\sqrt{(462+11a)^2-660a^2}}{66}
=\frac{10a^2}{462+11a+\sqrt{(462+11a)^2-660a^2}}.
\]
Then \(f_a(x)=1+aL_4(x)+b(a)L_2(x)\) is a strictly positive, symmetric, nonuniform polynomial probability density on \([0,1]\). For the uncensored Sreedevi--Kattumannil uniformity U-statistic, its population discrepancy \(\Delta(f_a)\) is exactly zero. Within the natural two-mode family \(1+aL_4+bL_2\) with \(|a|\le1\), this is the unique admissible zero-contrast value of \(b\) (the uniform density occurs at \(a=b=0\)).

Under every such nonuniform alternative, the usual two-sided null-normal-calibrated test has a strictly positive, finite limiting rejection probability, not limiting power one. More strongly, the admissible member \(a=-1\) has limiting rejection probability \(0.017188026350862136\ldots\) at nominal level \(0.05\), strictly *below* the nominal level.

## Assumptions and scope
Let \(X_1,X_2,\dots\) be independent identically distributed random variables supported on \([0,1]\), with no censoring and no fitted support endpoint. For independent copies \(X,Y\), define the bounded symmetric kernel
\[
h(x,y)=\max(x,y)-x-y+\frac{x^2+y^2}{2},
\qquad \widehat\Delta_n={\binom n2}^{-1}\sum_{1\le i<j\le n}h(X_i,X_j),\quad n\ge2,
\]
and \(\Delta(F)=\mathbb E_F h(X,Y)=\mathbb E_F\max(X,Y)-2\mathbb E_F X+\mathbb E_F X^2\). This is the uncensored scalar test in the 2021 preprint and 2023 journal version cited below. Its nominal \(\alpha\)-level asymptotic rejection rule is
\[
\sqrt{45n}\,|\widehat\Delta_n|>z_{1-\alpha/2},\qquad 0<\alpha<1,
\]
where \(z_p\) is the standard normal \(p\)-quantile. The theorem concerns this *signed scalar integral*; it does not concern an entire pointwise characterization, an integrated squared distance, or a right-censoring estimator.

## Proof
**Exact polynomial discrepancy.** Both \(L_2,L_4\) have integral zero on \([0,1]\) and are invariant under \(x\mapsto1-x\). Hence every \(f_{a,b}=1+aL_4+bL_2\) integrates to one and has mean \(1/2\), whenever it is nonnegative. With \(F_{a,b}(x)=\int_0^x f_{a,b}(t)\,dt\), continuity gives
\[
\mathbb E\max(X,Y)=2\int_0^1 x f_{a,b}(x) F_{a,b}(x)\,dx.
\]
Direct polynomial integration yields the exact identity
\[
\boxed{\Delta(f_{a,b})=\frac{462b+11ab-33b^2-5a^2}{6930}.}
\]
Thus the zero-discrepancy equation is \(33b^2-(462+11a)b+5a^2=0\); its two algebraic solutions are
\[
b_\pm(a)=\frac{462+11a\pm\sqrt{(462+11a)^2-660a^2}}{66}.
\]
The discriminant is positive for every \(|a|\le1\), and \(b(a)=b_-(a)\). For \(a\ne0\), \(0<b_-(a)<10/901<1/80\), since \(462+11a\ge451\) and \(\sqrt{(462+11a)^2-660a^2}>450\). Meanwhile \(b_+(a)>900/66>13\), so at \(x=1/2\), where \(L_2=-1/2\) and \(L_4=3/8\), one has \(f_{a,b_+}(1/2)=1+3a/8-b_+/2<0\). The larger algebraic root can never be a density.

**Strict positivity of the lower branch.** Write \(u=x(1-x)\in[0,1/4]\). Then \(L_2=1-6u\) and \(L_4=1-20u+70u^2\). For \(-1\le a\le0\), the function
\[
 f_{a,b(a)}=(1+a+b(a))+(-20a-6b(a))u+70a u^2
\]
is concave in \(u\). Its minimum is attained at an endpoint: at \(u=0\) the value is \(1+a+b(a)>0\), and at \(u=1/4\) it is \(1+3a/8-b(a)/2\ge5/8-1/160>0\). For \(0\le a\le1\), the inequalities \(L_4\ge-3/7\) and \(L_2\ge-1/2\) give \(f_{a,b(a)}\ge4/7-1/160>0\). Hence all members are strictly positive and analytic. Since \(L_4\) is orthogonal to \(1\) and \(L_2\), no \(a\ne0\) member equals the uniform density.

**Fixed-alternative limiting power.** Set
\[
Q_F(x)=\int_0^x\big(F(t)+t-1\big)\,dt,
\qquad \sigma_F^2=4\operatorname{Var}_F(Q_F(X)).
\]
The conditional expectation \(\mathbb E[h(x,Y)]\) differs from \(Q_F(x)\) only by a constant, as its derivative is \(F(x)+x-1\). The standard nondegenerate order-two U-statistic central limit theorem gives
\[
\sqrt n\big(\widehat\Delta_n-\Delta(F)\big)
\ \xrightarrow{\mathcal D}\ N(0,\sigma_F^2).
\]
For each \(f_a\), the derivative of \(Q_F\) equals \(-1\) at zero and \(+1\) at one; because \(f_a>0\), \(Q_F(X)\) is nonconstant and \(0<\sigma_{f_a}^2<\infty\). Under the uniform null, \(Q_F(x)=x^2-x\) and \(\sigma_0^2=1/45\). Since \(\Delta(f_a)=0\), the asymptotic rejection probability is exactly
\[
\boxed{\pi_\alpha(a)=2\Phi\!\left(-\frac{z_{1-\alpha/2}}{\sqrt{45\sigma_{f_a}^2}}\right)\in(0,1),}
\]
where \(\Phi\) is the standard normal CDF. Thus the test is not consistent against these fixed smooth alternatives.

**Explicit subnominal case.** Taking \(a=-1\), write
\[
b_*=\frac{451-\sqrt{451^2-660}}{66}=0.01109548253032186777\ldots.
\]
For general \(a,b\), direct integration of \(Q_F'\) gives
\[
Q_{a,b}(x)=\frac{x(x-1)}6\left(14ax^4-28ax^3+17ax^2-3ax+3bx^2-3bx+6\right).
\]
Integrating \(Q_{-1,b}\) and its square against \(f_{-1,b}\) gives the exact variance polynomial
\[
\sigma^2_{-1,b}=\frac{3187127}{212270058}+\frac{536b}{257985}-\frac{282713b^2}{56756700}+\frac{461b^3}{363825}-\frac{b^4}{11025}.
\]
Since \(0<b_*<1/80\), the two negative-power corrections can be dropped, and the two positive corrections bounded by their values at \(1/80\), giving the rigorous strict bound
\[
\sigma^2_{-1,b_*}<\frac{3187127}{212270058}+\frac{536}{257985\cdot80}+\frac{461}{363825\cdot80^3}<\frac1{45}.
\]
Thus subnominal limiting rejection probability follows *analytically*, without trusting a decimal computation. High-precision evaluation of these exact finite polynomial integrals gives
\[
\sigma^2_{f_{-1}}=0.0150369325099423829699\ldots,
\qquad \pi_{0.05}(-1)=0.0171880263508621362153\ldots<0.05.
\]
These numbers are evaluations of algebraic constants, not Monte Carlo extrapolations.

## Verification
The accompanying `check.py` derives the contrast identity symbolically from independent integral formulas, checks the zero equation, reconstructs the conditional-projection polynomial and null variance, and evaluates the exceptional member using independent high-precision quadrature. It also tests density positivity at a finite grid and verifies direct U-statistic/order-statistic agreement for several finite samples. Its 8,617 checks passed. The interval positivity argument and U-statistic limit above, rather than a numerical grid or simulation, justify the infinite-domain statements. Run with `python check.py` using Python 3, SymPy and mpmath.

## Relationship to prior work
Sreedevi and Kattumannil's earliest publicly dated June 11, 2021 preprint, and its 2023 journal version, introduce the scalar \(\widehat\Delta_n\), derive its null variance and report power on selected alternatives. Their starting point is a pointwise uniform-distribution characterization, which does not imply that a *signed integrated* discrepancy is zero only under uniformity. Neither inspected version supplies this polynomial zero manifold or its explicit subnominal limiting-power example. The pointwise characterization and the squared-integral beta goodness-of-fit procedure of Ebner and Liebenberg concern different statistics: a pointwise identity (or integral of its square) cannot cancel across thresholds in the same fashion. Standard U-statistic theory supplies the CLT mechanism but does not identify these nonuniform alternatives or their exact power law.

## Limitations
The conclusion is confined to the fully observed, fixed-support signed statistic and its published null-normal calibration; it does not transfer automatically to Kaplan--Meier reweighting, maximum-estimated endpoints, or a sup-norm/squared-integral test. The CLT is a fixed-alternative large-sample statement, not a finite-sample guarantee. The algebraic family is complete only within the specified two-Legendre-mode slice and parameter range, not among all probability densities. Related generic observations that a scalar statistic need not be omnibus are classical; historical priority for this *specific exact family and power coefficient* has not been independently certified.

## References
1. S. K. Kattumannil and E. P. Sreedevi, *A new goodness of fit test for uniform distribution with censored observations*, arXiv:2106.06368v1, first publicly submitted 2021-06-11. https://arxiv.org/html/2106.06368
2. E. P. Sreedevi and S. K. Kattumannil, *Goodness of fit test for uniform distribution with censored observation*, Journal of the Korean Statistical Society 52 (2023), 382--394, DOI:10.1007/s42952-023-00205-8. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC9869324/
3. B. Ebner and S. C. Liebenberg, *On a new test of fit to the beta distribution*, arXiv:2009.13995 (2020), Stat 10 (2021), e341. https://arxiv.org/abs/2009.13995
4. W. Hoeffding, *A class of statistics with asymptotically normal distribution*, Annals of Mathematical Statistics 19 (1948), 293--325. https://doi.org/10.1214/aoms/1177730196
