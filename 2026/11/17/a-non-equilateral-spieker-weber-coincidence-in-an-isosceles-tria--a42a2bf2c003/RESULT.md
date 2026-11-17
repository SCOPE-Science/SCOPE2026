# A non-equilateral Spieker–Weber coincidence in an isosceles triangle

## Finding

For every \(h>0\), let \(T_h\) be the Euclidean triangle with vertices \((-1,0),(1,0),(0,h)\). Give its boundary uniform arclength measure. Its Spieker center \(S_h\) is the arclength centroid, while its perimeter Weber center \(W_h\) is the unique global minimizer of the total Euclidean distance to its boundary.

There is **exactly one** \(h_*\in(7/10,4/5)\) for which \(S_{h_*}=W_{h_*}\), with \(h_*\approx0.746554270914034533\). This triangle is non-equilateral. For \(7/10\le h<h_*\), the Weber center lies strictly *above* the Spieker center on the symmetry axis (closer to the apex); for \(h_*<h\le4/5\), it lies strictly *below*. At \(h=\sqrt3\) the two centers also coincide, by equilateral symmetry. No classification outside the displayed interval is asserted.

The dimensionless height \(h_*\) is specified exactly as the unique zero in \((7/10,4/5)\) of the explicit elementary function \(G\) defined below. The uniqueness and the sign reversal are certified by outward-rounded interval bounds, in addition to an analytical derivation of \(G\).

## Assumptions and scope

Write \(s=\sqrt{1+h^2}\), \(y=hs/(2(1+s))\), and \(S_h=(0,y)\). The perimeter-distance functional is
\[
J_h(z)=\int_{\partial T_h}\|z-p\|_2\,d\ell(p).
\]
There are no discrete point masses at the vertices, and the distance in this integral is **ambient Euclidean distance**, not a boundary shortest-path distance or squared distance. Normalizing \(J_h\) by perimeter does not change its minimizer. The result concerns nondegenerate isosceles triangles \(h>0\), normalized to base length \(2\).

Let \(\operatorname{arsinh}\) denote the real inverse hyperbolic sine. Define
\[
\begin{aligned}
G(h)={}&2y\operatorname{arsinh}(1/y)\\
&+2\left[\frac h s\bigl(\sqrt{1+y^2}-h+y\bigr)
-\frac{h-y}{s^2}\left(\operatorname{arsinh}(h)+
\operatorname{arsinh}\frac{1+hy}{h-y}\right)\right],
\end{aligned}
\]
with \(s,y\) as defined above. This is a smooth real function on \((0,\infty)\).

## Proof

**1. Existence and uniqueness of the Weber center.** The functional \(J_h\) is continuous, coercive and strictly convex on \(\mathbb R^2\). Indeed, for two distinct sites, the Euclidean norm convexity inequality is strict at all boundary points except those on the common line of the two sites; since the nondegenerate triangle boundary is not concentrated on a line, integration yields strict convexity. Reflection in the vertical axis preserves \(J_h\), so its unique minimizer is \((0,w(h))\). The vertical derivative is strictly increasing. It is negative at height \(0\) and positive at height \(h\), since the base and sloping sides contribute, respectively, nonpositive/nonnegative derivatives with strict sign from the other sides. Hence \(0<w(h)<h\).

**2. Arclength centroid.** The base has length \(2\) and midpoint height zero. The sloping sides each have length \(s\) and midpoint height \(h/2\). Their length-weighted centroid therefore has height \(y=hs/(2(1+s))\), with \(0<y<h\).

**3. Exact derivative.** At a point \((0,y)\), the contribution of the base to \(\partial J_h/\partial y\) is
\[
\int_{-1}^1 \frac{y}{\sqrt{x^2+y^2}}\,dx=2y\operatorname{arsinh}(1/y).
\]
For the left sloping side, use the unit tangent \(e=(1,h)/s\) and unit normal \(n=(-h,1)/s\), based at \((-1,0)\). The tangential and signed normal coordinates of \((0,y)\) are \(\zeta=(1+hy)/s\) and \(\rho=(y-h)/s\). Direct differentiation of the line-segment distance integral gives
\[
\begin{aligned}
&\int_0^s \frac{y-ht/s}{\sqrt{(t-\zeta)^2+\rho^2}}\,dt\\
&=\frac h s\bigl(\sqrt{1+y^2}-(h-y)\bigr)
-\frac{h-y}{s^2}\left[\operatorname{arsinh}(h)+
\operatorname{arsinh}\frac{1+hy}{h-y}\right].
\end{aligned}
\]
The right sloping side gives the same contribution. Consequently \(\partial J_h(0,y)/\partial y=G(h)\). By strict convexity and reflection symmetry, \(S_h=W_h\) holds **if and only if** \(G(h)=0\); and \(G(h)<0\) means \(w(h)>y\), whereas \(G(h)>0\) means \(w(h)<y\).

