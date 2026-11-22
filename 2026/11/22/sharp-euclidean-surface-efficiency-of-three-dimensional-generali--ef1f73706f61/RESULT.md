# Sharp Euclidean surface efficiency of three-dimensional generalized parking-function polytopes

## Finding
For every real \(t\ge 0\), define the three-dimensional polytope
\[
P_t=\left\{z\in\mathbb R^3:\ 0\le z_i\le t+2,\ z_i+z_j\le 2t+3\ (i<j),\ z_1+z_2+z_3\le3t+3\right\}.
\]
Its ordinary Euclidean volume and two-dimensional boundary area are
\[
V(t)=t^3+6t^2+\frac{21}{2}t+4,
\qquad S(t)=6t^2+(18+3\sqrt2)t+12+3\sqrt3.
\]
The Euclidean isoperimetric quotient \(Q(t)=S(t)^3/V(t)^2\) has **exactly one global minimizer** \(t_*\ge0\). It is the unique positive root of
\[
\begin{aligned}
D(t)={}&(18-9\sqrt2)t^3+(72-18\sqrt2-18\sqrt3)t^2\\
&+\left(45+\frac{63\sqrt2}{2}-72\sqrt3\right)t+36\sqrt2-63\sqrt3-36.
\end{aligned}
\]
Numerically \(t_*=2.52596465810683\ldots\), with sharp lower bound \(Q(t)\ge Q(t_*)=193.05681241440385\ldots\). The equal-volume cube has quotient \(216\). There is exactly one cube-crossing parameter \(t_c=0.629939681219772\ldots\); thus \(P_t\) has strictly lower Euclidean surface area than its equal-volume cube if and only if \(t>t_c\), with equality at \(t_c\). The quotient approaches \(216\) from below as \(t\to\infty\).

## Assumptions and scope
All geometry is in the **original Euclidean coordinate metric** (not normalized lattice boundary area). The parameter is real and nonnegative. For integers \(a,b\ge1\), the generalized parking-function polytope \(\mathfrak X_3(a,b,b)\), in its established natural embedding, equals \((1,1,1)+bP_t\) at \(t=(a-1)/b\). Thus the result applies exactly to all such integer parking-function polytopes; real \(t\) additionally provides their natural continuous shape interpolation. The endpoint \(t=0\) is included. The scale-invariant quotient is unchanged by translation and positive uniform dilation. At \(t>0\) the polytope has ten facets; at \(t=0\) the three pair facets collapse, leaving seven facets.

## Proof
The known facet-description theorem for generalized parking-function polytopes [2, Theorem 2.3(c)] gives the displayed inequalities after subtracting \(1\) from each coordinate and scaling by \(b\). It also confirms that the inequalities are facet-defining for \(t>0\), with the pair inequalities redundant at \(t=0\). Each of the three lower facets \(z_i=0\) is a square of side \(t+2\) with a unit-leg corner triangle removed; its area is \(A_L=(t+2)^2-1/2\). Each upper coordinate facet \(z_i=t+2\) is a square of side \(t+1\) with a unit-leg corner triangle removed, of area \(A_U=(t+1)^2-1/2\). On each of the three pair facets \(z_i+z_j=2t+3\), the varying pair is \((t+1+u,t+2-u)\) for \(0\le u\le1\), while the third coordinate independently ranges over \([0,t]\). Hence its Euclidean area is \(A_P=\sqrt2\,t\). Finally, on the top facet, writing \(y_i=z_i-t\), the constraints reduce to \(0\le y_i\le2\) and \(\sum_i y_i=3\). This is the regular hexagon with the six permutations of \((0,1,2)\) as vertices, of area \(A_T=3\sqrt3\). Therefore
\[
S(t)=3A_L+3A_U+3A_P+A_T
=6t^2+(18+3\sqrt2)t+12+3\sqrt3.
\]
The classical divergence identity \(3V=\sum_F h_FA_F\), with support distances measured from the origin, uses no lower-facet contribution. It gives
\[
3V(t)=3(t+2)A_U+3t(2t+3)+9(t+1),
\]
which simplifies to the stated cubic. This recovers an already-known volume [1]; only its use in the new metric optimization is claimed here.

