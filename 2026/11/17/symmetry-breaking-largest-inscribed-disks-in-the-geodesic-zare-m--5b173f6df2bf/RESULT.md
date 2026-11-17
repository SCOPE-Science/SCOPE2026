# Symmetry-breaking largest inscribed disks in the geodesic Zare monotiles

## Finding

For every even integer \(q\ge 2\), the geodesic hyperbolic \((2q+3)\)-gon \(T_q\) defined below is invariant under reflection in the vertical geodesic \(x=L/2\), yet **no center of a largest inscribed hyperbolic disk lies on that reflection axis**. The largest radius attainable by a disk whose center is constrained to the axis is exactly
\[
\rho_{\mathrm{axis}}(q)=\frac12\log\!\left(\frac{1+1/q}{\sqrt{1+1/(4q^4)}}\right).
\]
Its unique axis-constrained maximizing center is \((L/2,\sqrt{rH})\). The unrestricted inradius is strictly greater than \(\rho_{\mathrm{axis}}(q)\); hence it has at least two distinct, reflection-related maximizing centers. This is an infinite family of nonconvex, arbitrarily small-diameter hyperbolic monotiles for which symmetrizing an inball center loses optimality.

## Assumptions and scope

Work in the curvature \(-1\) upper half-plane \(\mathbb H^2=\{(x,y):y>0\}\) with metric \(ds^2=(dx^2+dy^2)/y^2\). For each even \(q\ge 2\), put
\[
\delta=q^{-2},\quad r=(q+1)/q,\quad H=\sqrt{1+\delta^2/4},\quad L=(q+1)\delta.
\]
Let \(\varphi\) be the \(\delta\)-periodic continuous function specified, for each integer \(k\) and \(k\delta\le x\le(k+1)\delta\), by
\[
\varphi(x)=\sqrt{H^2-(x-(k+1/2)\delta)^2}.
\]
Define the compact geodesic polygon
\[
T_q=\{(x,y):0\le x\le L,\quad \varphi(x)\le y\le r\varphi(x/r)\}.
\]
The construction and congruent tiling are those of Liao and Wang, Section 7.2, arXiv:2610.05438v1. A disk is *inscribed* if its closed hyperbolic metric ball is contained in \(T_q\); the inradius is the supremum of all such radii. No exact value for the unrestricted inradius is asserted here. Reflection means the hyperbolic isometry \((x,y)\mapsto(L-x,y)\).

## Proof

**Reflection and boundary locations.** The function \(\varphi\) is even about every integer multiple of \(\delta\), and \(L=(q+1)\delta\), \(L/r=q\delta\). Consequently \(\varphi(L-x)=\varphi(x)\) and \(\varphi((L-x)/r)=\varphi(x/r)\); thus the indicated reflection preserves \(T_q\). Let \(x_0=L/2\). Because \(q\) is even, \(x_0=(q/2+1/2)\delta\) is the center of one lower circular arc, whereas \(x_0/r=(q/2)\delta\) is a join of two upper arcs. Hence the lower and upper boundary heights above \(x_0\) are exactly \(H\) and \(r\), respectively. Observe \(1\le\varphi\le H<r\), so the closed Euclidean rectangle \([0,L]\times[H,r]\) is contained in \(T_q\).

**Sharp axis-constrained radius.** A disk of hyperbolic radius \(\rho\) centered at \((x_0,y)\) includes the vertical geodesic points \((x_0,y e^{-\rho})\) and \((x_0,y e^{\rho})\). Inclusion in \(T_q\) thus gives
\[
\rho\le\min\{\log(y/H),\ \log(r/y)\}\le\rho_0:=\tfrac12\log(r/H),
\]
with equality in the second inequality only for \(y=y_0:=\sqrt{rH}\). The hyperbolic disk of radius \(\rho_0\) centered at \(P_0=(x_0,y_0)\) is a Euclidean disk centered at \((x_0,y_0\cosh\rho_0)\) with Euclidean radius \(y_0\sinh\rho_0\). Its vertical extrema are \(y_0e^{-\rho_0}=H\) and \(y_0e^{\rho_0}=r\), and its horizontal half-width is \((r-H)/2\). Since
\[
L=(q+1)/q^2>1/q\ge r-H,
\]
it lies in \([0,L]\times[H,r]\subset T_q\). This proves the exact axis-constrained formula and uniqueness of \(P_0\).

**Strict off-axis improvement.** The disk just constructed meets \(\partial T_q\) only at its bottom \(A=(x_0,H)\) and its top \(B=(x_0,r)\): every other part of the lower boundary has height at most \(H\), every other part of the upper boundary has height at least \(r\), the disk reaches those levels only at \(x_0\), and it misses both vertical sides strictly. At \(A\) the lower boundary is a smooth geodesic arc, supported by the Euclidean circle with center \((x_0,0)\) and radius \(H\); \(A\) lies in its relative interior. At \(B\) two upper geodesic arcs meet in a strict upward corner. With \(s=x-x_0\), their upper boundary graph near \(B\) is
\[
y=r+(\delta/2)|s|+O_q(s^2).
\]

