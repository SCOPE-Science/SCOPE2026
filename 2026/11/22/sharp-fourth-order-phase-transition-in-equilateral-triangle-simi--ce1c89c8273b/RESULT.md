# Sharp fourth-order phase transition in equilateral-triangle similarity-containment volume

## Finding

Let the source triangle be the unit-side equilateral triangle
\[
T=\operatorname{conv}\{(0,0),(1,0),(1/2,\sqrt3/2)\},
\]
and let the target be the closed axis-aligned rectangle \(Q_{a,b}=[0,a]\times[0,b]\), for arbitrary positive reals \(a,b\). With \(J(x,y)=(-y,x)\), define the **four-dimensional orientation-preserving similarity-containment polytope**
\[
\mathcal C_{a,b}=\{(s,t,u,v)\in\mathbb R^4:(sI+tJ)T+(u,v)\subseteq Q_{a,b}\}.
\]
All volumes below are ordinary Lebesgue volumes in these four specified coordinates. Put \(m=\min(a,b)\), \(q=\max(a,b)/m\ge1\), and \(\rho=2/\sqrt3\). Then the **exact full-aspect-ratio volume law** is
\[
\boxed{\operatorname{vol}_4(\mathcal C_{a,b})=
 m^4\left\{\frac{8\sqrt3q-7}{12}
 +\frac34(\rho-q)_+^4\right\}},
\qquad x_+=\max\{x,0\}.
\]
The two analytic branches meet with three continuous derivatives, but not four: for the normalized function \(V(q)=\operatorname{vol}_4(\mathcal C_{q,1})\),
\[
V^{(4)}(\rho^-)=18,\qquad V^{(4)}(\rho^+)=0.
\]
For rectangles with fixed area \(ab=S>0\), the unique volume maximizer up to exchanging the sides is the square, with sharp value
\[
\boxed{\max_{ab=S}\operatorname{vol}_4(\mathcal C_{a,b})
 =\left(\frac{15}{2}-4\sqrt3\right)S^2.}
\]
In particular, the parameter-space volume of all orientation-preserving scaled and translated triangle placements is not determined just by the area of the scale-rotation feasibility footprint: its translational fibers create a fourth-order threshold correction.

## Assumptions and scope

The triangle is fixed and has side length one. The rectangle sides are positive and parallel to the coordinate axes. Similarities are represented by \((s,t,u,v)\), where \((s,t)\) is the real and imaginary part of the complex multiplier and \((u,v)\) is translation. The signed multiplier includes equivalent rotations differing by a half-turn; reflection-reversing maps are excluded. Zero scale is included but has measure zero. The formula is symmetric in exchanging \(a\) and \(b\) and is homogeneous of degree four in the target side lengths. No random-orientation or Haar-motion-invariant measure is used; the claim concerns the explicitly stated Euclidean Lebesgue measure on \(\mathbb R^4\).

## Proof

**Step 1: translation fibers.** Let \(z=(s,t)\), and let \(w_x(z)\), \(w_y(z)\) be the horizontal and vertical spans of \((sI+tJ)T\). A translation into \(Q_{a,b}\) exists if and only if \(w_x(z)\le a\) and \(w_y(z)\le b\). When it exists, its feasible \((u,v)\)-set is a rectangle of area \((a-w_x(z))(b-w_y(z))\). Fubini therefore gives
\[
\operatorname{vol}_4(\mathcal C_{a,b})
 =\int_{\mathbb R^2}(a-w_x(z))_+(b-w_y(z))_+\,ds\,dt,
\]
where the integrand is understood to vanish whenever either span exceeds its corresponding target side. The three edge differences of \(T\) give the explicit width formulas
\[
 w_x(s,t)=\max\left\{|s|,\frac{|s+\sqrt3t|}{2},\frac{|s-\sqrt3t|}{2}\right\},
\]
\[
 w_y(s,t)=\max\left\{|t|,\frac{|\sqrt3s+t|}{2},\frac{|\sqrt3s-t|}{2}\right\}.
\]

**Step 2: homogeneity and twelve symmetric sectors.** Swapping the two target axes interchanges \(a\) and \(b\). Rescaling all four transform coordinates with the target side lengths gives \(\operatorname{vol}_4(\mathcal C_{a,b})=m^4 V(q)\). Since the three unoriented edge directions of an equilateral triangle are separated by \(\pi/3\), both span functions, and hence the fiber-area integrand, are invariant under rotation of \(z\) by \(\pi/3\) and under complex conjugation. The twelve sectors bounded by consecutive rays of angular separation \(\pi/6\) therefore contribute equally. In the fundamental sector \(s\ge0\) and \(0\le t\le s/\sqrt3\), the span functions reduce exactly to
\[
w_x(s,t)=s,\qquad w_y(s,t)=(\sqrt3s+t)/2.
\]
For \(q\ge1\), the feasible section in that sector is cut out solely by \(s\le q\) and \(\sqrt3s+t\le2\). To see that no other inequalities are needed, note that \(s+\sqrt3t\le2s\le2q\) and \(t\le s/\sqrt3\le (\sqrt3s+t)/2\le1\) there. The upper boundary switches at \(s_0=\sqrt3/2\) between \(t=s/\sqrt3\) and \(t=2-\sqrt3s\). The maximum feasible \(s\) is \(\min(q,2/\sqrt3)\). Consequently
\[
\begin{aligned}
\frac{V(q)}{12}={}&
\int_0^{\sqrt3/2}\int_0^{s/\sqrt3}
 (q-s)\left(1-\frac{\sqrt3s+t}{2}\right)dt\,ds\\
&+\int_{\sqrt3/2}^{\min(q,\,2/\sqrt3)}
 \int_0^{2-\sqrt3s}(q-s)\left(1-\frac{\sqrt3s+t}{2}\right)dt\,ds.
\end{aligned}
\]
The lower limit \(\sqrt3/2<1\le q\) ensures these two integrals describe the entire sector for every admissible \(q\), including the threshold.

