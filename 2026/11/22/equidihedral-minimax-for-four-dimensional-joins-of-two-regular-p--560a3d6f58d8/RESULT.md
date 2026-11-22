# Equidihedral minimax for four-dimensional joins of two regular polygons

## Finding

For integers \(m,n\ge3\), let \(A_m(a)\) and \(B_n(b)\) be centered Euclidean regular \(m\)- and \(n\)-gons, of circumradii \(a,b>0\), lying in orthogonal two-planes of \(\mathbb R^4\). Put
\[P_{m,n}(a,b)=\operatorname{conv}(A_m(a)\cup B_n(b)).\]
Let \(\Theta(P)\) be the largest *interior Euclidean dihedral angle* along any two-dimensional ridge, measured as \(\pi\) minus the angle between the two outward unit normals of incident facets. Then \(P\) has exactly two ridge-angle populations, each appearing at precisely \(mn\) ridges (they can coincide). Among all positive radii, the sharp minimax value is
\[
\boxed{\inf_{a,b>0}\Theta(P_{m,n}(a,b))
=\pi-\arccos\!\left(1-\frac{2\sin^2(\pi/m)\sin^2(\pi/n)}{\sin^2(\pi/m)+\sin^2(\pi/n)}\right).}
\]
The minimizing similarity class is unique, characterized by
\[
\boxed{\frac ab=\frac{\tan(\pi/m)}{\tan(\pi/n)}.}
\]
At precisely this ratio, **all \(2mn\) ridges are equidihedral**. For unit-circumradius joins \(a=b=1\), every ridge has the same dihedral angle exactly when \(m=n\). In particular the recently characterized maximum-volume ten-vertex inscribed four-polytope (the orthogonal join of two regular pentagons) is equidihedral, whereas the corresponding square–pentagon nine-vertex maximum-volume polytope has two distinct ridge-angle classes.

## Assumptions and scope

The polygons are full-dimensional in their respective two-dimensional mutually orthogonal linear subspaces. Their centers are at the common origin, and radius means Euclidean circumradius. Dihedral angles are intrinsic four-dimensional facet/ridge angles; they are **not** spherical angles of arbitrary nonadjacent facet pairs. The polygon boundaries are cyclic simplicial one-spheres, and the boundary of the four-polytope is the combinatorial join of these cycles, so each facet consists of one edge from each polygon.

Write \(u=\pi/m\), \(v=\pi/n\), \(c_m=\cos u\), \(c_n=\cos v\), \(U=1/(a^2c_m^2)\), and \(V=1/(b^2c_n^2)\). Both cosines are strictly positive because \(m,n\ge3\).

## Proof

**Facet normals and all ridges.** Let \(e_i\) be the outward unit normal to the \(i\)-th pentagon-type edge of the regular \(m\)-gon, and \(f_j\) that of the \(j\)-th edge of the \(n\)-gon (with cyclic indices). The common facet supporting equation is
\[
\frac{\langle e_i,x_A\rangle}{a c_m}
+\frac{\langle f_j,x_B\rangle}{b c_n}=1.
\]
Its outward unit normal is \(N_{ij}=(e_i/(a c_m),f_j/(b c_n))/\sqrt{U+V}\). The facets indexed by \((i,j)\) and \((i',j')\) share a ridge exactly if one of their indices agrees and the other differs by one modulo its cycle. Thus there are \(mn\) ridges changing the \(m\)-edge and \(mn\) changing the \(n\)-edge, a total of \(2mn\).

**Two exact angle classes.** Adjacent edge normals in a regular \(m\)-gon have scalar product \(\cos(2\pi/m)\). Consequently the cosines of the angles between outward four-dimensional facet normals at the two ridge types are
\[
C_A=\frac{U\cos(2u)+V}{U+V}
=1-\frac{2U\sin^2u}{U+V},\qquad
C_B=\frac{U+V\cos(2v)}{U+V}
=1-\frac{2V\sin^2v}{U+V}.
\]
The interior ridge angles are \(\theta_A=\pi-\arccos C_A\) and \(\theta_B=\pi-\arccos C_B\). Each has multiplicity exactly \(mn\). No other ridge types exist.

**Sharp minimax.** Let \(t=U/(U+V)\in(0,1)\). The two cosines become
\[C_A(t)=1-2t\sin^2u,\qquad C_B(t)=1-2(1-t)\sin^2v.\]
Since \(\pi-\arccos C\) is strictly increasing in \(C\), minimizing the *larger* interior angle is equivalent to minimizing \(\max\{C_A(t),C_B(t)\}\). The first affine function strictly decreases, the second strictly increases, and they cross exactly once:
\[
t_*\sin^2u=(1-t_*)\sin^2v,\qquad
t_* =\frac{\sin^2v}{\sin^2u+\sin^2v}.
\]
Their common value equals \(1-2\sin^2u\sin^2v/(\sin^2u+\sin^2v)\). This proves the value and uniqueness. The ratio equation \(U/V=t_*/(1-t_*)=\sin^2v/\sin^2u\), together with the definitions of \(U,V\), is equivalent to \(a/b=\tan u/\tan v\).

**Equal circumradii.** For \(a=b\), the equidihedral condition reduces to \(\tan u=\tan v\); because \(u,v\in(0,\pi/3]\) and tangent is strictly increasing, this means \(m=n\). For \(m=n=5\), the unique volume-maximizing ten-vertex four-polytope of Medgyes has unit equal radii, and hence belongs to the equidihedral class. For \(m=4,n=5\), the required ratio is \(\tan(\pi/4)/\tan(\pi/5)\neq1\), so equal radii yield two distinct dihedral angles.

## Verification

A standalone standard-library verifier `verify.py` constructs the adjacent facet normals directly from trigonometric coordinates, counts both ridge families, and compares their dot products with the formulas for several unequal polygon orders and off-optimum radii. It separately tests equality at the prescribed optimal radius ratio and strict deterioration on both sides. The mathematical argument above proves the result for all \(m,n\ge3\); finite numerical checks are supplementary, not a proof of universal quantifiers.

## Relationship to prior work

Medgyes, *The inscribed 4-polytope of maximal volume with ten vertices* (2026), proves global volume optimality and uniquely identifies the orthogonal regular pentagon–pentagon join. His earlier nine-vertex paper identifies the square–pentagon join. Neither article determines the two intrinsic dihedral-angle populations or optimizes the largest angle over the independent polygon radii. Previously studied three-dimensional antiprisms and bipyramids have equidihedral minimax results; they are different polytopes and do not imply the four-dimensional formula. Other work on orthogonal regular-polygon joins studies random normal-cone angles and covering distributions, not the ridge-dihedral minimax.

## Limitations

The optimization varies only the two positive polygon circumradii while keeping each polygon regular, the two planes orthogonal and their centers coincident. It does not minimize largest dihedral angle among **all** four-polytopes with the same number of vertices or combinatorial type. No claim is made that equidihedral geometry maximizes volume when the polygon orders differ. Historical priority remains provisional because broad general treatments of dihedral geometry for polygonal free sums may not be indexed.

## References

Csaba Medgyes, *The inscribed 4-polytope of maximal volume with ten vertices*, arXiv:2611.14674v1, first posted 2026-11-10. https://arxiv.org/html/2611.14674v1

Csaba Medgyes, *The inscribed 4-polytope of maximal volume with nine vertices*, arXiv:2611.10078v1, first posted 2026-11-06. https://arxiv.org/html/2611.10078v1
