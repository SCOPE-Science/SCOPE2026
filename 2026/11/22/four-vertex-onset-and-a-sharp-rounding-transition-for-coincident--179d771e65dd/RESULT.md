# Four-vertex onset and a sharp rounding transition for coincident planar centroids

## Finding
Let \(K\subset\mathbb R^2\) be a compact convex body with interior and write \(K_t=K+tB\), where \(B\) is the closed unit disk and \(t\ge0\). Denote the uniform-area centroid of \(K_t\) by \(G(t)\) and its uniform-arclength boundary centroid by \(H(t)\). Call \(t>0\) an **isolated coincidence radius** if \(G(t)=H(t)\) and the equality is not identically true at every radius.

**Theorem (sharp polygonal onset and local phase law).**

1. Any planar convex body has at most one isolated coincidence radius. More precisely, let \(G,H,S\) be its area centroid, arclength-perimeter centroid, and curvature-weighted Steiner point. If they all coincide, \(G(t)=H(t)\) for every \(t\ge0\). Otherwise an isolated coincidence radius exists precisely when \(G,H,S\) are collinear and \(H\) lies strictly outside the closed line segment \([G,S]\); it is then unique, and the centroid path \(G(t)\) reverses direction there.
2. No nondegenerate triangle has an isolated coincidence radius. Every non-equilateral isosceles triangle has a strictly monotone centroid path, and every scalene triangle has a nonstraight, nonstationary centroid path. Equilateral triangles have permanent coincidence. **Four is the minimum number of vertices of a convex polygon admitting isolated coincidence.**
3. The minimum is robust at every unequal base ratio. For arbitrary \(0<a<b\), consider the isosceles trapezoid
   \[
   T(a,b,h)=\operatorname{conv}\{(-a,0),(a,0),(b,h),(-b,h)\},\qquad h>0.
   \]
   Set \(s=a+b\), \(d=b-a\), \(z=d/(2s)\in(0,1/2)\), and
   \[
   h_0=\sqrt{4s^2-d^2}=2s\sqrt{1-z^2}.
   \]
   For each such base ratio there exists \(\varepsilon>0\) such that **all** heights \(h\in(h_0-\varepsilon,h_0)\) yield exactly one positive coincidence radius \(t_*(h)\), a strict axial maximum of \(G(t)\). At \(h=h_0\) and throughout some interval just above it, no positive coincidence occurs. The birth is linear, with an exact, strictly positive coefficient:
   \[
   \boxed{\lim_{h\uparrow h_0}\frac{t_*(h)}{h_0-h}
   =\frac{z\sqrt{1-z^2}}{\pi z-3\arcsin z}.}
   \]

An explicit rational-coordinate witness is \(T(1,4,9)\), with vertices \((-1,0),(1,0),(4,9),(-4,9)\). Its unique positive coincidence occurs at \(t_*\approx10.828304094462\). Thus a rounded, asymmetric convex quadrilateral can have equal area and boundary centroids **at one radius only**, even though they disagree before and after.

## Assumptions and scope
All geometry is Euclidean. The boundary centroid uses uniform one-dimensional Hausdorff measure on the **entire** boundary, including the rounded arcs, not only original polygon edges. The Steiner point \(S\) is the curvature centroid: for a convex polygon with vertices \(v_i\) and positive exterior turning angles \(\theta_i\), \(S=(2\pi)^{-1}\sum_i\theta_i v_i\); for general convex bodies use its continuous extension. An isolated radius is strictly positive. A straight stationary point of the centroid path is not automatically a coincidence of other center definitions; here it is exactly the area-versus-arclength centroid equality. The local phase statement does not purport to classify every height of every trapezoid. The general centroid polynomial, the triangle rigidity, and the static (unrounded) planar-frustum height where area and boundary centroids coincide are prior knowledge; the four-vertex realization for **every** unequal base ratio, its positive-radius rounding bifurcation, and onset coefficient are the conclusions assessed here.