**Step 3: exact integration and differentiability.** Integrating first in \(t\) uses the elementary primitive
\[
(q-s)\left[\left(1-\frac{\sqrt3s}{2}\right)t-\frac{t^2}{4}\right].
\]
Substituting the two upper boundaries and evaluating the remaining polynomial integrals gives
\[
V(q)=\begin{cases}
\displaystyle\frac{3q^4-8\sqrt3q^3+24q^2-8\sqrt3q+3}{4},&1\le q\le 2/\sqrt3,\\[4pt]
\displaystyle\frac{8\sqrt3q-7}{12},&q\ge2/\sqrt3.
\end{cases}
\]
Subtracting the second polynomial from the first yields the exact identity
\[
\frac{3q^4-8\sqrt3q^3+24q^2-8\sqrt3q+3}{4}
 -\frac{8\sqrt3q-7}{12}=\frac34\left(q-\frac2{\sqrt3}\right)^4.
\]
Thus the asserted positive-part representation holds. The fourth derivative has a jump of exactly \(18\) at \(\rho=2/\sqrt3\), while all lower derivatives agree.

**Step 4: fixed-area global maximization.** Because \(ab=m^2q\), normalize by the square of target area to obtain \(V(q)/q^2\). Direct differentiation gives, for \(1<q<2/\sqrt3\),
\[
\frac d{dq}\frac{V(q)}{q^2}
 =\frac{(q^2-1)(3q^2-4\sqrt3q+3)}{2q^3}<0,
\]
since \(3q^2-4\sqrt3q+3=3(q-1/\sqrt3)(q-\sqrt3)<0\) on the indicated interval. For \(q\ge2/\sqrt3\),
\[
\frac d{dq}\frac{V(q)}{q^2}
 =-\frac{4\sqrt3q-7}{6q^3}<0.
\]
Continuity and these strict inequalities show that the unique maximum for \(q\ge1\) occurs at \(q=1\). Evaluating \(V(1)=15/2-4\sqrt3\) proves the sharp square statement. This also establishes uniqueness among all positive target aspect ratios, modulo swapping sides.

## Verification

The standalone `CHECK.py` evaluates the original translation fiber integral by a two-dimensional midpoint grid using the three transformed vertex coordinates (rather than the sector width simplification). It separately performs a piecewise Simpson quadrature of the sector integral. Both are compared against the exact formula at ten target ratios spanning the square, both sides of the threshold, the threshold itself, and elongated targets. Running `python3 CHECK.py` completed with `PASS`. A separate exact-symbolic polynomial calculation checked the piecewise integration, derivative continuity through order three and fourth-derivative jump. All real-parameter statements rely on the foregoing analytic integration and inequalities, not on finite experiments.

## Relationship to prior work

Choi and Choi, *The Containment Polytope of a Triangle and a Convex Polygon* (arXiv:2611.08556v1, first public 2026-11-05), define the same four similarity coordinates and determine the combinatorial organization of optimal placements for a general-position polygonal target. Their general-position assumptions explicitly exclude parallel-sided rectangles; their statements concern silhouettes and placement algorithms, not explicit four-dimensional volume profiles. A previously published *Complete orientation law for equilateral triangle containment in rectangles* determines the **two-dimensional** feasible multiplier polygon (dodecagonal versus hexagonal) and the random-orientation largest-fit scale, but does not determine the translation-fiber integral or the four-volume. The latter is not the multiplier footprint area. The published *A sharp equilateral extremum and a universal beta law for triangle self-containment polytopes* calculates four-volume when the **target is itself a triangle**; there, translation fibers are homothetic triangles, whereas here they are rectangles. A previously recorded formula for the four-volume of a **right-isosceles source triangle** inside a rectangle concerns a different source shape; an affine change of triangle does not preserve the isotropic similarity multiplier form and does not turn that formula into the present one. None of these compared statements directly supplies the explicit fourth-order volume threshold for unit-side equilateral sources. These are comparisons of claims, not claims of exhaustive historical priority.

## Limitations

The theorem is restricted to a single equilateral source shape, arbitrary positive rectangular targets, and ordinary four-coordinate Lebesgue volume; it does not extend to arbitrary triangle sources, arbitrary convex targets or the Euclidean-motion-invariant measure on similarities. The two-dimensional footprint transition and the corresponding scale distribution are already known and are not claimed as new. Likewise the general four-dimensional containment representation and the right-triangle rectangular case are established background. Independent historical-literature coverage is incomplete, and no independent mathematical audit has been performed.

## References

1. Y. Choi and S. Choi, *The Containment Polytope of a Triangle and a Convex Polygon*, arXiv:2611.08556v1 (2026-11-05), https://arxiv.org/html/2611.08556v1 .
2. *Complete orientation law for equilateral triangle containment in rectangles*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-complete-orientation-law-for-equilateral-triangle-containment-in--a89dd8dd2257 .
3. *A sharp equilateral extremum and a universal beta law for triangle self-containment polytopes*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-sharp-equilateral-extremum-and-a-universal-beta-law-for-triang--0f26f49ae237 .
4. P. K. Agarwal, N. Amenta and M. Sharir, *Largest placement of one convex polygon inside another*, Discrete Comput. Geom. 19 (1998), 95–104, as cited in Choi and Choi (2026).
