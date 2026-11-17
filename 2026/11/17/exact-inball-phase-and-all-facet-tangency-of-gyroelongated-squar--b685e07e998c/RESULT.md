# Exact inball phase and all-facet tangency of gyroelongated square bipyramids

## Finding
For \(3-2\sqrt2<h<1\), define \(r=\sqrt{1-h^2}\), two apices \(a_\pm=(0,0,\pm1)\), and eight alternating-latitude vertices
\[
v_j=(r\cos(\pi/8+j\pi/4),\ r\sin(\pi/8+j\pi/4),\ (-1)^j h),\qquad j=0,\ldots,7.
\]
Let \(P_h=\operatorname{conv}\{a_+,a_-,v_0,\ldots,v_7\}\). Its unrestricted Euclidean inradius is
\[
\operatorname{inrad}(P_h)=
\begin{cases}
\sqrt{(1+h)/(3-h)},&3-2\sqrt2<h\le\sqrt2-1,\\
\displaystyle\left[\frac{(4-2\sqrt2)^2}{1-h^2}+\frac{(3-2\sqrt2)^2}{h^2}\right]^{-1/2},&\sqrt2-1\le h<1.
\end{cases}
\]
The unique inradius-maximizing height is \(h_0=\sqrt2-1\), and the sharp inradius is
\[
\boxed{\operatorname{inrad}(P_{h_0})=\sqrt{\frac{1+2\sqrt2}{7}}}.
\]
At \(h=h_0\), exactly all sixteen triangular facets are tangent to the unique maximal insphere, centered at the origin. The unique maximum-volume height for the same symmetric family, \(h_V=(\sqrt{10+6\sqrt2}-1)/(3(1+\sqrt2))\), is strictly greater than \(h_0\); hence the two geometric objectives have distinct optimizers. This is a sharp **within-family** theorem. No global covering optimality among arbitrary ten-point sphere configurations is asserted.

## Assumptions and scope
All geometry is Euclidean in \(\mathbb R^3\), with the ten points constrained to the unit sphere. The open height interval is precisely the nondegenerate gyroelongated-square-bipyramid range in this symmetric parametrization. The inradius allows the center of the inscribed sphere to vary freely. The endpoint \(h=3-2\sqrt2\) is excluded because the facet combinatorics changes there; \(h=1\) is degenerate. The angular covering radius of these sites on the unit sphere is \(\arccos(\operatorname{inrad}(P_h))\), because the origin-centered supporting planes encode the spherical Voronoi cells.

## Proof
**Supporting faces.** The source configuration has four upper cap triangles \([a_+,v_{2i},v_{2i+2}]\), four lower cap triangles \([a_-,v_{2i+1},v_{2i+3}]\), and eight belt triangles \([v_j,v_{j+1},v_{j+2}]\), with indices interpreted cyclically. Their supporting inequalities are verified directly from the ten coordinates. For instance, rotate the horizontal coordinates so that two neighboring upper-ring vertices have horizontal coordinates \((r/\sqrt2,\pm r/\sqrt2)\), while the intervening lower-ring vertex has horizontal coordinates \((r,0)\). The upper cap has equation
\[
\frac{\sqrt2(1-h)}{r}\,x+z=1.
\]
The belt triangle containing those three ring vertices has equation
\[
\frac{4-2\sqrt2}{r}\,x+\frac{3-2\sqrt2}{h}\,z=1.
\]
The other cap and belt equations follow by rotational and reflection symmetries. For every \(h>3-2\sqrt2\), the remaining vertices lie strictly on the inward side of each plane: the restrictive cap test is \(\sqrt2(1-h)-h<1\), and the restrictive belt test is \((3-2\sqrt2)/h<1\). All other tests follow from smaller horizontal projections. Thus these are sixteen distinct exposed triangular facets. Since all ten generating points lie on the sphere and are distinct, they are extreme vertices. Euler's planar formula gives at most \(2(10)-4=16\) triangular facets for any simplicial triangulation, so the listed faces exhaust the boundary; there are no hidden face orbits.

**Distances and free-center optimality.** The distances of the cap and belt planes from the origin are, respectively,
\[
C(h)=\sqrt{\frac{1+h}{3-h}},\qquad
L(h)=\left[\frac{(4-2\sqrt2)^2}{1-h^2}+\frac{(3-2\sqrt2)^2}{h^2}\right]^{-1/2}.
\]
For any candidate inball radius \(t\), the set of feasible centers is convex and invariant under the full symmetry group of \(P_h\). Averaging a feasible center over this group gives the origin, so the unrestricted inradius equals \(\min\{C(h),L(h)\}\). Let \(A=4-2\sqrt2\) and \(B=3-2\sqrt2\). Multiplying the sign of \(C(h)^2-L(h)^2\) by the positive quantity \((3-h)[A^2h^2+B^2(1-h^2)]\) gives
\[
F(h)=-(h+1)(h-B)(h-\sqrt2+1)
\bigl(h^2-(2+\sqrt2)h+1-\sqrt2\bigr).
\]
The last quadratic is negative on \((0,1)\). Therefore \(C(h)<L(h)\) for \(B<h<\sqrt2-1\) and \(L(h)<C(h)\) for \(\sqrt2-1<h<1\), proving the asserted piecewise profile.

