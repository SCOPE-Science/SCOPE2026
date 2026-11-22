# A two-scale boundary-clearance law and parabolic pinch for ideal hyperbolic quadrilaterals

## Finding

Fix a geodesically convex ideal quadrilateral \(Q_c\) in curvature-\(-1\) hyperbolic space. Use the Klein unit disk to represent its four ideal vertices by \((\pm c,\pm s)\), where \(c^2+s^2=1\) and \(1/\sqrt2\le c<1\). Write \(\rho_c=\operatorname{arsinh}((4c^2-1)^{-1/2})\) for its maximal inscribed-disk radius (a known geometric formula). Sample a point \(X\) from the uniform hyperbolic area distribution on \(Q_c\), and set \(D_c=d_{\mathbb H}(X,\partial Q_c)\).

**Fixed-shape upper tail.** For each fixed nonsquare \(1/\sqrt2<c<1\),
\[
\boxed{\Pr(D_c>\rho_c-h)=\frac{(4c^2-1)^{3/2}}{\pi(2c^2-1)}h^2+o_c(h^2),\qquad h\downarrow0.}
\]
At the exactly square ideal quadrilateral \(c=1/\sqrt2\),
\[
\boxed{\Pr(D_c>\rho_c-h)=\frac2\pi h^2+o(h^2).}
\]
The fixed nonsquare coefficient diverges when the quadrilateral approaches the square, so these limits are not uniform in its shape.

**Critical shape–clearance scaling.** Fix \(\lambda>0\), and choose the quadrilateral varying with \(h\) according to \(c_h^2=\frac12+\lambda\sqrt h\) and \(s_h^2=\frac12-\lambda\sqrt h\). Define the region
\[
\mathcal R_\lambda=\left\{(u,v):\ |u|\le2\sqrt2\lambda,\quad |v|\le1+\frac{u^2}{2\sqrt2}-2\sqrt2\lambda^2\right\}
\]
(the displayed inequalities implicitly require a nonnegative right side), and let \(\mathcal A(\lambda)\) be its ordinary Euclidean area. It is explicitly
\[
\boxed{\mathcal A(\lambda)=8\sqrt2\lambda-\frac{64}{3}\lambda^3+
\frac{2\sqrt2}{3}\bigl(8\lambda^2-2\sqrt2\bigr)_+^{3/2},\qquad z_+=\max(z,0).}
\]
Then
\[
\boxed{\Pr(D_{c_h}>\rho_{c_h}-h)=\frac{\mathcal A(\lambda)}{2\pi}h^{3/2}+o_\lambda(h^{3/2}).}
\]
Conditionally on the event in this last formula, the Klein-coordinate vector \((x/\sqrt h,y/h)\) converges in **total variation** to uniform area on \(\mathcal R_\lambda\). At \(\lambda_*=2^{-3/4}\), the limiting open region changes from one connected component (\(\lambda<\lambda_*\)) to two (\(\lambda\ge\lambda_*\)); at equality its closed support has a single pinch point. The area profile has a characteristic positive \((\lambda-\lambda_*)_+^{3/2}\) contribution after subtraction of the analytic polynomial, and \(\mathcal A(\lambda)\sim1/\lambda\) as \(\lambda\to\infty\).

At fixed nonsquare \(c\), after centering at each of the two (known) maximizing disk centers and scaling both Klein coordinates by \(h\), the conditional law converges to an equally weighted mixture of uniform measures on two explicitly specified congruent triangles (defined in the proof). At the square, scaling both coordinates by \(h\) yields the uniform law on \([-1,1]^2\).

## Assumptions and scope

All distances are intrinsic distances on the complete hyperbolic plane of constant curvature \(-1\). The ideal quadrilateral's vertices lie on the unit circle at infinity, while all sampled points lie in the open disk. Its hyperbolic area is exactly \(2\pi\), by Gauss–Bonnet. The boundary comprises four complete geodesic sides. The parameter \(c\) denotes the larger Klein-coordinate half-width, so the square is \(c=s=1/\sqrt2\). Statements involving a fixed nonsquare hold for that fixed shape only, not uniformly as \(c\downarrow1/\sqrt2\). The critical \(\lambda\) is fixed and strictly positive while \(h\downarrow0\); the exactly square case is a separate scaling regime. These three limits are stated in the indicated order. The known two-inball geometry is used as input and is not claimed as a new result.

## Proof

