# Sharp packing-contact threshold before redundancy in three orthogonal cylinders

## Finding
Let \(0<\alpha\le\beta\le\gamma\) be the squared radii of three infinite right circular cylinders with mutually perpendicular, concurrent coordinate axes. Define their compact intersection
\[
K_{\alpha,\beta,\gamma}=\{(x,y,z)\in\mathbb R^3:x^2+y^2\le\alpha,\quad y^2+z^2\le\beta,\quad z^2+x^2\le\gamma\}.
\]
Among **all translated axis-parallel rectangular boxes** contained in this body, there is exactly one of maximal volume. Put
\[
\Delta=\sqrt{\alpha^2-\alpha\beta+\beta^2},\quad
v_*={\alpha+\beta-\Delta\over3},\quad
\gamma_*={\alpha+\beta+2\Delta\over3}.
\]
The unique box is \([-u,u]\times[-v,v]\times[-w,w]\), of volume \(8uvw\), with squared half-sides \(U=u^2,V=v^2,W=w^2\) given by the **complete two-phase law**
\[
\boxed{(U,V,W)=
\begin{cases}
\bigl((\alpha+\gamma-\beta)/2,(\alpha+\beta-\gamma)/2,(\beta+\gamma-\alpha)/2\bigr),&\beta\le\gamma\le\gamma_*,\\
\bigl(\alpha-v_*,v_*,\beta-v_*\bigr),&\gamma\ge\gamma_*.
\end{cases}}
\]
One has \(\beta<\gamma_*<\alpha+\beta\), so the optimal box stops touching the third cylinder **strictly before that cylinder becomes geometrically redundant**. Thus, for every \(\gamma_*<\gamma<\alpha+\beta\), the convex body genuinely changes with \(\gamma\) but its unique optimal box and volume remain exactly constant. At \(\gamma=\gamma_*\) all three cylinder inequalities are equalities at every box vertex, despite the third constraint having zero optimality multiplier.

For fixed \(\alpha,\beta\), the function \(f(\gamma)=\log\bigl(8uvw\bigr)\), defined for \(\gamma\ge\beta\), is continuously differentiable at \(\gamma_*\) but not twice differentiable there. Writing \((U_*,V_*,W_*)=(\alpha-v_*,v_*,\beta-v_*)\),
\[
\lim_{\gamma\uparrow\gamma_*}f''(\gamma)=-\frac18\left(U_*^{-2}+V_*^{-2}+W_*^{-2}\right)<0,
\qquad f''(\gamma)=0\quad(\gamma>\gamma_*).
\]
At the symmetric normalization \(\alpha=\beta=1\), the contact threshold is \(\gamma_*=4/3\), the volume plateau equals \(16/(3\sqrt3)\), and the redundancy threshold is \(\gamma=2\).

## Assumptions and scope
All three cylinders are *solid* and have infinite height, with axes the three mutually perpendicular coordinate lines. Their squared radii are positive. Arbitrary permutation of the original three radii can be realized by relabeling coordinate axes, so the ordering is without loss of generality. An **axis-parallel rectangular box** is any Cartesian product of three nondegenerate closed intervals, of unrestricted center and positive side lengths, whose faces are parallel to the coordinate planes. Competing boxes with rotated faces or general parallelepiped edges are not included. The classification concerns Euclidean volume, not surface area or a maximal ellipsoid.

## Proof
**1. Centering and exact feasible region.** Write a candidate box as
\(B=\prod_{i=1}^3[t_i-h_i,t_i+h_i]\) with \(h_i>0\). Maximizing any quadratic cylinder expression over the box replaces the corresponding coordinate magnitudes by \(|t_i|+h_i\). Hence containment is equivalent to
\[
(|t_1|+h_1)^2+(|t_2|+h_2)^2\le\alpha,\quad
(|t_2|+h_2)^2+(|t_3|+h_3)^2\le\beta,\quad
(|t_3|+h_3)^2+(|t_1|+h_1)^2\le\gamma.
\]
In particular, the centered box with the same half-sides is feasible, and it has the same volume. Set \(U=h_1^2,V=h_2^2,W=h_3^2\). Maximizing box volume is therefore equivalent to maximizing
\(g(U,V,W)=\log U+\log V+\log W\) over
\[
\mathcal P=\{U,V,W>0:U+V\le\alpha,\quad V+W\le\beta,\quad W+U\le\gamma\}.
\]
There is a positive feasible point, and a maximizing point cannot lie on a coordinate-zero boundary. Since \(g\) is strictly concave and \(\mathcal P\) is convex and bounded, the optimal triple is unique. Both the first two constraints must be active at the optimum: at least two constraints must be active, because a coordinate belonging only to a single active inequality could otherwise be increased. More formally, in the Karush–Kuhn–Tucker (KKT) system below, the stationarity of each coordinate requires at least one of its two incident multipliers to be positive; a single positive multiplier cannot cover all three coordinates. If exactly two constraints are active, the largest right-hand-side constraint is the only one eligible to be slack, as shown in Step 3.

