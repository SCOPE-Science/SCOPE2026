# Exact facet-jump spectrum of intrinsic distances on flat three-tori

## Finding
Let \(\Lambda\subset\mathbb R^3\) be any full-rank Euclidean lattice, \(T=\mathbb R^3/\Lambda\) its flat Riemannian torus, and \(X,Y\) independent Haar-uniform points of \(T\). Put \(F(r)=\Pr(d_T(X,Y)\le r)\), \(V=\operatorname{covol}(\Lambda)\), and let \(\mathcal R(\Lambda)\) be the finite set of *oriented* Voronoi-relevant lattice vectors: those nonzero \(v\) for which the perpendicular bisector of \(0\) and \(v\) contains a two-dimensional facet of the Voronoi cell of \(\Lambda\). For \(r>0\) define \(m(r)=\#\{v\in\mathcal R(\Lambda):\|v\|=2r\}\).

The function \(F\) is continuously differentiable on \((0,\infty)\). Its second derivative exists away from finitely many radii, has finite one-sided limits at every positive radius, and obeys the **exact jump formula**
\[
\boxed{F''(r+)-F''(r-)=-\frac{2\pi r}{V}\,m(r)\qquad(r>0).}
\]
In particular **no edge, vertex, or simultaneous cap-intersection event creates a spurious jump**. The distance distribution recovers \(V\) from
\[
\boxed{V=\lim_{t\downarrow0}\frac{4\pi t^3}{3F(t)}}
\]
and then recovers the complete multiset \(\{\|v\|:v\in\mathcal R(\Lambda)\}\), including multiplicity, from its negative second-derivative jumps. The sum of the recovered multiplicities is the number of Voronoi facets. No claim of reconstruction of the entire lattice from that multiset is made.

## Assumptions and scope
All lattices have full rank three, with the Euclidean quotient metric and uniform volume measure. Vectors \(v\) and \(-v\) count separately, matching the opposite facets. No genericity or distinct-critical-radius condition is imposed; coalescence of facet, edge, and vertex critical radii is permitted. The derivatives in the jump formula are one-sided limits of \(F''\) at nearby differentiability points, not assumptions that the second derivative exists at the jump itself. There are finitely many exceptional radii because the Voronoi cell has finitely many facets and its spherical boundary arrangement changes combinatorial type at only finitely many algebraic contact values.

## Proof
**1. Distribution as radial volume.** The difference \(X-Y\) is Haar-uniform on \(T\). Its unique nearest-lattice representative away from a null set lies uniformly in the Euclidean Voronoi cell
\[
C=\{x\in\mathbb R^3:\|x\|\le\|x-v\|\text{ for all }v\in\Lambda\}.
\]
Consequently \(F(r)=V^{-1}\operatorname{vol}_3(C\cap B_r)\). In particular, if \(r\) is below the lattice injectivity radius, \(F(r)=4\pi r^3/(3V)\); this proves the stated recovery of \(V\).

**2. Every facet has a strictly interior radial foot.** If a facet of \(C\) corresponds to \(v\in\Lambda\), then its supporting plane has equation \(x\cdot v=\|v\|^2/2\) and its distance to the origin is \(a_v=\|v\|/2\). The facet is \(C\cap(C+v)\). Because \(C=-C\), reflection \(x\mapsto v-x\) preserves this intersection. Thus this full-dimensional convex facet is centrally symmetric about \(v/2\); its center belongs to its relative interior. Hence the radial direction \(u_v=v/\|v\|\) belongs to the interior, as a spherical point, of the angular domain cut off *only* by this facet at its birth radius.

**3. Angular cap formula.** Choose one defining inequality for each facet, indexed by all oriented relevant vectors. For \(r>a_v\) let
\[
K_v(r)=\{u\in S^2:u\cdot u_v>a_v/r\},
\]
and let \(K_v(r)=\varnothing\) for \(r\le a_v\). The part of the Euclidean sphere of radius \(r\) lying in \(C\) consists exactly of directions outside \(\bigcup_vK_v(r)\). Writing \(U(r)\) for the usual unit-sphere area of this union gives
\[
F'(r)=\frac{r^2}{V}\,[4\pi-U(r)]. \tag{1}
\]
This also proves that \(F'\) is continuous. Each individual cap has spherical area
\[
\operatorname{area}(K_v(r))=2\pi(1-a_v/r)\quad(r>a_v). \tag{2}
\]

**4. Continuity of the union-area derivative away from cap births.** Fix an interval avoiding all \(a_v\). Each moving cap boundary is a genuine small circle on \(S^2\), with smooth radius and nonzero finite angular speed. Distinct facet planes give distinct circles; their pairwise intersections are finite unless empty. The first variation of the union area is the sum, over each boundary circle, of the outward angular speed integrated along the *exposed* arcs (arcs not covered by another cap). To verify continuity at any parameter \(r_0\) in the interval, parametrise each circle smoothly. For all but finitely many parameter angles, the exposure indicator converges as \(r\to r_0\); the exceptional angles are precisely pairwise boundary intersections. Circle length elements and angular speeds converge uniformly. Dominated convergence therefore shows the exposed-length integral, and hence \(U'(r)\), is continuous at \(r_0\), including tangencies and triple intersections. The same argument gives the one-sided derivative of \(U\) at every such parameter. This is why edge/vertex transitions contribute no jump to \(F''\).

**5. Cap births give all jumps.** At any threshold \(a>0\), each new cap has center \(u_v\) corresponding to the relative-interior foot \(v/2\). Finiteness of the facet set and Step 2 ensure that all new caps are, for a sufficiently small right-hand interval, disjoint from the previously present caps and from one another. They contribute additively to \(U\), with right derivative \(2\pi/a\) each by (2), and zero left derivative. All previously active caps contribute continuously by Step 4. Hence
\[
U'(a+)-U'(a-)=\frac{2\pi}{a}m(a).
\]
Differentiating (1) on either side, the continuous terms cancel, giving \(F''(a+)-F''(a-)=-2\pi a\,m(a)/V\). Away from these thresholds Step 4 gives zero jump. This proves all assertions.

## Verification
A standalone script `check.py` evaluates the exact ball-cap formula on an orthogonal three-torus with side lengths \(1,1.6,2.7\), checks both predicted second-derivative jumps at radii \(0.5\) and \(0.8\) by convergent difference quotients, and compares five exact CDF values with \(2^{20}\) scrambled Sobol samples of uniform torus differences. It outputs `TORUS_FACET_CHECK_OK` when its independently computed inequalities pass. For the first two facets, the predicted jumps are approximately \(-1.4544410433\) and \(-2.3271056693\), respectively. The proof is analytical; the checker is only a reproducibility and normalization aid.

## Relationship to prior work
Classical Voronoi theory and Voigt–Weis (arXiv:1003.4173, 2010) supply the halfspace viewpoint; Blömer–Kohn (arXiv:1512.00720, publicly available 2015) establish general correspondences between relevant vectors and Voronoi facets. Neither source gives a radial geodesic-distance distribution or a second-derivative jump law. Distance-distribution inverse problems are studied by Mémoli–Needham (arXiv:1810.09646, 2018); the present assertion is the explicit three-dimensional facet-jump identity without genericity assumptions, not a claim of global metric rigidity. The planar square-root facet signature has different differentiability and does not directly imply the three-dimensional, all-degeneracy result. This comparison is subject to the literature access limits noted below.

## Limitations
The recovered facet-length multiset need not by itself determine the isometry class of the torus; no such injectivity statement is proved. The theorem concerns population distance distributions, not statistically stable recovery from finitely many samples. The proof uses the Euclidean quotient metric and does not cover arbitrary Finsler metrics or nonflat Riemannian manifolds. Full-text historical comparison of every potential distance-histogram source was not possible; originality remains a best-knowledge assessment, not an independently certified priority determination.

## References
- I. Voigt and S. Weis, *Polyhedral Voronoi Cells*, arXiv:1003.4173v1 (first public version 2010-03-22), Beitr. Algebra Geom. 51 (2010), 587–598.
- J. Blömer and K. Kohn, *Voronoi Cells of Lattices with Respect to Arbitrary Norms*, arXiv:1512.00720v1 (first public version 2015-11-27), SIAM J. Appl. Algebra Geom. 2 (2018), 314–338.
- F. Mémoli and T. Needham, *Distance Distributions and Inverse Problems for Metric Measure Spaces*, arXiv:1810.09646v1 (2018), Stud. Appl. Math. 149 (2022), 943–1001.