**1. Exact clearance inequalities.** In the Klein disk, \(Q_c=\{|x|<c,\ |y|<s\}\). Its area element is
\[
 dA_{\mathbb H}=\frac{dx\,dy}{(1-x^2-y^2)^{3/2}}.
\]
The hyperboloid model and its four normalized supporting-plane normals give, at every interior point,
\[
\sinh D_c(x,y)=\frac{1}{\sqrt{1-x^2-y^2}}\min\left\{\frac{c-|x|}{s},\ \frac{s-|y|}{c}\right\}.
\]
Therefore the exact superlevel set \(E(c,h)=\{D_c>\rho_c-h\}\) is characterized by the two strict inequalities
\[
 c-|x|>s k_h\sqrt{1-x^2-y^2},\qquad
 s-|y|>c k_h\sqrt{1-x^2-y^2},\quad k_h=\sinh(\rho_c-h).
\]
The prior geometric classification gives the complete set of maximizers: for \(c>s\), the two points \((\pm x_*,0)\), where \(x_*=(2c^2-1)/c\), and for \(c=s\), only \((0,0)\). This ensures that for each fixed shape the shrinking superlevel sets have no other components.

**2. A fixed nonsquare: two triangular blow-ups.** Fix \(c>s\), and put \(L=4c^2-1\) and \(H^2=1-x_*^2=s^2 L/c^2\). Center at \((x_*,0)\), setting \(x=x_*+hu\), \(y=hv\). Since
\[
 k_h=L^{-1/2}-2cL^{-1/2}h+O_c(h^2),
\]
the two exact clearance constraints, divided by \(h\), converge to
\[
 u\le U:=\frac{s^2L}{c^2},\qquad
 |v|\le 2cs+\frac{c(2c^2-1)}{sL}\,u.
\]
Thus the limiting triangle has left vertex \((-V,0)\), where \(V=2s^2L/(2c^2-1)\), and right vertical base at \(u=U\) of half-height \(sL/c\). Its Euclidean area is
\[
 T_c=\frac{s^3L^3}{c^3(2c^2-1)}.
\]
The hyperbolic area density tends to \(H^{-3}=c^3/(s^3L^{3/2})\), so the hyperbolic area of one component is \(H^{-3}T_c h^2+o_c(h^2)=L^{3/2}h^2/(2c^2-1)+o_c(h^2)\). Reflection gives the second, and division by the full quadrilateral area \(2\pi\) gives the fixed nonsquare coefficient. The two rescaled conditional component densities tend in \(L^1\) to constant densities on these triangles; symmetry gives weight \(1/2\) each.

**3. The square: a four-contact blow-up.** For \(c=s=1/\sqrt2\), put \(x=hu\), \(y=hv\). Here \(\rho_c=\operatorname{arsinh}1\), and the exact constraints reduce at first order to \(|u|<1\) and \(|v|<1\). The Klein area density tends to \(1\), giving hyperbolic superlevel area \(4h^2+o(h^2)\), hence probability \(2h^2/\pi+o(h^2)\) and a uniform rescaled square limit.

**4. The critical parabolic blow-up.** Fix \(\lambda>0\), set \(\delta=\sqrt h\), \(c_h^2=1/2+\lambda\delta\), and write \(x=\delta u\), \(y=\delta^2v\). The threshold expands as
\[
 k_h=1-2\lambda\delta+(6\lambda^2-\sqrt2)\delta^2+O_\lambda(\delta^3).
\]
For bounded \((u,v)\), the signed vertical-side clearance quantity (the first entry of the minimum above) and the horizontal-side quantity respectively expand to
\[
 \frac{c_h-|x|}{s_h\sqrt{1-x^2-y^2}}=1+(2\lambda-\sqrt2|u|)\delta+O_\lambda(\delta^2),
\]
\[
 \frac{s_h-|y|}{c_h\sqrt{1-x^2-y^2}}=1-2\lambda\delta+(2\lambda^2+u^2/2-\sqrt2|v|)\delta^2+O_\lambda(\delta^3).
\]
Comparison with \(k_h\) yields precisely \(|u|\le2\sqrt2\lambda\) and \(|v|\le1+u^2/(2\sqrt2)-2\sqrt2\lambda^2\). The limiting region has nonempty interior for every fixed \(\lambda>0\), and its boundary has planar Lebesgue measure zero.

To justify passage from local expansions to full probabilities, compactness plus the known unique square maximizer show that any sequence of points in \(E(c_h,h)\) satisfies \(x,y\to0\). The exact side constraints first imply \(|x|=O_\lambda(\delta+x^2+y^2)\) and \(|y|=O_\lambda(\delta^2+x^2+y^2)\). Absorbing their small quadratic terms gives \(|x|=O_\lambda(\delta)\), \(|y|=O_\lambda(\delta^2)\). Hence every superlevel set lies in a fixed bounded region of the rescaled plane. Uniform Taylor expansions there, the zero-measure boundary, and convergence of the area density to \(1\) imply convergence in \(L^1\) of the rescaled unnormalized probability densities to \(\mathbf1_{\mathcal R_\lambda}\). Since the Jacobian is \(dx\,dy=\delta^3 du\,dv=h^{3/2}du\,dv\), this proves the probability law and total-variation convergence after conditioning.

