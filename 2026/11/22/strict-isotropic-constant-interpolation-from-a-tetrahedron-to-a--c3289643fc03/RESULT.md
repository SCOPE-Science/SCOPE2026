# Strict isotropic-constant interpolation from a tetrahedron to a triangular prism under a one-vertex cut

## Finding
For each nondegenerate tetrahedron \(T\subset\mathbb R^3\) and a selected vertex, let \(K_t(T)\) be the retained body after cutting away a corner by a plane parallel to the opposite face. The affine-invariant depth \(t\in[0,1)\) is defined by the equivalent standard model
\[
K_t=\{x\in\mathbb R^3:x_i\ge0\ (i=1,2,3),\quad t\le x_1+x_2+x_3\le1\}.
\]
Let \(X_t\) be volume-uniform on \(K_t\), and define the isotropic constant by
\[
L(K_t)^6=\frac{\det(\operatorname{Cov}(X_t))}{\operatorname{Vol}_3(K_t)^2}.
\]
Set \(P(t)=1+t+t^2+t^3+t^4\) and \(Q(t)=1+4t+10t^2+4t^3+t^4\). The complete affine-invariant profile is
\[
\boxed{L(K_t)^6=\frac{9P(t)^2Q(t)}{8000(1+t+t^2)^6}.}
\]
It is **strictly decreasing** as the cut depth increases on \((0,1)\), for every initial tetrahedron. The sharp endpoints and limiting ratio are
\[
\boxed{L(K_0)^6=\frac9{8000},\qquad \lim_{t\uparrow1}L(K_t)^6=\frac1{1296},\qquad\frac{L(K_{1^-})^6}{L(K_0)^6}=\frac{500}{729}.}
\]
The lower value is not attained by a full-dimensional member; after an affine rescaling, the limiting body is a triangular prism. Near the original tetrahedron, the first decrease is cubic:
\[
L(K_t)^6=\frac9{8000}-\frac9{800}t^3+O(t^4).
\]
Near the triangular-prism limit, the gap is quadratic:
\[
L(K_t)^6-\frac1{1296}=\frac{(1-t)^2}{3240}+O((1-t)^3).
\]

## Assumptions and scope
A tetrahedron is any convex hull of four affinely independent points in Euclidean three-space. A single vertex is clipped by a plane parallel to its opposite face; no other vertex is cut. The parameter \(t\) is the barycentric level of the new plane relative to the removed vertex, so \(t=0\) is the original tetrahedron and \(t\uparrow1\) retains an increasingly thin slab next to the opposite facet. The endpoint \(t=1\) itself is a two-dimensional set and is excluded from the definition of its three-dimensional isotropic constant. The density of \(X_t\) is normalized three-dimensional Lebesgue measure, not boundary measure or vertex counting. The result is affine invariant because covariance transforms by congruence and volume by the absolute determinant of the linear map. All conclusions apply to the original tetrahedron by affine equivalence.

## Proof
**1. Exact raw moments.** Let \(\Delta=\{x_i\ge0,\sum_i x_i\le1\}\). The removed corner is \(t\Delta\), with interiors disjoint from \(K_t\). The base simplex has volume \(1/6\) and Dirichlet barycentric moments
\[
\mathbb E_\Delta X_i=\frac14,\qquad\mathbb E_\Delta X_i^2=\frac1{10},\qquad\mathbb E_\Delta X_iX_j=\frac1{20}\quad(i\ne j).
\]
These follow, for example, by repeatedly integrating monomials on \(\Delta\), or from the uniform Dirichlet law of its four barycentric coordinates. Homothety multiplies an integral of a homogeneous polynomial of degree \(k\) over \(t\Delta\) by \(t^{k+3}\). Subtracting these integrals and normalizing by the retained volume yields
\[
V_t=\frac{1-t^3}{6},\quad
m_t:=\mathbb E X_i=\frac{1-t^4}{4(1-t^3)},\quad
A_t:=\mathbb E X_i^2=\frac{1-t^5}{10(1-t^3)},\quad
B_t:=\mathbb E X_iX_j=\frac{1-t^5}{20(1-t^3)}\ (i\ne j).
\]
All denominators are positive for \(0\le t<1\).

**2. Covariance eigenvalues and exact determinant.** By coordinate-permutation symmetry, the covariance has diagonal entries \(A_t-m_t^2\) and off-diagonal entries \(B_t-m_t^2\). The two-dimensional plane orthogonal to \((1,1,1)\) has eigenvalue \(A_t-B_t=B_t\); the axial vector has eigenvalue \(A_t+2B_t-3m_t^2=4B_t-3m_t^2\). Therefore
\[
\det\operatorname{Cov}(X_t)=B_t^2(4B_t-3m_t^2).
\]
Substitution into \(L(K_t)^6=B_t^2(4B_t-3m_t^2)/V_t^2\), cancellation of \((1-t)^3\) factors and polynomial multiplication give the displayed rational expression with \(P\) and \(Q\). This is also manifestly positive for all admissible parameters, as required by positive definiteness.

