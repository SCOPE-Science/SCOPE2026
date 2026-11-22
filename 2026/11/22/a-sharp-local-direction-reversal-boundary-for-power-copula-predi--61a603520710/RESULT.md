# A sharp local direction-reversal boundary for power copula predictability

## Finding
For the one-variable-power copula family of Chesneau (2023), take
\[
C_{\alpha,\beta}(u,v)=u\,v^{1+\beta(1-u^\alpha)},\qquad
\alpha>0,\quad 0<\beta\le1/\alpha,\quad (u,v)\in[0,1]^2.
\]
Let \(\xi(V\mid U)\) and \(\xi(U\mid V)\) be the *population*, directional Chatterjee rank-dependence coefficients of the two uniform coordinates. Write
\[\Delta(\alpha,\beta)=\xi(U\mid V)-\xi(V\mid U).\]
All these nonindependent copulas are strictly negatively quadrant dependent at every interior point. Nevertheless their **direction of greater rank predictability reverses** at a sharp shape threshold as dependence weakens: for each fixed \(\alpha>0\), \(\alpha\ne9/2\), sufficiently small positive \(\beta\) gives
\[
\operatorname{sign}\Delta(\alpha,\beta)=\operatorname{sign}(9-2\alpha).
\]
More precisely, uniformly for \(\alpha\) in compact subsets of \((0,\infty)\),
\[
\Delta(\alpha,\beta)=D_2(\alpha)\beta^2+D_3(\alpha)\beta^3+O(\beta^4),
\]
with the exact coefficients
\[
D_2(\alpha)=\frac{-4\alpha^3(2\alpha-9)}{9(\alpha+3)(2\alpha+1)(2\alpha+3)},
\]
\[
D_3(\alpha)=\frac{8\alpha^4(2\alpha^2-43\alpha-27)}{9(\alpha+1)(\alpha+3)(2\alpha+1)(2\alpha+3)(3\alpha+1)}.
\]
At the critical exponent, \(D_2(9/2)=0\), \(D_3(9/2)=-1458/1595\), so the reverse conditioning direction strictly dominates for sufficiently small positive \(\beta\). There is an open neighborhood of \((9/2,0)\) and a **unique** smooth curve \(\alpha_*(\beta)\), defined for all sufficiently small positive \(\beta\), on which the two coefficients are equal. In that neighborhood,
\[
\alpha_*(\beta)=\frac92-\frac{3240}{319}\beta+O(\beta^2),
\]
with \(\Delta>0\) below the curve and \(\Delta<0\) above it. Thus the transition bends left as dependence grows. The uniqueness claim is **local**, not global over all admissible parameters.

## Assumptions and scope
The family is the power example (with its auxiliary shape exponent set to one) in Chesneau, *Axioms* **12** (2023), article 392, Section 2.2, Function 1. The original parameters permit every \(\alpha>0\) and \(0\le\beta\le1/\alpha\). The case \(\beta=0\) is the independent copula; here it is used only to expand the functionals. The coefficient \(\xi(W\mid Z)\) means the proportion of integrated conditional indicator variance for response \(W\) given predictor \(Z\). In particular the two directions must not be interchanged or regarded as causal. The theorem concerns weak but nonzero dependence, and the critical-curve assertion is confined to a neighborhood of the independence boundary at exponent \(9/2\). No sample-size or estimator statement is asserted.