**Sharpness and contacts.** The cap distance \(C(h)\) is strictly increasing. The belt distance \(L(h)\) is strictly decreasing once \(h^2>B/(A+B)\), as follows by differentiating \(L(h)^2=h^2(1-h^2)/(B^2+(A^2-B^2)h^2)\). Because \(B/(A+B)<B=(\sqrt2-1)^2\), the belt distance decreases throughout \(h\ge h_0\). The two branches therefore meet at the unique global maximum \(h_0=\sqrt2-1\). Substitution yields the claimed radical inradius. At the crossing all eight cap and all eight belt facets have identical distance, so all sixteen are tangent to the origin-centered sphere. If another center achieved the same radius, its signed distances from all sixteen outward unit normals would be nonpositive. Symmetry makes those normals sum to zero, so every signed distance would vanish; since the normals span \(\mathbb R^3\), the center must be the origin.

**Volume contrast.** The already-established volume formula for this family is \(\operatorname{vol}_3(P_h)=\tfrac43(1-h^2)(1+(1+\sqrt2)h)\). Its derivative vanishes at the unique interior maximizer \(h_V=(\sqrt{10+6\sqrt2}-1)/(3(1+\sqrt2))\). Algebra gives \(h_0<h_V\): after multiplying by \(3(1+\sqrt2)\), the inequality becomes \(\sqrt{10+6\sqrt2}>4\), which follows from \(\sqrt2>1\). Hence \(\operatorname{vol}_3(P_{h_0})<\operatorname{vol}_3(P_{h_V})\) while \(\operatorname{inrad}(P_{h_0})>\operatorname{inrad}(P_{h_V})\).

## Verification
The standalone standard-library script `verify.py` independently enumerates all supporting triples among the ten vertices, retains actual supporting planes, and verifies sixteen triangular facets, their minimum origin distance, and the divergence-theorem volume formula over 201 interior parameter values and seven boundary/critical samples. It passes 620 finite checks and reproduces the exact numerical specializations. The proof above, not finite sampling, establishes every real height in the stated interval.

## Relationship to prior work
Hoehner's November 7, 2026 manuscript proves that the **volume** of a ten-vertex sphere-inscribed polytope is globally maximized by the specified gyroelongated square bipyramid and supplies its coordinates and volume. Its facial description also identifies the sixteen relevant triangles. This paper's global volume result and symmetry class are used, not presented as new. Hardin, Sloane and Smith's 1994 table records a putatively optimal **ten-site spherical covering radius** \(42.3078266^\circ\); the value agrees with \(\arccos\sqrt{(1+2\sqrt2)/7}\) to table precision. Thus neither the numerical covering value nor the proposal of this covering configuration is claimed as novel. The present assertion is the exact inradius profile over the *entire symmetric combinatorial family*, its unique height optimizer, the simultaneous sixteen-facet tangency with center rigidity, and its proven distinction from the new volume-maximizing realization. Published covering results for two latitude rings without two poles treat a different generating set and do not by themselves imply this ten-vertex profile.

## Limitations
The sharpness claim is restricted to the stated one-parameter family and does not prove global optimality among all spherical ten-point sets or arbitrary ten-vertex inscribed polyhedra. Earlier literature could include a derivation of the same full profile under spherical-covering terminology; historical priority is therefore provisional. The 1994 numerical database is treated as genuine prior numerical evidence, not dismissed because it lacks a displayed symbolic profile. No independent mathematical audit has been performed.

## References
1. S. Hoehner, *On maximum volume polytopes inscribed in the sphere*, arXiv:2611.10777v1 (first public November 7, 2026), especially Theorem 1.1 and the ten-vertex facet description. https://arxiv.org/abs/2611.10777
2. R. H. Hardin, N. J. A. Sloane and W. D. Smith, *Spherical Coverings*, numerical library (1994), ten-point entry. https://neilsloane.com/coverings/index.html
3. H. Cohn, *Sloane's tables of point configurations on spheres*, numerical covering compilation, ten-point entry. https://cohn.mit.edu/sloane/
