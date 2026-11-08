# Sharp all-power geodesic-distance aspect ratios for fixed-area flat cylinders

## Finding
Let \(C_{c,h}=\big(\mathbb R/c\mathbb Z\big)\times[0,h]\) be the flat circular cylinder's lateral surface, with circumference \(c>0\), height \(h>0\), and Riemannian area \(A=ch\). For two independent area-uniform points, let \(D\) be their intrinsic shortest-path distance, and put \(q=c/(2h)\). For every real \(p>0\), the normalized moment \(\mathbb E[D^p]/A^{p/2}\) has a **unique** minimizing aspect ratio \(q_p\in(0,1)\). Its exact characterization is the unique positive solution of
\[
\int_0^1\!\int_0^1 2(1-v)\big(q u^2-q^{-1}v^2\big)\big(q u^2+q^{-1}v^2\big)^{p/2-1}\,du\,dv=0.
\]
The first two even-power optimizers are distinct and algebraic:
\[
q_2=\frac1{\sqrt2},\qquad q_4=3^{-1/4}.
\]
Their sharp normalized minimum moments are
\[
\min\frac{\mathbb E[D^2]}A=\frac1{3\sqrt2},\qquad
\min\frac{\mathbb E[D^4]}{A^2}=\frac1{10\sqrt3}+\frac1{36}.
\]
The large-power optimal aspect ratio has a sharp first correction:
\[
q_p=1-\frac2p+o(p^{-1})\qquad(p\to\infty).
\]
In physical dimensions, the optimal circumference-to-height ratio \(c/h=2q_p\) changes from \(\sqrt2\) for the mean square to \(2\cdot3^{-1/4}\) for the fourth moment and approaches \(2\) from below for high powers. Thus there is no fixed-area cylinder simultaneously minimizing every positive distance moment.

## Assumptions and scope
The cylinder consists **only of its lateral surface**, with its intrinsic product metric \(dx^2+dz^2\). The two boundary circles may be included or excluded without changing area sampling. No shortcuts through the solid interior or through attached caps are allowed. Point sampling is independently uniform in Riemannian area. All parameters \(c,h,p\) are strictly positive; the optimization keeps \(A=ch\) fixed. Every conclusion includes all finite real \(p>0\), not merely integer moments. The small-\(p\) limit and global monotonicity of \(p\mapsto q_p\) are not claimed.

## Proof
**Distance reduction.** A shortest lifted path between \((x_1,z_1)\) and \((x_2,z_2)\) is a straight segment in the unrolled flat strip. Minimizing over horizontal deck translations gives
\[
D^2=\min_{k\in\mathbb Z}(x_1-x_2+kc)^2+(z_1-z_2)^2.
\]
Since \(x_1,x_2\) are independent uniform modulo \(c\), the normalized shortest circular displacement \(U=2\min_{k\in\mathbb Z}|x_1-x_2+kc|/c\) is uniform on \([0,1]\). Independently, \(V=|z_1-z_2|/h\) has density \(2(1-v)\) on \([0,1]\). Hence
\[
\frac{D^2}{A}=\frac12\big(qU^2+q^{-1}V^2\big),\qquad
M_p(q):=\frac{\mathbb E[D^p]}{A^{p/2}}=2^{-p/2}\int_0^1\!\int_0^1 2(1-v)(q u^2+q^{-1}v^2)^{p/2}\,du\,dv.
\]

**Unique optimum for every power.** Put \(s=\log q\). At every \(u,v>0\),
\(s\mapsto (e^su^2+e^{-s}v^2)^{p/2}\) is strictly log-convex, because the logarithm is a positive multiple of the strict log-sum-exp of \(s\) and \(-s\). Hölder's inequality makes the integral strictly log-convex in \(s\). Moreover, as \(s\to\infty\) it is at least \(e^{ps/2}\mathbb E[U^p]\), and as \(s\to-\infty\) at least \(e^{-ps/2}\mathbb E[V^p]\). Thus it diverges at both ends, and it has exactly one minimizing \(s_p\). Differentiation under the integral gives the displayed stationarity equation.

To locate the optimizer, differentiate at \(s=0\). After swapping integration variables on half of the unit square, the derivative has the sign of
\[
2\int_{0<v<u<1}(u-v)(u^2-v^2)(u^2+v^2)^{p/2-1}\,du\,dv>0.
\]
The powers are locally integrable for all \(p>0\). Strict convexity then forces \(s_p<0\), or \(0<q_p<1\).

**Exact even powers.** Independence gives \(\mathbb E[U^{2j}]=1/(2j+1)\) and \(\mathbb E[V^{2j}]=2/((2j+1)(2j+2))\). Therefore
\[
M_2(q)=\frac q6+\frac1{12q},\qquad
M_4(q)=\frac14\left(\frac{q^2}5+\frac19+\frac1{15q^2}\right).
\]
Elementary strict minimization yields precisely the stated \(q_2,q_4\) and minimum values; uniqueness also follows from the preceding argument.

