# A sharp two-apex invisibility law for asymmetric triangular bipyramids

## Finding
Fix an equilateral triangle \(B\subset\mathbb R^2\) of circumradius \(1\), centered at the origin. For any \(a,b>0\), form the convex bipyramid
\[
K_{a,b}=\operatorname{conv}\bigl((B\times\{0\})\cup\{(0,0,a),(0,0,-b)\}\bigr).
\]
Orthogonally project onto \(V^\perp\), where the unit vector \(V\in S^2\) is Haar-uniform. Let \(E_{a,b}\) be the event that the projected hull is **exactly the projected equatorial triangle**: neither axial apex is a vertex of the projected convex hull. Define
\[
\alpha=\frac1{2a},\qquad\beta=\frac1{2b},\qquad Q(a,b)=\Pr(E_{a,b}).
\]
Then, including the equality boundaries,
\[
Q(a,b)=\begin{cases}
1-\dfrac{3}{2\pi}\arccos\!\left(\dfrac{\beta^2-1/2}{1+\beta^2}\right), &\alpha\ge2\beta,\\[3pt]
1-\dfrac{3}{2\pi}\arccos\!\left(\dfrac{\alpha^2-1/2}{1+\alpha^2}\right), &\beta\ge2\alpha,\\[3pt]
1-\dfrac3\pi\arccos\!\left(\dfrac{1/2+\alpha\beta}{\sqrt{(1+\alpha^2)(1+\beta^2)}}\right),&\alpha<2\beta,\ \beta<2\alpha.
\end{cases}
\]
The formulas agree on the boundaries. The admissible viewing-direction region on a hemisphere is the spherical image of a Euclidean **triangle** if \(\max\{a/b,b/a\}\ge2\), and a genuine **hexagon** otherwise.

**Sharp balance.** For every fixed total apex separation \(s=a+b>0\), \(Q(a,s-a)\) has exactly one maximizer, \(a=b=s/2\). At that point,
\[
Q(h,h)=1-\frac3\pi\arccos\!\left(\frac{1+2h^2}{1+4h^2}\right).
\]
More precisely, as \(t\to0\) with \(|t|<h\),
\[
Q(h,h)-Q(h+t,h-t)=
\frac{3(3+4h^2)}{\pi h(1+4h^2)^2\sqrt{1+3h^2}}\,t^2+O_h(t^4).
\]
The quadratic coefficient is strictly positive for every \(h>0\).

## Assumptions and scope
All lengths and angles are Euclidean. The base has circumradius one; a common scaling changes none of the probabilities. A viewing direction \(V\) and its antipode define the same projection. A zero-measure set of directions produces degeneracy or boundary incidence, so the event's meaning does not depend on conventions for those directions. The event concerns simultaneous invisibility of the **two named axial apices**, not the total number of visible vertices for arbitrary asymmetric shapes.

## Proof
**Projection criterion.** Write the three outward unit side normals of \(B\) as \(n_0,n_1,n_2\), ordered at angles \(\pi/3,\pi,5\pi/3\). They satisfy \(n_i\cdot n_j=-1/2\) for distinct indices and \(n_0+n_1+n_2=0\). Thus
\[
B=\{z\in\mathbb R^2:n_i\cdot z\le1/2\ (i=0,1,2)\}.
\]
Outside the measure-zero set \(V_z=0\), replace \(V\) by its antipode if necessary so \(V_z>0\), and define \(u=(V_x/V_z,V_y/V_z)\). A spatial point projects inside the projected base triangle if and only if the line through it parallel to \(V\) meets \(B\times\{0\}\). The lines through the upper and lower apices meet that plane at \(-au\) and \(bu\), respectively. Consequently
\[
E_{a,b}\iff u\in C_{\alpha,\beta}:=\{u:-\alpha\le n_i\cdot u\le\beta\ \text{for all }i\}.
\]
The slope variable has density \((2\pi)^{-1}(1+\|u\|^2)^{-3/2}\). Therefore \(Q\) is the area of the spherical image \(\{(u,1)/\sqrt{1+\|u\|^2}:u\in C_{\alpha,\beta}\}\) divided by \(2\pi\).

**Active-face classification.** If \(\alpha\ge2\beta\), the upper inequalities \(n_i\cdot u\le\beta\), together with \(\sum_i n_i=0\), imply all lower inequalities; the feasible polygon is the triangle \(B/b\). If \(\beta\ge2\alpha\), the lower inequalities alone define the triangle \(-B/a\). In the strict remaining regime, all six support lines give genuine edges; their consecutive intersections combine one upper and one lower constraint with distinct indices, forming a threefold-symmetric hexagon. At equality, three edges contract to zero length.

