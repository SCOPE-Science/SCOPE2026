# Exact Euclidean area of every Hilbert ball in a square: corner-cut law and sharp center stability

## Finding
Let \(Q=(-1,1)^2\), equip it with the **unhalved** Hilbert cross-ratio distance, and write \(\mathcal A(c,r)\) for the ordinary Euclidean area of the closed Hilbert radius-\(r\) ball centered at \(c=(u,v)\in Q\). For every \(r>0\), put \(t=\tanh(r/2)\in(0,1)\). For \(\varepsilon,\eta\in\{-1,1\}\), set \(a=\varepsilon u\), \(b=\eta v\), and
\[
T_{\varepsilon,\eta}=
\frac{t^2(1-t^2)}{2}\,
\frac{(a-b)^2\bigl(1-ab-|a-b|\bigr)}{(1+ta)^2(1+tb)^2}.
\]
Then the **complete all-center, all-radius area law** is
\[
\boxed{\mathcal A((u,v),r)=
\frac{4t^2(1-u^2)(1-v^2)}{(1-t^2u^2)(1-t^2v^2)}
-\sum_{\varepsilon,\eta\in\{-1,1\}}T_{\varepsilon,\eta}.}
\tag{1}
\]
All four terms subtracted are nonnegative and arise from disjoint corner triangles. The ball has four Euclidean vertices for \((u,v)=(0,0)\); six for \(u=v\ne0\) or \(u=-v\ne0\); and eight otherwise. Consequently the center is the unique maximizer of Euclidean ball area:
\[
\mathcal A(c,r)\le 4\tanh^2(r/2),\quad
\text{with equality precisely at }c=(0,0).
\tag{2}
\]
The exact local positional stability is
\[
\boxed{\mathcal A((u,v),r)=4t^2-6t^2(1-t^2)(u^2+v^2)+O_r\!\left((u^2+v^2)^{3/2}\right).}
\tag{3}
\]
In particular the area Hessian at the center is \(-12t^2(1-t^2)I_2\). For sampling by normalized Euclidean area, divide (1)–(3) by \(4\). Every affine image of the square (every nondegenerate parallelogram) satisfies the corresponding formula in affine-normalized center coordinates, because Hilbert distance is projectively invariant and affine maps multiply all Euclidean areas by the same determinant.

## Assumptions and scope
The domain is the *open* square, with ordinary Euclidean area as an external sampling measure, not intrinsic Busemann/Holmes–Thompson Hilbert area. The Hilbert distance is the full logarithm of the boundary cross-ratio (no factor \(1/2\)); this choice is essential for \(t=\tanh(r/2)\). The center is interior and the radius is finite and strictly positive. Open versus closed Hilbert balls has no effect on their Euclidean area, and statements about vertex counts refer to the closed ball. All formulae hold at zero center coordinates and at equal-coordinate centers without generic-position assumptions.

## Proof
**1. Facet-ratio form of the Hilbert distance.** Write \(f_{1,\pm}(y)=1\pm y_1\) and \(f_{2,\pm}(y)=1\pm y_2\). The two intersections of the line through \(c,y\) with the boundary of the square give the standard polytope Hilbert expression
\[
d_Q(c,y)=\log\frac{\max_{i,\sigma}f_{i,\sigma}(y)/f_{i,\sigma}(c)}{\min_{j,\tau}f_{j,\tau}(y)/f_{j,\tau}(c)}.
\tag{4}
\]
One may verify (4) directly: for the line parameter \(c+s(y-c)\), every positive facet function is affine in \(s\), and the first forward and backward zeros control the two factors of the cross-ratio. Hence membership in the radius-\(r\) ball is equivalent to the twelve cross-facet inequalities
\[
\frac{f_{i,\sigma}(y)}{f_{i,\sigma}(c)}\le e^r\frac{f_{j,\tau}(y)}{f_{j,\tau}(c)}\quad\text{for all }(i,\sigma),(j,\tau).
\tag{5}
\]
The four inequalities internal to each coordinate say exactly \(y_1\in J(u)\), \(y_2\in J(v)\), where
\[
J(w)=\left[\frac{w-t}{1-tw},\frac{w+t}{1+tw}\right],\qquad
|J(w)|=\frac{2t(1-w^2)}{1-t^2w^2}.
\tag{6}
\]
Thus the ball is obtained from the rectangle \(P=J(u)\times J(v)\) by cross-coordinate inequalities.

