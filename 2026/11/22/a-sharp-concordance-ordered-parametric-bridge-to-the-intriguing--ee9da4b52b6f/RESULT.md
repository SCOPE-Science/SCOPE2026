# A sharp concordance-ordered parametric bridge to the intriguing-1 copula

## Finding

For a real parameter \(\gamma\), define \(a_\gamma(x)=1+\gamma(1-x)/x\) for \(0<x<1\), and set
\[
C_\gamma(x,y)=x\left[1+y(1-x)^{a_\gamma(x)}-(1-xy)^{a_\gamma(x)}\right],\qquad 0<x<1,\quad 0\le y\le1.
\]
Extend by continuity at \(x=0\) and \(x=1\). Then **\(C_\gamma\) is a bivariate copula if and only if \(0\le\gamma\le1\)**. Within this exact domain, \(C_0(x,y)=xy\) is independence and \(C_1\) is the original intriguing-1 (Int1) copula of Chesneau (2023).

Moreover, if \(0\le\gamma_1<\gamma_2\le1\), then
\[
C_{\gamma_1}(x,y)<C_{\gamma_2}(x,y)\qquad (0<x<1,\ 0<y<1).
\]
Thus the bridge is strictly ordered by positive quadrant dependence and by Spearman's rho: the latter varies continuously and strictly from zero to its value for the published Int1 endpoint.

## Assumptions and scope

The coordinates \(x,y\) range over the full closed unit square. The exponent is evaluated on the open \(x\)-interval and the boundary values are continuous limits; no integer or asymptotic approximation of the exponent is used. A copula means a grounded two-increasing distribution function on the unit square with uniform margins. Parameters outside the exact interval are considered as formal analytic expressions, not probability models.

The construction is the natural affine interpolation of the exponent \(1\) (producing independence) and the published Int1 exponent \(1/x\):
\[
a_\gamma(x)=(1-\gamma)+\gamma/x.
\]
It is generally **not** the affine mixture of the endpoint copulas.

## Proof

**Margins and continuity.** For any fixed real \(\gamma\) the open-square formula is smooth. Direct evaluation gives \(C_\gamma(x,0)=0\) and \(C_\gamma(x,1)=x\). Since \(a_\gamma(1)=1\), the limit at \(x=1\) is \(C_\gamma(1,y)=y\). As \(x\downarrow0\),
\[
(1-x)^{a_\gamma(x)}\longrightarrow e^{-\gamma},\qquad
(1-xy)^{a_\gamma(x)}\longrightarrow e^{-\gamma y};
\]
the square-bracketed quantity remains bounded uniformly for \(0\le y\le1\), so \(C_\gamma(0,y)=0\) continuously. Hence all marginal conditions hold for every real parameter, and the remaining question is two-increasingness.

