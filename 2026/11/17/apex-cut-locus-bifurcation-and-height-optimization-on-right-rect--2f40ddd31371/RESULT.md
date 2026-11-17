# Apex cut-locus bifurcation and height optimization on right rectangular pyramids

## Finding
Fix real numbers \(a\ge b>0\) and \(h>0\). Let \(S\) be the complete intrinsic surface of the convex right rectangular pyramid with base \(K=[-a,a]\times[-b,b]\) in the plane \(z=0\) and apex \(v=(0,0,h)\). Intrinsic distance means the infimum of lengths of surface paths; the base face is included. Write
\[
 s_a=\sqrt{h^2+a^2},\quad s_b=\sqrt{h^2+b^2},\quad C_a=a+s_a,\quad C_b=b+s_b,
 \quad t=\frac{C_b}{C_a},\quad u=a-bt.
\]
The following conclusions hold for every such pyramid, without genericity assumptions.

**Exact distance and cut locus.** For every \((x,y)\in K\),
\[
 d_S(v,(x,y,0))^2=\min\left\{(C_a-|x|)^2+y^2,\quad x^2+(C_b-|y|)^2\right\}.
\]
On every lateral triangular face the distance to \(v\) is the ordinary Euclidean chord distance within that face. If \(a>b\), the cut locus from \(v\) consists exactly of the base segment joining \((-u,0)\) to \((u,0)\) and the four straight base segments joining \((u,0)\) to \((a,\pm b)\) and \((-u,0)\) to \((-a,\pm b)\). It is a tree with two trivalent branch nodes, both interior to the base. At the square case \(a=b\), \(u=0\), and the cut locus is the four base diagonals from the center to the corners, with one degree-four branch node.

**Farthest points and cut-locus length.** The farthest surface points from the apex are exactly \((\pm u,0,0)\) when \(a>b\), and exactly the base center when \(a=b\). The apex eccentricity and total intrinsic cut-locus length are respectively
\[
 E=\sqrt{C_b^2+u^2},\qquad
 \mathcal L=2u+4b\sqrt{1+t^2}.
\]
Thus even an arbitrarily small rectangular distortion of a square base separates its unique farthest point into two farthest points, and splits its four-valent cut-locus node into two trivalent nodes.

**Sharp height optimization.** Keep \(a\ge b\) fixed and let \(h\) vary over \((0,\infty)\). If \(a=b\), then \(\mathcal L=4\sqrt2\,a\) for *every* positive height. If \(1<a/b\le\sqrt3\), then \(\mathcal L\) increases strictly with height, and its infimum is the unattained zero-height limit
\[
 \inf_{h>0}\mathcal L=2a-\frac{2b^2}{a}+4b\sqrt{1+\frac{b^2}{a^2}}.
\]
If \(a/b>\sqrt3\), there is exactly one minimizing positive height,
\[
 \boxed{h_*=\sqrt{3a^2+3b^2-4\sqrt3\,ab}},
 \qquad \boxed{\mathcal L(h_*)=2a+2\sqrt3\,b}.
\]
Below this height the length decreases strictly, and above it the length increases strictly. Hence the aspect-ratio threshold \(\sqrt3\) separates two qualitatively distinct cut-locus-length responses to changing the pyramid height.

## Assumptions and scope
The base is a genuine Euclidean rectangle with half-side lengths \(a,b\), and the apex lies strictly above its center. The entire closed polyhedral boundary (base plus four triangles) carries its intrinsic length metric. The convention \(a\ge b\) only labels the longer base direction; exchanging axes covers all nondegenerate right rectangular pyramids. The cut locus is the closure of points other than the source admitting multiple minimizing surface geodesics. The limiting expression as \(h\downarrow0\) is an infimum over positive-height pyramids, not a claim about a degenerate zero-height polyhedron.

## Proof
**1. Unfolded-source distance, with global justification.** For a point \(p\) on a lateral face, its straight segment from the apex lies in that face, and attains the ambient Euclidean lower bound for any surface path. Therefore \(d_S(v,p)=|v-p|\), with a unique minimizing path (also on common lateral edges).