Differentiation yields
\[
Q'(t)=\frac{S(t)^2}{V(t)^3}\,D(t).
\]
The coefficients of \(D\), in descending degree, have signs \((+,+,-,-)\): the explicit expressions above give strictly positive cubic and quadratic coefficients and strictly negative linear and constant coefficients (their signs can be bounded directly by \(1.41<\sqrt2<1.42\), \(1.73<\sqrt3<1.74\)). Descartes' rule of signs gives at most one positive root. Because \(D(0)<0\) and the leading coefficient is positive, the intermediate value theorem gives exactly one. Since \(S,V>0\), \(Q\) decreases strictly before that root and increases strictly afterwards, proving global uniqueness. The exact rational isolating bounds \(2.52596<t_*<2.52597\) follow by substitution in \(D\); the printed decimals are numerical refinements.

At \(t=0\), \(Q(0)=(12+3\sqrt3)^3/16>216\). Its leading behavior is
\[
\frac{Q(t)}{216}=1+\left(\frac{3\sqrt2}{2}-3\right)\frac1t+O(t^{-2}),\qquad t\to\infty,
\]
so the limit is \(216\) and is approached from **below**. Strict decrease to \(Q(t_*)<216\) followed by strict increase toward \(216\) proves the unique positive crossing \(t_c\) and the stated comparison. Its numerical value is the single positive root of the explicit equation \(S(t)^3=216V(t)^2\). Finally, positive rational \(t=(a-1)/b\) are dense in \([0,\infty)\), so the bound is also the sharp infimum over the integer-parameter family, without asserting that an integer-parameter polytope attains it.

## Verification
The accompanying `verification/verify.py` independently enumerates permutation-vertex families and compares their three-dimensional convex-hull surface area and volume at nine parameter values with the formulas. It also checks symbolic expressions for all derivative coefficients, the unique positive stationary point, and the cube crossing. Execute `python verification/verify.py` after installing the packages in `verification/requirements.txt`. Numerical finite-hull checks are diagnostic; the proof above establishes all real parameters.

## Relationship to prior work
Hanada–Lentfer–Vindas-Meléndez [1] introduced the two-parameter generalized parking-function polytopes and established volume formulas, so the volume polynomial is not asserted as a new invariant. Bayer et al. [2] gave a general minimal inequality and vertex characterization, which is used explicitly. Neither inspected primary treatment establishes the ordinary Euclidean boundary-area formula, the sharp normalized surface-area minimum, or its comparison with the equal-volume cube. The question here is a metric extremal problem, not the previously investigated face enumeration, lattice surface coefficient, circumsphere, or inball. Earlier equivalent work outside the inspected sources remains a possible historical-priority limitation.

## Limitations
The optimizer is global **within this specific one-parameter continuous family up to positive uniform scaling**, not among all convex bodies or all generalized parking-function polytopes with arbitrary three independent parking parameters. Finite numerical tests do not establish originality or prove the infinite-parameter statement. The sharp real optimum need not occur at an integer pair \((a,b)\); only approximation by integer pairs is asserted. No independent mathematical audit has been performed.

## References
[1] M. Hanada, J. Lentfer and A. R. Vindas-Meléndez, *Generalized parking function polytopes*, arXiv:2212.06885 (first posted 2022-12-13), Annals of Combinatorics 28 (2024), 575–613. https://arxiv.org/html/2212.06885v2

[2] M. M. Bayer et al., *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387 (first posted 2024-03-12), Discrete & Computational Geometry (2025 online), Theorem 2.3. https://link.springer.com/article/10.1007/s00454-025-00770-1
