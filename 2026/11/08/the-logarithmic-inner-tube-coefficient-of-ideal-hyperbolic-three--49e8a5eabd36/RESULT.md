# The logarithmic inner-tube coefficient of ideal hyperbolic three-polyhedra

## Finding

Let \(P\subset\mathbb H^3\) be a fixed, nondegenerate, finite-sided **convex ideal polyhedron** in curvature \(-1\), with \(v\) vertices at infinity, hyperbolic volume \(V>0\), and interior dihedral angles \(\beta_e\in(0,\pi)\) at its edges \(e\). Let \(D_P\) be the ambient hyperbolic distance from a hyperbolic-volume-uniform point in \(P\) to \(\partial P\). Then, as \(s\downarrow0\),

\[
\Pr(D_P\le s)=\frac{2\pi(v-2)}{V}\,s
 -\frac{2}{V}\left(\sum_{e}\cot\frac{\beta_e}{2}\right)s^2\log(1/s)+O_P(s^2).
\]

In particular, the first departure from the finite-surface-area linear tube law is a **negative logarithmic second-order term**, determined exactly by the dihedral angles. Put \(B(P)=2\sum_e\cot(\beta_e/2)\). This is intrinsic to the ideal polyhedron and strictly positive.

For every ideal tetrahedron, \(B(P)\ge12\sqrt3\), with equality if and only if \(P\) is the regular ideal tetrahedron. Moreover the *normalized* logarithmic coefficient obeys the sharp inequality \(B(P)/V\ge12\sqrt3/v_3\), where
\[
v_3=3\Lambda(\pi/3),\qquad \Lambda(\theta)=-\int_0^\theta\log(2\sin u)\,du,
\]
and equality again characterizes the regular ideal tetrahedron. There the entire formula specializes to
\[
\Pr(D_P\le s)=\frac{4\pi}{v_3}s-\frac{12\sqrt3}{v_3}s^2\log(1/s)+O(s^2).
\]

## Assumptions and scope

A convex ideal polyhedron is the intersection of finitely many geodesic half-spaces in \(\mathbb H^3\), with each polyhedral vertex lying on the ideal boundary and at least four noncoplanar ideal vertices. Its finite-volume interior carries normalized Riemannian volume. Distances are ambient distances in the complete curvature-\(-1\) space, not intrinsic distances along the polyhedral surface. The asymptotic is for each **fixed** polyhedron; no uniform error is claimed as its dihedral angles degenerate. The symbol \(v\) counts ideal vertices (not hyperbolic volume). Each \(\beta_e\) is the interior angle, not its supplement.

## Proof

**1. Local cusp geometry.** Fix an ideal vertex \(q\). Move it to infinity in the upper-half-space model, with metric \(ds^2=(dx^2+dy^2+dz^2)/z^2\) and volume element \(dx\,dy\,dz/z^3\). For sufficiently large fixed \(z_0>0\), the portion of \(P\) above the horosphere \(z=z_0\) is \(Q\times[z_0,\infty)\), for a bounded convex Euclidean polygon \(Q\subset\mathbb R^2\). Precisely the faces incident to \(q\) are vertical above this horosphere; all other supporting planes are separated from this cusp. The interior angles \(\theta_j\) of \(Q\) are the interior hyperbolic dihedral angles of edges incident to \(q\).

For \((x,z)\) in the cusp, the hyperbolic distance to a vertical supporting face with Euclidean horizontal supporting line \(\ell\) is
\[
\operatorname{arsinh}\!\left(\frac{\operatorname{dist}_{\mathbb R^2}(x,\ell)}{z}\right).
\]
This follows by reducing to the perpendicular two-dimensional upper-half-plane cross section and minimizing the hyperbolic distance to its vertical geodesic. Since \(P\) is the intersection of the face half-spaces, its distance to its boundary is the minimum of the distances to the supporting planes. For sufficiently small \(s>0\), nonincident planes cannot be nearer than \(s\) in the chosen cusp. Thus the subset at distance greater than \(s\) from \(\partial P\) has horizontal section \(Q_{-z\sinh s}\), the Euclidean inward parallel polygon at offset \(z\sinh s\), with \(Q_{-t}=\{x\in Q:\operatorname{dist}(x,\partial Q)>t\}\).

