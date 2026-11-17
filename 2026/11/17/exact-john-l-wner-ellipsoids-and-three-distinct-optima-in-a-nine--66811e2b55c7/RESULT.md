# Exact John–Löwner ellipsoids and three distinct optima in a nine-vertex spherical prism family

## Finding

For every real \(r\) with \(1/2<r<1\), put \(h=\sqrt{1-r^2}\) and define the spherical nine-vertex convex polytope
\[
P_r=\operatorname{conv}\left(\{a_j:0\le j<3\}\cup\{b_j^+,b_j^-:0\le j<3\}\right),
\]
where
\[
a_j=(\cos(2\pi j/3),\sin(2\pi j/3),0),\qquad
b_j^\pm=(r\cos(\pi/3+2\pi j/3),r\sin(\pi/3+2\pi j/3),\pm h).
\]
These are symmetric triaugmented triangular prisms, including the unique nine-vertex sphere-inscribed volume maximizer identified in [1]. All ellipsoids and volumes below use the standard Euclidean metric in \(\mathbb R^3\).

**Exact extremal ellipsoids.** The unique maximum-volume ellipsoid contained in \(P_r\) (John ellipsoid) is
\[
J_r=\left\{(x,y,z):\frac{x^2+y^2}{A(r)}+\frac{z^2}{h^2}\le1\right\},\qquad
A(r)=\frac{3r^2}{4(1-r+r^2)}.
\]
It touches precisely eight of the fourteen facet planes: the two horizontal triangles and six vertical triangles. The six remaining (sloping) facet planes are strictly separated from it for every \(1/2<r<1\).

The unique minimum-volume ellipsoid containing \(P_r\) (Löwner ellipsoid) has the equation
\[
L_r=\left\{(x,y,z):\frac{x^2+y^2}{C(r)}+\frac{z^2}{D(r)}\le1\right\},
\]
where
\[
(C(r),D(r))=
\begin{cases}
(1,1),&1/2<r\le\sqrt{2/3},\\
(3r^2/2,\,3(1-r^2)),&\sqrt{2/3}<r<1.
\end{cases}
\]
At the sharp contact transition \(r=\sqrt{2/3}\), all nine vertices touch the unit Löwner sphere. Below it all nine vertices touch; above it precisely the six prism-ring vertices touch, while the three equatorial augmenting vertices lie strictly inside.

**Sharp distortion and incompatible optimizers.** The ratio of outer to inner ellipsoid volumes is
\[
Q(r):=\frac{\operatorname{vol}_3(L_r)}{\operatorname{vol}_3(J_r)}=
\begin{cases}
\displaystyle\frac{4(1-r+r^2)}{3r^2\sqrt{1-r^2}},&1/2<r\le\sqrt{2/3},\\
2\sqrt3(1-r+r^2),&\sqrt{2/3}\le r<1.
\end{cases}
\]
It has a unique global minimum \(Q(r_J)=2.900134231069\ldots\) at the unique root \(r_J\in(77/100,39/50)\) of
\[
r^4-2r^3+3r^2+r-2=0,
\qquad r_J=0.773295293450\ldots.
\]
The Euclidean inradius of \(P_r\) is
\[
\rho(r)=\min\left\{\sqrt{1-r^2},\,\frac{\sqrt3\,r}{2\sqrt{1-r+r^2}}\right\}.
\]
It has a unique global maximum at the root \(r_I=0.717869821226\ldots\) in \((71/100,18/25)\) of
\[
4r^4-4r^3+3r^2+4r-4=0.
\]
The previously known ordinary-polytope-volume maximizer [1] occurs at \(r_V=\sqrt3-1=0.732050807569\ldots\). Thus the three geometrically natural extremizers are strictly different:
\[
\boxed{r_I<r_V<r_J<\sqrt{2/3}.}
\]
The polytope-volume extremum \(r_V\) is explicitly credited to [1], not asserted here as new.

## Assumptions and scope

The family uses *all* \(r\in(1/2,1)\), not merely the sphere-inscribed volume-optimal parameter. The lower bound \(1/2\) is the nondegenerate combinatorial chamber where there are fourteen triangular facets of triaugmented-prism type; at \(r=1/2\) four supporting vertices become coplanar, and below it the face incidence changes. No assertions are made for nonsymmetric nine-vertex polytopes, or for optimizing ellipsoid distortion over all point configurations on the sphere. Ellipsoid uniqueness is the classical John–Löwner theorem. A facet-plane contact here means that the ellipsoid's boundary meets that supporting facet, not merely its infinite extension.

