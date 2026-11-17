# An eight-facet insphere transition in symmetric triaugmented triangular prisms

## Finding

Consider the one-parameter family of nine-vertex spherical triaugmented triangular prisms defined below. Every member has the **same 14-triangle face structure**, yet its Euclidean incenter locus changes dimension from two to zero to one as the parameter decreases. The unique maximizer of the insphere radius within this family occurs at the zero-dimensional transition, where its largest ball contacts eight facets. The separately known maximum-volume member is on the two-dimensional side of the transition and has only two contacting facets at its symmetry center.

For \(1/2<r<1\), write
\[
h=\sqrt{1-r^2},\qquad
v(r)=\frac{\sqrt3\,r}{2\sqrt{1-r+r^2}}.
\]
There is a unique \(\rho\in(2/3,2/\sqrt7)\), numerically \(\rho=0.717869821226\ldots\), satisfying
\[
4(1-\rho+\rho^2)(1-\rho^2)=3\rho^2.
\]
For the polytope \(P_r\) defined below, its maximum-inscribed-Euclidean-ball radius is
\[
\boxed{\operatorname{inrad}(P_r)=\min\{\sqrt{1-r^2},v(r)\}.}
\]
The complete locus of centers is as follows. Put \(k=(1-r/2)/h\), \(b=(2-r)/(\sqrt3r)\), and let \(u_i\) be the equatorial unit vectors of angles \(2\pi i/3\), with \(u_i^\perp\) their counterclockwise quarter-turns, for \(i=0,1,2\).

* **\(\rho<r<1\):** The radius is \(h\); the incenter locus is the two-dimensional polygon
\[
\left\{(p,0):\ \langle u_i,p\rangle\le1-h\sqrt{1+k^2},\quad
\langle u_i\pm b u_i^\perp,p\rangle\le1-h\sqrt{1+b^2}
\quad(i=0,1,2)\right\}.
\]
At the symmetry center the ball contacts exactly the two triangular base facets.
* **\(r=\rho\):** The incenter is uniquely the origin. Its radius is \(h=v(\rho)\), and it touches exactly eight facets (both bases and all six vertical lateral triangles).
* **\(1/2<r<\rho\):** The radius is \(v(r)\); every incenter is on the explicit nondegenerate segment
\[
\left\{(0,0,z): |z|\le h-v(r)\right\}.
\]
The ball centered at the origin touches exactly the six vertical lateral facets; at either endpoint of the segment it additionally touches the corresponding base facet.

Because \(h\) strictly decreases and \(v\) strictly increases with \(r\), the unique maximum inradius over the entire displayed combinatorial family is
\[
\boxed{\max_{1/2<r<1}\operatorname{inrad}(P_r)
=\sqrt{1-\rho^2}=0.696177362295\ldots.}
\]
The inscribed spherical nine-vertex **volume** maximizer of Hoehner and Ledford has \(r_*=\sqrt3-1>\rho\) and \(h_*=\sqrt{2\sqrt3-3}=0.681250038633\ldots\). Hence its maximum inscribed ball has radius \(h_*\), while the family member that maximizes inradius has a different shape and eight, rather than two, central facet contacts.

## Assumptions and scope

All distances are measured in the standard Euclidean metric of \(\mathbb R^3\). Set
\[
u_i=(\cos(2\pi i/3),\sin(2\pi i/3)),\qquad
v_i=(\cos((2i+1)\pi/3),\sin((2i+1)\pi/3)).
\]
With \(1/2<r<1\), \(h=\sqrt{1-r^2}\), let
\[
P_r=\operatorname{conv}\Bigl(\{(u_i,0)\}_{i=0}^2\cup
\{(r v_i,h),(r v_i,-h)\}_{i=0}^2\Bigr).
\]
Its nine vertices lie on the unit sphere. The open parameter interval is essential: at \(r=1/2\) several facet planes coincide and the stated simplicial combinatorial structure changes; parameters on the other side are not claimed. The independent volume optimum quoted above is a previously published result, not part of the new extremal proof.

## Proof

**1. All fourteen facets.** Let \(p\in\mathbb R^2\), \(z\in\mathbb R\). Direct substitution in the nine defining vertices gives the complete halfspace description
\[
\tag{1}
|z|\le h,\qquad
\langle u_i,p\rangle+k|z|\le1,\qquad
\langle u_i\pm b u_i^\perp,p\rangle\le1
\quad (i=0,1,2).
\]
Here \(k=(1-r/2)/h\) and \(b=(2-r)/(\sqrt3r)\). Each of the fourteen individual bounding planes contains three affinely independent vertices: the top and bottom triples, a middle-ring vertex with two adjacent upper or lower vertices, or a middle-ring vertex with one upper and one lower vertex. At the other six vertices each inequality is strict for \(r>1/2\); in particular, the only potentially critical cross-vertex value for a vertical side plane is \(1/r-1<1\). Therefore the planes support fourteen distinct triangular facets. A three-dimensional polytope with nine vertices has at most \(2\cdot9-4=14\) facets, by Euler's relation and the fact that each facet has at least three edges, so (1) is complete. In particular, the combinatorial type is constant throughout the stated interval.

**2. The centered radius is the unrestricted inradius.** Rotation by \(2\pi/3\) about the \(z\)-axis and reflection in \(z=0\) preserve \(P_r\), and their only common fixed point is the origin. For a fixed trial radius \(t\), its feasible-center set is the intersection of the planes in (1) displaced inward by \(t\) times their Euclidean normal lengths. This set is convex and invariant under both symmetries. Averaging any feasible center under the symmetry group makes the origin feasible for the same radius. Thus the global inradius equals the centered inradius. The three facet-normal lengths are \(1\), \(\sqrt{1+k^2}\), and \(\sqrt{1+b^2}\); their corresponding distances from the origin are
\[
\tag{2} h,\qquad s=\frac{1}{\sqrt{1+k^2}},\qquad
v=\frac{1}{\sqrt{1+b^2}}=\frac{\sqrt3r}{2\sqrt{1-r+r^2}}.
\]

