# A reentrant two-to-three-contact transition for the smallest sphere containing a circular helix arc

## Finding

For a unit-radius circular helix of positive pitch per radian \(\eta>0\), define
\[
\Gamma_{L,\eta}=\{(\cos t,\sin t,\eta t):-L\le t\le L\}\subset\mathbb R^3,
\qquad 0<L\le\pi.
\]
Its unique smallest enclosing Euclidean ball has center \((x_*,0,0)\), where
\[
 c=\cos L,\quad k=\eta^2L^2,\quad
 v=-\frac{k}{2(1-c)},\quad x_*=\max\{c,v\}.
\]
Its exact radius is
\[
 R(L,\eta)=
 \begin{cases}
 \sqrt{\sin^2L+\eta^2L^2},&k\ge-2c(1-c),\\[2mm]
 1+\dfrac{k}{2(1-c)},&k<-2c(1-c).
 \end{cases}
\]
This formula covers all \(0<L\le\pi\), including cases with \(c\ge0\), where the first branch necessarily applies. The contact set consists of precisely the two endpoints \(\Gamma(-L)\) and \(\Gamma(L)\) when \(k>-2c(1-c)\), and precisely these endpoints plus the central sample \(\Gamma(0)\) when \(k\le-2c(1-c)\). For fixed \(L\in(\pi/2,\pi]\), the radius is once, but not twice, continuously differentiable as a function of \(k\) across the positive threshold \(k_0=-2c(1-c)\).

There is a **reentrant contact transition** as the arc length grows with fixed pitch. On \(\pi/2<L\le\pi\), put
\[
 q(L)=\frac{-2\cos L(1-\cos L)}{L^2}.
\]
There is a unique \(L_*\in(\pi/2,\pi)\) maximizing \(q\), characterized by
\[
 -\tan L_*+\cot(L_*/2)-\frac2{L_*}=0,
 \qquad L_*=2.670778089087041\ldots,
\]
and its critical pitch is \(\eta_* =\sqrt{q(L_*)}=0.6874374448319006\ldots\). Every fixed pitch
\[
 \frac2\pi<\eta<\eta_*
\]
has exactly two distinct critical half-spans \(L_-(\eta)<L_+(\eta)\) in \((\pi/2,\pi)\). The enclosing ball contacts **two points, then three, then two again** as \(L\) increases, with the three-contact set occurring exactly for \(L\in[L_-(\eta),L_+(\eta)]\). In particular, at \(\eta=0.65\), these critical half-spans are \(2.30957875155775\ldots\) and \(3.07120882676805\ldots\).

For \(0<\eta<2/\pi\), there is one critical half-span and three contacts persist up to \(L=\pi\); for \(\eta=2/\pi\) the upper boundary occurs at \(L=\pi\). At \(\eta=\eta_*\), three contacts occur at the single half-span \(L=L_*\); for \(\eta>\eta_*\), there are always exactly two contacts. At the two root boundaries the midpoint is a third contact, but the enclosing sphere is already determined by the diametral endpoint pair.

## Assumptions and scope

The curve is a full continuum of parameter points, not merely a finite sampling. All distances are ambient Euclidean distances in \(\mathbb R^3\). The horizontal radius is one and the angular half-span is at most \(\pi\) (total angular span at most one full turn). The axial pitch parameter \(\eta\) is strictly positive; the zero-pitch circle requires a separate degenerate contact analysis and is not claimed. The smallest enclosing ball of a curve is also the smallest enclosing ball of its convex hull. A contact is a point of the curve on the boundary sphere.

The pitch here means vertical advance per radian; the physical rise over a full turn would be \(2\pi\eta\). Rotating/translating the curve preserves the result, but arbitrary anisotropic changes of Euclidean coordinates need not.

## Proof

**1. Uniqueness and symmetry.** For any nonempty compact \(K\subset\mathbb R^3\), the function \(z\mapsto\max_{y\in K}\|z-y\|^2\) is strictly convex, being \(\|z\|^2\) plus a maximum of affine functions of \(z\). It is coercive, so it has exactly one minimizer. The isometry \((x,y,z)\mapsto(x,-y,-z)\) sends the helix at parameter \(t\) to the point at \(-t\). Uniqueness therefore forces its optimal center to have the form \((x,0,0)\).