**3. Global strict monotonicity.** Exact differentiation and polynomial factorization give
\[
\boxed{\frac{d}{dt}L(K_t)^6=\frac{27t^2(t-1)(t+1)^3P(t)}{800(1+t+t^2)^7}.}
\]
Every factor is strictly positive except \(t-1\), which is strictly negative for \(0<t<1\). Thus the derivative is strictly negative throughout the entire nondegenerate family. Continuity at \(t=0\) proves strict decrease on \([0,1)\), including its endpoint. The cubic small-cut law follows by expanding this exact derivative at zero and integrating.

**4. Sharp endpoints and the prism limit.** Direct substitution in the rational expression gives \(L(K_0)^6=9/8000\) and continuous limiting value \(1/1296\); their quotient is \(500/729\). Expanding at \(t=1\) gives \(1/1296+(1-t)^2/3240+O((1-t)^3)\). Under an affine map that stretches the thin direction by \((1-t)^{-1}\), the cross-sections of \(K_t\) converge to congruent copies of a triangular base, so the limit is an affine triangular prism \(\Delta_2\times[0,1]\). Independently, \(L(\Delta_2)^4=1/108\) and \(L([0,1])^2=1/12\), so the product invariant is \(1/(108\cdot12)=1/1296\). This agrees with the rational limit and supplies a geometric explanation for the sharp endpoint. \(\square\)

## Verification
The standalone standard-library script `verify.py` triangulates every selected frustum into three tetrahedra, integrates linear and quadratic monomials over each tetrahedron using barycentric coordinates, and compares the resulting volume, centroid, covariance and normalized determinant with the closed form **in exact rational arithmetic**. It passed 151 checks at ten rational cut depths from zero through \(99/100\), including strict ordering and both formula endpoints. This decomposition-based implementation does not use the removed-corner moment formulas to compute its integrals. These finite checks corroborate the algebra; strict monotonicity for all real admissible parameters rests on the exact displayed derivative and its sign.

Run `python3 verify.py` with Python 3 and no third-party packages. The expected final line is `EXACT_FRUSTUM_TETRAHEDRAL_CHECKS_PASSED 151`.

## Relationship to prior work
Kipp's *Small perturbations of polytopes* (first publicly posted March 31, 2023) proves first-order necessary conditions for extremal polytopes, including a local isotropic-constant condition, but not an all-depth covariance profile for one clipped tetrahedral vertex. His *Isotropic constants and regular polytopes* (first posted July 1, 2024) strengthens a characterization of possible local maximizers with simplicial vertices; it does not itself imply monotonicity for a specified one-vertex cut.

The published *The exact isotropic-constant profile of uniformly vertex-truncated simplices* treats simultaneous symmetric cuts at **every** simplex vertex, not the one-vertex prismatoid considered here. The published *Exact Godbersen mixed-volume profile for one-vertex simplex truncations* treats precisely these bodies, but its outputs are opposite-body mixed-volume coefficients, rather than the centroid and covariance determinant. *Exact John–Löwner ellipsoids and a sharp volume-ratio spectrum for one-vertex simplex frusta* likewise treats the same geometry but its optimized enclosing and inscribed ellipsoids do not determine the volume-uniform covariance determinant. The present claim is the exact isotropic-constant ordering of a one-cut tetrahedron, not a new formula for those previously studied invariants.

## Limitations
The classification applies to one facet-parallel cut of a tetrahedron, not arbitrary oblique or multiple truncations or all higher-dimensional simplices. The limiting triangular prism is an affine limit after anisotropic rescaling, not an actual three-dimensional member at \(t=1\). Monotonicity along this family is not a universal maximization theorem for all convex bodies. The determinant can be computed by elementary moments, so the mathematical contribution is the natural **complete sharp all-depth order and equality structure**, not a claim that its individual integration steps are new. Historical priority remains provisional: a generic inertia formula or an unindexed classical prismatoid calculation might reproduce this special normalized determinant.

## References
1. C. Kipp, *Small perturbations of polytopes*, arXiv:2303.18033v1, first posted 2023-03-31; https://arxiv.org/abs/2303.18033.
2. C. Kipp, *Isotropic constants and regular polytopes*, arXiv:2407.01353v1, first posted 2024-07-01; https://arxiv.org/abs/2407.01353.
3. *The exact isotropic-constant profile of uniformly vertex-truncated simplices*, public research record, 2026-11-08.
4. *Exact Godbersen mixed-volume profile for one-vertex simplex truncations*, public research record, 2026-10-11.
5. *Exact John–Löwner ellipsoids and a sharp volume-ratio spectrum for one-vertex simplex frusta*, public research record, 2026-11-02.
6. F. Tonon, *Explicit Exact Formulas for the 3-D Tetrahedron Inertia Tensor in Terms of its Vertex Coordinates*, J. Math. Stat. 1 (2005), 8–11; DOI:10.3844/jmssp.2005.8.11 (used only as prior generic tetrahedral inertia context).