**2. A single triangle at each corner.** At the corner \(p_{\varepsilon,\eta}=(J(u)^{\varepsilon},J(v)^{\eta})\), where superscripts denote left/right endpoints, the respective high and low facet ratios in coordinate \(1\) are
\[
H_1=\frac{1+t}{1+t\varepsilon u},\qquad L_1=\frac{1-t}{1+t\varepsilon u}=e^{-r}H_1,
\]
and similarly \(H_2=(1+t)/(1+t\eta v)\), \(L_2=e^{-r}H_2\). Every coordinate-internal inequality is saturated. If \(a<b\), then \(H_1>H_2\), and the only violated cross inequality is \(H_1\le e^r L_2\); if \(a>b\), the reversed one is violated; if \(a=b\), none is. Each inequality cuts off a right triangle from the rectangle: when \(a<b\), moving inward along the two adjacent rectangle edges gives intercept lengths
\[
\xi=(H_1-H_2)(1+a),\qquad
\zeta=e^{-r}(H_1-H_2)(1-b).
\]
For \(a>b\) exchange the two coordinates. Using
\[
|H_1-H_2|=\frac{t(1+t)|a-b|}{(1+ta)(1+tb)},\qquad e^{-r}=\frac{1-t}{1+t},
\]
the triangle's area \(\xi\zeta/2\) is exactly \(T_{\varepsilon,\eta}\), since the required product of endpoint factors is \((1+\min(a,b))(1-\max(a,b))=1-ab-|a-b|\).

There is no double subtraction. Indeed, throughout \(P\), the larger-to-smaller ratio within *each* coordinate is at most \(e^r\); hence the two possible opposite-direction cross violations cannot coexist, since their product would require the product of those two within-coordinate ratios to exceed \(e^{2r}\). Moreover, each cross violation stays in the open rectangle quadrant beyond \((u,v)\) corresponding to its corner: on the lines \(y_1=u\) or \(y_2=v\) all cross inequalities hold strictly because each coordinate's high facet ratio is strictly below \(e^r\) and its low facet ratio strictly above \(e^{-r}\) for an interior center. The violation half-plane at a corner therefore intersects \(P\) in exactly the indicated triangle, and the four regions lie in disjoint coordinate quadrants. Taking the area of \(P\) minus the four triangles proves (1).

The factor \(1-ab-|a-b|\) is strictly positive for \(|a|,|b|<1\), so a corner is cut off exactly when \(a\ne b\). Counting the remaining vertices (one new vertex on each adjacent edge for a cut corner) proves the stated four/six/eight trichotomy.

**3. Sharp global center and second variation.** Since \(0<t<1\), (6) implies \(|J(w)|\le2t\), with equality only for \(w=0\). Since the ball is contained in \(P\), its area is at most \(4t^2\), strictly below it away from \((0,0)\). At \(c=0\), all four corner cuts vanish, and \(P=[-t,t]^2\), proving (2).

To expand (1), use \((1-w^2)/(1-t^2w^2)=1-(1-t^2)w^2+O(w^4)\). For each \(\varepsilon,\eta\), the corner term is \(\tfrac12t^2(1-t^2)(\varepsilon u-\eta v)^2+O_r(\|(u,v)\|^3)\), uniformly across quadrants, since the absolute-value factor first enters at cubic order. The sum of the four squares equals \(4(u^2+v^2)\). Subtracting yields (3). The local expression is twice differentiable at the origin (the possible nonsmooth factors are of cubic order), establishing the exact Hessian.

## Verification
The standalone file `check_area.py` independently constructs each Hilbert ball by clipping the original square with the twelve linear inequalities (5), and evaluates the resulting polygon by the shoelace formula. It compares this geometry-only calculation against (1) for 350 reproducibly seeded centers over five radii; all agree to the indicated floating-point tolerance. It also checks the sharp center area, the local quadratic coefficient along a coordinate axis, and the 4/6/8 vertex classes. Run with `python check_area.py` using Python 3.9 or later; no third-party dependencies are required. These numerical checks are diagnostic; the algebraic proof above establishes the universal assertions.

## Relationship to prior work
Papadopoulos and Troyanov, *From Funk to Hilbert Geometry* (arXiv:1406.6983v1, first public 2014-06-26), derives the standard polytope facet-ratio description of Hilbert geometry and discusses ball structures in Funk/Hilbert metrics. Nielsen and Shao, *On Balls in a Hilbert Polygonal Geometry* (SoCG 2017, DOI 10.4230/LIPIcs.SoCG.2017.67), gives a general polygonal Hilbert-ball construction and its combinatorial behavior. Their constructive shape theorem accounts for polyhedral balls, and the square's possible vertex counts should be regarded as a direct specialization of that known structure, not independent mathematical novelty. The contribution asserted here is the compact all-center **Euclidean area functional**, together with the strict global center optimum and its exact nondegenerate second variation. These statements are not present as theorems in the inspected sources; nevertheless the known construction supplies an algorithmic route to compute special cases, so claims of absolute historical priority or conceptual independence from that construction are not made.

## Limitations
The result is for squares/parallelograms and ordinary normalized Euclidean area. It does not assert analogous global optimality for arbitrary convex polygons or intrinsic Hilbert volume forms. The given all-center closed form is a simplification of finite polygonal geometry; a generic algorithm to construct Hilbert polygonal balls is already known. No independent mathematical or historical certification is claimed. All bounds concern finite positive radii and interior centers.

## References
1. A. Papadopoulos and M. Troyanov, *From Funk to Hilbert Geometry*, arXiv:1406.6983v1 (public 2014-06-26), https://arxiv.org/html/1406.6983v1.
2. F. Nielsen and L. Shao, *On Balls in a Hilbert Polygonal Geometry*, Proceedings of SoCG 2017, Article 67, DOI 10.4230/LIPIcs.SoCG.2017.67, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2017.67.
