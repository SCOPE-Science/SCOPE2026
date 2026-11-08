# Universal Santaló displacement and sharp Mahler response of unequal-height bipyramids

## Finding
Let \(d\ge2\), and let \(B\subset\mathbb R^{d-1}\) be any convex body placed with its Santaló point at the origin. For \(a,b>0\), set
\[
K_{a,b}(B)=\operatorname{conv}\bigl((B,0),(0,a),(0,-b)\bigr)\subset\mathbb R^d.
\]
The following conclusions hold **for every such base**, including asymmetric or nonsmooth bases. Let \(s(K)\) be the Santaló point, and \(\Pi(K)=\operatorname{vol}(K)\operatorname{vol}((K-s(K))^\circ)\) its affine volume product.

**Universal centering and strict centroid separation.** The Santaló point is \((0,s)\). If \(a>b\), its height satisfies the strict, dimension-uniform bracket
\[
\boxed{\frac{a-b}{d+1}<s<\frac{a-b}{2}.}\tag{1}
\]
The lower endpoint is the ordinary volume-centroid height; the upper endpoint is the midpoint of the two axial apices. For \(a<b\), both signs reverse, and for \(a=b\) all three heights vanish. For \(a>b\), \(s\) is the unique real number in the interval (1) satisfying
\[
\boxed{G_d\!\left(\frac{a}{a-s}\right)=G_d\!\left(\frac{b}{b+s}\right),\quad
G_d(u)=u^d(d+1-du).}\tag{2}
\]
In particular, the Santaló centering is independent of the geometry of \(B\).

**Exact product and sharp symmetry deficit.** Define
\[
J_d(z;a,b)=\begin{cases}
\displaystyle\frac{(a/(a-z))^d-(b/(b+z))^d}{dz},&z\ne0,\\[4pt]
\displaystyle\frac1a+\frac1b,&z=0.
\end{cases}
\]
Then
\[
\boxed{\frac{\Pi(K_{a,b}(B))}{\Pi(B)}=\frac{a+b}{d}\,J_d(s;a,b).}\tag{3}
\]
At fixed \(a+b\), this ratio decreases strictly as \(|a-b|/(a+b)\) grows. Normalize \(a=1+\delta\), \(b=1-\delta\). As \(\delta\to0\),
\[
\boxed{\begin{aligned}
s&=\frac{3\delta}{d+2}+O_d(\delta^3),\\
\frac{\Pi(K_{1+\delta,1-\delta}(B))}{\Pi(B)}
&=\frac4d\left[1-\frac{d-1}{2(d+2)}\delta^2+O_d(\delta^4)\right].
\end{aligned}}\tag{4}
\]
This identifies the exact, strictly positive quadratic decay coefficient. The maximal product ratio is \(4/d\) at equal heights, and its limit as one apex merges with the base is \((d+1)^{d+1}/d^{d+2}\). Strict monotonicity itself also follows from the general shadow-system theorem of Meyer and Reisner, and is **not** presented as a historically new standalone assertion; the specific centering interval and quadratic coefficient are the main contributions.

## Assumptions and scope
Here a convex body is compact, convex, and full-dimensional in its affine space; \(0\in\operatorname{int}B\). The polar \(B^\circ\) uses the Euclidean pairing in \(\mathbb R^{d-1}\); Santaló centering of \(B\) is equivalent to \(\operatorname{centroid}(B^\circ)=0\). The polar \((K-(0,z))^\circ\) is taken in \(\mathbb R^d\). No symmetry of the base is required. The open assumption \(a,b>0\) ensures a genuine double pyramid; the one-apex limit is continuous and separately identified. The specified axial parameterization is affine-normalized: simultaneous scaling of \(a,b\) is immaterial to the volume product.

