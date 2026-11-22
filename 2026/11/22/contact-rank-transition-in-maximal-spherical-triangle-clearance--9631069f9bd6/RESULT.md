# Contact-rank transition in maximal spherical-triangle clearance

## Finding
For a uniformly surface-area-sampled point \(X\) of a fixed *spherical* geodesic triangle, the probability of lying within \(\varepsilon\) of its greatest attainable boundary distance has exactly three contact-rank regimes. The endpoint exponent is \(2\) when all three supporting sides have strictly positive optimal weights, and \(3/2\) when only two sides have positive weights. On the boundary between these regimes all three sides touch the maximizing disk, but only two have positive weights: the \(3/2\) coefficient is exactly half its strict two-contact value. Each regime has an explicit conditional limiting geometry. This is a family of sharp local distribution laws, not a formula for the full-distance CDF.

## Assumptions and scope
Work on the unit two-sphere \(S^2\) with geodesic distance and spherical area. Let \(n_1,n_2,n_3\in S^2\) be linearly independent *inward* unit normals, and let
\[
T=\{x\in S^2:n_i\cdot x\ge0\ \text{for }i=1,2,3\}.
\]
Assume the displayed intersection is the proper convex spherical triangle contained in an open hemisphere (equivalently, take the designated common positive spherical cell). It has area
\[
A=2\pi-\sum_{1\le i<j\le3}\arccos(n_i\cdot n_j)>0.
\]
Let \(X\) be area-uniform in \(T\). The clearance \(D(x)\) is the distance to \(\partial T\), and inside this convex cell it equals \(\min_i\arcsin(n_i\cdot x)\). The equality with the distance to *side arcs*, not merely supporting great circles, follows because the shortest exit from the intersection of hemispheres occurs when the first of these supporting great circles is reached.

Let \(z\) minimize \(\|z\|\) over \(\operatorname{conv}\{n_1,n_2,n_3\}\). Define \(r=\|z\|\), \(b=\sqrt{1-r^2}\), \(o=z/r\), \(\rho=\arcsin r\). For a proper triangle, \(0<r<1\), and there is a unique probability vector \((\lambda_1,\lambda_2,\lambda_3)\) representing \(z=\sum_i\lambda_i n_i\). Set \(G_{ij}=n_i\cdot n_j\).

**Three positive weights.** If every \(\lambda_i>0\), set \(c_{ij}=(G_{ij}-r^2)/b^2\) and
\[
C_3=\sum_{i<j}\sqrt{\frac{1-c_{ij}}{1+c_{ij}}}.
\]
Then \(C_3>0\) and
\[
\Pr\{D(X)\ge\rho-\varepsilon\}=\frac{C_3}{A}\,\varepsilon^2+o(\varepsilon^2).
\]
Define \(w_i=(n_i-r o)/b\in o^\perp\) and the bounded Euclidean tangent triangle
\[
P=\{y\in o^\perp:w_i\cdot y\ge-1\ \text{for }i=1,2,3\}.
\]
Conditionally on the displayed clearance event, \(\varepsilon^{-1}\log_o X\) converges in distribution to the **uniform area law on \(P\)**, where \(\log_o\) is the local inverse spherical exponential map. In this case \(\operatorname{area}(P)=C_3\). One may calculate \(r\) and the weights from the Gram matrix via \(r^2=(\mathbf1^\top G^{-1}\mathbf1)^{-1}\) and \(\lambda=G^{-1}\mathbf1/(\mathbf1^\top G^{-1}\mathbf1)\).

**Two positive weights, strict or critical.** If \(\lambda_i,\lambda_j>0\), \(\lambda_k=0\), the equal unit norms force \(\lambda_i=\lambda_j=1/2\). Let \(v=(n_i-n_j)/(2b)\in o^\perp\) and take unit \(e\in o^\perp\) perpendicular to \(v\), with \(n_k\cdot e>0\) if the third side is tight. The third normal has \(n_k\cdot o\ge r\).