## Proof

**1. The fourteen facet inequalities.** For \(j=0,1,2\), write \(u_j=(\cos(2\pi j/3),\sin(2\pi j/3))\) and let \(v_j\) be its counterclockwise quarter-turn. Besides \(\pm z\le h\), for each \(j\) and sign \(\sigma\in\{-1,1\}\) the supporting inequalities are
\[
\frac{\sqrt3r}{2}\,u_j\cdot(x,y)
+\sigma\left(1-\frac r2\right)v_j\cdot(x,y)
\le\frac{\sqrt3r}{2},\tag{1}
\]
and
\[
h\,u_j\cdot(x,y)+\sigma\left(1-\frac r2\right)z\le h.\tag{2}
\]
The first six are vertical; the second six slope outward from an augmenting apex. Direct substitution of the nine displayed vertices shows that each is supporting and has exactly three affinely independent vertex contacts when \(r>1/2\). For (1) the decisive nonincident augmenting-vertex inequality reduces to \(1-r<r\); all others are strict except its stated three contacts. The horizontal facets each contain three ring vertices. Thus we exhibit fourteen distinct triangular facets. A three-dimensional polytope with nine vertices has at most \(2\cdot9-4=14\) facets, proving that this list is complete.

**2. Symmetry reduction.** Both extremal ellipsoids exist uniquely for every full-dimensional convex body [2,3]. Every symmetry of \(P_r\) preserves each of them. The threefold rotation about the vertical axis forces the horizontal covariance block of each ellipsoid to be a scalar matrix and its horizontal center to vanish. Reflection across \(z=0\) forces its remaining center coordinate and cross terms to vanish. Therefore each extremal ellipsoid is necessarily centered at zero and has two equal horizontal semiaxes \(a>0\) and one vertical semiaxis \(b>0\).

**3. John's ellipsoid.** In a centered spheroid with squared horizontal semiaxis \(s=a^2\) and vertical semiaxis \(b\), the top and bottom facets require \(b\le h\). The norm of the horizontal normal in (1) is \(\sqrt{1-r+r^2}\), so the six vertical facets require
\[
s\le A(r)=\frac{3r^2}{4(1-r+r^2)}.
\]
Consequently \(\operatorname{vol}(E)\le (4\pi/3)A(r)h\). For the spheroid \(s=A(r),b=h\), the left side support of each slope (2) is \(\sqrt{h^2A(r)+(1-r/2)^2h^2}\). It lies strictly below \(h\), since the exact identity
\[
1-\left(1-\frac r2\right)^2-A(r)
=\frac{r(2-r)^2(1-r)}{4(1-r+r^2)}>0
\]
holds throughout the specified open parameter interval. Thus this upper bound is feasible and attained; uniqueness identifies \(J_r\). Equality at precisely the two horizontal and six vertical facet planes, and strictness at the six sloping facets, follows from the same inequalities.

**4. Löwner's ellipsoid.** A centered spheroid with squared horizontal semiaxis \(s\) and squared vertical semiaxis \(t\) contains all nine vertices if and only if
\[
s\ge1,\qquad \frac{r^2}{s}+\frac{h^2}{t}\le1.
\]
For fixed \(s\) the smallest permissible \(t\) is \(h^2s/(s-r^2)\). Minimizing its volume is therefore equivalent to minimizing
\[
h\,\frac{s^{3/2}}{\sqrt{s-r^2}}\quad(s\ge1).
\]
The logarithmic derivative is \((2s-3r^2)/(2s(s-r^2))\). Its unique minimum on \([1,\infty)\) lies at \(s=1\) if \(3r^2\le2\), and otherwise at \(s=3r^2/2\). Substitution gives the two stated ellipsoids and the contact classification. At equality \(3r^2=2\), every vertex remains on the sphere; if \(3r^2>2\), the three \(a_j\) satisfy \(1/C(r)<1\) while each \(b_j^\pm\) lies on the ellipsoid.

