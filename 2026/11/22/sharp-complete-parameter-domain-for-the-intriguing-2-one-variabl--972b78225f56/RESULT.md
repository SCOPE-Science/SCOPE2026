# Sharp complete parameter domain for the intriguing-2 one-variable-power copula

## Finding

The two-parameter function introduced as the *intriguing-2* (Int2) copula in Chesneau (2023),
\[
C_{\alpha,\gamma}(x,y)
=x\bigl[1+x^{\alpha}(y^{-1}-1)\bigr]^{-x^{-\gamma}},
\qquad 0<x,y\le1,
\]
has a copula extension to the unit square **if and only if** one of the following mutually exclusive parameter cases holds:

1. \(\gamma=0\) and \(-1\le\alpha\le1\).
2. \(\gamma>0\), \(-1<\alpha\le0\), and \(0<\gamma\le1+\alpha\).
3. \(\gamma>0\), \(0<\alpha\le1\), and \(\alpha\le\gamma\le1+\alpha\).
4. \(\gamma>0\), \(1<\alpha\le\alpha_{\rm c}\), and \(\alpha\le\gamma\le\Gamma(\alpha)\), where
\[
\alpha_{\rm c}=\frac1{1-\log2}=3.258891353270929454\ldots,
\]
and \(\Gamma(\alpha)\) is the **unique** solution \(\gamma\in[\alpha,1+\alpha)\) of
\[
1-\alpha+\gamma\log\left(\frac{2\alpha}{\gamma}\right)=0.
\]
At \(\alpha=\alpha_{\rm c}\), the solution is \(\Gamma(\alpha)=\alpha\); for \(1<\alpha<\alpha_{\rm c}\) it lies strictly between \(\alpha\) and \(1+\alpha\). No other real parameters give copulas.

For instance, \((\alpha,\gamma)=(2,5/2)\) is admissible, despite lying outside the original sufficient parameter box; the sharp upper boundary at shape \(\alpha=2\) is \(\Gamma(2)=2.797962307543087825\ldots\). Negative shapes \(-1<\alpha<0\) also produce valid copulas for the indicated positive exponents.

## Assumptions and scope

Parameters \(\alpha,\gamma\) are arbitrary real numbers. The expression is evaluated for \(0<x,y\le1\); define \(C(x,0)=C(0,y)=0\) and use the specified margins for the remaining boundary points. This extension is continuous because \(0\le C(x,y)\le x\), and because for each fixed \(x>0\), \(C(x,y)\to0\) as \(y\downarrow0\). Throughout, \(\log\) is the natural logarithm.

The result concerns exact two-increasing copula admissibility, not merely pointwise nonnegativity or a finite-grid numerical test. The variable substitution below covers all \(w\ge0\) at every interior \(x>0\), so it loses no possible negative-density region.

## Proof

**1. Margins and the density factor.** The formulas immediately give \(C(x,1)=x\) and \(C(1,y)=y\). For \(0<x,y<1\) put
\[
k=x^{-\gamma},\qquad w=x^{\alpha}(y^{-1}-1),\qquad
L=1+\alpha-\gamma+\gamma k\log(1+w)
-\alpha(k+1)\frac{w}{1+w}.
\]
Direct differentiation, retaining the positive factor, gives
\[
C_y=xk x^{\alpha}y^{-2}(1+w)^{-k-1}>0,
\qquad C_{xy}=\frac{C_y}{x}\,L.
\]
Thus \(C\) is a copula exactly when \(L\ge0\) throughout the open unit square: nonnegative continuous mixed density proves two-increasingness by integration; conversely a strictly negative mixed density at any interior point gives a rectangle of negative probability. Boundary evaluations of \(L\) below yield interior counterexamples by continuity.

**2. Nonpositive \(\gamma\).** If \(\gamma<0\), fix \(x\in(0,1)\) (hence a fixed positive \(k\)) and let \(w\to\infty\). The term \(\gamma k\log(1+w)\) tends to negative infinity, while the rational term stays bounded. Thus \(\gamma<0\) is impossible.

For \(\gamma=0\), \(k=1\) and
\[
L=1+\alpha-2\alpha\frac{w}{1+w}.
\]
The infimum over \(w\ge0\) is \(1-|\alpha|\), giving the first case, including both endpoints.

**3. Positive \(\gamma\), nonpositive \(\alpha\).** For \(\gamma>0\) and \(\alpha\le0\), both \(\gamma k\log(1+w)\) and \(-\alpha(k+1)w/(1+w)\) are nonnegative. They vanish at \(w=0\), so the exact infimum of \(L\) is \(1+\alpha-\gamma\). This is nonnegative exactly in the second case.

**4. Excluding \(\gamma<\alpha\) for positive \(\alpha\).** Suppose \(\gamma>0\), \(\alpha>\gamma\). For \(k\to\infty\) and fixed \(w=\alpha/\gamma-1>0\), the coefficient of \(k\) in \(L\) equals
\[
\gamma\log\left(\frac\alpha\gamma\right)
-\alpha\left(1-\frac\gamma\alpha\right)
=-\gamma\left[\frac\alpha\gamma-1-\log\left(\frac\alpha\gamma\right)\right]<0.
\]
Consequently \(L\to-\infty\) for interior values of \(x,y\). Necessarily \(\gamma\ge\alpha\).