If \(n_k\cdot o>r\), then
\[
\Pr\{D(X)\ge\rho-\varepsilon\}=\frac{8}{3A}\sqrt{\frac{2b}{r}}\,\varepsilon^{3/2}+o(\varepsilon^{3/2}).
\]
If \(n_k\cdot o=r\), then
\[
\Pr\{D(X)\ge\rho-\varepsilon\}=\frac{4}{3A}\sqrt{\frac{2b}{r}}\,\varepsilon^{3/2}+o(\varepsilon^{3/2}).
\]
In either case, conditioned on this event, the pair \(((v\cdot X)/\varepsilon,(e\cdot X)/\sqrt\varepsilon)\) converges to the uniform area law on
\[
Q=\{(u,t)\in\mathbb R^2:|u|+\tfrac{r}{2b}t^2\le1\},
\]
when the third side is slack, or on \(Q\cap\{t\ge0\}\) when it is tight and \(e\) is chosen as specified. The area of \(Q\) is \((8/3)\sqrt{2b/r}\); the half-set has exactly half that area.

**Explicit phase test.** A pair \(i,j\), with complementary index \(k\), determines the two-weight optimum if and only if
\[
G_{ki}+G_{kj}\ge1+G_{ij}.
\]
A strict inequality means a genuinely two-side-contacting largest disk; equality means three geometric contacts but only two positive optimal weights. At most one pair qualifies in any nondegenerate triangle. If no pair qualifies, all weights are positive.

## Proof
1. **Dual extremum and uniqueness.** The nearest point \(z\) to the origin in the Euclidean convex hull of the normals satisfies \((n_i-z)\cdot z\ge0\) for each \(i\). Hence \(n_i\cdot o\ge r\). For any \(x\in S^2\),
\[
\min_i n_i\cdot x\le\sum_i\lambda_i n_i\cdot x=z\cdot x\le r,
\]
with equality attained at \(x=o\). Since \(z\ne0\), equality in the last Cauchy–Schwarz inequality forces \(x=o\). The maximum clearance is therefore \(\rho=\arcsin r\), attained uniquely. Distinct unit normals cannot have a single vertex as their minimal-norm convex combination: projecting onto the segment to any other distinct unit normal initially strictly decreases the norm. The only possibilities are relative interior of the full triangle or of one edge, including equality of an unused constraint.

2. **Contact test.** The nearest point on the edge joining \(n_i,n_j\) is their midpoint \(z=(n_i+n_j)/2\) because both have unit norm. It minimizes distance over the whole three-point convex hull exactly when \((n_k-z)\cdot z\ge0\), or \(G_{ki}+G_{kj}\ge1+G_{ij}\). Equality means all three normal constraints are tight at \(o\), but the third convex weight remains zero. Two different eligible edges would contradict uniqueness of the normal-hull projection, except in degenerate configurations excluded by linear independence.

3. **Three-contact tangent blow-up.** Use geodesic normal coordinates \(x=\exp_o(\varepsilon y)\). Since \(n_i\cdot o=r\) for each active normal,
\[
n_i\cdot x=r+b\varepsilon(w_i\cdot y)+O(\varepsilon^2),\qquad
\sin(\rho-\varepsilon)=r-b\varepsilon+O(\varepsilon^2).
\]
Consequently, the clearance superlevel set, rescaled by \(\varepsilon^{-1}\), tends to \(P\). Positive convex weights satisfy \(\sum_i\lambda_iw_i=0\), with all \(\lambda_i>0\), making \(P\) bounded. This also bounds the rescaled sets uniformly, ensuring dominated convergence. The spherical Jacobian tends to the Euclidean Jacobian, giving area \(\varepsilon^2\operatorname{area}(P)+o(\varepsilon^2)\) and the claimed conditional uniform law. The triangle \(P\) is circumscribed about the Euclidean unit disk, with outward-normal pair angle \(\arccos c_{ij}\) and corresponding interior angle \(\pi-\arccos c_{ij}\); its area (inradius times semiperimeter) is \(\sum_{i<j}\cot((\pi-\arccos c_{ij})/2)=C_3\).