Fix \(y_0\) and move the ball center horizontally to \(P_t=(x_0+t,y_0)\). The hyperbolic distance from \(P_t\) to the *entire supporting geodesic* of the lower arc at \(A\) is, for all sufficiently small \(|t|\),
\[
d_-(t)=\operatorname{arsinh}\left(\frac{t^2+y_0^2-H^2}{2Hy_0}\right),
\]
and its orthogonal foot remains in the relative interior of that arc. Since \(d_-(0)=\rho_0\), this distance strictly increases for every sufficiently small \(t\ne0\).

Likewise, for small \(|t|\), the nearest point to \(P_t\) on the two upper arcs adjacent to \(B\) is the corner \(B\) itself. To verify this last assertion, for an upper-edge point \((x_0+s,Y(s))\) near \(B\) we have \(Y(0)=r\), \(Y'(0+)=\delta/2\), and \(Y'(0-)=-\delta/2\). Differentiating the hyperbolic distance through
\[
\cosh d(P_t,(x_0+s,Y(s)))=1+\frac{(s-t)^2+(Y(s)-y_0)^2}{2y_0Y(s)}
\]
shows that the right derivative at \(s=0\), for \(t=0\), is \(\frac{\delta}{4y_0}(1-y_0^2/r^2)>0\), while the left derivative is its negative. These strict one-sided inequalities persist for small \(|t|\), so \(B\) is the unique local closest boundary point there. Its distance satisfies
\[
\cosh d_+(t)=1+\frac{t^2+(r-y_0)^2}{2r y_0}
=\cosh\rho_0+\frac{t^2}{2r y_0},
\]
which is strictly greater than \(\cosh\rho_0\) for \(t\ne0\).

Finally, remove small open neighborhoods of \(A\) and \(B\) from the compact boundary. Its distance from \(P_0\) is strictly greater than \(\rho_0\), so by continuity the same remains true for \(P_t\) at all sufficiently small \(|t|\). The two displayed local-distance formulas show that the distances to the remaining boundary arcs near \(A\) and \(B\) are also strictly greater than \(\rho_0\) when \(0<|t|\ll_q1\). Therefore
\[
d_{\mathbb H^2}(P_t,\partial T_q)>\rho_0
\]
for some (indeed all sufficiently small nonzero) \(t\). Since \(P_t\) is interior, the closed ball of any radius strictly between \(\rho_0\) and this boundary distance is contained in \(T_q\). Thus the unrestricted inradius is strictly greater than \(\rho_0\).

Compactness of \(T_q\) implies that the continuous distance-to-boundary function attains a maximum. None of its maximizers can lie on the reflection axis, by the sharp axis constraint. Reflecting any maximizer yields a second, distinct maximizer. This proves every assertion. \(\square\)

## Verification

All geometric formulas above follow from the elementary upper-half-plane distance identity
\[
\cosh d((x,y),(u,v))=1+\frac{(x-u)^2+(y-v)^2}{2yv}.
\]
For the lower supporting semicircle of Euclidean radius \(H\) centered at \((x_0,0)\), the signed geodesic distance is \(\operatorname{arsinh}(((x-x_0)^2+y^2-H^2)/(2Hy))\) on the region above it. Numerical regression tests of the axis radius, strict local improvement, boundary corner derivatives, and the vertical-side clearance are provided in the standalone \(\texttt{verify.py}\). The proof, rather than these finite tests, covers every even \(q\ge2\).

## Relationship to prior work

Liao and Wang (arXiv:2610.05438v1, Section 7.2) define exactly these nonconvex monotiles, establish the tiling, and bound their area and diameter. Their construction is adopted without alteration. The published result “Exact diameter of the geodesic Zare monotiles” gives the exact opposite-extreme-point metric diameter, not distances to the boundary or the location of largest inscribed disks. Standard maximum-inscribed-circle algorithms address arbitrary polygons but do not imply the exact axis-constrained formula or this even-parameter symmetry-breaking statement without a new geometric analysis. Unlike convex invariant bodies, a nonconvex reflection-symmetric region need not have a largest ball centered on its reflection axis; this theorem supplies an explicit natural tiling family illustrating the obstruction.

## Limitations

The unrestricted inradius and the full set of incenter positions are not determined. The theorem addresses even integers \(q\); no classification of odd-parameter incenters is claimed. The result is specific to the curvature \(-1\) geodesic family, not a theorem about all hyperbolic monotiles. The numerical tests are finite checks and do not certify the infinite-parameter proof; historical priority remains open to independent verification.

## References

1. Y. Liao and E. Wang, *Area and diameter gaps for hyperbolic monotiles*, arXiv:2610.05438v1 (first public version, 2026-10-04), Section 7.2, https://arxiv.org/abs/2610.05438.
2. *Exact diameter of the geodesic Zare monotiles*, published mathematical research record, https://github.com/published-finding corpus/2026 (public record identifier f5389af65e93).
3. O. Martinez, *An Efficient Algorithm to Calculate the Center of the Biggest Inscribed Circle in an Irregular Polygon*, arXiv:1212.3193 (2012), https://arxiv.org/abs/1212.3193.
