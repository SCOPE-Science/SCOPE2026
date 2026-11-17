# A symmetry-breaking interface optimum in a two-coset Voronoi tiling

## Finding
Let
\[
S_t=2\mathbb Z^2\;\cup\;\bigl((1+t,1)+2\mathbb Z^2\bigr),\qquad 0\le t\le1.
\]
Every Voronoi cell of this periodic planar point set has area exactly \(2\), and all cells are mutually congruent (by a half-turn exchanging the two cosets). Write \(P(t)\) for their common perimeter, \(R(t)\) for the covering radius of \(S_t\), and \(Q(t)\) for the area-average squared distance to the generating site, calculated in its Voronoi cell.

For \(0<t<1\), the cell of the origin is the six-vertex polygon, in counterclockwise order,
\[
(-1,-t^2/2),\quad(t,-1+t^2/2),\quad(1,-t^2/2),\quad
(1,t^2/2),\quad(t,1-t^2/2),\quad(-1,t^2/2).
\]
At the two endpoints the polygon reduces to a quadrilateral. Its three exact profiles are
\[
\begin{aligned}
P(t)&=2t^2+2(1+t)\sqrt{1+(1-t)^2}+2(1-t)\sqrt{1+(1+t)^2},\\
R(t)^2&=1+\frac{t^4}{4},\\
Q(t)&=\frac{4+2t^2-t^4}{12}.
\end{aligned}
\]
The last two profiles strictly increase for \(0<t<1\). By contrast, \(P(t)\) strictly decreases up to a **unique** parameter \(t_*\in(0,1)\) and strictly increases afterwards. More precisely, put
\[
\begin{split}
w(u)&=\sqrt{u^2+4},\\
q(u)&=\sqrt{2(u+2+w(u))},\\
\Phi(u)&=u+q(u)-\frac{4u}{q(u)},\qquad 0\le u\le1.
\end{split}
\]
Then \(P(t)=2\Phi(t^2)\), \(\Phi\) is strictly convex throughout \([0,1]\), and \(t_*\) is characterized by the unique root \(\Phi'(t_*^2)=0\). Numerically,
\[
t_*=0.35320480862795778248\ldots,\qquad
P(t_*)=5.64928854396555055919\ldots<4\sqrt2=P(0).
\]
Thus a genuinely non-Bravais, two-coset Voronoi arrangement **improves the intercell boundary length** over the square-lattice endpoint while simultaneously making both the covering radius and squared-distance quantization error worse. The interface improvement is about \(0.133744\%\); its significance is the exact, unique symmetry-breaking tradeoff, not a large numerical gain. There is no claim of global optimality among arbitrary equal-area tilings or all planar point sets.

## Assumptions and scope
The ambient metric is the ordinary Euclidean metric on \(\mathbb R^2\). The two cosets are disjoint for the entire closed interval; the point density is \(1/2\), hence mean cell area \(2\). The Voronoi cell of \(s\in S_t\) is \(\{x:|x-s|\le|x-v|\text{ for all }v\in S_t\}\), with equality allowed at boundaries. The covering radius is \(\sup_x\min_{s\in S_t}|x-s|\). The squared-distance error is \(Q(t)=\frac12\int_{V_t}|x|^2\,dx\), where \(V_t\) denotes the cell of the origin. Perimeter counts the boundary of one full cell; the physical interface length per unit area is \(P(t)/4\), since interfaces are shared. No randomness, independent process, or diffusion dynamics is asserted.

## Proof
**(1) Exact cell and universal neighbor reduction.** Comparison with the four other same-coset points \((\pm2,0)\) and \((0,\pm2)\) restricts the cell to \([-1,1]^2\). For any \((x,y)\) in this square, the nearest coordinate of the opposite coset among \(1+t+2\mathbb Z\) is either \(t-1\) or \(t+1\), while the nearest element of \(1+2\mathbb Z\) is either \(-1\) or \(1\). Because Euclidean squared distance is coordinate-separable, no opposite-coset site other than the four points \((t\pm1,\pm1)\) can cut the cell. Likewise, no further same-coset site can cut it: in \([-1,1]^2\), the origin is coordinatewise nearest within \(2\mathbb Z^2\). Intersecting these eight bisector half-planes gives precisely the six displayed vertices (with coincident vertices at endpoints). The cross-product shoelace sum gives \(\operatorname{area}(V_t)=2\). A half-turn about \((1+t,1)/2\) exchanges the two cosets and therefore their cell shapes; translations by \(2\mathbb Z^2\) give the remaining congruences.

**(2) Three exact profiles.** The two vertical cell edges each have length \(t^2\). The other four edges form two equal pairs of lengths
\[
(1+t)\sqrt{1+(1-t)^2}\quad\text{and}\quad
(1-t)\sqrt{1+(1+t)^2},
\]
which yields \(P(t)\). Every polygon vertex has squared distance \(1+t^4/4\) to the generator, and the convexity of squared distance places its maximum at a vertex; this proves the covering-radius formula. Applying the exact polygonal second-moment identity
\[
\int_V (x^2+y^2)\,dx\,dy
=\frac1{12}\sum_j (x_jy_{j+1}-x_{j+1}y_j)
\bigl(x_j^2+x_jx_{j+1}+x_{j+1}^2+y_j^2+y_jy_{j+1}+y_{j+1}^2\bigr)
\]
with the cyclic vertices above gives \(\int_{V_t}|x|^2dx=(4+2t^2-t^4)/6\). Division by the cell area \(2\) gives \(Q(t)\). Both \(1+t^4/4\) and \((4+2t^2-t^4)/12\) strictly increase for \(0<t<1\).

**(3) Strict convexity and unique perimeter optimum.** Let \(u=t^2\), \(a=\sqrt{u-2t+2}\), and \(b=\sqrt{u+2t+2}\). Then
\[
(a+b)^2=2(u+2+\sqrt{u^2+4}),\qquad b-a=\frac{4t}{a+b}.
\]
Substitution into the perimeter expression gives \(P(t)/2=\Phi(u)\). For \(w=\sqrt{u^2+4}\) and \(q=\sqrt{2(u+2+w)}\), direct differentiation gives
\[
q'=\frac{1+u/w}{q},\quad
q''=\frac4{w^3q}-\frac{(1+u/w)^2}{q^3},\quad
\Phi''=\left(1+\frac{4u}{q^2}\right)q''+
\frac{8q'}{q^2}\left(1-\frac{u q'}q\right).
\]
For all \(0\le u\le1\), \(q^2\ge8\), \(2\le w\le\sqrt5\), and \(1+u/w\le3/2\). Consequently
\[
\frac{4q^2}{w^3}\ge\frac{32}{5\sqrt5}>\frac94\ge(1+u/w)^2,
\qquad 0\le\frac{u q'}q\le\frac{3}{16}<1.
\]
Therefore \(q''>0\) and \(\Phi''>0\) on the entire interval. The endpoint derivatives are
\[
\Phi'(0)=1-\frac{3\sqrt2}{4}<0,
\qquad \Phi'(1)=\frac{3-\sqrt5}{2}>0.
\]
Thus exactly one root \(u_*\in(0,1)\) exists, and strict convexity gives the asserted strict decrease/increase in \(P(t)\). Root evaluation gives \(u_*=0.12475363683791228038\ldots\), and the numerical perimeter above; these decimals are not used to establish existence or uniqueness.

**(4) Non-Bravais character.** If \(0<t<1\), the additive combination of two copies of the nonzero coset representative \((1+t,1)\) belongs to neither coset modulo \(2\mathbb Z^2\). Therefore \(S_t\), which contains the origin, is not a lattice. This proves that the optimum is an actual two-site-basis, rather than a reparametrized one-site Bravais lattice.

## Verification
Run `python STAGGERED_VORONOI_CHECKS.py` with Python 3 and SymPy. The checker reconstructs polygon area and radial second moment exactly by rational polynomial identities, checks all vertex radii algebraically, verifies nearest-site inequalities for several rational offsets against a finite explicit window of additional sites, verifies the equivalent radical perimeter expression, and independently locates the unique stationary point numerically. The proof's coordinate-neighbor reduction and positive derivative bounds are universal and do not depend on finite enumeration, numerical root finding, or code. Expected marker: `STAGGERED_VORONOI_TRADEOFF_CHECKS_OK`.

## Relationship to prior work
Hales's 1999 honeycomb theorem establishes the *global* area-normalized perimeter lower bound, attained by a regular hexagonal honeycomb; it does not determine the unique optimizer in the present restricted, non-Bravais, two-coset Voronoi family, nor the contrasting covering/quantization profiles. Choe's 1989 study of minimal fundamental domains of flat tori shows that a square fundamental domain need not minimize boundary length, and constructs a skew hexagonal fundamental domain; this concerns domains for a fixed lattice action, not a Voronoi tessellation from this moving two-coset point set or its exact three-way tradeoff. Yates and Baker (2013) analyze why Voronoi partitions matter on nonuniform grids for a reaction–diffusion model but do not optimize this two-coset perimeter. Du, Faber and Gunzburger (1999) review centroidal Voronoi tessellations and squared-distance error, not this interface-minimizing staggered family. The claimed new contribution is precisely the complete strict perimeter profile in the natural one-shift two-site family together with its incompatible monotone nearest-site quality profiles; no worldwide honeycomb or quantization theorem is claimed.

## Limitations
The uniqueness is only within the explicitly defined one-parameter family \(S_t\) with \(0\le t\le1\). The near-optimum perimeter reduction is small, approximately \(0.133744\%\) relative to the square-lattice endpoint; it is not a universal efficiency claim. The squared-distance error is an exact cell average, not a dynamic diffusion error or an optimal-transport estimate. No statement about anisotropic norms, non-Euclidean geometry, noisy perturbations, or globally optimal site arrangements is made. The literature comparison is best knowledge rather than a certification of historical priority, and independent review has not been performed.

## References
- T. C. Hales, *The Honeycomb Conjecture*, arXiv:math/9906042, first submitted 8 June 1999; *Discrete & Computational Geometry* **25** (2001), 1–22. https://arxiv.org/abs/math/9906042
- J. Choe, *On the Existence and Regularity of Fundamental Domains with Least Boundary Area*, *Journal of Differential Geometry* **29** (1989), 623–663. https://newton.kias.re.kr/~choe/fundamental.pdf
- C. A. Yates and R. E. Baker, *Importance of the Voronoi domain partition for position-jump reaction-diffusion processes on nonuniform rectilinear lattices*, *Physical Review E* **88** (2013), 054701; published 22 November 2013. https://doi.org/10.1103/PhysRevE.88.054701
- Q. Du, V. Faber and M. Gunzburger, *Centroidal Voronoi Tessellations: Applications and Algorithms*, *SIAM Review* **41** (1999), 637–676. https://doi.org/10.1137/S0036144599352836
