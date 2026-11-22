# Third directional-width moments of signed acyclotopes recover frustrated triangles

## Finding
Let \(G=(V,E)\) be a finite simple graph with \(n=|V|\ge3\). For an edge signing \(\sigma:E\to\{+1,-1\}\), set
\[
Z_\sigma=\sum_{\{i,j\}\in E}\left[-\frac{e_i-\sigma_{ij}e_j}{2},\frac{e_i-\sigma_{ij}e_j}{2}\right]\subset\mathbb R^n.
\]
Its width in direction \(u\) is \(W_\sigma(u)=\sum_{\{i,j\}\in E}|u_i-\sigma_{ij}u_j|\). For \(U\) uniform on the **ambient** unit sphere \(S^{n-1}\), put \(M_j(\sigma)=\mathbb E[W_\sigma(U)^j]\). The unbalanced-triangle count \(b(\sigma)\) is the number of triangles whose three signs multiply to \(-1\). For any two signatures on the same graph,
\[
M_1(\sigma)=M_1(\tau),\qquad M_2(\sigma)=M_2(\tau),\qquad
M_3(\sigma)-M_3(\tau)=\kappa_n\bigl(b(\sigma)-b(\tau)\bigr),
\]
with a strictly positive coefficient
\[
\kappa_n=6\frac{\Gamma(n/2)}{\Gamma((n+3)/2)}\left(F_+-F_-\right),\quad
F_-=\frac{3}{2\sqrt{2\pi}},\quad F_+=\mathbb E[f(Z)^3],
\]
where \(Z\sim N(0,1)\) and
\[
f(z)=\frac{e^{-z^2/2}}{\sqrt\pi}+\frac{z}{\sqrt2}\operatorname{erf}\left(\frac{z}{\sqrt2}\right).
\]
Thus the third moment detects the signed-graph frustration statistic exactly, even though the first two moments are blind to the signs. Numerically \(F_+-F_-\approx0.14915548175434\), while positivity is proved without numerical approximation.

## Assumptions and scope
The graph is simple; isolated vertices are allowed. All generators use the canonical orthonormal coordinate vectors and unit edge weights. Moments are taken over the ambient \(n\)-sphere even if the zonotope has lower affine dimension. Positive links correspond to difference roots and negative links to sum roots, agreeing up to translation with the canonical signed acyclotope convention. The identity compares signings of the **same** graph, not arbitrary graphs with matching numerical invariants.

## Proof
**1. Gaussian radial reduction.** Let \(X=(X_1,\ldots,X_n)\) have independent standard-normal coordinates, and write \(X=RU\), with \(U\) uniform on \(S^{n-1}\), \(R\) independent and \(\mathbb E R^3=2^{3/2}\Gamma((n+3)/2)/\Gamma(n/2)\). Set \(Y_e=|X_i-\sigma_e X_j|/\sqrt2\) for \(e=\{i,j\}\). Then \(W_\sigma(X)=\sqrt2\sum_eY_e\), so
\[
M_3(\sigma)=\frac{2^{3/2}\mathbb E(\sum_eY_e)^3}{\mathbb E R^3}.
\]
The analogous identity holds at orders one and two.

**2. Only signed triangles survive comparison.** Expand the Gaussian moment as a sum over ordered triples of edges with repetitions. For any multiset of at most three edges whose *distinct* edges form a forest, a diagonal coordinate-sign flip removes all edge signs. Since \(X\) is invariant under those flips and \(|Y_e|=Y_e\), the associated moment is independent of \(\sigma\). If a multiset of at most three edges contains a cycle, the graph is simple, so it must comprise exactly the three distinct edges of a triangle. Two signings of a triangle are equivalent under coordinate sign flips if and only if their three sign products agree. As a result, orders one and two are signing-independent, and the entire difference at order three consists of six permutations per triangle.

**3. The two triangle integrals.** Every \(Y_e\) is a standard folded Gaussian. On a triangle with sign product \(+1\), its three normal vectors are (after sign changes) the three pairwise differences. They form a rank-two equiangular configuration, and an orthonormal Gaussian basis in their span gives
\[
(Y_1,Y_2,Y_3)\stackrel d=\bigl(|A|,|-A/2+\sqrt3 B/2|,|-A/2-\sqrt3 B/2|\bigr)
\]
for independent standard-normal \(A,B\). Their product is \(\frac14|(A^3-3AB^2)|\). Writing \((A,B)=T(\cos\theta,\sin\theta)\), the Rayleigh moment \(\mathbb E T^3=3\sqrt{\pi/2}\) and \(\mathbb E|\cos(3\theta)|=2/\pi\) yield \(F_-=3/(2\sqrt{2\pi})\).

