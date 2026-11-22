# The isoperimetric curvature law for isotropic constants of rounded triangles

## Finding
Let \(T\subset\mathbb R^2\) be **any nondegenerate Euclidean triangle**, with area \(A>0\), perimeter \(P\), inradius \(r>0\), and let \(B\) be the Euclidean unit disk. For a full-dimensional planar convex body \(K\), write
\[
\mathcal J(K)=\frac{\det\operatorname{Cov}(X_K)}{\operatorname{area}(K)^2},
\]
where \(X_K\) is uniformly distributed on \(K\). Define the signed parallel family \(T_t=T+tB\) for \(t\ge0\), and \(T_t=T\mathbin{\sim}(-t)B\) for \(-r<t<0\), where \(\sim\) denotes Minkowski erosion.

Then
\[
\boxed{\mathcal J(T_t)=\frac1{108}\quad(-r<t\le0),}
\]
while the exact right-hand quadratic response is
\[
\boxed{\mathcal J(T_t)=\frac1{108}-\frac{P^2-4\pi A}{108A^2}\,t^2+O_T(t^3),\qquad t\downarrow0.}
\tag{1}
\]
Thus the signed profile is \(C^1\) but not \(C^2\) at \(0\), and
\[
\mathcal J''(0-)=0,\qquad
\mathcal J''(0+)=-\frac{P^2-4\pi A}{54A^2}<0.
\tag{2}
\]
The coefficient is **exactly the Euclidean isoperimetric deficit**, multiplied by \(1/(108A^2)\), for every scalene as well as every isosceles triangle. In particular, with scale-free rounding parameter \(u=t/\sqrt A\), the coefficient of the drop is
\[
\boxed{\lim_{u\downarrow0}\frac{\mathcal J(T)-\mathcal J(T+u\sqrt A B)}{u^2}
=\frac{P^2/A-4\pi}{108}\ge\frac{3\sqrt3-\pi}{27},}
\tag{3}
\]
with **equality if and only if \(T\) is equilateral**. Knowing \(A\), the right curvature of \(\mathcal J(T_t)\) at zero uniquely recovers \(P\).

## Assumptions and scope
All moment integrals use planar Lebesgue area and ordinary Euclidean distance. The covariance is taken about the **current centroid of \(T_t\)**, not the original triangle centroid; this correction matters for scalene triangles. The expansion (1) holds for each fixed nondegenerate triangle and is not claimed uniform as triangles degenerate. The right-hand family is a disk Minkowski sum, while the left-hand family is erosion, not formal subtraction of support functions outside its valid range. This is a **local second-order theorem**; no assertion of all-radius strict monotonicity for arbitrary triangles is made. The equilateral specialization is already covered by earlier regular-polygon rounding work; the all-triangle isoperimetric identity and its inverse and rigidity consequences are the contribution.

## Proof
Translate the centroid of \(T\) to the origin, and let its three counterclockwise vertices be \(v_0,v_1,v_2\). Thus \(v_0+v_1+v_2=0\). Denote by \(\ell_i\) the Euclidean length of the side opposite \(v_i\), and by \(n_i\) that side's outward unit normal. Put
\[
S=\sum_{i=0}^2v_iv_i^{\mathsf T},\qquad P=\ell_0+\ell_1+\ell_2.
\]
Since \(T\) is nondegenerate, \(S\) is positive definite. Uniform barycentric integration over a triangle gives the unnormalized second-moment matrix and the basic determinant identities
\[
Q_0:=\int_Txx^{\mathsf T}\,dx=\frac A{12}S,\qquad
\det S=\frac{4A^2}{3},\qquad
v_i^{\mathsf T}S^{-1}v_j=\begin{cases}2/3&i=j,\\-1/3&i\ne j.\end{cases}
\tag{4}
\]
Consequently \(\mathcal J(T)=1/108\).

