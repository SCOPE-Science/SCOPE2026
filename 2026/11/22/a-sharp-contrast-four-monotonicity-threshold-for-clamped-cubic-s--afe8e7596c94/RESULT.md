# A sharp contrast-four monotonicity threshold for clamped cubic splines

## Finding
Let \(S\) be the unique \(C^2\) piecewise-cubic interpolant of four increasing ordinates at four knots, subject to zero first derivative at both endpoints. On equally spaced knots, write the three positive vertical increments as \(a,b,c\), and put \(\rho=\max(a,b,c)/\min(a,b,c)\). **Every** increasing dataset with \(\rho\le4\) has a nondecreasing interpolant. This threshold is sharp: for each \(\rho>4\), the data increments \((1,\rho,1)\) produce endpoint-adjacent decrease, whereas \((\rho,1,\rho)\) produce a central decreasing pocket.

Among all *reflection-symmetric* four-knot grids whose three successive lengths are proportional to \((h,1,h)\), \(h>0\), the equally spaced grid is uniquely best for the worst-case class \(\rho\le R\): no such grid preserves monotonicity for **every** dataset of contrast \(R>4\), and for each \(h\ne1\) it already fails for some contrast \(R<4\). This is an optimality statement within reflection-symmetric grids; no assertion is made about unrestricted asymmetric grids or five or more knots.

At the sharp uniform-grid boundary, these two mechanisms have distinct quantitative onset laws. For increments \((1/4-\varepsilon,1,1/4-\varepsilon)\), the negative endpoint undershoot is \(\frac{4096}{125}\varepsilon^3+O(\varepsilon^4)\). For \((4+\varepsilon,1,4+\varepsilon)\), the decrease between the central local maximum and minimum is \(\frac{1}{3\sqrt6}(3\varepsilon/5)^{3/2}+O(\varepsilon^{5/2})\) as \(\varepsilon\downarrow0\). These are vertical deviations, with the central increment normalized to one.

## Assumptions and scope
All knots are strictly ordered and the ordinates strictly increasing. Affine shifts of the ordinates and positive common rescalings of both coordinates do not affect the contrast criterion. For the uniform case, take knots \(0,1,2,3\) and ordinates \(0,a,a+b,a+b+c\), where \(a,b,c>0\). The cubic spline is specified by interpolation, global \(C^2\) continuity and \(S'(0)=S'(3)=0\); it exists uniquely. For the grid-design comparison, take knots \(0,h,h+1,2h+1\), again with vertical increments \(a,b,c\) and flat endpoint derivatives.

The word monotone means nondecreasing on the *whole closed interval*. At equality \(\rho=4\), a derivative may vanish at an interior point or to higher order at an endpoint, yet the spline remains strictly increasing as a function.

## Proof
**Derivative reduction.** Use the standard cubic Hermite basis on an interval of length \(\ell\):
\[
H_{00}=2t^3-3t^2+1,\quad H_{01}=-2t^3+3t^2,\quad H_{10}=t^3-2t^2+t,\quad H_{11}=t^3-t^2,
\]
with \(t\in[0,1]\). For the uniform mesh let \(m_1=S'(1)\), \(m_2=S'(2)\). Continuity of the second derivative gives \(4m_1+m_2=3(a+b)\) and \(m_1+4m_2=3(b+c)\). Thus
\[
m_1=(4a+3b-c)/5,\qquad m_2=(-a+3b+4c)/5.
\]
The derivative on the first cell, in its local coordinate \(t\), equals
\[
S_1'(t)=\frac{t}{5}\left[2(11-9t)a+3(3t-2)b-(3t-2)c\right].
\]
The derivative on the middle cell equals
\[
S_2'(t)=\frac15\left[(9t^2-14t+4)a+(-12t^2+12t+3)b+(9t^2-4t-1)c\right].
\]
The derivative on the last cell is obtained by reflecting the first and swapping \(a,c\).

**Uniform contrast-four certificate.** Normalize \(\min(a,b,c)=1\). If \(\rho\le4\), then all increments lie in \([1,4]\). Each displayed derivative is affine in \((a,b,c)\); its minimum on that cube is therefore attained at a vertex. For the first cell, the coefficient of \(a\) is positive, and the coefficients of \(b,c\) have opposite signs, switching at \(t=2/3\). The exact minimum over the cube is \(3t^2\) for \(0\le t\le2/3\) and \(t(24-21t)/5\) for \(2/3\le t\le1\), both nonnegative.