## Proof
**Copula validity and dependence sign.** Set \(f(u)=1+\beta(1-u^\alpha)\). Then \(f(1)=1\), \(f\ge1\), \(f'=-\alpha\beta u^{\alpha-1}\le0\), and
\[
f(u)+u f'(u)=1+\beta[1-(1+\alpha)u^\alpha]\ge1-\alpha\beta\ge0.
\]
Chesneau's OVP copula criterion therefore applies. Alternatively its mixed density is
\[
\partial_u\partial_v C=v^{f(u)-1}\bigl[f(u)+u f'(u)+u f(u)f'(u)\log v\bigr]\ge0,
\]
with the standard four uniform-margin boundary identities. Since \(f(u)>1\) for \(u\in(0,1)\) and \(\beta>0\), we have \(C(u,v)<uv\) for all \((u,v)\in(0,1)^2\), proving strict NQD.

**Exact population functionals.** For continuous uniform margins, Chatterjee's normalized population formula is
\[
\xi(V\mid U)=6\int_0^1\!\int_0^1(\partial_u C(u,v)-v)^2\,dv\,du,
\quad
\xi(U\mid V)=6\int_0^1\!\int_0^1(\partial_v C(u,v)-u)^2\,dv\,du.
\]
Here \(\partial_u C=v^{f(u)}(1+u f'(u)\log v)\) and \(\partial_v C=u f(u)v^{f(u)-1}\). Elementary integrations in \(v\) (all denominators are strictly positive because \(f\ge1\)) give two exact one-dimensional representations:
\[
\xi(U\mid V)=6\int_0^1u^2\left[\frac{f(u)^2}{2f(u)-1}-1\right]du,
\]
\[
\xi(V\mid U)=6\int_0^1\left[\frac1{2f+1}-\frac{2u f'}{(2f+1)^2}+\frac{2u^2(f')^2}{(2f+1)^3}-\frac2{f+2}+\frac{2u f'}{(f+2)^2}+\frac13\right]du.
\]
These identities independently fix both direction conventions and allow differentiation in the dependence parameter.

**Taylor calculation.** Put \(g(u)=1-u^\alpha\) and \(h(u)=(ug(u))'=1-(1+\alpha)u^\alpha\). Expanding the conditional-CDF deviations to cubic order, and using
\(\int_0^1 v^2(\log v)^2dv=2/27\),
\(\int_0^1 v^2(\log v)^3dv=-2/27\), and
\(\int_0^1(1+\log v)(\log v+(\log v)^2/2)dv=-1\), yields
\[
\xi(V\mid U)=\frac49\beta^2\int_0^1h^2du-\frac49\beta^3\int_0^1h(g^2+2ug g')du+O(\beta^4),
\]
\[
\xi(U\mid V)=6\beta^2\int_0^1u^2g^2du-12\beta^3\int_0^1u^2g^3du+O(\beta^4).
\]
The four elementary power integrals are
\[
\int_0^1h^2du=\frac{\alpha^2}{2\alpha+1},\quad
\int_0^1u^2g^2du=\frac{2\alpha^2}{3(\alpha+3)(2\alpha+3)},
\]
\[
\int_0^1h(g^2+2ug g')du=\frac{2\alpha^3}{(2\alpha+1)(3\alpha+1)},\quad
\int_0^1u^2g^3du=\frac{2\alpha^3}{3(\alpha+1)(\alpha+3)(2\alpha+3)}.
\]
Subtracting the two expansions and simplifying gives the displayed \(D_2,D_3\). On any compact positive \(\alpha\)-interval, \(0\le g\le1\) and \(|u f'|\le\alpha\beta\), and the exact representations have denominators bounded away from zero for \(\beta\) sufficiently near zero. Taylor remainders of order four are consequently uniform; derivatives in \(\alpha\) are locally uniformly integrable (powers of \(u^\alpha\log u\) cause no problem). Thus the function \(G(\alpha,\beta)=\Delta(\alpha,\beta)/\beta^2\) extends real-analytically in a neighborhood of \((9/2,0)\), with \(G(\alpha,0)=D_2(\alpha)\).

**Sharp crossing and drift.** \(D_2\) has precisely one positive root \(9/2\); it is positive below that point and negative above. The exact boundary derivatives are
\[
\partial_\alpha G(9/2,0)=D_2'(9/2)=-\frac9{100},\qquad
\partial_\beta G(9/2,0)=D_3(9/2)=-\frac{1458}{1595}.
\]
The analytic implicit-function theorem produces a unique locally defined \(\alpha_*(\beta)\) satisfying \(G=0\). Its derivative is
\[
\alpha_*'(0)=-\frac{\partial_\beta G(9/2,0)}{\partial_\alpha G(9/2,0)}=-\frac{3240}{319}.
\]
Continuity keeps \(\partial_\alpha G<0\) in a sufficiently small neighborhood, proving both local uniqueness and the asserted signs. All sufficiently small positive \(\beta\) here are automatically admissible since \(\beta<1/\alpha\) around \(\alpha=9/2\).

## Verification
The companion standalone `verify.py` uses SymPy to rederive each of the two Taylor coefficients from four independent exact power integrals, checks the critical values and crossing slope as rational identities, and checks partial derivatives of the copula. It independently evaluates the two **exact** one-dimensional Chatterjee integrals with 70-digit mpmath quadrature at several exponents and positive parameters; direct nonlinear roots near the critical shape agree with the predicted first-order drift. The script prints `PASS` after all checks. Finite numerical probes are supplementary; the all-parameter local conclusions come from the analytic expansion and implicit-function proof above.

## Relationship to prior work
Chesneau (2023), Theorem 1 and Section 2.2 Function 1, establish validity of the whole power-OVP family. Sections 3.1–3.3 focus on a different inverse-power member and discuss copula shape, concordance, and ordinary correlations, not the two directed Chatterjee coefficients of the present power member. Chatterjee (2019/2021), Theorem 1.1, supplies the population dependence measure and distinguishes its two directions; the measure itself is not claimed as new. Ansari and Rockel (2024) provide ordering results and dependence tables for major copula families, not this small-parameter power-OVP direction-reversal boundary. A 2024 companion paper by Chesneau treats two other variable-power constructions; the accessible abstract does not resolve the present parameter-specific comparison. The assessed contribution is solely the exact \(9/2\) threshold, its nonvanishing critical cubic term, and the local equal-predictability boundary and slope; general Chatterjee formulas and construction of this copula are prior work.

## Limitations
The \(9/2\) threshold is for **sufficiently small positive** \(\beta\) at fixed shape, not a claimed universal phase classification over the entire admissible two-parameter domain. Uniqueness of the equality curve is local near \((9/2,0)\). Population \(\xi\) is not a causal statistic, and this work makes no finite-sample power or inference claim. The mathematical result has had a self-review, not an independent audit. Search-based historical originality is provisional, especially for less-accessible variable-power papers.

## References
1. C. Chesneau, "Theoretical Validation of New Two-Dimensional One-Variable-Power Copulas," *Axioms* **12** (2023), 392, published 2023-04-18. https://doi.org/10.3390/axioms12040392.
2. S. Chatterjee, "A new coefficient of correlation," arXiv:1909.10140 (first public version 2019-09-23); later published in *Journal of the American Statistical Association*. https://arxiv.org/abs/1909.10140.
3. J. Ansari and M. Rockel, "Dependence properties of bivariate copula families," *Dependence Modeling* **12** (2024), 20240002. https://doi.org/10.1515/demo-2024-0002.
4. H. Dette, K. F. Siburg and P. A. Stoimenov, "A copula-based non-parametric measure of regression dependence," *Scandinavian Journal of Statistics* **40** (2013), 21–41. https://doi.org/10.1111/j.1467-9469.2011.00767.x.
5. C. Chesneau, "Solutions to two open problems on bivariate variable-power copulas," *Bulletin of Computational Applied Mathematics* **12** (2024), 93–118. https://www.compama.co.usb.ve/table-of-contents/abstract-92.