**High-power optimizer.** Write \(S_q(u,v)=qu^2+q^{-1}v^2\) and \(r_q=q+q^{-1}\). Its essential maximum on the sampling square is \(r_q\). For each compact interval of positive \(q\), the \(L^{p/2}\) norm \(\mathbb E[S_q^{p/2}]^{2/p}\) converges uniformly to \(r_q\). The inequalities
\[
\mathbb E[S_q^{p/2}]\ge \frac{q^{p/2}}{p+1},\qquad
\mathbb E[S_q^{p/2}]\ge \frac{2q^{-p/2}}{(p+1)(p+2)},\qquad
\mathbb E[S_1^{p/2}]\le2^{p/2}
\]
confine the optimizing \(q_p\) to a fixed compact positive interval for sufficiently large \(p\). Since \(r_q\) has unique minimum at \(q=1\), this proves \(q_p\to1\).

For the first correction, tilt the sampling law by the positive density proportional to \(S_q(U,V)^{p/2}\), and set \(X_p=p(1-U)\), \(Y_p=p(1-V)\). Uniformly for \(q\) near one, the endpoint change of variables and dominated convergence give convergence with first moments to two independent laws: \(X\) exponential of rate \(q/r_q\), and \(Y\) gamma of shape two and rate \(q^{-1}/r_q\). In particular \(\mathbb E[X]=r_q/q\) and \(\mathbb E[Y]=2r_q q\). The required uniform domination follows from
\[
S_q(1-x/p,1-y/p)\le r_q-\frac{qx+q^{-1}y}{p}
\]
for \(0\le x,y\le p\), giving an exponentially decaying envelope after raising to \(p/2\). The score equation for the minimizing \(q_p\), under this tilted law, reads
\[
0=\mathbb E\left[\frac{q_pU^2-q_p^{-1}V^2}{q_pU^2+q_p^{-1}V^2}\right].
\]
Expanding the fraction at \(U=V=1\) using uniform first-moment convergence and \(q_p\to1\) yields
\[
0=\frac{q_p-q_p^{-1}}{q_p+q_p^{-1}}+\frac2p+o(p^{-1}).
\]
Since \((q-q^{-1})/(q+q^{-1})=(q-1)+O((q-1)^2)\) near one, it follows first that \(q_p-1=O(p^{-1})\), and then that \(q_p=1-2/p+o(p^{-1})\).

## Verification
The standalone numerical checker `CHECK.py` evaluates the two-dimensional integral by Gauss--Legendre quadrature, verifies the exact second- and fourth-moment optima, checks the score sign across the minimizer at several further powers, and tests 350,000 independently generated point pairs against the second-moment formula. It returns `FLAT_CYLINDER_LP_OPTIMIZATION_OK 350000`. The check of \(p=100\) gives \(q_{100}\approx0.9805634068\), consistent with the proved first correction; it is not used as proof of an asymptotic. The analytical argument, rather than the computation, covers every \(p>0\).

## Relationship to prior work
Tu and Fischbach (arXiv:math-ph/0201046, first posted 2002-01-22) analyze point-distance distributions and moments in Euclidean spherical bodies, not intrinsic geodesic distance on a periodic cylindrical surface or fixed-area aspect-ratio minimization. Tong and Pan (arXiv:1602.03407, first posted 2016-01-21), especially Section IV, develop planar point-distance distributions in polygonal rings. Their ring distances are ambient Euclidean distances in planar regions, not quotient-metric shortest-path distances on a cylinder. The present distance law uses a flat circular quotient, a different metric and sampling space. General geodesic formulas for a flat cylinder are elementary and not claimed as new. The contribution asserted here is the **joint all-positive-power sharp shape optimization and its high-power correction**. A complete historical-priority search is not claimed.

## Limitations
The theorem is restricted to flat lateral cylinders with a uniform product-area measure. It does not apply to capped-cylinder intrinsic distances allowing passage over caps, to ambient three-dimensional chord lengths, or to noncircular or curved-cylinder metrics. The exact minimizer for general \(p\) is characterized implicitly by one explicit two-dimensional integral; elementary closed forms are given only for \(p=2\) and \(p=4\). No monotonicity in \(p\), small-power optimum, or second asymptotic correction is asserted. An independent research audit has not been performed.

## References
1. Shu-Ju Tu and Ephraim Fischbach, *Random Distance Distribution for Spherical Objects: General Theory and Applications to n-Dimensional Physics*, arXiv:math-ph/0201046 (first public version 2002-01-22), https://arxiv.org/abs/math-ph/0201046.
2. Fei Tong and Jianping Pan, *Random Distances Associated with Arbitrary Polygons: An Algorithmic Approach between Two Random Points*, arXiv:1602.03407 (first public version 2016-01-21), https://arxiv.org/abs/1602.03407.
