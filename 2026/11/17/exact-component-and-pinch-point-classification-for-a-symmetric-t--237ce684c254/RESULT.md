# Exact component and pinch-point classification for a symmetric three-site anisotropic Voronoi diagram

## Finding

Let \(v_1,v_2,v_3\) be the vertices of the unit-circumradius equilateral triangle centered at the origin, indexed counterclockwise from \(v_1=(1,0)\). For every \(\kappa>0\), assign each site the constant positive-definite quadratic matrix
\[
 M_j=I+(\kappa-1)v_jv_j^{\mathsf T},\qquad j=1,2,3,
\]
and define the closed full-plane nearest-site cells
\[
 V_j=\{z\in\mathbb R^2:(z-v_j)^{\mathsf T}M_j(z-v_j)\le (z-v_i)^{\mathsf T}M_i(z-v_i)\text{ for all }i\}.
\]
Every \(M_j\) has the same eigenvalues \(\{1,\kappa\}\) and the same determinant \(\kappa\); thus the family has genuine rotated, site-dependent anisotropy for \(\kappa\ne1\), not site-dependent scalar weights.

Write \(z=(X,\sqrt3Y)\). The complete classification, including equality boundaries, is as follows, with the cells \(V_2,V_3\) obtained from \(V_1\) by rotations of \(120^\circ\).

**Cheaper radial direction, \(0<\kappa<1\).** Set \(c=2\kappa/(1-\kappa)\). Then
\[
 V_1=C_{\mathrm{near}}\mathbin{\dot\cup}C_{\mathrm{orphan}},\qquad
 C_{\mathrm{near}}=\{X\ge|Y|,\ -X+3|Y|\le2c\},\qquad
 C_{\mathrm{orphan}}=\{X+3|Y|\le-2c\}.
\]
Both are nonempty, closed, convex, unbounded polyhedra. They are exactly the two connected components of \(V_1\). The first contains \(v_1\), while the second contains no generating site of \(V_1\). Their minimum Euclidean separation is exactly \(2c=4\kappa/(1-\kappa)\), attained uniquely between \(z=(0,0)\) and \(z=(-2c,0)\).

**Isotropic case, \(\kappa=1\).** The cell is the ordinary closed convex wedge
\[
 V_1=\{X\ge|Y|\}.
\]

**Costlier radial direction, \(\kappa>1\).** Set \(c=2\kappa/(\kappa-1)\). Then
\[
 V_1=K\cup E_+\cup E_-,\qquad
 K=\{X\ge|Y|,\ X+3|Y|\le2c\},
\]
\[
 E_+=\{Y\ge|X|,\ X+3Y\ge2c\},\qquad
 E_-=\{-Y\ge|X|,\ X-3Y\ge2c\}.
\]
The bounded central quadrilateral \(K\) has consecutive Euclidean vertices
\[
 (0,0),\quad(c/2,\sqrt3c/2),\quad(2c,0),\quad(c/2,-\sqrt3c/2)
\]
and exact area \(\sqrt3c^2\). Each \(E_\pm\) is convex and unbounded, and
\[
 K\cap E_+=\{(c/2,\sqrt3c/2)\},\quad
 K\cap E_-=\{(c/2,-\sqrt3c/2)\},\quad E_+\cap E_-=\varnothing.
\]
Consequently \(V_1\) is path connected and contractible but not star-shaped at its generating site, has exactly two cut points, and its topological interior has exactly three connected components. Its two cut points are precisely the stated one-point intersections. The three constituent polyhedra give an explicit global decomposition, not merely a bounded-window observation.

In either anisotropic regime the additional features recede to infinity as \(\kappa\to1\); on every fixed compact subset of the plane, the cells tend to the ordinary Euclidean wedge. Thus the unique isotropic parameter separates a disconnected-cell regime from a connected-but-pinched regime.

## Assumptions and scope

The sites are exactly the three stated equilateral vertices at circumradius one, and the distance functions are the square roots of their *site-assigned* fixed quadratic forms. All cells are considered as closed subsets of the entire Euclidean plane: ties belong to all minimizing cells. A generating site's cell need not be bounded. Topological interiors, connected components, cut points and Euclidean distances use the standard topology and metric of \(\mathbb R^2\). The parameter \(\kappa\) ranges over all positive real numbers, and neither \(\kappa=0\) (not positive definite) nor arbitrary three-site positions or independently chosen matrices is included. The area assertion concerns only the bounded core \(K\), not the unbounded full cell.

## Proof

