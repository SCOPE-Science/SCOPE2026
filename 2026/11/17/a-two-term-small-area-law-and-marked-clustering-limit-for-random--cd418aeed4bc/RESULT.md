# A two-term small-area law and marked clustering limit for random cyclic quadrilaterals

## Finding

Let \(Z_1,Z_2,Z_3,Z_4\) be independent arclength-uniform points on the Euclidean unit circle, and let \(A\) be the area of their convex quadrilateral in circular order. As \(t\downarrow0\),
\[
\boxed{\Pr(A<t)=\frac{t}{\pi}+C_*t^{5/3}+o(t^{5/3}),}
\qquad
\boxed{C_*=\frac{1}{24\pi^3}\int_{\Delta}
\frac{(1-u)^2+(1-v)^2+(1-w)^2}{[\frac14(1-u)(1-v)(1-w)]^{5/3}}\,du\,dv,}
\]
where \(\Delta=\{(u,v,w):u,v,w>0,\ u+v+w=1\}\) is parameterized by \((u,v)\), \(w=1-u-v\). The integral is absolutely convergent, positive, and numerically \(C_*\approx0.242278704743\).

There is also an explicit *marked* rare-event limit. Given \(A<t\), with probability tending to one a unique circular gap between successive vertices exceeds \(2\pi-\delta\) for any fixed sufficiently small \(\delta>0\). Reading the other three consecutive gaps as \((a,b,c)\), put
\[
W=a+b+c,\quad (U,V,H)=(a,b,c)/W,\quad
h(u,v,w)=\tfrac14(1-u)(1-v)(1-w),\quad
R_t=W[h(U,V,H)/t]^{1/3}.
\]
Then, conditional on \(A<t\), the joint law of the gap index, \((U,V,H)\), \(R_t\), and a rotational orientation converges weakly to a product law: the gap index is uniform on four possibilities, the orientation uniform on the circle, \(R\sim\operatorname{Beta}(3,1)\), and the normalized gap fractions have density
\[
\boxed{f(u,v)=\frac{4}{\pi^2(1-u)(1-v)(1-w)},\qquad w=1-u-v.}
\]
All these marks are independent in the limit. Consequently \(A/t\), conditional on \(A<t\), converges to an independent uniform variable on \([0,1]\). The result does **not** claim an unknown general scalar area distribution: a previously published conditional area law given the diagonal angle already provides a complete integral representation of that marginal.

## Assumptions and scope

Each point has normalized uniform arclength measure and the four samples are independent; ties have probability zero. Area is the ordinary nonnegative Euclidean convex-polygon area, not the area enclosed by circular arcs. Circular gaps are in radians; select one labeled point as the starting vertex, then order the remaining points counterclockwise. The large-gap index is defined only when there is exactly one circular gap above \(2\pi-\delta\). Define marks arbitrarily on the exceptional configurations, whose conditional probability tends to zero. The orientation is the angle of the starting labeled point; it is uniform and independent of all gaps exactly. Convergence of the full marked law means weak convergence on the product of the finite index, open simplex, unit interval and circle; no total-variation assertion is made for the rescaled marks.

## Proof

**1. Exact gap density and area factorization.** Fix one labeled sampled point as angular origin. The circular gaps \((G_1,G_2,G_3,G_4)\), summing to \(2\pi\), have the \(2\pi\)-scaled \(\operatorname{Dirichlet}(1,1,1,1)\) law. Their density in three gap coordinates is \(6/(2\pi)^3\). Set \(a=G_1\), \(b=G_2\), \(c=G_3\), \(G_4=2\pi-a-b-c\). The shoelace formula and a trigonometric identity give
\[
A=\frac12\left(\sin a+\sin b+\sin c-\sin(a+b+c)\right)
=2\sin\frac{a+b}{2}\sin\frac{b+c}{2}\sin\frac{c+a}{2}.
\]
The same factorization holds after cyclic permutation of the four gaps. All factors are nonnegative because the paired gap sums lie in \((0,2\pi)\).