**5. Minimization over the entire support.** Suppose \(\gamma\ge\alpha>0\). For fixed \(k=x^{-\gamma}\ge1\),
\[
\frac{\partial L}{\partial w}
=\frac{\gamma k(1+w)-\alpha(k+1)}{(1+w)^2}.
\]
Let \(r=\alpha/\gamma\le1\) and \(z_k=r(1+k^{-1})\). If \(z_k\le1\), the minimum is at \(w=0\) and equals \(1+\alpha-\gamma\). If \(z_k>1\), it is attained at \(w=z_k-1\) and equals
\[
1+\alpha-\gamma-\gamma k\bigl(z_k-1-\log z_k\bigr).
\]
On the range \(z_k>1\), differentiation shows
\[
\frac{d}{dk}\Bigl[k(z_k-1-\log z_k)\Bigr]
=r\left(1-\frac1{z_k}\right)-\log z_k<0,
\]
because \(r\le1\) and \(\log z>1-z^{-1}\) for every \(z>1\). Thus the worst negative correction occurs at \(k=1\), the boundary limit \(x\uparrow1\). It follows that the exact infimum over \(x,y\) is
\[
\inf L=\begin{cases}
1+\alpha-\gamma,&\gamma\ge2\alpha,\\
1-\alpha+\gamma\log(2\alpha/\gamma),&\alpha\le\gamma<2\alpha.
\end{cases}
\]
This formula is exact, including \(\gamma=2\alpha\) by continuity. When the infimum is negative at the boundary \(k=1\), continuity gives a negative value at some finite \(k>1\) and \(w>0\).

**6. Solving the phase boundaries.** If \(0<\alpha\le1\), the second branch is nonnegative whenever \(\alpha\le\gamma<2\alpha\), because \(1-\alpha\ge0\) and the logarithm is positive. The first branch requires \(\gamma\le1+\alpha\); since \(2\alpha\le1+\alpha\), this yields precisely case 3.

If \(\alpha>1\), \(\gamma\ge2\alpha\) is invalid since \(1+\alpha-\gamma<0\). On \(\gamma\in[\alpha,2\alpha)\) let
\[
H_\alpha(\gamma)=1-\alpha+\gamma\log(2\alpha/\gamma).
\]
Here \(H_\alpha'(\gamma)=\log(2\alpha/\gamma)-1\le\log2-1<0\). At the lower endpoint, \(H_\alpha(\alpha)=1-\alpha(1-\log2)\), which is nonnegative exactly for \(\alpha\le\alpha_{\rm c}\). At \(\gamma=1+\alpha<2\alpha\), the minimizer has positive \(w\), so \(H_\alpha(1+\alpha)<1+\alpha-(1+\alpha)=0\). By strict monotonicity and continuity there is exactly one zero \(\Gamma(\alpha)\) on \([\alpha,1+\alpha)\) when \(1<\alpha\le\alpha_{\rm c}\); the inequality \(H_\alpha(\gamma)\ge0\) is equivalent to \(\gamma\le\Gamma(\alpha)\). This proves case 4 and rules out larger \(\alpha\).

All possible parameter cases are exhausted, proving necessity and sufficiency.

## Verification

The included `checker.py` uses symbolic differentiation to independently verify the stated factorization and a deterministic high-precision calculation of \(\alpha_{\rm c}\) and several \(\Gamma(\alpha)\) values. It also tests sample parameter points and numerical mixed derivatives, without treating sampling as proof. Run `python checker.py` with Python 3, SymPy and mpmath installed. Analytic steps 1–6, not the finite tests, establish the global classification.

## Relationship to prior work

Chesneau, *Axioms* **12** (2023), 392, Proposition 7, introduced this exact function and established copula validity on the sufficient region \(0<\alpha\le\gamma\le1\); the article also noted separately that \(\gamma=0\) works for \(0\le\alpha\le1\). The current theorem addresses the **same formula** but proves a necessary-and-sufficient region over all real parameters. It adds negative-shape copulas, a larger positive-exponent band, shapes above one, and the sharp logarithmic terminal boundary \(\alpha_{\rm c}\). These enlargements are not implied by a merely sufficient proposition.

Related modified Ali–Mikhail–Haq constructions alter different analytic formulas and are not interchangeable with this exact Int2 family. A 2024 related paper was available by abstract but not complete full text in the source access used for this comparison; no novelty claim is based solely on its abstract.

## Limitations

This result classifies validity of this specific family only; it does not assert the maximality of any dependence coefficient, new estimation results, or extensions to arbitrary variable-power formulas. The shape cutoff and logarithmic boundary are derived for real parameters; numerical decimal values are approximations of exactly defined constants. Published-literature priority cannot be certified exhaustively: unpublished, unindexed, or inaccessible results may contain equivalent statements. No independent mathematical audit has been carried out.

## References

1. C. Chesneau, “Theoretical Validation of New Two-Dimensional One-Variable-Power Copulas,” *Axioms* **12** (2023), 392, Proposition 7, https://doi.org/10.3390/axioms12040392 (published 18 April 2023).
2. C. Chesneau, “Exploring Two Modified Ali-Mikhail-Haq Copulas and New Bivariate Logistic Distributions,” *Pan-American Journal of Mathematics* **3** (2024), article 4, https://doi.org/10.28919/cpr-pajm/3-4 (related, distinct formulas; only abstract accessible during comparison).