For positive \(t\), partition \(T+tB\), up to null boundaries, into the original triangle, the three width-\(t\) rectangles outside the edges, and the three circular sectors at the vertices. The planar Steiner area formula yields
\[
A_t=\operatorname{area}(T+tB)=A+Pt+\pi t^2.
\tag{5}
\]
Let \(M(t)=\int_{T+tB}x\,dx\) and \(Q(t)=\int_{T+tB}xx^{\mathsf T}\,dx\). Integration along each edge, whose midpoint is \(-v_i/2\), gives
\[
M(t)=tM_1+O_T(t^2),\qquad M_1=-\frac12\sum_i\ell_i v_i,
\tag{6}
\]
\[
Q(t)=Q_0+tQ_1+t^2Q_2+O_T(t^3),\qquad Q_1=\frac P6 S=\frac{2P}{A}Q_0.
\tag{7}
\]
For the second-order matrix, write \(Q_2=Q_{2,\mathrm{edge}}+Q_{2,\mathrm{corner}}\). The edge strips contribute
\[
Q_{2,\mathrm{edge}}=-\frac14\sum_i\ell_i\bigl(v_in_i^{\mathsf T}+n_iv_i^{\mathsf T}\bigr).
\tag{8}
\]
The oriented edge length normal satisfies the exact triangle identity
\[
\ell_i n_i=-2A S^{-1}v_i.
\tag{9}
\]
Indeed, the dot product of both sides with \(v_i\) is \(-4A/3\), and the dot product with either other vertex is \(2A/3\), because those two vertices lie on the opposite edge; (4) then proves the equality of the vectors. Substituting (9) into (8) gives a **shape-independent** matrix:
\[
Q_{2,\mathrm{edge}}=\frac A2\sum_i\bigl(v_i(S^{-1}v_i)^{\mathsf T}+(S^{-1}v_i)v_i^{\mathsf T}\bigr)=A I_2.
\tag{10}
\]
If \(\alpha_i>0\) denotes the exterior turning angle at \(v_i\), then \(\sum_i\alpha_i=2\pi\) and the sector contributions at order \(t^2\) are
\[
Q_{2,\mathrm{corner}}=\frac12\sum_i\alpha_i v_iv_i^{\mathsf T}.
\tag{11}
\]
The next-order terms are irrelevant for the quadratic coefficient. From (4), (10) and (11),
\[
\operatorname{tr}(Q_0^{-1}Q_{2,\mathrm{corner}})=\frac{8\pi}{A},\quad
\operatorname{tr}(Q_0^{-1}Q_{2,\mathrm{edge}})=12\operatorname{tr}(S^{-1})=\frac{3\sum_i\ell_i^2}{A^2}.
\tag{12}
\]
The last equality follows from (9) and \(S=\sum_i v_iv_i^{\mathsf T}\): summing \(\|\ell_i n_i\|^2=4A^2\|S^{-1}v_i\|^2\) yields \(\sum_i\ell_i^2=4A^2\operatorname{tr}(S^{-1})\). Similarly, the mutual inner products in (4) show
\[
\frac1A M_1^{\mathsf T}Q_0^{-1}M_1=\frac{3\sum_i\ell_i^2-P^2}{A^2}.
\tag{13}
\]

The centered unnormalized matrix is \(N(t)=Q(t)-M(t)M(t)^{\mathsf T}/A_t\), so \(\mathcal J(T+tB)=\det N(t)/A_t^4\). Equations (5)--(7) give, by a second-order determinant expansion,
\[
\mathcal J(T+tB)=\frac1{108}\Biggl[1+t^2\biggl(
\operatorname{tr}(Q_0^{-1}Q_2)
-\frac1A M_1^{\mathsf T}Q_0^{-1}M_1
-\frac{2P^2}{A^2}-\frac{4\pi}{A}\biggr)+O_T(t^3)\Biggr].
\tag{14}
\]
Substituting (12)--(13) makes every squared individual side length cancel. The bracketed quadratic coefficient becomes \(-P^2/A^2+4\pi/A\), proving (1). The strict negativity follows from \(P^2\ge12\sqrt3\,A>4\pi A\) for triangles.

