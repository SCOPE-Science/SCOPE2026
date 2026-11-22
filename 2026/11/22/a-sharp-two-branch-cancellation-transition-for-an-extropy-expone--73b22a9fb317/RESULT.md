# A sharp two-branch cancellation transition for an extropy exponentiality test

## Finding

The scalar normalized-dynamic-survival-extropy (NDSE) exponentiality contrast of Kandpal and Gupta is not an omnibus discrepancy. In the natural two-cohort lifetime model
\[
F_{p,b}=p\,\mathrm{Unif}(0,1)+(1-p)\,\mathrm{Unif}(0,b),\qquad b>1,\quad 0\leq p\leq1,
\]
its population contrast \(\Delta=\mathbb E X-3\mathbb E\min(X_1,X_2,X_3)\) exhibits a sharp two-branch cancellation transition. Write
\[
\begin{aligned}
4b^2\Delta(p,b)&=P_b(p),\\
P_b(p)&=3(b-1)^3p^3+(-9b^3+24b^2-21b+6)p^2\\
&\quad +(7b^3-16b^2+12b-3)p-b^3,
\end{aligned}
\]
and define \(b_*\) to be the unique root greater than one of
\[
Q(b)=32b^4-144b^3+39b^2+18b-9=0.
\]
Then \(b_*=4.180098403603496\ldots\), and the complete zero classification in the interior \(0<p<1\) is:

- \(1<b<b_*\): no zero; the contrast is strictly negative at every mixing weight.
- \(b=b_*\): exactly one distinct zero \(p_*=0.5977073861451475\ldots\), of multiplicity two; the contrast is nonpositive.
- \(b>b_*\): exactly two simple zeros \(0<p_-(b)<p_+(b)<1\). The contrast is positive precisely between them and negative elsewhere.

At the onset, the roots split with a square-root law
\[
p_{\pm}(b)=p_*\pm K\sqrt{b-b_*}+O(b-b_*),\qquad
K=0.2502581513893773\ldots.
\]
Both components individually have strictly negative population contrasts, \(-1/4\) and \(-b/4\). Thus cancellation is created by mixing rather than inherited from a component. Every zero is a nonexponential continuous distribution and has a nonconstant NDSE profile.

This cancellation is robust: for each fixed \(b>b_*\), the two component uniforms can be replaced by sufficiently close \(C^\infty\), strictly positive densities on \((0,\infty)\), and their mixture still has at least two distinct interior cancellation weights. The sharp quartic threshold above is asserted only for the exact uniform-mixture family, not for arbitrary smoothed components.

For independent observations, define the sample contrast \(\widehat\Delta_n=\overline X_n-3\binom n3^{-1}\sum_{i<j<k}\min(X_i,X_j,X_k)\) and the scale-free statistic \(\widehat\Delta_n^*=\widehat\Delta_n/\overline X_n\). At each of the two blind weights, \(\widehat\Delta_n^*\to0\) almost surely but
\[
\sqrt n\,\widehat\Delta_n^*\ \Longrightarrow\ N(0,v_F),\qquad
v_F=\frac{\operatorname{Var}\!\left(X-9\int_0^X\overline F(t)^2\,dt\right)}{(\mathbb E X)^2}>0.
\]
Consequently the original left-sided test, calibrated using null asymptotic variance \(4/5\) and fixed nominal level \(0<\alpha<1/2\), has limiting rejection probability
\[
\Phi\!\left(z_\alpha\sqrt{\frac{4/5}{v_F}}\right)<1,
\]
where \(z_\alpha\) is the lower standard-normal \(\alpha\)-quantile. In particular, at \(b=6\) the blind weights are \(0.3346846973374498\ldots\) and \(0.8569101973499097\ldots\). Their normalized variances are respectively \(0.60103119368594\ldots\) and \(1.41841748723474\ldots\); at \(\alpha=0.05\), limiting rejection probabilities are \(0.02886890450816\ldots\) and \(0.10836061655085\ldots\), respectively, not one.

## Assumptions and scope

