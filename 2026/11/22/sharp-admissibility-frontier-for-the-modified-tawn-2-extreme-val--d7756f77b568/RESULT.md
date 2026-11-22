# Sharp admissibility frontier for the modified-Tawn-2 extreme-value copula

## Finding

**Theorem.** Fix real parameters \(a\geq1\), \(0<b,c\leq1\), and \(d\geq0\). The modified-Tawn-2 function
\[
A(w)=1-c+(c-b)w+\left[b^a w^a+d\{w(1-w)\}^{a/2}+c^a(1-w)^a\right]^{1/a},\qquad 0\leq w\leq1,
\]
is a Pickands dependence function, equivalently generates a bivariate extreme-value copula, **if and only if** either
\[
d=0\quad\text{(any \(a\geq1\))},
\]
or
\[
a\geq2,\qquad 0<d\leq2(a-1)(bc)^{a/2}.
\]
At the positive critical value \(d=2(a-1)(bc)^{a/2}\) for \(a>2\), curvature vanishes at exactly one interior point \(w_*=c/(b+c)\); above it, the function is not convex. When \(a=2\), the critical function is exactly \(A\equiv1\), the independence copula. Thus, within the stated domain, these conditions are necessary as well as sufficient, including all boundary cases.

The published sufficient range for \(d>0\) is \(a\geq2\) and \(d\leq2\sqrt{a-1}(bc)^{a/2}\). For \(a>2\), the sharp upper bound is a factor \(\sqrt{a-1}\) larger. For instance, \((a,b,c,d)=(3,1,1,7/2)\) is valid under this theorem but lies outside the previously established sufficient range.

## Assumptions and scope

A Pickands dependence function means a continuous convex function \(A:[0,1]\to\mathbb R\) satisfying \(A(0)=A(1)=1\) and \(A(w)\geq\max\{w,1-w\}\) everywhere. Such a function generates the standard bivariate extreme-value copula \(C(u,v)=\exp\{\log(uv)A(\log(v)/\log(uv))\}\) for \(0<u,v<1\), with continuous boundary extension. Parameters are restricted to the explicitly stated real domain; no statement is made for negative \(d\), nonpositive \(b,c\), or \(a<1\). The model and the earlier sufficient parameter bounds are those of Chesneau (2024), Proposition 2, equation (6).

## Proof

**Boundary and obstacle conditions.** Write \(P(w)=b^a w^a+d\{w(1-w)\}^{a/2}+c^a(1-w)^a\). Since \(a\geq1\), \(b,c>0\), and \(d\geq0\), the root \(P(w)^{1/a}\) is well defined, and \(A(0)=A(1)=1\). Moreover,
\[
A(w)\geq1-c(1-w)\geq w,\qquad A(w)\geq1-bw\geq1-w.
\]
Thus the Pickands property reduces exactly to convexity.

**Exact curvature.** On \(0<w<1\), direct differentiation gives
\[
A''(w)=\frac14\{w(1-w)\}^{a/2-2}P(w)^{1/a-2}K(w),
\]
where
\[
K(w)=(a-2)d\{b^a w^a+c^a(1-w)^a\}+\{4(a-1)(bc)^a-d^2\}\{w(1-w)\}^{a/2}.
\]
The prefactor is strictly positive. One direct reconstruction avoids ambiguous fractional-power differentiation: let \(z=w/(1-w)\) and \(H(z)=b^a z^a+d z^{a/2}+c^a\). Then \(P(w)^{1/a}=(1-w)H(z)^{1/a}\), and its second derivative is \((1-w)^{-3}(H^{1/a})''(z)\). Expanding its numerator gives
\[
\frac{z^{a/2}}4\big[(a-2)d\{b^a z^a+c^a\}+(4(a-1)(bc)^a-d^2)z^{a/2}\big],
\]
which, after the positive factors are restored, is precisely the stated \(K(w)\).