**3. The slanted facets never control the radius.** A direct rational simplification gives
\[
\tag{3}
\operatorname{sign}(s^2-v^2)=\operatorname{sign}(4-7r^2),
\]
indeed the numerator after clearing positive denominators is \((2-r)^2(4-7r^2)/4\). Also \(s\ge h\) holds precisely when \(r\ge2/3\). The function \(h\) decreases strictly on \((1/2,1)\), while \(v\) increases strictly there, because
\[
\frac{d}{dr}v(r)^2=\frac{3r(2-r)}{4(1-r+r^2)^2}>0.
\]
At \(r=2/3\), \(h>v\); at \(r=2/\sqrt7\), \(h<v\). Hence they cross at one \(\rho\in(2/3,2/\sqrt7)\). On \(r\ge\rho\), \(s\ge h\); on \(r\le\rho\), \(s\ge v\). Both are strict at \(\rho\), so \(\min(h,s,v)=\min(h,v)\). The crossing equation is exactly the displayed quartic. To compare the volume optimizer without decimal assumptions, note that at \(r=18/25\), \(h^2=301/625<243/499=v^2\); hence \(\rho<18/25<\sqrt3-1=r_*\). This proves the radius formula, unique maximizing parameter, central contact counts, and strict separation from the volume optimum.

**4. Every incenter.** If \(r>\rho\), the two base planes are the only tangent planes at the origin. An inball center \((p,z)\) must satisfy \(z=0\), since both \(z\le h-t\) and \(-z\le h-t\) hold with \(t=h\). Inserting \(z=0\) and shifting all the other planes inward by their normal lengths gives exactly the planar inequalities in the Finding. At \(p=0\) all those inequalities are strict by (2), so the polygon is genuinely two-dimensional.

At \(r\le\rho\), the six vertical facet constraints for radius \(v\) say \(\langle u_i\pm bu_i^\perp,p\rangle\le0\). These six normals sum to zero and span \(\mathbb R^2\); summing the constraints forces all to be equalities, hence \(p=0\). For \(r=\rho\), both base inequalities then force \(z=0\). For \(r<\rho\), the bases give \(|z|\le h-v\). It remains to check that none of the slanted facets removes a point from this segment. Their inward-shifted inequalities reduce to
\[
\tag{4} k(h-v)+v\sqrt{1+k^2}\le1.
\]
Using \(v^{-1}=\sqrt{1+b^2}\), squaring positive quantities shows (4) is equivalent to
\[
\tag{5} 3(1-r+r^2)\ge (1-r)(1+r)^3.
\]
The left side is at least \(9/4\); the right side is at most \(27/16\) on \((0,1)\) (its maximum occurs at \(r=1/2\)). Thus (5) is strict, and the whole segment is feasible. The contact counts at its interior and endpoints follow from the strict inequality and the base equations. This proves the complete center classification.

## Verification

The independent calculation in `checker.py` constructs all nine vertices and all fourteen candidate facet planes, verifies that each supports exactly three vertices, independently reconstructs convex hulls and solves the full inball linear program. It corroborates the formula, the three center regimes, and the origin's contact multiplicities at representative parameters. It also checks the decisive symbolic polynomial identity in (3). Executing `python checker.py` with NumPy, SciPy, and SymPy prints **466 passed checks**, a transition value \(\rho=0.717869821226245\ldots\), and the volume optimizer's radius. These checks support the proof but do not establish its universal quantifiers; those are settled by steps 1–4.

## Relationship to prior work

Hoehner and Ledford, *The maximum volume polytope with nine vertices inscribed in the sphere*, arXiv:2608.04392 (first submitted August 5, 2026; revised November 6, 2026), prove the unrestricted nine-vertex maximum-volume theorem and supply its explicit coordinates. Their published work establishes the volume optimizer and the geometric setting used here. This finding instead optimizes and classifies **Euclidean inscribed balls** across a one-parameter, combinatorially fixed family; in particular, the volume and inradius optima are distinct.

The classical equilateral-face Johnson solid \(J_{51}\) is a different Euclidean realization of the same combinatorial type. Published descriptions of that solid and of the volume optimum do not directly give the sharp family-wide inball transition or the complete center loci. Standard convex-symmetry averaging and linear programming are used openly as tools, not claimed as novel principles.

## Limitations

The theorem is restricted to the explicit, sphere-inscribed, threefold-symmetric family \(1/2<r<1\). It does **not** optimize the inradius over all nine-vertex inscribed polytopes, nor over all asymmetric triaugmented triangular prisms. The distinctness of the volume optimum is based on the cited maximum-volume classification. Its historical originality is provisionally assessed using accessible mathematical records and primary texts; equivalent unpublished or differently named calculations cannot be completely excluded.

## References

1. S. Hoehner and J. Ledford, *The maximum volume polytope with nine vertices inscribed in the sphere*, arXiv:2608.04392 (v1 August 5, 2026; v2 November 6, 2026), https://arxiv.org/html/2608.04392v2 .
2. E. W. Weisstein, *Triaugmented Triangular Prism*, MathWorld, https://mathworld.wolfram.com/TriaugmentedTriangularPrism.html (classical equilateral-face realization).
3. *Triaugmented triangular prism*, Polyhedra Viewer, https://polyhedra.tessera.li/triaugmented-triangular-prism/info (14-face combinatorial type).