**1. Reducible bisectors.** Put \(t_j=z\cdot v_j\), so \(t_1+t_2+t_3=0\), and denote the squared assigned distance by \(Q_j(z)\). The unit length of \(v_j\) gives the exact identity
\[
 Q_j(z)=\|z\|_2^2+\kappa+(\kappa-1)t_j^2-2\kappa t_j.
\]
For any permutation \((i,j,k)\) of \((1,2,3)\), subtraction and \(t_i+t_j=-t_k\) give
\[
 Q_i-Q_j=(t_i-t_j)\bigl[-(\kappa-1)t_k-2\kappa\bigr].\tag{1}
\]
Every nominally conic pairwise bisector factors into two real lines, a nontrivial consequence of the radial alignment and equal matrix spectra. In the coordinates \(z=(X,\sqrt3Y)\),
\[
 t_1=X,\quad t_2=(-X+3Y)/2,\quad t_3=(-X-3Y)/2.
\]
Set \(u=X-Y\) and \(v=X+Y\), and note that \(t_1-t_2=3u/2\) and \(t_1-t_3=3v/2\).

**2. Exactly two components for \(0<\kappa<1\).** Put \(c=2\kappa/(1-\kappa)>0\) and \(h=2c\). By (1), after multiplication by positive constants, the two inequalities \(Q_1\le Q_2,Q_3\) become
\[
 u(-u+2v+h)\ge0,\qquad v(2u-v+h)\ge0.\tag{2}
\]
If \(u,v>0\), (2) requires \(-u+2v+h\ge0\) and \(2u-v+h\ge0\); substituting back yields \(X\ge|Y|\) and \(-X+3|Y|\le h\), the interior and appropriate boundaries of \(C_{\mathrm{near}}\). If \(u,v<0\), both bracketed factors must be nonpositive, equivalent to \(X+3|Y|\le-h\), the orphan polyhedron. The mixed strict-sign cases are impossible: when \(u>0>v\), the second bracket \(2u-v+h\) is strictly positive despite the required nonpositive sign, and the other mixed case is symmetric. When one factor vanishes, direct substitution in (2) places any surviving point on the boundary of one of the two polyhedra; no extra ray occurs. This proves the exact union including all ties.

Both displayed pieces are intersections of finitely many closed halfplanes, hence convex. The near piece has \(X\ge|Y|\ge0\), and the orphan piece has \(X\le-h-3|Y|\le-h\). Hence they are disjoint with distance at least \(h\), attained at the unique pair \((X,Y)=(0,0)\) and \((-h,0)\). Both extend to infinity along their respective horizontal axes. Each is therefore a connected component, and the far piece is an orphan because \(v_1=(1,0)\) belongs to the near piece.

**3. The isotropic limit.** At \(\kappa=1\), formula (1) reads \(Q_i-Q_j=-2(t_i-t_j)\), so \(Q_1\le Q_2,Q_3\) if and only if \(u,v\ge0\), namely \(X\ge|Y|\).

**4. Exact pinch decomposition for \(\kappa>1\).** Put \(c=2\kappa/(\kappa-1)>0\), \(h=2c\). Formula (1) now gives
\[
 u(u-2v+h)\ge0,\qquad v(v-2u+h)\ge0.\tag{3}
\]
If \(u,v>0\), the brackets are nonnegative, giving \(X\ge|Y|\) and \(X+3|Y|\le h\), the central quadrilateral \(K\). If \(u<0<v\), the first bracket must be nonpositive and the second is automatically strictly positive; the conditions reduce to \(Y\ge|X|\) and \(X+3Y\ge h\), namely \(E_+\). The case \(v<0<u\) similarly gives \(E_-\). The strictly negative-negative case cannot occur: both brackets would be nonpositive and adding their inequalities gives \(u+v\ge2h>0\), contradicting \(u+v<0\). Substitution on the axes \(u=0\) or \(v=0\) proves that their surviving endpoints lie in the displayed sets, so the decomposition includes all equality boundaries.

