# Sharp Euclidean surface efficiency and cube crossing for three-dimensional parking-function polytopes

## Finding

For \(t\ge 0\), let
\[
P_t=\{z\in\mathbb R^3:0\le z_i\le t+2,\ z_i+z_j\le 2t+3\ (i<j),\ z_1+z_2+z_3\le3t+3\}.
\]
Write \(S(t)\) and \(V(t)\) for its ordinary Euclidean boundary area and volume, and \(Q(t)=S(t)^3/V(t)^2\). Within this family, **up to uniform rescaling, there is exactly one shape of least surface area at fixed volume**. Its parameter \(t_*\) is the unique positive root of
\[
\begin{aligned}
D(t)={}&(18-9\sqrt2)t^3+(72-18\sqrt2-18\sqrt3)t^2\\
&+\left(45+\frac{63\sqrt2}{2}-72\sqrt3\right)t+36\sqrt2-63\sqrt3-36.
\end{aligned}
\]
The values are \(t_*\simeq 2.52596465810683\) and \(Q(t_*)\simeq193.056812414404\). There is exactly one \(t_c\simeq0.629939681219772\) for which \(P_t\) and its equal-volume cube have the same boundary area. The boundary area of \(P_t\) is strictly less than the cube's if and only if \(t>t_c\). The quotient increases from its minimum toward the cube value \(216\) from below.

## Assumptions and scope

Area is the Euclidean two-dimensional boundary measure, not the lattice-normalized boundary coefficient. For integers \(a,b\ge1\) the usual embedding of the generalized parking-function polytope gives \(\mathfrak X_3(a,b,b)=(1,1,1)+bP_{(a-1)/b}\) by the facet description in [2, Theorem 2.3(c)]. The real family includes the endpoint \(t=0\); the three pair facets then have zero area and are not facets. Translation and positive uniform scaling do not affect \(Q\). The continuous sharp lower bound is also the infimum over integer \(a,b\), since the parameters \((a-1)/b\) are dense in \([0,\infty)\). The theorem does not require attainment by an integer pair.

## Geometric inputs

The established volume formula [1, Theorem 1.1] and the general Euclidean boundary-area decomposition [3, Proof, “Exact boundary decomposition”] give
\[
V(t)=t^3+6t^2+\frac{21}{2}t+4,\qquad
S(t)=6t^2+(18+3\sqrt2)t+12+3\sqrt3.
\]
Indeed, the area decomposition in dimension three is \(3V_2(t+1)+3V_2(t)+3\sqrt2\,t+3\sqrt3\), with \(V_2(s)=(s+1)^2-1/2\). Geometrically, the lower and upper coordinate facets are squares of sides \(t+2\) and \(t+1\), respectively, with a unit-leg triangle removed. The three pair facets are rectangles with sides \(\sqrt2\) and \(t\). On the top facet, subtracting \(t\) from each coordinate gives the regular hexagon with vertices the six permutations of \((0,1,2)\), of area \(3\sqrt3\). The divergence formula also checks the volume: summing area times support height gives
\[
3V(t)=3(t+2)((t+1)^2-1/2)+3t(2t+3)+9(t+1).
\]

## Proof of the sharp comparison

Since uniform dilation cancels in \(S^3/V^2\), minimizing \(Q\) is equivalent to minimizing area after normalizing volume. Differentiation gives
\[
Q'(t)=\frac{S(t)^2}{V(t)^3}\bigl(3V(t)S'(t)-2S(t)V'(t)\bigr)=\frac{S(t)^2}{V(t)^3}D(t).
\]
The four coefficients of \(D\), in descending order, have signs \(+,+,-,-\); for example the signs follow from \(1.41<\sqrt2<1.42\) and \(1.73<\sqrt3<1.74\). Descartes' rule gives at most one positive root, and the opposite signs of \(D(0)\) and \(D(t)\) for large \(t\) give existence. Therefore \(Q\) decreases strictly until \(t_*\) and increases strictly thereafter. For example, substitution gives \(2.52596<t_*<2.52597\).

An equal-volume cube has area \(6V(t)^{2/3}\), hence quotient \(216\). At \(t=0\), \((12+3\sqrt3)^3/16>216\). At infinity,
\[
\frac{Q(t)}{216}=1+\left(\frac{3\sqrt2}{2}-3\right)t^{-1}+O(t^{-2}),
\]
so \(Q\) tends to \(216\) from below. Its strictly increasing portion lies strictly below \(216\), and its strictly decreasing portion crosses \(216\) exactly once. This yields the stated cube comparison. For numerical evaluation, one can solve the unique positive root of \(S(t)^3-216V(t)^2=0\) for \(t_c\).

## Verification

The symbolic formulas and finite convex-hull diagnostics can be checked by `verification/verify.py` using the dependencies in `verification/requirements.txt`. The analytic sign and monotonicity arguments prove the conclusions for all real \(t\ge0\); finite checks do not certify them.

## Relationship to prior work and limitations

The embedding, facet description and volume are existing inputs [1, 2]. The Euclidean area polynomial is a direct specialization of the general Euclidean facet decomposition [3] and is not claimed as a separate new formula. This result concerns the unique normalized optimizer and the global comparison with the equal-volume cube in dimension three. The general area decomposition supplies the input function but does not itself give the sign pattern, unique optimizer, or cube crossing. No optimum is asserted over arbitrary convex bodies, higher dimensions, or generalized parking-function polytopes with three independent parking parameters. Historical priority beyond the compared records is not certified.

## References

1. M. Hanada, J. Lentfer and A. R. Vindas-Meléndez, *Generalized parking function polytopes*, Ann. Comb. 28 (2024), 575–613, https://arxiv.org/abs/2212.06885.
2. M. M. Bayer et al., *Combinatorics of generalized parking-function polytopes*, Discrete Comput. Geom., https://doi.org/10.1007/s00454-025-00770-1.
3. *An area-weighted facet-rank law and logarithmic boundary tail*, Resultary, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-an-area-weighted-facet-rank-law-and-logarithmic-boundary-tail-an--11ff2c69295a.
