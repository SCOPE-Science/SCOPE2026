# A universal brightness-stabilizing height for convex prisms

## Finding
Let \(B\subset\mathbb R^2\) be any compact convex body with interior, area \(A>0\), and Euclidean width \(w_B(\theta)\) in the direction \((\cos\theta,\sin\theta)\). Define
\[
\beta=\frac1{2\pi}\int_0^{2\pi}w_B(\theta)\,d\theta=\frac{\operatorname{per}(B)}\pi,
\quad \eta=\frac1{2\pi}\int_0^{2\pi}w_B(\theta)^2\,d\theta,
\quad q=\frac\eta{\beta^2}\ge1.
\]
For \(H>0\), form \(P_H=B\times[-H/2,H/2]\subset\mathbb R^3\), and let \(S_H\) be the area of the Euclidean orthogonal projection of \(P_H\) onto a Haar-uniform unoriented plane. Then the squared coefficient of variation \(\mathcal C_B(H)^2=\operatorname{Var}(S_H)/(\mathbb E S_H)^2\) has a **unique global minimum** at
\[
\boxed{H_*=\frac{A\beta(\pi-2)}{4\eta-\pi\beta^2}}.
\]
The optimized value depends on the base only through its normalized second width moment:
\[
\boxed{\mathcal C_B(H_*)^2=
\frac{8q-3\pi^2+12\pi-16}{3(8q+\pi^2-4\pi)}.}
\]
This expression is strictly increasing in \(q\). Therefore the sharp universal bound
\[
\mathcal C_B(H_*)^2\ge
\frac{-3\pi^2+12\pi-8}{3(\pi^2-4\pi+8)}
\]
holds, with equality if and only if \(B\) has constant Euclidean width. Furthermore,
\[
\boxed{0<\frac{H_*\beta}{A}\le\frac{\pi-2}{4-\pi},}
\]
with the same equality condition. These include all nonsmooth planar convex bases.

For a centered equilateral triangular base with circumradius one, the coefficient-of-variation optimum is \(H_*=1.035995798238795\ldots\), but the height minimizing the worst-view brightness ratio is exactly \(H_{\rm worst}=\sqrt3/2\). Both are unique, and \(H_*>H_{\rm worst}\).

## Assumptions and scope
Haar-uniform unoriented planes mean rotation-invariant probability on the two-dimensional Grassmannian of \(\mathbb R^3\), equivalently the orthogonal complement of a uniform vector \(U\in S^2\). Shadow area means ordinary two-dimensional Lebesgue area. The base need not be centered, smooth, strictly convex or polygonal. Width is the sum of support functions in antipodal directions; consequently \(w_B\) is continuous and strictly positive. The height \(H\) is the **full** distance between the two base planes (not a half-height). The area \(A\), the first width moment \(\beta\) and the second width moment \(\eta\) refer to the same planar base.

## Proof
**1. Exact shadow-area decomposition.** Write a viewing normal as
\[
U=(\sqrt{1-Z^2}\cos\Phi,\sqrt{1-Z^2}\sin\Phi,Z).
\]
The projection of a prism is the Minkowski sum of the projected base and the projected vertical segment. The former has area \(A|Z|\); the latter has length \(H\sqrt{1-Z^2}\). The planar width of the projected base perpendicular to that segment equals the original base width in the horizontal direction perpendicular to \((\cos\Phi,\sin\Phi)\). The elementary planar swept-area identity \(\operatorname{area}(K+[0,t]v)=\operatorname{area}(K)+t\,w_K(v^\perp)\) therefore gives, including vertical and horizontal limiting directions,
\[
\boxed{S_H=A|Z|+H\sqrt{1-Z^2}\,w_B(\Phi+\pi/2).}\tag{1}
\]
This geometric identity is exact, not asymptotic.

**2. Exact first and second moments.** For uniform \(U\), the variable \(|Z|\) is uniform on \([0,1]\) and independent of \(\Phi\), which is uniform on \([0,2\pi)\). The elementary moments are
\[
\mathbb E|Z|=\tfrac12,\quad \mathbb EZ^2=\tfrac13,\quad
\mathbb E\sqrt{1-Z^2}=\tfrac\pi4,\quad
\mathbb E(1-Z^2)=\tfrac23,\quad
\mathbb E(|Z|\sqrt{1-Z^2})=\tfrac13.
\]
Using the two width moments in (1) yields
\[
\mathbb ES_H=\frac A2+\frac{\pi H\beta}4,
\]
\[
\operatorname{Var}(S_H)=\frac{A^2}{12}+AH\beta\left(\frac23-\frac\pi4\right)
+H^2\left(\frac{2\eta}3-\frac{\pi^2\beta^2}{16}\right).\tag{2}
\]
Both are valid for every \(H>0\).

**3. The unique optimum.** Put \(s=H\beta/A>0\) and \(q=\eta/\beta^2\). The ratio (2) becomes
\[
F_q(s)=\frac{\frac1{12}+\left(\frac23-\frac\pi4\right)s
+\left(\frac{2q}3-\frac{\pi^2}{16}\right)s^2}
{\left(\frac12+\frac{\pi s}4\right)^2}.
\]
A direct differentiation, with strictly positive denominator, gives the exact derivative
\[
F_q'(s)=\frac{(2-\pi)+(4q-\pi)s}
{6\left(\frac12+\frac{\pi s}4\right)^3}.\tag{3}
\]
By Jensen's inequality, \(q\ge1\). Since \(4-\pi>0\) and \(\pi-2>0\), the numerator of (3) changes sign exactly once on \((0,\infty)\), from negative to positive, at
\[
s_* = \frac{\pi-2}{4q-\pi}.
\]
Thus the displayed \(H_*=As_*/\beta\) is the unique global minimizer, including both open endpoints of the height range. Substituting \(s_*\) gives the stated optimized quotient.