For the inner family, let \(z\) be the incenter of \(T\), with inradius \(r\). All three supporting lines are distance \(r\) from \(z\). Eroding by a radius-\(s\) disk, for \(0\le s<r\), moves all three supporting lines inward by \(s\), hence
\[
T\mathbin{\sim}sB=z+(1-s/r)(T-z).
\]
Because \(\mathcal J\) is invariant under nondegenerate affine maps, it is constantly \(1/108\) along this left family. The right expansion has zero linear term and strictly negative quadratic term, proving (2) and the precise \(C^1\)-not-\(C^2\) assertion. Finally, the sharp triangle perimeter inequality \(P^2\ge12\sqrt3 A\), with equality only for the equilateral triangle, gives (3) and its equality case. Solving (2) for \(P^2\) gives the perimeter-recovery claim.

## Verification
The accompanying `verify.py` uses SymPy to check the coordinate-free triangle moment identities symbolically in a generic triangle with vertices \((0,0),(1,0),(x,y)\). It verifies the outward normal relation, the edge-strip cancellation \(Q_{2,\mathrm{edge}}=A I_2\), the centroid correction, and the exact quadratic coefficient after imposing the true squared side lengths. An independent geometric regression constructs rounded-triangle boundaries from line segments and circular arcs, calculates their area and raw second moments by Green's theorem, and checks the limiting coefficient on 20 scalene/equilateral shapes and several offsets. Execute `python verify.py` with SymPy installed; all geometric checks otherwise use the Python standard library. Finite numerical tests are only consistency checks, not proofs of the quantified theorem; the algebra above proves that theorem for every nondegenerate triangle.

## Relationship to prior work
Richter and Saorín Gómez established monotonicity of the isoperimetric **quotient** along inner and outer parallel bodies, with an earliest public preprint on March 31, 2020. Their result concerns area and perimeter rather than the determinant of centroidal covariance. It supplies the natural geometric setting but does not imply (1): the value of area/perimeter alone does not determine a convex body's covariance. The classical Steiner formula and uniform-simplex covariance identity are used as known inputs.

Rademacher's treatment of the isotropic constant provides the affine-invariant normalization. The independently published cube-rounding analysis computes a second-order isotropic-constant response for cubes, not triangles, and does not recover the planar triangle isoperimetric deficit. Earlier regular-polygon rounding calculations **already include the equilateral specialization** and its all-radius monotonicity; the novelty asserted here is the shape-independent isoperimetric-curvature identity for *all*, including scalene, triangles and the sharp inverse/rigidity consequences. A published first-moment centroid-path analysis of rounded triangles does not cover the required second-moment/covariance cancellation. These comparisons are not a claim of unconditional historical priority.

## Limitations
No all-positive-radius monotonicity theorem is claimed for scalene or irregular triangles. The result does not extend automatically to quadrilaterals or higher-dimensional simplices, where the second-order identity may have a different form. The \(O_T(t^3)\) remainder depends on the particular nondegenerate triangle. The curvature formula is a right-hand local statement and must not be used for finite-radius perimeter estimation without controlling higher-order terms. Previously published equilateral and cube results are not presented as new. A less searchable historical computation of rounded-triangle covariance remains a possible priority risk.

## References
1. C. Richter and E. Saorín Gómez, *On the monotonicity of the isoperimetric quotient for parallel bodies*, arXiv:2003.14182, first submitted March 31, 2020; Journal of Geometric Analysis 32 (2022), article 15. https://arxiv.org/abs/2003.14182.
2. L. Rademacher, *A simplicial polytope that maximizes the isotropic constant must be a simplex*, arXiv:1404.5662 (2014). https://arxiv.org/abs/1404.5662.
3. *Sharp isotropic response to Euclidean rounding of cubes*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-isotropic-response-to-euclidean-rounding-of-cubes--c7d29f80bf57/RESULT.md.
4. *Sharp isotropic-constant monotonicity for circular roundings of all regular polygons*, published mathematical record; the triangular regular-polygon case is acknowledged as prior.
5. *Hyperbolic curvature paths and quantitative triangle rigidity*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-hyperbolic-curvature-paths-and-quantitative-triangle-rigidity--7220229bf166/RESULT.md.