**2. Three-active candidate.** Suppose all three inequalities are equalities. Solving the linear system gives
\[
U=(\alpha+\gamma-\beta)/2,\quad V=(\alpha+\beta-\gamma)/2,\quad W=(\beta+\gamma-\alpha)/2.
\]
The multipliers for constraints \(U+V\le\alpha\), \(V+W\le\beta\), \(W+U\le\gamma\), respectively, must satisfy
\[
\lambda_1=(U^{-1}+V^{-1}-W^{-1})/2,\quad
\lambda_2=(V^{-1}+W^{-1}-U^{-1})/2,\quad
\lambda_3=(W^{-1}+U^{-1}-V^{-1})/2.
\]
For \(\beta\le\gamma<\alpha+\beta\), the coordinates are positive, and \(W\ge U\ge V\). Consequently \(\lambda_1,\lambda_2>0\). The remaining multiplier \(\lambda_3\) decreases strictly with \(\gamma\), because its derivative is
\(-\tfrac14(U^{-2}+V^{-2}+W^{-2})\). At \(\gamma=\beta\) it is positive, and as \(\gamma\uparrow\alpha+\beta\) it tends to negative infinity. There is one zero of \(\lambda_3\).

**3. Exact transition and two-active candidate.** With the third multiplier zero, stationarity reads
\[
\frac1U=\lambda_1,\qquad \frac1V=\lambda_1+\lambda_2,\qquad\frac1W=\lambda_2.
\]
The two active constraints give \(U=\alpha-V\), \(W=\beta-V\), and hence
\[
\frac1V=\frac1{\alpha-V}+\frac1{\beta-V}
\quad\Longleftrightarrow\quad
3V^2-2(\alpha+\beta)V+\alpha\beta=0.
\]
The only root in \(0<V<\min(\alpha,\beta)\) that satisfies this equation is \(v_*\). (The other root exceeds the smaller constraint bound.) Thus the third cylinder is slack exactly when \(\gamma>U+W=\alpha+\beta-2v_*=\gamma_*\). At equality the two candidates coincide. Direct inequalities show \(\gamma_*>\beta\): writing \(\Delta^2=(\beta-\alpha/2)^2+3\alpha^2/4\), one has \(2\Delta>2\beta-\alpha\). Also \(\Delta<\alpha+\beta\), so \(\gamma_*<\alpha+\beta\). For \(\gamma\le\gamma_*\), Step 2 yields nonnegative KKT multipliers; for \(\gamma\ge\gamma_*\), Step 3 yields the nonnegative multipliers \((1/U,1/W,0)\), with the third feasibility inequality satisfied. In either case, concavity and the KKT supporting-hyperplane inequality prove unique global optimality: for every feasible positive \((X,Y,Z)\),
\[
g(X,Y,Z)\le g(U,V,W)+(X-U)/U+(Y-V)/V+(Z-W)/W
\le g(U,V,W).
\]
The second inequality is the nonnegative linear combination of the three constraint differences, with complementary slackness.

To justify the exclusivity statement without assuming in advance which constraints are active, note that the displayed candidates satisfy every KKT condition in the stated regimes, so strict concavity alone identifies the unique optimum over the entire feasible region. The first two active equalities in these candidates are therefore not an extra assumption.

**4. Center uniqueness.** In both regimes the optimal \(U+V=\alpha\) and \(V+W=\beta\). If an off-center axis-parallel box of the same optimal half-side lengths fitted, its first two cylinder inequalities from Step 1 would force \(t_1=t_2=t_3=0\). Since the optimal half-side lengths are unique, the box itself is unique among all translations.

**5. Two distinct thresholds.** For all points in the first two cylinders,
\(x^2+z^2=(x^2+y^2)+(y^2+z^2)-2y^2\le\alpha+\beta\), so the third cylinder is redundant if \(\gamma\ge\alpha+\beta\). If \(\gamma<\alpha+\beta\), choose \(\delta>0\) small with \(\alpha+\beta-2\delta>\gamma\). The point \((\sqrt{\alpha-\delta},0,\sqrt{\beta-\delta})\) lies strictly inside the first two cylinders and outside the third, proving genuine nonredundancy. Combining this with \(\gamma_*<\alpha+\beta\) proves the entire invisibility window.

