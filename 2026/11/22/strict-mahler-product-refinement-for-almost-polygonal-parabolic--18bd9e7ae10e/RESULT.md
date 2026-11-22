# Strict Mahler-product refinement for almost-polygonal parabolic bodies

## Finding
Let \(A=\{1=a_0>a_1>\cdots>a_m=0\}\) be an arbitrary finite decreasing mesh in \([0,1]\), with \(m\ge1\). Form the origin-symmetric planar polytope
\[
K_A=\operatorname{conv}\{(\sigma a,\tau(1-a^2)):a\in A,\ \sigma,\tau\in\{-1,1\}\},
\qquad
\mathcal M(A)=\operatorname{area}(K_A)\operatorname{area}(K_A^\circ).
\]
Here \(K_A^\circ=\{z:\langle z,x\rangle\le1\text{ for all }x\in K_A\}\); the origin is the Santaló point. The area of the primal polytope and the polar's first-quadrant vertices are exactly
\[
\boxed{\operatorname{area}(K_A)=\frac83-\frac23\sum_{i=0}^{m-1}(a_i-a_{i+1})^3,}
\qquad
\boxed{w(a,b)=\left(\frac{a+b}{1+ab},\frac1{1+ab}\right)}
\]
with the polar boundary vertices in order \((1,0),w(a_0,a_1),\ldots,w(a_{m-1},0),(0,1)\) in the first quadrant. Thus the polar area is an explicit finite rational function of the mesh.