**4. Constant-width rigidity and sharpness.** The derivative with respect to \(q\) of the optimized quotient is
\[
\frac{32(\pi-2)^2}{3(8q+\pi^2-4\pi)^2}>0.
\]
Hence the smallest possible optimized variance and the largest possible normalized optimizing height occur at \(q=1\). Jensen equality \(\eta=\beta^2\) means that the continuous function \(w_B(\theta)\) equals \(\beta\) for all \(\theta\), which is precisely the constant-width condition. Disks and other planar constant-width bodies realize equality. The exact height deficit for a non-constant-width base is
\[
\frac{\pi-2}{4-\pi}-\frac{H_*\beta}{A}
=\frac{4(\pi-2)(q-1)}{(4-\pi)(4q-\pi)}.
\]

**5. A distinct worst-view optimizer for equilateral bases.** Take the equilateral triangle of circumradius one. Here \(A=3\sqrt3/4\), \(\beta=3\sqrt3/\pi\) and \(\eta=3/2+9\sqrt3/(4\pi)\), obtained by integrating the squared support of its regular hexagonal difference body. Inserting these into the general height law gives \(H_*=1.035995798238795\ldots\). Alternatively write \(t=\sqrt3H/2\); its shadow area at a normal \(u=(u_x,u_y,u_z)\) is
\[
S_H=A|u_z|+t\sum_{j=0}^2 |u_x\cos(2\pi j/3)+u_y\sin(2\pi j/3)|.
\]
The three horizontal normal projections sum to zero, so the absolute-value sum ranges from \(\sqrt3\sqrt{1-u_z^2}\) to \(2\sqrt{1-u_z^2}\). Optimizing over \(|u_z|\in[0,1]\) yields the exact global extrema
\[
\min_u S_H=\min\{A,\sqrt3t\},\qquad \max_u S_H=\sqrt{A^2+4t^2}.
\]
Consequently the maximal-to-minimal shadow-area ratio decreases strictly until \(H=\sqrt3/2\), then increases strictly. This unique ratio minimizer differs from \(H_*\); its minimum ratio is \(\sqrt{7/3}\). The comparison \(H_*>\sqrt3/2\) follows directly from the explicit constants, for instance using \(3.14159<\pi<3.14160\) and \(1.73205<\sqrt3<1.73206\).

## Verification
The accompanying standard-library Python file `verify_prism_brightness.py` computes projected convex-hull areas directly from the vertices of four distinct polygonal prism bases (equilateral triangle, square, regular pentagon and an irregular convex pentagon), with three positive heights for each base. It checks (1) at 57,600 seeded, Haar-sampled directions against independent shoelace hull areas (absolute error tolerance \(10^{-10}\)); then independently compares sampled first and second moments against (2), calculates width moments by angular quadrature, and tests the unique optimizing-height inequality on both sides of the predicted optimum. It verifies the equilateral example's two distinct heights. The executed output was `ALL_CONVEX_POLYGON_PRISM_SHADOW_CHECKS_PASSED` and `TRIANGLE_TWO_DISTINCT_OPTIMAL_HEIGHTS_PASSED`. Finite sampling does not establish the theorem for all bases; steps 1--5 are its complete analytic proof.

## Relationship to prior work
Cauchy's planar perimeter and three-dimensional projection formulas, the swept-area identity, and the elementary spherical coordinate distribution are classical and not claimed as new. Black and Criado [1], whose first public version appeared in June 2024, develop bounds on the number of vertices of random polytope shadows; their full preprint concerns shadow complexity rather than the height optimizing relative variance of projected **area**. An independently available result on exact mean-square directional **width** of uniform regular polygonal prisms [2] uses a related Cartesian-product width-moment decomposition; it covers fixed unit-edge regular bases and unit height and does not state the all-base brightness optimization or the sharp constant-width rigidity. More general width-moment identities are an evident route to (2), which is treated here as an ingredient rather than the standalone originality claim. Existing polytope projected-area tensor calculations [3] treat orthotopes and do not determine all convex-base prism optimizers. The claimed contribution is specifically the universal unique optimizing height, its exact normalized shape dependence, and the sharp constant-width equality classification, with the equilateral worst-view contrast as an example.

## Limitations
The shadow law is for ordinary Euclidean orthogonal projections of finite right prisms with a planar convex base, not oblique prisms, nonconvex bases, or higher-dimensional products. The proof does not determine the full distribution of shadow area or characterize the minimizers of alternative loss functions. The bibliographic check is not an exhaustive historical priority certification: older stereological or caliper-width literature could contain equivalent optimized-height relations. This report has not received an independent mathematical audit.

## References
[1] A. E. Black and F. Criado, "Random Shadows of Fixed Polytopes", arXiv:2406.06936v1, first posted 2024-06-11, https://arxiv.org/html/2406.06936v1.

[2] "Exact mean-square width of every uniform regular prism", published research record, 2026, available in the public published-finding corpus mathematics collection (the regular-prism width-moment result; not a statement of the present optimization).

[3] "Exact planar shadow-area moments for all orthotopes", published research record, 2026 (the all-orthotope projected-area moment calculation; not an all-convex-base right-prism result).