## Proof
**1. The inherited curvature-centroid formula and coincidence criterion.** Write \(A=|K|>0\), \(L=\operatorname{per}(K)>0\) and let \(G,H,S\) refer to \(K\) at \(t=0\). The planar Steiner first-moment formula is
\[
q(t)=|K_t|=A+Lt+\pi t^2,\qquad
G(t)=\frac{AG+LtH+\pi t^2S}{q(t)}.\tag{1}
\]
This formula is established in earlier curvature-centroid literature; it is restated, not newly claimed. For a polygon it follows by decomposing its outside parallel layer into edge strips of area \(t\ell_i\) and vertex sectors of area \(\theta_i t^2/2\); the outward-normal first moments cancel over the full circle. Approximation gives (1) for all convex bodies. Differentiating first moments (or (1)) gives
\[
H(t)=\frac{LH+2\pi tS}{L+2\pi t},\qquad
q(t)G'(t)=(L+2\pi t)\bigl(H(t)-G(t)\bigr).\tag{2}
\]
Thus coincidence and stationarity are equivalent for each positive \(t\).

Set \(X=H-G\) and \(Y=S-H\). Direct differentiation yields
\[
q(t)^2G'(t)=a(t)X+b(t)Y,\qquad
\begin{aligned}
a(t)&=A(L+2\pi t),\\
b(t)&=\pi t(2A+Lt).
\end{aligned}\tag{3}
\]
For \(t>0\), both coefficients are positive. Their ratio \(R(t)=b(t)/a(t)\) satisfies
\[
R(0)=0,\quad \lim_{t\to\infty}R(t)=\infty,\quad
R'(t)=\frac{2\pi Lq(t)}{A(L+2\pi t)^2}>0.\tag{4}
\]
Consequently, unless \(X=Y=0\), (3) can vanish at a positive radius only if \(X\) and \(Y\) are nonzero opposing vectors. This is equivalent to \(H\notin[G,S]\) on their common line. In that case exactly one radius exists by (4), with the scalar derivative changing sign across it. If both vectors vanish, (1) is constant and (2) gives coincidence for all radii. If either one vanishes alone or the vectors are not opposing, there is no stationary radius.

**2. Triangles cannot exhibit an isolated coincidence.** For a triangle with vertices \(v_i\), opposite sides \(a_i\), angles \(\alpha_i\) and perimeter \(L\), the barycentric coefficients of the three centers at the vertices are
\[
G:\ \frac13,\qquad H:\ \frac{L-a_i}{2L},\qquad
S:\ \frac{\pi-\alpha_i}{2\pi}.
\]
The determinant expressing collinearity of \(G,H,S\) is a nonzero constant times \(\det(1,a_i,\alpha_i)\). The sine rule gives \(a_i=2R\sin\alpha_i\). For three distinct angles, the strict concavity of \(\sin\) on \((0,\pi)\) makes this determinant nonzero; thus scalene triangles have no stationary radius by (3). For an isosceles triangle of apex angle \(\theta\), the three apex barycentric coordinates are
\[
\frac13,\qquad\frac{1}{2+2\sin(\theta/2)},\qquad
\frac{\pi-\theta}{2\pi}.
\]
The function \(f(\theta)=(\pi-\theta)\sin(\theta/2)-\theta\) is strictly concave on \((0,\pi)\) and vanishes at \(0\) and \(\pi/3\). It is positive for \(0<\theta<\pi/3\) and negative for \(\pi/3<\theta<\pi\). Therefore the perimeter coordinate lies **strictly between** the other two coordinates for every non-equilateral isosceles triangle. Criterion (3) rules out a positive stationary radius. For an equilateral triangle all centers coincide, giving permanent rather than isolated equality. These triangle properties are also covered by the earlier triangle-curvature-path classification cited below; their use here is a minimality premise, not a new triangle theorem.