**4. Certified simple crossing.** The accompanying executable `check_spieker.py` constructs the exact symbolic derivative \(G'(h)\) and evaluates it by outward-rounded interval arithmetic on the one hundred closed intervals
\[
\left[\frac{700+k}{1000},\frac{701+k}{1000}\right],\qquad k=0,1,\ldots,99.
\]
Each enclosure has lower endpoint greater than \(9/100\). The same verified interval procedure gives
\[
-0.006646<G(7/10)<-0.006645,\qquad
0.006715<G(4/5)<0.006716.
\]
These bounds are strict interval certificates, not a plot or finite sampling argument. The intermediate value theorem and strict increase yield the unique zero \(h_*\) inside \((7/10,4/5)\), its simplicity, and the asserted sign reversal. As \(h_*<4/5<\sqrt3\), its triangle is not equilateral. The decimal approximation is not used to establish existence or uniqueness.

## Verification

Run `python check_spieker.py` with the versions in `requirements.txt`. The checker differentiates the symbolic formula, encloses its values over the *entire* stated height interval with directed interval rounding, checks the strict endpoint signs, and separately compares the closed-form derivative with high-precision quadrature of the original three edge integrals at four heights. Its success marker is `SPIEKER_WEBER_COINCIDENCE_OK`. The proof of the overall centering statement is analytic; the finite computer-assisted certification is confined to the stated interval bounds and is fully reproducible from the included code.

## Relationship to prior work

The Spieker center as arclength centroid is classical. Zhang and Carlsson (2014, arXiv:1403.3715v1) develop general line-integral formulas and a continuous Weiszfeld method for the Euclidean perimeter Weber problem on convex polygons. Their general formulas supply the context, but their inspected treatment does not determine the Spieker–Weber coincidence shapes or prove the nonregular local reversal. The result here is specifically that an exact, simple nonregular coincidence exists and that the ordering changes across it; it does not claim the general distance-integral formula, uniqueness of Weber medians, or the definition of the Spieker point as new.

The earlier work of Fekete, Mitchell, and Beurer (2005) treats the continuous median mainly in the \(\ell_1\) norm, and Carmi, Har-Peled, and Katz (2005) study area-uniform convex bodies rather than the perimeter-uniform triangle model. Neither provides an identified assertion equivalent to the present local crossing. A broader implicit optimization formula could of course be specialized to this family; priority over unexamined specialized triangle-center literature is not asserted.

## Limitations

The exact result isolates and proves uniqueness of one exceptional shape **only for** \(7/10<h<4/5\). It does not classify possible additional coincidences among other isosceles or scalene triangles. The root decimal is merely a numerical aid. Historical originality is subject to independent literature review, and the interval checker is not independent mathematical validation.

## References

1. T. T. C. K. Zhang and J. G. Carlsson, *On the Continuous Fermat-Weber Problem for a Convex Polygon Using Euclidean Distance*, arXiv:1403.3715v1, first submitted 2014-03-14, https://arxiv.org/abs/1403.3715 .
2. E. W. Weisstein, *Spieker Center*, MathWorld, https://mathworld.wolfram.com/SpiekerCenter.html .
3. S. P. Fekete, J. S. B. Mitchell, and K. Beurer, *On the Continuous Fermat-Weber Problem*, Operations Research 53 (2005), 61–76, DOI:10.1287/opre.1040.0137.
4. P. Carmi, S. Har-Peled, and M. J. Katz, *On the Fermat-Weber Center of a Convex Object*, Computational Geometry 32 (2005), 188–195, DOI:10.1016/j.comgeo.2005.01.002.