**Exact spherical areas.** Form the positive homogeneous cone over \(C_{\alpha,\beta}\) in the upper half-space. For an upper constraint its outward facet normal is \((n_i,-\beta)\); for a lower constraint it is \((-n_i,-\alpha)\). The exterior spherical turning angle at the intersection of two such facets is the angle between their outward normals. If only the upper (respectively lower) constraints are active, the three equal turning angles have cosine \((\beta^2-1/2)/(1+\beta^2)\) (respectively \((\alpha^2-1/2)/(1+\alpha^2)\)). In the strict hexagonal regime, all six equal turning angles have cosine
\[
\frac{1/2+\alpha\beta}{\sqrt{(1+\alpha^2)(1+\beta^2)}}.
\]
For any geodesically convex spherical polygon in an open hemisphere, spherical Gauss–Bonnet gives its area as \(2\pi\) minus the sum of its exterior turning angles. Dividing the corresponding three-angle or six-angle formula by \(2\pi\) establishes all branches and their continuity at the transitions.

**Unique optimum.** Fix \(s=a+b\). By symmetry assume \(b\ge a\). In the triangular regime \(b\ge2a\), the feasible slope region is \(B/b\). As one decreases \(b\) at fixed \(s\) toward the boundary \(b=2a\), these triangles strictly expand, so \(Q\) strictly increases. In the hexagonal regime put \(p=ab\). The cosine of the common exterior spherical angle becomes
\[
c_s(p)=\frac{1+2p}{\sqrt{1+4s^2-8p+16p^2}},\qquad
c_s'(p)=\frac{6+8s^2-24p}{(1+4s^2-8p+16p^2)^{3/2}}>0,
\]
where the strict sign follows from \(0<p\le s^2/4\). The probability \(1-3\arccos(c_s(p))/\pi\) therefore increases strictly with \(p\), which is uniquely maximized at \(a=b=s/2\). This proves global uniqueness.

**Quadratic deficit.** Set \(a=h+t,b=h-t\). Then \(p=h^2-t^2\). Taylor expansion of the analytic hexagonal branch at \(p=h^2\), using
\[
c_{2h}(h^2)=\frac{1+2h^2}{1+4h^2},\quad
c_{2h}'(h^2)=\frac{6+8h^2}{(1+4h^2)^3},\quad
\sqrt{1-c_{2h}(h^2)^2}=\frac{2h\sqrt{1+3h^2}}{1+4h^2},
\]
yields the asserted strictly positive coefficient and remainder \(O_h(t^4)\).

## Verification
The standalone `verify.py` checks the event directly in independently constructed orthogonal projections, with 1,260,000 pseudorandom test directions across seven configurations, including both triangular phases and the hexagonal phase. Every discrepancy lies below 4.5 predicted binomial standard errors. In addition, independent midpoint quadrature of the slope-polygon spherical-area integral agrees with the closed formula to within \(2\times10^{-8}\) in five test configurations. Deterministic grid checks also confirm strict balancing on six fixed-separation slices. The program terminates with `ASYMMETRIC_BIPYRAMID_BOTH_APICES_HIDDEN_OK 1260000`. These finite checks are corroborative; the infinite assertions follow from the proof above, not simulations.

## Relationship to prior work
Glisse and Lazard's 2007 paper develops silhouettes under random orthogonal viewing and states the classical exterior-dihedral-angle formula for expected silhouette complexity. The 2013/2014 Glisse–Lazard–Michel–Pouget manuscript studies asymptotic silhouette complexity for random polytopes, not this fixed bipyramid's simultaneous-apex invisibility law. The special symmetric subfamily \(a=b\) is related by polarity to central sections of equilateral triangular prisms and is **not claimed as a new stand-alone result**. The content claimed here is the full two-parameter asymmetric event law, its height-ratio-two active-face phase diagram, the fixed-separation global optimizer, and its sharp quadratic deficit. These results are not implied by the symmetric restriction or by a generic expected-silhouette bound. Classical spherical polygon area and cone-angle facts are used, not claimed as original.

## Limitations
This is not a full polygon-vertex-count law for asymmetric bipyramids; asymmetric configurations can also have triangular shadows containing one axial apex. It does not treat non-equilateral bases, skew apices, or nonuniform viewing distributions. The general literature and record searches do not establish exhaustive historical priority; a specialized unpublished derivation could exist. Independent mathematical and historical validation has not been performed.

## References
1. M. Glisse and S. Lazard, *An Upper Bound on the Average Size of Silhouettes*, first publicly posted 2007-02-14, arXiv:cs/0702087, https://arxiv.org/abs/cs/0702087.
2. M. Glisse, S. Lazard, J. Michel and M. Pouget, *Silhouette of a random polytope*, INRIA RR-8327 (2013, preprint revised 2014), HAL hal-00841374, https://hal.science/hal-00841374.
3. F. Affentranger and R. Schneider, *Random projections of regular simplices*, Discrete & Computational Geometry 7 (1992), 219–226, DOI 10.1007/BF02187839 (general Grassmannian projection background; no claimed fixed-bipyramid theorem).
