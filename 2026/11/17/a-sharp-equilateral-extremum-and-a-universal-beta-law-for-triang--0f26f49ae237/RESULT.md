# A sharp equilateral extremum and a universal beta law for triangle self-containment polytopes

## Finding
Let \(T\subset\mathbb R^2\) be any nondegenerate closed Euclidean triangle, and let \(J(x,y)=(-y,x)\). Its **orientation-preserving similarity self-containment polytope** is
\[
\mathcal C(T)=\{(s,t,b_1,b_2)\in\mathbb R^4:(sI+tJ)T+(b_1,b_2)\subseteq T\}.
\]
Write \(F(T)\subset\mathbb R^2\) for its orthogonal projection onto the \((s,t)\)-coordinate plane, \(A=\operatorname{area}_2(T)>0\), and \(E=\operatorname{conv}\{(1,0),(-1/2,\sqrt3/2),(-1/2,-\sqrt3/2)\}\). Then:

1. **Sharp rotation-scale envelope.** For every \(T\), \(F(T)\subseteq E\), with equality if and only if \(T\) is equilateral.
2. **Exact four-volume identity and sharp extremum.** For every \(T\),
   \[
   \operatorname{vol}_4(\mathcal C(T))=\frac{A}{6}\operatorname{area}_2(F(T))\le\frac{\sqrt3}{8}A.
   \]
   Equality in the inequality holds exactly for equilateral triangles.
3. **Universal gauge law.** Define the Minkowski functional (radial gauge) \(g_T(z)=\inf\{r>0:z\in rF(T)\}\), with \(g_T(0)=0\). If \((S,U,B_1,B_2)\) is uniform in \(\mathcal C(T)\), then \(R=g_T(S,U)\) has density \(12r(1-r)^2\) on \(0<r<1\), equivalently \(R\sim\operatorname{Beta}(2,3)\). Its distribution function is \(6r^2-8r^3+3r^4\) for \(0\le r\le1\).

All volumes refer to ordinary Lebesgue measure in the specified **four real similarity parameters**; reflection-reversing maps are not included. Zero scale is allowed in the closed polytope and has no effect on its volume.

## Assumptions and scope
The source and target are the same nondegenerate triangle, with arbitrary location, orientation, and shape. Its three edges have outward unit normals \(n_1,n_2,n_3\), lengths \(\ell_1,\ell_2,\ell_3>0\), and supporting constants \(h_j=h_T(n_j)\). There are no general-position hypotheses. Define \(\alpha_j=\ell_j/(2A)\); the elementary equilibrium and area relations are
\[
\sum_{j=1}^{3}\alpha_j n_j=0,\qquad \sum_{j=1}^{3}\alpha_jh_j=1.
\]
For \(z=(s,t)\), write \(L_z=sI+tJ\), and set
\[
H_j(z)=h_{L_zT}(n_j),\qquad g(z)=\sum_{j=1}^{3}\alpha_jH_j(z).
\]
The quantity \(g(z)\) is unchanged by translating the source triangle. As the support function is positively homogeneous and convex in \(z\), so is \(g\).

## Proof
**Step 1: three support inequalities and a homothetic translation fiber.** The inclusion \(L_zT+b\subseteq T\) is equivalent to
\[
\langle n_j,b\rangle\le h_j-H_j(z)\quad(j=1,2,3).
\]
For any triple of right-hand sides \(c_j\), the intersection of the three corresponding halfplanes, if nonempty and bounded, is a translated homothetic copy of \(T\). Indeed, the linear map \(b\mapsto(\langle n_1,b\rangle,\langle n_2,b\rangle,\langle n_3,b\rangle)\) has image the codimension-one subspace defined by \(\sum_j\alpha_jc_j=0\), because \(\sum_j\alpha_jn_j=0\) and the normals span the plane. Thus the unique scalar homothety ratio is \(k=\sum_j\alpha_jc_j=1-g(z)\). For \(k\ge0\), choose a translation matching the remaining two-dimensional part of the right-hand sides; the intersection is a translate of \(kT\), of area \(Ak^2\). For \(k<0\), summing the three inequalities with positive \(\alpha_j\) gives a contradiction. Hence
\[
F(T)=\{z:g(z)\le1\},\qquad \operatorname{area}_2\{b:L_zT+b\subseteq T\}=A(1-g(z))^2\quad(z\in F(T)).
\]
The equality is valid on the boundary, where the fiber has zero area. The gauge \(g\) is strictly positive for \(z\ne0\): by the planar Minkowski mixed-area inequality,
\[
Ag(z)=V(T,L_zT)\ge\sqrt{\operatorname{area}(T)\operatorname{area}(L_zT)}=A\sqrt{s^2+t^2}.
\]
Here \(V(T,K)=\tfrac12\sum_j\ell_jh_K(n_j)\) is mixed area, so the displayed identity follows directly from the definition. Consequently \(F(T)\) is a bounded convex neighborhood of zero and \(g\) is its Minkowski functional.

