# Exact quartic circle point evaluation and a strict eight-fold fourth-moment bound

## Finding
Let \(dm=d\theta/(2\pi)\) denote normalized Haar measure on \(\mathbb T\). For every complex polynomial \(P\) of degree at most four,
\[
\|P\|_{L^\infty(\mathbb T)}^4\le C_{4,4}\int_{\mathbb T}|P(z)|^4\,dm(z),
\]
where the **sharp** constant is
\[
C_{4,4}=Q(x_*,y_*)^{-1}=7.85084136369994627944\ldots<8.
\]
Here
\[
\begin{aligned}
Q(x,y)={}&70x^4+160x^3y-80x^3+168x^2y^2-144x^2y+36x^2\\
&+112xy^3-120xy^2+48xy-8x+70y^4-80y^3+36y^2-8y+1,
\end{aligned}
\]
and \((x_*,y_*)=(0.27125164797342481019\ldots,\,0.15751363732587504484\ldots)\) is the **unique real common solution** of
\[
\begin{aligned}
f(x,y)&=35x^3+60x^2y-30x^2+42xy^2-36xy+9x+14y^3-15y^2+6y-1=0,\\
g(x,y)&=20x^3+42x^2y-18x^2+42xy^2-30xy+6x+35y^3-30y^2+9y-1=0.
\end{aligned}
\]
The unique normalized optimizer at the evaluation point \(z=1\) is
\[
P_*(z)=x_*(1+z^4)+y_*(z+z^3)+(1-2x_*-2y_*)z^2.
\]
All nonzero equality cases are exactly the complex scalar multiples of \(P_*(\xi z)\) for \(|\xi|=1\).

An equivalent univariate algebraic specification uses the unique real root \(x_*\) of
\[
\begin{aligned}
R(x)={}&1486485x^9-2058210x^8+1342737x^7-545445x^6\\
&+152559x^5-30600x^4+4435x^3-453x^2+30x-1,
\end{aligned}
\]
contained in \((0.271251647973,0.271251647974)\), together with
\[
y_*=-\frac{13860x_*^5-13146x_*^4+4770x_*^3-868x_*^2+78x_*-3}{12474x_*^4-6405x_*^3+1242x_*^2-91x_*+2}.
\]
The denominator is positive at this root. This exact result also determines the sharp \(H^4(\mathbb D^2)\)-to-\(A^4(\mathbb D)\) norm of the diagonal restriction on homogeneous bidisc quartics:
\[
\kappa_4=(C_{4,4}/9)^{1/4}=0.96642559447899307467\ldots.
\]

## Assumptions and scope
All polynomial coefficients may be complex. The circle integral uses probability Haar measure and the essential supremum is the ordinary maximum. The disk \(A^4\) norm uses normalized planar area; the bidisc \(H^4\) norm uses product probability Haar measure. The statements apply to degree at most four for point evaluation and to homogeneous degree exactly four for the diagonal map. No claim is made for other polynomial degrees or other exponents.

## Proof
Fix a nonzero \(P\), rotate a point of maximum modulus to \(z=1\), then divide by its value there. Thus the optimal coefficient is the reciprocal of the minimum of \(\int|P|^4dm\) under \(P(1)=1\). In finite dimension this functional is coercive, so the affine minimization has a solution. Since \(w\mapsto |w|^4\) is strictly convex on \(\mathbb C\), distinct polynomials differ on a set of positive circle measure, and the minimizer is **unique**.

The operations \(P(z)\mapsto\overline{P(\bar z)}\) and \(P(z)\mapsto z^4P(1/z)\) preserve both \(P(1)=1\) and the fourth integral. Uniqueness forces the minimizer to have real palindromic coefficients \((x,y,1-2x-2y,y,x)\). Conversely every real pair \((x,y)\) gives a normalized polynomial of this form. Parseval applied to its square shows
\[
\int_{\mathbb T}|P(z)|^4dm(z)
=\sum_{k=0}^{8}\left|\sum_{\substack{0\le j\le4\\0\le k-j\le4}}a_ja_{k-j}\right|^2=Q(x,y).
\]
In particular \(Q\) is coercive and strictly convex on \(\mathbb R^2\). Exact differentiation gives \(\partial_xQ=8f\) and \(\partial_yQ=8g\). Therefore their common real stationary point exists and is unique, and attains the absolute minimum even among unrestricted complex polynomials.