Each piece is the intersection of closed halfplanes. The four constraints defining \(K\) give exactly the four listed vertices. In \((X,Y)\) coordinates the shoelace area is \(c^2\); the change to Euclidean coordinates \((X,\sqrt3Y)\) multiplies area by \(\sqrt3\), yielding \(\sqrt3c^2\). If a point lies in both \(K\) and \(E_+\), then \(X\ge|Y|\), \(Y\ge|X|\), so \(X=Y\ge0\); the two opposite inequalities \(X+3Y\le h\) and \(X+3Y\ge h\) force \(X=Y=h/4=c/2\). The lower intersection is its reflection. The wings cannot intersect each other because their opposing \(Y\) constraints would force \(X=Y=0\), violating \(h>0\). These exact incidences exhibit a tree of three contractible convex sets joined at two points, so the closed cell is path connected and contractible. Deleting either one-point junction separates the corresponding wing, giving exactly two cut points. Since the three convex bodies meet only at these points, their (nonempty) open interiors are exactly the three connected components of \(\operatorname{int}V_1\). The site \(v_1\) lies in the interior of \(K\); visibility of an open wing from it would force a two-dimensional bridge where the wing and core only touch at one point, so the cell is not star-shaped about \(v_1\).

**5. Symmetry and local limit.** Rotation through \(2\pi/3\) permutes both sites and matrices, taking \(V_1\) to each other cell. For either anisotropic side, \(c\to\infty\) as \(\kappa\to1\). On each fixed compact region, all affine cutoff inequalities involving \(2c\) become inactive, and distant orphan or wing pieces disappear; this is the claimed local convergence.

## Verification

The standalone standard-library script `verify.py` computes the actual three quadratic costs using exact rational arithmetic at \(86{,}700\) rational grid configurations over twelve positive anisotropy ratios, then checks the proposed component membership independently at each point. It additionally checks exact triple-site ties, junctions and the shoelace area coefficient. Execute `python3 verify.py` in the directory containing this document. The expected output is `EQUILATERAL_ANISOTROPIC_EXACT_CHECKS_OK 86778`. These finite diagnostics do not establish the all-real-parameter or topological statements; those follow from the factorization and the exhaustive sign analysis in the proof.

## Relationship to prior work

Venkovic and Anzt (2026) formulate site-dependent quadratic anisotropic Voronoi diagrams and derive tensor boundary formulas *under site-star-convexity hypotheses*. Their introduction acknowledges disconnected anisotropic cells, but their formulas do not supply the present three-site radial-alignment decomposition, the exact orphan separation, or two-pinch topology. Labelle and Shewchuk (2003) provide the classical model and exhibit general orphan behavior; this fact is prior art rather than novel here. Canas and Gortler (2011) study sufficient conditions for orphan-free anisotropic diagrams. Published two-site Loewner-orphan classifications and a separate three-collinear-site, isotropically scaled phase diagram are closer in theme but neither covers this noncollinear, equally spectral, cyclically rotated matrix triple. In particular their theorems do not imply the factorization (1) or the three-way exact component classification above.

The conceptual contribution here is not that generic anisotropic cells can disconnect, nor that quadratic polynomials may factor. It is the explicit, complete classification of a natural symmetric three-site anisotropic family, including both the disconnected orphan regime and the distinct connected but non-manifold pinch regime, with sharp geometric constants.

## Limitations

The reducibility of the bisectors relies essentially on regular-triangle symmetry and radial eigenvector alignment. It should not be asserted for general anisotropic site triples, perturbations, bounded observation windows, or spatially varying metrics. The full cells are unbounded; the stated finite area belongs to the central quadrilateral alone. Independently established historical priority is not claimed; earlier geometric-degeneracy studies may have an equivalent formulation not found in the literature examined. The result is supported by an analytic proof and deterministic diagnostics, not an independent external audit.

## References

1. N. Venkovic and H. Anzt, *Minkowski Tensors of Planar Anisotropic Voronoi Diagrams*, arXiv:2610.08656v1 (first posted 2026-10-06), https://arxiv.org/html/2610.08656v1.
2. F. Labelle and J. R. Shewchuk, *Anisotropic Voronoi Diagrams and Guaranteed-Quality Anisotropic Mesh Generation*, SoCG (2003), https://people.eecs.berkeley.edu/~jrs/papers/aniso.pdf.
3. G. D. Canas and S. J. Gortler, *Orphan-Free Anisotropic Voronoi Diagrams*, arXiv:1102.3670 (2011), https://arxiv.org/abs/1102.3670.
4. *Loewner rigidity and an exact angular orphan law for two-site anisotropic Voronoi cells*, published 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-loewner-rigidity-and-an-exact-angular-orphan-law-for-two-site-an--53c1e4e86bb9.
5. *Sharp minimal-site visibility and three-site phase thresholds in quadratic Voronoi geometry*, published 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-minimal-site-visibility-and-three-site-phase-thresholds-in--dbd6f50c026b.