## Proof
**1. Polar sections and global Santaló center.** Fix \(-b<z<a\). The polar \(Q_z=(K_{a,b}(B)-(0,z))^\circ\), with horizontal variable \(y\) and axial variable \(t\), consists exactly of
\[
-\frac1{b+z}\le t\le\frac1{a-z},\qquad y\in(1+zt)B^\circ.
\tag{5}
\]
Both endpoint dilation factors are positive. Fubini and a one-variable antiderivative give
\[
\operatorname{vol}_d(Q_z)=\operatorname{vol}_{d-1}(B^\circ)
\int_{-1/(b+z)}^{1/(a-z)}(1+zt)^{d-1}\,dt
=\operatorname{vol}_{d-1}(B^\circ)J_d(z;a,b).
\tag{6}
\]
Because \(\operatorname{centroid}(B^\circ)=0\), every horizontal polar section has horizontal first moment zero. At any axial stationary point of (6), the axial polar first moment also vanishes, by the polar-volume gradient identity. Hence that point is the full Santaló point, by strict convexity and uniqueness of the polar-volume minimizer. The centroid of \(K_{a,b}(B)\), from the volumes and centroids of its two pyramidal halves, has axial coordinate
\[
c=\frac{a-b}{d+1}.\tag{7}
\]
The original volume is \((a+b)\operatorname{vol}_{d-1}(B)/d\), proving (3).

**2. Algebraic Santaló equation.** For \(z\ne0\), put \(R=a/(a-z)\), \(T=b/(b+z)\) and \(G_d(u)=u^d(d+1-du)\). Differentiating (6) yields the exact identity
\[
\frac{\partial J_d}{\partial z}=\frac{G_d(T)-G_d(R)}{dz^2}.\tag{8}
\]
At \(z=0\), the continuous derivative is
\[
J_d'(0;a,b)=\frac{d+1}{2}\left(\frac1{a^2}-\frac1{b^2}\right).\tag{9}
\]
For \(a>b\), this is negative, so the Santaló height is positive. Equation (2) is (8) at the unique interior minimum. Its restricted interval is important because the undivided algebraic equation also has the spurious root \(z=0\) when \(a\ne b\).