**2. Exact planar input.** Write \(A=\operatorname{area}(Q)\), \(L=\operatorname{perimeter}(Q)\), and
\[
C(Q)=\sum_{j}\cot(\theta_j/2).
\]
There exists \(\eta>0\), depending on \(Q\), such that for \(0\le t\le\eta\),
\[
A-\operatorname{area}(Q_{-t})=Lt-C(Q)t^2.
\]
Indeed, the inward-offset side lengths vary linearly until the first side disappears, and the lost strip area is the sum of widths times the original side lengths minus the corner-overlap triangles. At a vertex with angle \(\theta_j\), that corner correction is \(t^2\cot(\theta_j/2)\). Equivalently, differentiate the area of the offset polygon using its linearly varying perimeter. This proves the displayed polynomial directly, without requiring a general tube theorem.

**3. Integration produces the logarithm.** Set \(h=\sinh s\). The cusp's boundary-layer volume is exactly
\[
I_q(s)=\int_{z_0}^{\infty}z^{-3}\bigl[A-\operatorname{area}(Q_{-zh})\bigr]\,dz.
\]
For \(s\) small enough that \(z_0h<\eta\), split the integral at \(z=\eta/h\). The portion above that height is \(O_Q(h^2)\), because the bracket lies between zero and \(A\). On the lower portion the exact planar polynomial yields
\[
\begin{aligned}
I_q(s)&=\int_{z_0}^{\eta/h}(Lhz^{-2}-C(Q)h^2z^{-1})\,dz+O_Q(h^2)\\
&=\frac L{z_0}h-C(Q)h^2\log(1/h)+O_{Q,z_0}(h^2)\\
&=\frac L{z_0}s-C(Q)s^2\log(1/s)+O_{Q,z_0}(s^2).
\end{aligned}
\]
The finite area of the original faces *inside this cusp* is exactly \(L/z_0\), since each vertical polygon edge contributes its Euclidean length times \(\int_{z_0}^\infty z^{-2}dz\). No choice of horosphere affects the logarithmic coefficient \(C(Q)\), which depends only on its angles.

**4. Compact remainder.** Choose disjoint sufficiently deep horoball cusps about every ideal vertex and remove their interiors. The remaining truncated part is compact. Its boundary consists of finitely many totally geodesic face patches meeting along finite-length edges, plus artificial horospherical cuts. For the distance to the *actual* polyhedron boundary, ordinary normal coordinates on the relative interiors of the compact face patches give their area times \(s+O(s^3)\). The portions within distance \(O(s)\) of their finite edge intersections and of the artificial cuts have volume \(O_P(s^2)\); near cuts these estimates follow in bounded smooth local charts. The compact contribution is therefore the area of its original face portions times \(s+O_P(s^2)\). Adding the cusp formulas proves
\[
\operatorname{Vol}\{x\in P:d(x,\partial P)\le s\}
 =\operatorname{Area}(\partial P)s
 -\Bigl(\sum_{q\text{ ideal vertex}}C(Q_q)\Bigr)s^2\log(1/s)+O_P(s^2).
\]
Each polyhedral edge has exactly two ideal endpoints, and the horospherical polygon angle at either endpoint is \(\beta_e\); hence \(\sum_qC(Q_q)=2\sum_e\cot(\beta_e/2)=B(P)\).

Every face is an ideal hyperbolic polygon with \(m_f\) vertices and area \((m_f-2)\pi\). The total edge incidence count is \(\sum_fm_f=2E\). Euler's formula \(v-E+F=2\) then gives
\[
\operatorname{Area}(\partial P)=\pi(2E-2F)=2\pi(v-2).
\]
Dividing by the finite hyperbolic volume \(V\) gives the probability formula.

