# The three-fifths rare-area law of the quartic Lamé oval

## Finding
Let \(\Gamma=\{(x,y)\in\mathbb R^2:x^4+y^4=1\}\), with Euclidean perimeter \(L\). Let \(P_1,P_2,P_3\) be independent, Euclidean-arclength-uniform points of \(\Gamma\), and let \(A=\frac12|\det(P_2-P_1,P_3-P_1)|\) be their unsigned Euclidean triangle area. Then
\[
\boxed{\Pr(A\le t)\sim C_4\,t^{3/5}\quad(t\downarrow0),\qquad
C_4=\frac{4I_4}{L^3}\approx1.77940494420824,}
\]
where the completely explicit universal homogeneous-volume constant is
\[
I_4=2\,8^{3/5}\sqrt{\frac\pi6}\,\frac{\Gamma(1/10)}{\Gamma(3/5)}3^{1/10}
\int_0^1\frac{dz}{[z(1-z)]^{3/5}(1-z+z^2)^{1/10}}\approx153.7442264223871.
\]
Here \(\Gamma(\cdot)\) in the displayed constant denotes Euler's gamma function, not the curve. The perimeter is the independently defined Euclidean arclength of \(\Gamma\), numerically \(L=7.017697943564\ldots\).

There is a stronger marked geometric limit. Let \(q_1=(1,0)\), \(q_2=(0,1)\), \(q_3=(-1,0)\), \(q_4=(0,-1)\). For a sufficiently small fixed choice of disjoint neighborhoods of these four points, conditioned on \(A\le t\), with probability tending to one all three samples lie in the same neighborhood. Their common tip becomes asymptotically uniform on the four tips. If \(y_1,y_2,y_3\) are the signed local tangent coordinates relative to that tip, the conditional joint law of \((t^{-1/5}y_1,t^{-1/5}y_2,t^{-1/5}y_3)\) converges in **total variation** to the probability density
\[
\boxed{I_4^{-1}{\bf1}_{\{H(u_1,u_2,u_3)\le1\}}}\quad\text{on }\mathbb R^3,
\]
independently of the asymptotically uniform tip, where
\[
H(u)=\frac{1}{8}(u_{(2)}-u_{(1)})(u_{(3)}-u_{(2)})(u_{(3)}-u_{(1)})
\sum_{1\le i\le j\le3}u_i u_j.
\]
The sorted coordinates satisfy \(u_{(1)}\le u_{(2)}\le u_{(3)}\); the last factor is nonnegative because it equals \(\frac12[(\sum u_i)^2+\sum u_i^2]\). Thus \(H\ge0\), \(H\) is homogeneous of degree five, and \(I_4=\int_{\mathbb R^3}{\bf1}_{\{H(u)\le1\}}du\in(0,\infty)\). No independence among the three limiting coordinates is asserted.

## Assumptions and scope
The curve is the *entire* quartic Lamé oval of unit semiaxes, smooth and strictly convex, with exactly four points of zero curvature. Sampling is independent with normalized Euclidean arclength, not uniform polar angle, affine arclength, or area in the enclosed region. The threshold \(t\) is ordinary Euclidean triangle area. The asymptotics apply to this fixed curve; no parameter-uniform statement for all Lamé exponents is claimed. The marked limit uses signed Euclidean tangent coordinates in a consistent orthonormal chart at each tip; any fixed choice of tangent orientations produces the same limiting density because \(H(-u)=H(u)\).

## Proof
**1. The only zero-area configurations.** Since \(\Gamma\) is strictly convex, a straight line meets its boundary in at most two distinct points. Hence a triangle with vertices on \(\Gamma\) has zero area precisely when two of its vertices coincide. On the part of this zero set where exactly two vertices coincide and the third remains distinct, the area vanishes *linearly* in the arclength difference of the colliding pair: the linear coefficient is half the chord length times a positive sine, equivalently half the positive distance of the third vertex from the tangent at the collision point. Uniform compactness away from the triple diagonal therefore makes these neighborhoods contribute \(O(t)\) to \(\Pr(A\le t)\).

**2. Triple clusters away from the four tips.** If three points coalesce at a point where curvature \(\kappa>0\), order their small successive arclength gaps \(a,b>0\). The determinant expansion is \(A=\kappa ab(a+b)/4\,(1+o(1))\), uniformly for the nearby base point and sufficiently short gaps. The elementary two-dimensional sublevel volume of \(ab(a+b)\le h\) is \(\frac12B(1/3,1/3)h^{2/3}\). A finite cover of any closed subset of the curve disjoint from the four tips therefore gives \(O_\delta(t^{2/3})\) for the triples clustering there, for each fixed excluded tip radius \(\delta>0\). Together with Step 1, configurations outside the four neighborhoods where all three points approach the *same* flat tip contribute \(O_\delta(t^{2/3})+O_\delta(t)=o(t^{3/5})\). This covering argument uses only local smoothness and strict convexity and does not assume a positive global minimum curvature.