**5. Exact area and pinch.** Write \(a=2\sqrt2\lambda\) and \(b=1-2\sqrt2\lambda^2\). Integrating the heights of the vertical sections gives
\[
\mathcal A(\lambda)=2\int_{-a}^{a}\max\{0,b+u^2/(2\sqrt2)\}\,du.
\]
Evaluating the polynomial integral and, when \(b<0\), subtracting the negative central interval \(|u|<\sqrt{8\lambda^2-2\sqrt2}\), gives exactly the stated \(\mathcal A(\lambda)\). The central vertical section vanishes at \(\lambda=2^{-3/4}\), which proves the connected-to-two-lobe pinch. Binomial expansion at large \(\lambda\) yields
\[
\mathcal A(\lambda)=\lambda^{-1}+\frac{\sqrt2}{24}\lambda^{-3}+O(\lambda^{-5}),
\]
consistent with the outer (fixed-shape) coefficient on the common asymptotic scale. This last consistency statement is an expansion of the explicit scaling function, not a claim of a uniform two-parameter remainder beyond the fixed-\(\lambda\) theorem.

## Verification

A self-contained numerical diagnostic program is provided at `checks/clearance_quadrature.py`; it requires Python 3 and SciPy, and evaluates the exact one-dimensional area integral obtained by integrating the Klein density in the \(y\)-direction. It compares the predicted coefficients with exact quadrature at two fixed nonsquare shapes, four positive critical parameters on both sides of the pinch, and the exact square. Nine deterministic comparisons pass, with the largest relative discrepancy below \(0.009\). The area integral follows directly by elementary antidifferentiation of \((1-x^2-y^2)^{-3/2}\); it is not Monte Carlo. These numerical checks are supplementary: the preceding local-limit and exact-integration arguments establish the infinite-domain claims.

## Relationship to prior work

Izmestiev (2014, arXiv:1408.2247) develops Klein-model hyperbolic isometries and circular cross-ratios; its full text concerns porisms and does not address pointwise clearance superlevel areas. Xu (2014, arXiv:1410.4052) concerns geodesic-chord intersection lengths under Liouville measure, not uniformly sampled points in an ideal quadrilateral. Published geometry work on the same ideal-quadrilateral family establishes the exact inradius and the symmetry-breaking **count and positions** of largest inscribed disks. Those facts are used in step 1 and are not claimed as new. Published results on area-uniform points of ideal polygons establish **small** nearest-side distance and a renormalized logarithmic boundary-layer coefficient; they do not imply the upper-end probability constants or the singular near-square two-scale limit. The proposed contribution is the exact fixed-shape rare-tail constants, the critical \(h^{3/2}\) crossover with its explicit nonanalytic area, and conditional blow-up geometries. A literature search cannot prove absolute historical novelty; specialized general inner-parallel-area formulas remain a priority risk.

## Limitations

Only geodesically convex **ideal** quadrilaterals in the complete curvature-\(-1\) plane and hyperbolic-area-uniform interior points are covered. There is no assertion for finite-vertex quadrilaterals, for polygons with more than four sides, or for other sampling measures. The nonsquare and square asymptotics are fixed-shape limits; the critical result fixes \(\lambda>0\) before sending \(h\) to zero. No uniform estimate covering \(\lambda\to0\) or \(\lambda\to\infty\) simultaneously with \(h\downarrow0\) is asserted. Numerical quadrature is finite evidence, not a proof; independent mathematical verification and exhaustive historical-priority validation have not been performed.

## References

- I. Izmestiev, *A porism for cyclic quadrilaterals, butterfly theorems, and hyperbolic geometry*, arXiv:1408.2247 (first public preprint, 10 August 2014). https://arxiv.org/abs/1408.2247
- B. Xu, *On the Ambartzumian-Pleijel identity in hyperbolic geometry*, arXiv:1410.4052 (first public preprint, 15 October 2014). https://arxiv.org/abs/1410.4052
- *A two-inball symmetry breaking theorem for ideal hyperbolic quadrilaterals* (2026), previously published geometric classification of their inradius and maximizing disk centers; its classification is used here as a known lemma. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-two-inball-symmetry-breaking-theorem-for-ideal-hyperbolic-quad--94e6734758c9
- *The logarithmic boundary-distance law and a renormalized shape invariant for ideal hyperbolic polygons* (2026), previously published small-clearance and ideal-triangle results; these are distinct from the present upper-clearance asymptotics. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-logarithmic-boundary-distance-law-and-a-renormalized-shape-i--1d7379fbdbb6