For a base point \(p\), any surface path from the apex has a first contact \(q\) with the base boundary. Its length up to \(q\) is at least the ambient chord length \(|v-q|\), and its length from \(q\) to \(p\) is at least the planar chord \(|p-q|\). Both lower bounds are simultaneously attainable: \(v\) and each base-edge point \(q\) lie on a common triangular face, and the base segment \([q,p]\) is contained in the rectangle. Thus
\[
 d_S(v,p)=\min_{q\in\partial K}\bigl(|v-q|+|p-q|\bigr).
\]
Unfold the triangular face adjacent to the edge \(x=a\) into the base plane. The image of its apex is \((C_a,0)\). For \(p=(x,y)\in K\), the segment from this image to \(p\) crosses \(x=a\) at ordinate \(y_* =y\,s_a/(C_a-x)\). Since \(C_a-x\ge s_a\), one has \(|y_*|\le |y|\le b\), so the crossing lies on the actual edge. The triangle inequality is therefore sharp and the minimum through this edge equals \(\sqrt{(C_a-x)^2+y^2}\). The other edges analogously give image points \((-C_a,0)\), \((0,C_b)\), \((0,-C_b)\) and corresponding unfolded Euclidean distances. Taking the minimum of these four proves the displayed exact formula and also proves that no additional traversals through other surface faces improve it.

**2. Complete cut locus.** Interior points of lateral triangular faces have unique straight-to-apex minimizing paths. For an interior base point, the distinct shortest paths correspond precisely to distinct nearest sites among the four unfolded apex images. By reflection symmetry, in the first quadrant the two candidate squared distances are \((C_a-x)^2+y^2\) and \(x^2+(C_b-y)^2\). Their equality is the line
\[
 C_a x-C_b y=\frac{C_a^2-C_b^2}{2}=aC_a-bC_b,
\]
where the second equality uses \(C_a^2-2aC_a=C_b^2-2bC_b=h^2\). It joins the corner \((a,b)\) to \((u,0)\). Reflecting in the coordinate axes yields four corner arms; the equal distances to the north and south images on \(y=0\) yield the intervening segment \([-u,u]\times\{0\}\). Since \(C_a>C_b\) exactly when \(a>b\), one has \(0<u<a\) in that case, and the branch nodes are distinct. If \(a=b\), \(C_a=C_b\), \(u=0\), and all four arms meet at the center. No other ties occur in either the lateral faces or base interiors; the base vertices are endpoints in the closure of the cut locus.

**3. Farthest-point rigidity.** The lateral-face distance squared is convex on each triangular face, and hence maximized at a face vertex, with maximum \(h^2+a^2+b^2\). In the base, each Voronoi cell of an unfolded apex site is convex. Its distance squared is a convex quadratic, so a maximum on that cell occurs at a vertex of the cell polygon. These vertices are among the four base corners and the two branch nodes \((\pm u,0)\) (or the single center when \(u=0\)). The branch-node distance squared is \(C_b^2+u^2\), and its gap above the base-corner and lateral-vertex squared distance is
\[
 C_b^2+u^2-(h^2+a^2+b^2)
 =\frac{2b s_b}{C_a}(s_a+bt)>0.
\]
The farthest points are therefore exactly the stated branch nodes. In the square case they coincide at the base center.

**4. Metric length and height transition.** The central segment has length \(2u\). Each of the four other arms has Euclidean length \(\sqrt{(a-u)^2+b^2}=b\sqrt{1+t^2}\), giving \(\mathcal L=2a-2bt+4b\sqrt{1+t^2}\). When \(a>b\), the parameter \(t\) increases strictly with \(h\), since
\[
 \frac{d}{dh}\log t=\frac{1}{h}\left(\frac{a}{\sqrt{h^2+a^2}}-\frac{b}{\sqrt{h^2+b^2}}\right)>0,
\]
and has endpoint limits \(b/a\) and \(1\). Differentiating the length with respect to \(t\) gives
\[
 \frac{d\mathcal L}{dt}=2b\left(-1+\frac{2t}{\sqrt{1+t^2}}\right),
\]
which is negative for \(t<1/\sqrt3\) and positive for \(t>1/\sqrt3\). If \(a/b>\sqrt3\), this critical ratio is traversed exactly once. Solving \(t=1/\sqrt3\) with the two identities \(C_a^2-2aC_a=C_b^2-2bC_b=h^2\) gives \(h_*^2=3a^2+3b^2-4\sqrt3 ab\); substituting into the length gives \(2a+2\sqrt3 b\). If \(1<a/b\le\sqrt3\), the derivative remains positive for all positive heights, giving the stated unattained infimum. If \(a=b\), then \(t=1\) for all heights and \(\mathcal L=4\sqrt2 a\). This completes all assertions.