**3. Every unequal trapezoid base ratio produces reversal.** For \(T(a,b,h)\) set \(d=b-a\), \(s=a+b\) and \(\ell=\sqrt{d^2+h^2}\). Elementary integration over horizontal chords, midpoint-weighting along sides, and exterior-angle weighting at vertices yield the following vertical coordinates (all horizontal coordinates vanish by reflection):
\[
\begin{aligned}
A&=hs,\quad L=2(s+\ell),\\
G_y&=\frac{h(a+2b)}{3s},\\
H_y&=\frac{h(2b+\ell)}{2(s+\ell)},\\
S_y&=h\left(\frac12+\frac1\pi\arctan\frac dh\right).
\end{aligned}\tag{5}
\]
In particular,
\[
H_y-G_y=\frac{h d(2s-\ell)}{6s(s+\ell)},\qquad
\frac{H_y-S_y}{h}=\frac{d}{2(s+\ell)}-\frac1\pi\arctan\frac dh.\tag{6}
\]
At \(h=h_0\), one has \(\ell=2s\), so \(H_y=G_y\) (this unrounded-center height is a known planar specialization of the tangential-frustum crossing theorem) while
\[
\frac{H_y-S_y}{h_0}=\frac z3-\frac{\arcsin z}{\pi}>0.\tag{7}
\]
The inequality holds because \(\arcsin z/z=\int_0^1(1-z^2u^2)^{-1/2}\,du\) is strictly increasing in \(z>0\), and at \(z=1/2\) its value is \(\pi/3\). The standing assumption \(a>0\) ensures \(z<1/2\). By continuity, for \(h<h_0\) sufficiently close to \(h_0\), equations (6)–(7) show \(H_y>G_y\) and \(H_y>S_y\), so criterion (3) supplies a unique positive stationary radius and a strict local maximum. For \(h>h_0\) sufficiently close, both \(H_y-G_y\) and \(S_y-H_y\) are negative, so no positive stationary radius exists. At \(h=h_0\), \(H_y-G_y=0\) and \(S_y-H_y<0\), again ruling it out.

**4. Sharp onset slope.** Put \(\delta=h_0-h\downarrow0\). From \(\ell(h)=\sqrt{d^2+h^2}\), differentiation of (6) gives
\[
H_y-G_y=\frac{d h_0^2}{36s^3}\,\delta+O(\delta^2),
\qquad H_y-S_y=h_0\left(\frac z3-\frac{\arcsin z}{\pi}\right)+O(\delta).
\]
If \(r=(H_y-G_y)/(H_y-S_y)\), the stationary equation is \(R(t_*)=r\) with \(R\) from (4). Since \(R(t)=2\pi t/L+O(t^2)\) as \(t\downarrow0\) and \(L\to6s\), substitution yields
\[
\frac{t_*}{\delta}\longrightarrow
\frac{z\sqrt{1-z^2}}{\pi z-3\arcsin z}>0,
\]
as claimed. This is a **one-sided local** bifurcation law; no global height-phase assertion is needed.

**5. An explicit four-vertex certificate.** At \((a,b,h)=(1,4,9)\), \(\ell=3\sqrt{10}<19/2\), \(A=45\), and \(L=10+6\sqrt{10}\). The centers in (5) satisfy
\[
G_y=\frac{27}{5},\quad
H_y=\frac{9(8+3\sqrt{10})}{2(5+3\sqrt{10})},\quad
S_y=\frac92+\frac9\pi\arctan\frac13.
\]
For an exact sign certificate, use \(223/71<\pi<22/7\) and the alternating-series bounds \(26/81<\arctan(1/3)<391/1215\). They imply
\[
\frac{27}{5}<\frac92+\frac{9(26/81)}{22/7}
<S_y<\frac92+\frac{9(391/1215)}{223/71}
<\frac{315}{58}<H_y.
\]
Hence \(G_y<S_y<H_y\) rigorously. Setting \(r=(H_y-G_y)/(H_y-S_y)>0\), its unique coincidence radius is the positive root of
\[
\boxed{\pi L t^2+2\pi A(1-r)t-rAL=0.}\tag{8}
\]
Numerically \(t_*\approx10.828304094462\). Because no triangle permits an isolated radius and this quadrilateral does, the vertex count four is sharp.

