# Two sharp mode-collapse thresholds for a four-source Poisson extension

## Finding
Let \(h>0\) and consider the harmonic Poisson extension of four equal positive boundary point masses at \(-3,-1,1,3\):
\[
U_h(x)=\frac{h}{\pi}\sum_{a\in\{-3,-1,1,3\}}\frac{1}{(x-a)^2+h^2},\qquad x\in\mathbb R.
\]
Put \(q=h^2\). There are exactly two distinct critical values \(0<q_{\mathrm f}<q_{\mathrm c}\), defined as the unique positive roots of
\[
H(q)=123245q^5-361571q^4+965120q^3+1003680q^2-3075840q-2633472,
\]
\[
Q(q)=q^4+42q^2-40q-1107.
\]
They are \(q_{\mathrm f}=1.888599554243986\ldots\) and \(q_{\mathrm c}=4.537308167671079\ldots\). The exact number of distinct strict local maxima of \(x\mapsto U_h(x)\) is **four** when \(0<q<q_{\mathrm f}\), **two** when \(q_{\mathrm f}\le q<q_{\mathrm c}\), and **one** when \(q\ge q_{\mathrm c}\). In particular, three maxima never occur. At \(q=q_{\mathrm f}\), a symmetric pair of outer maxima annihilates with adjacent minima through two nonextremal stationary shoulders; at \(q=q_{\mathrm c}\), the two surviving maxima coalesce into a quartically flat strict central maximum.

## Assumptions and scope
Four *equal* point masses at the specified locations; a common positive Poisson height; local maxima along the horizontal coordinate \(x\) only. Global multiplicative scaling does not affect mode counts. The result does not classify arbitrary four-point supports or unequal masses, and makes no assertion about the number of critical points in the full two-dimensional upper half-plane.