For an **unbalanced** triangle (sign product \(-1\)), the three standardized Gaussian projections have pairwise correlation \(+1/2\) after independently reversing the vector orientations. Hence their joint law is that of \(((Z+N_1)/\sqrt2,(Z+N_2)/\sqrt2,(Z+N_3)/\sqrt2)\), with independent standard normals. Conditional independence given \(Z\) gives the absolute-product expectation \(F_+=\mathbb E f(Z)^3\), where the explicitly displayed \(f\) is the mean absolute normal shift.

**4. Strict separation by an analytic bound.** Write \(\mu=\mathbb E f(Z)=\sqrt{2/\pi}\), \(a=\mu-1/\sqrt\pi\), and \(V=\operatorname{Var}(f(Z))=1/6+(\sqrt3-2)/\pi\), using the standard bivariate normal absolute-product identity at correlation \(1/2\). Because \(f(Z)\ge1/\sqrt\pi\), the centered variable \(Q=f(Z)-\mu\) satisfies \(Q\ge-a\), so the pointwise inequality \(Q^3\ge-aQ^2\) proves
\[
F_+\ge\mu^3+(3\mu-a)V>0.6837>F_-=\frac3{2\sqrt{2\pi}}<0.5985.
\]
This proves \(F_+>F_-\) strictly, without trusting a numerical quadrature or a finite experiment.

**5. Assemble the coefficient.** Replacing one balanced triangle by an unbalanced triangle changes the ordered Gaussian cubic sum by \(6(F_+-F_-)\). Radial normalization therefore multiplies the change by \(2^{3/2}/\mathbb E R^3\), giving precisely \(\kappa_n=6\Gamma(n/2)(F_+-F_-)/\Gamma((n+3)/2)\). Additivity over triangles proves the result for arbitrary signings.

## Verification
The companion standalone `CHECKER.py` checks the analytic positive-gap bound, evaluates \(F_+\) by one-dimensional Gaussian quadrature, verifies the balanced-triangle Rayleigh formula numerically, and compares the predicted third-width moment difference against deterministic Sobol Gaussian samples for signed triangles and a triangle-with-leaf graph. These calculations are diagnostics only; steps 1–5 are a proof for all finite simple graphs. The numerical constant is not needed to establish strict positivity.

## Relationship to prior work
Bach, Beck and Rehberg introduce the signed acyclotope and the signed-root incidence matrix, studying Ehrhart polynomials and dual zonotopes. That foundational construction supplies the geometrically natural object here but does not establish angular-width moment identities. The closest identified indexed antecedent, *Third angular-width moments of regular graphical zonotopes recover graph triangles* (2026), concerns **unsigned** graphical zonotopes and comparisons between regular underlying graphs; it does not identify the number of unbalanced triangles from moments of differently signed acyclotopes over one fixed graph. The present result uses genuinely sign-sensitive triangle Gaussian laws and does not assume regularity. The general classification of signed-graph switching is classical, and this paper makes no claim to invent it.

## Limitations
The width is measured in the ambient coordinate space; intrinsically normalized directions in an affine span may behave differently when signing changes its rank. The first three width moments recover only the **number** of unbalanced triangles, not their locations, all cycles, or the full switching class. A graph with no triangles has no signing information in its first three width moments. Historical priority remains provisional because unindexed equivalent metric-moment results cannot be ruled out conclusively.

## References
- E. Bach, M. Beck, S. Rehberg, *Acyclotopes, Tocyclotopes, and Their Ehrhart Polynomials*, arXiv:2409.15227, first public version 23 September 2024. https://arxiv.org/abs/2409.15227
- F. Belardo, S. M. Cioabă, J. H. Koolen, J. Wang, *Open problems in the spectral theory of signed graphs*, arXiv:1907.04349 (2019), background on signed graph balance and switching. https://arxiv.org/abs/1907.04349
- *Third angular-width moments of regular graphical zonotopes recover graph triangles* (2026), relevant published metric-moment antecedent, contrasted by subject and implication in the review.