**3. Exact quartic tangent model.** Near \((1,0)\), use signed tangent coordinate \(y\). The curve is
\[
(x(y),y)=\left((1-y^4)^{1/4},y\right),\qquad
x(y)=1-\frac{y^4}{4}+O(y^8).
\]
Its arclength density in this coordinate is \(j(y)=\sqrt{1+x'(y)^2}=1+O(y^6)\). Let \(A_\Gamma(y_1,y_2,y_3)\) be the triangle area of the three corresponding curve points. For \(y_i=t^{1/5}u_i\), the determinant identity and Taylor expansion give locally uniformly
\[
\frac{A_\Gamma(t^{1/5}u_1,t^{1/5}u_2,t^{1/5}u_3)}{t}\longrightarrow H(u_1,u_2,u_3).
\]
Indeed the unsigned triangle area formed by the graph \(x=1-y^4/4\) is exactly \(H(y)\). To check, order \(y_1<y_2<y_3\), write \(a=y_2-y_1\), \(b=y_3-y_2\), \(m=(y_1+y_2+y_3)/3\); the second divided difference of \(y^4\) yields
\[
H(y)=\frac{ab(a+b)}8\left(6m^2+\frac{a^2+ab+b^2}{3}\right).
\]
The formula extends continuously to coincident arguments and to any ordering.

**4. An integrable majorant.** Define \(f(y)=1-(1-y^4)^{1/4}\), a locally convex function with \(f''(y)=3y^2+O(y^6)\). For a sufficiently small fixed tip chart \(|y|<\delta\), \(f''(y)\ge\frac12(3y^2)\). On three ordered abscissae, the triangle area for the graph of any convex function is half the Vandermonde product times a second divided difference, which is a *positive linear functional* of its second derivative (the standard positive Peano kernel). Consequently comparison of second derivatives gives
\[
A_\Gamma(y_1,y_2,y_3)\ge\frac12H(y_1,y_2,y_3)
\quad(|y_i|<\delta).
\]
The rescaled indicator of \(A_\Gamma\le t\) is therefore bounded by \({\bf1}_{\{H(u)\le2\}}\), which is integrable once finiteness of \(I_4\) is established in Step 5. The level set \(H=1\) is null: in the variables of Step 5, for each fixed \(w,z\) it contains exactly one radial value. The densities \(j\) are bounded and tend to one. Dominated convergence on \(\mathbb R^3\) proves that each flat tip contributes precisely \((I_4/L^3)t^{3/5}+o(t^{3/5})\), and proves convergence of its *unnormalized rescaled conditional density in* \(L^1\).

**5. Exact volume of the homogeneous sublevel.** In the ordered sector \(u_1<u_2<u_3\), write \(a=u_2-u_1>0\), \(b=u_3-u_2>0\), \(m=(u_1+u_2+u_3)/3\). The Jacobian of \((u_1,u_2,u_3)\mapsto(m,a,b)\) has absolute value one. There are six sectors. Put \(r=a+b\), \(z=a/r\in(0,1)\), \(m=rw\), and \(q(z)=(1-z+z^2)/3\). The new volume element is \(dm\,da\,db=r^2\,dw\,dr\,dz\), while
\[
H=\frac{r^5}{8}z(1-z)[6w^2+q(z)].
\]
Integrating \(0<r<[8/(z(1-z)(6w^2+q(z)))]^{1/5}\) gives
\[
I_4=2\,8^{3/5}\int_0^1[z(1-z)]^{-3/5}
\int_{\mathbb R}(6w^2+q(z))^{-3/5}\,dw\,dz.
\]
The elementary integral \(\int_{\mathbb R}(6w^2+q)^{-3/5}dw=\sqrt{\pi/6}\,q^{-1/10}\Gamma(1/10)/\Gamma(3/5)\) proves the displayed one-dimensional formula. Its integrand is bounded by a constant times \(z^{-3/5}(1-z)^{-3/5}\), and is thus integrable at both endpoints: \(0<I_4<\infty\).

**6. Four-tip summation and marked total variation.** Rotations through multiples of \(\pi/2\) preserve both \(\Gamma\) and its arclength measure, hence all four tips give identical contributions. Step 2 is lower order, so their sum gives \(4I_4t^{3/5}/L^3\). Step 4 already supplies \(L^1\) convergence of each rescaled tip contribution; normalization by the total probability, with Step 2 showing that non-tip configurations have vanishing conditional mass, yields the stated total-variation mixture of four uniform tip labels and a common density \(I_4^{-1}{\bf1}_{H\le1}\). This proves both assertions.

## Verification
The standalone `verify.py` evaluates the perimeter via two independent coordinate systems, evaluates \(I_4\) via two independently organized integrals (Gamma-integrated mean and direct gap/mean cutoff), and uses 77 exact rational arithmetic determinant identities to check the quartic factorization. Running `python verify.py` produced:

```text
exact-rational identities passed: 77
perimeter L: 7.017697943564 independent chart: 7.0176979434992
homogeneous sublevel volume I: 153.74422642242 gap-integral: 153.74422642241
probability constant C=4I/L**3: 1.7794049442086
All diagnostics passed. Numerical checks are not an infinite-limit proof.
```

The preceding block is the original double-precision diagnostic, not a certificate for its last digits. The refined approximations above can be reproduced with `python3 verify_refined.py` (mpmath). It integrates the perimeter over one symmetry octant with a smooth endpoint and computes the gap integral in two ways: smoothing its endpoint by \(z=x^5/2\) on half of the interval, and using Euler's hypergeometric integral after the change of variable \(v=4z(1-z)\). The proof of the infinite asymptotic and total-variation limit is analytical (Steps 1–6); these scripts check computations, not the theorem in lieu of proof. For extremely small thresholds, convergence of finite-sample estimates can be slow because the limiting homogeneous sublevel has long integrable tails.

## Relationship to prior work
The classic unit-circle triangle-area problem and its maximal-area asymptotics are not claimed as new. Koroleva and Nikitin (first public 2013-01-07, arXiv:1301.1360) analyze maximum perimeter/area among random inscribed polygons on the **circle**, not the lower tail on a curvature-degenerate quartic oval. Zhao (journal public 2015-06-18; arXiv:1509.05485 first posted 2015-09-18) treats curvature measures and affine surface area for convex bodies, providing background on convex curvature but not this probability law. The published research record *A sharp small-area law for inscribed random triangles and the optimal affine sampling density* (2026-11-08) proves a \(t^{2/3}\) law for \(C^3\) ovals with **strictly positive curvature everywhere**. That theorem does not cover this curve: at a coordinate-axis tip \(\kappa(s)\sim3|s|^2\), so the prior curvature integral \(\int\kappa^{-2/3}ds\) diverges. Its coefficient cannot be substituted into this problem. It is credited as the closest result for the regular-curvature case, not presented as a new result here.

The general 1978 work of Silverman and Brown on short distances, flat triangles and Poisson limits treats clustering and collinearity in spatial data; publicly available abstracts do not establish the specific arclength-boundary quartic limit. Its complete text was not inspected, so that historical-priority risk remains explicit. Kendall's 1985 shape-density paper treats **area-uniform interior** points in a convex region, not independent arclength-uniform boundary points at isolated zero-curvature tips. Searches for quartic-superellipse and vanishing-curvature small-triangle laws disclosed no source with a direct matching assertion; non-discovery is not a novelty proof.

## Limitations
Only the fixed quartic Lamé oval and independent uniform Euclidean-arclength samples are included. No uniform transition law over changing Lamé exponent and no result for interior-uniform sampling is claimed. The embedded numerical checker is not an independent mathematical audit. The historical search is finite; independent priority review remains outstanding. No conclusion is drawn about maxima of triangle area, limiting laws of a sample minimum over growing sample sizes, or arbitrary curves with flat points.

## References
1. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360, first public 2013-01-07, https://arxiv.org/abs/1301.1360.
2. Yiming Zhao, *On \(L_p\) Affine Surface Area and Curvature Measures*, published online 2015-06-18, https://doi.org/10.1093/imrn/rnv178; open preprint arXiv:1509.05485 (2015-09-18).
3. *A sharp small-area law for inscribed random triangles and the optimal affine sampling density*, published research record dated 2026-11-08, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-a-sharp-small-area-law-for-inscribed-random-triangles-and-the-op--36a2639eeafd.
4. Bernard W. Silverman and Tim Brown, *Short distances, flat triangles and Poisson limits*, Journal of Applied Probability **15** (1978), 815–825, https://doi.org/10.2307/3213436.
5. D. G. Kendall, *Exact distributions for shapes of random triangles in convex sets*, Advances in Applied Probability **17** (1985), 308–329, https://doi.org/10.2307/1427143.
6. E. W. Weisstein, *Circle Triangle Picking*, MathWorld, https://mathworld.wolfram.com/CircleTrianglePicking.html.