All populations are nonnegative, with finite positive mean. In the exact phase diagram, \(X\) has the two-component mixture distribution above, and \(X_1,X_2,X_3\) denote independent copies. For the sampling result, the data are independent identically distributed from one fixed interior blind mixture, and sample size tends to infinity; finite second moments hold automatically. The normalized statistic is defined for \(n\geq3\) and positive sample mean, almost surely in this model. The one-sided threshold is the fixed asymptotic Gaussian-null threshold, not an adaptive or censored-data calibration. For the smoothing assertion, only existence of at least two roots is claimed.

## Proof

**Exact polynomial.** On \(0\leq x\leq1\), the survival function equals \(1-cx\), where \(c=p+(1-p)/b\). On \(1<x\leq b\), it equals \((1-p)(1-x/b)\), and it vanishes above \(b\). The tail-integral formula for a nonnegative minimum gives
\[
\mathbb E\min(X_1,X_2,X_3)=\int_0^\infty\overline F(x)^3\,dx
=1-\frac{3c}{2}+c^2-\frac{c^3}{4}
+\frac{(1-p)^3(b-1)^4}{4b^3}.
\]
Since \(\mathbb E X=[p+(1-p)b]/2\), expanding the difference produces \(P_b(p)/(4b^2)\), with no asymptotic approximation. At \(p=0\) and \(p=1\), the differences are \(-b/4\) and \(-1/4\).

**Exact bifurcation.** Direct algebra gives the cubic discriminant
\[
\operatorname{disc}_p(P_b)=3b^2(b-1)^6Q(b).
\]
With \(t=b-1>0\),
\[
Q(1+t)=32t^4-16t^3-201t^2-208t-64.
\]
Descartes' sign rule and its endpoint signs show this has exactly one positive root, defining \(b_*\). Below it the cubic has exactly one real root; because the endpoint values on \([0,1]\) are both negative while the leading coefficient is positive, that sole root lies above one. Above it there are three simple real roots. At \(b=5\), direct polynomial evaluation shows two in \((0,1)\) and one above one (the local maximum occurs at \(p=7/12\) and \(\Delta(7/12,5)=1/9\)); on the connected interval \(b>b_*\), no root can cross \(p=0\) or \(p=1\), since neither endpoint contrast ever vanishes. Therefore there are exactly two interior roots for all \(b>b_*\); by continuity they merge to a double interior root at \(b_*\). The signs follow from the positive leading coefficient and the three ordered roots. The onset coefficient follows by Taylor-expanding \(\Delta(p,b)\) at the double point:
\[
K=\sqrt{-\frac{2\,\partial_b\Delta(p_*,b_*)}
{\partial_{pp}\Delta(p_*,b_*)}},
\]
where the numerator derivative is positive and the second derivative is negative, as independently evaluated from the exact polynomial.

**Nonexponential nature and robustness.** Each mixture has finite upper support \(b\), hence is not exponential. The source characterization says constant NDSE implies exponentiality, so its NDSE cannot be constant. At a zero, the original integrand \(\delta(x)\) integrates to zero but is not identically zero, and therefore must take both signs on its effective support; this is a cancellation of a signed integral, not a counterexample to the full-function characterization. The map \(F\mapsto\Delta(F)\) is Lipschitz for nonnegative laws of finite mean under one-dimensional Wasserstein-1 distance: since \(|u^3-v^3|\le3|u-v|\) for survival probabilities,
\[
|\Delta(F)-\Delta(G)|\le \int_0^\infty|\overline F-\overline G|\,dx
+9\int_0^\infty|\overline F-\overline G|\,dx
=10W_1(F,G).
\]
Approximate each uniform component by a \(C^\infty\) positive density with arbitrarily small \(W_1\) error (smooth compact-support approximation plus an arbitrarily small exponential tail). Mixing does not increase the maximum component \(W_1\) error. Three fixed weights with negative, positive, negative contrast straddling the two simple roots retain their signs, and the intermediate-value theorem supplies two distinct zeros for the smoothed mixture.