4. **Two-contact parabolic blow-up.** Let \(x=\sqrt{1-s^2-t^2}\,o+s v+t e\), using ordinary coordinates in the tangent plane. The two positive-weight normals are \(n_i=r o+b v\) and \(n_j=r o-b v\). Thus their minimum constraint reads
\[
r\sqrt{1-s^2-t^2}-b|s|\ge\sin(\rho-\varepsilon).
\]
Uniformly on the clearance event, \(s=O(\varepsilon)\), \(t=O(\sqrt\varepsilon)\); after \(s=\varepsilon u\), \(t=\sqrt\varepsilon\,v_0\), the inequality becomes \(|u|+(r/2b)v_0^2\le1+o(1)\). If \(n_k\cdot o>r\), its constraint is inactive throughout this shrinking neighborhood. If \(n_k\cdot o=r\), linear independence implies \(n_k\cdot e\ne0\); although \(n_k\cdot v\) need not vanish, its term is of order \(\varepsilon\) while the \(e\)-term is of order \(\sqrt\varepsilon\); hence its leading constraint is \((n_k\cdot e)v_0\ge0\), cutting \(Q\) in half. The spherical area element is \((1-s^2-t^2)^{-1/2}\,ds\,dt=(1+o(1))\varepsilon^{3/2}du\,dv_0\) on these bounded rescaled regions. Direct integration yields
\[
\operatorname{area}(Q)=\int_{-\sqrt{2b/r}}^{\sqrt{2b/r}}2(1-\tfrac{r}{2b}t^2)\,dt=\tfrac83\sqrt{2b/r}.
\]
Dominated convergence supplies the coefficients and the conditional uniform laws. All conclusions hold for each *fixed* nondegenerate triangle in the stated case.

## Verification
An independent deterministic checker included as `verify.py` computes spherical-triangle areas from the normal Gram matrix, verifies the three contact types on an explicit one-parameter family, and compares exact inner-area integrals against the asymptotic coefficients. For \(n_1=(1,0,0)\), \(n_2=(0,1,0)\), and \(n_3=(a,a,\sqrt{1-2a^2})\), the choices \(a=0.35,0.50,0.60\) realize respectively three positive weights, a critical zero multiplier, and two strict positive weights. In the three-weight case the scaled area coefficients at deficits \(0.015,0.005,0.0015\) are approximately \(6.4316,6.6293,6.7096\), converging to \(6.7462\). For the critical case they are approximately \(2.1406,2.0306,1.9642\), converging to \(1.8856\). For the strict two-weight case they are \(3.7937,3.7788,3.7735\), converging to \(3.7712\). These checks are diagnostic, not a substitute for the analytic proof.

## Relationship to prior work
Lassak's published 2013 article on widths of spherical convex bodies gives the relevant historical spherical supporting-hemisphere/lune framework, but not the probability laws proved here. Bezdek and Lángi's 2022 preprint (2024 journal version), Section 2 and Lemma 1, *already establishes the distinction between a disk touching three sides and a maximal inscribed disk touching only two sides*. That contact distinction itself is **not claimed new**. The elementary two-contact tail also reduces locally to the known sharp spherical-lune clearance behavior. The contribution offered here is the contact-rank-complete endpoint asymptotic for fixed spherical triangles, including the critical zero-multiplier half-law, a computable three-contact coefficient, and all conditional marked blow-up limits. Fillmore and Fillmore's 2014 treatment of spherical triangle geometry supplies background area methods. None of the inspected primary texts states this combined sharp distributional and conditional result.

## Limitations
This theorem is local in the clearance deficit; it does not provide the entire clearance distribution. It assumes a fixed nondegenerate, geodesically convex spherical triangle contained in an open hemisphere, with uniformly sampled area. It does not establish error estimates uniform while the triangle itself approaches contact-rank transition or degeneracy, nor a finite-sample inference guarantee. The proof and source comparisons have not received independent mathematical audit. Related general parallel-set and spherical-cap intersection literature could contain an equivalent formulation not located in the inspected sources.

## References
- M. Lassak, *Width of spherical convex bodies*, Aequationes Mathematicae 89 (2015), first published online 6 December 2013, DOI: https://doi.org/10.1007/s00010-013-0237-3 (primary MSC 52A55).
- K. Bezdek and Z. Lángi, *From the separable Tammes problem to extremal distributions of great circles in the unit sphere*, arXiv:2201.11234, first submitted 26 January 2022; specifically Section 2, Lemma 1 on maximal disks contacting two sides.
- S. Fillmore and J. Fillmore, *Whitney Forms for Spherical Triangles I*, arXiv:1404.6592, first submitted 26 April 2014 (area-geometric context).