**2. Localization of very small area.** In the closed gap tetrahedron, the zero set of \(A\) is precisely the union of its six edges (configurations with at most two nonzero gaps). Choose a fixed small \(\delta>0\) and four disjoint vertex neighborhoods \(\{G_j>2\pi-\delta\}\). On each compact subsegment of an edge outside those neighborhoods, two gaps remain bounded away from zero and the area is bounded below by a constant times the sum of the other two small gaps. Hence the volume of its sublevel set is \(O_\delta(t^2)\). A finite covering of the compact remainder, where area is positive, completes the estimate that the probability outside the four vertex neighborhoods is \(O_\delta(t^2)=o(t^{5/3})\).

**3. Uniform radial expansion at one vertex.** Work where \(G_4>2\pi-\delta\), writing \((a,b,c)=W(u,v,w)\) with \((u,v,w)\in\Delta\) and \(0<W<\delta\). The Jacobian is \(W^2\,dW\,du\,dv\). Put \(h(u,v,w)=\frac14(1-u)(1-v)(1-w)\) and \(Q(u,v,w)=(1-u)^2+(1-v)^2+(1-w)^2\). The sine product has the *uniform* Taylor expansion
\[
A=W^3h(u,v,w)\left(1-\frac{W^2Q(u,v,w)}{24}+O(W^4)\right).
\]
For \(\delta\) small, area is strictly increasing in \(W\). At a fixed interior fraction, set \(W_0=(t/h)^{1/3}\). Inverting the series gives the radial threshold
\[
W_t=W_0\left(1+\frac{Q}{72}W_0^2+O(W_0^4)\right),\quad
\frac{W_t^3}{3}=\frac{t}{3h}+\frac{Q}{72}\left(\frac{t}{h}\right)^{5/3}+O((t/h)^{7/3}).
\]
The expansion is pointwise in fractions. Crucially, it is not integrated termwise without controlling the corners of \(\Delta\).

**4. Integrability and boundary control.** Near a vertex of \(\Delta\), \(h\) is comparable to the sum of the other two barycentric coordinates. Therefore \(h^{-\alpha}\) is integrable over \(\Delta\) for every \(\alpha<2\); in particular \(h^{-1}\) and \(Qh^{-5/3}\) are integrable. The set \(\{h<\eta\}\) has area \(O(\eta^2)\), while \(\int_{h<\eta}h^{-1}=O(\eta)\). This makes the cubic radial-volume truncation \(\min\{\delta^3,t/h\}/3\) differ from \(t/(3h)\), after integration, by \(O(t^2)\). For the exact and cubic radial roots, the difference between their *capped* cubes is zero where \(W_0\ge\delta\), and otherwise is bounded by \(C W_0^5\); the pointwise limit of this difference divided by \(t^{5/3}\) is \(Q/(24h^{5/3})\). Dominated convergence against the integrable \(h^{-5/3}\) gives the one-vertex volume
\[
\frac{t}{3}\int_\Delta h^{-1}\,du\,dv
+\frac{t^{5/3}}{72}\int_\Delta Qh^{-5/3}\,du\,dv+o(t^{5/3}).
\]
The four vertices have equal contributions. Multiplying by their number and the Dirichlet density gives the factor \(4\cdot6/(2\pi)^3=3/\pi^3\).

**5. Leading constant.** Writing \(s=u+v=1-w\), partial fractions yield
\[
\int_\Delta\frac{du\,dv}{(1-u)(1-v)(1-w)}
=\int_0^1\frac{-2\log(1-s)}{s(2-s)}\,ds
=\frac{\pi^2}{6}+\frac{\pi^2}{12}=\frac{\pi^2}{4}.
\]
Since \(h^{-1}=4/[(1-u)(1-v)(1-w)]\), the leading coefficient is \((3/\pi^3)(1/3)\pi^2=1/\pi\); the second coefficient is exactly the displayed \(C_*\). This proves the two-term expansion.