**Necessity below exponent two.** If \(1\leq a<2\) and \(d>0\), then \(K(w)\to(a-2)d c^a<0\) as \(w\downarrow0\). Therefore \(A''(w)<0\) on some interval and the function is not Pickands. For \(d=0\), the function is the classical asymmetric logistic/Tawn Pickands function: its curvature formula has \(K(w)=4(a-1)(bc)^a\{w(1-w)\}^{a/2}\geq0\) for every \(a\geq1\). This proves the zero-cross-term branch.

**Sharp condition for exponent at least two.** For \(a\geq2\) and \(d>0\), divide \(K(w)\) by the strictly positive \(\{w(1-w)\}^{a/2}\), and put \(r=(w/(1-w))^{a/2}>0\). Convexity is equivalent to nonnegativity, for *every* \(r>0\), of
\[
(a-2)d\left(b^a r+\frac{c^a}{r}\right)+4(a-1)(bc)^a-d^2.
\]
The AM–GM inequality gives the exact minimum \(2(a-2)d(bc)^{a/2}+4(a-1)(bc)^a-d^2\), attained at \(r=(c/b)^{a/2}\). This minimum factors as
\[
\big[2(a-1)(bc)^{a/2}-d\big]\big[d+2(bc)^{a/2}\big].
\]
The second factor is positive. Therefore nonnegative curvature on the whole interval is equivalent to \(d\leq2(a-1)(bc)^{a/2}\). When \(a>2\), at equality the AM–GM minimizer is unique and corresponds to \(w_*=c/(b+c)\); if \(d\) exceeds the threshold then curvature at that same point is strictly negative. When \(a=2\), the curvature bracket is independent of \(w\) after division, and at the threshold \(d=2bc\) the radical simplifies to \(bw+c(1-w)\), so \(A(w)=1\) identically. All cases are covered.

## Verification

The standalone `CHECK.py` uses exact symbolic algebra to verify the curvature numerator and sharp quadratic factorization, compares direct second derivatives for selected exact parameter values, checks an admissible parameter point outside the previously sufficient region, verifies critical curvature and strict postcritical failure at an asymmetric point, and checks the quadratic independence endpoint. Run `python CHECK.py` with Python 3 and SymPy. The global necessity and sufficiency for real \(a,b,c,d\) are proved above by algebra and AM–GM, not inferred from a finite numerical grid.

## Relationship to prior work

Chesneau (2024), Proposition 2, establishes the original MT2 construction for \(d=0\), or for \(a\geq2\), \(d>0\), and \(d^2\leq4(a-1)(bc)^a\). Its curvature factorization requires two separate nonnegative coefficients and thus supplies a sufficient rather than a necessary condition. Here the two terms are optimized together, yielding an exact necessary-and-sufficient criterion and exposing a larger admissible region. Chesneau (2023) discusses the classical Tawn and a symmetric mixed-power special case, not the exact four-parameter positive-cross-term domain. The Pickands characterization and the classical asymmetric logistic construction predate both.

## Limitations

The claim is limited to the specified nonnegative cross coefficient and positive marginal coefficients. It does not classify extensions allowing negative \(d\), vanishing \(b,c\), or dimensions above two. Existing general convexity theory is used, so the contribution is the sharp family-specific boundary rather than a new general characterization of copulas. An independent mathematical audit and a comprehensive historical-priority certification have not been performed.

## References

1. C. Chesneau, “On two new modified Tawn copulas,” *Model Assisted Statistics and Applications* 19 (2024), 35–48, first available online 1 February 2024. DOI: https://doi.org/10.3233/MAS-231451. See Proposition 2, equation (6), and Section 3.2.
2. C. Chesneau, “Current Developments on Extreme Value Copulas: Extended Pickands Dependence Functions,” *International Journal of Emerging Multidisciplinaries: Mathematics* 2 (2023), article 6. DOI: https://doi.org/10.59790/2790-3257.1036. See Table 1 and Section 2.
3. J. Pickands, “Multivariate extreme value distributions,” *Proceedings of the 43rd Session of the International Statistical Institute* 49 (1981), 859–878, 894–902.
4. J. A. Tawn, “Bivariate extreme value theory: models and estimation,” *Biometrika* 75 (1988), 397–415.