**3. Strict bounds.** Suppose \(a>b\), and write \(r=a/b>1\). At \(c=(a-b)/(d+1)\), the substitutions in (8) give
\[
G_d(R_c)=\frac{(d+1)^{d+1}r^d}{(dr+1)^{d+1}},\qquad
G_d(T_c)=\frac{(d+1)^{d+1}r}{(r+d)^{d+1}}.
\]
Define
\[
H(r)=\frac{d-1}{d+1}\log r-\log\frac{dr+1}{r+d}.
\]
Since \(H(1)=0\) and
\[
H'(r)=\frac{d(d-1)(r-1)^2}{(d+1)r(dr+1)(r+d)}>0\quad(r>1),
\]
one has \(G_d(R_c)>G_d(T_c)\), hence \(J_d'(c)<0\).

At the apex midpoint \(m=(a-b)/2\), put \(\eta=(a-b)/(a+b)\in(0,1)\). Then \(R_m=1+\eta\), \(T_m=1-\eta\). For \(\eta\ge1/d\), \(G_d(1+\eta)\le0<G_d(1-\eta)\). For \(0<\eta<1/d\), logarithmic differentiation gives
\[
\frac{d}{d\eta}\log\frac{G_d(1+\eta)}{G_d(1-\eta)}
=-\frac{2d(d+1)(d-1)\eta^2}{(1-\eta^2)(1-d^2\eta^2)}<0.
\]
Thus \(G_d(R_m)<G_d(T_m)\) in every case, implying \(J_d'(m)>0\). Strict convexity and uniqueness place the Santaló height strictly between \(c\) and \(m\). Reflection across the base hyperplane handles \(a<b\), including asymmetric bases.

**4. Monotonicity and exact quadratic coefficient.** Normalize the total height to two, so \(a=1+\delta\), \(b=1-\delta\). For \(\delta>0\), let \(z=s(\delta)\) be the Santaló height. Envelope differentiation of (6), using only the moving integration endpoints, gives
\[
\frac{d}{d\delta}J_d(s(\delta);1+\delta,1-\delta)
=\frac{b^{d-1}}{(b+s)^{d+1}}-\frac{a^{d-1}}{(a-s)^{d+1}}.\tag{10}
\]
The right side is negative precisely when
\[
\frac{a-s}{b+s}<\left(\frac ab\right)^{(d-1)/(d+1)}.
\]
At \(s=c\) this is exactly \(H(a/b)>0\) from Step 3; and the left side strictly decreases as \(s\) increases. Since \(s>c\), the inequality holds, giving strict decrease of the minimized polar volume and hence of the product at fixed total height. Reflection makes the product even in \(\delta\).

For the local coefficient, write \(J(\delta,z)=J_d(z;1+\delta,1-\delta)\). The smooth even-in-\((\delta,z)\) expansion about \((0,0)\) is
\[
J(\delta,z)=2+2\delta^2-2(d+1)\delta z
+\frac{(d+1)(d+2)}3z^2+O_d((|\delta|+|z|)^4).
\]
The stationarity equation implies \(s(\delta)=3\delta/(d+2)+O_d(\delta^3)\). Substituting it gives
\[
J(\delta,s(\delta))=2-\frac{d-1}{d+2}\delta^2+O_d(\delta^4),
\]
which proves (4). At equal heights \(J(0;1,1)=2\). At the one-apex limit \(b\downarrow0\), the resulting pyramid's Santaló height is \(a/(d+1)\), and direct substitution into (6) yields the endpoint factor \((d+1)^{d+1}/d^{d+2}\). This endpoint coincides with the classical pyramid product formula.

## Verification
Run `python bipyramid_santalo_check.py` with Python 3, SymPy, NumPy, and SciPy. The checker independently expands the polar-section integral using exact fractions, differentiates the resulting rational function symbolically, checks centroid/midpoint signs in multiple dimensions and rational height ratios, checks exact second-order Taylor coefficients, and compares the polar volume with independently constructed convex hulls of two- and three-dimensional polar polytopes, including a nonsymmetric triangular facet model. It reports `ASYMMETRIC_BIPYRAMID_CHECKS_PASSED 18 18 128 8 25 9`. These are reproducible regression checks; all-dimension strictness follows from the analytic inequalities proved above.

## Relationship to prior work
Pavlov and Telen, *Santaló Geometry of Convex Polytopes*, develop the rational polar-volume and Santaló-center framework for polytopes. Their arXiv preprint (29 February 2024) motivates explicit geometric instances, but does not state the strict bipyramid centering interval or the quadratic coefficient (4).

Meyer and Reisner, *Shadow systems and volumes of polar convex bodies* (2006), explicitly consider double pyramids, and their Theorem 1 and double-pyramid discussion imply the monotone volume-product trend under axial imbalance. We do **not** claim that trend alone as new. Their published discussion does not give (1) or the coefficient (4); our separate calculations quantify them.

The public result *Universal Santaló and volume-product laws for homothetic frusta* gives closed formulas for Santaló centers and ordinary centroids of homothetic frusta. An axial polar section here is a homothetic frustum, so its centroid formula can be used to re-derive the implicit centering equation (2) by polarity and algebra. Thus **the polar integration and implicit root alone are not asserted to be historically novel**. That result compares the Santaló point of a frustum with its centroid, whereas (1) compares the Santaló point of its unequal-height bipolar counterpart with that body's own centroid and apex midpoint. Its stated results do not supply this strict two-sided bound or the normalized quadratic Mahler coefficient.

Izmestiev's *Matching centroids by a projective transformation* (2014 preprint, 2023 journal) provides the general polar-centroid characterization and discusses double pyramids in a different centering question. That background is credited. No claim of independence or historical priority beyond the inspected results is made.

## Limitations
The two apex points must lie on the same line through the Santaló point of the common equatorial base, on opposite sides. Arbitrary skew bipyramids are not covered. The results concern the affine Santaló volume product, not Euclidean surface area or a general Mahler inequality. The second-order formula is local near equal apex heights; the exact product (3) applies globally. General shadow-system monotonicity and pyramid endpoints predate this result. The strongest residual priority risk is an earlier, possibly differently parameterized centroid–Santaló comparison or exact second-variation computation for suspensions/double cones, not located in the inspected primary texts.

## References
1. D. Pavlov and S. Telen, *Santaló Geometry of Convex Polytopes*, arXiv:2402.18955v1, 29 February 2024, especially §§1–2; primary MSC2020 52B20.
2. M. Meyer and S. Reisner, *Shadow systems and volumes of polar convex bodies*, arXiv:math/0606305v1, 13 June 2006, *Mathematika* 53 (2006), 129–148, especially Theorem 1, §3 double-pyramid case, and the pyramid product lemma.
3. I. Izmestiev, *Matching centroids by a projective transformation*, arXiv:1409.6176v1, 2014; *Geometriae Dedicata* 217 (2023), article 53, especially §4 and Example 5.2.
4. *Universal Santaló and volume-product laws for homothetic frusta*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-santal-and-volume-product-laws-for-homothetic-frusta--3dbfdaf0b359 (scientific statements compared for polarity implications).