**Fixed-alternative limit.** The symmetric degree-three kernel is \(h(x,y,z)=(x+y+z)/3-3\min(x,y,z)\). Its first-order Hájek projection, multiplied by the kernel degree, is the centered version of \(x-9G_F(x)\), where \(G_F(x)=\int_0^x\overline F(t)^2dt\). The degree-three U-statistic central limit theorem therefore gives \(\sqrt n(\widehat\Delta_n-\Delta)\Rightarrow N(0,\operatorname{Var}(X-9G_F(X)))\). The projection is nonconstant because its derivative on \((0,b)\) equals \(1-9\overline F(x)^2\), which is not identically zero under a strictly decreasing survival. Thus its variance is positive. At a blind weight \(\Delta=0\), dividing by \(\overline X_n\to\mathbb E X\) proves the stated Gaussian limit. The known exponential-null variance of the normalized statistic is \(4/5\). The normal distribution is continuous, so taking limits in the lower-tail rejection event gives the stated limiting probability.

## Verification

The bundled script `verification/check.py` is executable with Python, SymPy and mpmath; it performs 69 assertions, checking the symbolic tail-integral polynomial, cubic discriminant, endpoint signs, quartic shift, explicit rational witness \(\Delta(1/2,6)=89/384\), double-root residual, finite-sample U-statistic identity, exact projection variance, numerical root locations and independent numerical integration. At \(b=6\), the projected variance uses exact polynomial integration on \([0,1]\) and \([1,6]\), not simulation. The resulting variance numerator is
\[
-\frac{1640625p^6-8125000p^5+14743750p^4-11518000p^3+2940825p^2+653240p-345024}{26880}.
\]
The script verifies this identity symbolically and evaluates it at both roots. The root-count proof and stochastic limit are mathematical arguments above; numerical checking alone is not used as a proof for infinitely many parameters or sample sizes.

## Relationship to prior work

Kandpal and Gupta, arXiv:2407.11634v1 (first public posting July 16, 2024), introduce the NDSE profile, its exponential characterization, the signed scalar contrast \(\mathbb EX-3\mathbb E\min(X_1,X_2,X_3)\), the associated degree-three U-statistic and fixed-distribution normal limits. Those formulas are acknowledged prerequisites. The paper explicitly frames the lower-tail test against the increasing-NDSE class; the present uniform mixtures at the cancellation weights lie outside both strict one-sided sign classes, and the theorem does not dispute consistency within the stated restricted alternative. The new claim is the *complete sharp mixture-parameter zero set*, its bifurcation, persistence under smoothing, and its paired, nontrivial limiting calibration effects. These are not the paper's general characterizing identity or null distribution rewritten. Its reported simulations concern other alternative families, not the two-uniform cancellation phase. Related literature on estimation of finite uniform mixtures concerns mixture inference, not this NDSE contrast.

## Limitations

The classification is exact for mixtures of two uniforms with common lower endpoint, not all distribution mixtures. Smoothing guarantees existence but not exact location or uniqueness of roots. The fixed-alternative rejection probabilities apply to the original one-sided Gaussian-asymptotic calibration; exact finite-sample critical values, censored estimation, power of omnibus tests and joint local alternatives are not studied. The 2025 journal version of the source could not be inspected in full, leaving a historical-priority risk; this result has no independent expert validation.

## References

1. G. Kandpal and N. Gupta, *A goodness-of-fit test for testing exponentiality based on normalized dynamic survival extropy*, arXiv:2407.11634v1, first posted July 16, 2024, https://arxiv.org/abs/2407.11634 (relevant pages 3–6 and Section 5).
2. G. Kandpal and N. Gupta, *A goodness-of-fit test for testing exponentiality based on normalized dynamic survival extropy*, Mathematica Slovaca 75(3), 679–698 (2025), DOI https://doi.org/10.1515/ms-2025-0050 (bibliographic and abstract metadata only; full journal text not reviewed).
3. R. D. Gupta and K. Miyawaki / finite-mixture literature discussed in *Parameter estimation for finite mixtures of uniform distributions*, Communications in Statistics (1997), https://doi.org/10.1080/03610929708832026 (abstract only; models of component mixtures, not the NDSE test).