**Sufficiency.** Fix \(0\le\gamma\le1\) and \(0<x<1\). Put
\[
s=1-x,\quad t=1-xy,\quad b=\frac{\gamma s}{x},\quad q=\gamma+(1-\gamma)x=xa_\gamma(x).
\]
Then \(0<s\le t\le1\), \(b\ge0\), and the derivative in \(y\) is
\[
\partial_y C_\gamma=x s^{b+1}+xq t^b.
\]
Write \(c_\gamma=\partial_x\partial_y C_\gamma=D_1+D_2\), where direct differentiation (using \(b'=-\gamma/x^2\)) gives
\[
D_1=s^b\left(s-q-\frac{\gamma s}{x}\log s\right),
\]
\[
D_2=t^b\left[\gamma+2(1-\gamma)x+\frac{\gamma q}{x}L_s(t)\right],\qquad
L_s(t)=-\log t-\frac{s(1-t)}{t}.
\]
For \(s\le t\le1\), \(L_s(1)=0\) and \(L_s'(t)=(s-t)/t^2\le0\), so \(L_s(t)\ge0\). Also \(\gamma+2(1-\gamma)x\ge0\) and \(t^b\ge s^b\). Consequently
\[
D_2\ge s^b[\gamma+2(1-\gamma)x]
\]
and therefore
\[
\boxed{c_\gamma(x,y)\ge s^b\left[1-\gamma x-\frac{\gamma s}{x}\log s\right]>0.}
\]
Indeed \(\log s<0\) and \(1-\gamma x>0\) for \(0<x<1\), \(0\le\gamma\le1\). By integrating this strictly positive mixed density over rectangles, and using the continuous margins, \(C_\gamma\) is a copula. No finite discretization of the unit square is involved.

**Sharpness above one.** For any fixed real \(\gamma\), the formula for the mixed derivative has the one-sided boundary limit
\[
\lim_{x\uparrow1}c_\gamma(x,0)=1-\gamma.
\]
If \(\gamma>1\) this is negative. By continuity at interior points near \((1,0)\), a strictly negative-density open rectangle exists, violating two-increasingness.

**Sharpness below zero.** For each fixed \(0<y<1\), the other boundary limit is
\[
\lim_{x\uparrow1}c_\gamma(x,y)=1-\gamma-\gamma\log(1-y).
\]
For every \(\gamma<0\), this tends to \(-\infty\) as \(y\uparrow1\). Choose a fixed interior \(y\) making it negative, then choose \(x<1\) sufficiently close to one. The mixed density is negative on an open neighborhood, ruling out a copula. This proves necessity of \(\gamma\ge0\) and completes the exact parameter classification.

**Strict dependence ordering.** For \(0\le\gamma\le1\), let \(a=a_\gamma(x)\ge1\). Since \(t=(1-y)+ys\), strict convexity of \(u\mapsto u^a\) when \(a>1\) yields
\[
C_\gamma(x,y)-xy=x\left[(1-y)+ys^a-t^a\right]>0
\]
for \(\gamma>0\) and interior \(x,y\). For the stronger parameter order define
\[
h_a(u)=\frac{u^a(-\log u)}{1-u}=u^{a-1}\frac{-u\log u}{1-u}.
\]
The function \(h_1\) is strictly increasing on \((0,1)\), since
\[
h_1'(u)=\frac{-\log u-1+u}{(1-u)^2}>0.
\]
Thus \(h_a\) is strictly increasing for every \(a\ge1\). Using \(y=(1-t)/(1-s)\), differentiation in the parameter gives
\[
\partial_\gamma C_\gamma(x,y)
=s(1-t)[h_a(t)-h_a(s)]>0
\]
for interior \(x,y\). This proves the strict pointwise copula order. Integrating the strict inequalities in the identity \(\rho_S(C)=12\int_0^1\int_0^1 C(x,y)\,dx\,dy-3\) proves the strictly increasing Spearman coefficient. Continuity in \(\gamma\) follows by dominated convergence because valid copulas lie in \([0,1]\).

## Verification

The proof explicitly handles the entire continuous unit square, both sharp excluded sides, and strict ordering. The accompanying standalone `check_int1.py` reproducibly verifies the derivative identities by high-precision numerical differentiation, the explicit global density lower bound at randomized interior points, the parameter ordering, and concrete invalidity witnesses. At 60-digit working precision, its current fixed-seed run passed 3614 supporting checks. These checks are finite diagnostics, not substitutes for the infinite-domain proof.

Run with Python 3 and the `mpmath` and `sympy` packages: `python check_int1.py`.

## Relationship to prior work

Chesneau, *Theoretical Validation of New Two-Dimensional One-Variable-Power Copulas* (2023), Proposition 6, proves validity of the parameter-free Int1 endpoint \(C_1\) and expressly notes its lack of tuning parameters. The paper's Lemma 1, Function 5, also uses the exponent \(1+\gamma(1/x-1)\), but **for the different model** \(xy^{1+\gamma(1/x-1)}\), not for the Int1 power-chord construction studied here. Neither assertion yields the present family-wide two-increasingness, its converse outside \([0,1]\), or its strict dependence order. The 2023 ratio-scheme copula families of Chesneau have different functional forms and do not imply this result.

The new statement is an exact classification of a concrete, motivated parameterization of an established parameter-free copula; it is not an assertion that arbitrary power-chord constructions are copulas. Published mathematical literature and relevant comparable findings were searched by formula, aliases, source and implication. No direct coverage was identified; absence of a match is not a proof of historical priority.

## Limitations

The theorem does not address statistical estimators, finite-sample efficiency, optimal model fit, higher-dimensional extensions, or arbitrary exponent functions. It establishes a strict concordance order only inside the admissible parameter interval and does not assert likelihood-ratio or total-positivity ordering. Originality remains conditional on coverage of the accessible literature; an independent mathematical audit has not been performed.

## References

1. C. Chesneau (2023). *Theoretical Validation of New Two-Dimensional One-Variable-Power Copulas*. **Axioms** 12(4), 392. Published 18 April 2023. https://doi.org/10.3390/axioms12040392 — see Theorem 1, Lemma 1 (Function 5) and Proposition 6 (Int1).
2. C. Chesneau (2023). *A Collection of Two-Dimensional Copulas Based on an Original Parametric Ratio Scheme*. **Symmetry** 15(5), 977. Published 25 April 2023. https://doi.org/10.3390/sym15050977 — different rational family.
3. C. Chesneau (2023). *Theoretical Advancements on a Few New Dependence Models Based on Copulas with an Original Ratio Form*. **Modelling** 4(2), 102–132. Published 29 March 2023. https://doi.org/10.3390/modelling4020008 — different ratio-polynomial/logarithmic constructions.