**5. Sharp ratio and three optimizers.** Ellipsoid volumes are \((4\pi/3)a^2b\), yielding the displayed \(Q(r)\) after cancellation. On the first branch its reciprocal is
\[
A(r)h=\frac{3r^2\sqrt{1-r^2}}{4(1-r+r^2)}.
\]
The sign of its derivative is opposite to the sign of \(H(r)=r^4-2r^3+3r^2+r-2\). Indeed
\[
\frac{d}{dr}\log(A(r)h)
=\frac{H(r)}{r(r-1)(r+1)(r^2-r+1)}.
\]
Since \(H'(r)=4r^3+6r(1-r)+1>0\) on \((0,1)\), \(H\) has exactly one zero there. The rational sign checks at \(77/100\) and \(39/50\) isolate the zero strictly below \(\sqrt{2/3}\). On the second branch \(Q'(r)=2\sqrt3(2r-1)>0\). These observations give the asserted unique global minimum.

To obtain \(\rho(r)\), average a maximal inscribed-ball center over the finite symmetry group; this gives the origin as an admissible maximal center. Its radius is the minimum distance to the fourteen facet planes. The three distances are \(h\), \(\sqrt{A(r)}\), and
\[
\frac{h}{\sqrt{h^2+(1-r/2)^2}}.
\]
For \(r\ge2/3\) the last is at least \(h\). For \(1/2<r\le2/3\) it is at least \(\sqrt{A(r)}\), as the difference of their squares is
\[
\frac{(2-r)^2(4-7r^2)}{4(1-r+r^2)(8-4r-3r^2)}>0.
\]
Hence it never determines the inradius. The function \(h\) decreases strictly in \(r\), whereas \(A(r)\) increases strictly, with \(A'(r)=3r(2-r)/(4(1-r+r^2)^2)>0\). Their square roots cross once; clearing denominators gives the stated quartic and the rational isolating interval. The exact source value \(r_V=\sqrt3-1\) lies between the disjoint isolating intervals for \(r_I\) and \(r_J\), establishing the strict ordering.

## Verification

Run the included standalone, standard-library-only `verify.py` with `python3 verify.py`. In the packaged state it completed 18,199 deterministic numerical and rational-sign assertions. The verifier reconstructs all nine vertices and fourteen supporting triangles for 312 parameter values, checks every support incidence and the containment/contact constraints of both ellipsoids, and tests the quartic root brackets and distortion-minimizer inequalities. Numerical checks do not prove the continuum statements; the preceding exact algebra, symmetry argument and elementary one-variable minimizations supply those proofs.

## Relationship to prior work

Hoehner and Ledford [1] determined the unique maximal-volume inscribed nine-vertex polyhedron and its vertex coordinates, including the parameter \(r_V\). Their volume result is the input motivating this family, not a consequence advertised as new. Their full manuscript studies volume inequalities and type reduction, not explicit John or Löwner ellipsoids or the sharp ellipsoid-volume ratio. Classical extremal-ellipsoid existence, uniqueness and symmetry inheritance [2,3] reduce the new computation to two semiaxes; they do not themselves determine the fourteen active constraints, the contact phase transition or the root of the distortion-minimization polynomial. The equilateral Johnson solid [4] is one particular, differently normalized geometry; its listed edge/area/volume data do not give this spherical one-parameter ellipsoid profile. Other recent calculations for two-ring polygonal prismatoids address a different vertex/facet configuration, not the three-equatorial-apex, nine-vertex family.

## Limitations

This is an exact result within the full open one-parameter symmetric triaugmented-prism chamber, not an inequality for arbitrary nonsymmetric nine-vertex polyhedra. The contact count at the combinatorial endpoint \(r=1/2\) is intentionally excluded. The numerical decimals are approximations to the precisely specified algebraic quantities. No claim of independent validation is made. Historical novelty is assessed against the identified, inspected literature and mathematical records; an unindexed equivalent old calculation remains possible.

## References

[1] S. Hoehner and J. Ledford, *The maximum volume polytope with nine vertices inscribed in the sphere*, arXiv:2608.04392, v1 publicly posted 2026-08-05; v2 2026-11-06. https://arxiv.org/abs/2608.04392

[2] F. John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant on his 60th Birthday*, 1948, pp. 187–204 (classical extremal-ellipsoid theorem).

[3] E. W. Weisstein, *Löwner Ellipsoid*, MathWorld, on existence, uniqueness and contact characterizations. https://mathworld.wolfram.com/LoewnerEllipsoid.html

[4] E. W. Weisstein, *Triaugmented Triangular Prism*, MathWorld (Johnson solid J51, classical geometry). https://mathworld.wolfram.com/TriaugmentedTriangularPrism.html