**5. Tetrahedral sharpness.** For an ideal tetrahedron, the opposite dihedral angles agree in pairs, and its three distinct values \(\alpha,\beta,\gamma\in(0,\pi)\) satisfy \(\alpha+\beta+\gamma=\pi\). Thus
\[
B(P)=4\bigl[\cot(\alpha/2)+\cot(\beta/2)+\cot(\gamma/2)\bigr].
\]
Since \(x\mapsto\cot(x/2)\) is strictly convex on \((0,\pi)\), Jensen's inequality yields \(B(P)\ge12\sqrt3\), with equality only at \(\alpha=\beta=\gamma=\pi/3\), the regular ideal tetrahedron.

For completeness, the classical ideal tetrahedron volume formula is \(V=\Lambda(\alpha)+\Lambda(\beta)+\Lambda(\gamma)\). With \(\gamma=\pi-\alpha-\beta\), the Hessian in \((\alpha,\beta)\) has diagonal entries \(-\sin\beta/(\sin\alpha\sin\gamma)\), \(-\sin\alpha/(\sin\beta\sin\gamma)\) and determinant \(1\), so is negative definite. The unique symmetric maximum is therefore \(v_3=3\Lambda(\pi/3)\). Combining \(B(P)\ge12\sqrt3\) and \(V\le v_3\) proves the sharp normalized inequality, with equality only in the regular case.

## Verification

The accompanying `check_cusp_tube.py` uses independent Euclidean half-plane clipping to compute inward erosions of an equilateral triangle and square, followed by numerical integration of the actual hyperbolic cusp volume. It compares these values with the two-term exact cusp integration and tests dihedral-angle Jensen bounds. This verifies signs, powers, normalizations, and the factor-two edge-incidence coefficient on two elementary ideal cusp types. The calculations are finite checks; the uniform \(O_P(s^2)\) statement follows from the geometric argument above, not from the checker.

## Relationship to prior work

Koçak and Ratiu derive piecewise-polynomial **Euclidean** inner tube formulas for compact polytopes, including the two-dimensional polygon angle coefficient used here. Their Euclidean setting does not include ideal hyperbolic cusps or produce the \(s^2\log(1/s)\) divergence. Leibon discusses Euclidean horospherical vertex figures, ideal-polyhedron dihedral angles, and Schläfli volume variation, but not volume collars about ideal-polyhedron boundaries. Calegari's Kleinian-group notes derive the ideal tetrahedron volume function; that earlier formula is used solely for the sharp normalized extremal corollary. The present boundary-distance law is not an angle-variation formula for volume.

## Limitations

The theorem is restricted to convex finite-sided ideal hyperbolic three-polyhedra with all vertices ideal. Compact or hyperideal vertices, dimensions other than three, nonconvex regions, and degenerating families are outside the claim. Constants in \(O_P(s^2)\) need not be uniform. No exact distribution away from the small-distance regime is asserted. Historical priority of the full logarithmic inner-tube coefficient remains provisional; especially older treatments of hyperbolic inner parallel bodies may use alternative terminology.

## References

1. G. Leibon, *Characterizing the Delaunay decompositions of compact hyperbolic surfaces*, Geometry & Topology **6** (2002), 361–391 (arXiv first public 2001-03-26, journal published 2002-07-13). https://www2.math.ethz.ch/EMIS/journals/UW/gt/ftp/main/2002/2002s12.pdf (especially horospherical Euclidean polygons and ideal tetrahedron dihedral angles, pp. 371, 377–378).
2. Ş. Koçak and A. V. Ratiu, *Inner tube formulas for polytopes*, arXiv:1008.2040, version 1 first public 2010-08-12; Proc. Amer. Math. Soc. **140** (2012), 999–1010. https://arxiv.org/abs/1008.2040 .
3. D. Calegari, *Notes on Kleinian Groups*, notes dated 2015-05-21, Section 3.3, Proposition 3.7 (ideal tetrahedron volume). https://doczz.net/doc/6805293/here---university-of-chicago .
4. R. Roeder, J. Hubbard and W. Dunbar, *Andreev’s Theorem on hyperbolic polyhedra*, Ann. Inst. Fourier **57** (2007), 825–882 (MSC 51M10). https://www.numdam.org/item/AIF_2007__57_3_825_0/ .