For the middle cell set \(\alpha=(7-\sqrt{13})/9\) and \(\beta=(2+\sqrt{13})/9\). The coefficient of \(b\) is positive throughout, while those of \(a,c\) change sign at \(\alpha,\beta\), respectively. The exact minimum over the cube is, in the three respective regions,
\[
\begin{cases}
3(11t^2-6t+1)/5,&0\le t\le\alpha,\\
3(2t-1)^2,&\alpha\le t\le\beta,\\
3(11t^2-16t+6)/5,&\beta\le t\le1.
\end{cases}
\]
The outer quadratics have negative discriminant and positive leading coefficients; the central expression is a square. Reflection handles the last cell. Hence \(S'\ge0\) everywhere for all data of contrast at most four.

**Sharpness and mesh optimality.** For uniform increments \((1,R,1)\), the interior derivatives both equal \(3(1+R)/5\). When \(R>4\), the first-cell derivative is negative immediately to the right of its left endpoint. For \((R,1,R)\), the midpoint derivative on the middle cell is \((3-m_1)/2<0\), proving a second witness.

For symmetric spacing \((h,1,h)\) and symmetric vertical increments \((r,1,r)\), continuity gives the two equal interior first derivatives
\[
m=\frac{3(r/h+h)}{3h+2}.
\]
An outer cell with derivatives \((0,m)\) is monotone exactly when \(0\le m\le3r/h\). The middle cell, with derivatives \((m,m)\) and increment one, is monotone exactly when \(0\le m\le3\). Therefore the *exact* monotonicity condition for this symmetric-data subfamily is
\[
\frac{h^2}{3h+1}\le r\le2h(h+1).
\]
A symmetric mesh that is robust for *all* increments with contrast at most \(R\ge1\) must in particular handle symmetric data with \(r\in[1/R,R]\). Hence
\[
R\le \min\left\{2h(h+1),\frac{3h+1}{h^2}\right\}.
\]
The first bound increases strictly with \(h\), the second decreases strictly, and they equal four only at \(h=1\). Thus every other symmetric grid has a strictly smaller admissible contrast ceiling, while the uniform grid attains four for all data by the preceding certificate.

**Boundary loss laws.** For the uniform symmetric data \((r,1,r)\), the interior derivative is \(m=3(r+1)/5\). When \(r<1/4\), let \(e=m/r-3=3(1-4r)/(5r)>0\). On the left cell, the local polynomial is \(S(t)=r[-e t^2+(1+e)t^3]\); its exact negative minimum equals \(-4re^3/[27(1+e)^2]\) at \(t=2e/[3(1+e)]\). Expanding at \(r=1/4-\varepsilon\) gives the stated cubic undershoot.

When \(r>4\), put \(d=m-3=3(r-4)/5>0\). On the middle cell the derivative in \(u=t-1/2\) is \(-d/2+(12+6d)u^2\). Its zeros are at \(u=\pm\sqrt{d/(24+12d)}\); the exact drop between them equals \((2d/3)\sqrt{d/(24+12d)}\), yielding the \(3/2\)-power law.

## Verification
Run \(\texttt{python3 verify.py}\) beside this document, using only the standard library. The checker verifies the \(C^2\) linear equations with exact rational arithmetic, checks boundary witnesses and symmetric-mesh inequalities at exact rational points, and supplements the universal proof with exact-rational derivative samples. All infinite and uniform assertions are proved by the analytic sign certificates above, not by the finite tests. Its execution output is included as \(\texttt{verify-output.txt}\).

## Relationship to prior work
Fritsch and Carlson (1980) give general necessary-and-sufficient monotonicity conditions for a *single cubic Hermite interval*, and describe a \(C^1\) monotonicity-adjusting interpolation algorithm. Their generic criterion supports the background but does not assert a universal four-knot \(C^2\), flat-endpoint, all-data contrast bound, a mesh optimization or the two explicit failure laws. Saeidian et al. (2021) study constrained cubic Hermite interpolation with \(C^2\) constraints and numerical optimization, rather than sharp contrast robustness of the prescribed clamped spline. Related four-node polynomial/rational range-defect and natural-cubic total-variation results concern different operators, boundary conditions or losses. The exact robust contrast and mesh-optimality statements are the claim here, not the established one-interval Hermite formulas.

## Limitations
No guarantee is made for larger datasets, different end slopes, unrestricted asymmetric mesh design, or arbitrary \(C^1\) shape-preserving Hermite interpolation. The uniform bound is sufficient for all increasing data, not a necessary condition for each individual data triple. A complete historical priority search of all spline monographs and unpublished treatments is not claimed; independent validation has not been performed. The first two limiting laws concern the specified symmetric witness families, not every direction of approach to the feasibility boundary.

## References
- F. N. Fritsch and R. E. Carlson, *Monotone Piecewise Cubic Interpolation*, SIAM J. Numer. Anal. 17 (1980), 238–246. https://doi.org/10.1137/0717021
- J. Saeidian, M. Sarfraz, A. Azizi, S. Jalilian, and N. Tang, *A New Approach of Constrained Interpolation Based on Cubic Hermite Splines*, Journal of Mathematics (2021), article 5925163, first published 2021-08-31. https://doi.org/10.1155/2021/5925163
- F. N. Fritsch and J. Butland, *A Method for Constructing Local Monotone Piecewise Cubic Interpolants*, SIAM J. Sci. Stat. Comput. 5 (1984), 300–304. https://doi.org/10.1137/0905021