**2. Farthest-parameter reduction.** The squared distance to such a center equals
\[
 d_x(t)^2=1+x^2+\eta^2t^2-2x\cos t.
\]
By evenness it suffices to consider \(t\in[0,L]\). Let \(f_x(t)=\eta^2t^2-2x\cos t\). If \(x\ge0\), then \(f_x'(t)=2\eta^2t+2x\sin t>0\) for \(0<t<L\le\pi\). If \(x<0\), then
\[
 f_x'(t)=2t\left(\eta^2+x\frac{\sin t}{t}\right).
\]
The function \(\sin t/t\) is strictly decreasing on \((0,\pi)\), hence the parenthesized expression is strictly increasing for \(x<0\). Therefore \(f_x\) either increases throughout or first decreases and then increases, and in either case all global maxima lie at \(t=0\) or \(t=L\); any interior parameter is strictly below their larger value. The exact minimax objective is consequently
\[
 F(x)=\max_{-L\le t\le L}d_x(t)^2
 =\max\{(1-x)^2,\ 1+x^2+k-2cx\}.
\]
No finite mesh or assumption about an unverified farthest point is used here.

**3. Exact minimization and contact set.** The two quadratics in \(F(x)\) intersect only at \(v=-k/[2(1-c)]<0\). The first is active for \(x\le v\) and strictly decreases there, because \(x<1\). For \(x\ge v\), the second is active and attains its constrained minimum at \(\max\{c,v\}\). This proves \(x_*=\max\{c,v\}\) and uniqueness. When \(c\ge v\), the endpoint chord has midpoint \((c,0,0)\) and half-length \(\sqrt{\sin^2L+k}\), proving the first radius formula. The third point \(t=0\) is on the sphere exactly at equality \(c=v\). When \(c<v\), both quadratics are active at \(x=v\), and \(F(v)=(1-v)^2\), proving the second radius formula. The strict interior inequality in Step 2 proves that there are no additional curve contacts. At \(c<v\), the center lies strictly between the midpoint of the endpoints and \(\Gamma(0)\), giving an independent positive three-contact barycentric certificate for minimality; for \(c\ge v\) the diametral endpoints alone certify minimality.

**4. One-dimensional phase boundary.** The three-contact condition \(c\le v\) requires \(c<0\), hence \(L>\pi/2\), and is equivalent to \(\eta^2\le q(L)\). On this interval,
\[
 \frac{d}{dL}\log q(L)=-\tan L+\cot(L/2)-\frac2L,
\]
\[
 \frac{d^2}{dL^2}\log q(L)
 =-\sec^2L-\frac12\csc^2(L/2)+\frac2{L^2}<0.
\]
Indeed, the first two negative terms sum to at most \(-3/2\), while \(2/L^2<8/\pi^2<3/2\). The first logarithmic derivative tends to \(+\infty\) at \(\pi/2\) from above and tends to \(-2/\pi\) at \(\pi\); it therefore has exactly one zero \(L_*\). Since \(q(\pi/2+)=0\) and \(q(\pi)=4/\pi^2\), every horizontal level strictly between \(4/\pi^2\) and \(q(L_*)\) is crossed twice, proving reentrance and all remaining boundary cases. The quoted numbers are obtained by ordinary bisection of this strictly monotone derivative and of the two strict boundary crossings, not by an unproved global numerical optimization.

**5. Regularity at contact creation.** Fix \(L>\pi/2\), put \(d=1-c>0\) and \(k_0=-2cd\). Near the transition, the three-contact radius (on \(k\le k_0\)) is \(1+k/(2d)\), while the two-contact radius (on \(k\ge k_0\)) is \(\sqrt{1-c^2+k}\). Both have value \(d\) and first derivative \(1/(2d)\) at \(k_0\). Their second derivatives are respectively \(0\) and \(-1/(4d^3)\), proving exactly \(C^1\), not \(C^2\), regularity.

## Verification

The standalone Python 3 standard-library file `VERIFY.py` checks the exact minimax radius and center at 96 parameter choices spanning all regimes and transition boundaries; at each choice it evaluates 1,201 points of the continuous helix as a *finite diagnostic only*, along with 121 alternative candidate centers. It checks the unique maximum of the critical pitch function, the two crossing parameters for the reentrant example, contact types, and one-sided second derivatives. The observed output is `HELIX_ENCLOSING_BALL_REENTRANT_CHECKS_OK`. The analytic steps above, not these finite checks, establish the statements for all real parameters in scope.

## Relationship to prior work

Minimum-enclosing-ball/Chebyshev-center theory is classical. The open full text of Jahn (2014), especially its introduction and finite two-/three-contact discussion, treats planar finite-site problems and their algorithms, not the exact finite three-dimensional helix arc or nonmonotone phase boundary. González, Maddocks and Smutny (2002) study circles and spheres associated with helical curvature and thickness, defined through *minimum* local/multipoint radius, rather than the **minimum sphere containing an entire finite helix segment**. The published published-finding corpus moment-curve sphere calculation concerns polynomial moment curves \((t,t^2,\ldots,t^d)\), not this trigonometric spatial helix; its exact center and parameter thresholds do not imply these formulas. Chan and Pathak (2014) address approximation algorithms for arbitrary finite point sets, not the contact classification for a continuum arc. Matching the word 'helix' or 'enclosing sphere' is therefore not sufficient for coverage, and conversely unsuccessful searches cannot establish global historical novelty.

## Limitations

The phase classification is limited to total angular span at most \(2\pi\) and strictly positive pitch; longer arcs may have different interior farthest-point structure. There is no claim of a universal theorem for generic space curves, anisotropic metrics, or arbitrary helices. Finite checker runs are corroborating calculations, not completeness proofs. The literature comparison supports provisional originality only; an overlooked specialized treatment of helix circumballs remains possible, and independent mathematical review has not been performed.

## References

- T. Jahn, *Geometric Algorithms for Minimal Enclosing Discs in Strictly Convex Normed Planes*, arXiv:1410.4725, first public October 17, 2014, https://arxiv.org/abs/1410.4725 .
- O. González, J. H. Maddocks, and J. Smutny, *Curves, circles, and spheres*, Contemporary Mathematics (2002), https://sma.epfl.ch/lcvmwww/publications/data/articles/65/paper.pdf .
- T. M. Chan and V. Pathak, *Streaming and dynamic algorithms for minimum enclosing balls in high dimensions*, Computational Geometry 47 (2014), 240–247, https://doi.org/10.1016/j.comgeo.2013.05.007 .
- P. Martín, H. Martini and M. Spirova, *Chebyshev Sets and Ball Operators*, J. Convex Analysis 21 (2014), 601–618, https://journalofconvexanalysis.com/articles/jca21032/ .
- *Two and three contact points for minimum enclosing spheres of symmetric moment-curve hulls*, published November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-and-three-contact-points-for-minimum-enclosing-spheres-of-sy--6a878f319c33 .