**Step 2: an equilateral universal envelope.** Let \(v_1,v_2,v_3\) be the vertices of \(T\). For every feasible \(L_zT+b\subseteq T\), express its three image vertices barycentrically relative to \(T\). These coefficients form a \(3\times3\) nonnegative column-stochastic matrix \(B\). Under the affine barycentric identification, the linear map induced by \(B\) on the two-dimensional sum-zero subspace is conjugate to \(L_z\). Therefore the three eigenvalues of \(B\) (with algebraic multiplicity) are \(1,s+it,s-it\). Nonnegative diagonal entries imply
\[
\operatorname{tr}B=1+2s\ge0,\quad\text{so }s\ge-\tfrac12.
\]
Moreover nonnegativity and Cauchy–Schwarz yield
\[
\operatorname{tr}(B^2)=\sum_{i,j}B_{ij}B_{ji}\ge\sum_i B_{ii}^{2}\ge\frac{(\operatorname{tr}B)^2}{3}.
\]
Substituting the eigenvalues gives \((1-s)^2\ge3t^2\). Since area inclusion also gives \(s^2+t^2\le1\), in particular \(s\le1\), we conclude \(|t|\le(1-s)/\sqrt3\). Together these are precisely the three supporting inequalities of \(E\), proving \(F(T)\subseteq E\).

If \(T\) is equilateral, rotation of \(T\) by either \(2\pi/3\) or \(4\pi/3\) about its center preserves \(T\). These two complex multipliers, together with \(1\), are the three vertices of \(E\). The set \(F(T)\) is convex, hence equals \(E\). Conversely, if \(F(T)=E\), the multiplier \((-1/2,\sqrt3/2)\) is feasible. Its absolute scale is one, so its image has the same area as \(T\); inclusion of equal-area triangles forces equality. Consequently \(T\) is invariant under a \(120^\circ\) planar rotation and must be equilateral.

**Step 3: exact four-volume and beta law.** Because \(g\) is the gauge of \(F(T)\), the area of \(\{z:g(z)\le r\}\) equals \(r^2\operatorname{area}(F(T))\) for \(0\le r\le1\). Fubini's theorem and the translation-fiber formula give
\[
\begin{aligned}
\operatorname{vol}_4\mathcal C(T)
&=A\int_{F(T)}(1-g(z))^2\,dz\\
&=2A\operatorname{area}(F(T))\int_0^1r(1-r)^2\,dr\\
&=\frac{A\operatorname{area}(F(T))}{6}.
\end{aligned}
\]
Since the equilateral triangle \(E\) has area \(3\sqrt3/4\), the sharp normalized bound is \(\sqrt3/8\). Equality of planar areas for convex bodies under inclusion \(F(T)\subseteq E\) forces equality of these bodies, which by Step 2 forces \(T\) equilateral.

For a uniform point of \(\mathcal C(T)\), the probability density of the projected multiplier \(z\) is proportional to \((1-g(z))^2\). Differentiating the sublevel-area formula and normalizing by \(\operatorname{vol}_4\mathcal C(T)\) gives the density \(12r(1-r)^2\) for \(g(z)\). Direct integration yields the asserted distribution function and \(\operatorname{Beta}(2,3)\) law.

## Verification
The standalone `verify.py` independently builds the nine vertex-to-halfplane inequalities for the four-dimensional containment polytope and evaluates its volume using a four-dimensional convex hull. It separately computes the planar projection and the support-gauge fiber integral, and checks the equilateral upper bound, using five fixed and 120 seeded random nondegenerate triangles. It also verifies several beta moments by numerical quadrature. The actual script passed 382 deterministic assertions; these finite and floating-point checks are supplementary, not a substitute for the preceding proof.

## Relationship to prior work
The four-parameter similarity containment polytope, its projected footprint, and its relation to largest placements are explicitly developed by Choi and Choi (2026), following Agarwal–Amenta–Sharir (1998) and Chan–Hair (2024). These sources address algorithmic complexity, silhouettes, or optimal placements; they do not give the self-triangle four-dimensional volume identity, its sharp extremizing shape, or the universal gauge distribution. The stochastic-matrix eigenvalue framework is classical (Dmitriev–Dynkin and Karpelevič); the proof's trace inequalities are elementary and are not claimed as new spectral theory. The contribution is the combined sharp geometric volume/extremum/distribution theorem for the specific self-containment configuration.

## Limitations
Only orientation-preserving planar similarities are included; the parameter measure is the ordinary Lebesgue measure in the specified coordinates. No claim is made for distinct source and target polygons or for dimension greater than two. The normalized volume is invariant under Euclidean similarities of the ambient triangle, not arbitrary coordinate rescalings of the four transformation parameters. Historical priority against all unindexed literature is not established, particularly for older similarity-containment computations; the older 1998 source was compared using its accessible description rather than its complete text. No independent external mathematical audit has been performed.

## References
- Y. Choi and S. Choi, *The Containment Polytope of a Triangle and a Convex Polygon*, arXiv:2611.08556v1 (first public 2026-11-05), https://arxiv.org/html/2611.08556v1.
- T. M. Chan and E. Hair, *Convex Polygon Containment: Improving Quadratic to Near Linear Time*, SoCG 2024, DOI:10.4230/LIPIcs.SoCG.2024.34, https://doi.org/10.4230/LIPIcs.SoCG.2024.34.
- P. K. Agarwal, N. Amenta and M. Sharir, *Largest Placement of One Convex Polygon Inside Another*, Discrete & Computational Geometry 19 (1998), DOI:10.1007/PL00009337, https://doi.org/10.1007/PL00009337.
- C. R. Johnson and P. Paparella, *A matricial view of the Karpelevič Theorem*, arXiv:1611.06970 (2016), https://arxiv.org/abs/1611.06970.