**6. Sharp smoothness loss.** Below \(\gamma_*\), differentiate \(f=\log8+\tfrac12(\log U+\log V+\log W)\), using \(U'=W'=1/2\), \(V'=-1/2\), to obtain
\[
f'(\gamma)=\frac14(U^{-1}-V^{-1}+W^{-1})=\lambda_3/2,
\qquad f''(\gamma)=-\frac18(U^{-2}+V^{-2}+W^{-2}).
\]
Above \(\gamma_*\), all three dimensions are fixed, so \(f'=f''=0\). At the threshold, \(\lambda_3=0\), and the positive finite limiting dimensions prove \(C^1\) matching, while the negative one-sided second derivative proves failure of \(C^2\). For \(\alpha=\beta=1\), substitution gives \(v_*=1/3\), \(U_*=W_*=2/3\), \(\gamma_*=4/3\), and the announced volume and redundancy values. This completes the proof.

## Verification
The standalone Python file `check_tricylinder_boxes.py` uses only the standard library. Running `python3 check_tricylinder_boxes.py` checks 2,507 parameter triples, with 80 separately generated feasible competitors for each, all active/slack constraints and KKT identities, the exact equal-radius benchmark, and the one-sided quadratic loss at the threshold. Independent local optimization was also performed on random positive squared-radius triples during derivation, agreeing with the explicit candidates. These finite checks corroborate but **do not replace** the analytic proof for all positive radii. The checker is reproducible without a network connection.

## Relationship to prior work
The equal-radius tricylinder and its classical volume and surface area were studied long before this note; in particular the earlier geometric literature does **not** make the existence of the solid itself new. May (2013) concerns flattened two-cylinder surface-intersection geometry, not maximal boxes. Behroozi (2019) develops general optimization frameworks for axis-aligned inscribed boxes in convex sets. Its generic model provides an applicable way to compute instances but does not state the closed three-cylinder threshold, the nonredundant interval of unchanged box volume, or the \(C^1\)-not-\(C^2\) phase transition. The published two-cylinder John–Löwner work concerns ellipsoids, not axis-parallel rectangular boxes; a published equal-radius tricylinder central-section study concerns sectional area, not unequal-radius box packing. These comparisons distinguish the present explicit geometry from underlying convex-programming principles; they do not establish absolute historical priority.

## Limitations
The theorem is **not** a claim about arbitrary rotated boxes, arbitrary parallelepipeds, maximal ellipsoids, or finite-length cylinders. The smoothness claim varies the *squared* largest radius \(\gamma\) with the other squared radii fixed. At a tie of the radii, ordering and relabeling are harmless, but no differentiability across changes of the sorted-label convention is claimed. The earliest exact-day archival seed used here is 2013-12-12; the older tricylinder construction is documented by month/year or year only in inspected accessible sources, and no day is imputed to those sources. Historical-priority verification remains provisional, and no independent mathematical audit has been performed.

## References
1. M. P. May, “A closed-form solution for the flat-state geometry of cylindrical surface intersections bounded on all sides by orthogonal planes,” arXiv:1312.3604, first public posting 2013-12-12. https://arxiv.org/abs/1312.3604.
2. P. Bourke, “What object is a circle in plan, front and side views?”, *Intersecting Cylinders*, dated March 1992 (exact day not established); and “Steinmetz solid,” dated December 2003 (exact day not established). https://www.paulbourke.net/geometry/cylinders/.
3. E. W. Weisstein, “Steinmetz Solid,” *MathWorld*, consulted 2026-11-17. https://mathworld.wolfram.com/SteinmetzSolid.html.
4. M. Behroozi, “Largest Inscribed Rectangles in Geometric Convex Sets,” arXiv:1905.13246, first public posting 2019-05-30. https://arxiv.org/abs/1905.13246.
5. “Exact John–Löwner ellipsoids and an angle-independent ratio for intersecting cylinders,” published 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-john-l-wner-ellipsoids-and-an-angle-independent-ratio-for--bef1cf01440b.
6. “Exact twelve-sector sections and cubic directional anisotropy of the Steinmetz tricylinder,” published 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-twelve-sector-sections-and-cubic-directional-anisotropy-of--428486a75562.