## Verification
Run `python3 verify.py` using only the Python standard library. The program checks exact rational enclosures for the strict witness signs, recomputes centroids from shoelace, edge-midpoint, and exterior-angle definitions, independently integrates area and boundary first moments of outer-parallel polygons by strip/sector decomposition, tests the critical-height onset for six base ratios, and verifies the small-onset slope and unique stationary root. It reports 256 deterministic checks passing. These finite tests independently guard normalization and signs; they do not replace the universal proofs above. The analytic statements apply to every indicated \(a,b,h\) and every planar convex body.

## Relationship to prior work
The vector-valued Steiner/curvature-centroid formula (1) is explicitly given in Gollapudi et al., arXiv:2106.04819v1, Section 5.1, and is **not** claimed to be new. An earlier publicly indexed published-finding corpus geometry result, *Hyperbolic curvature paths and quantitative triangle rigidity*, derives the planar hyperbola/straight-path dichotomy and the triangle classification used in Step 2; its theorem explicitly leaves more general collinear-center bodies unclassified. In particular, the universal one-stationary-point observation from (1) is an elementary implication of prior machinery. A later indexed published-finding corpus result, *A universal axial surface–volume centroid transition for tangential frusta*, already gives the static height \(h_0\) for equal unrounded centers in the planar trapezoid case (its formula \(h_2(a)=\sqrt{(a+3)(3a+1)}\) matches \(h_0/b\) after writing \(a\) there for the small-to-large base ratio); **that static height is not claimed new**. The assessed contribution is the sharp **four-vertex onset of an isolated positive-radius coincidence**, the open family of rounding reversals at **every** unequal trapezoid base ratio, and the exact one-sided onset slope for its positive stationary radius. Myroshnychenko, Ryabogin, Tatarko and Yaskin (2026) establish a sharp bound on the *distance* between area and boundary centroids at a single body, but no positive-radius coincidence/reversal law; the related Nazarov–Ryabogin–Yaskin planar bound (2023 preprint) likewise concerns separation maxima rather than offset-stationary radii. These are mathematical comparisons of statements, not novelty conclusions from search absence.

## Limitations
The local transition occurs for each fixed unequal base ratio in a neighborhood of the specified critical height; the theorem does not claim a complete global height diagram or cover non-Euclidean offset norms. All positive stationary radii are classified by the general center-order criterion, but the geometric classification of all convex bodies satisfying that criterion is not attempted. Numerical root digits are illustrative; existence, uniqueness, the strict example signs and the asymptotic coefficient have analytic proofs. General formulas and the triangle obstruction are pre-existing, and historical priority for the **four-vertex onset** remains subject to independent literature review. No independent mathematical audit or external proof certification has been performed.

## References
- S. Myroshnychenko, D. Ryabogin, K. Tatarko, V. Yaskin, *The sharp bound on the distance between the centers of mass of a convex body and its boundary*, arXiv:2611.11635v1, first publicly submitted 2026-11-08. https://arxiv.org/abs/2611.11635
- S. Gollapudi, G. Guruganesh, K. Kollias, P. Manurangsi, R. Paes Leme, J. Schneider, *Contextual Recommendations and Low-Regret Cutting-Plane Algorithms*, arXiv:2106.04819v1, first publicly submitted 2021-06-09, Section 5.1. https://arxiv.org/abs/2106.04819
- F. Nazarov, D. Ryabogin, V. Yaskin, *On the maximal distance between the centers of mass of a planar convex body and its boundary*, arXiv:2305.15646v1, first publicly submitted 2023-05-25. https://arxiv.org/abs/2305.15646
- *Hyperbolic curvature paths and quantitative triangle rigidity*, public research record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-hyperbolic-curvature-paths-and-quantitative-triangle-rigidity--7220229bf166
- *A universal axial surface–volume centroid transition for tangential frusta*, public research record, 2026-11-17 (postdating the motivating source). https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-universal-axial-surface-volume-centroid-transition-for-tangent--5920fe6f6170
