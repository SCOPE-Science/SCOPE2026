# Eight Cayley cubic components of the octahedral intersection-body boundary

## Finding
The eight signed cubic components of the intersection-body boundary of the standard octahedron are all projectively equivalent to the Cayley cubic. In the original affine coordinates their nodes are explicit: for component \(s\) they are \(0,2s_1e_1,2s_2e_2,2s_3e_3\), with no further singularities at infinity. The origin is in the real Zariski closure but is not a point of the Euclidean boundary.

For the section-area and component equations used in this classification, let \(O=\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le1\}\). For \(v\ne0\), write \(a=|v_1|\), \(b=|v_2|\), and \(c=|v_3|\). With \(\rho_{IO}(v)=\operatorname{area}(O\cap v^\perp)/\|v\|_2\), the radial function is
\[
\rho_{IO}(v)=\frac{2(ab+ac+bc)}{(a+b)(a+c)(b+c)}
\]
when at least two magnitudes are positive, and \(2/|v_i|\) when only \(v_i\ne0\).

For \(s\in\{\pm1\}^3\), set \((a_s,b_s,c_s)=(s_1x_1,s_2x_2,s_3x_3)\), and let
\[
F_s(x)=(a_s+b_s)(a_s+c_s)(b_s+c_s)-2(a_sb_s+a_sc_s+b_sc_s).
\]
The real algebraic boundary is exactly \(\bigcup_s\mathcal V_{\mathbb R}(F_s)\). These eight distinct irreducible cubics have total degree 24, with no planar components.

## Assumptions and scope
All section areas are two-dimensional Euclidean areas. For unit \(v\) the radial function equals the section area, and the extension to general \(v\ne0\) is homogeneous of degree \(-1\). The real algebraic boundary is the real Zariski closure of the topological boundary in affine \(\mathbb R^3\).

## Proof
**Section area.** By reflection it suffices first to take \(v=(a,b,c)\) with all three coordinates positive. A central section crosses precisely the edges joining vertices of opposite signs with distinct coordinate axes. In cyclic order the six section vertices are \(u,w,z,-u,-w,-z\), where
\[
u=\frac{(b,-a,0)}{a+b},\qquad
w=\frac{(c,0,-a)}{a+c},\qquad
z=\frac{(0,c,-b)}{b+c}.
\]
Indeed each consecutive pair shares a triangular face of the octahedron. Triangulating at the origin, the area is the norm of \(u\times w+w\times z+z\times(-u)\): opposite triangles have equal areas, cancelling the factor \(1/2\), and the three cross products are positive multiples of \(v\). Dividing by \(\|v\|_2\) gives
\[
\frac{a}{(a+b)(a+c)}+\frac{c}{(a+c)(b+c)}+\frac{b}{(b+c)(a+b)}
=\frac{2(ab+ac+bc)}{(a+b)(a+c)(b+c)}.
\]
Section area is continuous in the direction: after a continuously chosen local rotation of the section plane, its area is the circle integral of \(\tfrac12\|u\|_1^{-2}\), with \(u\) the rotated unit vector in that plane. Thus the expression also holds when just one coordinate is zero. On a coordinate axis the section is the coordinate diamond of area 2, giving the stated axial value.

**Boundary patches.** In the open signed octant \(s_ix_i>0\) the boundary condition is \(\rho_{IO}(x)=1\), equivalent to \(F_s(x)=0\) since the denominator is positive. The diagonal restriction is \(F_s(rs_1,rs_2,rs_3)=2r^2(4r-3)\), so the point with signed coordinates \((3/4,3/4,3/4)\) is a smooth point of this patch. The radial boundary is continuous, so all coordinate-plane and axis boundary points are limits of open-octant patches and lie in the indicated finite algebraic union.

**Cayley form and singularities.** Homogenize \(F_s\) in the variable \(t\). Write \((a,b,c)=(a_s,b_s,c_s)\) and use the invertible change
\[
q_0=t-(a+b+c)/2,\quad q_1=a/2,\quad q_2=b/2,\quad q_3=c/2.
\]
The homogenized polynomial is \(-8\sum_{i<j<k}q_iq_jq_k\). For the latter elementary symmetric cubic the derivative at index \(i\) is \(q_i^2-Sq_i+E_2\), where \(S=\sum q_i\) and \(E_2=\sum_{i<j}q_iq_j\). Thus at a projective singularity there are at most two different coordinates. Four equal coordinates cannot give a nonzero singular vector. With multiplicities 1 and 3 and values \(u,v\), the root sum implies \(u+v=u+3v\), so \(v=0\). With multiplicities 2 and 2, the sum implies \(u+v=0\), and the root product then requires \(-u^2=-2u^2\), impossible for nonzero \(u\). The only singularities are therefore the four coordinate points. At each, the quadratic part in the chart with the nonzero coordinate set to 1 is \(xy+xz+yz\), nondegenerate. The inverse change puts all four nodes in the affine chart \(t=1\), at the listed points. A reducible projective cubic would have a positive-dimensional singular locus: two positive-degree surface factors intersect in at least a curve, or a repeated factor is singular along its surface. Thus the cubic is absolutely irreducible.

**Distinctness and closure.** In the cubic part the coefficient of \(x_i^2x_j\) for \(i\ne j\) is \(s_j\), so proportionality forces all signs to change by the same factor, either \(1\) or \(-1\). The quadratic part is unchanged under simultaneous sign reversal and nonzero, ruling out \(-1\). Each smooth real octant patch is Zariski dense in its absolutely irreducible cubic, since no proper algebraic subset can contain a relatively open two-dimensional patch of smooth points. Thus the inclusion established above is equality, and the degree of the reduced product is \(8\cdot3=24\).

## Verification and limits
The polygon calculation gives every direction, not a finite sample. The accompanying `check.py` tests the same radial expression with edge-plane intersections and tests the exact Cayley change, distinctness and the nodes. The claim is for this particular three-dimensional octahedron, not arbitrary polytopes or dimensions.

## Relation to earlier work
The algebraic-boundary framework for general polytope intersection bodies is due to Berlow, Brandenburg, Meroni and Shankar. Their explicit three-cube example has six planes and eight cubics. In the octahedral case, the radial formula is a three-dimensional evaluation of the known cross-polytope section integral (see Brazitikos–Pandis, Eq. (2.3), and their references to Meyer–Pajor and Koldobsky). The general cross-polytope boundary calculation cited below explicitly notes the dimension-three specialization \(P_3=e_2\), yielding the same eight signed cubic equations. We do not claim the radial identity, component count or degree as new here. The contribution is the Cayley normal form and the singularity classification of each of those real algebraic boundary components in the original coordinates.

## References
1. K. Berlow, M.-C. Brandenburg, C. Meroni and I. Shankar, *Intersection Bodies of Polytopes*, arXiv:2110.05996, DOI 10.1007/s13366-022-00621-7, especially Section 5 and Example 5.3.
2. M.-C. Brandenburg and C. Meroni, *Intersection bodies of polytopes: translations and convexity*, arXiv:2302.11764, DOI 10.1007/s10801-024-01328-9.
3. Brazitikos and Pandis, *Restricted Hyperplane Sections of the Cross-Polytope and the Simplex*, arXiv:2606.07163, §2.1, Eq. (2.3).
4. [*Exact algebraic-boundary degrees for intersection bodies of cross-polytopes*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-algebraic-boundary-degrees-for-intersection-bodies-of-cros--27eb6be26fa6), Finding and dimension-three remark.