## Proof
Write \(u=x^2\), \(q=h^2\), and ignore the positive factor \(h/\pi\). Combining each pair of symmetric sources gives
\[
 F(u,q)=\sum_{a\in\{1,9\}}\frac{2(u+a+q)}{D_a(u,q)},\quad
 D_a=u^2+2(q-a)u+(q+a)^2>0\quad(u\ge0,q>0).
\]
Define
\[
 N_a(u,q)=(q+a)(3a-q)-2(q+a)u-u^2,\qquad
 E(u,q)=N_1D_9^2+N_9D_1^2.
\]
Direct differentiation gives \(\partial_x F(x^2,q)=4xE(x^2,q)/(D_1^2D_9^2)\). Therefore positive stationary abscissae correspond exactly to positive real roots of the degree-six polynomial \(E(\cdot,q)\). Its leading coefficient in \(u\) is \(-2\); the central derivative coefficient and the parameter discriminant are the exact identities
\[
 E(0,q)=-2(q+1)(q+9)Q(q),
\]
\[
 \operatorname{disc}_u E=664082786653543858176(q+1)^5(q+4)^4(q+9)H(q).
\]
The quintic \(H\) has exactly one positive zero. Indeed, \(H''(q)=4[q(616225q^2-1084713q+1447680)+501840]>0\) for \(q\ge0\), because the displayed quadratic has negative discriminant and positive leading coefficient. Thus \(H'\) strictly increases; together with \(H(0)<0\), \(H(1)<0<H(2)\), and \(H(q)\to\infty\), strict convexity forces one positive crossing. Similarly \(Q''=12q^2+84>0\), \(Q(0)<0\), and \(Q(4)<0<Q(5)\) imply one positive zero, with \(q_{\mathrm f}\in(1,2)\) and \(q_{\mathrm c}\in(4,5)\).

For exact root counts, apply the classical Sturm sign-variation rule to \(E(u,q)\) in \(u\) at \(u=0\) and \(u=+\infty\). At the three rational parameter values the respective pairs \((V(0),V(+\infty))\) are
\[
 q=1:(4,1),\qquad q=2:(3,2),\qquad q=5:(2,2).
\]
Thus the numbers of *positive* roots are \(3,1,0\), respectively. The enclosed standalone exact-symbolic checker constructs the polynomial, verifies the entire discriminant identity, and recomputes these Sturm counts without floating-point root classification. Since no multiple root occurs for positive \(q\) except \(q_{\mathrm f}\), and no root can pass through zero except at \(q_{\mathrm c}\), these three counts hold throughout the three intervening open intervals. No roots escape to infinity because the leading coefficient of \(E\) is the fixed nonzero number \(-2\).

For \(q<q_{\mathrm c}\), \(E(0,q)>0\), whereas \(E(u,q)<0\) for large \(u\). Three simple positive roots alternate maxima–minima–maxima along \(x>0\); one simple positive root gives one right-hand maximum. Reflection doubles these maxima. For \(q>q_{\mathrm c}\), the derivative on \(x>0\) has no zeros and is negative, giving one central maximum. At \(q_{\mathrm f}\), the change of root count from three to one and the simple parameter-discriminant zero force one simple positive root and one ordinary positive double root; a double zero of \(E\) is stationary but nonextremal. At \(q_{\mathrm c}\), a simple positive root passes through \(u=0\); the fact that \(H(q_{\mathrm c})\ne0\) makes this zero simple in \(u\). Its derivative sign is negative at the crossing, so the central maximum has a strictly negative fourth-order coefficient and is quartically flat. This settles both boundaries.

## Verification
Run \(\texttt{python3 verify.py}\) with SymPy. The script checks the derivative identity, discriminant factorization, center-root identity, threshold uniqueness algebra, and independent exact Sturm root counts at three rational parameter witnesses. Reported critical heights are \(h_{\mathrm f}=\sqrt{q_{\mathrm f}}\approx1.3742632769\) and \(h_{\mathrm c}=\sqrt{q_{\mathrm c}}\approx2.1300958119\). Decimal approximations are not used to prove any infinite statement.

## Relationship to prior work
The four-source Poisson extension is a common-scale four-component Cauchy mixture up to normalization. Kalantan–Einbeck (2019) examine parameter estimation for such mixtures, including a four-component simulation with unequal weights and widths, not the exact mode-transition algebra for this symmetric configuration. Ruzgas–Lukauskas–Čepkauskas (2021) investigate nonparametric Cauchy-mixture density estimation, not a sharp four-source modal classification. Došlá (2009) treats criteria for mixtures of **two** unimodal densities, including two Cauchy laws; a two-component statement alone cannot imply the four-source sextic root diagram. A separately indexed three-equally-spaced-source Poisson calculation has a single threshold \(h=1/\sqrt2\), a genuinely different configuration. No checked statement was found to contain or imply the present pair of critical polynomials, although absence of an indexed match does not establish historical priority.

## Limitations
The exact classification is specific to the symmetric four-point support and equal positive masses. There is no claimed formula for arbitrary weights, spacing, or higher-dimensional modes. Prior literature may contain an equivalent four-component Cauchy modality theorem not captured by the searched full texts or indexed records; independent historical-priority verification remains open. Independent mathematical audit has not been performed.

## References
1. Z. I. Kalantan and J. Einbeck, *Quantile-Based Estimation of the Finite Cauchy Mixture Model*, Symmetry **11** (2019), 1186, https://doi.org/10.3390/sym11091186 (first publicly dated 2019-09-19).
2. T. Ruzgas, M. Lukauskas and G. Čepkauskas, *Nonparametric Multivariate Density Estimation: Case Study of Cauchy Mixture Model*, Mathematics **9** (2021), 2717, https://doi.org/10.3390/math9212717.
3. Š. Došlá, *Conditions for bimodality and multimodality of a mixture of two unimodal densities*, Kybernetika **45** (2009), 279–292, https://www.dml.cz/handle/10338.dmlcz/140075.