## Verification
The independently executable `check.py` in this package computes the intrinsic apex distance by numerical minimization over each base-edge crossing, separately from the four-image distance expression. Across seven rectangular/square parameter configurations and 100 interior sample targets per configuration, the two calculations agree to the declared numerical tolerance. Additional checks verify the exact branch-junction equalities, the positive farthest-corner gap, the optimizing-height formula, the monotonic and nonmonotonic regimes, and the square-base invariance. Its output is `RECTANGULAR_PYRAMID_APEX_CUT_LOCUS_CHECKS_OK`.

Execute `python3 check.py` using Python 3 standard-library modules only. The analytic proof, not the finite tests, establishes the assertions for all real parameters. The package contains no claim of external proof certification or statistical evidence of novelty.

## Relationship to prior work
Miller and Pak, *Metric combinatorics of convex polyhedra: cut loci and nonoverlapping unfoldings* (public preprint 2003), establish the general polyhedral source-image/Voronoi characterization (Theorem 2.9) and algorithmic construction. The present work uses that classical perspective but proves a concrete *complete, parameterized* nonsquare right-rectangular-pyramid cut-locus classification and an exact height-minimization phase transition. The general algorithm does not state these explicit formulas or the \(\sqrt3\) aspect threshold.

The publicly available note *Apex distance tails reconstruct every right regular pyramid* treats only **regular** polygonal bases, including the square case. Its base-center cut-locus and farthest-point results agree with the \(a=b\) boundary of the present formulas; the nonsquare rectangle's two farthest points, trivalent tree and height-optimization threshold lie outside its hypotheses. O'Rourke and Vîlcu's *Skeletal Cut Loci on Convex Polyhedra* (2023 first preprint) treats possible abstract trees and skeletal realizations, not these apex-source right-rectangular metric formulas. Zamfirescu's *Antipodal trees and mutually critical points on surfaces* concerns general finiteness of farthest-point sets, not the explicit bifurcation here.

## Limitations
Only right rectangular pyramids with the apex directly above the base center and positive height are treated. The theorem is a classification within that three-parameter family, not a general solution for oblique pyramids, other polygonal bases, arbitrary source points, or variable edge weights. The square boundary case is shared with previously known regular-pyramid work and is not separately claimed as new. Published general source-image algorithms underlie the method, and specialist historical priority for the explicit nonsquare formula still calls for independent review. No independent mathematical audit has been performed.

## References
1. E. Miller and I. Pak, *Metric combinatorics of convex polyhedra: cut loci and nonoverlapping unfoldings*, arXiv:math/0312253v1, first posted 12 December 2003, https://arxiv.org/abs/math/0312253 . Theorem 2.9 and Sections 2 and 8.8 were inspected in the accessible full text.
2. J. O'Rourke and C. Vîlcu, *Skeletal Cut Loci on Convex Polyhedra*, arXiv:2312.01534v1, first posted 3 December 2023, https://arxiv.org/abs/2312.01534 . Introduction and construction sections were inspected in accessible full text.
3. T. Zamfirescu, *Antipodal trees and mutually critical points on surfaces*, Advances in Geometry 7 (2007), 385–390, https://doi.org/10.1515/ADVGEOM.2007.024 . Public abstract and bibliographic description were inspected, not complete text.
4. *Apex distance tails reconstruct every right regular pyramid*, publicly accessible mathematical note (2026), examined in full for its regular-base restriction and explicit square-base result; bibliographic author attribution is not asserted.