**6. Conditional shape.** Restrict to one vertex sector and change variables from \(W\) to \(r=W(h/t)^{1/3}\). After dividing by its asymptotic probability \(t/(4\pi)\), the limiting joint density is \(3r^2\,dr\cdot h^{-1}\,du\,dv/\pi^2\) for \(0<r<1\). The integrable domination in step 4 justifies this convergence first on compact subsets of the open simplex and then globally by tightness. Therefore the shape density equals \(h^{-1}/\pi^2=4/[\pi^2(1-u)(1-v)(1-w)]\) and the radial variable is independent \(\operatorname{Beta}(3,1)\). Symmetry assigns probability \(1/4\) to each large-gap index. Finally \(A/t=R_t^3(1+o(1))\) in conditional probability, and \(R^3\) is uniform on \([0,1]\). Rotational invariance gives the separate uniform orientation mark.

## Verification

The standalone `verify_small_area.py` evaluates \(C_*\) by independent adaptive two-dimensional integration, verifies the \(\pi^2/4\) leading integral, and samples 4,000,000 independent quadruples directly on the circle. At thresholds \(0.2,0.1,0.05,0.02,0.01\) it compares measured probabilities against \(t/\pi+C_*t^{5/3}\). The reported second coefficient is \(0.242278704743\), and the checker prints `CYCLIC_QUAD_SMALL_AREA_TWO_TERM_DIAGNOSTIC_OK`. Tolerances include sampling fluctuations and neglected higher-order terms. Run `python verify_small_area.py` with Python 3, NumPy and SciPy. Numerical diagnostics are not a proof of infinite asymptotics or historical novelty.

## Relationship to prior work

Finch (2016), especially the random area analysis, studies moments of four circle-uniform points and motivates questions about the full area distribution; it does not give this local lower-tail expansion or marked collapse law. Koroleva–Nikitin (2013) study *near-maximum*, not near-zero, areas of random inscribed polygons. The published result *Conditional area law for random cyclic quadrilaterals at a fixed diagonal angle* gives the **full scalar conditional distribution** of area for a fixed diagonal angle, and hence determines the unconditional scalar area law implicitly after integration over that angle. Thus neither the general scalar distribution nor its recoverability in principle is asserted as new. The present result explicitly extracts a nonanalytic second lower-tail term and resolves the additional three-dimensional conditional *gap-shape* law, which is not determined by a one-dimensional area-versus-angle marginal. The published *Exact perimeter–area second moments of a random cyclic quadrilateral* establishes moment values, but not the rare-area marks or second tail coefficient. Priority of the exact asymptotic and marked law remains provisional, especially given possible older studies of degenerate random cyclic polygons.

## Limitations

The limit is for exactly four i.i.d. uniform-arclength samples on the unit circle, not disk-uniform samples, nonuniform boundary samples, or larger polygons. The coefficient \(C_*\) is supplied as a convergent two-dimensional integral rather than an elementary closed form. The convergence of conditional marked shapes is weak, not asserted in total variation. The remainder is \(o(t^{5/3})\), not a certified uniform finite-threshold error bound. Finite simulations do not establish an asymptotic theorem. Historical priority and independent mathematical validation have not been certified.

## References

1. S. R. Finch, *Random Cyclic Quadrilaterals*, arXiv:1610.00510v1, first submitted 3 October 2016, particularly area/moment discussion. https://arxiv.org/abs/1610.00510
2. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360v1, 7 January 2013, Section 2.2 (near-maximum polygon areas). https://arxiv.org/abs/1301.1360
3. *Conditional area law for random cyclic quadrilaterals at a fixed diagonal angle*, published mathematical research record, 25 October 2026, full result at https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-conditional-area-law-for-random-cyclic-quadrilaterals-at-a-fixed--e05b854129e9
4. *Exact perimeter–area second moments of a random cyclic quadrilateral*, published mathematical research record, 12 October 2026, full result at https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-perimeter-area-second-moments-of-a-random-cyclic-quadrilat--1c13b772d78d