For an optional single-variable algebraic certificate, exact elimination gives \(\operatorname{Res}_y(f,g)=-189R(x)\). The penultimate polynomial subresultant is \(63(A(x)y+B(x))\), where
\[
\begin{aligned}
A(x)&=12474x^4-6405x^3+1242x^2-91x+2,\\
B(x)&=13860x^5-13146x^4+4770x^3-868x^2+78x-3.
\end{aligned}
\]
A rational Sturm-chain calculation shows that \(R\) has exactly one real root, lying strictly between \(271251647973/10^{12}\) and \(271251647974/10^{12}\). The polynomial \(A\) has no root in that interval and is positive there. Exact polynomial division verifies that substituting \(y=-B/A\) makes both \(A^3f\) and \(A^3g\) divisible by \(R\). Thus this algebraic root yields the unique minimizer, not merely a numerical stationary point. Existence and uniqueness also follow independently from strict convexity.

The additional explicit inequality \(C_{4,4}<8\) has a small rational certificate. Take the three rational points
\[
v_1=(27/100,16/100),\quad v_2=(28/100,16/100),\quad v_3=(27/100,15/100)
\]
and weights \((\lambda_1,\lambda_2,\lambda_3)=(1004160,148115,345024)/1497299\). Exact differentiation verifies that every weight is positive, their sum is one, and \(\sum_j\lambda_j\nabla Q(v_j)=0\). By convexity, summing their three supporting hyperplanes gives, for **every** real \((x,y)\),
\[
Q(x,y)\ge\sum_j\lambda_j\bigl(Q(v_j)-\nabla Q(v_j)\cdot v_j\bigr)
=\frac{14888369619}{116976484375}>\frac18.
\]
It follows that \(C_{4,4}<8\). Since a normalized minimizer cannot exceed one in modulus anywhere else on the circle (otherwise rotation and renormalization contradict minimality), undoing the rotation gives exactly all stated equality cases.

Finally, a homogeneous bidisc quartic \(F(z,w)=\sum_{j=0}^4a_jz^{4-j}w^j\) satisfies \(\|F\|_{H^4}^4=\|P\|_{L^4}^4\), with \(P(t)=\sum a_jt^j\). Its diagonal restriction equals \(F(u,u)=P(1)u^4\), and normalized disk area has \(\int_{\mathbb D}|u|^{16}dA(u)=1/9\). The sharp diagonal ratio is consequently \(C_{4,4}/9\), attained by the same coefficient vector.

## Verification
Execute `python3 checker.py` with Python 3 and SymPy. The standalone script recomputes the ninth-degree fourth-moment polynomial directly from coefficient convolution, both exact gradients, the resultant and linear subresultant, the uniqueness of the real resultant root by a Sturm count, a strict rational enclosure, exact divisibility after recovering the second coefficient, and the three-hyperplane rational lower certificate. The script completed with `PASS`. Numerical approximations are supplementary: they are not the basis for global optimality, which follows from the analytic strict-convexity proof and exact algebra.

## Relationship to prior work
Instanes, *Point evaluation for polynomials on the circle* (arXiv:2509.22035v1, September 26, 2025; *Collectanea Mathematica*, 2026), defines these sharp constants, proves existence and structure of extremizers, proves nonsharp bounds for degrees through four, and explicitly treats optimized zeros numerically (Theorems 1, 14, 16 and Section 7). Its inspected complete open-access text does not give the exact \(d=4,p=4\) invariant or the ninth-degree optimizer. The published published-finding corpus finding *Exact fourth-power point-evaluation constant for quadratic circle polynomials* (October 25, 2026) solves \(d=2,p=4\), which neither determines nor bounds sharply the coupled degree-four invariant. Brevig, Gómez-Serrano, Ortega-Cerdà and Seip, *Contractivity of Rudin's diagonal restriction operator for \(H^p\) of the polydisc* (arXiv:2610.16227v1, October 12, 2026), proves general contractivity and point-evaluation bounds. Its abstract and a secondary discussion were accessible, but the primary full text could not be inspected; possible additional quantitative special cases remain an acknowledged priority risk.

## Limitations
The result is a finite-degree exact norm, not an all-degree Nikolskii inequality. The decimal values are rounded representations of precisely defined algebraic numbers. The rational certificate improves the general degree-four fourth-power bound but is not itself the sharp constant. Full inspection of the 2026 general contractivity paper was blocked by access, and older unindexed equivalent computations cannot be excluded.

## References
1. S. M. Instanes, *Point evaluation for polynomials on the circle*, arXiv:2509.22035v1 (2025), DOI: 10.1007/s13348-026-00516-z. https://link.springer.com/article/10.1007/s13348-026-00516-z
2. *Exact fourth-power point-evaluation constant for quadratic circle polynomials*, published-finding corpus, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-fourth-power-point-evaluation-constant-for-quadratic-circl--038070a4eb80
3. O. F. Brevig, J. Gómez-Serrano, J. Ortega-Cerdà, K. Seip, *Contractivity of Rudin's diagonal restriction operator for \(H^p\) of the polydisc*, arXiv:2610.16227v1 (2026). https://arxiv.org/abs/2610.16227