**Exact local exchange and strict monotonicity.** If a new point \(c\) is inserted into any consecutive mesh interval \(a>c>b\), put
\[
q=2(a-b)(a-c)(c-b),\qquad D=(1+ab)(1+ac)(1+bc).
\]
Then, with \(A'=A\cup\{c\}\),
\[
\boxed{\operatorname{area}(K_{A'})-\operatorname{area}(K_A)=q,\qquad
\operatorname{area}(K_A^\circ)-\operatorname{area}(K_{A'}^\circ)=\frac qD,}
\]
\[
\boxed{\mathcal M(A')-\mathcal M(A)
=q\left(\operatorname{area}(K_A^\circ)-\frac{\operatorname{area}(K_{A'})}{D}\right)
\ge q\left(\pi-\frac83\right)>0.}
\]
In particular, adding *any* missing parabolic vertex (and its sign reflections) strictly increases the Mahler product; this property does not hold for arbitrary inclusions of centrally symmetric convex bodies.

**Sharp product interval.** For every such finite mesh,
\[
\boxed{8\le\mathcal M(A)<\frac{4(\pi+4)}3,}
\]
with equality at the lower endpoint precisely for the two-knot mesh \(A=\{0,1\}\). The lower value is the Mahler product of the square/rhombus \(\{|x|+|y|\le1\}\). The upper endpoint is not attained by any finite mesh. The same strict two-sided bounds
\[
\boxed{8<\mathcal M(A)<\frac{4(\pi+4)}3}
\]
hold for every infinite Schütt–Werner sequence \(1=a_0>a_1>\dots\downarrow0\), including those with nonincreasing positive gaps. Each endpoint is sharp within that infinite-sequence class: the geometric sequences \(a_n=r^n\), \(0<r<1\), approach the lower endpoint as \(r\downarrow0\) and the upper endpoint as \(r\uparrow1\).

## Assumptions and scope
All areas are ordinary two-dimensional Euclidean areas, not floating-body area deficits. The finite mesh is strictly decreasing with both endpoints \(0\) and \(1\). For an infinite sequence, include its limiting point \(0\) in \(A\) and take the closed convex hull; no convex-gap assumption is needed for the identities, although nonincreasing gaps place the example exactly within the standard almost-polygonal/fractal-string construction. The polar is taken at the origin. No statement is made about nonsymmetric polytopes, arbitrary supporting curves, or higher-dimensional analogues.

## Proof
**1. Primal area and cubic gap term.** On \([0,1]\), the upper boundary of \(K_A\) is the piecewise-linear interpolation of the concave graph \(f(x)=1-x^2\) through the chosen knots. For any adjacent \(a>b\), its chord \(L_{a,b}(x)\) satisfies
\[
f(x)-L_{a,b}(x)=(a-x)(x-b)\quad(b\le x\le a),\qquad
\int_b^a[f(x)-L_{a,b}(x)]\,dx=\frac{(a-b)^3}{6}.
\]
The region has fourfold reflection symmetry. Therefore its area equals \(4\int_0^1 f(x)\,dx=8/3\) minus four times the sum of these segment deficits, proving the first area formula. Splitting one gap of length \(a-b\) at \(c\) changes it by
\[
\frac23[(a-b)^3-(a-c)^3-(c-b)^3]=2(a-b)(a-c)(c-b)=q.
\]

**2. Exact polar boundary.** Because the generating vertices are unconditional (four independent sign choices), the first quadrant of the polar is described by
\[
\{(u,v):u,v\ge0,\ u\le1,\ v\le1,\ t u+(1-t^2)v\le1\ (t\in A)\}.
\]
The intersection of the two boundary lines indexed by adjacent knots \(a>b\) is
\[
w(a,b)=\bigl((a+b)/(1+ab),\ 1/(1+ab)\bigr).
\]
At this intersection the inequality indexed by an arbitrary \(t\in A\) has slack
\[
1-[t w_1+(1-t^2)w_2]
=\frac{(t-a)(t-b)}{1+ab}\ge0,
\]
since no knot lies strictly between consecutive \(a,b\). This also shows that each consecutive pair is active, and that the polar's first-quadrant boundary consists precisely of the displayed ordered vertices joining \((1,0)\) to \((0,1)\). Reflection gives the full polar, and the ordinary shoelace area is four times the area enclosed with the origin.

**3. Local polar area loss.** Insertion of \(c\) leaves all other polar vertices fixed and replaces the corner \(w(a,b)\) by the adjacent corners \(w(a,c),w(c,b)\). Elementary determinant expansion gives
\[
\left|\det\big(w(a,c)-w(a,b),w(c,b)-w(a,b)\big)\right|
=\frac{(a-b)(a-c)(c-b)}{(1+ab)(1+ac)(1+bc)}.
\]
The cut-off triangle has half this determinant as its area in each quadrant. Thus the whole polar loses exactly \(2(a-b)(a-c)(c-b)/D=q/D\). Multiplication of the two altered areas yields the exact product exchange in the finding.

**4. Strict sign.** Every generator satisfies
\[
a^2+(1-a^2)^2=1-a^2+a^4\le1\quad(0\le a\le1).
\]
It follows that \(K_A\subseteq B_2^2\), hence \(B_2^2\subseteq K_A^\circ\) and \(\operatorname{area}(K_A^\circ)\ge\pi\). Likewise \(K_{A'}\subseteq L:=\{(x,y):|y|\le1-x^2,\ |x|\le1\}\), so \(\operatorname{area}(K_{A'})\le8/3\). As \(D\ge1\), the product exchange is at least \(q(\pi-8/3)>0\). These are strict inequalities for every insertion because \(q>0\).

**5. Upper envelope, limits and infinite meshes.** The complete parabolic lens \(L\) has area \(8/3\). Its polar's first quadrant has maximal horizontal coordinate \(u=1\) when \(0\le v\le1/2\), and \(u=2\sqrt{v(1-v)}\) when \(1/2\le v\le1\). The first-quadrant polar area is
\[
\frac12+\int_{1/2}^1 2\sqrt{v(1-v)}\,dv=\frac12+\frac\pi8,
\]
so \(\operatorname{area}(L^\circ)=2+\pi/2\) and \(\mathcal M(L)=4(\pi+4)/3\). For any finite mesh, repeated vertex insertions increase the product monotonically. A sequence of finite refinements with maximal gap tending to zero converges in Hausdorff metric to \(L\); the origin remains uniformly interior, so areas of bodies and polars converge. Hence every finite product is at most \(\mathcal M(L)\), strictly below it by inserting a further missing knot first. For an infinite decreasing null sequence, finite prefixes together with \(0\) converge to its closed hull, giving the area formulas by limits and retaining strict inequalities: the lower follows by comparing to \(\{0,1,a_1\}\), and the upper by inserting one new knot within any of its positive gaps and then refining to \(L\). Finally \(\{0,1,r,r^2,\ldots\}\to\{0,1\}\) as \(r\downarrow0\), while its maximal gap \(1-r\to0\) as \(r\uparrow1\). Hausdorff continuity proves both sharp but unattained limits.

## Verification
The standalone standard-library program `verify.py` uses exact `fractions.Fraction` arithmetic. It computes the polar area independently by half-plane clipping, not merely from the vertex formula. It exercises all \(128\) subsets of seven rational interior knots and every missing-knot insertion, plus \(1000\) reproducible rational random meshes, verifying the primal and dual increments, exact Mahler exchange, and strict sign. The run reported `PASS: 7376 exact-rational assertions, independent polar clipping, and exhaustive grid refinements; analytic proof needed for infinite sequences.` The exact checks are finite evidence; the inequalities for all meshes and infinitely many knots follow from steps 1–5 above.

## Relationship to prior work
Schütt and Werner (1992) introduced the almost-polygonal body associated to decreasing convex sequences and analyzed its convex-floating-body deficit. Thäle and Winter (2026) identify those gaps with a fractal string and derive floating-body and random-polygon asymptotics; **the geometry of the bodies themselves is prior**, and neither cited source establishes the displayed Mahler-product refinement law. The simple cubic chord-deficit identity is also present in independent work on random parabolic arc hulls, but that identity alone does not imply the dual-area exchange or the sign of the product change.

The planar Mahler lower bound \(8\) is classical, so its value here is not independently new. A publicly available result on *symmetric circular lenses* already computed the parabolic lens's product \(4(\pi+4)/3\) as a limiting affine model; **that endpoint constant is prior**. The present contribution is its sharp role as a global upper envelope for *all* these parabolic vertex samples, together with a quantitative local polar/exterior exchange that forces strict increase under every knot insertion. A published theorem on regular-polygon rotational intersections also establishes a type of Mahler majorization, but applies to a different family with angular tangent facets. Meyer–Reisner's shadow-system convexity and planar vertex-removal arguments do not by themselves imply this special direction-by-direction strict exchange. Literature comparisons establish no equivalent theorem in the examined material; historical priority is not certified.

## Limitations
The theorem concerns the specific unconditional parabolic-arc sample geometry and origin polar. The parabola's quadratic form drives the cubic primal deficit and the rational polar intersection; neither identity is claimed for general curves. Strict monotonicity under arbitrary inclusion of convex bodies is false in general. No floating-body deficit asymptotic, Mahler conjecture, or multidimensional extension is proved. Priority checks include the full twenty pages of the 1992 primary source and other accessible mathematical records; an unindexed historical equivalent remains possible. Finite code checks do not replace the analytic proof.

## References
1. C. Thäle and S. Winter, *Floating Body Asymptotics via Fractal Strings*, arXiv:2611.16052v1, first posted 2026-11-11, https://arxiv.org/abs/2611.16052 .
2. C. Schütt and E. Werner, *The convex floating body of almost polygonal bodies*, Geometriae Dedicata 44 (1992), 169–188, DOI:10.1007/BF00182948.
3. M. Meyer and S. Reisner, *Shadow systems and volumes of polar convex bodies*, arXiv:math/0606305, https://arxiv.org/abs/math/0606305 .
4. Y. Lin and G. Leng, *Convex bodies with minimal volume product in \(\mathbb R^2\) — a new proof*, Discrete Mathematics 310 (2010), 3018–3025, https://archive.ymsc.tsinghua.edu.cn/pacm_download/248/8610-4.pdf .
5. *Sharp Mahler-product monotonicity of symmetric planar circular lenses*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-mahler-product-monotonicity-of-symmetric-planar-circular-l--b079d50aa217 .
6. *Endpoint-driven Gamma and interior Gaussian fluctuations for random parabolic hulls*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-endpoint-driven-gamma-and-interior-gaussian-fluctuations-for-ran--77a979074148 .
7. *Strict angular-gap majorization of Mahler products for rotational polygon intersections*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-strict-angular-gap-majorization-of-mahler-products-for-rotationa--073641383518 .
